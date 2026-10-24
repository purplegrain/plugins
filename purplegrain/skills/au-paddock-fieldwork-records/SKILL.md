---
name: au-paddock-fieldwork-records
description: "Check and save Australian paddock field work before writing it to PurpleGrain. Use for harvest, cutting or baling hay or silage, cultivation, slashing, rolling, burning or irrigation. Includes the facts a seller needs for a commodity vendor declaration. Bought-in feed belongs to au-mob-feeding-records."
---

# Australian paddock field work

Version 1.0.0. Follow `pg-core`. If the paddock does not exist, offer `pg-onboarding`. Do not block a read.

Field work has no withholding of its own and does not change a paddock's status. The server still checks harvest and hay against withholding already on the paddock. Read `warnings` on the response and tell the farmer. A warning does not block the write.

This is a record. It is not agronomy or fire advice.

## 1. Fields

`kind`: `cultivate`, `harvest`, `hay_silage`, `slash`, `roll`, `burn`, `irrigate`.

| Kind | Store | Do not send |
|---|---|---|
| `harvest` | `outcomes.harvest`: `crop`, `tonnes`, `yield_t_ha`, `moisture_pct`, `protein_pct`, `grade` | Hay or irrigation keys |
| `hay_silage` | `outcomes.hay_silage`: `bales`, `bale_type` | Harvest keys |
| `irrigate` | `outcomes.irrigate.ml` | |
| `cultivate`, `slash`, `roll`, `burn` | `implement`, `area_ha` | An outcomes block the kind does not carry. Extra figures are refused |

`area_ha` defaults to the paddock. A product such as a hay preservative is optional. Its batch and expiry use `li-product-batch-expiry`. Its rate needs a unit.

## 2. Line items

| Line item | Applies when |
|---|---|
| `li-grazing-harvest-whp` | Harvest, or hay and silage. Use the paddock withholding and the server `warnings`. Do not recalculate a shorter date |
| `li-state-chem-record-rules` | A stored-grain chemical, or a product on the job. NT stored-grain treatment is a record (23 Oct 2026, V). Do not claim that for every state |
| `li-product-batch-expiry` | A product line |
| `li-operator-credential` | Who did the job. A spray credential is not the usual question for cultivation |
| `li-record-retention` | After the save |

Not in this release: `li-harvest-mrl-check`, `li-cvd-generator`, `li-burning-permit`, `li-irrigation-water-meter`. The judge deferred the permit and meter items because the rules were not verified. Keep them as prompts.

## 3. Prompts that are not hard rules

**Harvest and hay.** If `warnings` says a harvest withholding or a grazing withholding is still running, tell them in the words the warning uses. Do not say the grain meets a buyer's MRL. Australian MRLs are not an importing country's limit. Grain Trade Australia tables were not verified (23 Oct 2026, U).

**Selling hay, silage, grain or a by-product as stock feed.** The seller completes a commodity vendor declaration from the paddock records (ISC, paddock research, 23 Oct 2026, V). This skill does not fill in the form. Read `getTreatmentRegister` for the paddock (`kind: "spray"` and `kind: "paddock-inputs"`) and list the products, dates and intervals so they can copy them. A buyer with no declaration applies a 60-day withhold from when stock last ate that feed (livestock research, 23 Oct 2026, V). A 90-day export figure in later strategy notes was not in that research. Do not state it.

**Burning.** Permit rules were not verified state by state (23 Oct 2026, U). Ask whether they needed a permit and, if they have a number, put it in `record_notes`. Do not assert that a permit was required, and do not quote a fire-service phone number from memory.

**Irrigation.** Metering rules were not verified (U). Store the megalitres in `outcomes.irrigate.ml`. Licence or meter numbers they offer go in `record_notes`. Do not assert that a meter was legally required.

**Cultivation on native grassland or a steep bank.** Do not assert a clearing breach. If they ask, say the rules were not verified here and the local land or catchment body is the place to check.

## 4. Confirm, save, read back

```
Harvest - North, barley, 18/11/26
399 t, 4.2 t/ha, moisture as stated, grade as stated
Checks: server warning, or none
Save this record?
```

`createFieldworkRecord`: `paddock_id`, `confirm: true`, `body.data.type: "fieldwork-record"`. The server sets `operation_type: fieldwork` and `capture_source: agent`. This tool accepts `Idempotency-Key`. Notes follow `pg-core`. If the write fails, read the paddock's records before retrying.

Tell them the warnings, if any, and that the paddock status did not change because of this record.
