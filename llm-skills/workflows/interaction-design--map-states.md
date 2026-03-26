<!-- Workflow: Map States | Category: Interaction Design -->
<!-- Model the states and transitions for a complex UI component. -->
<!-- Input: [component name, e.g., 'media player' or 'multi-step checkout'] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# map-states
Model states and transitions for a complex component.
## Steps
1. **Identify states** — List all possible states using the state-machine skill (see skills/interaction-design--state-machine.md).
2. **Map transitions** — Define events and transitions using the state-machine skill (see skills/interaction-design--state-machine.md).
3. **Loading states** — Define loading behavior per state using the loading-states skill (see skills/interaction-design--loading-states.md).
4. **Error states** — Map error conditions using the error-handling-ux skill (see skills/interaction-design--error-handling-ux.md).
5. **Feedback** — Define feedback per transition using the feedback-patterns skill (see skills/interaction-design--feedback-patterns.md).
6. **Animation** — Specify transition animations using the animation-principles skill (see skills/interaction-design--animation-principles.md).
## Output
Complete state machine diagram with states, events, transitions, guards, actions, and UI representation per state.
Consider following up with the design-interaction workflow for detailed interaction specs.
