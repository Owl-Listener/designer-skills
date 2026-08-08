<!--
  COMMAND TEMPLATE — copy to <plugin>/commands/<verb>.md
  Replace every placeholder in angle-brackets with your content.
  Delete all HTML comments before opening your PR.

  Rules enforced by the linter (scripts/lint-frontmatter.py):
  - `description` must be present and non-empty
  - `argument-hint` must be present and use bracketed placeholder format:
    "[what the user passes, e.g., 'example value']"

  Rules enforced by CONTRIBUTING.md:
  - Only reference skills from the same plugin (no cross-plugin skill references)
  - Suggest follow-ups in natural language only (no cross-plugin command references)
  - One command per PR (open an issue first for new commands)
-->
---
description: <One sentence completing "This command will…". Under 100 characters.>
argument-hint: "[<what the user provides, e.g., 'screen or feature name, e.g., checkout flow'>]"
---
# /<command-name>
<Same sentence as the description — restated as the command's heading.>
## Steps
1. **<Step label>** — <What the agent does and which skill drives it: "Do X using `skill-name` skill.">
2. **<Step label>** — <Each step applies one named skill from the same plugin. 3–7 steps is the right range.>
3. **<Step label>** — <More than 7 steps is a signal the command is doing too much.>
## Output
<One to three sentences describing the artifact produced: what it contains, how it is structured, what the designer does with it next.>
Consider following up with `/<related-command>` to <what that command adds>.
