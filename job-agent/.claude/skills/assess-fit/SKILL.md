---
name: assess-fit
description: Score a captured job against the candidate profile and decide go/no-go. Use after intake, or when the user asks "is this worth applying", "score this", "should I apply".
---

# Assess fit

Purpose: **fit score, strengths, honest gaps, go/no-go** → `fit.md`

## Inputs
- `applications/<folder>/jd.md` (required)
- `profile/facts.md` and `profile/master-resume.docx` (evidence, read-only)
- `profile/answers.md` (logistics)

## Steps
1. **Decompose the JD** into weighted dimensions using the `fit.md` table.
   Weight *core skills* highest; weight logistics only enough to kill a bad
   match early.
2. **Score 0-5 per dimension** with a one-line justification. Half-points are
   allowed. A score of 0 requires an explicit note.
3. **Walk the must-have list** row by row: met / partial / no, with the
   evidence in `facts.md`. A "no" on a true must-have caps the verdict at
   CONDITIONAL GO.
4. **List strengths** as evidence-backed claims, each with its `facts.md` metric.
5. **List honest gaps.** For each: description, whether it blocks, and the one
   sentence to say out loud. Gaps are the point of this skill — never zero out.
6. **Verdict:** GO (≥3.5) / CONDITIONAL GO (2.5-3.49) / NO-GO (<2.5).
7. **Recommend the next step** and state it plainly.
8. Update `tracker.csv` via `log`: `fit_score` and status → `assessed`
   (or `skipped` on NO-GO).

## Never
- Do not soften a score to make an application look viable.
- Do not use claims that are absent from `facts.md`.
- Do not proceed to tailoring on a NO-GO without explicit user instruction.
