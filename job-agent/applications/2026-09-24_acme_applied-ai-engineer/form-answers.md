# Form Answers — Acme, Applied AI Engineer

Anything not in `profile/answers.md` is job-specific and lives here.
Checkbox/radio/date fields are what breaks an auto-filler, so record them
explicitly. The agent fills fields but **stops before submit**.

## Pre-filled from `profile/answers.md`
- Work authorization: _(from answers.md)_
- Sponsorship required: _(from answers.md)_
- Notice period: _(from answers.md)_
- Desired salary: _(from answers.md)_
- Earliest start date: _(from answers.md)_
- Relocation / work arrangement: _(from answers.md)_
- LinkedIn / GitHub: _(from facts.md)_

## Job-specific answers
| Question | Answer | Source |
|---|---|---|
| Why Acme? | _one specific sentence from the posting_ | jd.md |
| Why this role now? | | facts.md |
| Notice of prior application? | | |
| Referral / recruiter contact? | | |
| Cover letter attached? | Yes — `cover-letter.pdf` | |

## Attachments
- [ ] `resume.pdf`
- [ ] `cover-letter.pdf`
- [ ] Other requested document: _e.g. transcript, work sample_

## Sensitive / must-confirm before submit
- Anything needing a human decision: _salary above stated range, work auth
  attestation, conflict disclosure, demographic questions._
- **The agent does not click Submit. You do.**

## Submit checklist
- [ ] All required fields non-empty
- [ ] No `TODO` or `[ ]` left in this file
- [ ] Attachments attached, correct versions
- [ ] `tracker.csv` row updated to `applied` (via the `log` skill)
