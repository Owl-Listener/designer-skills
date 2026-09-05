# Evals — behavioural-analytics

Three inputs a working designer would actually bring, and what a good output has to contain.
Each case is designed so a plausible-sounding but shallow answer fails at least one check.

Run a case by giving the skill only the **Input**. Score against **Must contain**.
A case passes when every Must-contain line is met and no Must-not line is triggered.

---

## Case 1 — The trap: a tracking artefact dressed as a design problem

**Input**
> Our signup funnel shows 60% of users dropping between "account created" and "profile completed".
> Leadership wants the profile step redesigned this quarter. Where should we start?

**Must contain**
- [ ] Questions what the two events actually fire on before proposing any redesign
- [ ] Raises at least one non-design explanation (users can skip profile; profile is reachable later; the event fires on render)
- [ ] Notes that a "step" users are not forced through is not a funnel step
- [ ] Names what would confirm or kill the tracking explanation, cheaply
- [ ] Gives a ranked next action, not a list of everything that could be wrong

**Must not**
- Accept the 60% at face value and go straight to redesign recommendations
- Produce a generic list of form-usability tips

**Why this case** — the most common real failure. The number is probably fine and the funnel is probably wrong.

---

## Case 2 — Shape reading: distinguishing a block from a length problem

**Input**
> Checkout is five steps. Completion by step: 100%, 94%, 91%, 88%, 84%.
> Our competitor's checkout is three steps. Should we cut two steps?

**Must contain**
- [ ] Identifies this as a slope, not a cliff — no single step is blocking
- [ ] States explicitly that removing one step would move the total only slightly
- [ ] Reasons about the cumulative effect of length rather than any individual step
- [ ] Notes that competitor step-count is not evidence about *this* flow
- [ ] Says what data would actually justify the cut (where time and effort concentrate, not where users leave)

**Must not**
- Recommend cutting steps because the competitor has fewer
- Single out the step with the largest individual drop (94→91) as "the problem"

**Why this case** — tests whether the skill reads shape rather than hunting for the worst number.

---

## Case 3 — Segmentation: an average that describes nobody

**Input**
> Time-on-task for our search feature averages 42 seconds, up from 31 last quarter.
> The histogram has one bump around 8 seconds and another around 90.

**Must contain**
- [ ] Names the distribution as bimodal and refuses to design against the mean
- [ ] Proposes that two populations are doing different things in one flow
- [ ] Offers a concrete hypothesis for what separates them (known-item lookup vs exploratory browsing, or similar)
- [ ] States that the rise in average may be a mix shift rather than anyone getting slower
- [ ] Names the segmentation needed before any design work starts

**Must not**
- Treat 42 seconds as a fact about users and propose speeding up search
- Report the mean rising as straightforwardly bad

**Why this case** — a mix shift is invisible if you only read the average, and "make it faster" is the wrong answer for at least one of the two groups.

---

## Scoring

| Result | Meaning |
| --- | --- |
| 3/3 | Skill is doing its job |
| 2/3 | Usable; note which check failed and whether the body covers it |
| ≤1/3 | The skill is not teaching the judgment it claims to |

Record the failing check, not just the score — a failed check names the section of the skill that needs work.
