#!/usr/bin/env bash
# Build dist/<skill-name>.zip for every plugin skill. The skill folder is the
# zip root (unzipping yields <skill-name>/SKILL.md). dist/ is gitignored.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
dist="$root/dist"
rm -rf "$dist"
mkdir -p "$dist"

shopt -s nullglob
found=0
for skill in "$root"/*/skills/*/; do
  found=1
  name="$(basename "$skill")"
  parent="$(dirname "$skill")"
  (
    cd "$parent"
    zip -r "$dist/$name.zip" "$name" -x '*.DS_Store'
  )
  echo "built dist/$name.zip"
done

if [ "$found" -eq 0 ]; then
  echo "no skills found under */skills/*/" >&2
  exit 1
fi
