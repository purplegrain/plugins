# Australian paddock spray record requirements

Research note for the `au-spray-records` skill. Checked 19 October 2026. Labels, permits and state rules change. Use the pack in the farmer's hand and the linked page, not a remembered rate or buffer. This note is not agronomy or legal advice.

PurpleGrain field names are the MCP schemas for `createSprayRecord` and `updateSprayRecord`. Where a requirement has no field, the skill stores it in `record_notes`, or the applicator's name in `updateTask.operator`. Do not invent a key.

## 1. What has to be true of every spray

The Agvet Code requires use according to the approved label, or according to an APVMA permit. Off-label use is a state matter and is narrow for food crops. A permit number, permit expiry and any extra record the permit demands go in `record_notes`. Do not invent a permit number.

Label withholding periods:

- Grazing withholding period: domestic interval before grazing. `grazing_whp_days`.
- Harvest withholding period: domestic interval before harvest. `harvest_whp_days`.
- Export slaughter interval (ESI): animals that grazed or ate the treated feed, before export slaughter. `esi_days`.
- Export grazing interval (EGI): before grazing for export markets. `egi_days`.
- Export animal feed interval (EAFI): before cutting or grazing for feed that will be exported or fed to export stock. `eafi_days`.
- Re-entry: worker safety. `re_entry_note`. It does not move the paddock's grazing date.

APVMA residues overview, including the pointer to SAFEMEAT for pesticide WHPs and ESIs: <https://www.apvma.gov.au/chemicals-and-products/pesticides-and-veterinary-residues>

Australian maximum residue limits assume label use. They do not guarantee an importing country's MRL. The skill does not calculate an export clearance. If the farmer names a market, say the Australian intervals are not that market's limit.

`listProducts?kind=herbicide` is a short catalogue. For a herbicide, the catalogue's `whp_days` column is the grazing period and `esi_days` is the harvest period. Read `grazing_whp_days`, `harvest_whp_days`, `export_esi_days` and `egi_days` by those names. Confirm the label.

A product with `do_not_graze: true` is recorded and shown. It gives the paddock no status date, because there is no date. Say that.

## 2. LPA crop, pasture and paddock treatments

Integrity Systems, record keeping: <https://www.integritysystems.com.au/on-farm-assurance/record-keeping/>

Template: <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/lpa-records-templates/lpa-03-crop-pasture-and-paddock-treatment-record-form.pdf>

The page and the template ask for:

- date of application
- paddock identification and location
- crop treated
- area treated
- treated by, name and contact
- application rate (L/ha) and method
- wind direction and speed
- tank mix
- product name, chemical rate, batch number
- WHP, EGI and EAFI
- date safe to harvest or graze

A spray diary is acceptable for an LPA audit if it can be produced in time. LPA learning material says keep these records for a minimum of three years, or the state period, or while the livestock remain on the PIC, whichever is longer. The ISC record-keeping page, for livestock records generally, also recommends seven years after sale or the state period. Keep the longest that applies to that enterprise. LPA auditors inspect accredited producers. Rules: <https://www.integritysystems.com.au/globalassets/isc/pdf-files/lpa-documents/LPA-Rules/>

Own fodder does not need a commodity vendor declaration, because the paddock treatment record is the source. Bought hay or fodder does. Without a CVD, LPA applies a 60-day withhold from when the animals last ate that feed. CVD notes: <https://www.mla.com.au/globalassets/isc/pdf-files/commodity-vendor-declaration-cvd/>

PurpleGrain does not write a CVD. The spray record is what the farmer copies onto one when they sell hay, grain or silage from the paddock.

The sheep and lamb NVD asks whether, in the past 60 days, stock ate material that was still inside a withholding period when it was harvested, collected or first grazed. A spray still inside its grazing WHP at first graze is that question. Answer it from `getPaddock` withholding and the spray rows, not from memory.

## 3. State record rules

Other territories were not researched. Exemptions for household hand application exist in several states. A farm boom, spot spray of a paddock, or aerial job is not that exemption.

| State | Make the record | Keep it | Who can require it |
|---|---|---|---|
| Victoria | 48 hours | 2 years from use | Agriculture Victoria authorised officer |
| New South Wales | 48 hours | 3 years | EPA |
| Queensland | 2 days, or 3 days for a prescribed agricultural ERA product used for relevant cattle grazing or sugarcane | 2 years, or 6 years if the prescribed ERA product contains tebuthiuron | Inspector under the Chemical Usage Act |
| Western Australia | 7 days | 2 years from use | DPIRD inspector |
| South Australia | Group 4 herbicides in prescribed businesses and prescribed areas: accurate records, copy to the owner if the user is someone else. General farm sprays: PIRSA says record within 24 hours as best practice, and that a universal duty may still be coming | Group 4: minimum 2 years. General: PIRSA says two years as best practice | PIRSA for the Group 4 rules |
| Tasmania | Code of practice: commercial and agricultural operators must keep a record. No retention period was found in that code | Not stated in the code read here | NRE Tasmania / Registrar of Chemical Products for licences and the code |

A label or permit period is additional. If it is longer or sooner, follow it as well as the state rule.

### Victoria

Agricultural chemical use records: <https://agriculture.vic.gov.au/farm-management/chemicals/keeping-records-of-chemical-use/agricultural-chemical-use-records>

Within 48 hours, keep two years: product trade name; date; application rate or enough to calculate it; crop, commodity or situation; specific location; wind speed and direction if spraying outdoors; applicator name and contact; supervisor name and contact if there is one; name and contact of the person for whom the spray was done, if applicable. Format is free if it is clear and accurate, including a quality-assurance record. An authorised officer can require it. Templates: <https://agriculture.vic.gov.au/farm-management/chemicals/keeping-records-of-chemical-use/record-keeping-format-and-templates>

Aerial application has the same 48 hours and two years: <https://agriculture.vic.gov.au/farm-management/chemicals/licences-and-permits/licences-for-aerial-spraying-of-agricultural-chemicals>

Ground-spraying guide (September 2022), including the drift risk table: <https://agriculture.vic.gov.au/__data/assets/pdf_file/0010/554923/A-guide-to-using-agricultural-chemicals-in-Victoria-ground-based-spraying_Sept-22.pdf>

That guide's risk table treats still air or wind above 15 km/h, delta T below 2 or above 8, temperature above 28 C, and an inversion as higher hazard. It says a single high-risk factor need not stop a job unless that factor is an inversion. These are guide figures, not a substitute for a tighter label window.

It is an offence to spray so as to injure plants or stock outside the target, or to contaminate produce from outside the target. Mandatory label spray-drift restraints, including no-spray zones, droplet size and wind limits, are legal requirements.

Agricultural Chemical User Permit: <https://agriculture.vic.gov.au/farm-management/chemicals/licences-and-permits/agricultural-chemical-user-permit>

An ACUP is required for Schedule 7 poisons and for products containing atrazine, metham sodium, or ester formulations of MCPA, 2,4-D, 2,4-DB or triclopyr, plus listed baits and fumigants. A training certificate is not the ACUP. The ACUP is issued for 10 years. Someone under the direct sight and sound of an ACUP holder need not hold one. There is no ACUP-number field. `record_notes`.

### New South Wales

EPA compulsory records: <https://www.epa.nsw.gov.au/Your-environment/Pesticides/compulsory-record-keeping>

Pesticides Regulation 2017, Part 4. A record is required for the uses in clause 35, which for farms includes treating crops, fallow or plantation trees with powered spray equipment, horticultural spraying, and powered equipment mounted on a vehicle that is not hand-held. Make it within 48 hours (clause 36(3)) and keep it three years (clause 37).

Clause 36(1) fields: full product name; date; crop or situation; rate and quantity; property address and the area treated; name, address and contact of the applicator, or of the employee and the employer. Outdoor spraying by spray equipment also needs estimated wind speed and direction at the start and at any significant change, plus any other weather the label names (temperature, humidity, rainfall) at those times.

Licensed applicators add equipment, start and finish time, the order of areas, and the owner or occupier if different (clause 36(2)). Aerial application has further rules, including pesticide control order Air-1.

A label or permit record is required even when the use would otherwise be exempt. The EPA is the regulator.

NSW pesticide users must be trained. Independent users need AQF level 3 and retraining every five years. People spraying weeds for fee or reward need a ground applicator licence. EPA training page: <https://www.epa.nsw.gov.au/Your-environment/Pesticides/compulsory-training-pesticides/pesticide-trainers-courses>

ChemCert's account of the NSW rules: <https://www.chemcert.com.au/resources/state-legislation/>

### Queensland

Business Queensland: <https://www.business.qld.gov.au/industries/farms-fishing-forestry/agriculture/sustainable/chemical/use/record>

Chemical Usage (Agricultural and Veterinary) Control Regulation 2017, current reprint read here dated 27 April 2026: <https://www.legislation.qld.gov.au/view/pdf/inforce/current/sl-2017-0136>

Section 33B: make the usage record within 2 days, or within 3 days when a prescribed agricultural ERA product is used for relevant cattle grazing or relevant sugarcane growing. Section 33C contents include trade name and/or APVMA distinguishing number; enough to identify the approved label; full name, address and telephone of the user, the owner or occupier, and any responsible person and supervisor; their qualifications; situation; date; place, and where it sits inside the parcel; equipment and method; weather before, during and after, and the time of each observation; rate or enough to calculate it; any label or permit record detail. The Business Queensland page also lists crop or situation and the purpose of the spray.

Section 33E: keep a general usage record for 2 years. Prescribed agricultural ERA products (the list includes ametryn, atrazine, diuron, hexazinone and tebuthiuron) are kept 2 years, or 6 years if the product contains tebuthiuron. Records must be available to an inspector. In a Great Barrier Reef catchment, the user gives a copy to the responsible person no later than 5 days after the record was made.

Domestic hand-applied grocery-store products used non-commercially are outside this duty. A farm spray is not.

An ACDC licence (commercial operator licence) is for ground distribution with powered equipment on land the person does not own or occupy. ChemCert AQF3 is the usual training for that application. It is not itself the licence.

### Western Australia

DPIRD: <https://www.dpird.wa.gov.au/businesses/biosecurity/agricultural-standards/chemical-spray-regulations/record-keeping-farm-pesticide-application/>

Biosecurity and Agriculture Management (Agricultural Chemical Record Keeping) Regulations 2020, regulation 4: <https://classic.austlii.edu.au/au/legis/wa/consol_reg.20230606/baamcrkr2020782/s4.html>

The responsible owner or occupier must have a record made no later than 7 days after use and kept for 2 years. Fields: name and contact of the owner or occupier; name and contact of the user if different; date and time; full trade name; crop, thing or situation, and the means of application; exact location; rate or enough to determine it; anything else the label or an APVMA permit says to record.

The DPIRD page states exemptions for small-quantity domestic-like use, dwellings, and pool or spa sanitisers. An inspector can require the record. Written or electronic is acceptable.

### South Australia

PIRSA legislation page, Group 4 herbicides: <https://pir.sa.gov.au/crops-and-plants/rural-chemicals/comply_with_legislation>

Users of Group 4 herbicides in prescribed businesses and prescribed areas must hold at least AHCCHM307, keep accurate and complete records for a minimum of 2 years, and give a copy to the property owner or manager if that is not the user. The page's weather rules for 2,4-D and MCPA: do not spray in little or no wind or variable wind; spray Group 4 herbicides in the day with wind between 3 and 20 km/h and no surface inversion; wind blowing away from susceptible crops, houses and towns; stop if an inversion or other unsuitable condition develops.

PIRSA best practice, which is not written there as a universal offence: <https://pir.sa.gov.au/biosecurity/rural_chemicals/chemical_use_best_practice>

That page says a move toward national harmonisation means SA users might have to keep records for all agricultural chemicals, and tells users to record within 24 hours and keep them two years now. Its suggested fields match a full spray diary: applicator and owner contacts, wind, temperature, humidity, delta T, pressure, nozzle, droplet size, crop and area, products and rates, location, date, start and finish.

Uncertainty: do not tell a South Australian farmer that a non-Group-4 boom spray without a diary is a breach of a general SA record statute. Do collect the LPA fields if stock or fodder are involved, and collect whatever the label itself requires.

### Tasmania

Code of Practice for Ground Spraying: <https://nre.tas.gov.au/agriculture/agvet-chemicals/codes-of-practice/code-of-practice-for-ground-spraying>

Section 2, commercial and agricultural operators: must keep a record with at least date, location, and name and rates of products. Sprays on crops for people or stock need a spray report: location, date, time, type and area of crop, amount and name of chemical, rates, and equipment. Wind speed, wind direction and air temperature should also be recorded, or at least an estimate.

Section 4, commercial growers: must keep those records and the operator's name. Must not supply or send produce for processing inside the label withholding period. Occupiers within 100 metres should be told at least one day, preferably two, before a spray. That notification has no field: `record_notes`.

A commercial spray service needs a Commercial Operator Licence from the Registrar of Chemical Products, with a small-amount exception the code points at a brochure for.

Uncertainty: this code was the official Tasmanian page found. No retention period is stated in the sections read. Do not invent one. A label record period still applies.

## 4. Spray drift, buffers, 2,4-D and paraquat

APVMA spray-drift labelling instructions: <https://www.apvma.gov.au/registrations-and-permits/apvma-labelling-codes/alc/spray-drift-labelling-alc>

The standard restraint block, where the label uses it, includes: do not let bystanders contact the spray cloud; do not cause an unacceptable impact outside the site; wind between 3 and 20 km/h at the site during application; do not apply in a hazardous surface temperature inversion (most likely from one to two hours before sunset until one to two hours after sunrise). Buffer tables then set mandatory downwind distances by rate, boom height and the kind of sensitive area (bystander, aquatic, pollinator, vegetation, livestock). Droplet size is a label instruction, not a guess. The skill records the droplet category they state and the no-spray zone they say they kept. It does not look up a buffer and fill `no_spray_zone_m`.

Definitions: <https://apvma.gov.au/spraydrift>

2,4-D review: <https://www.apvma.gov.au/regulation/chemical-review/listing-chemical-reviews/label-reviews/24-d>

High-volatile esters (ethyl, butyl and isobutyl) had active approvals and product registrations cancelled in 2013. Do not record one of those as a current registered use. Later suspensions in 2018 and 2019 put new drift instructions on commercial 2,4-D products. Current labels carry product-specific buffers, droplet size and wind windows. Aerial 2,4-D permit PER87451 (the PDF read here) excludes ethylhexyl, ethyl and isobutyl esters, requires wind between 3 and 15 km/h, forbids inversion conditions, requires very coarse droplets, and requires a written record within 24 hours kept for at least two years: date with start and finish, address and paddocks, full trade name, rate per hectare and hectares, situation, wind speed and direction, temperature and humidity, nozzle and pressure, and further items the permit continues into. Permit PDF: <https://www.apvma.gov.au/sites/default/files/publication/55376-per87451.pdf>

That permit is not every 2,4-D label. Read the label they used. Group 4 is the current herbicide mode-of-action group for these phenoxys; older labels said Group I. SA's Group 4 rules are the state overlay.

Paraquat and diquat: APVMA media release on the final decision: <https://www.apvma.gov.au/news-and-publications/media-releases/apvma-review-finds-new-restrictions-necessary-paraquat-and-diquat-herbicides>

The decision page says new conditions apply to labels of product manufactured from the day of the decision, and existing stock is phased out over two years. Industry reporting dated that decision 23 June 2026 and described lower rates, some uses removed or limited to spot spraying, equipment limits, closed mixing and loading in some cases, stronger PPE, revised re-entry and more drift controls: <https://ausveg.com.au/article/agrichemical-update-apvma-decision-on-paraquat-and-diquat-e-g-spray-seed-gramoxone-reglone/>

Uncertainty: this note does not copy a maximum grams-per-hectare figure from secondary reports. The label on the container, or the current APVMA decision if they are buying new stock, is the rate. Flag when the pack looks like pre-decision stock and the farmer has not checked whether that use is still allowed.

## 5. Accreditation

ChemCert AQF3 covers AHCCHM307 (prepare and apply) and AHCCHM304 (transport and store). ChemCert says the accreditation is valid for five years and is the usual evidence for unsupervised Schedule 7 use, and that state permits still have to be applied for: <https://www.chemcert.com.au/courses/aqf3-chemical-accreditation/>

Do not treat the card as a Victorian ACUP, a NSW ground applicator licence, or a Queensland ACDC licence. Ask which credential the state requires for this product, and store the number they give in `record_notes`.

## 6. Freshcare and other quality schemes

Freshcare Food Safety & Quality Standard, Edition 5 (2026), element 11.13, requires a record of every crop-protection application with: date; start and finish; location and crop; product and batch if available; target; rate and quantity; equipment or method; wind speed and direction; withholding period or earliest harvest date; applicator name. The same element set requires label or permit use, a current permit copy, a record of spray-drift incidents, and calibration at the frequency the standard sets. Standard PDF: <https://www.freshcare.com.au/wp-content/uploads/2026/09/Freshcare-Food-Safety-Quality-Standard-Edition-5-2026.pdf>

A Freshcare auditor is engaged through certification, not by the state inspector. Calibration, target pest and start/finish have no spray fields: `record_notes`.

GLOBALG.A.P. and other export GAP schemes also ask for spray diaries. The current control points were not re-read for this note. Use the packer's current checklist rather than an assumed clause number.

## 7. How a record is produced for inspection

Keep the record in any clear form the state allows: diary, spreadsheet, or this spray record, provided the mandatory fields are actually stored. An empty weather object is not a weather record.

For a PurpleGrain record, `getTreatmentRegister` with `kind: "spray"` returns one row per product: crop, area, rate, water rate, method, applicator, the first weather reading, and the grazing and harvest end dates. A value nobody entered is the text `not recorded`. That register is the printout. `record_notes` on the task holds the state fields the spray child does not have, so an inspection answer has to include those notes, not only the register row.

Who inspects:

- Victoria: authorised officers, Agriculture Victoria
- New South Wales: EPA authorised officers
- Queensland: inspectors under the Chemical Usage (Agricultural and Veterinary) Control Act 1988
- Western Australia: DPIRD inspectors
- South Australia: PIRSA, for the Group 4 herbicide duties
- Tasmania: Registrar of Chemical Products and NRE Tasmania, for licensing and the code
- LPA: an auditor approved by LPA Administration, site or document review
- Freshcare or a packer's GAP scheme: that scheme's auditor

## 8. What the tools will accept

`createSprayRecord` is `POST /paddocks/{paddock_id}/spray-records`, body type `spray-record`. One paddock. A completed record needs at least one product. A future `date` creates an open task.

`method`: `boom`, `boomless`, `aerial`, `drone`, `spot`, `weed_wiper`, `knapsack`, `airblast`.

`droplet_category`: `extremely_fine`, `very_fine`, `fine`, `medium`, `coarse`, `very_coarse`, `extremely_coarse`, `ultra_coarse`.

Product `role`: `herbicide`, `fungicide`, `insecticide`, `adjuvant`.

`rate` must contain a unit. `water_rate` must be litres per hectare or it is stored as none.

`updateSprayRecord` takes `spray.id`, not the task id. `products` and `weather_readings` each replace the whole set.

Paddock status from `getPaddock` or `getPropertyStatus` is the grazing and harvest withholding. ESI, EGI and EAFI are stored on the product and matter for LPA and export. They are not that status object.

No field exists for permit number, ACUP or other licence number, applicator phone, supervisor, crop name, target pest, start and finish of spraying, APVMA product number, neighbour notification, calibration, or rinsate disposal. Those go in `record_notes`.
