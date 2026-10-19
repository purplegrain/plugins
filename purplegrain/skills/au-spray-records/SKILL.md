---
name: au-spray-records
description: Check and save Australian paddock spray records before writing them to PurpleGrain or copying them as a chemical-use row. Use for a herbicide, fungicide, insecticide, adjuvant or other agricultural chemical applied to a paddock or crop, including boom, spot, aerial, drone, knapsack and weed-wiper work. Covers grazing and harvest withholding, export intervals, weather, buffer zones, tank mixes and the state spray-record rules.
---

# Australian paddock spray records

Use this whenever a farmer asks to record, import or correct a spray on a paddock, whether typed, spoken, or from a photo of a spray diary. A spray is a herbicide, fungicide, insecticide or adjuvant on a paddock. A drench, lice treatment, jet or dip on sheep is a mob treatment, not this record. Fertiliser is not a spray.

Never save first and check later. Always: collect -> check -> confirm with the farmer -> save -> read back.

This is a completeness check. It is not agronomy or legal advice. The label on the pack, the APVMA permit if there is one, and the state rule are the authority. Source detail, retention and who inspects are in `references/spray-requirements.md`. Read that file when a state, drift, permit, export or accreditation point needs a source, or when a figure might have changed.

## 1. Collect

One spray is one paddock. A tank mix is several products on that one record, up to 10. Three paddocks means three records. A block is not a record: if they sprayed every paddock in a block, make one record per paddock.

Pull out what they already said and ask only for what is missing. An unknown value stays unset and prints "not recorded". Never invent a batch, expiry, rate, water rate, withholding period, wind, temperature or area.

### Fields the spray record holds

| Field | Where it goes |
|---|---|
| Date | `date` as `YYYY-MM-DD`. A job already done is not in the future |
| Paddock | An existing paddock, resolved before the write |
| Area | `area_ha`. May be less than the paddock. Omitting it stores the whole paddock area, so a spot spray must send the smaller area or you must ask |
| Product trade name | One `products` entry each |
| Role | `herbicide`, `fungicide`, `insecticide` or `adjuvant` when clear |
| Active | `active`, when stated |
| Batch and expiry | `batch`, `expiry` as `YYYY-MM-DD` |
| Rate | `rate` verbatim, such as `3 L/ha` or `300 mL/ha`. A number with no unit is refused. `rate_value`, `rate_unit` (`g`, `kg`, `t`, `mL`, `L`, `seeds`, `%`) and `rate_basis` (`ha`, `head`, `100_kg_seed`, `100_l`, `total`) may be sent; the server can parse them from `rate` |
| Grazing WHP | `grazing_whp_days`, whole days, from the label |
| Harvest WHP | `harvest_whp_days`. If the label gives one interval for both, send it in both and say so |
| Export slaughter, grazing and feed intervals | `esi_days`, `egi_days`, `eafi_days` only when the label or a stated export interval gives that one. Do not copy the grazing WHP into all three |
| Do not graze | `do_not_graze: true` only when the label says DO NOT graze. That stores no end date |
| Method | `boom`, `boomless`, `aerial`, `drone`, `spot`, `weed_wiper`, `knapsack`, `airblast`. Ask if the word is ambiguous |
| Water rate | `water_rate` in L/ha, such as `80` or `80 L/ha`. Anything else is stored as none |
| Nozzle, pressure, boom height, speed | `nozzle`, `pressure_kpa`, `boom_height_m`, `speed_kmh` |
| Droplet size | `droplet_category`: `extremely_fine`, `very_fine`, `fine`, `medium`, `coarse`, `very_coarse`, `extremely_coarse`, `ultra_coarse` |
| Downwind no-spray zone kept | `no_spray_zone_m` |
| Re-entry | `re_entry_note`, the label interval in the farmer's words |
| Neighbour drift | `neighbour_drift` only when they say drift from a neighbour was a factor |
| Weather | One `weather_readings` object per observation: `read_at`, `wind_kmh`, `gust_kmh`, `wind_dir`, `temp_c`, `rh_pct`, `delta_t`, `cloud_pct`, `rain_mm`, `inversion_observed`, `source`. A reading nobody took stays off the list |
| Title | `description`, for example "Boom spray canola, North" |

`product_id` from `listProducts` with `kind=herbicide` is optional. On that catalogue, `grazing_whp_days` is the grazing period and `harvest_whp_days` is the harvest period. Do not read the stored `whp_days` and `esi_days` columns as meat and export. The catalogue is a hint. Confirm the label. It is not the APVMA permit list.

### Facts with no spray field

Put these in `record_notes` after the record exists, and the applicator's name in `updateTask` `operator` when it is not the signed-in user.

- Applicator phone and address, supervisor, and the person the spray was done for
- Chemical-user credential actually held: Victorian ACUP, NSW AQF qualification, Queensland ACDC licence, or the certificate number. A ChemCert card is training, not those permits
- APVMA permit number for an off-label use, and the permit expiry if they have it
- APVMA product or label number
- Crop or situation, target weed, pest or disease, and why it was sprayed
- Start and finish time of the application
- Total product used, if the rate and area do not already show it
- Neighbour notification, rinsate disposal, a spray-drift incident, and equipment calibration

## 2. Check before saving

Report every check as a short list. Do not silently fix anything.

**Missing fields.** Name each gap. Batch, expiry, rate unit, grazing and harvest intervals, wind and applicator are the ones most often missing. A label or permit that demands a written record (many 2,4-D labels, and permit conditions) adds that record's own fields and its own deadline, often 24 hours and two years. Follow the label the farmer has.

**Dates.** Grazing end = spray date + `grazing_whp_days`. Harvest end = spray date + `harvest_whp_days`. Do the same for `egi_days` and `eafi_days` when those were given, and label them export grazing and export animal-feed, not domestic. A one-day difference against a diary is a convention: say which day you are using. A larger gap is a likely error. Spray date after expiry: flag. A future date is a plan: stop if they said the spray was done. `do_not_graze` has no end date. Say so.

**Numbers.** Area above the paddock area: flag. Rate with no unit: ask, do not send it. Water rate that is not litres per hectare: ask, because the server will drop it. Do not judge whether a rate is legal unless the farmer has given the label rate or a permit rate. If they have, and the stated rate is above it, flag it.

**Weather and drift.** Record only measurements they give. Queensland wants a reading before, during and after: if they are in Queensland and gave one reading, say the other two are missing. A label wind window (often 3–20 km/h, sometimes 3–15) or a "do not spray in a hazardous inversion" restraint is checked against what they measured. Outside the window, or inversion not checked when the label forbids it: flag. Delta T outside 2–8 is a Victorian ground-spraying risk guide, not a number on every label. No-spray zone shorter than the label buffer they quoted: flag. Do not invent a buffer.

**Restricted products.** High-volatile 2,4-D esters (ethyl, butyl, isobutyl) were cancelled. If they name one, flag it and do not treat it as a current use. Ester 2,4-D, atrazine and Schedule 7 products need the state credential (in Victoria, an ACUP). Paraquat and diquat labels changed after the APVMA decision of June 2026, with a two-year phase-out of older stock. Follow the label on the pack they used. Do not substitute a remembered rate.

**Livestock and fodder.** If stock will graze the paddock or eat hay, grain or silage from it, the grazing WHP, and any EGI or EAFI, have to be on the record before the mob is turned in or the feed is sold. A bought-in fodder without a commodity vendor declaration is a 60-day withhold from the last feed under LPA, which is a feeding fact, not a spray date.

**Duplicates.** Resolve the paddock first. `listTasks` with `asset_id` of the paddock and `filter_status: ["completed"]`, and follow pagination. Read `spray.products`. Same day and same product is probably a duplicate: ask.

**Unclear input.** A value you could not read or hear is UNCLEAR and must be confirmed. Never guess a product name, batch or rate.

## 3. Confirm with the farmer

Show one compact summary and wait for a yes. Show it again if anything changes.

```
Spray - North, canola (72 ha of 80), 19/10/26, boom, by JS
- Atrazine 500 SC 3 L/ha, batch 123456, exp 08/27
  grazing WHP 15 weeks -> graze 02/02/27
  harvest WHP not stated
Water 100 L/ha. Wind SW 12 km/h at 14:00, 18 C, delta T 4. Inversion not checked.
Checks: applicator phone missing; harvest WHP missing
Save this record?
```

Use the farmer's real figures. The lines above only show the shape.

## 4. Save

Find the property and the paddock first. `fetchCurrentUser` is the signed-in user. `listBusinessMembers` with that user's id and `include: "organization"` lists accepted memberships. `listProperties` without `organization_id` is personal properties only; pass the business `organization_id` for its properties. `listPaddocks` with `property_id` lists that property's paddocks. `getPropertyPicture` shows the paddocks and mobs. Never substitute an account or guess an id. Creating a missing paddock needs its own confirmation.

`createSprayRecord`: `paddock_id`, `confirm: true` only after the farmer's yes, and `body.data.type: "spray-record"`. Fields sit in `body.data.attributes`. A completed spray needs at least one product row.

The server sets `operation_type: spray`, `capture_source: agent` and `producer`. Do not send `broadcast`, `share_scope`, `operation_type: ai` or `rerun_ai`. Do not fall back to `createTask` to get around a refusal. A 403 with `code: insufficient_access` is a real refusal: show its `detail` and stop.

`updateSprayRecord` uses `spray.id` on the saved task, not the task id. `products` replaces the whole set. `weather_readings` replaces the whole list. Send the full list back.

`record_notes`, tags and `operator` are a later `updateTask` on the task, with `confirm: true`. Notes do not set grazing or harvest dates.

If a write fails or times out, read that paddock's completed spray records before retrying, and do not create a second record when the first one is already there. If the first attempt sent an `Idempotency-Key`, send that same key on any retry.

Without PurpleGrain, produce the same summary as a row the farmer can copy onto a state spray record or the LPA crop, pasture and paddock treatment record.

## 5. Read back

`getPaddock` `withholding`, or `getPropertyStatus`, is the paddock's grazing and harvest status. It is derived from completed sprays and from a sowing's seed treatments. Fertiliser does not change it. A `do_not_graze` product does not either. Export grazing and export animal-feed intervals are on the product lines; they are not that withholding object. Do not tell the farmer the paddock is clear from the new record alone.

`getTreatmentRegister` with `kind: "spray"` and the paddock's `paddock_ids` is the chemical-use register. Tell them what was saved, the grazing and harvest dates, and any check still open (credential, permit, missing weather, a mob that must stay off the paddock). One or two sentences for the save; the open checks as a short list.
