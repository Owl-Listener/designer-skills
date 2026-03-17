#!/bin/bash
# install-codex.sh — Install designer-skills for OpenAI Codex
#
# Creates symlinks in ~/.agents/skills/ so Codex discovers all 65 design skills.
# Safe to re-run (uses ln -sf to overwrite existing links).

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="${HOME}/.agents/skills"
COUNT=0

echo "Installing designer-skills for Codex..."
echo "  Source: $REPO_DIR"
echo "  Target: $SKILLS_DIR"
echo ""

mkdir -p "$SKILLS_DIR"

# Scan all plugin directories + workflow for skills
for plugin_dir in design-research design-systems ux-strategy ui-design interaction-design prototyping-testing design-ops designer-toolkit workflow; do
  skills_path="$REPO_DIR/$plugin_dir/skills"
  if [ -d "$skills_path" ]; then
    for skill_dir in "$skills_path"/*/; do
      skill_name=$(basename "$skill_dir")
      if [ -f "$skill_dir/SKILL.md" ]; then
        ln -sf "$skill_dir" "$SKILLS_DIR/$skill_name"
        COUNT=$((COUNT + 1))
      fi
    done
  fi
done

echo "Installed $COUNT designer skills to $SKILLS_DIR"
echo ""
echo "Restart Codex to discover the skills."
echo "Verify: ls ~/.agents/skills/ | head -20"
echo ""
echo "To uninstall: bash $REPO_DIR/scripts/uninstall-codex.sh"
