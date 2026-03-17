---
name: design:validate
description: Validate problem understanding, stakeholder alignment, context freshness, and gap analysis before proceeding to ideation. Run after design:feed (pre-agent) and after Wave 1 (post-research).
user-invokable: true
---

# design:validate — Validate Understanding

You are validating that the design problem is well-understood, stakeholders are aligned, context is fresh, and gaps are addressed before proceeding.

## When to Use

**Pre-agent:** After `/design:feed`, before `/design:run`
**Post-research:** After Wave 1 agents complete, before Wave 2

## Determine Context

1. Read `.design/DESIGN-STATE.md` to determine current state
2. If "Context feeding" is complete but "Agents run" is pending → Pre-agent validation
3. If Wave 1 agents completed but Wave 2 pending → Post-research validation

If neither state matches:
> "Nothing to validate right now. Run `/design:feed` to add context, then validate. Or run `/design:run` to complete Wave 1, then validate."

## Pre-Agent Validation

### 1. Read Context

Read `.design/BRIEF.md` to understand all context sections added.

### 2. Stakeholder Mapping

Build stakeholder map from "Source:" labels:

```
MoM - Product Sync 2026-03-10 → Product Manager
Email from Engineering → Engineer  
User interview with Sarah → Customer
Slack thread - Design Critique → Designer
```

Update BRIEF.md by appending:

```markdown
## Stakeholders
| Source | Role | Key Input |
|--------|------|-----------|
| [source] | [role] | [1-line summary] |
```

### 3. Conflict Detection

Scan context sections for contradictory statements:
- "focus on speed" vs "focus on stability"
- "simplicity" vs "more features"
- "users want X" vs "users don't like X"

If conflicts found, add to validation report:

```markdown
### Potential Conflicts
- [conflict description]
- Suggestion: Discuss with team before proceeding
```

### 4. Context Age Analysis

Parse timestamps from context sections:
- < 7 days: Fresh ✅
- 7-30 days: ⚠️ Consider refreshing
- > 30 days: ⚠️ Potentially stale

Add to validation report:

```markdown
### Context Age
- [date] ([age]) - [status]
```

### 5. Understanding Confidence

Rate confidence by area:

| Area | Confidence | Notes |
|------|------------|-------|
| Problem statement | HIGH/MEDIUM/LOW | Based on source agreement |
| User needs | HIGH/MEDIUM/LOW | Based on research depth |
| Technical constraints | HIGH/MEDIUM/LOW | Based on engineering input |
| Business goals | HIGH/MEDIUM/LOW | Based on strategy docs |

### 6. Problem Reflection Prompt

Prompt designer:

```
## Problem Reflection

Before we run agents, confirm your understanding:

**What problem are we solving?**
[Synthesize from BRIEF.md]

**Who experiences this?**
[Users identified in context]

**If we solve this, what changes?**
[Designer answers]

**If we DON'T solve this, what happens?**
[Designer answers]

---
Ready to proceed? (yes/no/revise)
```

Save designer's responses to `.design/PROBLEM-REFLECTION.md`.

### 7. Sign-off Tracking

Initialize sign-offs in DESIGN-STATE.md:

```markdown
## Sign-offs
- [ ] Product Manager - pending
- [ ] Engineering - pending  
- [ ] Designer - pending
```

## Post-Research Validation

### 1. Read Research Output

Read `.design/research/RESEARCH.md` to get the synthesized problem statement.

### 2. Compare with Reflection

Read `.design/PROBLEM-REFLECTION.md` (from pre-agent validation).

Compare:
- Does research match designer's understanding?
- Are there significant deviations?

### 3. Validation Prompt

```
## Research Validation

Research has synthesized:

**[Problem Statement from RESEARCH.md]**

**Your earlier reflection:**
[From PROBLEM-REFLECTION.md]

**Quick Check:**
- [ ] Research matches my understanding
- [ ] This problem is worth solving (impact > effort)
- [ ] We have enough evidence to proceed

---
If all pass → proceed to Wave 2
If any fail → /design:feed more context
```

### 4. Confidence Update

Update confidence based on research findings:

```markdown
## Understanding Confidence (Post-Research)

| Area | Confidence | Evidence |
|------|------------|----------|
| Problem statement | HIGH | Research synthesis confirms |
| User needs | MEDIUM | Research adds detail |
| [etc] | [rating] | [source] |
```

### 5. Critical Gaps

From research, surface unknowns that could change the solution:

```markdown
### Critical Unknowns
- What happens if export fails? (edge case)
- How often is this used? (prioritization)
- Technical capacity? (scope)
```

## Generate Validation Report

Create `.design/VALIDATION-REPORT.md`:

```markdown
# Validation Report: [PROJECT]
Generated: [DATE]

## Status
- [x] Pre-agent validation: [date]
- [ ] Post-research validation: pending

## Stakeholders
[Stakeholder table]

## Conflicts
[Any conflicts detected]

## Context Health
[Age analysis]

## Confidence Score
[Confidence table]

## Critical Gaps
[Unknowns]

## Sign-offs
[Who approved]

## Next Step
[Proceed / Need more context / Revise]
```

## Mark Validation Complete

Update `.design/DESIGN-STATE.md`:

- If pre-agent: mark "Pre-agent validation: complete"
- If post-research: mark "Post-research validation: complete"

## Output

- Updated `.design/BRIEF.md` (stakeholder section)
- Updated `.design/GAPS.md` (confidence scoring)
- Updated `.design/DESIGN-STATE.md` (validation status)
- New `.design/PROBLEM-REFLECTION.md` (designer's answers)
- New `.design/VALIDATION-REPORT.md` (full report)

## Usage

```
/design:validate
```

## Platform

Claude Code, OpenCode CLI
