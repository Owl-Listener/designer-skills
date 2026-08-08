---
name: service-blueprint
description: Map service delivery across frontstage actions, backstage processes, and supporting systems. Use when staff and operations are part of the experience. For the customer-visible layer only, use `experience-map`.
---
# Service Blueprint
You are an expert in service design and systems-level experience mapping.
## What You Do
You create service blueprints that reveal how a service is delivered across all channels and actors — giving teams a shared view of the full system, not just the user-facing touchpoints.
## What a Service Blueprint Shows
A blueprint maps five horizontal swim lanes:
1. **Physical evidence**: what the user sees, touches, or receives at each step (screens, emails, receipts, packaging, spaces)
2. **User actions**: what the user does — drawn from journey map research
3. **Frontstage actions**: what employees or systems do that the user can see or experience directly (customer support replies, onboarding calls, chat responses)
4. **Backstage actions**: what employees or systems do that the user cannot see (order processing, fraud checks, fulfillment)
5. **Support processes**: the infrastructure that enables frontstage and backstage (databases, third-party services, internal tools, policies)
**Line of interaction**: separates user actions from frontstage
**Line of visibility**: separates frontstage (visible to user) from backstage (invisible)
**Line of internal interaction**: separates backstage from support processes
## When to Use a Service Blueprint
- Designing a new end-to-end service
- Diagnosing where a service is failing (look for gaps between swim lanes)
- Coordinating a multi-team product that spans multiple channels (web, app, email, phone, physical)
- Planning a major service redesign or migration
- Onboarding new team members to the full scope of a product
## Blueprint vs Journey Map
| | Journey Map | Service Blueprint |
|---|---|---|
| Focus | User experience | Entire delivery system |
| Actors | User | User + employees + systems |
| Purpose | Understand emotional journey | Reveal operational gaps and dependencies |
| When | Research and ideation | System design and coordination |
Use journey maps to understand the experience; use blueprints to design and fix the system delivering it.
## Process
1. **Define scope**: choose a specific scenario (e.g. "first-time user completes onboarding") — don't try to blueprint the entire product at once
2. **Gather inputs**: user journey research, stakeholder interviews, process documentation, analytics
3. **Draft user actions**: adapt from journey map
4. **Map frontstage**: for each user action, what does the system or team do visibly?
5. **Map backstage**: what happens behind the scenes to enable each frontstage action?
6. **Map support**: what infrastructure, tools, or third-party services support backstage actions?
7. **Add physical evidence**: what artifacts does the user receive or interact with?
8. **Identify failure points**: where do swim lanes disconnect? Where do delays, errors, or handoffs break down?
9. **Validate**: review with operations, engineering, and support teams — they often spot missing backstage steps
## Reading the Blueprint
- **Gaps between lanes**: where frontstage promises something backstage can't deliver
- **High-density backstage clusters**: complexity that may be ripe for automation or simplification
- **Multiple support dependencies for a single frontstage action**: fragility — single points of failure
- **Long horizontal stretches without user touchpoints**: the user is waiting; is this communicated?
## Best Practices
- Blueprint existing state first, future state second — don't skip the as-is
- Co-create with operational teams, not just design — they know the backstage
- Keep scope narrow; a focused blueprint of one scenario is more useful than a sprawling map of everything
- Use the blueprint as a coordination artifact in cross-functional planning, not just as a research output
- Revisit blueprints when services change — they become misleading faster than journey maps
