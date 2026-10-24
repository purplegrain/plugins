---
name: au-mob-treatment-records
description: "Check and save an Australian mob treatment before writing it to PurpleGrain or copying it as an LPA row. Use for a drench, fluke, lice or fly treatment, jetting or dipping, vaccine, antibiotic, pain relief or other veterinary chemical given to a mob. Marking, mulesing, docking, castration, shearing and the other husbandry jobs belong to au-mob-husbandry-records."
---

# Australian mob treatment records

Version 2.0.0. Husbandry moved to `au-mob-husbandry-records`. A vaccine or pain relief given on marking day stays on that husbandry record. Do not also save a treatment for the same products.

Follow `pg-core`. If the account has no mob to attach this to, offer `pg-onboarding`. Do not block a read. Do not collect setup fields here.

This is a record. It is not veterinary or legal advice. The label, the APVMA list and the vet's written direction are the authority.

Never save first and check later. Collect, check, confirm, save, read back.

If this folder is installed, `references/sheep-requirements.md` (checked 19 Oct 2026, with an eID correction on 24 Oct 2026) is the long note. The line items below are the rules to apply. The eID dates in that note's older paragraphs are superseded by `li-eid-tagging`.

## 1. Choose the record

| What happened | Record |
|---|---|
| A product given to the mob | `createTreatmentRecord`, one mob, `category` set |
| Marking, mulesing, docking, castration, tagging, crutching, shearing, scanning, weaning, weighing, dehorning, spaying | `au-mob-husbandry-records` |
| Marking day, or crutch or shear with a chemical the same day | One husbandry record. Not also a treatment |
| HGP on sheep or goats | Stop. Do not use `category: hgp` or `hgp_earmarked`. There is no ordinary sheep or goat HGP practice (LPA Rules 11.5, sheep reference, 19 Oct 2026, E) |
| HGP on cattle | This record, `category: hgp`. `li-hgp-cattle` is not in this release. Ask whether the triangular ear punch was done and store `hgp_earmarked` only if they say so. Do not state an EU status |
| Paddock move, sale, or a move off the PIC | `au-stock-movement-records`. Not this skill |

A completed treatment needs at least one product. Three mobs means three calls.

`category`: `drench`, `fluke`, `lice`, `flystrike`, `other_external_parasite`, `vaccine`, `vitamin_mineral`, `antibiotic`, `pain_relief`, `feed_water_additive`, `foot_treatment`, `reproductive`, `hgp`, `other`.

`route`: `oral`, `injection`, `backline`, `jetting`, `dip`, `capsule`, `topical`, `in_feed_water`. Ask if the word is ambiguous. A footbath is not a dip. The route is this skill's field. No line item owns it.

A plunge dip or powered spray race in NSW is also a pesticide record: applicator contact, property address, and outdoor weather, kept 3 years (sheep reference, 19 Oct 2026, E). Pour-ons and hand-held treatments are outside that pesticide record. Put the extra pesticide facts in `record_notes`. Weather fields are on a spray, not on a treatment. `li-vetchem-state-rules` is not in this release. This paragraph is the stand-in.

## 2. Line items

Read each installed skill. Ask one or two missing things at a time, legal first. If a skill is not installed, still ask for its fields and say the detailed check was skipped.

| Line item | Applies when | What it owns |
|---|---|---|
| `li-off-label-vet` | Off-label, Schedule 4, or `antibiotic` | `vet_authorisation` |
| `li-withholding-meat-esi` | Every product | `whp_days`, `esi_days`, `wool_interval_days`, `milk_whp_days` |
| `li-operator-credential` | Every record. Credential only if a state chemical rule applies (a NSW dip) | `operator` |
| `li-product-batch-expiry` | Every product | `batch`, `expiry` |
| `li-dose-liveweight` | Every product | `dose`, `dose_value`, `dose_unit`, `dose_basis`, live weight in notes |
| `li-adverse-reaction` | Every treatment | `adverse_reaction` |
| `li-record-retention` | After the save | Keep-until note. Do not ask them to choose |

Not in this release: `li-hgp-cattle`, `li-vetchem-state-rules`, `li-equipment-calibration`. Still ask the short forms below.

| Fact with no shipped line item | Where it goes |
|---|---|
| Date | `date` as `YYYY-MM-DD`. A future date is a plan, not a completed record. Stop and ask |
| Mob | Resolve it before the write |
| Head treated | `head`. May be less than the mob. If omitted, the server uses the mob's count. Check that default |
| Where they were treated | No paddock field. `description` or `record_notes` |
| Chemical group, when stated | `drench_group`: `BZ`, `LV`, `ML`, `AD`, `SI`, `OP`, `TZ`, `SA`, `IQ`, or a combination |
| Equipment cleaned, only when they say | `equipment_cleaned` true or false. Who cleaned it, and a calibration date: `record_notes` |
| Total quantity, when Victoria's record is the one they are keeping and the dose does not already show it | `record_notes` |

Victoria, within 48 hours, keep 2 years, for a Schedule 4 product, a product with a withholding period, or an HGP: trade name, species, location, identification, dates, quantity (Agriculture Victoria, 19 Oct 2026, E). Queensland: treated animals stay identifiable through the withholding period, and supply inside that period needs written notice (Chemical Usage Act s 12T and s 12U, 19 Oct 2026, E). Do not block a shearing solely because a meat WHP is still running. NSW: the farmer's ordinary drench is not the vet's s 39E record. SA, WA, Tasmania, NT and the ACT veterinary-chemical record rules were not researched (23 Oct 2026). Do not state them.

## 3. Check

Report a short list. Do not silently fix anything.

Run every line item that applies. Also: head treated above the mob's head count, flag. Duplicate: `listTasks` as in `pg-core`, reading `treatment.products`. Same day and same product: ask. A value you could not read is UNCLEAR.

`equipment_cleaned` left unset is "not recorded", not a no.

## 4. Confirm

```
Drench - Ewes (250 hd), 05/06/26, treated by JS
- Startect 15 mL/hd oral, batch 123456, exp 03/27
  WHP 14 d -> safe for domestic 19/06/26
  ESI 28 d -> safe for export 03/07/26
Checks: OK (or the list)
Save this record?
```

Use their figures. Wait for a yes. Show it again if anything changes.

## 5. Save

Resolve the account as in `pg-core`. `getPropertyPicture` or `listMobs` with `property_id` finds the mob. Never guess an id.

`createTreatmentRecord`: `mob_id`, `confirm: true` only after the yes, `body.data.type: "treatment-record"`. Fields in `body.data.attributes`. `category` is required.

The server sets `operation_type`, `capture_source: agent`, `operator` and `producer`. Do not send `broadcast`, `share_scope` or `operation_type: ai`.

Notes, tags and a corrected operator follow `pg-core` (on the create if the tool accepts them, otherwise `updateTask` with `confirm: true`). The treatment create schema reviewed on 24 Oct 2026 does not take `record_notes`, `operator` or `tags`. This tool accepts `Idempotency-Key`. If the write fails or times out, read the mob's completed records before retrying, and reuse that key when the first attempt sent one.

Without PurpleGrain, produce the same summary as a row they can copy onto the LPA livestock treatment record.

## 6. Read back

`getMob` `withholding`, or `getPropertyStatus`, is the status. It includes completed treatment and husbandry products. Do not decide the mob is clear from the new record alone.

`getTreatmentRegister` with `kind: "register"` is one row per product. `kind: "nvd"` is what is still inside a WHP or ESI. Pass `mob_ids` for one mob. An empty NVD view does not prove the animals can be sold or slaughtered.

Tell them what was saved, the withholding dates, and any check still open. One or two sentences, then the open checks.
