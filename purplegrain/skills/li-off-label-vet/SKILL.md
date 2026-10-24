---
name: li-off-label-vet
description: "Line item for PurpleGrain record skills. Do not use directly. Vet's written authority, and the vet's withholding period, for off-label use, a Schedule 4 product or an antibiotic on a mob."
---

# Off-label use and the vet

Version 1.0.0. Do not call a PurpleGrain write. Do not authorise an off-label use. That decision is the vet's. This item records the authority they already have.

## Applies when

The farmer says the use was off-label, the product is Schedule 4, or the category is `antibiotic`. On-label use: leave `vet_authorisation` unset. Do not ask for a vet on an ordinary labelled drench.

Veterinary chemical record rules for South Australia, Western Australia, Tasmania, the Northern Territory and the ACT were not researched (livestock note, 23 Oct 2026). If the property is in one of those places, the Victoria, NSW and Queensland points below are not a statement of that state's law. Say so. Still ask who authorised an off-label or Schedule 4 use, because inventing an authority is worse than an incomplete state table.

## Collect

| Fact | Where it goes |
|---|---|
| Who authorised it, in their words | `vet_authorisation` |
| The vet's withholding period, when the use was off-label and the vet set one | `whp_days` and `esi_days` are owned by `li-withholding-meat-esi`. Pass the vet's figures to that item and say they replace the label figures for this use |

Do not invent a vet's name or a vet's interval. If they do not have the written direction, record the gap. They may still save what was given.

## What was checked

| Place | Rule | Last checked | Status |
|---|---|---|---|
| Victoria | Off-label use on sheep, a major species, needs written authorisation from a registered veterinarian. The label WHP may not fit. Stock must not be sold inside a WHP unless the buyer is told in writing | 19 Oct 2026 | E |
| New South Wales | Off-label use needs a veterinarian's written directions (Stock Medicines Act 1989 s 39D). The statutory treatment record in s 39E is the vet's, for two years. A farmer's ordinary drench is not that vet record. s 40A: the buyer is told of a withholding period | 19 Oct 2026 | E |
| Queensland | People who are not vets use registered or permit products according to the label or permit. Sheep are a major trade species. Off-label use is tightly limited. Treated animals must stay identifiable through the withholding period (s 12T). Supply inside the withholding period needs written notice (s 12U) | 19 Oct 2026 | E |

Sheep, cattle and goats are treated as major food species in the states above. Do not extend that sentence to a state that was not read.

## Checks

Severity: `legal`.

- Antibiotic, Schedule 4 or off-label with no authority named: flag, and ask before saving. They can record the use after they have seen the gap.
- Do not block a record of a use that has already happened.
- HGP is not this item. The treatment orchestrator stops HGP on sheep and goats. `li-hgp-cattle` is not in this release.

## Confirm fragment

`Off-label: {vet_authorisation}` or `Authority: not recorded`.

## Sources

Agriculture Victoria veterinary chemicals: <https://agriculture.vic.gov.au/farm-management/chemicals/veterinary-chemicals> (19 Oct 2026, E).

NSW stock medicines: <https://www.dpi.nsw.gov.au/agriculture/chemicals/animal-chemicals/stock-medicine> (19 Oct 2026, E).

Queensland, treating animals: <https://www.business.qld.gov.au/industries/farms-fishing-forestry/agriculture/sustainable/chemical/use/animals> (19 Oct 2026, E).

Queensland Act: <https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1988-103> (19 Oct 2026, E).
