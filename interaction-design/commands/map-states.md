---
description: Model a component's states and transitions end to end — states, events, guards, and edge cases.
argument-hint: "[component name, e.g., 'media player' or 'multi-step checkout']"
---
# /map-states
Model states and transitions for a complex component.
## Steps
1. **Identify states** — List all possible states using `state-machine` skill.
2. **Map transitions** — Define events and transitions using `state-machine` skill.
3. **Loading states** — Define loading behavior per state using `loading-states` skill.
4. **Error states** — Map error conditions using `error-handling-ux` skill.
5. **Feedback** — Define feedback per transition using `feedback-patterns` skill.
6. **Animation** — Specify transition animations using `animation-principles` skill.
## Output
Complete state machine diagram with states, events, transitions, guards, actions, and UI representation per state.
Consider following up with `/design-interaction` for detailed interaction specs.
