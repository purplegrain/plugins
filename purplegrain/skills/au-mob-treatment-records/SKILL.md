---
name: au-mob-treatment-records
description: Check and save Australian mob treatment records and sheep husbandry records before writing them to PurpleGrain or copying them as an LPA row. Use for a drench, fluke, lice or fly treatment, jetting or dipping, vaccine, antibiotic, pain relief or other veterinary chemical, and for marking, mulesing, tail docking, castration, ear marking, NLIS tagging, crutching, shearing, wigging, scanning, weaning or weighing. Covers LPA treatment fields, meat WHP, ESI, wool interval, and the sheep welfare, wool declaration, health declaration and traceability checks.
---

# Australian mob treatment and sheep husbandry records

Use this whenever a farmer asks to record, import or correct an animal treatment, or a sheep husbandry job, whether typed, spoken, or from a photo. Treatments follow the same LPA path for any mob. Sheep adds husbandry procedures and the compliance checks below.

Never save first and check later. Always: collect -> check -> confirm with the farmer -> save -> read back.

This is a completeness check. It is not veterinary or legal advice. Label directions, the current APVMA sheep ESI list, and the state rule are the authority. Source detail, retention periods and who inspects are in `references/sheep-requirements.md`. Read that file when a sheep welfare, wool, health-declaration, NLIS, biosecurity or state-law point needs a source, or when a figure might have changed.

## 1. Choose the record

| What happened | Record |
|---|---|
| A product given to the mob: drench, fluke, lice, flystrike, other external parasite, vaccine, vitamin or mineral, antibiotic, pain relief on its own, foot treatment, reproductive treatment, in-feed or in-water additive | `createTreatmentRecord`, one mob, `category` set |
| Something done to a sheep mob: marking, mulesing, tail docking, castration, eID tagging, crutching, shearing, wigging, scanning, weaning, classing, weighing | `createHusbandryRecord` |
| Marking day (dock, castrate, mules, mark, tag, plus the vaccine and the pain relief) | One husbandry record. Procedures and product lines together. Do not also save a treatment for the same vaccine or pain relief |
| Crutch or shear with a jet or dip chemical on the same day | One husbandry record: the procedure plus the product lines |
| HGP on sheep | Stop. HGPs are not an ordinary sheep treatment. Do not use `category: hgp` or `hgp_earmarked` for sheep |
| Paddock-to-paddock move on the same property | `moveMob`, and only when the farmer asked to move the mob |
| Sale, agistment, or any move onto another PIC | Not a treatment or husbandry record, and not `moveMob`. The receiver updates the NLIS database. Collect the declaration facts in section 2 and leave them out of the product fields |

A completed treatment needs at least one product row. A husbandry record may have none (a scan or a weigh). Three mobs means three calls.

## 2. Collect

Pull out what the farmer already said and ask only for what is missing. The farmer may save with a gap; an unknown value stays unset and prints "not recorded". Never invent a batch, expiry, dose, rate, WHP, ESI, wool interval or head count.

### Treatment fields (LPA, any mob)

| Field | Where it goes |
|---|---|
| Treatment date | `date` as `YYYY-MM-DD`. Not in the future for a job already done |
| Mob | An existing mob, resolved before the write |
| Head treated | `head`. May be less than the mob. If omitted, the server uses the mob's count: check that default first |
| Product trade name | One `products` entry each, up to 10 |
| Active constituent | `active`, when stated |
| Batch number | `batch`. LPA wants it even when a vet treated |
| Expiry | `expiry` as `YYYY-MM-DD` |
| Dose | `dose` verbatim, plus `dose_value`, `dose_unit` (`mL`, `L`, `g`, `kg`) and `dose_basis` (`per_head`, `per_kg`, `per_mob`) when clearly stated. Do not parse a dose per 5 kg into a per-kg value |
| Route | Treatment `route`: `oral`, `injection`, `backline`, `jetting`, `dip`, `capsule`, `topical`, `in_feed_water`. Ask if the word is ambiguous. A footbath is not a dip |
| Meat WHP days | `whp_days`, whole days, from the label |
| ESI days | `esi_days`. If the label and the current APVMA list have no separate ESI, send the WHP only after saying so. The server does not substitute |
| Wool harvest interval | `wool_interval_days` when the label states one. Sheep rehandling interval has no field: `record_notes` |
| Milk WHP | `milk_whp_days` only if this mob is milked and the label states one |
| Treated by | The server sets `operator` from the signed-in user. Someone else: `updateTask` `operator` after saving. A phone number has no field: `record_notes` |
| Chemical group | `drench_group` when stated (`BZ`, `LV`, `ML`, `AD`, `SI`, `OP`, `TZ`, `SA`, `IQ`, or a combination) |
| Equipment cleaned | `equipment_cleaned` true or false only when stated. Who cleaned it: `record_notes` |
| Adverse reaction or broken needle | `adverse_reaction`. Which individual still has a needle: `record_notes`. A mob record does not identify one sheep |
| Off-label or vet instruction | `vet_authorisation` with who authorised it. On-label use: leave unset |
| Where they were treated | No paddock field on a treatment. Name the paddock in `description` or `record_notes` |

`description` is a short title, for example "Drench ewes". Optional catalogue link: `product_id` from `listProducts`. Values are copied at save.

### Sheep husbandry fields

| Procedure | `procedures` value | Structured outcomes | Also collect |
|---|---|---|---|
| Marking | `mark` | `lambs_marked`, `ewes_joined` | Method in `method` |
| Tail docking | `tail_dock` | None. Extra numbers are refused | Method (rings, hot knife, knife). Whether one palpable joint remains, and that the ewe dock covers the vulva: `record_notes` |
| Castration or cryptorchid | `castrate` | None | Method. Cryptorchid stated in `method` |
| Mulesing | `mules` | None | Age, pain relief, and that only wool-bearing skin was removed: `record_notes` if not already on a product |
| eID or NLIS tag | `eid_tag` | None | Breeder or pink post-breeder, year colour, PIC on the tag: `record_notes` |
| Ear notch or brand | No procedure. Use `mark` when it is part of lamb marking, otherwise `other` | None | The mark itself in `method` and `record_notes` |
| Crutching | `crutch` | None | |
| Shearing | `shear` | `shearer` (text), `bales`, `wool_kg` | Cuts treated, shelter: `record_notes` |
| Wigging | `other` | None | Say "wigging" in `description` and `record_notes` |
| Weaning | `wean` | `weaned`, `avg_kg` | |
| Scanning | `scan` | `singles`, `twins`, `triplets`, `dry` | |
| Classing | `class` | None | Class result in `record_notes` |
| Weighing | `weigh` | `avg_kg`, `lightest_kg`, `heaviest_kg` | |

`marking_percent` is calculated when the record is read. Never send it.

Pain relief, a vaccine at marking, and jetting fluid are `products` on the husbandry record. Same product shape as a treatment (name, active, batch, expiry, dose, `whp_days`, `esi_days`, `wool_interval_days`, `milk_whp_days`, `drench_group`). Husbandry has no `route`, `category`, `equipment_cleaned`, `adverse_reaction` or `vet_authorisation`. Put route, off-label authority and a broken needle in `record_notes`.

`head` is the number the work was done to. `method` is the procedure method, such as "rings", not the vaccine route.

### Sheep facts that have no API field

Ask when the job makes them relevant, then put the answer in `record_notes` after the record exists. Do not invent a JSON key.

- Lamb age, so the welfare check can be made.
- National Wool Declaration mob status the farmer is actually claiming: `NM`, `LN`, `AA` or `M`. Mixed mobs take the lowest of `NM`, then `LN`, then `AA`, then `M`. `CM` is a property answer (both ceased-mulesing questions "no"), not a mob code. `PR` is the old name for `AA`.
- Sheep Health Declaration points when they are selling or moving: virulent footrot, benign footrot or scald, lice, JD approved vaccinates and years of continuous lamb vaccination, SheepMAP, a negative JD test and its date. State rules differ on when the form is mandatory.
- NLIS: animals born on or after 1 January 2025 need an approved eID before they leave the property of birth. Victoria has required an eID on all sheep leaving a property since 1 January 2022. The receiver records the movement on the NLIS database. Do not claim this record did that.
- A plunge dip or powered spray race in NSW also wants the applicator contact, property address, and outdoor spray weather. Pour-ons and hand-held treatments are outside that pesticide record.
- Total quantity used, if Victoria's record is the one they are keeping and the per-head dose does not already show it.

## 3. Check before saving

Run every check and report it as a short list. Do not silently fix anything.

**Missing fields.** Name each missing LPA field. Batch, expiry, route and ESI are the ones most often missing. For husbandry, name any procedure they described but did not confirm, and any product line missing batch, expiry, dose or a withholding figure the label should have.

**Dates.** Meat WHP end = treatment date + `whp_days`. ESI end = treatment date + `esi_days`. Wool end = treatment date + `wool_interval_days` when that number was given. Calculate these yourself. A one-day difference against a sheet is a convention: say which day you are using. A larger gap, or a safe date copied from the row above, is a likely error. Treatment date after expiry: flag, product was out of date. A future date is a plan, not a completed record: stop and ask.

**Numbers.** Head treated above the mob's head count: flag. Dose with no unit, or a WHP, ESI or wool interval that is not a whole number of days: ask. Do not judge a dose against a label you have not seen.

**Product and intervals.** If you can search, compare the ESI with the current APVMA sheep list at <https://www.apvma.gov.au/chemicals-and-products/pesticides-and-veterinary-residues/esi-sheep>. Report a difference. Do not override the farmer without telling them. `listProducts` with `kind=drench` is a short catalogue, not that list, and it has no vaccine or lice kind. Several products: the mob waits until the latest end date. Oxytetracycline or chlortetracycline: keep the listed ESI in `esi_days` and add the SAFEMEAT provisional 90-day Russian market note in `record_notes`. Do not silently store 90 as the ESI.

**Sheep welfare (flag, do not rewrite the history).** National sheep standards: no mulesing under 24 hours or over 12 months; pain relief is mandatory for mulesing at 6–12 months; no mulesing of ill-thrift sheep; only wool-bearing skin. Tail docking and castration over 6 months need pain relief and haemorrhage control, and a docked tail keeps at least one palpable joint. Guidelines, not bans: dock and castrate after 24 hours and before 12 weeks; pain relief where practical at marking; mules at 2–12 weeks. Tasmania is stricter (no mulesing under 14 days or over 6 months, and pain relief at every mulesing). If the farmer states an age or a method outside the national standard, show the standard and ask before saving. Shearing: the standard is to shear before the wool is longer than twice that breed's average annual growth.

**NWD.** Mulesing with an APVMA-registered analgesic or anaesthetic is `AA`. Mulesing without one is `M`. Liquid nitrogen is `LN`, and it is not mulesing. Never assign a status the farmer did not state.

**Duplicates.** `listTasks` with `asset_id` of the mob and `filter_status: ["completed"]`, after the mob has been resolved, and follow pagination. Read `treatment.products` or `husbandry.procedures` and `husbandry.products`. Same day and same product, or the same husbandry procedures, is probably a duplicate: ask.

**Unclear input.** A value you could not read or hear is UNCLEAR and must be confirmed. Never guess a product name or batch.

## 4. Confirm with the farmer

Show one compact summary and wait for a yes. Show it again if anything changes.

```
Drench - Ewes (250 hd), 05/06/26, treated by JS
- Startect 15 mL/hd oral, batch 123456, exp 03/27
  WHP 14 d -> safe for domestic 19/06/26
  ESI 28 d -> safe for export 03/07/26
Checks: OK (or a list of what needs attention)
Save this record?
```

```
Marking - Lambs (412 hd), 12/08/26, by JS
Procedures: mark, tail dock (rings), castrate (rings), mules. Age stated: about 4 weeks
- Tri-Solfen, dose as stated, batch and expiry as stated
  WHP and ESI as stated
Checks: pain relief is on the record; one palpable tail joint not confirmed; NWD status not stated
Save this record?
```

Use the farmer's real figures. The lines above only show the shape.

## 5. Save

Find the property and the mob first. `fetchCurrentUser` is the signed-in user. `listBusinessMembers` with that user's id and `include: "organization"` lists accepted memberships. `listProperties` without `organization_id` is personal properties only; pass the business `organization_id` for its properties. `getPropertyPicture` shows every mob on one property. `listMobs` with `property_id` scopes to that property. Never substitute an account or guess an id. Creating a missing mob needs its own confirmation.

`createTreatmentRecord`: `mob_id`, `confirm: true` only after the farmer's yes, and `body.data.type: "treatment-record"`. `category` is required: `drench`, `fluke`, `lice`, `flystrike`, `other_external_parasite`, `vaccine`, `vitamin_mineral`, `antibiotic`, `pain_relief`, `feed_water_additive`, `foot_treatment`, `reproductive` or `other`. Fields sit in `body.data.attributes`.

`createHusbandryRecord`: `body.data.type: "husbandry-record"`. Send only outcome keys listed in section 2, nested under the procedure, for example `outcomes.mark.lambs_marked`. A figure the procedure does not carry is refused.

The server sets `operation_type`, `capture_source: agent`, `operator` and `producer`. Do not send `broadcast`, `share_scope`, `operation_type: ai` or `rerun_ai`. Do not fall back to `createTask` to get around a refusal. A 403 with `code: insufficient_access` is a real refusal: show its `detail` and stop.

`record_notes`, tags and a corrected `operator` are a later `updateTask` on the saved task, with `confirm: true`. Notes do not set withholding dates. Tags do not either.

If a write fails or times out, read the mob's completed records before retrying, and do not create a second record when the first one is already there. If the first attempt sent an `Idempotency-Key`, send that same key on any retry.

`moveMob` only places the mob in a paddock on its own property. It does not write an NLIS transfer.

Without PurpleGrain, produce the same summary as a row the farmer can copy onto the LPA livestock treatment record, and a husbandry note for anything that form does not hold.

## 6. Read back

`getMob` `withholding`, or `getPropertyStatus` for the property, is the current status. It already includes completed treatment and husbandry products. Do not decide the mob is clear by reading the new record alone.

`getTreatmentRegister` with `kind: "register"` is the LPA treatment register, one row per product on completed treatments and husbandry. A husbandry with no product has no row. `kind: "nvd"` is what is still inside a WHP or ESI today. Pass `mob_ids` when the question is about one mob. Missing dates or an empty NVD view do not prove the sheep can be sold or slaughtered.

Tell the farmer what was saved, the withholding dates, and any sheep check that is still open (NWD, health declaration, NLIS movement, welfare flag). One or two sentences for the save; the open checks as a short list.
