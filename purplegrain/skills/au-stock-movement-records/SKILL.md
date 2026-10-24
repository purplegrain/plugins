---
name: au-stock-movement-records
description: "Check and save an Australian stock movement. Use when a mob moves to another paddock on the same property, or when stock are sold, agisted or leave the PIC and the NVD, NLIS and health-declaration facts need recording. An on-property move uses moveMob. An off-property movement has no dedicated PurpleGrain record yet."
---

# Australian stock movements

Version 1.0.0. Follow `pg-core`. If the mob or the destination paddock does not exist, offer `pg-onboarding`. Do not block a read.

This skill does not update the NLIS database and does not fill in an NVD. It records what the farmer said, and it shows withholding rows they must not ignore.

## 1. On the same property

`moveMob` only. Destination: a live paddock on the mob's own property, not the paddock it is already in. `capture_source: "agent"`. `completed_at` when they are writing a past move. `confirm: true` after they agree the mob and the paddock.

The origin is worked out by the server. The first move of a mob that has never been placed has no "from". Back-dating a move behind a newer one files the diary entry and leaves the current paddock where the newest completed record says it is. Say that if they are back-dating.

Do not ask for an NVD for a paddock-to-paddock move. `li-eid-tagging` does not block an on-property move.

If the write fails, `listMobs` or `getMob` before retrying. Do not send `Idempotency-Key`. The schema reviewed on 24 Oct 2026 does not have it.

## 2. Off the PIC

There is no off-property movement record and, on the schema reviewed 24 Oct 2026, no PIC on the property. Do not call `moveMob` for a sale or agistment. That would place the mob in a paddock. Do not set `operation_type` to `move_stock` on a task. That type is the on-property move.

Store a plain task: `createTask`, asset the mob, `producer` set to the business when the property belongs to one, `capture_source: "agent"`, `status: "completed"`, `created_as: "record"`, description such as "Sale of ewes", and the facts in `record_notes`. `confirm: true`. Tell them this did not transfer the stock on NLIS and did not move the pin on the map.

`li-nlis-movement` and `li-health-declaration` are not in this release. Collect the following anyway, and say the full skills are not installed.

| Fact | Where |
|---|---|
| Date, head | Notes, and the task date |
| Destination PIC, NVD or waybill serial | Notes. Do not invent a serial |
| Transporter, if they know | Notes |
| Whether the NLIS database was updated, and when | Notes. The receiver does that update. This task does not |
| Withholding still running | Read `getTreatmentRegister` `kind: "nvd"` for the mob. Show the rows. Do not answer the NVD for them. An empty list is not a declaration |
| eID | `li-eid-tagging` |

Sheep and goat property-to-property movements recorded on NLIS within 2 days: verified for South Australia and NSW (livestock research, 23 Oct 2026, V). Do not say every state. Cattle: electronic identification is national. The "receiver updates within 48 hours" line was not verified (U). Do not state it.

A wool-declaration code is not collected again here. `li-nwd-status` is not in this release. If they are selling wool, use the code already in the husbandry notes (`li-welfare-sheep-mulesing`). Do not assign one.

Health declarations, from the October 2024 National Sheep Health Declaration form note (sheep reference, 19 Oct 2026, E): mandatory for sheep movements in South Australia and for sheep moved into NSW and Tasmania. Voluntary elsewhere on that form. SA says failing to provide it is an offence. Prefer the form note, and tell them to check the destination. Section C (recent treatments) can be read from this mob's treatment records. Do not invent footrot, lice or Johne's answers. Section B answers go in the notes only when they state them.

National Cattle Health Declaration states, and the Goat Health Declaration, were not verified (23 Oct 2026, U). Ask whether the destination asked for one. Do not say it is mandatory.

## 3. Line items and retention

| Line item | Applies when |
|---|---|
| `li-eid-tagging` | Sheep or goats leaving the property, or an `eid_tag` job tied to the move |
| `li-record-retention` | The task. NVD: LPA Rules 11.7 say 3 years or while stock remain, and the ISC page says 7 years after sale. Keep the longest and cite both |
| `li-operator-credential` | Who organised the move, only if they want a name on the note |

## 4. Confirm

On property: `Move {mob} from {paddock or unplaced} to {paddock} on {date}?`

Off property: list destination PIC, NVD serial, head, any withholding still open, and the sentence "This does not update NLIS." Wait for a yes.

Read `getMob` afterwards. For a paddock move, `current_paddock_id` should match. For a sale note, the mob's paddock should be unchanged. Say so.
