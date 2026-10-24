---
name: li-adverse-reaction
description: "Line item for PurpleGrain record skills. Do not use directly. Whether a mob treatment caused an adverse reaction or left a broken needle, and that it is passed on at sale."
---

# Adverse reaction and broken needle

Version 1.0.0. Do not call a PurpleGrain write. Husbandry has no `adverse_reaction` field. On a husbandry record the same fact goes to `record_notes`. Do not ask this on a spray.

## Applies when

A mob treatment. Ask once, with the other LPA gaps, not before the legal intervals.

## Collect

| Fact | Where it goes |
|---|---|
| What happened, or that nothing did | `adverse_reaction` |
| Which animal still has a needle | `record_notes`. A mob record does not identify one animal |

If they say there was none, store `None` so an auditor can see it was asked. If you have not asked and they are saving with gaps, leave it unset. Unset prints `not recorded`, which is not the same as none.

LPA expects the reaction to be passed on at sale. Remind them. Do not write that into an NVD yourself.

## Checks

Severity: `lpa`.

- A broken needle with no note of which animal: flag it.
- Do not diagnose the reaction.

## Confirm fragment

`Reaction: {text}` when you asked.

## Sources

| Source | Last checked | Status |
|---|---|---|
| LPA treatment template and 2025 audit checklist: adverse reactions, broken needle, passed on at sale | 19 Oct 2026 | E |

<https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-audits-checklist-2025.pdf>
