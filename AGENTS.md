# PurpleGrain plugins — Agent Guide

The PurpleGrain plugin marketplace: the `purplegrain` Claude Code plugin (its MCP
connector, `pg-core`, `pg-onboarding`, the record skills and the line-item
skills) and the skill zips published on GitHub Releases. The list is
[purplegrain/CATALOGUE.md](purplegrain/CATALOGUE.md). See [README.md](README.md).

## Check a change

```bash
bash scripts/verify.sh                 # all four below, one verdict
claude plugin validate .               # the marketplace
claude plugin validate ./purplegrain   # the plugin
python3 scripts/check-skills.py        # names, field ownership, catalogue
bash scripts/build-skill-zips.sh       # dist/<skill>.zip, one per skill
```

These are the steps the `Validate` workflow runs on every pull request, on a
GitHub-hosted runner with Claude Code pinned (`validate.yml`).

This repository is public. Pull-request workflows run on GitHub-hosted runners
only; never point a `pull_request` job at `self-hosted`, because a fork's code
would run on the org Mac. Only the tag-triggered `release` job uses the Mac.

## Shipping

- **Every change reaches `main` through a pull request.** Never push to `main`
  directly, even when told it is fine; `main` is protected. Rebase on the latest
  `origin/main` before opening or updating a PR.
- **All required checks must pass before a PR merges**: `validate`
  (`.github/workflows/validate.yml`).
- **Merging is a release to plugin users.** Claude Code installs the marketplace
  from `main`, so people get a merged change the next time they update the
  plugin. The skill zips ship separately: pushing a `v*` tag on a commit already
  on `main` runs `validate` again and publishes `dist/*.zip` to a GitHub Release.
  Tag only on the owner's word.
