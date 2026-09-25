---
name: apply-external
description: Complete a job application on a company site or ATS (Workday, Greenhouse, Lever, Ashby, Jobright, others), including sign-in and account creation. Use when an Apply ↗ link leaves LinkedIn or Hadi gives an application URL.
---

# External application

Goal: a submitted application with correct information. Every site differs; use judgment toward that goal.
Browser: Claude in Chrome tools only. No host-level mouse clicks.

## Before starting
Know title, company, track and any posted salary range. If called directly, read the
posting (`get_page_text`) and apply the fit rules from `apply-linkedin`.

## Steps
1. Click Apply. Wait through any `linkedin.com/safety/go` redirect. On the company page click its own Apply.
2. Sign-in or account wall → Authentication.
3. Read the whole form first. List every required field, especially a resume upload at the top.
4. Fill:
   - Resume: upload `profile/resumes/<track>/resume-<track>.pdf` via My Device / upload.
     Ignore Dropbox / OneDrive. "Autofill from resume" is allowed; verify every field after.
   - Chrome or site autofill is allowed. Verify each value against `answers.md` and fix
     mismatches. Street address precision is low priority; city, province, country and
     postal code must be right.
   - Contact: First Hadi, Last Amiri, email, country code Canada (+1), phone without
     country code, phone type Cell.
   - Current / most recent title: per track in `answers.md`.
   - Salary: posted range → its minimum, but not below 85,000 CAD. No range → 85,000 CAD. Annual.
   - SMS consent: agree.
   - LinkedIn, work authorization, education: `answers.md` / `facts.md`. GitHub and portfolio: blank.
   - Screening questions: rules in `apply-linkedin`.
   - Cover letter: only if the field is required. Run `cover-letter` for this job and upload
     the PDF. Optional field: skip.
5. Submit per `submit_mode`. On validation errors, fix the flagged fields and resubmit.
6. Count as applied only when a confirmation / thank-you page appears.
7. Close the tab, return to LinkedIn. "Did you finish applying?" → Yes. Log it.

## Authentication
Hadi authorizes sign-in and account creation for job applications.
- Sign in: if Chrome has filled saved credentials, click Sign in. "Continue with Google"
  or LinkedIn: choose `mhadiamiri27@gmail.com`.
- Create account: `mhadiamiri27@gmail.com` plus details from `answers.md`. For the password,
  use Chrome's suggested strong password so Chrome saves it.
- Never write a password into chat, files, or `tracker.csv`.
- Email verification: open Gmail in a new tab, open the newest message from that
  company, use the code or link, close the tab.
- Workday: each company has its own account. Same email every time.
- Passkey / Windows Hello, CAPTCHA, or any step the tools cannot complete: do not stall.
  Park the job as `waiting-auth` with URL and reason, move to the next job. Hadi handles
  all `waiting-auth` jobs together at the end of the session.
- In tracker notes write "account created on <site>" (never the password).

## Jobright-hosted postings
If the link lands on `jobright.ai` and a Jobright profile exists: Send my profile /
Direct Apply, confirm contact info and the original resume (not a Jobright template
or generated resume), submit, wait for confirmation.

## Guardrails
- No Jobright sidebar Autofill, credits, custom resumes or generated cover letters unless asked.
- A Chrome tool fails 2 to 3 times on one step: park the job, move on.
