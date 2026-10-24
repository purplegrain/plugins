---
name: au-paddock-sowing-records
description: "Check and save an Australian paddock sowing record before writing it to PurpleGrain. Use when a crop is sown or seeded, including the seed lot, a seed treatment, fertiliser with the seed, or an inoculant. A spray after the crop is up belongs to au-spray-records."
---

# Australian paddock sowing records

Version 1.0.0. Follow `pg-core`. If the paddock does not exist, offer `pg-onboarding`. Do not block a read.

This is a record. It is not agronomy advice. The seed label and the technology agreement, when there is one, are the farmer's authority. Completing a sowing sets the paddock's `current_crop` to the seed line's `variety`, otherwise to `crop`. Read that back with `getPaddock`.

A completed sowing with no seed line is refused.

## 1. Fields

| Fact | Where it goes |
|---|---|
| Date, area, crop | `date`, `area_ha` (defaults to the paddock), `crop` such as `Barley` |
| Seed line, required | `products` entry `role: seed`. `variety`, `seed_source` (`retained`, `purchased`, `shared`), `seed_lot`, `germination_pct`, `tgw_g`, `rate` |
| Fertiliser with the seed, if used | `role: fertiliser`, `placement` `with_seed` or `banded`, `analysis`, `rate`. This line does not set a withholding |
| Inoculant, if used | `role: inoculant`, `inoculant_group`, `batch`, `expiry`. No withholding |
| Seed treatment, if the seed was treated | `li-seed-treatment` |
| Machinery, optional | `seeder`, `opener`, `depth_mm`, `row_spacing_mm`, `soil_moisture`, `speed_kmh`, `stubble`, `target_plants_m2` |

A rate needs a unit. `80 kg/ha` is valid. `80` is refused. Do not invent a variety, a lot, a germination or an analysis.

`li-plant-back-check` is not in this release. If they are sowing into a paddock that was sprayed, offer to read that paddock's spray history and compare it with a plant-back they read off the label. Do not invent the interval.

## 2. Line items

| Line item | Applies when |
|---|---|
| `li-seed-treatment` | The seed was treated |
| `li-product-batch-expiry` | Seed treatment, inoculant, or any line with a batch |
| `li-grazing-harvest-whp` | A seed treatment. Its grazing WHP becomes the paddock status |
| `li-state-chem-record-rules` | A seed treatment. The state offence is unverified. Still collect the LPA facts. Do not call it a breach |
| `li-operator-credential` | Someone treated the seed, or a contractor sowed |
| `li-record-retention` | After the save |

Not in this release: `li-treated-grain-segregation`, `li-plant-back-check`, `li-gm-crop-stewardship`, `li-export-intervals`.

ESI on the seed treatment: ask when the label states one, store `esi_days`, and do not copy the grazing WHP across unless you have said the label has no separate ESI. EGI is notes, if they state it. There is no EGI field on a sowing product.

GM varieties: stewardship specifics and a Tasmanian moratorium end date were not verified (paddock research, 23 Oct 2026, U). Ask whether the variety is GM. If it is, ask what their technology user agreement requires them to keep, and put that in `record_notes`. Do not state a delivery code, and do not state a moratorium year.

## 3. Confirm, save, read back

```
Sowing - North, barley (80 ha), 12/05/26
- Seed Spartacus CL, purchased, lot as stated, 80 kg/ha
- Seed treatment as stated, grazing WHP as stated
Checks: germination not recorded
Save this record?
```

`createSowingRecord`: `paddock_id`, `confirm: true`, `body.data.type: "sowing-record"`. The server sets `operation_type: sow`, `capture_source: agent` and `producer`. Notes follow `pg-core`. If the write fails, read the paddock's records before retrying. This tool accepts `Idempotency-Key`.

Read `getPaddock` for `current_crop` and `withholding`. Fertiliser and inoculant lines do not change withholding. The seed treatment's grazing interval does.

`getTreatmentRegister` `kind: "paddock-inputs"` includes the sowing. A seed treatment that sets a grazing date is also visible on the paddock withholding, not as a spray row.
