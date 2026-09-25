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
- `tracker.csv`; Telegram approval and session cap from `CLAUDE.md`

## Targets
- Roles: AI engineer, applied AI engineer, artificial intelligence engineer,
  forward-deployed engineer, generative AI engineer, data engineer on Azure / Databricks / Fabric.
- Location: Ottawa, ON (80 km) or Remote (Canada). Date posted: Past 24 hours, always.

## Steps

### Phase 1: Scan (no applying)
1. Run both searches, each with location Ottawa, ON (80 km) and Date posted = Past 24 hours.
   Use the saved search if it exists under Recent job searches; otherwise paste the text.
   - AI search: "I need positions such as: - AI engineer - forward-deployed engineer -
     artificial intelligence engineer - applied AI engineer - anything related to generative
     AI engineering - data engineering in Microsoft Azure and Databricks. The location would
     be either Ottawa, Ontario, or remote Canada, anywhere, including Ottawa itself and other
     places posted in the past 24 hours"
   - Data search: "I need positions such as: - data engineer - cloud data engineer - Azure
     data engineer - Databricks engineer - Microsoft Fabric engineer - data platform engineer
     - analytics engineer. The location would be either Ottawa, Ontario, or remote Canada,
     anywhere, including Ottawa itself and other places posted in the past 24 hours"
2. Merge results, drop duplicates and any URL already in `tracker.csv`.
3. For each job: read the description, apply the fit rules, pick the track, save `jd.md`.
   Log skipped jobs with reasons.
4. Send ONE Telegram message with the shortlist:
```
   Shortlist (N jobs) · reply: ok 1 3 5 · ok all · skip
   1. <Title> · <Company> · <Location/Remote> · <ai|data> · <salary or "no range">
      <one-line fit reason>
      <LinkedIn URL>
```
   If the shortlist is empty, send "No matching jobs in the past 24 hours" and stop.
5. End the turn and wait for Hadi's reply. Log shortlisted jobs as status `awaiting-approval`.

### Phase 2: Apply approved jobs
1. Parse the reply. Unapproved jobs → status `skipped`, reason "not approved".
2. For each approved job in order: Easy Apply (steps as before) or `apply-external`.
   Submit. Confirm the confirmation page. Log.
3. After each job send one line to Telegram: "✓ 3/5 Applied: <Title> · <Company>" or
   "⏸ Parked: <Title> · <reason>".
4. End of session: send a summary to Telegram: applied, parked with reasons and URLs,
   auto-answered questions to review.

### Easy Apply
1. Open a new tab at https://www.linkedin.com/jobs/. If signed out, follow Authentication in `apply-external`.
2. "Easy Apply":
   - Contact: keep prefilled values, check them against `answers.md`, fix mismatches.
   - Resume: select the already-uploaded file for the track (AI: `Hadi-Amiri-AI.pdf`).
     Upload from `profile/resumes/<track>/` only if missing; upload once, reuse afterwards.
   - "Top choice" and other extras: do not mark. Next.
   - Questions: see Screening questions, then Unknown screening questions.
   - Review page: scroll to the bottom. Approved jobs submit here, no second confirmation.
   - Dismiss post-submit popups (Premium, similar jobs). Nothing else.
   - If a question cannot be answered truthfully: close the dialog, choose Save, park the job as
     `waiting-question`, continue.
   - "Apply ↗" instead of Easy Apply → run `apply-external` with this job's context, then return.

## Screening questions (also used by apply-external)
- Source order: `answers.md`, `facts.md`, then the resume. Optimistic but truthful:
  never exceed what the resume dates support.
- Defaults: Bachelor's completed Yes · Authorized to work in Canada Yes ·
  Sponsorship No · AI incl. ML / neural networks 4 · LLMs 3 · AI agents 2 ·
  other skills per the `answers.md` table.
- Essay-style questions: 1 to 3 plain sentences per `voice.md`, from the resume and posting.
- Voluntary self-ID: fill only lines that have a value in `answers.md`.

## Unknown screening questions (also used by apply-external)
- Answer with common sense, truthfully, from the resume and profile, and keep going.
- Append each to `answers.md` under "## Learned answers" tagged `(auto, review)`.
- Park only if the answer requires a fact that exists nowhere in profile or resume
  AND a wrong answer would be a false statement.
- Voluntary self-ID with no value in `answers.md`: choose "Prefer not to answer" /
  "I don't wish to self-identify".
- "I certify the information is accurate" checkboxes: check them.

## Guardrails
- No Premium, "tailor my resume", Jobright match-score or other upsells.
- A Chrome tool fails 2 to 3 times on one step: park the job, move on.
- Never invent degrees, employers, dates or numbers.

