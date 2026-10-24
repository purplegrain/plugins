---
name: pg-onboarding
description: "Set up a PurpleGrain account in conversation: individual or organisation and team, properties with PIC and state, paddocks or leased areas and blocks, mobs, then one real record. Use when the farmer wants the farm set up, or when pg-core finds onboarding not started or in progress. Version pg-onboarding@1. A suggestion, never a block on reading records."
---

# Set up the farm

Version `pg-onboarding@1` (skill version 1.0.0).

Follow `pg-core` for the disclaimer, the confirm rule and how to read metadata. This skill creates the account structure. The first real record is saved by the matching record skill, not by a dummy write here.

This sets up records. It is not legal, financial or farm-business advice. A PIC is private: leave the property `visibility` unset or `private`. Do not put a PIC on a public page.

The same text is what the connector should serve as the prompt `setup-my-farm` and the resource `purplegrain://skills/pg-onboarding`.

**Not confirmed (24 Oct 2026).** Those prompt and resource names are the onboarding spec of that date. The connector reviewed the same day did not advertise them. No separate onboarding tool names were in that spec or in the connector. Use the tools named below. If a later connector tool's description says it is the onboarding step for team, property, paddock, block or mob, prefer that tool and still collect the same facts. Do not invent a tool name.

## How to resume

Read `meta.onboarding` or `_meta.onboarding` as `pg-core` describes. The server's `next_step` wins. Do not redo a step listed in `completed_steps` unless the farmer wants to change it.

| `next_step` | Step |
|---|---|
| `create_team` | 1. Individual or organisation, and the team |
| `create_property` | 2. Properties, PIC and state |
| `map_paddocks` | 3. Paddocks and areas, owned or leased |
| `create_blocks` | 3. Blocks, after the paddocks exist |
| `add_mobs` | 4. Mobs |
| `first_record` | 5. One real record |

If they jump ahead ("just add the ewes"), do that step, then offer the skipped ones. Do not refuse. If they ask to record a job and the mob or paddock already exists, record it and let setup wait. If it does not exist, create that asset with them (the step below) and then the record. Never block a read because setup is unfinished.

Offer in the farmer's words, one or two questions at a time. Confirm before each write (`confirm: true`). A yes to "keep going" is not a yes to a particular property or invite.

### When the metadata is absent

**Not confirmed (24 Oct 2026).** The live responses reviewed that day had no onboarding block. Infer, and say you are inferring. First incomplete step in this order:

1. `create_team` — you have not asked individual versus organisation.
2. `create_property` — the chosen owner has no property.
3. `map_paddocks` — a property has no paddock, and they have not said it is one area.
4. `create_blocks` — paddocks exist and you have not asked whether any are grouped.
5. `add_mobs` — you have not asked about livestock.
6. `first_record` — structure exists and they have no completed record they confirmed in this setup.

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

## Step 2 — Properties, PIC and state

Ask: "What's the first property called?" Then: "What's its PIC? It's on your LPA or NLIS paperwork. We can leave it if you don't have it handy." Then: "Which state is it in?" Accept NSW, VIC, QLD, SA, WA, TAS, NT, ACT. Then: "Any other property, including country you lease?"

Do not check the PIC against a pattern. There is no confirmed format in this skill. If they are unsure, ask them to read it again. Do not reject it.

`createProperty` with `name`, on the personal account or the chosen organisation. Send `pic` and `state` on that create when the tool accepts them. That is the agreed contract.

**Not confirmed (24 Oct 2026).** `createProperty` reviewed that day accepts `name`, `location`, `size`, `place_label` and a centroid. It does not list `pic` or `state`. If the tool or the API rejects those attributes, create the property with the name, read it back, and tell them the PIC and state are not stored yet. Keep both in the conversation so they can be written when the field exists. Do not put the PIC in `location` or `place_label`. `location` may hold a town they want shown. Say that is not the PIC.

`visibility` stays unset or `private`.

One confirm per property: "Create '{name}' in {state}, PIC as you read it, on {owner}?"

### Done when

Pass if `completed_steps` contains `create_property`, or:

- At least one property exists for the owner they chose, and
- For every property created or claimed in this setup, you asked for the PIC and the state, and each is either stored or explicitly left as not recorded.

Fail while the chosen owner has no property and they have not said they will add one later. "Later" pauses setup. It does not fail the account.

## Step 3 — Paddocks, leased areas and blocks

`next_step` splits this into `map_paddocks` and `create_blocks`. Do the paddocks first.

Ask: "What do you call the paddocks or areas on {property}? Hectares is enough, and whether you own or lease each one." If they run it as one area: "I'll add one paddock for the whole property. What should it be called, and about how many hectares?"

`createPaddock` with `name`, `area_ha` when they gave it, and `area_source: "typed"` when the hectares were spoken. `land_use` (`cropping`, `grazing`, `mixed`, `fallow`) only when they said it. Do not infer it.

Owned or leased has no field on the schema reviewed on 24 Oct 2026. Do not send `tenure` or `leased`. Remember it in the summary you show them. There is nowhere on the paddock to store it until a field exists. Say that.

A name is enough to create a paddock. Area can be "not recorded".

Then ask: "Do you group any of those into blocks — an outblock across the road, an irrigation farm, or just a name for a group? If not, they stay in the home block."

`createBlock` needs `property_id`, `name`, `kind` and the `paddock_ids`. Map their words:

| Their words | `kind` |
|---|---|
| Across the road, a separate parcel, an outblock | `outblock` |
| An irrigation farm | `irrigation_farm` |
| A name for a group, and neither of the above | `management` |

If you use `management` because they only gave a name, tell them that is the label you used. A paddock left out stays in the home block. Grouping does not write, move or remove a record. A paddock is in one block; naming it on a new block moves it.

`getProperty` lists blocks. `listPaddocks` with `property_id` shows each paddock's `block_id`. Read that back in names, not as a test they have to pass.

### Done when

`map_paddocks` passes if `completed_steps` contains it, or every property in this setup has at least one paddock (a single whole-property paddock counts) and you asked owned or leased for each.

`create_blocks` passes if `completed_steps` contains it, or they said there are no blocks, or every block they named exists and they confirmed which paddocks are in it.

Fail `map_paddocks` while a property they are setting up has no paddock and they have not deferred it. Fail `create_blocks` while you have not asked the block question. Do not mark blocks done just because the home block exists. The home block is the default, and the question still has to have been asked.

## Step 4 — Mobs

Ask: "What mobs are on {property}? For each one: the name you use, the species, the class (ewes, weaners, steers), how many head, and which paddock they're in." Then: "Are they on electronic NLIS tags, visual tags, or not tagged yet?"

No livestock: "No stock is fine. We'll skip mobs and record a paddock job instead." That completes this step.

`createMob` with `name` and `head_count` when they gave a count. Send `species` and `class` when the tool accepts them. That is the agreed contract. Names are unique per property, including archived mobs. A new mob is not in a paddock until `moveMob`.

**Not confirmed (24 Oct 2026).** `createMob` reviewed that day has `name`, `head_count` and `archived` only. Its description says there are no species, class or breed fields yet, and to put those in the name. If `species` or `class` is rejected, create the mob with the name and head count, put the species and class in the name ("Merino ewes"), and tell them there is no species field on the mob yet. Do not send `breed`, `sex` or `birth_year`. Those names are not in the agreed onboarding contract.

NLIS or eID status has no mob field in that schema, and a mob has no notes field there. Keep the answer for the summary. Offer an eID tagging record later through `au-mob-husbandry-records` if they want it stored. Do not pretend `createMob` wrote the NLIS database.

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

When all six of `create_team`, `create_property`, `map_paddocks`, `create_blocks`, `add_mobs` and `first_record` are done, say the farm is set up and name what is still not recorded (PIC, hectares, a batch). Do not call it compliant. If the server still says `in_progress`, tell them what `next_step` is and do that, or show them the disagreement.

## Writes, in one place

| Step | Tool | Confirm shows |
|---|---|---|
| Business | `createBusiness` | The name |
| Invite | `createBusinessMember` | Email or mobile, and the permission. Say that a message is sent |
| Property | `createProperty` | Name, state, PIC as read, owner |
| Paddock | `createPaddock` | Name, hectares, owned or leased (lease is not stored yet) |
| Block | `createBlock` | Name, kind, paddock names |
| Mob | `createMob` | Name, species, class, head |
| Place a mob | `moveMob` | Mob and paddock |

Read the created property, paddock or mob back before telling them a contract field was stored. If a write times out, list that owner's properties, paddocks or mobs before retrying. Do not send `Idempotency-Key` on these tools. The schema reviewed on 24 Oct 2026 does not have it.
