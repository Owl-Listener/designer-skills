---
description: Show current workspace state — what context has been fed, which agents have run, what gaps remain, and what to do next.
argument-hint: ""
---
# /design:status
Show the current design workspace state.
## Steps
1. **Read workspace** — Read `.design/BRIEF.md`, `.design/DESIGN-STATE.md`, and `.design/GAPS.md` using the `design-status` skill.
2. **Check agents** — List which agent output files exist in `.design/research/`.
3. **Print summary** — Show workflow progress (context fed, agents run, brief generated), current gaps, and the next recommended action.
## Output
Printed status summary. No files modified.
