---
name: li-product-batch-expiry
description: "Line item for PurpleGrain record skills. Do not use directly. Batch number and expiry on every product line, and a flag when the expiry is before the day of use."
---

# Batch and expiry

Version 1.0.0. Do not call a PurpleGrain write. The orchestrator saves. Do not ask for dose, rate or withholding. Those belong to other line items.

## Applies when

Any product line on a treatment, husbandry, spray, sowing or fertiliser record.

## Collect

| Fact | Where it goes |
|---|---|
| Batch number, as printed | `products[].batch` |
| Expiry | `products[].expiry` as `YYYY-MM-DD` |

Ask for both when they are missing. LPA's livestock treatment template wants the batch even when a vet treated, and it wants the expiry. A spray or sowing product line has the same two fields. A fertiliser line has `batch` and no `expiry`. Do not send `expiry` on fertiliser.

Never invent a batch or an expiry. Unreadable is UNCLEAR. They may save with the field unset. It prints `not recorded`.

## Checks

Severity for ordering questions: `lpa`.

- Expiry before the date of use: flag it. Record what they used. Do not tell them they must not have used it, and do not block the save.
- No batch: name it as an LPA gap. Do not turn a missing batch into advice to throw the product out.
- Do not compare the batch with a catalogue. `listProducts` does not prove a batch.

## Confirm fragment

`batch {batch}, exp {expiry}` or `batch not recorded, exp not recorded`.

## Sources

| Source | Last checked | Status |
|---|---|---|
| ISC record keeping, and the LPA livestock treatment template (batch, expiry, within 48 hours is the template's timing, not this item's field) | 19 Oct 2026 | E, sheep reference |
| Integrity Systems record-keeping page | 23 Oct 2026 | V, livestock research |

The 48-hour recording timing is a state and LPA deadline. `li-record-retention` and `li-state-chem-record-rules` own deadlines. This item only owns batch and expiry.
