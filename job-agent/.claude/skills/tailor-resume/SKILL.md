---
name: tailor-resume
description: Produce a role-specific resume from the master resume, ordering and emphasizing to match a job description. Use after fit is GO, or when the user says "tailor my resume" or "write the resume".
---

# Tailor resume

Purpose: **master + JD → tailored `resume.md` → `.docx` → `.pdf`**

## Inputs
- `applications/<folder>/jd.md`, `fit.md`
- `profile/master-resume.docx` (**read-only — never edit**), `profile/facts.md`
- `profile/voice.md` (bullet shape)

## Steps
1. **Read the master** and build a working inventory of every bullet with its
   metric. Reordering and emphasis are allowed; rewriting facts is not.
2. **Select** the bullets that hit the JD's keywords and must-haves. Cut
   aggressively — a tailored resume is shorter or equal in length, never longer.
3. **Reorder experience** so the most relevant role is first. For a senior role,
   consider a 2-line summary that names the JD's core capability.
4. **Mirror the JD's terminology** where it is accurate (e.g. "Kubernetes" not
   "k8s orchestration" *if the JD uses the former*), but never insert a tool
   that was not actually used.
5. **Write `resume.md`** using the per-application template. Every bullet is
   `<strong verb> <what> → <measurable result>`.
6. **Run the voice check** and fix findings:
   `python .claude/hooks/check_voice.py applications/<folder>/resume.md`
7. **Delete the `## Tailoring notes` block** before export.
8. **Export** `resume.md` → `resume.docx` → `resume.pdf`, keeping the master's
   styling. Confirm the PDF is text-extractable (ATS) before proceeding.
9. Update `tracker.csv` via `log`: status → `resumed`.

## Never
- Never edit `profile/master-resume.docx` (blocked in `.claude/settings.json`).
- Never add a skill, employer, title, date, or number not in the master/facts.
- Never ship a text-layer-less or image-only PDF.
