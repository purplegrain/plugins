---
name: au-farm-task-records
description: "Check and save a PurpleGrain farm task that is not a treatment, husbandry job, spray, sowing, fertiliser, field work, movement or feed record. Use for fencing and for an observation, including a prompt when the farmer describes a possible notifiable disease."
---

# Fencing and observations

Version 1.0.0. Follow `pg-core`. If they have no property yet, offer `pg-onboarding`. Do not block a read. Do not turn a fence or a note into a chemical record.

## Which task

| What they describe | `operation_type` | Asset |
|---|---|---|
| Fencing | `fence` | The paddock, if they named one |
| Something they saw | `observation` | The mob or the paddock they name. Omit the asset only if they truly have nowhere to put it, and say it is unassigned |

A product they gave is not an observation. Hand it to `au-mob-treatment-records` or `au-mob-husbandry-records`. A spray, sowing, fertiliser or harvest is that skill. Stock that moved are `au-stock-movement-records`.

## Save

`createTask` with `capture_source: "agent"`, `status: "completed"` when it already happened, `created_as: "record"`, and `producer` set to the business when the property belongs to one. `description` is their words, shortened only for a title. Extra detail stays in `record_notes`. `confirm: true`. Do not send `broadcast`, `share_scope` or `operation_type: ai`.

No observation line item shipped in this release. The hotline below is the prompt.

If they describe unusual sickness, sudden deaths, blisters, or nervous signs, do not diagnose and do not invent a treatment. Tell them the Emergency Animal Disease Hotline is 1800 675 888, or their local animal health office (sheep reference, checked 19 Oct 2026, E). Ask whether they want that sentence stored on the observation. Do not report the disease for them.

`li-record-retention` can stamp a keep-until note. A fence note or a general observation has no state chemical period, and no LPA period, unless the note is actually about stock, feed or a chemical. Otherwise do not invent a retention period.

`li-welfare-biosecurity-plan` is not in this release. Do not start a yearly welfare-plan interview from a fencing job. LPA Module 6 and Module 7 (a biosecurity plan and a welfare plan) are real obligations for an accredited PIC (sheep reference, 19 Oct 2026, E). Mention them only when the farmer asks what an auditor looks for, and do not create the plan in PurpleGrain. The ISC page read on 19 Oct 2026 said that from 1 September 2026 the biosecurity plan has to be in the LPA account. That date is past. Remind them the plan lives in the LPA account, not in this task.

## Confirm

`Fence - {paddock}, {what they did}. Save this note?`

`Observation - {what they saw}. Save this note?` If the hotline applies, put it in the checks line before the question.
