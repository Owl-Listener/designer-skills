---
description: Run a parallel exploration end to end — frame the decision, build a spread of behaviourally distinct concepts, pressure-test each, and converge with a decision record.
argument-hint: "[design problem or the concept already on the table, e.g., 'notification settings' or 'the current checkout step 2']"
---
# /explore-options
Run a parallel exploration end to end — frame the decision, build a spread of behaviourally distinct concepts, pressure-test each, and converge with a decision record.
## Steps
1. **Frame the decision** — State what this exploration has to settle and fix the criteria that will decide it, before any concept exists, using `concept-selection` skill.
2. **Set the spread** — Decide how many concepts the stakes justify and which behavioural dimension they must differ on, using `parallel-concepts` skill.
3. **Draft each concept** — Specify structure, content priority, and annotations for every concept at matched fidelity, using `wireframe-spec` skill.
4. **Trace the difference** — Map each concept's user path and confirm the paths actually diverge; collapse any two that do not, using `user-flow-diagram` skill.
5. **Pressure-test** — Evaluate every concept against usability heuristics on its own terms before any comparison, using `heuristic-evaluation` skill.
6. **Converge** — Apply the criteria from step 1, choose one concept, and record what each rejected concept was testing and what would bring it back, using `concept-selection` skill.
## Output
A concept set and a decision record. The set contains each concept at matched fidelity with its wireframe spec, user flow, and heuristic findings. The record states the criteria fixed in step 1, the chosen concept and what it gives up, and one entry per rejected concept covering what it tested, what it lost on, and its revival condition. The designer takes the chosen concept into detailed design and keeps the record as the answer to "why not the other way".
Consider following up with `/test-plan` to validate the chosen concept with users before committing to build.
