---
name: li-welfare-sheep-mulesing
description: "Line item for PurpleGrain record skills. Do not use directly. Sheep mulesing age, pain relief, and the wool-declaration code the farmer states. Tasmania is stricter. Sheep-standards adoption in other states was not verified."
---

# Sheep mulesing

Version 1.0.0. Do not call a PurpleGrain write. Do not own `procedures`. The husbandry orchestrator sends `mules`. Pain-relief batch, expiry and withholding belong to `li-product-batch-expiry` and `li-withholding-meat-esi`. This item checks the age and whether a pain-relief product is on the record.

Do not apply these ages to cattle or goats. Cattle welfare is not this skill. Goat ages were not verified.

## Applies when

A husbandry record whose procedures include `mules`, on sheep. If the species is not sheep, stop and say this item does not apply.

## Collect

| Fact | Where it goes |
|---|---|
| Age or age range | `record_notes` |
| Pain relief product, when one was used | a `products` line. You do not write the line; tell the orchestrator |
| Only wool-bearing skin was removed, when they say so | `record_notes` |
| NWD code they are actually claiming | `record_notes`. Do not assign one |

## The standard

National sheep standards, January 2016 text. Standards are the mandatory tier where a state has adopted them. Which states have adopted the sheep standards was not verified (fetch of that page failed in the sheep work, and it was still open on 23 Oct 2026). Do not tell a farmer the national standard is an offence in their state unless you are in Tasmania, which has its own regulation.

- S7.2: not under 24 hours old and not over 12 months.
- S7.3: pain relief is mandatory from 6 to 12 months.
- S7.4: not sheep that are diseased, weak or ill-thrift.
- S7.5: only wool-bearing skin.
- Guidelines, not bans: where done, at 2–12 weeks (G7.6). Pain relief where practical at other ages (G7.8).

Tasmania, Animal Welfare (Sheep) Regulations 2023: no mulesing under 14 days or over 6 months, and pain relief at every mulesing. Last checked 19 Oct 2026, E. This is stricter than the national standard. Use it for a Tasmanian property. Do not apply the Tasmanian ages to tail docking. That is the other sheep welfare item.

Liquid nitrogen is not mulesing. Do not record it as `mules`. The husbandry skill can note it. The NWD code for liquid nitrogen is `LN`.

## NWD code, only when they state it

AWEX NWD version 10.0, effective 1 July 2024. Last checked 19 Oct 2026, E.

| Code | Meaning |
|---|---|
| `NM` | Not mulesed and not treated with liquid nitrogen |
| `LN` | Liquid nitrogen. Not mulesing |
| `AA` | Mulesed with an APVMA-registered analgesic or anaesthetic. Replaced `PR` in July 2024 |
| `M` | Mulesed without that product |
| `ND` | Not declared |

Mulesing with a registered pain-relief product is `AA` only when they are claiming that. Mulesing without one is `M` only when they say there was none. Never assign a code. `CM` is a property answer, not a mob code. Mixed mobs take the lowest of `NM`, then `LN`, then `AA`, then `M`. `li-nwd-status` is not in this release. At shearing, do not ask again if this note already has the code.

## Checks

Severity: `legal`, with the adoption limit above.

- Age or method outside the national standard, or outside the Tasmanian rule on a Tasmanian property: show the rule and the last-checked date, and ask before saving. Do not rewrite what they say happened. They may save after they have seen it.
- Pain relief missing for a stated age of 6–12 months (national), or for any mulesing in Tasmania: flag it.
- Ill-thrift stated: flag S7.4.

## Confirm fragment

`Mules. Age stated: {age}. Pain relief: {product or not recorded}. NWD: {code or not stated}.`

## Sources

Sheep standards PDF: <https://animalwelfarestandards.net.au/wp-content/uploads/2023/08/Sheep-Standards-and-Guidelines-for-Endorsed-Jan-2016-061017.pdf> (19 Oct 2026, E).

Tasmania: <https://www.legislation.tas.gov.au/view/pdf/asmade/sr-2023-054> (19 Oct 2026, E).

AWEX NWD: <https://www.awex.com.au/standards/national-wool-declaration-nwd> (19 Oct 2026, E).
