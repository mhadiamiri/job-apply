---
name: fill-application
description: Drive the browser to fill an application form and stop before submission. Use when the user says "fill the application", "apply on the site", or the portal needs completing.
---

# Fill application

Purpose: **browser part; STOPS BEFORE SUBMIT**

The one non-negotiable rule: **never click Submit, never click an equivalent
final action** ("Submit application", "Sign and send", "Finish"). Not once, not
"just to test", not after confirmation. The user submits.

## Inputs
- `applications/<folder>/form-answers.md` (per-field answers)
- `profile/answers.md` (boilerplate), `profile/facts.md` (identifiers)
- Attachments: `applications/<folder>/Hadi_Amiri_Resume.pdf` (staged by
  `select-resume`, unchanged) and `cover-letter.pdf`

## Steps
1. **Load the portal** and map the form before typing. Screenshot/scan every
   field group: required vs optional, text vs select vs radio, file uploads.
2. **Fill from `form-answers.md` first**, `profile/answers.md` second. Never
   free-associate an answer.
3. **Handle the fiddly field types deliberately:**
   - Selects and radios — choose by label/value, not position.
   - Date pickers — type ISO `YYYY-MM-DD` and verify the displayed value.
   - Checkboxes (EEOC, veteran, disability, work auth) — **leave for the user**;
     record them under `## Sensitive / must-confirm before submit`.
   - File uploads — attach `Hadi_Amiri_Resume.pdf` and `cover-letter.pdf`
     exactly as staged; never re-export or edit either. Verify the filename the
     portal shows.
4. **Verify every field** by re-reading the filled form against
   `form-answers.md`. Flag any field the form asks for that no answer covers.
5. **Stop.** Summarize: fields filled, fields skipped and why, attachments
   staged, and the exact button left for the user.
6. Update `tracker.csv` via `log`: status → `ready-to-submit`, and
   `date_applied` only *after* the user confirms they submitted.

## Never
- Never submit. Never work around a CAPTCHA, SSO challenge, or re-auth.
- Never answer demographic, disability, veteran, or work-authorization
  attestations on the user's behalf.
- Never invent a salary number that contradicts `answers.md`.
- Never apply to a role whose `fit.md` verdict is NO-GO.
