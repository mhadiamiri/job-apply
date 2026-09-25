---
name: log
description: Update tracker.csv with status, dates, fit score, and follow-ups, and surface due follow-ups. Use after any stage change, or when the user asks "what's the status", "what should I follow up on".
---

# Log

Purpose: **updates `tracker.csv`** — the single ledger of every application.

## Schema
`company,role,url,status,fit_score,resume_base,location,source,salary_entered,date_added,date_applied,date_followup_1,date_followup_2,followup_note`

`resume_base` sits immediately after `fit_score` and holds `ai`, `data`, or
blank if no base has been selected yet. See the base-selection rule in
`CLAUDE.md`.

- `location`: Ottawa / Remote (Canada) or the posting's location.
- `source`: where the job came from (LinkedIn, company site, referral).
- `salary_entered`: the number actually submitted, after the `answers.md` salary rule.

Allowed `status` values, in pipeline order:

`sourced` → `assessed` → `resumed` → `lettered` → `ready-to-submit` → `applied` → `interviewing` → `offer` → `closed`
Terminal negatives: `skipped` (NO-GO), `rejected`, `withdrawn`, `ghosted`
Parked, resolved later in the session: `waiting-question`, `waiting-auth`


## Update rules
- One row per company+role. **Update in place**; never append a duplicate.
- `date_added` = date `intake` ran. `date_applied` = date the user actually
  submitted (not the date the form was filled).
- `fit_score` mirrors the weighted total from `fit.md`, one decimal.
- `resume_base` mirrors the base recorded in `fit.md` (`ai` or `data`); set it
  at the `assess-fit` stage, not later.
- `url` is the original posting URL, always.
- Read the file, modify the single row, write it back with the header intact
  and unchanged field order.
- `tracker.csv` is **deny-listed for Edit** in `.claude/settings.json`. This
  skill writes it via an explicit script/Bash step, which the user sees.

## Follow-ups
- After `applied`: set `date_followup_1` = +7 days, `date_followup_2` = +14 days
  (cadence from `profile/answers.md`).
- On a status change to `interviewing`, clear the follow-up dates and record the
  next step in `followup_note`.
- When asked for status, report: counts by status, and a list of applications
  whose follow-up dates have passed or are due within 3 days, oldest first.

## Never
- Never silently change a status the user did not confirm (especially
  `applied`, `rejected`, `offer`).
- Never reformat or reorder the header.
- Never delete a row; set a terminal status and note why in `followup_note`.
