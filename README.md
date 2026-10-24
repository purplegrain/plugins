# PurpleGrain plugins

PurpleGrain is farm software for Australian properties, paddocks, mobs and records. This repository is the plugin marketplace.

## What's here

| Plugin | What it does |
|---|---|
| [purplegrain](purplegrain/) | Connects the PurpleGrain MCP server, offers farm setup when the account is empty, and checks a livestock, spray, sowing, fertiliser or field-work record before it is saved. The skill list is [purplegrain/CATALOGUE.md](purplegrain/CATALOGUE.md). |

## Install in Claude Code

```
claude plugin marketplace add purplegrain/plugins
claude plugin install purplegrain@purplegrain
```

Signing in uses PurpleGrain's own login. This repository has no tokens and no customer records.

## Install the skill in the Claude app

Download a skill zip from the [latest GitHub Release](https://github.com/purplegrain/plugins/releases) and upload it as a custom skill. The [catalogue](purplegrain/CATALOGUE.md) is the list. Record skills are the ones a farmer asks for (`au-mob-treatment-records`, `au-mob-husbandry-records`, `au-spray-records`, and the sowing, fertiliser, field work, movement, feeding and export skills). Line-item zips (`li-*`) are checks those record skills use. They are not separate jobs. `pg-onboarding` is farm setup (`pg-onboarding@1`). `pg-core` is the shared confirm and disclaimer.

The connector (properties, mobs, paddocks and saving) comes with the Claude Code plugin above. Other agents can use the same `SKILL.md` text. Whether Cursor installs this repository as a Claude plugin was not verified.

Husbandry is its own skill now. Update `au-mob-treatment-records.zip` when you add `au-mob-husbandry-records.zip`. An old treatment zip that still mentions marking will match the same job twice.

Releases before the treatment skill published `au-drench-records.zip`. Replace that custom skill with `au-mob-treatment-records.zip`. Keeping both installed makes the same drench request match two skills.

Build the zip locally with `bash scripts/build-skill-zips.sh`. Output is `dist/`, which is not committed.

## Issues

Report a problem on this repository's [issue tracker](https://github.com/purplegrain/plugins/issues).
