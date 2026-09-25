---
name: apply-linkedin
description: Run a LinkedIn job-apply session. Saved search, Past 24 hours, walk results, Easy Apply in place, hand off-site jobs to apply-external, log every job. Use when Hadi says "run LinkedIn", "apply to new jobs", "start a job session".
---

# LinkedIn apply session

Browser: Claude in Chrome tools only (tabs_context_mcp, navigate, read_page, find,
form_input, computer, get_page_text, file_upload). No host-level mouse clicks.

## Inputs
- `profile/answers.md` and `profile/facts.md`: the only source for form answers
- `profile/resumes/ai/resume-ai.pdf`, `profile/resumes/data/resume-data.pdf`
- `tracker.csv`; `submit_mode` and session cap from `CLAUDE.md`

## Targets
- Roles: AI engineer, applied AI engineer, artificial intelligence engineer,
  forward-deployed engineer, generative AI engineer, data engineer on Azure / Databricks / Fabric.
- Location: Ottawa, ON (80 km) or Remote (Canada). Date posted: Past 24 hours, always.

## Steps
1. Open a new tab at https://www.linkedin.com/jobs/. If signed out, follow Authentication in `apply-external`.
2. Under Recent job searches open the saved "I need positions such as: AI engineer –
   forward-deployed engineer …" search. If missing, search the role list.
   Confirm the location chip reads "Ottawa, ON (80 km)" and set Date posted = Past 24 hours.
3. Walk results top to bottom. For each card:
   a. Skip if marked Applied or its URL is already in `tracker.csv`.
   b. Read the full description (`get_page_text`). Skip if it states more than 5 years
      required, is off-target, or is staff/principal-only. A "Senior" title alone is
      not a skip. Record the skip reason.
   c. Save the description verbatim to
      `applications/<YYYY-MM-DD>_<company>_<role-slug>/jd.md` with URL and date at the top.
      No other files in the fast lane.
   d. Track: AI / GenAI / FDE roles → ai. Databricks / Azure / Fabric data roles → data.
      Hybrid: follow the posting's top 3 must-haves.
   e. "Easy Apply" → step 4. "Apply ↗" → run `apply-external` with this job's context, then return.
4. Easy Apply:
   - Contact: keep prefilled values, check them against `answers.md`, fix mismatches.
   - Resume: select the already-uploaded file for the track (AI: `Hadi-Amiri-AI.pdf`).
     Upload from `profile/resumes/<track>/` only if missing; upload once, reuse afterwards.
   - "Top choice" and other extras: do not mark. Next.
   - Questions: see Screening questions.
   - Review page: scroll to the bottom. review mode: stop, summarize, wait. auto: Submit.
   - Dismiss post-submit popups (Premium, similar jobs). Nothing else.
   - If a question has no answer: close the dialog, choose Save, park the job as
     `waiting-question`, continue.
5. Log every card (applied, skipped, waiting-question, waiting-auth) via `log`.
6. Stop at the end of the list or the session cap. Then:
   - Ask all parked questions in one batch. Append each Q&A to `answers.md` under
     "## Learned answers". Resume the parked jobs.
   - List `waiting-auth` jobs together so Hadi handles them in one sitting, then resume them.
   - Final summary: applied, skipped with reasons, still waiting.

## Screening questions (also used by apply-external)
- Source order: `answers.md`, `facts.md`, then the resume. Optimistic but truthful:
  never exceed what the resume dates support.
- Defaults: Bachelor's completed Yes · Authorized to work in Canada Yes ·
  Sponsorship No · AI incl. ML / neural networks 4 · LLMs 3 · AI agents 2 ·
  other skills per the `answers.md` table.
- Essay-style questions: 1 to 3 plain sentences per `voice.md`, from the resume and posting.
- Voluntary self-ID: fill only lines that have a value in `answers.md`.

## Guardrails
- No Premium, "tailor my resume", Jobright match-score or other upsells.
- A Chrome tool fails 2 to 3 times on one step: park the job, move on.
- Never invent degrees, employers, dates or numbers.

