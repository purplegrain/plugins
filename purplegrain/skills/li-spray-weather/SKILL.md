---
name: li-spray-weather
description: "Line item for PurpleGrain record skills. Do not use directly. Wind, temperature, humidity, delta T and inversion for an outdoor spray, including Queensland's before, during and after readings."
---

# Spray weather

Version 1.0.0. Do not call a PurpleGrain write. Record only measurements the farmer gives. A reading nobody took stays off the list. An empty object is not a weather record.

State variants live in this one skill. Separate `li-spray-weather-qld` skills are not part of this release.

## Applies when

A spray outdoors. A shed treatment with no outdoor spray does not need a wind reading unless the label or the state row asks for weather.

## Collect

One `weather_readings` object per observation. This item owns that list.

| Fact | Field |
|---|---|
| When it was taken | `read_at` |
| Wind speed, km/h | `wind_kmh` |
| Gust, km/h | `gust_kmh` |
| Direction | `wind_dir` |
| Temperature, °C | `temp_c` |
| Relative humidity, % | `rh_pct` |
| Delta T | `delta_t` |
| Cloud, % | `cloud_pct` |
| Rain, mm | `rain_mm` |
| Inversion seen, if they looked | `inversion_observed` |
| On-site, or a station and how far | `source` |

Finish time is not a second weather field. `li-state-chem-record-rules` puts start and finish in `record_notes` when the state requires them.

## Checks

Severity: `legal`.

- Queensland: a reading before, during and after, with the time of each (spray reference, Chemical Usage Regulation s 33C, 19 Oct 2026). One reading in Queensland: say the other two are missing. Do not invent them.
- NSW outdoor spray equipment: wind speed and direction at the start and at any significant change, plus any other weather the label names (19 Oct 2026). NT: temperature, wind speed and direction, and changes during use (23 Oct 2026, V).
- Compare wind with the window on the label they are using. The APVMA standard restraint, where the label uses it, is 3–20 km/h and no hazardous surface inversion (spray reference, 19 Oct 2026). Some labels say 3–15. Do not substitute a remembered window.
- South Australia, Group 4 herbicides in the prescribed businesses and areas: daytime, wind between 3 and 20 km/h, no surface inversion, and not little or variable wind (PIRSA, spray reference, 19 Oct 2026, E). Do not apply that sentence to every South Australian spray.
- Inversion not checked when the label forbids spraying in an inversion: flag it.
- Delta T outside 2–8, wind above 15 km/h, still air, or temperature above 28 °C are higher hazard in the Victorian ground-spraying guide (September 2022). The guide says a single high-risk factor need not stop a job unless that factor is an inversion. These are guide figures, not a limit on every label. Do not block the save on delta T alone. Say they are the Victorian guide, last checked 19 Oct 2026.

## Confirm fragment

`Wind {dir} {speed} km/h at {time}, {temp} C, delta T {n}. Inversion {checked or not}.`

## Sources

APVMA spray-drift labelling: <https://www.apvma.gov.au/registrations-and-permits/apvma-labelling-codes/alc/spray-drift-labelling-alc> (19 Oct 2026, E).

Victorian ground-spraying guide, September 2022, linked from the spray reference (19 Oct 2026, E).

NSW Pesticides Regulation 2017 cl 36, via the spray reference (19 Oct 2026, E).

Queensland s 33C, via the spray reference (19 Oct 2026, E).

NT record fields, paddock research (23 Oct 2026, V).
