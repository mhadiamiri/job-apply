# Cover Letter — Acme, Applied AI Engineer

Styled from `templates/cover-letter.docx`. Voice rules in `profile/voice.md` are
enforced by the `check_voice.py` hook.

Pipeline: `cover-letter.md` → `cover-letter.docx` → `cover-letter.pdf`

---

[Date]

Hiring Team
Acme

Dear [Name / Hiring Team],

**Hook — one or two sentences.** A specific thing about Acme's actual work or
this role's mandate that a generic applicant would not have written. Name the
problem in their language, taken from `jd.md`.

**Evidence — two short paragraphs or two bullets.** Concrete work, each ending
in a number from `profile/facts.md`. Show the shape of the role: [capability
they asked for] maps to [what you have actually done].

**Fit — one honest sentence.** Where you overlap, and where you don't, said
plainly. One gap, with why it doesn't stop you.

**Close — one sentence.** Clear ask, no flattery. Availability and where to
reach you.

Sincerely,
[Name]

---
## Notes (delete before export)
- Hook ties to: _which line of `jd.md` / which company fact_
- Claims used: _facts.md lines, for verification_
- Known gap acknowledged: _or "none"_
