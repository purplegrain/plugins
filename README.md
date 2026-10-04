# PurpleGrain plugins

PurpleGrain is farm software for Australian properties, paddocks, mobs and records. This repository is the plugin marketplace.

## What's here

| Plugin | What it does |
|---|---|
| [purplegrain](purplegrain/) | Connects the PurpleGrain MCP server and checks a livestock drench or other animal treatment for LPA completeness before it is saved. |

## Install in Claude Code

```
claude plugin marketplace add purplegrain/plugins
claude plugin install purplegrain@purplegrain
```

Signing in uses PurpleGrain's own login. This repository has no tokens and no customer records.

## Install the skill in the Claude app

Download `au-drench-records.zip` from the [latest GitHub Release](https://github.com/purplegrain/plugins/releases) and upload it as a custom skill. That zip is the drench checklist only. The connector (properties, mobs and saving) comes with the Claude Code plugin above.

Build the zip locally with `bash scripts/build-skill-zips.sh`. Output is `dist/`, which is not committed.

## Issues

Report a problem on this repository's [issue tracker](https://github.com/purplegrain/plugins/issues).
