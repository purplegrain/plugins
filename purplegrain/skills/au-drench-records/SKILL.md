---
name: au-drench-records
description: Check and save Australian livestock drench and animal treatment records (LPA, WHP, ESI) before creating them in PurpleGrain or any farm record system.
---

# Australian drench and treatment records

Use this whenever a farmer asks to record, import or correct a drench, vaccination, jetting, pour-on or other animal treatment for Australian livestock, whether typed, spoken, or from a photo of a paper treatment sheet. The job: make the record complete and correct for LPA before anything is saved, then save it.

Never save first and check later. Always: collect -> check -> confirm with the farmer -> save -> read back.

## 1. Collect these fields (one set per product given)

Required by LPA (Livestock Production Assurance):

| Field | Notes |
|---|---|
| Treatment date | DD/MM/YYYY. Must not be in the future. |
| Mob | An existing mob on the property, or a clearly named new one. |
| Head count treated | May be less than the mob. |
| Product trade name | One line per product when several are given together. |
| Batch number | Required even if a vet gave the treatment. |
| Expiry date | From the pack. |
| Dose | Value + unit (mL) + basis (per head or per kg). |
| Route | Oral, pour-on, injection (SC/IM), jetting, etc. |
| WHP days | Meat withholding period from the label. |
| ESI days | Export slaughter interval. If none exists, use the WHP. |
| Treated by | Name or initials. |

Optional but useful: equipment cleaned/calibrated, adverse reactions, broken needle, notes, drench group/active ingredients.

If the farmer gives everything in one sentence ("drenched the ewes with Startect 15 mL today, batch 123456"), pull out what is there and only ask for what is missing.

## 2. Check before saving

Run every check and report the results as a short list. Do not silently fix anything.

**Missing fields**
- List each missing required field by name. Batch, expiry, route and ESI are the ones most often missing.
- The farmer may choose to save without a field; if so, record it as "not recorded" rather than inventing a value.

**Dates**
- WHP end = treatment date + WHP days. ESI end = treatment date + ESI days (or + WHP days when there is no ESI).
- Calculate these yourself. If the farmer or the sheet gives a safe date, compare: a 1-day difference is a convention (last day under WHP vs first day safe) - say which you are using; a bigger difference is a likely error - flag it. A common paper-sheet error is safe dates copied from the row above.
- Treatment date after the expiry date -> flag: product was out of date.
- Treatment date in the future -> stop and ask.

**Numbers**
- Head count treated greater than the mob's head count -> flag.
- Dose with no unit, or WHP/ESI that is not a whole number of days -> ask.
- Do not judge whether a dose is right for the animal unless the farmer gives the label rate; you do not know the label.

**Product and intervals**
- If you can search the web, check the ESI against the APVMA ESI list (apvma.gov.au/esi), because ESIs change during the year. Report any difference; don't override the farmer's figure without telling them.
- `listProducts` with `kind=drench` is a short PurpleGrain catalogue, not that APVMA list. Use it as a hint and still confirm the label.
- If several products were given at once, check each one; the mob's withholding ends on the latest of them.

**Unclear input (photos and voice)**
- Any value you could not read or hear clearly is marked UNCLEAR and must be confirmed. Never guess a product name or batch number.

**Duplicates**
- Before saving, look at the mob's completed records (`listTasks` with `asset_id` set to the mob and `filter_status` including `completed`). Read `drench.products`. A treatment on the same date with the same product is probably a duplicate - ask.

## 3. Confirm with the farmer

Show one compact summary and wait for a yes:

```
Drench - Ewes (250 hd), 05/06/26, treated by JS
- Startect 15 mL/hd oral, batch 123456, exp 03/27
  WHP 14 d -> safe for domestic 19/06/26
  ESI 28 d -> safe for export 03/07/26
Checks: OK (or a list of what needs attention)
Save this record?
```

Apply any corrections and show the summary again if anything changed.

## 4. Save

In PurpleGrain (if its tools are available):

- Find the property. `fetchCurrentUser` is the signed-in user. `listOrganizationRoles` with that user's id and `include=organization` is the businesses they belong to. `listFarms` with no `organization_id` is personal properties only. A business's properties need `listFarms` with that `organization_id`. `getFarmPicture` is every mob on one property. `listMobs` with neither `farm_id` nor `organization_id` is personal-property mobs only.
- Save with `createDrenchRecord` on that mob. One record per mob. A combination treatment is several `products` on that one record, not one record per product. Three mobs means three calls.
- Send `date` as `YYYY-MM-DD` (the treatment day). The server stores midday in its time zone. A future date creates an open task instead of a record — stop and ask. Send `head` as the head count treated (omit it to use the mob's current count). Send `description` as a short title, for example "Drench rams".
- Each product is `{ name, active, batch, dose, whp_days, esi_days }`. `dose` is value, unit and basis, for example "15 mL per head" or "1 mL / 5 kg". If the label has no ESI, send the WHP number as `esi_days`. The server does not substitute.
- The server sets `operation_type` to `drench`, `capture_source` to `agent`, `status` and `created_as` from the date, `operator` from the signed-in user, and `producer` from the farm's owner. Do not send `broadcast` or `share_scope`.
- Expiry and route are not fields on `createDrenchRecord`. When the farmer stated them, write them afterwards with `updateTask` in `record_notes`, using "not recorded" rather than inventing a value. If someone other than the signed-in user treated, set `operator` on that same task (free text, for example "JS").
- Optional tags, also via `updateTask`: `drench`, one lowercase-hyphenated tag per product, `whp-until-YYYY-MM-DD`, `esi-until-YYYY-MM-DD`, `needs-review` if the farmer saved with an open flag, and `import-<source-id>` to group one imported sheet. Tags do not set the withholding dates.
- Pass `confirm: true` only if the server asks for it.
- If a write fails or times out, read the mob's completed records back before retrying, so no duplicate is created. A 403 whose `code` is `insufficient_access` is a real access refusal: show its `detail` and stop.
- Do not use `createTask` for a drench unless notes, tags or a different `operator` have to go in the same write. On that path, a business-owned property needs `producer` set to the owning organization (`type: organization`). Without it the write is refused with 403 detail "Unauthorized", which is a missing producer.

The response includes `drench.safe_for_slaughter_on` and `drench.export_eligible_on`, derived from the completion date plus the longest WHP and ESI among named products. Both are null while the task is open.

Without PurpleGrain, produce the same summary as an LPA treatment-record row the farmer can copy.

## 5. Read back

After saving, tell the farmer in one or two lines: what was saved, and the mob's withholding status ("Under withholding until 03/07/26 (export)" or "Clear to sell"). Read that from `drench.export_eligible_on` and `drench.safe_for_slaughter_on`, or from `withholding` on `getMob`. If the mob is still under WHP or ESI, remind them it must be declared on the NVD if sold before then.

## Limits

- This checks completeness and arithmetic. It is not veterinary or legal advice; label directions and the APVMA list are the authority.
- Never invent a batch number, expiry, WHP or ESI.
