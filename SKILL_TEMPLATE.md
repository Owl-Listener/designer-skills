<!--
  SKILL TEMPLATE — copy to <plugin>/skills/<skill-name>/SKILL.md
  Replace every placeholder in angle-brackets with your content.
  Delete all HTML comments before opening your PR.

  Rules enforced by the linter (scripts/lint-frontmatter.py):
  - `name` must match the directory name exactly
  - `name` must be kebab-case
  - `description` must be present and non-empty
  - File must contain an H1 heading and at least one H2 section

  Rules enforced by the PR template checklist:
  - One skill per PR (open an issue first for new skills)
  - Plugin manifest must be updated in the same commit
-->
---
name: <skill-name>
description: <One sentence — what this skill teaches Claude and when it applies. Under 120 characters.>
---
# <Skill Title in Title Case>

You are an expert in <the specific domain this skill covers — be precise, not broad>.

## What You Do

<Two to four sentences. State the agent's role when this skill is active: what it produces, what decisions it makes, and what it does NOT do. Be concrete about the output, not just the topic.>

## <Core Concept or First Principle>

<Explain the foundational idea. Use plain language. Define terms on first use. If comparing two approaches, use a table. If listing a sequence, use a numbered list.>

### <Sub-topic if needed>

<Add sub-sections only when a concept has meaningfully distinct parts. Avoid nesting beyond two levels (H2 → H3 only).>

## <Second Principle or Method>

<Continue with the next key idea. Aim for 2–4 H2 sections total. Each should encode a judgment the agent can apply — not just facts to recite.>

## Best Practices

- <What to always do — the habit that separates good work from mediocre.>
- <What to verify before shipping — the step most people skip.>
- <What not to do — the common mistake, and why it produces a worse outcome.>
- <When this skill does not apply — where a different approach is better.>
