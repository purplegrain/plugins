---
name: li-grazing-harvest-whp
description: "Line item for PurpleGrain record skills. Do not use directly. Grazing and harvest withholding periods, a do-not-graze label, and the safe dates, for a spray or a sowing seed treatment."
---

# Grazing and harvest withholding

Version 1.0.0. Do not call a PurpleGrain write. Meat WHP and ESI on a mob treatment belong to `li-withholding-meat-esi`. Export grazing interval (EGI) and export animal-feed interval (EAFI) are not owned here. `li-export-intervals` is not in this release. The orchestrator asks for those only when the label states them, and does not copy the grazing WHP into them.

## Applies when

A spray product, or a sowing product with `role: seed_treatment`. Fertiliser has no withholding and never changes a paddock's status. Do not put a fertiliser stock-off warning in these fields. That warning is an `advisory_note` on the fertiliser, owned by the fertiliser skill until `li-fertiliser-stock-warnings` ships.

## Collect

| Fact | Where it goes |
|---|---|
| Grazing WHP, whole days, from the label | `grazing_whp_days` on a spray product, or on a seed-treatment line |
| Harvest WHP, whole days, from the label | `harvest_whp_days` on a spray product. A seed-treatment line has no harvest field |
| Label says DO NOT graze | `do_not_graze: true` on a spray product only |

If the label gives one interval for both grazing and harvest, send it in both and say so. `do_not_graze` stores no end date. The paddock gets no status from it. Say that.

A seed treatment's grazing interval sets the paddock's grazing status the same way a spray does. That is PurpleGrain's rule, reviewed on the `createSowingRecord` schema on 24 Oct 2026.

Never invent an interval. On the herbicide catalogue, read `grazing_whp_days` and `harvest_whp_days` by those names. Do not read the catalogue's `whp_days` and `esi_days` as meat and export. The catalogue is a hint. The label wins. Never store a shorter period than that label.

## Checks

Severity: `legal`.

- Grazing end = spray or sowing date + `grazing_whp_days`. Harvest end = date + `harvest_whp_days`. Say which day you are using.
- Use date after the product expiry is `li-product-batch-expiry`, not this item.
- Field work: the server returns `warnings` when a harvest is before a harvest withholding ends, or hay or silage is cut before a grazing withholding ends. A warning does not block the write. The orchestrator reads it and tells the farmer. Do not tell them the grain meets a market MRL.
- After the save, paddock status is `getPaddock.withholding` or `getPropertyStatus`. Do not declare the paddock clear from the new row alone. Export intervals are not that withholding object.

## Confirm fragment

`grazing WHP {n} d -> {date}; harvest WHP {n} d -> {date}`. If `do_not_graze`, say there is no graze date.

## Sources

| Source | Last checked | Status |
|---|---|---|
| APVMA residues overview (label WHP; Australian MRLs assume label use) | 19 Oct 2026 | E, spray reference |
| LPA crop, pasture and paddock treatment template (WHP and safe date) | 19 Oct 2026 | E |
| PurpleGrain sowing schema: seed-treatment grazing WHP sets paddock status | 24 Oct 2026 | V, connector schema |

<https://www.apvma.gov.au/chemicals-and-products/pesticides-and-veterinary-residues>

<https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/lpa-records-templates/lpa-03-crop-pasture-and-paddock-treatment-record-form.pdf>
