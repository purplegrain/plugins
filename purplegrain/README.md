# PurpleGrain

Connects your assistant to your PurpleGrain account. On a new account it offers to set the farm up (who records, the property and its PIC, the boundary where parcel search covers the state, paddocks and blocks, mobs, then one real record). The setup skill is `pg-onboarding@1` at [skills/pg-onboarding/SKILL.md](skills/pg-onboarding/SKILL.md). After that it checks a record before saving it: a treatment, a husbandry job, a spray, a sowing, a fertiliser, field work, a stock move, or feed brought in.

The skill list is [CATALOGUE.md](CATALOGUE.md).

## What you can do

Ask in ordinary language. "I drenched the rams today with Startect, 20 mL a head, batch 123456." Or "We marked 400 lambs, rings, and mulesed them with pain relief." Or "I boom sprayed the canola in North, 3 litres of atrazine a hectare." The assistant finds the property and the mob or paddock, asks for anything still missing, and shows a short summary. Nothing is saved until you say yes.

The check asks for the fields the rules need. It is not veterinary, legal or agronomic advice, and it does not make the farm compliant by itself. The product label, the APVMA list and a vet's written direction are the authority for dose and intervals. A figure the research has not confirmed is marked unverified and does not block the save.

A spot spray is not saved as the whole paddock unless that is the area sprayed. Fertiliser does not put a paddock under a withholding period. A move between paddocks on the same property is not an NLIS transfer.

## Signing in

Installing the plugin connects to PurpleGrain at `https://api.purplegrain.com/mcp`. The first time you use it, you sign in with your PurpleGrain account. This plugin does not store a password.

A property on your personal account is listed on its own. A property owned by a business is listed with that business. If a farm you expect is missing, say which business it belongs to.
