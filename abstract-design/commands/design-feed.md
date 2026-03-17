---
description: Add context to the design project workspace. Paste MoMs, emails, Slack threads, research docs, or stakeholder notes.
argument-hint: ""
---
# /design:feed
Add context to the active design project workspace.
## Steps
1. **Prompt** — Ask the designer to paste their content (MoM, email, Slack thread, research doc, etc.).
2. **Ingest** — Append the content to `.design/BRIEF.md` as a new dated section using the `design-feed` skill.
3. **Analyze gaps** — Update `.design/GAPS.md` with what is understood and what is missing.
4. **Reflect** — Surface the key gaps to the designer and ask if they have more context to add.
5. **Suggest next step** — If ready, prompt them to run `/design:validate`.
## Output
- Updated `.design/BRIEF.md`
- Updated `.design/GAPS.md`
Consider following up with `/design:validate` to verify understanding before running agents.
