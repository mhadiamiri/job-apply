---
name: cover-letter
description: Draft a company-specific cover letter and export it to .docx and .pdf. Use after select-resume has staged the resume, or when the user says "write a cover letter".
---

# Cover letter

Purpose: **company + evidence → `cover-letter.md` → `.docx` → `.pdf`**

## Inputs
- `applications/<folder>/jd.md`, `fit.md`
- The selected base's `.md` mirror (`profile/resumes/<base>/resume-<base>.md`) —
  this is the evidence source. Do **not** use `applications/<folder>/resume.md`;
  that file is deleted and resumes are attached as-is.
- `templates/cover-letter.docx` (**your styling** — structure/layout template only)
- `profile/facts.md`, `profile/voice.md`

## Steps
1. **Research the company** from the JD and its site: what it ships, who it is
   for, current focus. The hook must reference something real and specific. If
   nothing concrete is found, ask rather than guess.
2. **Pick two pieces of evidence** from the selected base's `.md` mirror that
   map directly to the role's top responsibilities. These become the body.
3. **Write four short paragraphs**, no filler:
   hook (their problem, their words) → evidence (2 items, with numbers) →
   honest fit (one line, gaps included if any) → close (clear ask).
4. **Keep it under ~250 words.** A letter that restates the resume is a
   failure. No bullet may merely duplicate a resume line.
5. **Run the voice check** and fix findings:
   `python .claude/hooks/check_voice.py applications/<folder>/cover-letter.md`
6. **Delete the `## Notes` block**, then export `cover-letter.md` →
   `cover-letter.docx` → `cover-letter.pdf` using the template's styling.
7. Update `tracker.csv` via `log`: status → `lettered`.

## Never
- Never flatter the company generically ("I love your mission").
- Never claim a gap is not a gap.
- Never exceed the template's styling; the template is the house look.
