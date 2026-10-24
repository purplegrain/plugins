---
name: li-dose-liveweight
description: "Line item for PurpleGrain record skills. Do not use directly. Dose, the dose basis, and approximate live weight for a mob treatment or a husbandry product."
---

# Dose and live weight

Version 1.0.0. Do not call a PurpleGrain write. Do not ask for batch, WHP or route. The treatment orchestrator owns `route`.

## Applies when

A treatment product, or a product on a husbandry record (a vaccine or pain relief given that day).

## Collect

| Fact | Where it goes |
|---|---|
| Dose, in their words | `dose` |
| The number, only when it is clear | `dose_value` |
| Unit, only when it is clear: `mL`, `L`, `g`, `kg` | `dose_unit` |
| Basis, only when it is clear: `per_head`, `per_kg`, `per_mob` | `dose_basis` |
| Approximate live weight | `record_notes`. There is no weight field |

The server does not parse `dose` into `dose_value`, `dose_unit` and `dose_basis`. Send the structured fields only when the farmer stated them. Do not turn "1 mL per 5 kg" into a per-kg value. Ask if the unit or the basis is missing. A dose with no unit: ask, do not guess.

Never invent a dose. Do not judge a dose against a label you have not seen.

Head count above the mob size is the orchestrator's check, not this item. This item does not own `head`.

## Checks

Severity: `lpa`. The LPA treatment template asks for the dose rate and the approximate live weight.

- Missing dose on a product they gave: name it.
- Live weight unknown: leave it out of the notes rather than inventing kilograms. Name it as a gap.
- Husbandry `method` is the procedure (rings, knife), not the dose. Do not put the dose there.

## Confirm fragment

`{dose}` plus, when they gave it, `about {weight}`.

## Sources

| Source | Last checked | Status |
|---|---|---|
| LPA livestock treatment template: dose rate and approximate live weight | 19 Oct 2026 | E |

<https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/lpa-records-templates/lpa-02-livestock-treatment-record-form.pdf>

Weight has no API field. That gap was still true on the treatment schema reviewed 24 Oct 2026.
