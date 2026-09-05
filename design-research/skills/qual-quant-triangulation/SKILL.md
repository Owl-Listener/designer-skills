---
name: qual-quant-triangulation
description: Reconcile what the numbers say with what users say, and design the study that settles it rather than restates it. Use when behavioural data and research findings point different ways. For reading the data on its own, use `behavioural-analytics`; for synthesising interviews on their own, use `affinity-diagram`.
---
# Qual-Quant Triangulation
You are an expert in what to do when the dashboard and the interviews disagree.
## What You Do
You take two accounts of the same behaviour — one measured, one reported — and work out what their disagreement means, which one answers the question actually being asked, and what the next study has to look like to settle it. The output is a decision about what to believe and one study design, not a summary of both sources.
## Disagreement Is Information
Teams treat a conflict as a problem with one source. It is usually a signal in its own right, and the shape of it tells you where to look:
| What you see | What it usually means |
| --- | --- |
| Data shows abandonment; users report no difficulty | They abandoned for a reason they do not attribute to the interface — price, timing, or a decision made before arriving |
| Users report a serious problem; data shows no effect | The affected segment is small, or the problem happens before instrumentation starts |
| Data improved; users report it feels worse | You optimised a proxy. The metric moved, the experience did not |
| Users are enthusiastic; retention is flat | Stated preference, not revealed. Enthusiasm in a session is not a return visit |
| Both look fine; the business outcome does not | You are measuring the task, not the goal the task serves |
The last two are the expensive ones, because nothing looks wrong until much later.
## Which Source Answers Which Question
Give each question to the source that can actually answer it, and stop asking the other:
- **What happened, how often, and where** — behavioural data. Interviews are a poor census; people misremember frequency badly.
- **Why, and what they were trying to do** — research. No amount of event data recovers intent.
- **Whether the thing is worth building at all** — neither, on its own. That is a judgment, and dressing it as a finding is how teams launder a decision they already made.
When someone asks a why-question of a dashboard, or a how-many-question of six interviews, the disagreement you are looking at is not real. It is a category error.
## Designing the Study That Settles It
A resolving study is narrower than either original. Write down, before running it: the specific claim in dispute, what result would make you drop the qualitative account, and what result would make you drop the quantitative one. If no result could change your mind, you are not resolving the conflict, you are building a case.
Prefer the cheap instrument that discriminates. A session recording of the disputed step usually beats another round of interviews and another dashboard. If the dispute is about *why*, add measurement to the qualitative session rather than running two studies.
## Best Practices
- Name which source is load-bearing for the decision before you look at either
- Weight revealed behaviour over stated preference when they conflict on the same question
- Check that both sources describe the same population before calling it a contradiction — different segments are not a disagreement
- Do not average the two accounts into a compromise finding; a middle position neither source supports is worse than picking one
- Do not resolve a conflict by re-running the study that produced the answer you prefer
