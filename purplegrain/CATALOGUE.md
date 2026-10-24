# Skill catalogue

Version of this list: 24 October 2026. Machine-readable copy: [skills/index.json](skills/index.json). Each folder is one installable zip (`dist/<name>.zip`). Line items do not write to PurpleGrain. The record skill writes, once per mob or paddock, after `confirm: true`.

These are records and reminders, not veterinary, legal or agronomic advice. A point marked unverified in a skill is a warning, not a block. Sources and last-checked dates are in the skill.

`pg-onboarding` is version `pg-onboarding@1`.

## Core

| Skill | Version | What it does |
|---|---|---|
| `pg-core` | 1.0.0 | First PurpleGrain call. Offers setup when the account is empty or partial. Confirm, citations, disclaimer. |
| `pg-onboarding` | 1.0.0 (`pg-onboarding@1`) | Five setup steps. Resumes from `completed_steps` and `next_step`. A suggestion, never a block on a read. |

## Line items shipped (the P0 set)

Sixteen. The judge's review said to start near fifteen and leave per-state variants and the rest until there is demand. State differences that are already verified sit inside `li-state-chem-record-rules`, `li-spray-weather` and `li-eid-tagging`, not in separate state skills.

| Skill | Severity | Owns |
|---|---|---|
| `li-product-batch-expiry` | lpa | `products[].batch`, `products[].expiry` (no expiry on fertiliser) |
| `li-withholding-meat-esi` | legal | Meat WHP, ESI, wool and milk on a treatment or husbandry product |
| `li-grazing-harvest-whp` | legal | Grazing and harvest WHP, do-not-graze, seed-treatment grazing WHP |
| `li-dose-liveweight` | lpa | Dose and approximate live weight (weight has no field) |
| `li-spray-rate-tank-mix` | legal | One spray line each, rate with a unit |
| `li-operator-credential` | legal | `operator`, phone and credential in notes |
| `li-adverse-reaction` | lpa | `adverse_reaction` |
| `li-off-label-vet` | legal | `vet_authorisation` |
| `li-state-chem-record-rules` | legal | Deadline and extra spray fields. Tasmania retention unconfirmed |
| `li-spray-weather` | legal | `weather_readings` |
| `li-buffer-drift` | legal | No-spray zone, droplet category, neighbour drift |
| `li-record-retention` | legal | Keep-until. Longest of state, LPA 3 years, ISC 7 years |
| `li-welfare-sheep-mulesing` | legal | Sheep mulesing age and pain relief. Sheep-standards adoption unverified except Tasmania's regulation |
| `li-welfare-sheep-dock-castrate` | legal | Docking and castration. Same adoption limit |
| `li-eid-tagging` | legal | Sheep and goat eID dates. WA all-ages date unverified |
| `li-seed-treatment` | lpa | Seed-treatment name, active and rate. State record duty unverified |

## Record skills

| Skill | Version | Tool | Line items it runs |
|---|---|---|---|
| `au-mob-treatment-records` | 2.0.0 | `createTreatmentRecord` | Batch, dose, meat WHP and ESI, operator, adverse reaction, off-label vet, retention |
| `au-mob-husbandry-records` | 1.0.0 | `createHusbandryRecord` | Sheep mulesing, dock and castrate, eID, plus the shared product items |
| `au-spray-records` | 1.1.0 | `createSprayRecord` | Rate, grazing and harvest, weather, buffer, state record, operator, batch, retention |
| `au-paddock-sowing-records` | 1.0.0 | `createSowingRecord` | Seed treatment, batch, grazing WHP, state record, operator, retention |
| `au-paddock-fertiliser-records` | 1.0.0 | `createFertiliserRecord` | Batch, operator, retention. Fertiliser never sets a withholding |
| `au-paddock-fieldwork-records` | 1.0.0 | `createFieldworkRecord` | Grazing and harvest check via server warnings, state record, batch, operator, retention |
| `au-stock-movement-records` | 1.0.0 | `moveMob` for a paddock move. A sale is a note | eID, retention, operator |
| `au-mob-feeding-records` | 1.0.0 | `createTask` (`feed`) | Retention, operator. CVD and the feed ban are inline until their line items exist |
| `au-farm-task-records` | 1.0.0 | `createTask` (`fence`, `observation`) | Retention |
| `au-compliance-export` | 1.0.0 | `getTreatmentRegister` | Reads the rows. Does not invent a missing value |

`au-spray-records` keeps that name. A rename to `au-paddock-spray-records` would make one spray match two skills for anyone who still has the old zip.

`au-mob-treatment-records` 2.0.0 no longer records husbandry. Install `au-mob-husbandry-records` beside it, and replace an older treatment zip so marking is not claimed twice.

## Not in this release

Priority 1, to split out next: `li-export-intervals`, `li-equipment-calibration`, `li-hgp-cattle`, `li-vetchem-state-rules`, `li-apvma-permit`, `li-target-crop-pest`, `li-restricted-chemicals`, `li-application-time`, `li-record-deadline-reminder`, `li-welfare-cattle`, `li-husbandry-outcomes`, `li-nwd-status`, `li-nlis-movement`, `li-health-declaration`, `li-cvd-fodder`, `li-ram-ban`, `li-cvd-generator`, `li-harvest-mrl-check`, `li-treated-grain-segregation`, `li-plant-back-check`, `li-fertiliser-stock-warnings`, `li-reef-nutrient-qld`.

Priority 2: `li-apvma-product-id`, `li-gm-crop-stewardship`, `li-fertiliser-heavy-metals`, `li-welfare-biosecurity-plan`.

Still research, not skills: `li-burning-permit`, `li-irrigation-water-meter`, `li-effluent-manure`, `li-erosion-native-veg`, `li-seed-label-pbr`, `li-qa-scheme-overlay`.

The record skills still ask the short form of a deferred item when the farmer cannot otherwise make the record. They say the full check is not installed. Unverified figures are not stated as law.

Add-on plugins (`purplegrain-livestock`, `purplegrain-cropping`, `purplegrain-qld-reef`) and a per-orchestrator bundle zip are not in this release. One plugin ships every skill. Each skill is still its own zip.
