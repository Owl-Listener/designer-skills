#!/usr/bin/env bash
# Compiles GEMINI.md context files for each plugin from their source SKILL.md files.
# Run this whenever skills are added or updated.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXTENSIONS_DIR="$REPO_ROOT/.gemini/extensions"

plugins=(
  design-research
  design-systems
  ux-strategy
  ui-design
  interaction-design
  prototyping-testing
  design-ops
  designer-toolkit
  visual-critique
)

echo "Building Gemini extension context files..."

for plugin in "${plugins[@]}"; do
  plugin_dir="$REPO_ROOT/$plugin"
  ext_dir="$EXTENSIONS_DIR/$plugin"

  if [ ! -d "$plugin_dir/skills" ]; then
    echo "  Skipping $plugin (no skills directory)"
    continue
  fi

  mkdir -p "$ext_dir"
  output="$ext_dir/GEMINI.md"

  # Extract the one-line description that follows the heading in the plugin README
  description=$(awk '/^# /{found=1; next} found && NF{print; exit}' "$plugin_dir/README.md" 2>/dev/null || true)

  {
    echo "# $plugin"
    [ -n "$description" ] && echo ""  && echo "$description"
    echo ""
    echo "You are an expert design assistant with the following skills available."
    echo "Apply whichever skills are relevant to the user's request."
    echo ""
  } > "$output"

  # Append each SKILL.md in alphabetical order
  count=0
  for skill_dir in $(find "$plugin_dir/skills" -mindepth 1 -maxdepth 1 -type d | sort); do
    skill_file="$skill_dir/SKILL.md"
    [ -f "$skill_file" ] || continue

    {
      echo "---"
      echo ""
      cat "$skill_file"
      echo ""
    } >> "$output"

    count=$((count + 1))
  done

  # Append command summaries so Gemini knows the available workflows
  commands_dir="$plugin_dir/commands"
  if [ -d "$commands_dir" ] && [ "$(find "$commands_dir" -name '*.md' | wc -l)" -gt 0 ]; then
    {
      echo "---"
      echo ""
      echo "## Available Workflows"
      echo ""
      echo "The following workflows chain multiple skills together:"
      echo ""
    } >> "$output"

    for cmd_file in $(find "$commands_dir" -name '*.md' | sort); do
      cmd_name=$(basename "$cmd_file" .md)
      # Extract description from frontmatter
      cmd_desc=$(awk '/^description:/{sub(/^description:[[:space:]]*/,""); print; exit}' "$cmd_file" 2>/dev/null || true)
      echo "- **/$plugin:$cmd_name** — $cmd_desc" >> "$output"
    done
    echo "" >> "$output"
  fi

  echo "  $plugin: $count skills compiled → $(basename "$ext_dir")/GEMINI.md"
done

echo "Done. Extensions are in .gemini/extensions/"
