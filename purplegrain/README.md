# PurpleGrain

Connects Claude to your PurpleGrain account and checks an Australian livestock treatment, sheep husbandry record or paddock spray before it is saved.

## What you can do

Ask in ordinary language. "I drenched the rams today with Startect, 20 mL a head, batch 123456." Or "We marked 400 lambs, rings, and mulesed them with pain relief." Claude finds the property and the mob, asks for anything still missing (batch, expiry, dose, withholding period, export interval, who treated, and for sheep the procedure and the pain relief), and shows you a short summary. Nothing is saved until you say yes.

The check covers:

- the fields Livestock Production Assurance expects on a treatment record
- withholding (WHP), export (ESI) and wool-interval end dates, worked out from the treatment date
- a treatment dated after the product expired, or dated in the future
- a second record of the same product, or the same husbandry procedures, on the same mob and the same day
- sheep marking, mulesing, tail docking, castration, tagging, crutching, shearing, scanning and weaning, against the national sheep welfare standards
- what to note for a wool declaration, a sheep health declaration, or an NLIS movement, where PurpleGrain has no field for it

It is a completeness check. The product label and the APVMA list are the authority for dose and intervals. The state rule can be stricter than the national sheep standard.

The same check applies to a paddock spray. "I boom sprayed the canola in North, 3 litres of atrazine a hectare, batch 123456." Claude finds the paddock, asks for anything still missing (rate unit, batch, grazing and harvest intervals, wind, who sprayed), and shows a short summary before anything is saved. A spot spray is not saved as the whole paddock unless that is the area sprayed.

## Signing in

Installing the plugin connects to PurpleGrain at `https://api.purplegrain.com/mcp`. The first time you use it, Claude asks you to sign in with your PurpleGrain account. This plugin does not store a password.

A property on your personal account is listed on its own. A property owned by a business is listed with that business. If a farm you expect is missing, say which business it belongs to.
