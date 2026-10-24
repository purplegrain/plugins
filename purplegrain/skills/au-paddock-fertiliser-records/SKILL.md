---
name: au-paddock-fertiliser-records
description: "Check and save an Australian paddock fertiliser record before writing it to PurpleGrain. Use for urea, MAP, super, lime, gypsum, manure or other fertiliser spread, banded, drilled or fertigated. Fertiliser has no withholding period. A spray is au-spray-records."
---

# Australian paddock fertiliser records

Version 1.0.0. Follow `pg-core`. If the paddock does not exist, offer `pg-onboarding`. Do not block a read.

Fertiliser has no withholding period and never changes a paddock's status. `getPaddock` and `getPropertyStatus` ignore it. Do not tell the farmer the paddock is held back because of a fertiliser. An `advisory_note` is advice to pass on, not a status.

This is a record. It is not fertiliser advice.

## 1. Fields

| Fact | Where it goes |
|---|---|
| Date, area | `date`, `area_ha` (defaults to the paddock) |
| Product | `products[].name` |
| Analysis, when they know it | `analysis`, for example `{ "N": 46 }`. Do not invent a percentage. Nutrients per hectare are calculated when the record is read |
| Rate, with a unit | `rate` such as `100 kg/ha`. `rate_unit` is `g`, `kg`, `t`, `mL` or `L`. `rate_basis` is `ha` or `total`. A number with no unit is refused |
| How | `method`: `broadcast`, `banded`, `drilled`, `in_furrow`, `fertigation`, `foliar` |
| Incorporation | `incorporation`: `none`, `mechanical`, `rain`, `irrigation`. `incorporated_at` when they know when |
| Batch, supplier | `batch`, `supplier`. There is no expiry field. Do not send one |
| Spreader, bout, cost | `spreader`, `bout_width_m`, `cost_per_ha`. Optional |
| Label stock warning, in the label's words or theirs | `advisory_note` |

No line item owns the fertiliser rate. This skill does. `li-spray-rate-tank-mix` is sprays only.

## 2. Line items

| Line item | Applies when |
|---|---|
| `li-product-batch-expiry` | Batch, when they have it. No expiry on this record |
| `li-operator-credential` | Who spread it. A Fertcare number only if they mention a contractor or a quality scheme. It is industry, not established here as law |
| `li-record-retention` | After the save. Reef cane records have a 6-year line in that skill |

Not in this release: `li-fertiliser-stock-warnings`, `li-reef-nutrient-qld`, `li-fertiliser-heavy-metals`. Use the short forms below and say so.

## 3. Warnings that are not a withholding

Molybdenum and selenium, Victorian fertiliser guide as cited in the paddock research (23 Oct 2026, V): molybdenum above 10 mg/kg means keep stock off for about four weeks, and selenium products are toxic if over-applied. Put the label warning in `advisory_note`. Do not invent a withhold if you have not seen the label. Do not write a grazing WHP. There is no field for one.

Cadmium, Victorian fertiliser regulations as cited in that research (r9, V): at or under 300 mg cadmium per kg of phosphorus where phosphorus is at least 2 percent; trace-element products at or under 50 mg/kg; other products at or under 10 mg/kg. The label must state cadmium above 1 mg/kg and carry a warning. Other states mirroring those numbers was not verified (U). A mercury figure in the strategy notes was not in the paddock research. Do not state one. This is a labelling rule. Flag a high-cadmium phosphate only when the label states the figure and the paddock is going into potatoes, leafy vegetables or peanuts. Supplier "low cadmium" targets are not the legal limit. Do not block the save. `li-fertiliser-heavy-metals` will own the full check later.

Biosolids and poultry-litter stock withholds were not verified (U). If they are spreading those, say the withhold is unconfirmed and ask what the label or their state guideline says. Do not invent a 30-day figure. Litter that might be fed to cattle, sheep or goats is a restricted-animal-material question for `au-mob-feeding-records`.

## 4. Queensland reef

Ask this section when the property is in Queensland, or when the state is not stored. A property already stored in another state does not get these questions.

Do not decide the catchment from a town. Ask whether the property is in a Great Barrier Reef catchment. The strategy note names the Wet Tropics, Burdekin, Mackay Whitsunday, Fitzroy and Burnett Mary. Those names are for the farmer to recognise. They are not a boundary for the agent to draw.

Cane, from the paddock research (23 Oct 2026, V, the sugarcane ERA standard): a nitrogen and phosphorus budget, no ground-based broadcast of nitrogen fertiliser, and records within 3 business days kept 6 years. If they say they are in the catchment and growing cane, ask for the rate, the N and P percentage, and the method. If the method they state is ground broadcast of a nitrogen fertiliser, show that rule and ask before saving. They may still record what was done.

Grazing ERA record detail was not verified (U). Do not invent the grazing record fields.

Grains and horticulture had no agricultural ERA standard at that reading. A new or expanded commercial cropping above 5 hectares was described as needing an environmental authority. Ask whether they already hold it if they say the cropping is new or expanded in a reef catchment. Do not tell them they are in breach.

## 5. Confirm, save, read back

```
Fertiliser - North (80 ha), 02/06/26, broadcast, by JS
- Urea 100 kg/ha, analysis N 46, batch not recorded
Checks: reef catchment not asked
Save this record?
```

`createFertiliserRecord`: `paddock_id`, `confirm: true`, `body.data.type: "fertiliser-record"`. A completed record needs a product row. The server sets `operation_type: fertiliser` and `capture_source: agent`. Send confirmed `operator`, `record_notes` and `tags` in `body.data.attributes` with the record; an omitted or blank operator defaults to the signed-in user's display name. This tool accepts `Idempotency-Key`. Notes follow `pg-core`.

Read the task back. Do not read a withholding date off it. There is none. `getTreatmentRegister` `kind: "paddock-inputs"` is where the row prints. Fertiliser is not in the spray register and not in the NVD view.
