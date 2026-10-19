# Sheep treatment and husbandry requirements

Research note for the `au-mob-treatment-records` skill. Checked 19 October 2026. Figures change: use the linked page, not a remembered ESI or a remembered form version. This note is not veterinary or legal advice.

PurpleGrain field names below are the MCP tool schemas for `createTreatmentRecord`, `createHusbandryRecord`, `updateTask` and `moveMob`. Where a requirement has no field, the skill stores it in `record_notes` or asks. Do not invent a key.

## 1. LPA livestock treatment record

Integrity Systems Company (ISC) publishes the LPA program. Module 2 of the May 2025 standards, Safe and responsible animal treatments, requires enough records to trace withholding periods (WHP), export slaughter intervals (ESI) and broken needles, including for introduced livestock, and full records of any hormonal growth promotant (HGP).

- Standards (May 2025): <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-standards-2025-may.pdf>
- Rules, including retention and audits: <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/LPA-Rules/>
- Treatment record template (Requirement 3): <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/lpa-records-templates/lpa-02-livestock-treatment-record-form.pdf>
- Record-keeping booklet (May 2023), same treatment columns: <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/lpa-record-keeping-booklet-may23-online.pdf>
- Factsheet and checklist: <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/lpa-factsheets/safe-and-responsible-animal-treatments-factsheet-and-checklist.pdf>
- Audit checklist (2025): <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-audits-checklist-2025.pdf>
- Record keeping overview: <https://www.integritysystems.com.au/on-farm-assurance/record-keeping/>

The template says veterinary chemical details should be recorded within 48 hours of use. Columns:

- treatment date
- livestock description and location
- tag or mob number
- number treated
- product trade name
- batch number
- expiry
- dose rate, or dipping or jetting rate, and approximate live weight
- treated by, name and contact number
- WHP days
- ESI days
- date safe for slaughter
- adverse reactions
- broken needle still in the animal
- equipment cleaned or calibrated, the date, and who did it

The 2025 audit checklist asks for treatment date, animal or mob identification, chemical and dose, WHP/ESI and expiry, batch number, and adverse reactions with evidence they are passed on at sale.

The May 2025 Module 2 performance checklist also expects a current WHP/ESI chart, label or written veterinary directions, calibrated equipment, secure storage, and segregation of animals still inside a WHP or ESI. On a direct sale inside a WHP or ESI, the buyer is told in writing. The LPA NVD can carry that notice.

HGPs: standards requirement 4 and Rules paragraph 11.5. Treated livestock permanently identified with a triangular ear punch, and full use records kept. That is a cattle (and buffalo) control. There is no ordinary sheep HGP practice. Do not record `category: hgp` or `hgp_earmarked` for sheep.

### Retention and who inspects

Two ISC statements differ, and both are quoted here rather than merged:

- LPA Rules paragraph 11.7: NVDs and other records for introduced and dispatched livestock are kept for a minimum of three years, or for the statutory period, or for as long as the livestock remain on the PIC, whichever is longer.
- ISC record-keeping page: keep records for livestock on the PIC while they are there; after sale, keep them for a minimum of seven years or the state or territory period.

Follow the longest of those. State chemical rules below can be shorter than LPA; LPA still applies to an accredited PIC.

Who inspects: LPA Administration selects accredited producers for audit (Rules section 12). Audits are site audits, document reviews, or both, by an auditor approved by LPA Administration. Reaccreditation is every three years (Rules paragraph 6.3). Random audit material also says producers must produce the biosecurity plan and the treatment records. State inspectors are separate and are listed in sections 4 and 6.

## 2. Sheep and lamb LPA NVD

The paper series in force from 1 January 2021 is version 0720. ISC still describes meat WHP and ESI on that page and points ESI updates to the APVMA.

- Version change: <https://www.integritysystems.com.au/on-farm-assurance/national-vendor-declaration-nvd/nvd-0720-changes>
- Sheep map: <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/nvds/sheep--lambs-map.pdf>
- Explanatory notes (question wording): <https://www.integritysystems.com.au/globalassets/isc/pdf-files/sheep-and-lambs-explanatory-notes.pdf>
- Attachment for extra treatments: <https://www.integritysystems.com.au/globalassets/isc/pdf-files/attachment-to-the-lpa-national-vendor-declaration-and-waybill.pdf>

Uncertainty: those explanatory notes still read as the pre-0720 sheep form (they discuss questions numbered for that layout, and the APVMA sheep ESI PDF of November 2024 still says "Use Q4 on LPA NVD version S0413"). Confirm question numbers against the 0720 form in the producer's LPA account. The substance of the notes:

- Part A is completed by the owner or the person responsible for husbandry. PIC of dispatch, description, PICs on tags or a pink post-breeder tag, consignee, destination.
- Where eID tags are registered to the PIC of dispatch, the vendor does not visually read every tag, list every tag PIC, or add pink transaction tags. See the NLIS section.
- Scabby mouth: tick yes only with evidence of vaccination. Some live-export markets want vaccination at least 14 days before presentation. If unknown, tick no.
- Veterinary drugs and chemicals: oral, injection and skin treatments, including antibiotics, vaccines, worm treatments and external insecticides. Vitamin and mineral treatments are excluded from that question. If unknown, tick yes. Do not consign to slaughter inside a WHP or ESI.
- Wool withholding is not that meat question. The notes say to put wool WHP on the additional-information question or the attachment.
- Agricultural chemicals and feed: the 60-day question about material that was still inside a grazing withholding period when harvested, collected or first grazed.
- The attachment repeats the animal-treatment question: product, treatment date, WHP and ESI if set.

`getTreatmentRegister` with `kind: "nvd"` is PurpleGrain's list of mobs still inside a WHP or ESI. It is not a completed NVD, and an empty list is not a declaration.

## 3. APVMA ESI, WHP, wool and milk

- Sheep ESI list (page): <https://www.apvma.gov.au/chemicals-and-products/pesticides-and-veterinary-residues/esi-sheep>
- November 2024 PDF, stated as updated 20 November 2024: <https://www.apvma.gov.au/sites/default/files/2024-11/Export%20slaughter%20intervals%20of%20veterinary%20chemicals%20for%20use%20in%20sheep%20%E2%80%93%20November%202024.pdf>
- Residues overview, including PubCRIS for labels: <https://www.apvma.gov.au/chemicals-and-products/pesticides-and-veterinary-residues>

An ESI is the advisory interval before slaughter for export, agreed by the sheep industry and the registrant, so residues meet trading-partner limits. A meat WHP is mandatory for domestic slaughter and is on the label. ESIs change through the year. The skill compares a stated ESI with the current list and reports differences. It does not override the farmer silently.

The November 2024 list says SAFEMEAT applies a provisional 90-day ESI for Russian sheep-meat eligibility to products containing oxytetracycline or chlortetracycline, and that this is communicated on the NVD. Store the product's listed ESI in `esi_days`. Put the 90-day Russian market note in `record_notes`. Do not replace the listed ESI with 90 unless the farmer confirms that is the figure they want stored. The NVD version named in that PDF (S0413) is the retired form; the 90-day statement itself was still in the November 2024 list.

`wool_interval_days` and `milk_whp_days` exist on each product. Record a wool harvest interval or a milk WHP only when the label, the vet instruction or the farmer states it. A sheep rehandling interval has no field: `record_notes`. There is no API default that turns a missing ESI into the WHP; the skill sends that substitution only after telling the farmer.

`listProducts?kind=drench` is a short catalogue. It is not the APVMA list, and the tool's `kind` values do not include a sheep-vaccine or lice list.

## 4. State veterinary chemical records

LPA is national and voluntary accreditation. These state rules sit beside it. Other states were not researched for this note.

### Victoria

Agriculture Victoria, veterinary chemical use records: <https://agriculture.vic.gov.au/farm-management/chemicals/keeping-records-of-chemical-use/veterinary-chemical-use-records>

Farmers record use, within 48 hours, when the product is a Schedule 4 prescription animal remedy, has a withholding period, or is an HGP. Keep the record for two years from use. An authorised officer can require it to be produced. Fields: product trade name, species, location, identification number or a description that separates the treated animals, dates treated, quantity used for each treatment. Format is free, including a quality-assurance record, if it is clear and accurate.

Off-label use on sheep, a major species, needs written authorisation from a registered veterinarian: <https://agriculture.vic.gov.au/farm-management/chemicals/veterinary-chemicals>. The label WHP may not fit an off-label use. Stock must not be sold inside a WHP unless the buyer is told in writing (NVD or equivalent).

Legislation named on that site: Agricultural and Veterinary Chemicals (Control of Use) Act 1992 and the 2017 regulations. <https://agriculture.vic.gov.au/farm-management/chemicals/chemical-use-legislation-and-regulation/chemical-use-legislation>

PurpleGrain covers trade name, date, head count and dose. Species is implied by the mob but is not a treatment attribute. Location, a single-animal identity, total quantity, and the applicator's phone go in `record_notes` when Victoria is the record they need.

### Queensland

Business Queensland, treating animals: <https://www.business.qld.gov.au/industries/farms-fishing-forestry/agriculture/sustainable/chemical/use/animals>

People who are not veterinary surgeons use registered products, or permit products, according to the label or permit. Sheep are a major trade species. Off-label use is tightly limited. The page says treated animals must be identifiable by an NLIS device, by separation, or by written records during treatment and the withholding period, and that records must be kept for at least two years.

The Act is more specific than that summary. Chemical Usage (Agricultural and Veterinary) Control Act 1988:

- s 12T: a person in charge of a trade-species animal treated with a product that has a withholding period must take reasonable steps to keep it identifiable during treatment and the withholding period. Examples: tagging, physical segregation, written records.
- s 12U: supplying that animal before the withholding period ends requires written notice (withholding period or end date, product name or active, identity of the animal, treatment date). Supplier and receiver keep the notice for the prescribed period or, if none, two years.
- s 12V: during the withholding period the person in charge must not allow the animal to be shorn or slaughtered, or milk or eggs to be collected for human consumption.
- s 12R: veterinary surgeons keep their own supply and use records, for the prescribed period or two years.

Current Act: <https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1988-103>

Uncertainty: s 12V's phrase "for human consumption" may qualify only milk and eggs, or also shearing and slaughter. Wool selling is in practice governed by the label wool interval. Do not block a shearing record solely because a meat WHP is still running; show both the section and the wool interval and let the farmer decide. The Business Queensland "two years" line is a plain-language summary next to the identification options. The duty that is clearly two years in the Act text read here is retention of the s 12U supply notice and of veterinary surgeons' s 12R records.

Label or permit instructions that require a record: Chemical Usage (Agricultural and Veterinary) Control Regulation 2017 s 33, keep at least two years. <http://www.austlii.edu.au/cgi-bin/viewdoc/au/legis/qld/consol_reg/cuavcr2017570/s33.html>

Who inspects: standards officers under that Act. LPA auditors inspect the LPA records separately.

### New South Wales

Stock medicines and livestock pesticides are different records.

Stock Medicines Act 1989. DPI overview: <https://www.dpi.nsw.gov.au/agriculture/chemicals/animal-chemicals/stock-medicine>. The statutory treatment record in s 39E is kept by veterinary practitioners (unregistered products, off-label use on a major food-producing species, and restricted substances), for two years on the DPI page. A farmer's ordinary drench or pour-on is not that veterinary record. Owners still need LPA records, and s 40A requires the buyer to be told of a withholding period. Off-label use needs a veterinarian's written directions (s 39D). Major food-producing species include sheep.

Pesticides Regulation 2017. Livestock fact sheet: <https://www.epa.nsw.gov.au/sites/default/files/pesticide-factsheets-livestock.pdf>. Clause 35(1)(f) requires a record when livestock are treated for external parasites with a dip bath or powered spray equipment that is not hand-held (plunge dip, spray race, shower dip). Pour-ons, backliners, oral drenches and hand-held spot treatments are stock medicines, not this pesticide record. Make the record within 48 hours and keep it for three years (clause 37). Clause 36 fields include full product name, date, situation, rate and quantity, property address and area, and the applicator's name, address and contact. Outdoor spray equipment also needs wind speed and direction, and any other weather the label names. The EPA is the regulator. <https://www.epa.nsw.gov.au/Your-environment/Pesticides/compulsory-record-keeping>

Those extra pesticide fields have no treatment attributes. Put them in `record_notes` when the job was a plunge dip or a powered spray race. `route: dip` or `route: jetting` still applies when that is what the farmer did. A footbath is not automatically `dip`.

## 5. NLIS sheep and goats

- ISC, what eID is: <https://www.integritysystems.com.au/identification--traceability/national-livestock-identification-system/Sheep-and-Goat-eID/What-is-Sheep-and-Goat-eID/>
- Movements, including who updates the database: <https://www.integritysystems.com.au/identification--traceability/buying-selling-moving/>
- DAFF implementation plan: <https://www.agriculture.gov.au/biosecurity-trade/policy/partnerships/nbc/sheep-and-goat-traceability-task-force/implementation-plan>
- National plan PDF (updated 6 April 2023), with the state table: <https://www.agriculture.gov.au/sites/default/files/documents/national-implementation-plan.pdf>
- Victoria: <https://agriculture.vic.gov.au/livestock-and-animals/national-livestock-identification-system/livestock-identification>

From 1 January 2025, sheep and farmed goats born on or after that date must wear an NLIS-accredited electronic identification device before they leave their property of birth. A visual tag is not enough for those animals. The receiver records the movement on the NLIS database. LPA Module 5 requires the database update for livestock introduced to an accredited PIC within two days, and requires NLIS identification as the statute in that jurisdiction requires.

Victoria has been ahead of that national date: from 1 January 2022 every sheep and non-exempt goat, of any age, needs an electronic NLIS tag before it leaves a Victorian property. One electronic tag only. Tags bought for one PIC are not used on another. A damaged tag is the usual reason to remove one. Sheep entering Victoria may arrive on a visual tag; before they leave a Victorian property they need a pink electronic post-breeder tag unless they already have an electronic tag. A mob-based NLIS transfer is the path for visually tagged introductions.

The DAFF plan also lists 1 January 2027 for "all sheep and goats fitted with an eID before leaving a property, regardless of age". The April 2023 state table does not make that date uniform: Victoria was already all-ages; NSW and Queensland were listed as 1 January 2027 for all ages and 1 January 2025 for newborns; other jurisdictions were still undecided in that PDF. Check the current state rule before telling a farmer that an older visual tag is still legal off the property.

PurpleGrain: `procedures: ["eid_tag"]` records that the mob was tagged. It does not order tags or write the NLIS database. Tag colour, breeder versus post-breeder, and the PIC on the tag go in `record_notes`.

`moveMob` writes an on-property paddock move (`move_stock`) and updates `current_paddock_id`. The destination has to be a paddock on the same property. It is not an NLIS PIC transfer.

## 6. Sheep welfare standards

Endorsed national standards (January 2016 text, PDF dated in the file path 2023): <https://animalwelfarestandards.net.au/wp-content/uploads/2023/08/Sheep-Standards-and-Guidelines-for-Endorsed-Jan-2016-061017.pdf>

Standards are the mandatory tier where a state adopts them. Guidelines are recommended practice. LPA Module 7 (May 2025 standards) requires the PIC representative to have the current sheep standards available, to have completed LPA Learning or equivalent, to train staff, and to keep a documented animal welfare management plan. That plan is not a PurpleGrain record.

Mulesing is defined as removal of skin from the breech and/or tail with mulesing shears. The note under S7 says mulesing does not include clips, intradermal chemical injections, or later non-cutting methods. National standards:

- S7.1: competent operator, or direct supervision
- S7.2: not under 24 hours old and not over 12 months
- S7.3: pain relief is mandatory from 6 to 12 months
- S7.4: not sheep that are diseased, weak or ill-thrift
- S7.5: only wool-bearing skin
- G7.6: where done, at 2–12 weeks
- G7.8: pain relief where practical at other ages

Tail docking and castration:

- S6.2 and S6.4: over 6 months, pain relief and haemorrhage control are mandatory, including cryptorchid
- S6.3: at least one palpable free joint left on the tail
- G6.2 and G6.3: after 24 hours and before 12 weeks
- G6.14: pain relief where practical
- G6.17: hot knife or rubber rings preferred; hot knife when combined with mulesing
- G6.20: dock long enough to cover the vulva in females, similar length in males
- G6.22: lambs to be slaughtered before 12 weeks, or before puberty, should not be castrated

Shearing and crutching are guidelines plus one standard:

- S5.4: shorn before the wool length is greater than twice the average annual growth for that breed
- G5.20: minimise cuts; treat severe cuts
- G5.21: do not turn newly shorn sheep out into cold, wet, windy weather without shelter
- G5.23: sheep that keep their wool should be shorn annually

Business Queensland's sheep code page states the practical shearing rule as at least once every two years unless the wool is self-shedding, and restates the national mulesing and docking age rules: <https://www.business.qld.gov.au/industries/farms-fishing-forestry/agriculture/animal/health/welfare/codes/sheep>. That "two years" reading matches S5.4 if annual growth is the comparator. It is a paraphrase, not a different calendar rule.

Ear marking, tattooing and tagging: G5.15 and G5.17, sharp clean instruments, manufacturer's instructions, minimise infection. There is no husbandry procedure named `earmark`. Use `mark` inside a lamb-marking record, or `other`, and describe the mark in `method` and `record_notes`.

State law can be stricter. Tasmania's Animal Welfare (Sheep) Regulations 2023 prohibit mulesing under 14 days or over 6 months and require pain relief at every mulesing: <https://www.legislation.tas.gov.au/view/pdf/asmade/sr-2023-054>. Do not tell a farmer the national guideline clears them in their state. Flag the national standard, say the state may be stricter, and record what they say was done. Who enforces welfare is the state or territory animal-welfare authority, not the LPA treatment register. LPA auditors look for Module 7 (copy of the standards, training, staff, welfare plan).

There is no age, pain-relief-yes/no, or tail-length field. Age and tail length go in `record_notes`. Pain relief is a product line when a product was used.

## 7. National Wool Declaration

AWEX NWD version 10.0, released 3 October 2023, effective 1 July 2024.

- Business rules: <https://www.awex.com.au/NWD-release-notes-business-rules-for-mulesing.pdf>
- Summary: <https://www.awex.com.au/NWD-Business-Rules-Summary.pdf>
- How to complete: <https://www.awex.com.au/Form-Help-Completing-Your-NWD.pdf>
- Standard page: <https://www.awex.com.au/standards/national-wool-declaration-nwd>

Mob codes:

| Code | Meaning |
|---|---|
| NM | Not mulesed and not treated with liquid nitrogen |
| LN | Treated with liquid nitrogen. Not mulesing |
| AA | Mulesed with an APVMA-registered analgesic and/or anaesthetic. This replaced PR in July 2024 |
| M | Mulesed without that registered product |
| ND | Not declared |

Mixed mobs use the lowest status, in the order NM, then LN, then AA, then M, then ND. CM (ceased mulesing) is the property only, and only when both answers are no: no lambs born on the property in the last 12 months were mulesed, and no mulesed or AA ewes or wethers were purchased in the last 12 months. CM is not a mob code. Liquid nitrogen does not count as mulesing for those questions. The owner or manager signs the NWD and authorises AWEX to see it for the integrity program.

The rules PDF once prints "NM, LM, AA or M". The definition table in the same PDF uses LN. Treat LM as a transcription error unless AWEX publishes LM as a code.

No NWD field exists on a husbandry record. The farmer's stated code goes in `record_notes`. Do not assign one.

## 8. National Sheep Health Declaration

October 2024 form: <https://www.farmbiosecurity.com.au/wp-content/uploads/dlm_uploads/2024/11/National-Sheep-Health-Declaration_Fillable.pdf>

Animal Health Australia: <https://animalhealthaustralia.com.au/sheep-health-and-biosecurity/>

The form's own notes say it is mandatory for all sheep movements in South Australia and for sheep moved into NSW and Tasmania, and voluntary elsewhere. SA states that failing to provide it is an offence under the Livestock Act 1997: <https://pir.sa.gov.au/biosecurity/livestock_movement/sheep_goat_movement_documents>. An older NSW DPI page said the statement became voluntary for movements within NSW from 1 July 2013 and remained mandatory on entry because of footrot. Prefer the October 2024 form note, and still tell the farmer to check the destination state.

Section B asks:

- sources of introductions in five years (closed, 1–5, 6+, or rams only)
- virulent footrot free, and how that was judged
- benign footrot or scald free
- lice free
- ovine brucellosis accreditation, number and expiry (the form says except Queensland)
- JD approved vaccinates, and for how many years all retained lambs were vaccinated (vendor-bred sheep)
- SheepMAP status, year and certificate
- negative JD test, which test, and date
- other health information

Section C asks for the last external parasite treatment, internal parasite treatment, vaccination other than JD, and other treatments: type, product, date.

Virulent footrot is defined differently in each state. The form tells the vendor to use the destination state's department. Do not encode a state eradication program as if it were national.

PurpleGrain does not store a health declaration. Treatment dates already on the mob answer Section C when the products were recorded. Flock-status answers, when the farmer is selling or moving, go in `record_notes` only if they asked to keep them with a record. Do not invent a "free of lice" or "free of footrot" answer.

## 9. Biosecurity plan

LPA Module 6. Each PIC has a documented farm biosecurity plan covering introduction and movement of livestock, control of people, vehicles and equipment where reasonable, and regular monitoring of livestock health.

- ISC biosecurity page: <https://www.integritysystems.com.au/on-farm-assurance/Biosecurity>
- May 2025 standards, Module 6 checklist: same PDF as section 1
- Template (MLA copy of the LPA template): <https://www.mla.com.au/globalassets/mla-corporate/meat-safety-and-traceability/documents/livestock-production-assurance/record-keeping/22921-lpa-biosecurity-plan-template_web.pdf>

The checklist expects known health status on arrival (health declaration or equivalent), inspection and isolation of introductions, regular inspection, stock-proof boundaries, a path to a vet or animal health officer for unusual disease, and visitor records where practical. A SheepMAP or Johne's plan can be the LPA plan if it covers the three elements. Biosecurity has been an LPA requirement since 1 October 2017.

The ISC page, read 19 October 2026, says that from 1 September 2026 accreditation or reaccreditation requires the plan to be created in the LPA account or uploaded there. That date is already past. The skill reminds the farmer; it does not create the plan.

Unusual disease, including suspected footrot where the state says to report it: Emergency Animal Disease Hotline 1800 675 888, or the local animal health office. Do not write a treatment protocol.

## 10. Footrot, lice and antibiotic use

Footrot and lice are flock diseases. The health declaration is the sale document. A footbath, vaccination or antibiotic used on a mob is still a record:

- a chemical footbath is `category: foot_treatment` when the product is the event, or a product line on a husbandry record when it is part of a husbandry day
- a lice or fly product is `category: lice` or `flystrike`, with `route` `backline`, `jetting` or `dip` when that matches
- an antibiotic is `category: antibiotic`, with `vet_authorisation` when it was prescribed or off-label
- a vaccine, including an OJD vaccine or scabby mouth, is `category: vaccine` unless it is a product line on the marking-day husbandry record

Agriculture Victoria's eradication description (individual inspection, separation of infected sheep, repeat inspections, next-spring surveillance) is a program, not a record schema: <https://agriculture.vic.gov.au/biosecurity/animal-diseases/sheep-diseases/footrot-in-sheep/treating-sheep-with-footrot>. State notification and movement rules differ. Making More From Sheep points each state department: <https://www.makingmorefromsheep.com.au/manual/module-11-healthy-and-contented-sheep/tool-11-13-diagnosis-control-and-eradication-of-footrot-lice-ojd-and-ob/>.

Record the treatment the farmer gave. Do not declare the flock free, and do not invent a footrot virulence result.

## 11. What the tools will accept

Treatment `category`: `drench`, `fluke`, `lice`, `flystrike`, `other_external_parasite`, `vaccine`, `vitamin_mineral`, `antibiotic`, `pain_relief`, `feed_water_additive`, `foot_treatment`, `reproductive`, `hgp`, `other`. Do not send `hgp` for sheep.

Treatment `route`: `oral`, `injection`, `backline`, `jetting`, `dip`, `capsule`, `topical`, `in_feed_water`.

Husbandry `procedures`: `mark`, `eid_tag`, `tail_dock`, `castrate`, `mules`, `shear`, `crutch`, `wean`, `scan`, `class`, `weigh`, `dehorn`, `spay`, `other`.

Outcome keys that are documented: `mark.lambs_marked`, `mark.ewes_joined`, `scan.singles`, `scan.twins`, `scan.triplets`, `scan.dry`, `shear.shearer` (text), `shear.bales`, `shear.wool_kg`, `wean.weaned`, `wean.avg_kg`, `weigh.avg_kg`, `weigh.lightest_kg`, `weigh.heaviest_kg`. Any other figure is refused.

Product intervals that affect the mob's sale status are `whp_days` and `esi_days` on treatment and husbandry products. `wool_interval_days` and `milk_whp_days` are stored on the product. The mob `withholding` object is the meat WHP and the ESI, read from `getMob` or `getPropertyStatus`. A wool or milk interval still has to be told to the buyer; it is not that withholding object.

`updateTask.record_notes` is the farmer's words for everything in the tables above that has no attribute. `updateTask.operator` is who did the work when it was not the signed-in user. Neither call is sent with `broadcast` or `share_scope`.
