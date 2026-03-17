#!/bin/bash
# uninstall-codex.sh — Remove designer-skills symlinks from Codex
#
# Removes only symlinks that point back into this repo's skill directories.

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="${HOME}/.agents/skills"
COUNT=0

echo "Uninstalling designer-skills from Codex..."
echo "  Checking: $SKILLS_DIR"
echo ""

if [ ! -d "$SKILLS_DIR" ]; then
  echo "No skills directory found at $SKILLS_DIR. Nothing to do."
  exit 0
fi

for link in "$SKILLS_DIR"/*/; do
  if [ -L "${link%/}" ]; then
    target=$(readlink -f "${link%/}" 2>/dev/null || readlink "${link%/}")
    if echo "$target" | grep -q "$REPO_DIR"; then
      rm "${link%/}"
      COUNT=$((COUNT + 1))
    fi
  fi
done

echo "Removed $COUNT designer-skills symlinks."
echo "Restart Codex for changes to take effect."
