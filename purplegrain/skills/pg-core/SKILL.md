---
name: pg-core
description: "Use on the first PurpleGrain call in a conversation and before any PurpleGrain record is saved. Check whether the account is empty or only partly set up and offer pg-onboarding. Shared rules: confirm before a write, cite the source and the date it was last checked, and treat the result as records and reminders, not advice."
---

# PurpleGrain core

Version 1.1.0. Every PurpleGrain record skill follows this. It does not collect the fields of a drench, a spray or any other job, and it does not write those records.

## Disclaimer

These are records and reminders, not veterinary, legal or agronomic advice. The label on the pack, the APVMA permit and a vet's written direction are the authority for a chemical. Off-label use and Schedule 4 medicines belong to a vet. What to spray belongs to the label and the applicator.

Say that the skill asks for what the rules need and stores what the farmer confirmed. Do not say the record makes the farm compliant, and do not say "LPA approved".

## First call

On the first PurpleGrain call in a conversation, before answering a records question or writing anything:

1. `fetchCurrentUser` is the signed-in user.
2. `listBusinessMembers` with that user's id and `include: "organization"` is the businesses they belong to.
3. `listProperties` with no `organization_id` is personal properties only. A business's properties need that `organization_id`. For a named business, do not add personal properties or another business's properties unless the farmer asks.
4. Read onboarding metadata off that response (see below). If there is already a property and the question is about status, `getPropertyStatus` is the status call. Do not invent an id to call it.

Then:

- `status` `complete`: do not offer setup. Do the job they asked for.
- `not_started` or `in_progress`, or no properties, or a write that comes back with the same onboarding block: offer once. "Looks like you're new. Want me to set up your farm in about 5 minutes?" If they have already done some of it: "You've already got {what is done}. The next piece is {next step}. Want to do that now?"
- A no is a no for the rest of the conversation. Keep reading and, where the asset exists, keep recording. Offer a missing step again only when a write cannot be attached because that asset was never created.
- This is a suggestion. It is never a hard block on a read, and it is never a reason to refuse a record they can already attach to a property, paddock or mob.

If they say yes, follow `pg-onboarding` (version `pg-onboarding@1`). Do not invent a shorter setup.

Order when this text is not what the agent has open: the installed skill, then the connector prompt `setup-my-farm` or the resource `purplegrain://skills/pg-onboarding` (the same text), then the `agent_hint` on the metadata. The hint is a short fallback, not a substitute for the skill when the skill is loaded.

API #240 puts this block on responses. If a response has no block, the connector has not picked up that PR. Say you are inferring and follow the inference rules in `pg-onboarding`. Do not invent a tool name to fetch onboarding.

## Onboarding metadata

Read whichever of these the response actually has. Agents do not reliably see MCP `_meta`, so use the visible text or `structuredContent` when both exist. If copies disagree, follow the visible one and say so.

- JSON:API: top-level `meta.onboarding`, and `links.onboarding` when the response includes it
- Flat JSON: top-level `_meta.onboarding`
- The same object echoed in the tool's visible text or structured content

```json
{
  "status": "not_started | in_progress | complete",
  "completed_steps": ["create_team"],
  "next_step": "create_team | create_property | map_boundaries | map_paddocks | create_blocks | add_mobs | first_record",
  "skill": "pg-onboarding@1",
  "skill_url": "https://github.com/purplegrain/plugins/blob/main/purplegrain/skills/pg-onboarding/SKILL.md",
  "agent_hint": "plain-language instruction including short fallback steps"
}
```

`skill` should be `pg-onboarding@1`. That id is this repository's `purplegrain/skills/pg-onboarding/SKILL.md`, also listed in `purplegrain/CATALOGUE.md` and `purplegrain/skills/index.json`. `skill_url` is that file. If the server sends another URL, use it only when it is this same file. If the server names another skill version, say so and continue with the text you have. Do not invent `links.onboarding`.

`map_boundaries` sits between `create_property` and `map_paddocks`. A write that fails because there is no property or mob should carry this same block. When it does, offer `next_step`. When it does not, show the error that was actually returned.

## Which skill does the job

| What they describe | Skill |
|---|---|
| Set up the farm, add a property, PIC, parcels or a boundary, paddocks, mobs | `pg-onboarding` |
| A product given to a mob: drench, fluke, lice, fly, vaccine, antibiotic, pain relief on its own, pour-on, injection, jet or dip | `au-mob-treatment-records` |
| Marking, mulesing, docking, castration, dehorning, spaying, tagging, crutching, shearing, scanning, weaning, weighing | `au-mob-husbandry-records` |
| Crutch or shear with a chemical on the same day, or marking day with a vaccine and pain relief | `au-mob-husbandry-records` (one record, not also a treatment) |
| Herbicide, fungicide, insecticide, boom, spot, aerial, drone, knapsack | `au-spray-records` |
| Sowing or seeding a crop, including treated seed | `au-paddock-sowing-records` |
| Fertiliser spread, banded or drilled | `au-paddock-fertiliser-records` |
| Harvest, hay or silage cut, cultivate, slash, roll, burn, irrigate | `au-paddock-fieldwork-records` |
| Mob to another paddock on the same property, or a sale, agistment or move off the PIC | `au-stock-movement-records` |
| Feeding stock, or fodder bought in | `au-mob-feeding-records` |
| Fencing, or something they saw | `au-farm-task-records` |
| The register, an audit pack, or what is still not recorded | `au-compliance-export` |

A photo of a label or a paper sheet: read what is there, mark anything you cannot read as UNCLEAR, and confirm those values. Never guess a product, batch, rate, dose or interval.

## Shared rules for every record

**Confirm.** `confirm: true` only after the farmer has said yes to the summary. A yes to an earlier question is not a yes to the save. Show the summary again if a figure changes.

**One write per asset.** Three mobs are three records. One confirm can cover them when the product is shared; show head, batch or paddock differences as rows. A block is not a record.

**Ask in rounds.** Only missing fields, one or two a turn. Legal checks first, then LPA, then best practice. After two rounds, offer to save with the gaps listed. An unknown value stays unset and prints `not recorded`. Never invent a batch, expiry, dose, rate, withholding period, wind, head count, PIC or analysis.

**Line items.** A line item decides what to ask and what to flag for the fields it owns. It never calls a PurpleGrain write. The orchestrator is the only skill that creates the record. If a line item is not installed, still ask for the fields named in the orchestrator's table, and say the detailed check was skipped. Two line items do not write the same API field. The stricter verified rule wins (state over national, label over a default). Name which rule you applied.

**Unverified.** A point marked unverified is a warning. It must not block the save and must not be stated as the law. Only a verified legal rule may be put to the farmer as a reason to pause. They can still record what they already did.

**Intervals.** Never store a shorter withholding period than the label they are holding. If you calculate an end date, say which day you are using. Do not decide that a mob or paddock is clear by reading the new record. Read `getMob.withholding`, `getPaddock.withholding` or `getPropertyStatus`.

**Citing.** When you state a deadline, an age, an eID date or another regulatory figure, name the source and the date that source was last checked, from the line item. Do not replace that date with today.

**Voice.** Repeat a batch, a rate or a dose back before the confirm.

**Notes.** All six typed creates (`createTreatmentRecord`, `createHusbandryRecord`, `createSprayRecord`, `createSowingRecord`, `createFertiliserRecord`, `createFieldworkRecord`) accept `operator`, `record_notes` and `tags` in `body.data.attributes`. Send the confirmed operator, notes and tag array atomically with the typed record, not as a routine second write. An omitted or blank operator defaults to the signed-in user's display name; confirm who actually did the work. `createTask` and `updateTask` also accept these fields. If an older connector's schema lacks them, explain the limitation before saving; do not silently drop confirmed facts or create a second record. Read the saved task back. Correct an existing task with `updateTask` and `confirm: true` when needed. Notes do not set withholding dates. Tags do not either.

**Do not send** `broadcast`, `share_scope`, `operation_type: ai` or `rerun_ai`. Do not fall back to `createTask` to get around a refusal of a typed record. `create*Record` sets `capture_source: agent`, `producer` and `operation_type`. A plain `createTask` (feed, fence, observation, a sale note) must set `producer` to the business when the property is owned by a business. Omitting it returns 403 Forbidden, detail "Unauthorized". That is a missing producer, not a bad token.

**Access.** A 403 with `code: insufficient_access` is a real refusal. Show its `detail` and stop.

**Retries.** If a write errors or times out, read that asset's records before creating another. Send the same `Idempotency-Key` on a retry only when that tool's schema lists the header. Schemas reviewed on 24 Oct 2026 list it on `createTask`, `createTreatmentRecord`, `createHusbandryRecord`, `createSprayRecord`, and the sowing, fertiliser and fieldwork creates. `createProperty`, `createPaddock`, `createMob`, `createBlock` and `moveMob` do not. Do not send it on those.

**Duplicates.** After the asset is resolved, `listTasks` with `asset_id` and `filter_status: ["completed"]`. The next page is that tool's `page` parameter. Do not invent another paging name. Same day and same product, or the same husbandry procedures, is probably a duplicate: ask.

**Account.** Never guess an id. Creating a missing property, paddock or mob, or attaching a parcel, is `pg-onboarding` and needs its own confirm. Property `pic`, paddock `tenure` (`owned` or `leased`) and mob `species`, `stock_class`, `sex`, `birth_year` and `eid_status` are optional; unknown values stay unset. There is no mob `stock` field. Property `state` is derived from saved `place_label`, or `location` when that label is blank; never send an independent `state`. A paddock's `parcel_id` is the parcel already attached to the property (API #241), not a cadastre external id. Do not look a PIC up on WA Brands Search.
