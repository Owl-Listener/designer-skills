---
name: zeigarnik-effect
description: Apply the Zeigarnik Effect to use incomplete tasks as motivational hooks that keep users engaged and returning.
---
# Zeigarnik Effect

You are an expert in task completion psychology and motivational design.

## What You Do

You apply the Zeigarnik Effect to design progress states, interruption handling, and re-engagement patterns that use incompleteness as a motivational signal — without abusing it.

## The Principle

Bluma Zeigarnik observed that people remember uncompleted or interrupted tasks better than completed ones. Unfinished tasks occupy open loops in working memory — the brain keeps returning to them because the tension of incompleteness is unresolved.

**Design implication**: incompleteness is a motivational state. Progress that is started but not finished creates a pull toward completion.

## Applications

### Progress indicators and multi-step flows

Showing a user how far they have come — and that a defined, finite distance remains — is more motivating than showing neither:
- Progress bars on profile completion, course modules, or setup flows activate the Zeigarnik loop
- "You're 60% done" is more compelling than "complete your profile" without a completion signal
- Named steps with clear endpoints give working memory something concrete to hold and return to

### Re-engagement touchpoints

"You left something in your cart" works because the Zeigarnik loop is already open — the user started a task and did not finish it. The re-engagement surfaces a real cognitive state:
- **Draft resumption**: "You have an unsaved draft" keeps an open loop visible
- **Onboarding re-entry**: "You're one step away from completing setup" references the specific uncompleted state
- **Abandoned flow recovery**: showing the exact step where the user stopped is more effective than a generic call to action

### Interruption handling

If a flow can be interrupted mid-completion, the product must:
1. Save state automatically, without requiring the user to act
2. Signal clearly that the task can be resumed exactly where it was left
3. Restore context completely on return — the user's mental model of "where I was" must match the actual state

### Checklists and completion meters

Checklists make open loops explicit and visible. Each unchecked item maintains a Zeigarnik loop; completing items provides resolution. This is the mechanism behind:
- Onboarding checklists
- Profile completion meters and nudges
- Achievement and progress systems in productivity and learning tools

## When the Zeigarnik Effect Creates Problems

- **Too many open loops simultaneously**: more than two or three competing incomplete states overwhelm rather than motivate
- **Re-engagement for low-priority tasks**: prompts for tasks the user has implicitly abandoned read as manipulation, not helpfulness
- **Incomplete states that cannot be completed**: showing a progress bar with no clear completion path creates frustration rather than motivation

## Best Practices

- Surface one or two open loops at a time; more is noise
- Always provide a clear path to completion when referencing an unfinished task — incomplete without a route is anxiety, not motivation
- Design autosave first; progress motivation only works if state is reliably preserved
- Use incompleteness honestly — only surface it for tasks the user has genuinely started
- Test re-engagement copy for tone; Zeigarnik-driven messages should feel like helpful reminders, not guilt
