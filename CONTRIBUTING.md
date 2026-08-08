# Contributing

Designer Skills Collection is maintained by MC Dean. Contributions are welcome — whether it's a bug fix, a typo, or a new skill idea.

## How to Contribute

- **Bugs and small fixes** — open a PR directly.
- **New skills, commands, or larger changes** — open an issue first so we can discuss the approach. PRs for new skills or structural changes without a corresponding open issue will be closed without review.

## Guidelines

- Keep PRs focused — one change per PR.
- Follow existing patterns: **skills are nouns** (domain knowledge), **commands are verbs** (workflows).
- Every skill needs frontmatter with `name` and `description`.
- Every command needs `description` and `argument-hint`.
- Skill name must match its directory name.
- No cross-plugin references in commands.
- Suggest follow-ups in natural language only.
- Every contributor will be listed publicly.

## Using the templates

Copy the relevant template and follow the inline instructions:

- **New skill**: copy [`SKILL_TEMPLATE.md`](./SKILL_TEMPLATE.md) to `<plugin>/skills/<skill-name>/SKILL.md`
- **New command**: copy [`COMMAND_TEMPLATE.md`](./COMMAND_TEMPLATE.md) to `<plugin>/commands/<verb>.md`

Delete all HTML comments before opening your PR.

## Quality bar for skills

A skill is ready when it passes these tests:

1. **The linter passes** — run `python3 scripts/lint-frontmatter.py` and confirm it reports no errors. The linter checks frontmatter fields, name-directory match, kebab-case, and basic document structure.
2. **The description is a complete sentence** — it should tell an agent both what the skill covers and when it applies, in under 120 characters.
3. **"What You Do" is concrete** — it names a specific output, not just a topic. "Design the confirmation strategy for a transactional email" is concrete. "Help with email design" is not.
4. **Each H2 section teaches a judgment** — not just a fact. A reader should be able to apply the principle to a novel situation after reading it.
5. **Best Practices includes at least one "do not"** — the anti-pattern is often the highest-value line in the section.

## Quality bar for commands

A command is ready when:

1. **The linter passes** — same as above.
2. **Every step names a skill** — "using `skill-name` skill" at the end of each step line.
3. **No cross-plugin skill references** — a command in `interaction-design` may only reference skills in `interaction-design`.
4. **3–7 steps** — fewer than 3 is probably just a skill invocation, not a workflow. More than 7 is doing too much.
5. **Output is described specifically** — name the artifact and its sections, not just "a specification".

## Verifying your work

```
python3 scripts/lint-frontmatter.py
```

Run this before every commit. It will report any frontmatter errors with file and line references.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
