# PurpleGrain plugins

PurpleGrain is farm software for Australian properties, paddocks, mobs and records. This repository is the plugin marketplace.

## What's here

| Plugin | What it does |
|---|---|
| [purplegrain](purplegrain/) | Connects the PurpleGrain MCP server and checks a livestock treatment, sheep husbandry record or paddock spray for completeness before it is saved. |

## Install in Claude Code

```
claude plugin marketplace add purplegrain/plugins
claude plugin install purplegrain@purplegrain
```

Signing in uses PurpleGrain's own login. This repository has no tokens and no customer records.

## Install the skill in the Claude app

Download a skill zip from the [latest GitHub Release](https://github.com/purplegrain/plugins/releases) and upload it as a custom skill. `au-mob-treatment-records.zip` is the treatment and sheep husbandry checklist. `au-spray-records.zip` is the paddock spray checklist. The connector (properties, mobs, paddocks and saving) comes with the Claude Code plugin above.

Releases before this change published `au-drench-records.zip`. Replace that custom skill with `au-mob-treatment-records.zip`. Keeping both installed makes the same drench request match two skills.

Build the zip locally with `bash scripts/build-skill-zips.sh`. Output is `dist/`, which is not committed.

## Issues

Report a problem on this repository's [issue tracker](https://github.com/purplegrain/plugins/issues).
