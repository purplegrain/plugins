---
name: au-mob-feeding-records
description: "Check and save an Australian livestock feeding or introduced-fodder record. Use when stock are fed or when feed is bought in. Covers a commodity vendor declaration on bought fodder and the ruminant feed ban. Cutting or selling hay belongs to au-paddock-fieldwork-records."
---

# Australian feeding and fodder records

Version 1.0.0. Follow `pg-core`. If the mob does not exist, offer `pg-onboarding`. A cropping farm with no mob can attach the note to the paddock. Do not block a read.

There is no feed record in PurpleGrain. The schema gap was current on 24 Oct 2026. `createTask` with `operation_type: "feed"`, `capture_source: "agent"`, `status: "completed"`, `created_as: "record"`, the mob or paddock as the asset, and `producer` set to the business when the property belongs to one. All of the facts live in `description` and `record_notes`. The server will not calculate a withholding from this task. Say that.

`li-cvd-fodder` and `li-ram-ban` are not in this release. The rules below are the verified text those skills will be split from. Do not pretend a line item ran.

## Collect

LPA introduced stock-feed record and the livestock feeding record (livestock research, 23 Oct 2026, V, the ISC templates):

| Fact | Ask |
|---|---|
| Date received, or the dates fed (start and finish) | Yes |
| Feedstuff and amount | Yes |
| Origin or supplier | Yes when it was bought |
| Commodity vendor declaration: yes or no, and the reference | Yes when it was bought |
| Residue test, if they have one | Do not invent a result |
| Where it is stored | Yes |
| Which mobs | Yes |
| Who is responsible | Yes |

Home-grown feed does not need a CVD. The paddock's spray and seed-treatment records are the source. Point them at `getTreatmentRegister` for that paddock. Do not make them write a CVD for their own hay.

Bought hay or fodder: ask for the CVD. With no CVD, ISC states a 60-day withhold from when the stock eat the feed, and the risk assessment should be written down (23 Oct 2026, V). Put that in the notes as a reminder. It is not `getMob.withholding`. A 90-day export figure was not in the livestock or paddock research. Do not state it.

## Ruminant feed ban

ISC, same check (V): do not feed cattle, sheep or goats restricted animal material. The research names meat or bone meal, blood, fish, feather, poultry offal, dog biscuits and manure. If the feed description matches one of those, warn them and ask. Store restricted material separately from ruminant feed, and clean the equipment. State legislation behind the ban was not verified one Act at a time (U). Cite ISC, not a state Act you have not opened.

Do not block the save of a note that says they refused a load. If they are about to record that they fed one of those materials to cattle, sheep or goats, show the ISC rule and the date, and ask before saving. They may still record what already happened.

## Line items that do apply

| Line item | Applies when |
|---|---|
| `li-record-retention` | The task. LPA records: the longest of 3 years, while stock remain, and 7 years after sale |
| `li-operator-credential` | The person responsible, as a name. No spray licence |

`li-product-batch-expiry` does not fit. A feed bag batch can go in the notes. There is no product line on this task.

## Confirm, save, read back

```
Feed - Ewes, oaten hay bought from {supplier}, from {start} to {finish}
CVD: {ref or none}. If none: 60-day reminder from the last feed, not a mob withholding
RAM: not indicated
Save this note?
```

`confirm: true`. Do not send `broadcast` or `share_scope`. If the write fails, `listTasks` for that mob before retrying. This tool accepts `Idempotency-Key`.

Read the task back. Tell them the 60-day reminder is in the notes and that the mob's withholding object did not change because of feed.
