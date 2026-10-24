#!/usr/bin/env python3
"""Structural checks for PurpleGrain skills. No network.

Fails when a line item is missing its prefix, two line items claim one
API field, the catalogue drifts from the skill folders, or a skill names
a platform path.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "purplegrain" / "skills"
INDEX = SKILLS / "index.json"
CATALOGUE = ROOT / "purplegrain" / "CATALOGUE.md"

LINE_ITEM_PREFIX = "Line item for PurpleGrain record skills. Do not use directly."
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
KINDS = {"core", "onboarding", "line-item", "orchestrator", "output"}
SEVERITIES = {"legal", "lpa", "best-practice"}
BANNED_PATHS = (".cursor/", "/workspace", "~/")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def frontmatter(text: str, path: Path, errors: list[str]) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(errors, f"{path}: missing frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        fail(errors, f"{path}: unclosed frontmatter")
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        fail(errors, f"{path}: {exc}")
        return {}


def field_conflict(a: str, b: str) -> bool:
    if a == b:
        return True
    if a.endswith("[]") and b.startswith(a[:-2] + "[]."):
        return True
    if b.endswith("[]") and a.startswith(b[:-2] + "[]."):
        return True
    return False


def main() -> int:
    errors: list[str] = []
    folders = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not folders:
        fail(errors, "no skill folders")

    claimed: dict[str, str] = {}
    names: dict[str, dict] = {}

    for folder in folders:
        skill_md = folder / "SKILL.md"
        if not skill_md.is_file():
            fail(errors, f"{folder.name}: no SKILL.md")
            continue
        text = skill_md.read_text()
        meta = frontmatter(text, skill_md, errors)
        name = meta.get("name", "")
        description = meta.get("description", "")
        if name != folder.name:
            fail(errors, f"{folder.name}: frontmatter name is {name!r}")
        if not NAME_RE.match(folder.name):
            fail(errors, f"{folder.name}: name is not lowercase-hyphenated")
        if not description:
            fail(errors, f"{folder.name}: empty description")
        elif len(description) > 1024:
            fail(errors, f"{folder.name}: description is {len(description)} characters")

        for banned in BANNED_PATHS:
            if banned in text:
                fail(errors, f"{folder.name}: contains {banned}")

        lineitem = folder / "lineitem.json"
        skill_json = folder / "skill.json"
        if lineitem.is_file() and skill_json.is_file():
            fail(errors, f"{folder.name}: has both lineitem.json and skill.json")
        if folder.name.startswith("li-"):
            if not description.startswith(LINE_ITEM_PREFIX):
                fail(errors, f"{folder.name}: description must start with the line-item prefix")
            if not lineitem.is_file():
                fail(errors, f"{folder.name}: missing lineitem.json")
                continue
            payload = load_json(lineitem, errors)
            if payload.get("name") != folder.name:
                fail(errors, f"{folder.name}: lineitem.json name mismatch")
            if not VERSION_RE.match(str(payload.get("version", ""))):
                fail(errors, f"{folder.name}: lineitem.json version is not semver")
            if payload.get("severity") not in SEVERITIES:
                fail(errors, f"{folder.name}: bad severity")
            requires = payload.get("requires") or []
            if not any(str(item).startswith("pg-core") for item in requires):
                fail(errors, f"{folder.name}: line item must require pg-core")
            for field in payload.get("fields") or []:
                for prior, owner in claimed.items():
                    if field_conflict(prior, field):
                        fail(errors, f"field {field} claimed by {owner} and {folder.name}")
                claimed[field] = folder.name
            names[folder.name] = {
                "version": payload.get("version"),
                "kind": "line-item",
            }
        else:
            if description.startswith(LINE_ITEM_PREFIX):
                fail(errors, f"{folder.name}: orchestrator uses the line-item prefix")
            if not skill_json.is_file():
                fail(errors, f"{folder.name}: missing skill.json")
                continue
            payload = load_json(skill_json, errors)
            if payload.get("name") != folder.name:
                fail(errors, f"{folder.name}: skill.json name mismatch")
            if not VERSION_RE.match(str(payload.get("version", ""))):
                fail(errors, f"{folder.name}: skill.json version is not semver")
            kind = payload.get("kind")
            if kind not in KINDS or kind == "line-item":
                fail(errors, f"{folder.name}: kind {kind!r} is not valid for skill.json")
            if "pg-core" not in text:
                fail(errors, f"{folder.name}: does not mention pg-core")
            if "confirm" not in text:
                fail(errors, f"{folder.name}: does not mention confirm")
            if kind in {"orchestrator", "output"}:
                for item in payload.get("line_items") or []:
                    if item not in text:
                        fail(errors, f"{folder.name}: SKILL.md does not name {item}")
                for item in payload.get("line_items_not_shipped") or []:
                    if item not in text:
                        fail(errors, f"{folder.name}: SKILL.md does not name deferred {item}")
                    if (SKILLS / item).is_dir():
                        fail(errors, f"{folder.name}: {item} is listed as not shipped but the folder exists")
            names[folder.name] = {"version": payload.get("version"), "kind": kind}

    onboarding = SKILLS / "pg-onboarding" / "SKILL.md"
    if onboarding.is_file():
        body = onboarding.read_text()
        for token in (
            "pg-onboarding@1",
            "completed_steps",
            "next_step",
            "create_team",
            "create_property",
            "map_paddocks",
            "create_blocks",
            "add_mobs",
            "first_record",
        ):
            if token not in body:
                fail(errors, f"pg-onboarding: missing {token}")

    for folder_name, payload in names.items():
        if payload["kind"] in {"orchestrator", "output"}:
            skill_json = load_json(SKILLS / folder_name / "skill.json", errors)
            for item in skill_json.get("line_items") or []:
                if item not in names or names[item]["kind"] != "line-item":
                    fail(errors, f"{folder_name}: line item {item} is not installed")

    if not INDEX.is_file():
        fail(errors, "purplegrain/skills/index.json is missing")
    else:
        index = load_json(INDEX, errors)
        listed = index.get("skills") or []
        listed_names = [item.get("name") for item in listed]
        if sorted(listed_names) != sorted(names):
            missing = sorted(set(names) - set(listed_names))
            extra = sorted(set(listed_names) - set(names))
            fail(errors, f"index.json names differ. missing={missing} extra={extra}")
        for item in listed:
            name = item.get("name")
            if name not in names:
                continue
            if item.get("version") != names[name]["version"]:
                fail(errors, f"index.json version for {name} does not match the skill file")
            if item.get("kind") != names[name]["kind"]:
                fail(errors, f"index.json kind for {name} does not match the skill file")
            path = ROOT / item.get("path", "")
            if not path.is_file():
                fail(errors, f"index.json path for {name} does not exist")

    if not CATALOGUE.is_file():
        fail(errors, "purplegrain/CATALOGUE.md is missing")
    else:
        catalogue = CATALOGUE.read_text()
        for name in names:
            if f"`{name}`" not in catalogue:
                fail(errors, f"CATALOGUE.md does not mention `{name}`")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"\n{len(errors)} skill check(s) failed", file=sys.stderr)
        return 1
    print(f"skill checks passed ({len(names)} skills, {len(claimed)} owned fields)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
