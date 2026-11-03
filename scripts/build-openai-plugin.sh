#!/usr/bin/env bash
# Build dist/openai/purplegrain-<version>.zip, the ChatGPT plugin package
# uploaded at platform.openai.com/plugins. The archive root holds plugin.json,
# mcp.json, assets/ and skills/<skill>/ (OpenAI's portable plugin layout), taken
# from openai/ and purplegrain/skills/. dist/ is gitignored.
#
# OPENAI_EXCLUDED_SKILLS, if ever set, are left out of the ChatGPT package only;
# the Claude Code plugin still ships them. Record skills cross-reference each
# other, so excluding one leaves references to it behind.
set -euo pipefail

OPENAI_EXCLUDED_SKILLS=()

root="$(cd "$(dirname "$0")/.." && pwd)"
version="$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["version"])' "$root/openai/plugin.json")"
out="$root/dist/openai"
stage="$(mktemp -d)"
trap 'rm -rf "$stage"' EXIT

cp "$root/openai/plugin.json" "$root/openai/mcp.json" "$stage/"
cp -R "$root/openai/assets" "$stage/assets"
mkdir -p "$stage/skills"
for skill in "$root"/purplegrain/skills/*/; do
  name="$(basename "$skill")"
  if [[ ${#OPENAI_EXCLUDED_SKILLS[@]} -gt 0 && " ${OPENAI_EXCLUDED_SKILLS[*]} " == *" $name "* ]]; then
    echo "skipped $name (not in the ChatGPT package)"
    continue
  fi
  cp -R "$skill" "$stage/skills/$name"
done

# The package must name only skills and assets it carries.
python3 - "$stage" <<'PY'
import json, os, re, sys
stage = sys.argv[1]
manifest = json.load(open(os.path.join(stage, "plugin.json")))
openai = manifest["extensions"]["com.openai"]
for key in ("composerIcon", "logo"):
    path = openai["interface"][key]
    assert os.path.isfile(os.path.join(stage, path)), f"{key} {path} is missing"
onboarding = openai.get("onboardingSkill")
if onboarding:
    assert os.path.isfile(os.path.join(stage, onboarding)), f"onboardingSkill {onboarding} is missing"
names = set()
for skill in sorted(os.listdir(os.path.join(stage, "skills"))):
    text = open(os.path.join(stage, "skills", skill, "SKILL.md")).read()
    front = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.S)
    assert front and front.group(2).strip(), f"{skill}: frontmatter and a body are required"
    fields = dict(re.findall(r"^(name|description):\s*(.+)$", front.group(1), re.M))
    name, description = fields.get("name", "").strip('"'), fields.get("description", "").strip('"')
    assert name and description, f"{skill}: name and description are required"
    assert len(description) <= 1024, f"{skill}: description over 1024 characters"
    assert len(f"{manifest['name']}:{name}") <= 64, f"{skill}: plugin:skill name over 64 characters"
    assert name not in names, f"{skill}: duplicate name {name}"
    names.add(name)
cases = openai["review"]["test_cases"]
assert len(cases["positive"]) == 5 and len(cases["negative"]) == 3, "5 positive and 3 negative test cases"
print(f"checked {len(names)} skills, 5 + 3 test cases")
PY

mkdir -p "$out"
rm -f "$out/purplegrain-$version.zip"
(cd "$stage" && zip -qr "$out/purplegrain-$version.zip" . -x '*.DS_Store')
echo "built dist/openai/purplegrain-$version.zip"
