---
name: form-design
description: Design a form end to end — field order, grouping, validation, and completion. Use when the artifact is a form. For product-wide error strategy use `error-handling-ux`; for first-run signup use `onboarding-design`.
---
# Form Design
You are an expert in designing forms that are clear, forgiving, and efficient to complete.
## What You Do
You apply form design principles to reduce abandonment, prevent errors, and make data collection feel effortless — from single-field inputs to complex multi-step flows.
## Layout
- **Single column**: almost always correct for forms. Two-column layouts disrupt reading flow and create ambiguity about field order.
- **Field width should reflect expected input length**: a postcode field is narrow; a bio field is wide. Width is a affordance for what belongs there.
- **Top-aligned labels**: faster to scan and more resilient to long labels than left-aligned or placeholder-only patterns.
- **Group related fields** using proximity (Law of Proximity) and section headings for longer forms — don't let long forms run as an undifferentiated column.
## Labels and Instructions
- Every field has a persistent label — never rely on placeholder text as the only label (it disappears on input and fails accessibility)
- Labels are concise and in sentence case; avoid ALL CAPS
- Helper text goes below the label, above the field: "Format: DD/MM/YYYY"
- Required fields: mark optional, not required — if most fields are required, flagging optional reduces visual noise
- Character counts: show remaining characters when limits exist; show them always, not only on approach to the limit
## Input Types
Match input type to the data being collected:
| Data type | Input type |
|---|---|
| Short text | Text input |
| Long text | Textarea (with visible resize) |
| One from few options (≤5) | Radio buttons (all visible) |
| One from many options (6+) | Select / combobox |
| Multiple from few options | Checkboxes |
| Date | Date picker or segmented inputs (day/month/year) — never a freeform text field for structured dates |
| Phone / card numbers | Formatted text input with masking |
| Password | Password input with show/hide toggle |
## Validation
- **Inline validation**: validate on blur (when the user leaves the field), not on every keystroke — real-time validation on typing is distracting
- **Error placement**: directly below the field, not at the top of the form
- **Error messages**: explain what went wrong and how to fix it — "Email address must include @" not "Invalid email"
- **Success indication**: a subtle indicator (checkmark) on fields with non-obvious correctness (password strength, username availability)
- **Server-side errors**: surface inline to the field if possible; summarize at the top if multiple fields are affected
## Multi-Step Forms
- Show progress clearly (step indicator, not just "Step 2 of 5")
- Each step should feel completeable as a unit — related questions together
- Allow back navigation without losing data
- Save progress for long forms (auto-save or explicit "save and continue")
- Confirm before discarding partial input
## Accessibility
- Every field has a programmatic label (`<label for>` or `aria-label`)
- Error messages are associated with their field (`aria-describedby`)
- Focus order follows visual order
- Error summary at top is keyboard-focusable and links to each field
- Don't use color alone to indicate required or error states
## Best Practices
- Remove every optional field you can — fewer fields = higher completion
- Default to the most common answer where one exists; don't default to blank for binary choices
- Test forms with real users entering real data — synthetic test data hides length and format edge cases
- Measure field-level abandonment (which fields do users leave the form on?) — this is where to invest optimization effort
- For high-stakes forms (payments, medical, legal), add a review step before final submission
