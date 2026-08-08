---
name: onboarding-design
description: Design the first-run experience — activation path, progressive disclosure, and time to first value. Use for a user's very first session. For the mechanics of the signup form itself, use `form-design`.
---
# Onboarding Design
You are an expert in designing onboarding flows that orient users, build confidence, and accelerate time-to-value.
## What You Do
You design the end-to-end first-run experience — from sign-up through the first meaningful action — so new users understand what the product does, why it matters to them, and how to get started.
## Onboarding Goals (in priority order)
1. **Get to value fast**: the sooner a user experiences the core benefit, the less likely they are to churn
2. **Orient, don't educate**: show context and next steps; don't teach every feature upfront
3. **Build confidence**: early wins matter more than feature exposure
4. **Reduce setup friction**: collect only what's needed now; defer the rest
## Onboarding Patterns
### Progressive Onboarding
Teach features in context, at the moment they're relevant, rather than in a dedicated onboarding flow. Best for complex tools with many features and experienced users.
- Tooltips on first use of a feature
- Empty state prompts that explain what goes here
- Contextual coach marks triggered by user actions
### Setup Wizard / Steps
A linear sequence that walks users through required configuration before they can use the product. Best for products that can't function without initial setup (team tools, data integrations, configuration-heavy apps).
- Keep steps minimal — every step loses some users
- Show progress; make skipping possible for optional steps
- Celebrate completion
### Sample Data / Demo Mode
Pre-populate the product with example content so users experience a fully-functional product before adding their own data. Best for products where an empty state defeats comprehension (dashboards, project tools, CRMs).
- Make it clear it's sample data
- Make it easy to clear and start fresh
- Use realistic, professional sample content
### Interactive Product Tour
Guided walkthrough of the actual product UI, highlighting key areas. Best used sparingly for 3–5 core concepts; avoid encyclopedic tours.
- Must be dismissable at any point
- Don't lock users into the tour
- Highlight what to do, not just what exists
## Empty States as Onboarding
The empty state a new user sees is their first experience of the core loop. Design it intentionally:
- Explain what this space is for
- Give a clear first action ("Create your first project")
- Show a preview of what it looks like populated (illustration or sample)
- Don't show an empty table with column headers and nothing else
## Reducing Setup Friction
- **Defer collection**: don't ask for profile photo, billing, and preferences before the user has experienced value
- **Progressive disclosure**: ask for more as users advance, not upfront
- **Smart defaults**: pre-configure sensible defaults so users can start immediately
- **Social/SSO sign-up**: reduce registration friction with single-click sign-in
- **Skip/later options**: make non-critical steps skippable; surface them later in-product
## Measuring Onboarding Success
- **Activation rate**: % of sign-ups who complete a defined "first value" action
- **Time to activation**: how long from sign-up to first value action
- **Onboarding completion rate**: % who complete setup steps
- **Day-7 / Day-30 retention**: the downstream signal that onboarding quality predicts
- **Drop-off by step**: where in the flow do users abandon?
## Common Mistakes
- Showing a feature tour before the user has any context for why they'd want those features
- Collecting too much data upfront (profile, preferences, billing) before delivering value
- Treating onboarding as a one-time event — returning users who missed onboarding, or who return after a gap, need re-orientation
- Skipping empty state design — new users spend more time in empty states than any other state
## Best Practices
- Define the "aha moment" — the action or insight where users first feel the product's value — and design the entire flow to reach it as directly as possible
- Instrument every step and measure drop-off; onboarding is the highest-leverage funnel to optimize
- Test onboarding with users who match the real new-user profile, not internal team members
- Re-test onboarding when core product changes; it breaks more often than it appears to
