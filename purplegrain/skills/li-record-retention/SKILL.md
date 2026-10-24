---
name: li-record-retention
description: "Line item for PurpleGrain record skills. Do not use directly. The keep-until date is the longest of the state period, the LPA period and the ISC seven-year line. Do not ask the farmer to pick a shorter one."
---

# How long to keep the record

Version 1.0.0. Do not call a PurpleGrain write. Do not ask the farmer how long to keep it. Compute the date, tell them, and put it in `record_notes` as `Keep until {date}`. A tag `keep-until-YYYY-MM-DD` is optional and is not owned by this item. Tags are also used for imports.

Do not tell them they may destroy records. Do not delete a record to enforce a period.

## Applies when

A saved livestock, chemical, feed or movement record, after the state is known. If the state is unknown, still apply the LPA and ISC lines and say the state period is missing.

A fence note or a general observation is not one of those records. Do not stamp a chemical or LPA period on it unless the note is actually about stock, feed or a chemical. `au-farm-task-records` says the same.

## Which period

Take the longest that applies.

| Source | Period | Last checked | Status |
|---|---|---|---|
| State chemical-use row | The keep column in `li-state-chem-record-rules`. Tasmania: no period was found. Reef ERA tebuthiuron sprays: 6 years. Ordinary Queensland: 2 years | 19 Oct 2026, NT and ACT 23 Oct 2026 | E / V, as that skill marks them |
| Queensland reef cane fertiliser records | 6 years (paddock research, sugarcane ERA standard) | 23 Oct 2026 | V |
| LPA Rules paragraph 11.7 | NVDs and other records for introduced and dispatched livestock: minimum 3 years, or the statutory period, or as long as the livestock remain on the PIC, whichever is longer | 19 Oct 2026 | E |
| ISC record-keeping page | While livestock are on the PIC; after sale, minimum 7 years or the state period | 19 Oct 2026 | E |
| A label or permit | Its own period, if longer. PER87451 as read in the spray reference: 2 years, which is not longer than most state rows | 19 Oct 2026 | E |
| Freshcare | No retention number was verified. Do not add one | 23 Oct 2026 | U |

The two ISC statements differ. Do not merge them into one citation. Keep the longest, and name both when you tell the farmer. Seven years after sale is the longer ISC line. Three years is the Rules line for NVDs and movement records, and it still applies as a minimum while you also keep the seven-year line.

LPA's "while stock remain on the PIC" can be longer than a fixed year count. Say that, and do not pretend a calendar date ends it while those animals are still on the property.

## Checks

Severity: `legal`, because state retention is a legal duty where the state row states one. The LPA lines apply to an accredited PIC even when the state period is shorter.

- Stamp one keep-until date, from the latest end.
- SA general sprays and Tasmanian sprays: do not invent a statutory end date. You may still stamp the LPA or ISC date and label it as that, not as SA or Tasmanian law.
- This does not create a reminder task. `li-record-deadline-reminder` is not in this release.

## Confirm fragment

`Keep until {date} ({which rule}).`

## Sources

LPA Rules: <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/LPA-Rules/> (19 Oct 2026, E).

ISC record keeping: <https://www.integritysystems.com.au/on-farm-assurance/record-keeping/> (19 Oct 2026, E; the page was also opened in the livestock research on 23 Oct 2026).

State periods: the sources listed on `li-state-chem-record-rules`.

Queensland reef cane records: <https://www.qld.gov.au/environment/agriculture/sustainable-farming/reef/reef-regulations/sugarcane> (paddock research, 23 Oct 2026, V).
