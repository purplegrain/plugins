---
name: li-buffer-drift
description: "Line item for PurpleGrain record skills. Do not use directly. The downwind no-spray zone the farmer kept, the droplet size they used, and neighbour notification where Tasmania's code asks for it."
---

# Buffer, droplets and drift

Version 1.0.0. Do not call a PurpleGrain write. Do not look up a buffer table and fill `no_spray_zone_m`. Record the zone they say they kept, and the droplet category they state.

## Applies when

An outdoor spray, and always when they mention a sensitive area, a neighbour, or a buffer on the label.

## Collect

| Fact | Where it goes |
|---|---|
| Downwind no-spray zone kept, metres | `no_spray_zone_m` |
| Droplet size | `droplet_category`: `extremely_fine`, `very_fine`, `fine`, `medium`, `coarse`, `very_coarse`, `extremely_coarse`, `ultra_coarse` |
| Drift from a neighbour was a factor | `neighbour_drift` true only when they say that |
| Neighbour notification | `record_notes` |

`neighbour_drift` means drift from a neighbour affected this job. It is not "I notified the neighbour".

## Checks

Severity: `legal`. Mandatory label spray-drift restraints, including no-spray zones, droplet size and wind limits, are legal requirements where the label carries them (Victorian guide and APVMA labelling code, spray reference, 19 Oct 2026).

- They quote a label buffer, and the zone they kept is shorter: flag it. Do not invent the buffer they did not quote.
- Droplet category missing when the label they quoted names one: flag it.
- Tasmania's Code of Practice for Ground Spraying: occupiers within 100 metres should be told at least one day, preferably two, before a spray (19 Oct 2026, E). Ask that only for a Tasmanian property. Do not apply the 100 metre rule to other states.
- Wind and inversion are `li-spray-weather`.

## Confirm fragment

`No-spray zone {n} m. Droplets {category}.` Add the Tasmanian notification only when the property is in Tasmania.

## Sources

APVMA spray-drift labelling: <https://www.apvma.gov.au/registrations-and-permits/apvma-labelling-codes/alc/spray-drift-labelling-alc> (19 Oct 2026, E).

Tasmania code: <https://nre.tas.gov.au/agriculture/agvet-chemicals/codes-of-practice/code-of-practice-for-ground-spraying> (19 Oct 2026, E).
