---
name: li-operator-credential
description: "Line item for PurpleGrain record skills. Do not use directly. Who did the job, how to contact them, and the chemical-user credential when the state or the product requires one."
---

# Operator and credential

Version 1.0.0. Do not call a PurpleGrain write. All six typed record creates accept `operator`, `record_notes` and `tags` in `body.data.attributes`; an omitted or blank operator defaults to the signed-in user's display name. Give the orchestrator the confirmed operator and notes to save atomically with the record, then read the saved task. Use `updateTask` only for a confirmed correction to an existing task, not a routine second write. A plain `createTask` also takes `operator` on the create. Phone, address and the credential have no dedicated fields: `record_notes`.

Ask the credential when the state or the product requires one. Otherwise the name is the LPA field and follows the legal gaps. Do not ask for a licence number on an ordinary drench just to fill a gap.

## Applies when

Any record. The credential half applies to agricultural chemical use (spray, and a seed treatment the farmer says was done on the farm) and to fertiliser only when they mention a contractor spreader or a quality scheme.

## Collect

| Fact | Where it goes |
|---|---|
| Who did it, when it was not the signed-in user | `operator` |
| Phone, and address where the state record wants it | `record_notes` |
| Supervisor, and the person the job was done for | `record_notes` |
| Credential type and number they actually hold | `record_notes` |

Never invent a licence number. A training card is not a state permit.

## Credentials that were checked

| Place | What to ask | Last checked | Status |
|---|---|---|---|
| Victoria | An ACUP for Schedule 7 poisons, atrazine, metham sodium, ester formulations of MCPA, 2,4-D, 2,4-DB or triclopyr, and listed baits and fumigants. Issued for 10 years. A training certificate is not the ACUP. Someone under the direct sight and sound of an ACUP holder need not hold one | 19 Oct 2026 | E |
| New South Wales | Independent users: AQF level 3, retraining every five years. Spraying weeds for fee or reward: a ground applicator licence | 19 Oct 2026 | E |
| Queensland | An ACDC licence for ground distribution with powered equipment on land the person does not own or occupy. ChemCert AQF3 is the usual training. It is not the licence | 19 Oct 2026 | E |
| South Australia | Users of Group 4 herbicides in prescribed businesses and prescribed areas: at least AHCCHM307 | 19 Oct 2026 | E |
| Northern Territory | Prescribed products: approved training, or a ground spray applicator's or pilot (chemical rating) licence | 23 Oct 2026 | V |
| ChemCert | AQF3 covers AHCCHM307 and AHCCHM304. ChemCert says it is valid for five years. It is not a Victorian ACUP, a NSW ground applicator licence, or a Queensland ACDC licence | 19 Oct 2026 | E |
| Fertcare / Accu-Spread | Industry accreditation for advisers and spreaders. Often asked by quality schemes. Not established here as a legal duty. Ask only if they mention it, and mark it as industry rather than law | 23 Oct 2026 | S. The Fertcare URL was not verified |

Western Australia, Tasmania and the ACT credential rules for farm spraying were not re-stated as a licence type in the sources used here. Ask what they hold when the job is commercial spraying in those places, and do not name a permit you have not sourced.

## Checks

Severity: `legal`, because a missing ACUP or equivalent is a legal gap for the products above. For a plain livestock treatment the LPA template wants the name and the phone. Record the phone in notes. Do not block a treatment save on a missing phone. Do not block a spray save on a missing credential number they do not have in front of them: name the gap, and pause only when they are about to record a Victorian Schedule 7, atrazine or ester-phenoxy use and they say nobody held an ACUP. They may still record what was already done.

## Confirm fragment

`by {operator}`. Add the credential only when one was stated.

## Sources

Agriculture Victoria ACUP: <https://agriculture.vic.gov.au/farm-management/chemicals/licences-and-permits/agricultural-chemical-user-permit> (19 Oct 2026, E).

NSW EPA training: <https://www.epa.nsw.gov.au/Your-environment/Pesticides/compulsory-training-pesticides/pesticide-trainers-courses> (19 Oct 2026, E).

ChemCert AQF3: <https://www.chemcert.com.au/courses/aqf3-chemical-accreditation/> (19 Oct 2026, E).

NT records page, which states the training or licence point: <https://nt.gov.au/industry/agriculture/farm-management/using-chemicals-responsibly/keeping-records-of-chemical-use> (23 Oct 2026, V).

LPA treatment template, treated-by name and contact: the sheep reference, 19 Oct 2026, E.
