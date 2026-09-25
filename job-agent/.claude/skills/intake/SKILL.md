---
name: intake
description: Turn a job URL, pasted posting, or a search into a new application folder with jd.md. Use when the user pastes a job link or says "apply to", "add this job", "track this role".
---

# Intake

Purpose: **URL or search → `jd.md` + folder**

## Inputs
- A URL, a pasted posting, or a search query + filters.
- Optional: any constraint the user stated (skip on clearance mismatch, etc.).

## Steps
1. **Capture the posting.** Fetch the URL and save the posting's content to
   `applications/<YYYY-MM-DD>_<company>_<role-slug>/jd.md` using the template in
   an existing `jd.md`. Preserve requirements verbatim — postings disappear.
   - If the page needs JS or blocks fetching, ask the user to paste the text.
   - If only a search result is available, run the search and take the top
     postings; ask which one before creating folders.
2. **Name the folder** `YYYY-MM-DD_company_role-slug`: today's date, company
   lowercased with spaces→hyphens, role slugified.
3. **Normalize the company and role** as they should appear in `tracker.csv`
   (proper case in the row, slug in the folder).
4. **Extract constraints** into the `## Constraints` block: location, comp,
   clearance, seniority, visa.
5. **Add a `tracker.csv` row** via the `log` skill with status `sourced` and
   `date_added` = today. Do not duplicate an existing row for the same
   company+role.
6. **Create** `fit.md`, `cover-letter.md`, `form-answers.md` from their sibling
   templates. Do **not** create `resume.md`: resumes are attached as-is, so the
   only resume artifact in the folder is `Hadi_Amiri_Resume.pdf`, staged later
   by `select-resume`.

## Stop conditions
Ask the user before continuing if: the posting is ambiguous about location or
seniority, the company name is unclear, or the role is likely a repost of one
already in `tracker.csv`.

## Never
- Do not score fit here. That is `assess-fit`.
- Do not write resume or letter content here.
- Do not invent a posting that could not actually be captured.
