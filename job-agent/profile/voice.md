# Voice

How written output must read. Enforced by `.claude/hooks/check_voice.py`.

## Personality
- Plain, direct, professional. Senior-engineer register, not marketing.
- Confident, never boastful. State the work, then stop.
- Sentence case for headings. No exclamation marks.

## Hard bans
The following never appear in any generated document:

- Hollow superlatives: `passionate`, `dynamic`, `results-driven`, `detail-oriented`,
  `team player`, `self-starter`, `hardworking`, `proven track record`,
  `cutting-edge`, `world-class`, `best-in-class`, `synergy`, `leverage` (as a verb),
  `spearhead`, `utilize` (use "use"), `robust solution`
- Filler openers: `I am writing to apply`, `I am excited to apply`,
  `I believe I would be a great fit`, `I am writing to express my interest`
- Clichés: `hit the ground running`, `wear many hats`, `think outside the box`,
  `go-getter`, `reach out`, `circle back`, `at the end of the day`
- Em-dashes used as a crutch, and exclamation marks
- Weasel intensifiers: `very`, `extremely`, `incredibly`, `highly skilled`
- First-person plural (`we`, `our team`) in documents about your own experience

## Structure
- Resume bullets: `<strong verb> <what you did> → <measurable result>`. One line.
  Prefer a number. If no honest number exists, name the scope instead
  (team size, users, services, data volume) rather than inflating.
- Cover letter: 4 short paragraphs max — hook tied to the company's actual work,
  2 concrete evidence bullets, one honest fit line, one clear close.
- No bullet in a cover letter that just restates a resume line.

## Accuracy
- Every claim traces to `facts.md` or `master-resume.docx`.
- Never invent metrics, employers, titles, dates, or clearance.
- Keyword-matched phrasing is fine; keyword-stuffed sentences are not.
