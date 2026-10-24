#!/usr/bin/env bash
# The checks the `validate` workflow runs on every PR, with one verdict.
#   bash scripts/verify.sh
set -uo pipefail
cd "$(dirname "$0")/.."

failed=()
step() { local name=$1; shift; printf '\n\033[1m== %s\033[0m\n' "$name"; "$@" || failed+=("$name"); }

step "Validate the marketplace" claude plugin validate .
step "Validate the PurpleGrain plugin" claude plugin validate ./purplegrain
step "Check the skill catalogue" python3 scripts/check-skills.py
step "Build skill zips" bash scripts/build-skill-zips.sh

echo
if [[ ${#failed[@]} -eq 0 ]]; then
  printf '\033[32mVERIFY PASSED\033[0m\n'
else
  printf '\033[31mVERIFY FAILED\033[0m: %s\n' "${failed[*]}" >&2
  exit 1
fi
