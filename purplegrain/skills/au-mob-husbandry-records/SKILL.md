---
name: au-mob-husbandry-records
description: "Check and save an Australian mob husbandry record before writing it to PurpleGrain. Use for marking, mulesing, tail docking, castration, dehorning, spaying, ear marking, NLIS or eID tagging, crutching, shearing, wigging, scanning, weaning, classing or weighing. A product given on its own, with no husbandry procedure, belongs to au-mob-treatment-records."
---

# Australian mob husbandry records

Version 1.0.0. Follow `pg-core`. If there is no mob, offer `pg-onboarding`. Do not block a read.

This is a record of what was done. It is not veterinary or welfare advice. Where a state has adopted a standard, the standard is the authority. Sheep-standards adoption was not verified except for Tasmania's mulesing regulation, which is its own instrument.

A product used on the day (vaccine, pain relief, jetting fluid) is a product line on this record. Do not also save a treatment for it.

## 1. Choose the record

| What happened | `procedures` | Outcomes | Also |
|---|---|---|---|
| Marking | `mark` | `mark.lambs_marked`, `mark.ewes_joined` | Method in `method` |
| Tail docking | `tail_dock` | None. Extra numbers are refused | Method. Joint and vulva cover: notes, via `li-welfare-sheep-dock-castrate` |
| Castration or cryptorchid | `castrate` | None | Method. Cryptorchid stated in `method` |
| Mulesing | `mules` | None | `li-welfare-sheep-mulesing` |
| eID or NLIS tag | `eid_tag` | None | `li-eid-tagging` |
| Ear notch or brand | `mark` when it is part of lamb marking, otherwise `other` | None | The mark in `method` and notes |
| Crutching | `crutch` | None | |
| Shearing | `shear` | `shear.shearer` (text), `shear.bales`, `shear.wool_kg` | |
| Wigging | `other` | None | Say "wigging" in `description` |
| Weaning | `wean` | `wean.weaned`, `wean.avg_kg` | |
| Scanning | `scan` | `scan.singles`, `scan.twins`, `scan.triplets`, `scan.dry` | |
| Classing | `class` | None | Class result in notes |
| Weighing | `weigh` | `weigh.avg_kg`, `weigh.lightest_kg`, `weigh.heaviest_kg` | |
| Dehorning | `dehorn` | None | Cattle section below |
| Spaying | `spay` | None | Cattle section below |

`marking_percent` is calculated when the record is read. Never send it. Any outcome key not in this table is refused.

`head` is the number the work was done to. `method` is the procedure method, such as "rings", not the dose.

Husbandry has no `route`, `category`, `equipment_cleaned`, `adverse_reaction` or `vet_authorisation`. Those facts go in `record_notes`.

HGP is not husbandry. Hand it to `au-mob-treatment-records`.

A sale declaration, an NVD or an NLIS transfer is `au-stock-movement-records`. This record does not write the NLIS database.

## 2. Line items

| Line item | Applies when | What it covers |
|---|---|---|
| `li-welfare-sheep-mulesing` | `mules` on sheep | Age, pain relief, NWD code they state. Tasmania is stricter |
| `li-welfare-sheep-dock-castrate` | `tail_dock` or `castrate` on sheep | Pain relief over 6 months, one tail joint |
| `li-eid-tagging` | `eid_tag`, or they are about to send sheep or goats off the property | Tag type and the dates. WA all-ages date is unverified |
| `li-product-batch-expiry` | A product was used | `batch`, `expiry` |
| `li-dose-liveweight` | A product was used | Dose and live weight |
| `li-withholding-meat-esi` | A product was used | WHP, ESI, wool, milk |
| `li-operator-credential` | Every job | Who did it. A credential is not the usual question here |
| `li-record-retention` | After the save | Keep-until note |

Not in this release: `li-welfare-cattle`, `li-husbandry-outcomes`, `li-nwd-status`. Outcomes are the table in section 1. NWD codes live in `li-welfare-sheep-mulesing`. At shearing, ask for the code only if it is not already in the notes, and do not assign one.

## 3. Cattle, and what not to apply

`li-welfare-cattle` is not in this release. Do not use the sheep ages on cattle. Goat disbudding and castration ages were not verified (23 Oct 2026). Use the state code they name, and do not invent an age.

Cattle standards, from the livestock research of 23 Oct 2026 (V, the ACT instrument and the MLA toolbox as cited there). Show them. Do not rewrite the history.

- Castration and dehorning need pain relief unless the animal is under 6 months, or under 12 months at its first yarding where the state allows.
- Caustic disbudding only under 14 days, kept dry for 12 hours, separated from the dam for 4 hours.
- Spaying by a vet, or by an accredited person where the state permits. Pain relief for flank spaying or webbing.
- No vaginal spreaders on small or immature cattle.
- A guideline, not a ban: castrate as young as possible, under 12 weeks.

How those standards apply, as published on animalwelfarestandards.net.au and read for that research (as of April 2026, V). The page URL was not copied into the note.

| State | How they apply |
|---|---|
| SA | Regulated from 15 Apr 2017 |
| QLD | Mandatory code from 1 Jul 2021. Non-vet spaying from 1 Jan 2022 |
| TAS | Cattle regulations 2023 |
| NT | Animal protection regulations 2022 |
| NSW | Prescribed guidelines, evidentiary only, since Dec 2017. Do not call a breach from the guideline alone |
| ACT | Approved code from 23 Jan 2026 |
| WA | Code of practice. Regulations were still being drafted |
| VIC | Not yet adopted at that reading |

Sheep shearing, national S5.4 (19 Oct 2026, E): shear before the wool is longer than twice that breed's average annual growth. That is one standard among guidelines about cuts and shelter. Flag it. Adoption of the sheep standards by state was not verified, so do not call it an offence in a named state. The long sheep note's "once every two years" line is a paraphrase of S5.4, not a different calendar rule.

Unusual disease, sudden deaths or a suspected notifiable condition: do not diagnose and do not write a treatment protocol. Emergency Animal Disease Hotline 1800 675 888, or the local animal health office (sheep reference, 19 Oct 2026, E). A product they actually gave is still this record or a treatment, as section 1 says.

## 4. Check, confirm, save, read back

Run the line items. Duplicate: same day and the same procedures on the same mob. Ask.

```
Marking - Lambs (412 hd), 12/08/26, by JS
Procedures: mark, tail dock (rings), castrate (rings), mules. Age stated: about 4 weeks
- Tri-Solfen, dose as stated, batch and expiry as stated
  WHP and ESI as stated
Checks: pain relief is on the record; one palpable tail joint not confirmed; NWD status not stated
Save this record?
```

`createHusbandryRecord` with `body.data.type: "husbandry-record"`, `confirm: true` only after the yes. Nest outcomes as `outcomes.mark.lambs_marked`. The server sets producer, operator and `capture_source: agent`. This tool accepts `Idempotency-Key`. Do not send `broadcast` or `share_scope`. Notes follow `pg-core`. If the write fails, read the mob's records before retrying.

`getMob.withholding` includes husbandry products. A husbandry with no product has no row on `getTreatmentRegister` `kind: "register"`. Say what was saved and which welfare or eID check is still open.
