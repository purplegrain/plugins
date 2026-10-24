---
name: li-eid-tagging
description: "Line item for PurpleGrain record skills. Do not use directly. Whether sheep or goats need an electronic NLIS tag before they leave the property, by birth date and by state. Western Australia's all-ages date was not verified."
---

# Sheep and goat eID

Version 1.0.0. Do not call a PurpleGrain write. Do not claim this record updated the NLIS database. `procedures: ["eid_tag"]` means the mob was tagged. The husbandry orchestrator sends that procedure. This item does not own `procedures`.

`moveMob` is an on-property paddock move. It is not an NLIS transfer.

## Applies when

An `eid_tag` husbandry record, or any off-property movement of sheep or goats. Cattle are different: NLIS electronic identification for cattle is mandatory nationally (livestock research, 23 Oct 2026). Do not apply the sheep dates below to cattle. The time allowed for a cattle receiver to update NLIS was not verified. Do not say 48 hours for cattle.

## Dates

| Who | Rule | Last checked | Status |
|---|---|---|---|
| Sheep and farmed goats born on or after 1 January 2025 | An approved electronic tag before they leave the property of birth. A visual tag is not enough for those animals | 23 Oct 2026 | V, national. Also in the sheep reference, 19 Oct 2026 |
| Victoria, all ages | Electronic tag before they leave a Victorian property, since 1 January 2022 | 19 Oct 2026 | E |
| NSW, Queensland, South Australia, Tasmania, all ages | 1 January 2027, before they leave a property | 23 Oct 2026 | V, state pages. The research note did not copy the page URLs |
| Western Australia, all ages | A 1 July 2026 date appeared in a search summary only | 23 Oct 2026 | U. Do not state it |
| Harvested rangeland goats | A device-free pathway was stated for NSW | 23 Oct 2026 | V for NSW. Do not generalise to other states or to farmed goats |

The April 2023 DAFF implementation table left some jurisdictions undecided. That table is not the current position for NSW, Queensland, South Australia or Tasmania.

## Collect

| Fact | Where it goes |
|---|---|
| Breeder tag or pink post-breeder tag | `record_notes` |
| Year colour, and the PIC printed on the tag | `record_notes` |
| Birth year or cohort, so the 1 January 2025 line can be applied | `record_notes`. Do not send `birth_year` on `createMob`. That attribute is not in the onboarding contract |

Tags bought for one PIC are not used on another (Victoria, sheep reference, 19 Oct 2026, E). Do not claim that sentence for every state.

## Checks

Severity: `legal`.

- A movement off the property of animals born on or after 1 January 2025 with no eID stated: flag it.
- Victoria: any age leaving the property without an electronic tag stated: flag it.
- NSW, Queensland, South Australia, Tasmania, on or after 1 January 2027: any age leaving without an electronic tag stated: flag it. Before that date, the birth-date rule still applies.
- Western Australia: apply the national birth-date rule only. Say the all-ages date was not verified.
- Visual-tag sheep described as moving after the all-ages date in a verified state: flag it.
- This flag does not block a paddock move inside the property.

## Confirm fragment

`eID: {breeder or post-breeder, or not recorded}. Birth cohort: {year or not recorded}.`

## Sources

ISC, what sheep and goat eID is: <https://www.integritysystems.com.au/identification--traceability/national-livestock-identification-system/Sheep-and-Goat-eID/What-is-Sheep-and-Goat-eID/> (sheep reference, 19 Oct 2026, E).

DAFF implementation plan: <https://www.agriculture.gov.au/biosecurity-trade/policy/partnerships/nbc/sheep-and-goat-traceability-task-force/implementation-plan> (19 Oct 2026, E).

Victoria: <https://agriculture.vic.gov.au/livestock-and-animals/national-livestock-identification-system/livestock-identification> (19 Oct 2026, E).

The 1 January 2027 all-ages dates for NSW, Queensland, South Australia and Tasmania were marked verified against state pages on 23 Oct 2026. URLs for those four pages were not in the research note. Do not invent them.
