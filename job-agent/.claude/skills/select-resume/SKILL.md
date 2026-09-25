---
name: select-resume
description: Pick the AI or Data resume base for a job and stage its PDF in the application folder. Use after assess-fit returns GO or CONDITIONAL GO.
---

# Select resume

Purpose: **choose a base → gate it for ATS → stage the PDF unchanged**

Applications use the two resume PDFs **as-is**. Nothing is rewritten, reordered,
or re-exported. This skill only chooses and stages.

## Steps
1. **Pick the base.** Read the `Resume base:` line in
   `applications/<folder>/fit.md`. If it is empty, apply the base selection rule
   in `CLAUDE.md` and write the choice (and the reason) there. If the posting is
   a genuine hybrid tie, ask the user rather than guessing.
2. **Locate the source:** `profile/resumes/<base>/resume-<base>.pdf`.
3. **Text-layer gate.** Extract text with `pypdf`. **If fewer than 500
   characters, STOP** and tell the user the PDF is not ATS-readable. Never
   attach it, and never work around the gate. Ask them to re-export it with an
   embedded, selectable text layer.
4. **Stage it:** copy the PDF to
   `applications/<folder>/Hadi_Amiri_Resume.pdf` — a clean upload filename,
   because recruiters see it. Copy only; the source is never moved or renamed.
5. **Update the tracker** via `log`: `resume_base` = `<base>`, status →
   `resumed`.

## Never
- Never modify the PDF. Never rename or move the source.
- Never attach `profile/resumes/ai/resume-ai.legacy.pdf`; it has no text layer
  and fails the gate above. It exists for visual reference only.
- Never attach a base that `fit.md` did not select, and never proceed on a
  NO-GO verdict.
- Never hand-edit `profile/resumes/**`; mirrors come from
  `python scripts/sync_resumes.py`.
