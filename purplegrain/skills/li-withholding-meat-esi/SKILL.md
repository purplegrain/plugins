---
name: li-withholding-meat-esi
description: "Line item for PurpleGrain record skills. Do not use directly. Meat withholding period, export slaughter interval, wool and milk intervals, and the dates calculated from them, for a mob treatment or husbandry product."
---

# Meat WHP, ESI, wool and milk

Version 1.0.0. Do not call a PurpleGrain write. Do not ask for batch, dose or the applicator's licence. Grazing and harvest intervals on a spray or a seed treatment belong to `li-grazing-harvest-whp`.

## Applies when

A treatment or husbandry product line. Not a spray, not a fertiliser, not a sowing seed treatment (`esi_days` on a seed treatment is a different field and is not owned here).

## Collect

| Fact | Where it goes |
|---|---|
| Meat WHP, whole days, from the label | `whp_days` |
| ESI, whole days | `esi_days` |
| Wool harvest interval, only when the label states one | `wool_interval_days` |
| Milk WHP, only when this mob is milked and the label states one | `milk_whp_days` |

If the label and the current APVMA list have no separate ESI, you may send the WHP number as `esi_days` only after telling the farmer that is what you are doing. The server does not substitute. Do not send `0` to mean "not recorded". Leave it unset.

A sheep rehandling interval has no field. `record_notes`.

Never store a shorter interval than the label they are holding. Do not invent one. `listProducts?kind=drench` is a short catalogue, not the APVMA list, and it has no vaccine or lice kind.

## Checks

Severity: `legal`. The label WHP is the legal domestic interval. Recording it is also what LPA asks for.

- End dates, which you calculate: meat WHP end = treatment date + `whp_days`. ESI end = treatment date + `esi_days`. Wool end = treatment date + `wool_interval_days` when that number was given. Say which day you are using. A one-day difference against a sheet is a convention. A larger gap, or a date copied from the row above, is a likely error.
- Several products: the mob waits until the latest end. Say so.
- If you can search, compare a stated sheep ESI with the current APVMA sheep list and report a difference. Do not override the farmer silently. Cattle ESI list URL: unverified (livestock research, 23 Oct 2026). Do not invent that URL.
- Oxytetracycline or chlortetracycline in sheep: keep the listed ESI in `esi_days`. Add the SAFEMEAT provisional 90-day Russian sheep-meat note in `record_notes`. Do not store 90 as the ESI unless the farmer confirms that is the figure they want. That note is sheep meat, not cattle. Last checked in the November 2024 sheep ESI PDF via the sheep reference, 19 Oct 2026.
- Wool and milk intervals are not the mob `withholding` object. Meat WHP and ESI are. After the save, the orchestrator reads `getMob.withholding`. Do not tell them the stock can be sold or slaughtered from these dates alone.

## Confirm fragment

`WHP {n} d -> {date}; ESI {n} d -> {date}`. Add wool or milk only when a number was stored. If ESI was copied from the WHP, say so in the checks line.

## Sources

| Source | Last checked | Status |
|---|---|---|
| APVMA ESI, sheep | 19 Oct 2026 | E |
| November 2024 sheep ESI PDF, including the Russian 90-day OTC/CTC note | 19 Oct 2026 | E |
| LPA treatment template columns (WHP, ESI, safe slaughter date) | 19 Oct 2026 | E |
| Cattle ESI list | — | U. No URL was verified |

Sheep list: <https://www.apvma.gov.au/chemicals-and-products/pesticides-and-veterinary-residues/esi-sheep>
