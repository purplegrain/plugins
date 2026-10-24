---
name: li-welfare-sheep-dock-castrate
description: "Line item for PurpleGrain record skills. Do not use directly. Sheep tail docking and castration: pain relief over six months, and at least one tail joint left. State adoption of the sheep standards was not verified."
---

# Sheep tail docking and castration

Version 1.0.0. Do not call a PurpleGrain write. Do not own `procedures` or `method`. The husbandry orchestrator sends `tail_dock` and `castrate`, and the method (rings, hot knife, knife, cryptorchid).

Do not apply the Tasmanian mulesing ages to docking or castration. Do not apply these sheep ages to cattle or goats.

## Applies when

A sheep husbandry record with `tail_dock` or `castrate`.

## Collect

| Fact | Where it goes |
|---|---|
| Age | `record_notes` |
| Pain relief product, when used | a product line, written by the orchestrator |
| At least one palpable tail joint left, and that the ewe dock covers the vulva | `record_notes` |
| Haemorrhage control, when they say what they did | `record_notes` |

## The standard

National sheep standards, January 2016 text, last checked 19 Oct 2026, E. Adoption by state was not verified. Flag the standard. Do not call it an offence in a named state.

- S6.2 and S6.4: over 6 months, pain relief and haemorrhage control are mandatory, including cryptorchid.
- S6.3: at least one palpable free joint left on the tail.
- Guidelines, not bans: after 24 hours and before 12 weeks (G6.2, G6.3). Pain relief where practical (G6.14). Hot knife or rubber rings preferred (G6.17). Dock long enough to cover the vulva in females, and a similar length in males (G6.20). Lambs to be slaughtered before 12 weeks, or before puberty, should not be castrated (G6.22).

## Checks

Severity: `legal`, with the adoption limit above.

- Stated age over 6 months and no pain relief: show S6.2 / S6.4 and ask before saving. They may save what was done.
- Tail dock with the joint not confirmed: name that gap. Do not invent "one joint left".
- A guideline they did not follow: mention it as a guideline, not as a ban.

## Confirm fragment

`Tail dock ({method}). Castrate ({method}). Age: {age}. Joint left: {stated or not confirmed}.`

## Sources

Sheep standards PDF: <https://animalwelfarestandards.net.au/wp-content/uploads/2023/08/Sheep-Standards-and-Guidelines-for-Endorsed-Jan-2016-061017.pdf> (19 Oct 2026, E).
