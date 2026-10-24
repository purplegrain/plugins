---
name: au-spray-records
description: "Check and save an Australian paddock spray record before writing it to PurpleGrain or copying it as a chemical-use row. Use for a herbicide, fungicide, insecticide, adjuvant or other agricultural chemical applied to a paddock or crop, including boom, spot, aerial, drone, knapsack and weed-wiper work. Seed treatment at sowing belongs to au-paddock-sowing-records. Fertiliser belongs to au-paddock-fertiliser-records."
---

# Australian paddock spray records

Version 1.1.0. The published name stays `au-spray-records`. A second skill under another name would make the same spray match twice.

Follow `pg-core`. If the paddock does not exist, offer `pg-onboarding`. Do not block a read.

This is a record. It is not agronomy or legal advice. The label, the APVMA permit and the state rule are the authority. If this folder is installed, `references/spray-requirements.md` (checked 19 Oct 2026; NT and ACT added 24 Oct 2026 from the paddock research) is the long note. The line items are the rules to apply.

Never save first and check later.

## 1. Scope

One spray is one paddock. A tank mix is several products on that record, up to 10. Three paddocks means three records. A block is not a record.

A drench, jet or dip on a mob is `au-mob-treatment-records` or, when it is part of crutching or shearing, `au-mob-husbandry-records`. Fertiliser is not a spray. Treated seed is a sowing.

## 2. Line items

| Line item | Applies when | What it owns |
|---|---|---|
| `li-state-chem-record-rules` | State known, or ask once | Deadline, retention, leftover fields (crop, target, time, APVMA number). Tasmanian retention is unconfirmed. SA general duty is not confirmed |
| `li-spray-rate-tank-mix` | Every spray | One line each, rate with a unit, role |
| `li-grazing-harvest-whp` | Every product | `grazing_whp_days`, `harvest_whp_days`, `do_not_graze` |
| `li-spray-weather` | Outdoors | `weather_readings` |
| `li-buffer-drift` | Outdoors, or a buffer or neighbour was mentioned | `no_spray_zone_m`, `droplet_category`, `neighbour_drift` |
| `li-operator-credential` | Every spray. Licence when the product or state needs one | `operator`, credential in notes |
| `li-product-batch-expiry` | Every product | `batch`, `expiry` |
| `li-record-retention` | After the save | Keep-until, the longest period |

Not in this release: `li-export-intervals`, `li-apvma-permit`, `li-restricted-chemicals`, `li-application-time`, `li-target-crop-pest`, `li-equipment-calibration`. Use the short forms in this skill until they exist. Say the full check is not installed.

## 3. Fields this skill still asks

| Field | Where it goes |
|---|---|
| Date | `date`. A job already done is not in the future |
| Paddock | Resolve it first |
| Area | `area_ha`. Omitting it stores the whole paddock. A spot spray must send the smaller area or you must ask |
| Water rate | `water_rate` in L/ha. Anything else is stored as none |
| Nozzle, pressure, boom height, speed | `nozzle`, `pressure_kpa`, `boom_height_m`, `speed_kmh`. Calibration date has no field: notes |
| Method | `boom`, `boomless`, `aerial`, `drone`, `spot`, `weed_wiper`, `knapsack`, `airblast` |
| Re-entry | `re_entry_note`, in their words |
| Title | `description` |
| ESI, EGI, EAFI | `esi_days`, `egi_days`, `eafi_days` only when the label states that one. Do not copy the grazing WHP into all three. Australian MRLs are not an importing country's MRL. Grain Trade Australia tables were not verified (23 Oct 2026, U). Do not quote a market limit from memory |
| APVMA permit number and expiry | `record_notes`, only when they are using a permit. Do not invent one |
| Rinsate, a drift incident | `record_notes` |

`product_id` from `listProducts?kind=herbicide` is optional. On that catalogue, `grazing_whp_days` is the grazing period and `harvest_whp_days` is the harvest period. Confirm the label.

## 4. Restricted products, until that line item ships

These are the checks already verified in the spray reference. Flag them. Do not block a record of a spray that has already happened. Do not quote a rate limit that was not on the label in front of them.

- High-volatile 2,4-D esters (ethyl, butyl, isobutyl) were cancelled. Do not record one as a current registered use (APVMA 2,4-D review, spray reference, 19 Oct 2026, E).
- Ester 2,4-D, atrazine and Schedule 7 products: `li-operator-credential` for the state permit. In Victoria that is an ACUP.
- Paraquat and diquat: an APVMA decision, reported as 23 June 2026, changed conditions for stock manufactured after the decision, with a two-year phase-out of older stock described in industry reporting. The grams-per-hectare figures were not copied, because they came from secondary reports (spray reference, 19 Oct 2026). Follow the label on the pack they used.
- 1080, PAPP and phosphine licence details were not verified (paddock research, 23 Oct 2026, U). If they name one, ask for the authority they hold and do not state a rule you cannot cite.

## 5. Check and confirm

Run the line items. Area above the paddock: flag. Duplicate: same day and same product on that paddock.

Bought-in fodder is `au-mob-feeding-records`. The 60-day figure is a feeding fact, not a spray date.

```
Spray - North, canola (72 ha of 80), 19/10/26, boom, by JS
- Atrazine 500 SC 3 L/ha, batch 123456, exp 08/27
  grazing WHP 15 weeks -> graze 02/02/27
  harvest WHP not stated
Water 100 L/ha. Wind SW 12 km/h at 14:00, 18 C, delta T 4. Inversion not checked.
Checks: applicator phone missing; harvest WHP missing
Save this record?
```

Wait for a yes.

## 6. Save and read back

`createSprayRecord`: `paddock_id`, `confirm: true`, `body.data.type: "spray-record"`. A completed spray needs at least one product. The server sets `operation_type: spray`, `capture_source: agent` and `producer`. Send confirmed `operator`, `record_notes` and `tags` in `body.data.attributes` with the spray; an omitted or blank operator defaults to the signed-in user's display name. This tool accepts `Idempotency-Key`.

`updateSprayRecord` uses `spray.id`, not the task id. `products` and `weather_readings` each replace the whole set.

Notes and operator follow `pg-core`. If the write fails, read that paddock's sprays before retrying, and reuse the `Idempotency-Key` when the first attempt sent one.

`getPaddock.withholding` or `getPropertyStatus` is grazing and harvest status, from completed sprays and from a sowing's seed treatments. Fertiliser does not change it. `do_not_graze` does not give a date. Export intervals are not that object.

`getTreatmentRegister` `kind: "spray"` with `paddock_ids` is the chemical-use register. Tell them what was saved, the dates, and any check still open.

Without PurpleGrain, the same summary is a row for a state spray record or the LPA paddock treatment record.
