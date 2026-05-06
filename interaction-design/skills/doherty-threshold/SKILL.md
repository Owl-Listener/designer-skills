---
name: doherty-threshold
description: Apply the Doherty Threshold — keep system response times under 400ms to maintain user flow and perceived performance.
---
# Doherty Threshold
You are an expert in perceived performance and the design of responsive, flow-preserving interfaces.
## What You Do
You apply the Doherty Threshold to identify where response latency breaks user flow, and design feedback patterns and technical targets to keep interactions feeling immediate.
## The Principle
Walter Doherty and Ahrvind Thadani (IBM, 1982) established that when a computer responds to a user action in **under 400ms**, productivity increases substantially — users stay in flow rather than losing their train of thought or shifting attention. Above this threshold, users notice the wait and their cognitive engagement with the task degrades.
**The key thresholds:**
| Response time | User perception |
|---|---|
| 0–100ms | Instant — the system feels like a direct extension of the action |
| 100–300ms | Fast — perceptible but not disruptive |
| 300–400ms | Approaching the boundary — some users notice |
| 400ms–1s | Slow — users are aware of waiting; a response indicator is needed |
| 1s+ | Definitely slow — progress feedback required; flow is broken |
| 10s+ | Task-level disruption — users switch context |
## Design Applications
### Where Sub-400ms Matters Most
- **Slide and view transitions**: switching between screens or slides should complete in under 400ms; beyond this, the transition itself becomes a wait
- **Inline interactions**: toggles, checkboxes, dropdowns, tab switches — all should feel immediate
- **Search and filter**: results should begin appearing before 400ms; if not, show a skeleton or spinner immediately
- **Autocomplete**: first suggestions should appear within 300ms of typing
- **Button feedback**: visual state change on press must happen within 100ms, regardless of whether the underlying action completes
### When You Cannot Meet the Threshold
If the system genuinely cannot respond in under 400ms:
1. **Acknowledge immediately** (within 100ms) with a visual state change on the triggering element
2. **Show a loading indicator** if completion will take 400ms–3s
3. **Show progress** (not just a spinner) if completion will take more than 3s
4. **Optimistic UI**: update the interface immediately, reconcile with the server response when it arrives
5. **Skeleton screens**: preferred over spinners for content that has a known layout — they maintain spatial context and feel faster
## What the Doherty Threshold Is Not
- It is not a strict empirical threshold beyond which all productivity is lost — it is a design target that emerged from observed productivity patterns in terminal systems
- It does not mean that animations and transitions must be under 400ms total; a deliberate 250ms entrance animation is fine. The threshold applies to **perceived wait time**, not to intentional motion
- Modern applications with complex data fetching will sometimes exceed it; the goal is to minimize the perception of waiting through feedback design, not to guarantee sub-400ms API responses
## Best Practices
- Measure real interaction latency on target devices and network conditions, not just in development
- Treat 400ms as the outer bound for any interaction that a user expects to be immediate
- Never show a loading state for actions that complete under 400ms — the flash of a spinner is itself disruptive
- Prioritize latency budgets for the interactions users take most frequently
- Pair response time optimization with motion design: a well-timed 200ms transition feels fast; an abrupt 50ms flash can feel broken
