---
name: pg-tasks
description: "Check and save a PurpleGrain task for work that is still to do: a job to put on the list, a plan, a reminder, steps under a bigger job, or a job for a contractor. Not for work already done, which is a record and belongs to the record skills."
---

# Tasks: work still to do

Version 1.0.0. Follow `pg-core`. If they have no property yet, offer `pg-onboarding`. Do not block a read.

A task is the job in the farmer's words. It has no title, no due date and no priority. Do not ask for one, and do not invent one.

## Task or record

| What they describe | What it is |
|---|---|
| "I need to", "put it on the list", "remind me", "next week we'll", "get someone to" | A task. This skill |
| "I did", "we sprayed", "drenched them this morning" | A record. The skill for that job in `pg-core`'s table, not this one |
| A job planned for a paddock or mob that will need products or details when it is done (a spray, a drench, sowing) | A task now. The same record skill fills in the details when it is done. Do not collect a batch or a rate for a job that has not happened |
| Fencing or an observation that already happened | `au-farm-task-records` |

When it is not clear whether the work is done, ask once: "Is that done, or still to do?"

## What to collect

Only what they said. Ask for a missing item once, and save without it if they do not know.

| Item | Where it goes |
|---|---|
| The job | `description`, in their words. Keep a deadline they name ("by Friday", "before shearing") in the description. There is no date field for it |
| Where | The `asset` relationship: the paddock or mob they named, resolved to an id you read, never guessed. A job for the whole property has no asset. If two paddocks or mobs match the name, ask which |
| The property | The `property` relationship |
| Who owns it | `producer`: the business when the property belongs to one. Omitting it returns 403 "Unauthorized" |
| Steps | A bigger job with parts ("shear, then crutch the wethers, then drench") is one parent task and a sub-task for each part. Create the parent first, then each step with `parent` set to it. One level only: a step has no steps of its own |
| A contractor | `provider`. Setting it can email or text that contractor, so say so in the summary and wait for a yes. Use only a contractor you read from `listContractors`, `listLikedContractors` or `listClients`; never guess one from a name alone |
| Labels | `tags`, only ones they said |
| Photos | As `pg-core` describes |

Do not send `started_at` or `completed_at` on work that has not been done. Do not send `broadcast`, `share_scope` or `operation_type: ai`.

Several jobs in one message are several tasks. Summarise them together and save them one at a time.

## Save

`createTask` with `status: "pending"`, `created_as: "task"`, `capture_source: "agent"`, the relationships above, and `confirm: true` only after the yes. This tool accepts `Idempotency-Key`.

Read the saved task back and say what is on the list.

## Later

- Done: `updateTask` with `status: "completed"`. If they state when they started or finished, send `started_at` and `completed_at` as `pg-core` describes. If the job was a spray, a treatment or another typed record, follow that record skill for its details.
- Changed: `updateTask` with only what changed.
- Not happening: `updateTask` with `status: "cancelled"`. Delete only when they ask to delete.
- What is on the list: `listTasks` or `searchTasks` for the property, pending first. Nothing is overdue by a date, because there is no due date. Say when each was created.

## Confirm

`Task - {the job, in their words}. {Paddock or mob, or "whole property"}. Save this task?`

With steps: the parent line, then each step on its own line, then the question once.

With a contractor: add `This will notify {contractor}.` before the question.
