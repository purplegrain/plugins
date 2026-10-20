# PurpleGrain plugins — Agent Guide

The PurpleGrain plugin marketplace: the `purplegrain` Claude Code plugin (its MCP
connector and the `au-mob-treatment-records` and `au-spray-records` skills) and
the skill zips published on GitHub Releases. See [README.md](README.md).

## Check a change

```bash
claude plugin validate .               # the marketplace
claude plugin validate ./purplegrain   # the plugin
bash scripts/build-skill-zips.sh       # dist/<skill>.zip, one per skill
```

These are the steps the `Validate` workflow runs on every pull request.

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
