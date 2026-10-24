---
name: li-spray-rate-tank-mix
description: "Line item for PurpleGrain record skills. Do not use directly. One spray product line each, with a rate that has a unit. The longest withholding is calculated by the grazing line item, not this one."
---

# Spray rate and tank mix

Version 1.0.0. Do not call a PurpleGrain write. Do not ask for batch, weather or withholding days. A sowing rate and a fertiliser rate are not this item. Seed-treatment rate belongs to `li-seed-treatment`.

## Applies when

Every spray. One paddock, one record. A tank mix is several product lines on that record, up to 10. Three paddocks are three records. A block is not a record.

## Collect

| Fact | Where it goes |
|---|---|
| Trade name | `products[].name`. The orchestrator asks the name. This item checks the line exists |
| Role, when it is clear | `herbicide`, `fungicide`, `insecticide` or `adjuvant` |
| Rate, in their words, with a unit | `rate`, such as `3 L/ha` or `300 mL/ha` |
| Parsed rate, when clear | `rate_value`, `rate_unit` (`g`, `kg`, `t`, `mL`, `L`, `seeds`, `%`), `rate_basis` (`ha`, `head`, `100_kg_seed`, `100_l`, `total`) |

The server can parse `rate_value`, `rate_unit` and `rate_basis` from `rate`. A number with no unit is refused. Ask for the unit. Do not send `100` on its own.

An adjuvant is its own line when it was in the tank. Do not fold it into the herbicide's name.

Water rate is `water_rate` in L/ha and is not owned here. The spray orchestrator asks for it. Anything that is not litres per hectare is stored as none.

Do not invent a mixing order. No verified legal field requires one. If they mention it, the orchestrator can put it in `record_notes`.

## Checks

Severity: `legal`. State spray records require a rate or enough to calculate it (see `li-state-chem-record-rules`). LPA-03 also asks for the rate and the tank mix.

- Each product they named has its own line and its own rate.
- Rate above a label or permit rate they have actually given you: flag it. Do not judge a rate against a label you have not seen.
- The longest grazing or harvest interval in the tank is what holds the paddock. `li-grazing-harvest-whp` calculates it. Do not copy one product's interval onto another.

## Confirm fragment

One line per product: `{name} {rate}`.

## Sources

| Source | Last checked | Status |
|---|---|---|
| LPA-03: rate, method, tank mix, product | 19 Oct 2026 | E |
| State record rules require a rate or enough to calculate it (Victoria, NSW, Queensland, WA) | 19 Oct 2026 | E, spray reference |
| PurpleGrain spray schema: a rate with no unit is refused | 24 Oct 2026 | V, connector schema |

<https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/lpa-records-templates/lpa-03-crop-pasture-and-paddock-treatment-record-form.pdf>
