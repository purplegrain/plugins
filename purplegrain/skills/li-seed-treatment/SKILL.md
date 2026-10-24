---
name: li-seed-treatment
description: "Line item for PurpleGrain record skills. Do not use directly. The seed-treatment product on a sowing: name, active and rate per 100 kg of seed. Grazing withholding is a different line item. State record duty for treated seed was not verified."
---

# Seed treatment

Version 1.0.0. Do not call a PurpleGrain write. The sowing orchestrator saves. A completed sowing needs a seed line (`role: seed`). That line is the orchestrator's. This item applies only when the seed was treated.

## Owns, and does not own

| Fact | Owner |
|---|---|
| Treatment name, active, rate per 100 kg of seed | This item |
| Batch and expiry | `li-product-batch-expiry` |
| Grazing WHP | `li-grazing-harvest-whp` (`sowing.products[role=seed_treatment].grazing_whp_days`). It sets the paddock's grazing status |
| ESI | Not owned here. `li-export-intervals` is not in this release. Ask for the label ESI and give it to the orchestrator as `esi_days`. Do not copy the grazing WHP into `esi_days` unless the label has no separate ESI and you have said so |
| Who treated the seed, and where | `record_notes` |
| Leftover treated seed | `record_notes` |

## Collect

| Fact | Where it goes |
|---|---|
| Product and active | `name`, `active`, on the line with `role: seed_treatment` |
| Rate | `rate` in their words, such as `400 mL / 100 kg seed`. `rate_basis: 100_kg_seed` when that is what they said. A number with no unit is refused |

Never invent a rate, an active or an interval.

## Checks

Severity: `lpa`. LPA-03 is the verified reason to record a seed treatment that stock may graze (19 Oct 2026, E). Whether each state treats seed treatment as a spray-record offence was not verified (23 Oct 2026, U). Do not state that offence. `li-state-chem-record-rules` says the same.

- Grazing WHP missing on treated seed: flag it, because that number becomes the paddock status. The grazing item owns the field.
- Treated seed is not grain for sale or feed. Receiver rules and the exact legal wording were not verified against each receiver on 23 Oct 2026 (S/U). Warn, and ask what they did with leftovers. Do not block the sowing. Do not invent a delivery rejection code.
- `li-treated-grain-segregation` is not in this release.

## Confirm fragment

`Seed treatment {name} {rate}. Grazing WHP {from the grazing item}.`

## Sources

LPA-03 template fields, via the spray reference, 19 Oct 2026, E. <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/lpa-records-templates/lpa-03-crop-pasture-and-paddock-treatment-record-form.pdf>

PurpleGrain sowing schema, 24 Oct 2026: a seed treatment carries `grazing_whp_days` and `esi_days`, and the grazing interval sets paddock status.

State chemical-use duty for seed treatment: unverified, paddock research 23 Oct 2026.
