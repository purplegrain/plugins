---
name: pg-onboarding
description: "Set up a PurpleGrain account in conversation: individual or organisation and team, properties with a PIC, parcel boundaries where the state has a cadastre, paddocks with tenure and blocks, mobs, then one real record. Use when the farmer wants the farm set up, or when pg-core finds onboarding not started or in progress. Version pg-onboarding@1. A suggestion, never a block on reading records."
---

# Set up the farm

Version `pg-onboarding@1` (skill version 1.1.0).

Follow `pg-core` for the disclaimer, the confirm rule and how to read metadata. This skill creates the account structure. The first real record is saved by the matching record skill, not by a dummy write here.

This sets up records. It is not legal, financial or farm-business advice. A PIC is private: leave the property `visibility` unset or `private`. Do not put a PIC on a public page, and do not look a PIC up on WA Brands Search.

The same text is what the connector should serve as the prompt `setup-my-farm` and the resource `purplegrain://skills/pg-onboarding`. The file those names must resolve to is `purplegrain/skills/pg-onboarding/SKILL.md` in this repository, listed in `purplegrain/CATALOGUE.md` and `purplegrain/skills/index.json`. Its public URL is `https://github.com/purplegrain/plugins/blob/main/purplegrain/skills/pg-onboarding/SKILL.md`.

API #240 is the onboarding guidance (`meta.onboarding` / `_meta.onboarding`, skill `pg-onboarding@1`). API #239 adds the nullable columns below. API #241 and #242 are the parcel search and the parcel picker. If a tool named here is missing from the connector, say that connector has not picked up the PR yet. Do not invent a replacement tool, and do not use WA Brands Search to fill the gap.

## How to resume

Read `meta.onboarding` or `_meta.onboarding` as `pg-core` describes. The server's `next_step` wins. Do not redo a step listed in `completed_steps` unless the farmer wants to change it.

| `next_step` | Step |
|---|---|
| `create_team` | 1. Individual or organisation, and the team |
| `create_property` | 2. Properties and PIC |
| `map_boundaries` | 2b. Parcels, or a drawn boundary. After the property, before paddocks |
| `map_paddocks` | 3. Paddocks, tenure, and areas |
| `create_blocks` | 3. Blocks, after the paddocks exist |
| `add_mobs` | 4. Mobs |
| `first_record` | 5. One real record |

If they jump ahead ("just add the ewes"), do that step, then offer the skipped ones. Do not refuse. If they ask to record a job and the mob or paddock already exists, record it and let setup wait. If it does not exist, create that asset with them (the step below) and then the record. Never block a read because setup is unfinished.

Offer in the farmer's words, one or two questions at a time. Confirm before each write (`confirm: true`). A yes to "keep going" is not a yes to a particular property, parcel, or invite.

### When the metadata is absent

#240 puts the block on responses. If this response has none, the connector has not picked up that PR. Say you are inferring. First incomplete step in this order:

1. `create_team` — you have not asked individual versus organisation.
2. `create_property` — the chosen owner has no property.
3. `map_boundaries` — a property has no attached parcel and no paddock, and it is not in a state where parcel search is unsupported.
4. `map_paddocks` — a property has no paddock, and they have not said it is one area.
5. `create_blocks` — paddocks exist and you have not asked whether any are grouped.
6. `add_mobs` — you have not asked about livestock.
7. `first_record` — structure exists and they have no completed record they confirmed in this setup.

Stop inferring a step the farmer has already answered in the conversation.

## Step 1 — Individual or organisation, and the team

Ask: "Is this farm just you, or a business with other people on it?"

**Just them.** Properties will sit on the personal account (`listProperties` with no `organization_id`, and `createProperty` with no organisation). Do not create a business.

**A business.** If they already belong to one, ask which business these records are for. Do not create a second one for the same farm. If none fits: "What name should the business have in PurpleGrain?" Then `createBusiness` with that `name` only after they confirm. Leave `slug` unset.

Then: "Anyone else who should see the records? An email or mobile is enough. Should they be able to edit records (manager) or only look (viewer)?"

`createBusinessMember` with the organisation, `permission` of `manager` or `viewer` (or `admin` or `contractor` if that is the word they used), and `invited_email` or `invited_mobile`. Tell them an invite sends a message, and wait for the yes. Do not set the invite `status` to `accepted`. Do not offer `owner` for someone else.

"Just me for now" completes the invite part.

### Done when

Pass if `completed_steps` contains `create_team`, or all of these are true:

- They have said individual, or a business has been chosen or created.
- For a business, invites were sent or they said nobody else yet.

Fail while you have not asked individual versus organisation. A signed-in user is not this step.

## Step 2 — Properties and PIC

Ask: "What's the first property called?" Then: "What's its PIC? It's on your LPA or NLIS paperwork. We can leave it if you don't have it handy." Then: "What's its address, including the state?" Then: "Any other property, including country you lease?"

Do not check the PIC against a pattern. There is no format check in this skill. If they are unsure, ask them to read it again. Do not reject it. Do not look a PIC up on WA Brands Search, or on any other public register. The PIC is what they read to you.

`createProperty` with `name`, on the personal account or the chosen organisation. Send `pic` when they gave one. #239 and #240 add `pic` as a nullable column. Omit it when they do not have it; null is "not recorded". Do not put the PIC in `location` or `place_label`. `location` may hold the town-and-state caption they want shown ("Currawarna NSW"). Say that caption is not the PIC.

The server derives read-only `state` from saved `place_label`, or from `location` when `place_label` is blank. Save the address they confirmed in `place_label` (or their town-and-state caption in `location`), then read the returned state. Do not ask for or send an independent `state` field, and do not infer it from a PIC or a map point. If the address is unknown, leave it unset and say parcel search needs a saved address naming the state. If `createProperty` rejects `pic` as an unknown attribute, the connector has not picked up the column. Create the property with the name, keep the PIC in the conversation, and say it is not on this connector yet.

`visibility` stays unset or `private`.

One confirm per property: "Create '{name}' at {address or not recorded}, PIC as you read it, on {owner}?"

### Done when

Pass if `completed_steps` contains `create_property`, or:

- At least one property exists for the owner they chose, and
- For every property created or claimed in this setup, you asked for the PIC and the address, and the PIC is either stored or explicitly left unset.

Fail while the chosen owner has no property and they have not said they will add one later. "Later" pauses setup. It does not fail the account.

## Step 2b — Boundaries (`map_boundaries`)

Do this after the property exists and before paddocks. For each property, one of these finishes the step: a parcel is attached, the property already has paddocks, or the property is in a state with no parcel search. The step is done when every property in this setup meets one of those.

Read the property's server-derived `state` before you search. If it is missing, ask for a corrected address, confirm an `updateProperty` of `place_label` or `location`, and read the property back. A search address or point does not set the property's state. Supported cadastres: NSW, VIC, QLD, TAS. SA, WA, NT and ACT return `422` `parcel_search_unsupported`. Do not call `searchParcels` for those four. Tell them parcel search does not cover that state, and offer a drawn outline with `updatePropertyBoundary`. That offer completes the step for an unsupported state even if they draw it later.

### Search and attach

For NSW, VIC, QLD or TAS, ask for a street address or a point on the property. `searchParcels` is `GET /api/v1/properties/{property_id}/parcel-search` with `address`, or with `latitude` and `longitude`. If they give both, send the point and not the address: the point wins.

Show the parcels the tool actually returned, in their words (lot, address, area, whatever fields came back). Ask which ones are theirs. They can pick more than one.

`attachParcelsToProperty` is the POST. Send `external_ids` only, the ids from that search, and `confirm: true`. Do not send a different id field. Then `listPropertyParcels` and read the names back.

A wrong parcel comes off with `deletePropertyParcel` and `confirm: true`.

If `searchParcels` is not on the connector, say so. Offer `updatePropertyBoundary`. Do not scrape a cadastre site, and do not use WA Brands Search.

### When search fails

Match the `code`. Do not retry the same call unchanged.

| `code` | What to do |
|---|---|
| `parcel_search_state_required` | Ask for the property's address including its state. Confirm and save the corrected `place_label` (or `location` when no `place_label` is set) with `updateProperty`, then read its derived `state` before searching again. A search address or point alone cannot repair this. Do not send a `state` attribute. |
| `parcel_search_unsupported` | SA, WA, NT or ACT. Stop searching. Offer `updatePropertyBoundary`. |
| `parcel_geocode_unavailable` | The address lookup is down. Ask for a latitude and longitude, or leave the boundary for later. Do not invent a point. |
| `parcel_geocode_failed` | That address did not geocode. Ask them to say it again, or give a point. |
| `parcel_search_query_required` | Neither an address nor a point was sent. Ask for one. |
| `parcel_search_query_invalid` | Show the error. Ask them to restate the address or the point. Do not guess a correction. |
| `parcel_search_unavailable` | The cadastre service is down. Offer a drawn boundary, or a later search. Do not block the rest of setup. |
| `parcel_ids_required` | Attach was sent with no `external_ids`. Ask which parcel, then send those ids. |
| `parcel_not_in_search` | `409`. That external id was not in the latest search for this property. Search again and attach only an id from the new result. |

### Drawing the outline

`updatePropertyBoundary` saves the ring. `boundary` is an array of rings. Each ring is `[longitude, latitude]` pairs, longitude first, at least four positions, first point repeated at the end. It is not a GeoJSON object. `confirm: true`.

Send `area_source: "drawn"` when the ring should set the hectares. Send `area_source: "typed"` when they already gave a hectare figure they want kept. Do not invent a ring, a coordinate, or a hectare figure. If they cannot read coordinates in the chat, tell them the outline is drawn on the property map in PurpleGrain, and leave the boundary unset. `boundary_source` is `traced`, `grid`, `gps` or `imported`, and only when they told you how the ring was captured. Do not send `boundary_captured_by`.

### Done when

Pass if `completed_steps` contains `map_boundaries`, or every property in this setup has an attached parcel, or already has a paddock, or is in SA, WA, NT or ACT and you have told them search does not cover it.

Fail while a property in NSW, VIC, QLD or TAS has no parcel and no paddock, and they have not deferred the boundary. "Later" pauses this step. It does not fail the account.

## Step 3 — Paddocks, tenure and blocks

`next_step` splits this into `map_paddocks` and `create_blocks`. Do the paddocks first.

Ask: "What do you call the paddocks or areas on {property}? Hectares is enough, and whether you own or lease each one." If they run it as one area: "I'll add one paddock for the whole property. What should it be called, and about how many hectares?"

`createPaddock` with `name`, `area_ha` when they gave it, and `area_source: "typed"` when the hectares were spoken. `land_use` (`cropping`, `grazing`, `mixed`, `fallow`) only when they said it. Do not infer it.

#239 adds nullable `tenure` on the paddock. Send `owned` or `leased` as they said. Leave `tenure` unset when they do not know. Do not send any other tenure value. If the connector rejects `tenure`, create the paddock without it and say this connector has not picked up the column.

#241 adds `paddocks.parcel_id`. When they say a paddock sits on one parcel already attached, set `parcel_id` to that parcel's id from `listPropertyParcels`. That id is the parcel on the property, not the `external_id` you sent to attach. Omit `parcel_id` when the paddock is not on a single attached parcel. If create rejects `parcel_id`, set it with `updatePaddock`.

A name is enough to create a paddock. Area can be "not recorded".

Then ask: "Do you group any of those into blocks — an outblock across the road, an irrigation farm, or just a name for a group? If not, they stay in the home block."

`createBlock` needs `property_id`, `name`, `kind` and the `paddock_ids`. Map their words:

| Their words | `kind` |
|---|---|
| Across the road, a separate parcel of country, an outblock | `outblock` |
| An irrigation farm | `irrigation_farm` |
| A name for a group, and neither of the above | `management` |

"Parcel" in that table is their word for a block of country. It is not a cadastre parcel and it does not call `attachParcelsToProperty`.

If you use `management` because they only gave a name, tell them that is the label you used. A paddock left out stays in the home block. Grouping does not write, move or remove a record. A paddock is in one block; naming it on a new block moves it.

`getProperty` lists blocks. `listPaddocks` with `property_id` shows each paddock's `block_id`. Read that back in names, not as a test they have to pass.

### Done when

`map_paddocks` passes if `completed_steps` contains it, or every property in this setup has at least one paddock (a single whole-property paddock counts) and you asked owned or leased for each.

`create_blocks` passes if `completed_steps` contains it, or they said there are no blocks, or every block they named exists and they confirmed which paddocks are in it.

Fail `map_paddocks` while a property they are setting up has no paddock and they have not deferred it. Fail `create_blocks` while you have not asked the block question. Do not mark blocks done just because the home block exists. The home block is the default, and the question still has to have been asked.

## Step 4 — Mobs

Ask: "What mobs are on {property}? For each one: the name you use, the species, the class (ewes, weaners, steers), how many head, and which paddock they're in." Then: "Are they on electronic NLIS tags, visual tags, or not tagged yet?"

No livestock: "No stock is fine. We'll skip mobs and record a paddock job instead." That completes this step.

`createMob` with `name` and `head_count` when they gave a count. Optional stock fields are `species` (`sheep`, `cattle`, `goat`), `stock_class` (their free-text class, such as `Merino ewes`), `sex` (`female`, `male`, `mixed`), `birth_year` (an integer from 1901 to 2100) and `eid_status` (`visual`, `eid`, `device_free`). Send only values they supplied and confirmed; unknown values stay unset. Do not send `stock`, `class` or `breed`, and do not infer sex or birth year from a name or class. Names are unique per property, including archived mobs. A new mob is not in a paddock until `moveMob`.

If a connector does not expose these optional fields, explain what cannot be stored and confirm a name-and-count-only create before proceeding. Do not rename the mob to hide unstored fields, and read it back before claiming they were saved.

`eid_status` records the identification status they state. Do not map "not tagged yet" to `device_free`; that is a distinct status and must be confirmed. Offer an eID tagging record later through `au-mob-husbandry-records` when they want to record actual tagging work. Neither saving the mob's status nor a tagging record writes the NLIS database.

`moveMob` places the mob: the mob's id, `to_paddock`, `capture_source: "agent"`, and `completed_at` only when they are recording a past move. The destination has to be a live paddock on the same property. If they do not know the paddock, leave the mob unplaced and say so. Its own confirm: "Put {mob} in {paddock}?"

### Done when

Pass if `completed_steps` contains `add_mobs`, or:

- At least one mob exists and you asked species, class, head count, paddock and NLIS or eID status, and you placed it or they left it unplaced on purpose, or
- They said there is no livestock.

Fail while you have not asked and they have not said they have no stock. A missing head count they do not know is "not recorded", not a failure.

## Step 5 — First real record

Ask: "What's the last job you actually did — a drench, a spray, a sowing, a move, something else? We'll record that one. I won't make a test record just to finish setup."

Hand the job to the skill in `pg-core`'s table. That skill collects the regulatory fields, confirms, saves and reads back. This step is done only when that record exists, they confirmed it, and you read back the withholding or the register row (or, for a record with no withholding, the saved task).

If they do not want to record anything today, leave `first_record` open and stop. Setup can pause. Do not invent a record. `status` stays `in_progress` until a real record is saved. They can still use the account.

### Done when

Pass if `completed_steps` contains `first_record`, or a completed record from this conversation is on the asset and you read it back.

Fail if the only "record" is a placeholder, a cancelled write, or a summary they have not confirmed.

## After the last step

When all seven of `create_team`, `create_property`, `map_boundaries`, `map_paddocks`, `create_blocks`, `add_mobs` and `first_record` are done, say the farm is set up and name what is still not recorded (PIC, hectares, a batch). Do not call it compliant. If the server still says `in_progress`, tell them what `next_step` is and do that, or show them the disagreement.

## Writes, in one place

| Step | Tool | Confirm shows |
|---|---|---|
| Business | `createBusiness` | The name |
| Invite | `createBusinessMember` | Email or mobile, and the permission. Say that a message is sent |
| Property | `createProperty` | Name, saved address or caption, `pic` as read, owner |
| Find parcels | `searchParcels` | Address, or the point. No confirm; it is a read |
| Parcels on the property | `listPropertyParcels` | A read |
| Attach parcels | `attachParcelsToProperty` | The parcels, by the labels from the search. `external_ids` only |
| Remove a parcel | `deletePropertyParcel` | Which parcel is coming off |
| Draw the outline | `updatePropertyBoundary` | That you are saving a ring they supplied, or that you are not inventing one |
| Paddock | `createPaddock` | Name, hectares, `tenure` (`owned` or `leased`), `parcel_id` when it sits on one attached parcel |
| Block | `createBlock` | Name, kind, paddock names |
| Mob | `createMob` | Name, head and the optional species, class, sex, birth year and identification status they supplied |
| Place a mob | `moveMob` | Mob and paddock |

Read the created property, paddock or mob back before telling them `pic`, `tenure` or the optional mob fields were stored. If a write times out, list that owner's properties, paddocks or mobs before retrying. Do not send `Idempotency-Key` on these tools, or on the parcel tools. The schemas reviewed for the account tools do not have it, and #241/#242 do not add it.
