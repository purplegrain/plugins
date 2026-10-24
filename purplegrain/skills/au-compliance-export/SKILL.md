---
name: au-compliance-export
description: "Prepare an Australian compliance export from PurpleGrain registers. Use when the farmer asks for an LPA treatment register, an NVD withholding list, a spray diary, a paddock-inputs list, or what is still not recorded before an audit or a sale."
---

# Compliance export

Version 1.0.0. Follow `pg-core`. This skill does not create a treatment, a spray or any other record. It reads. If they want a gap filled, hand that one record to the matching skill. If there is no property, offer `pg-onboarding`. Do not block the read they asked for. An empty account has nothing to export. Say that.

This is a printout of what is stored. It is not an LPA audit, and it is not approval. Do not say "LPA approved".

## Which register

`getTreatmentRegister` on the property.

| They ask for | `kind` | Scope |
|---|---|---|
| LPA treatment register | `register` | `mob_ids` when it is one mob. Every treatment product and every husbandry product. A husbandry with no product has no row |
| What is still inside a WHP or ESI | `nvd` | `mob_ids` optional. This is not a completed NVD. An empty result does not mean the stock can be sold or slaughtered |
| Chemical-use register | `spray` | `paddock_ids` |
| Fertiliser and sowing | `paddock-inputs` | `paddock_ids`. Fertiliser is not in the spray register and not in the NVD view, because it has no withholding |

A value the record should carry and does not is the text `not recorded`. Say it that way. Do not fill it in. Do not invent a batch, a PIC or a date to make a column look finished.

## PIC and photos

`pic` is the property's identification code (API #239/#240), and it is nullable. If `pic` is null, say the PIC is not recorded. Do not copy a town out of `location` and call it the PIC. Do not look a PIC up on WA Brands Search.

Photos on a task are untyped. There is no document-type field for "label", "CVD" or "NVD" in the schema reviewed that day. List the photos that are actually on the tasks they asked about. Do not call an untyped image an NVD.

## What is missing

Walk the rows. For a legal or LPA gap, name the line item that would have asked for it, when one is installed:

| Gap on the row | Line item |
|---|---|
| Batch or expiry | `li-product-batch-expiry` |
| Meat WHP or ESI | `li-withholding-meat-esi` |
| Grazing or harvest WHP | `li-grazing-harvest-whp` |
| Dose | `li-dose-liveweight` |
| Who did it | `li-operator-credential` |
| Wind or weather | `li-spray-weather` |
| No-spray zone or droplets | `li-buffer-drift` |

`li-record-retention` is the keep-until rule if they ask how long to hold the export. Cite both ISC lines. Do not tell them to delete older rows.

State, species and the NWD or health-declaration answers are not register columns today when they were stored only in notes. Mention the notes. Do not drop them.

Offer to fix a gap only for the rows they care about. One record at a time, through the orchestrator, with a confirm. Do not bulk-update guessed values.

A PIC is private. Do not put the export on a public page or into a message to someone the farmer did not name.
