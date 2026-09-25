---
name: tailor-resume
description: Produce a role-specific resume from the master resume, ordering and emphasizing to match a job description. Use after fit is GO, or when the user says "tailor my resume" or "write the resume".
disable-model-invocation: true
---

# Tailor resume

> DISABLED: resumes are used as-is. Only run if the user invokes it by name.

Purpose: **master + JD → tailored `resume.md` → `.docx` → `.pdf`**

## Step 0: select the resume base
- AI base (`profile/resumes/ai/`): Applied AI, GenAI, ML/LLM Engineer,
  Forward Deployed AI Engineer, AI Solutions Engineer, agent/RAG roles.
- Data base (`profile/resumes/data/`): Data Engineer, Cloud Data Engineer,
  Data Platform, Analytics Engineer, Fabric/Databricks/ETL-migration roles.
- Hybrid (e.g. "AI Data Engineer", "ML Platform"): pick the base matching the
  posting's top 3 must-haves, record why in `fit.md`. If it's a genuine tie, ask.
- Read the `.md` mirror, never the `.pdf` directly. If the mirror is older than
  its source (compare mtimes), run `python scripts/sync_resumes.py` first.
- Never attach `profile/resumes/ai/resume-ai.legacy.pdf`: it has no text layer
  and ATS parsers cannot read it. Export the tailored text to a new PDF instead.

## Inputs
- `applications/<folder>/jd.md`, `fit.md`
- The selected resume base (`profile/resumes/<base>/resume-<base>.md`,
  **read-only**), `profile/facts.md`
- `profile/voice.md` (bullet shape)

## Steps
1. **Read the selected base** (`resume-<base>.md` mirror) and build a working
   inventory of every bullet with its metric. Reordering and emphasis are
   allowed; rewriting facts is not.
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
8. **Export** `resume.md` → `resume.docx` → `resume.pdf`, keeping the base's
   styling. Confirm the PDF is text-extractable (ATS) before proceeding.
9. Record the base in `fit.md` (`- **Resume base:**`) and in `tracker.csv`
   (`resume_base` column), via the `log` skill. Status → `resumed`.

## Never
- Never edit `profile/resumes/**` (blocked in `.claude/settings.json`; mirrors
  are written only by `scripts/sync_resumes.py`).
- Never add a skill, employer, title, date, or number not in the base/facts.
- Never ship a text-layer-less or image-only PDF, and never attach
  `resume-ai.legacy.pdf` to an application.
