---
name: li-state-chem-record-rules
description: "Line item for PurpleGrain record skills. Do not use directly. Which spray-record deadline, retention and extra fields apply in the property's state, including NT and the ACT. Tasmania's retention period is unconfirmed."
---

# State chemical-use records

Version 1.0.0. Do not call a PurpleGrain write. This item picks the row. It does not re-ask for batch, rate, weather, buffers or the operator. Those have their own line items. It asks only for the leftover facts in the last table, and it tells `li-record-retention` which state period to compare.

Ask the state once per property. `pg-onboarding` collects it for parcel search. API #239 and #240 do not add a `state` column, so do not send `state` on the property. If you were not told the state in this conversation, ask. Do not infer a state from a town name.

## Applies when

A spray. Also a sowing seed treatment or a stored-grain treatment, with the limits below.

Seed treatment as a state chemical-use record: the duty in each state was not verified (paddock research, 23 Oct 2026). Do not tell the farmer that a seed treatment without a spray diary is an offence in their state. Do collect the product, rate, date, place and user, because LPA-03 treats grazing a crop sown with treated seed as a paddock treatment (checked with the LPA-03 fields, 19 Oct 2026).

Stored grain: the Northern Territory requires a record (23 Oct 2026, V). Do not claim the same sentence for every other state. The general spray row still applies when the state row covers the use.

Household hand application is outside several of these duties. A farm boom, a paddock spot spray or an aerial job is not that exemption.

## The row

Use the property's state. A label or permit period is additional. If it is sooner or longer, follow it as well. Aerial 2,4-D permit PER87451, as read for the spray reference, wants a written record within 24 hours kept two years. That permit is not every 2,4-D label. Read the label they used.

| State | Make the record | Keep it | Who can require it | Status |
|---|---|---|---|---|
| VIC | 48 hours | 2 years from use | Agriculture Victoria authorised officer | E, 19 Oct 2026 |
| NSW | As soon as practicable and no later than 48 hours. NSW DPI's "24 hours" is guidance, not this deadline. Same day is best practice only | 3 years | EPA | E, 19 Oct 2026. Regulation text matched EPA and Service NSW. The legislation.nsw.gov.au page was not re-rendered in that check |
| QLD | 2 days, or 3 days for a prescribed agricultural ERA product used for relevant cattle grazing or sugarcane | 2 years, or 6 years if it contains tebuthiuron. For that ERA use in a reef catchment, give a copy to the responsible person within 5 days. That copy is not a rule for every Queensland spray | Inspector under the Chemical Usage Act | E, 19 Oct 2026 |
| WA | 7 days | 2 years from use | DPIRD inspector | E, 19 Oct 2026 |
| SA | Group 4 herbicides in prescribed businesses and areas: accurate records. A general farm spray is not, on the pages read, a universal statutory duty. PIRSA's 24 hours is best practice | Group 4: 2 years. General: PIRSA says two years as best practice | PIRSA for the Group 4 rules | E, 19 Oct 2026 |
| TAS | A record is required for commercial and agricultural operators. No deadline was stated in the code | Not stated. Do not invent one | NRE Tasmania / Registrar of Chemical Products | E, 19 Oct 2026. Retention unconfirmed |
| NT | As soon as practicable. Contract sprayers give it to the licensee as soon as practicable | 2 years after use | NT chemicals adviser or inspector | V, 23 Oct 2026 |
| ACT | 48 hours. Strict liability | 2 years | EPA / Access Canberra | V, 23 Oct 2026 |

South Australia: do not tell a farmer that a non-Group-4 boom spray without a diary is a breach of a general SA record statute.

Queensland products named in the spray reference: ametryn, atrazine, diuron, hexazinone, tebuthiuron. The 3-day timing (Chemical Usage Regulation s 33B, spray reference, 19 Oct 2026) applies when one of those products is used for relevant cattle grazing or relevant sugarcane. The copy to the responsible person within 5 days (s 33E) applies when that use is in a Great Barrier Reef catchment. Do not apply the 3-day timing to an ordinary paddock spray. Do not decide from a town that the property is in a reef catchment. Ask.

## Fields the state row adds

Owned elsewhere, so only name them when they are missing:

| Fact | Owner |
|---|---|
| Rate | `li-spray-rate-tank-mix` |
| Wind and other weather | `li-spray-weather` |
| Who applied it, and the credential | `li-operator-credential` |
| Batch and expiry | `li-product-batch-expiry` |
| Grazing and harvest intervals | `li-grazing-harvest-whp` |
| Keep-until date | `li-record-retention` |

No line item owns these yet. Ask them and put the answers in `record_notes`. `li-application-time`, `li-target-crop-pest` and `li-apvma-product-id` are not in this release. When they ship, they take these questions over.

| Fact | Ask when |
|---|---|
| Crop or situation, and target weed, pest or disease | NSW, Queensland, Victoria, NT, ACT, and a Freshcare property. Also WA (crop or situation) |
| Start and finish time | NT, ACT, WA (date and time), NSW licensed applicators, and a Freshcare record. If a weather reading is stored, the start can be that reading's `read_at`. Finish has no weather field |
| APVMA registration number | NT, and whenever the product name is ambiguous. Also Queensland, which accepts the trade name or the APVMA number |
| Applicator address | NSW. Victoria wants name and contact, which `li-operator-credential` already asks |
| Supervisor, and the person the spray was for | Victoria, when there is one. Queensland wants user, owner and supervisor contacts |
| Total quantity, if rate and area do not already show it | Victoria and NSW |
| Aerial: pilot, aircraft type and registration | NT, when the method is aerial |

Freshcare Food Safety & Quality, Edition 5 (2026), element 11.13, asks for start and finish, target, batch, wind, withholding and the applicator (spray reference, 19 Oct 2026). Its retention period was not read. Do not add a Freshcare year-count. Apply the element only when they say they are in the scheme.

## Checks

Severity: `legal`.

- Name the deadline and the keeper from the row, with the last-checked date, before they save a completed spray that is already close to the deadline.
- Missing mandatory leftover fields: list them. Do not block the save on an unverified cell (Tasmania retention, SA general duty, seed-treatment duty).
- `li-record-deadline-reminder` is not in this release. Do not create a second reminder task unless they ask for one.

## Confirm fragment

`{STATE} record: within {deadline}, keep {period}` plus any leftover gap. For Tasmania, `keep: not confirmed`. For SA non-Group-4, `statutory record duty not confirmed; LPA fields still asked`.

## Sources

Victoria: <https://agriculture.vic.gov.au/farm-management/chemicals/keeping-records-of-chemical-use/agricultural-chemical-use-records>

NSW: <https://www.epa.nsw.gov.au/Your-environment/Pesticides/compulsory-record-keeping> and Pesticides Regulation 2017 cl 36(3), as cited in the spray reference. Service NSW: <https://www.service.nsw.gov.au/transaction/keep-a-record-of-pesticide-use>

Queensland: <https://www.business.qld.gov.au/industries/farms-fishing-forestry/agriculture/sustainable/chemical/use/record>

WA: <https://www.dpird.wa.gov.au/businesses/biosecurity/agricultural-standards/chemical-spray-regulations/record-keeping-farm-pesticide-application/>

SA: <https://pir.sa.gov.au/crops-and-plants/rural-chemicals/comply_with_legislation> and <https://pir.sa.gov.au/biosecurity/rural_chemicals/chemical_use_best_practice>

Tasmania: <https://nre.tas.gov.au/agriculture/agvet-chemicals/codes-of-practice/code-of-practice-for-ground-spraying>

NT: <https://nt.gov.au/industry/agriculture/farm-management/using-chemicals-responsibly/keeping-records-of-chemical-use>

ACT: Environment Protection Regulation 2005 s 55B, <https://www.legislation.act.gov.au/sl/2005-38/> (paddock research, 23 Oct 2026, V).

The VIC, NSW, QLD, WA, SA and TAS rows were checked for the spray reference on 19 Oct 2026 (E). NT and ACT were checked in the paddock research on 23 Oct 2026 (V).
