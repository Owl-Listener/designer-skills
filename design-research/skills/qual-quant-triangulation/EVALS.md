# Evals — qual-quant-triangulation

Three conflicts a working designer would actually face, and what a good output has to contain.
Each case is designed so a plausible-sounding but shallow answer fails at least one check.

Run a case by giving the skill only the **Input**. Score against **Must contain**.
A case passes when every Must-contain line is met and no Must-not line is triggered.

---

## Case 1 — The category error: a why-question asked of a dashboard

**Input**
> Analytics says 40% abandon at the payment step. We interviewed eight users and all of them
> said the payment form was clear and easy. Which one is wrong?

**Must contain**
- [ ] States that neither is wrong — they answer different questions
- [ ] Names that the data establishes *where and how often*, the interviews establish *why*, and neither was asked its own question
- [ ] Raises that abandonment may have a cause users do not attribute to the interface (price, timing, a decision made before arriving)
- [ ] Notes that eight interviews cannot speak to a 40% rate
- [ ] Proposes one resolving study, narrower than either original

**Must not**
- Declare a winner between the two sources
- Recommend more interviews as the default next step

**Why this case** — the most common conflict, and usually not a conflict at all.

---

## Case 2 — The proxy trap: the metric moved, the experience did not

**Input**
> We simplified onboarding. Completion went from 55% to 71%. But in follow-up sessions users
> describe the new flow as "rushed" and several said they did not understand what they had set up.
> Ship it more widely?

**Must contain**
- [ ] Identifies completion as a proxy that can move without the experience improving
- [ ] Asks what happens *after* onboarding — activation, retention, support volume — not just completion
- [ ] Names the risk that the flow now defers confusion rather than removing it
- [ ] States that a completion gain and a comprehension loss are not on the same ledger and must both be priced
- [ ] Gives a concrete signal that would settle it, downstream of the metric that moved

**Must not**
- Recommend shipping because the primary metric improved
- Dismiss the qualitative signal as anecdote because n is small

**Why this case** — the expensive failure. Nothing looks wrong until much later.

---

## Case 3 — Stated versus revealed preference

**Input**
> In research sessions, 9 of 10 users said they would use the new saved-filters feature weekly.
> It launched six weeks ago. Weekly usage is 4% and flat.

**Must contain**
- [ ] Names this as stated versus revealed preference, and weights the behavioural evidence
- [ ] Notes that enthusiasm inside a facilitated session is a poor predictor of unprompted return
- [ ] Raises discoverability as a competing explanation before concluding users do not want it
- [ ] Distinguishes "they do not want it" from "they cannot find it" and says how to tell them apart
- [ ] Does not require another round of interviews to make progress

**Must not**
- Conclude the research was simply wrong or the users lied
- Conclude the feature should be removed on six weeks of flat usage alone

**Why this case** — tests whether the skill applies the revealed-behaviour rule *and* still checks the cheap alternative explanation before condemning the feature.

---

## Scoring

| Result | Meaning |
| --- | --- |
| 3/3 | Skill is doing its job |
| 2/3 | Usable; note which check failed and whether the body covers it |
| ≤1/3 | The skill is not teaching the judgment it claims to |

Record the failing check, not just the score — a failed check names the section of the skill that needs work.
