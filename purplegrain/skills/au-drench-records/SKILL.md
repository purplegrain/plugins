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
- Before saving, look at the mob's completed records (`listTasks` with `asset_id` set to the mob and `filter_status` including `completed`). Read `treatment.products`. Resolve the property and mob with the read-only discovery calls in section 4 first; use `filter_status: ["completed"]` and follow pagination before deciding there is no duplicate. A treatment on the same date with the same product is probably a duplicate - ask.

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

- Find the property and existing mob before proposing a write. `fetchCurrentUser` is the signed-in user. `listBusinessMembers` with `user_id` set to that user's id and `include: "organization"` lists their business memberships; use accepted memberships. `listProperties` without `organization_id` lists personal properties only; pass the business's `organization_id` for its properties. `getPropertyPicture` shows every mob on one property. `listMobs` with `property_id` scopes to that property; without `property_id` or `organization_id` it lists personal-property mobs only. Never substitute a different account or guess a mob id. If the mob is missing, clarify; creating it needs separate confirmation.
- Save with `createTreatmentRecord` using that mob's `mob_id` and the required `category`. Use `category: "drench"` for a drench, `vaccine` for a vaccination, and the matching advertised category for lice, flystrike or another treatment. One record per mob. Several products given together belong on one `products` array; three mobs means three calls.
- Send `date` as `YYYY-MM-DD` (the treatment day). The server stores midday in its time zone. A future date creates an open task instead of a completed record, so stop and clarify before saving a treatment said to be done. Send `head` as the number treated; omitting it uses the mob's recorded count, so check that default with the farmer first. `description` is a short title, for example "Drench rams".
- Put `route` on the treatment: `oral`, `injection`, `backline`, `jetting`, `dip`, `capsule`, `topical` or `in_feed_water`. Map the farmer's words only when unambiguous; otherwise ask. Each product accepts `name`, `active`, `batch`, `expiry` (`YYYY-MM-DD`), `dose`, `whp_days` and `esi_days`. Store route and expiry in those fields, not in notes. A missing value stays omitted or null, never the literal text "not recorded" in a date or number field.
- `dose` preserves the farmer's value, unit and basis, such as "15 mL per head" or "1 mL / 5 kg". When clearly stated, also send `dose_value`, `dose_unit` (`mL`, `L`, `g`, `kg`) and `dose_basis` (`per_head`, `per_kg`, `per_mob`). The server does not parse the numeric dose parts from `dose`; don't force a dose per 5 kg into a per-kg value without clarification. `drench_group` accepts the stated chemical group. Send `esi_days` equal to WHP only after confirming that no separate ESI applies; the server does not substitute it.
- Optional treatment fields are `equipment_cleaned` (boolean), `adverse_reaction` and `vet_authorisation` (text), plus `hgp_earmarked` when relevant and stated. Never fill absent fields with invented values or default "no".
- The server sets `operation_type: treatment`, `capture_source: agent`, `operator` from the signed-in user and `producer` from the property's owner; status and `created_as` follow the date. Do not send `broadcast`, `share_scope`, `operation_type: ai` or `rerun_ai`. If someone else treated, a confirmed `updateTask` can set that saved task's free-text `operator`. Notes or tags also use `updateTask` after saving; they do not set withholding dates. Don't fall back to `createTask` to bypass a refusal.
- After the farmer approves the summary, call with `confirm: true` on the first write. Without it the MCP guard refuses the call and asks for it again; that refusal is not permission to confirm without the farmer. Send the request body in the tool's advertised `body.data.attributes` shape, with `body.data.type: "treatment-record"` and treatment fields such as `category` and `products` inside `attributes`.
- If a write fails or times out, read the mob's completed records before retrying, so no duplicate is created. Check the actual saved `treatment.products`, not only the title. A 403 with `code: insufficient_access` is a real access refusal: show its `detail` and stop. Don't switch accounts, change permissions or try a different write route.

The response is the saved task, including its `treatment`. `treatment.safe_for_slaughter_on` and `treatment.export_eligible_on` are derived from the completion date and the longest applicable WHP/ESI among named products. Null means no derived date is recorded, not a safety clearance. These dates describe this record; the mob's current status can also reflect other completed treatment and husbandry records.

Without PurpleGrain, produce the same summary as an LPA treatment-record row the farmer can copy.

## 5. Read back

After saving, retrieve `getMob` and read its `withholding`, or use `getPropertyStatus` for the whole property's current status. `getTreatmentRegister` with `property_id` and `kind: "nvd"` reads the current NVD treatment list; apply any requested mob and date filters. Tell the farmer what was saved and the recorded withholding status in one or two lines. Missing dates or an empty NVD view do not prove compliance or clearance for sale or slaughter. If a recorded WHP or ESI is still running, report the actual dates and the NVD implications without inventing missing information.

## Limits

- This checks completeness and arithmetic. It is not veterinary or legal advice; label directions and the APVMA list are the authority.
- Never invent a batch number, expiry, WHP or ESI.
