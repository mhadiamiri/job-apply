#!/usr/bin/env python3
"""sync_resumes.py - generate the text mirrors the agent actually reads.

For each resume base, read the user-owned source, write a Markdown mirror next
to it, run the project's own voice linter against the mirror, and print the
facts inventory (word count, experience entries, years, numbers) that feeds
profile/facts.md.

Sources are the base PDFs, in preference order, per step 01b:

  data  profile/resumes/data/resume-data.pdf
  ai    profile/resumes/ai/resume-ai.pdf          <- preferred, ATS-readable
        profile/resumes/ai/resume-ai.legacy.txt   <- fallback, prints a warning

The AI base currently has no `resume-ai.pdf`: the only AI PDF present is
`resume-ai.legacy.pdf`, which has no text layer (0 characters, 0 images, 0
fonts). The fallback transcription is used until the user re-exports it, and a
warning says the AI PDF is not ATS-readable yet.

The script NEVER rewrites a source. It only reads them and writes mirrors.

Exit code is always 0: this is a reporting tool, not a gate.

Usage:  python scripts/sync_resumes.py
"""

import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

BASES = (
    {
        "name": "data",
        "dir": os.path.join(ROOT, "profile", "resumes", "data"),
        "pdf": "resume-data.pdf",
        "fallback": None,  # extract from the PDF
    },
    {
        "name": "ai",
        "dir": os.path.join(ROOT, "profile", "resumes", "ai"),
        "pdf": "resume-ai.pdf",  # preferred source, not present yet
        "fallback": "resume-ai.legacy.txt",  # used until the user re-exports
    },
)

HEADER = (
    "<!-- GENERATED from resume-{name}.pdf by scripts/sync_resumes.py. "
    "Do not edit. -->"
)

# Section headings that become "##" in the mirror.
SECTIONS = (
    "SUMMARY", "WORK EXPERIENCE", "EDUCATION", "SKILLS", "LANGUAGES",
    "CERTIFICATES AND CLEARANCES", "PROJECTS", "PUBLICATIONS", "AWARDS",
)

YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b")
SIMPLE_NUMBER_RE = re.compile(r"\b\d[\d,]*(?:\.\d+)?\s?(?:%|x|M|s|h)?\+?\b")
DATE_RANGE_RE = re.compile(
    r"\b(?:19|20)\d{2}\s*[-\u2013\u2014]\s*(?:present|(?:19|20)\d{2})\b", re.I
)


def load_linter():
    """Import lint_file() from the project's hook. Never copy it."""
    path = os.path.join(ROOT, ".claude", "hooks", "check_voice.py")
    spec = importlib.util.spec_from_file_location("check_voice", path)
    if spec is None or spec.loader is None:
        raise ImportError("cannot load %s" % path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def to_markdown(text, name):
    """Map source text to Markdown, preserving wording and order exactly.

    heading styles -> #/##, list paragraphs -> "- ", bold runs -> **bold**,
    tables -> Markdown tables. The PDFs carry no style names, so structure is
    recovered from the known section headings and the visual layout: a line
    that already begins with a bullet glyph is a list item; a pipe-delimited
    line is a table; a short leading line is the name heading.
    """
    out = [HEADER.format(name=name)]
    seen_section = False
    for raw in text.splitlines():
        stripped = raw.strip()
        if not stripped:
            if out and out[-1] != "":
                out.append("")
            continue

        # Tables: 2+ pipe-separated cells -> a Markdown table row.
        if stripped.count("|") >= 2 and not stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            out.append("| " + " | ".join(cells) + " |")
            continue

        # Existing bullet glyphs -> "- "
        if stripped[0] in "\u2022\u25aa\u25cf-\u2013*":
            body = stripped.lstrip("\u2022\u25aa\u25cf-\u2013* ").strip()
            out.append("- " + body)
            continue

        # Section headings (uppercase in the source) -> "##"
        upper = stripped.upper().strip(":")
        if upper in SECTIONS:
            seen_section = True
            out.extend(["", "## " + upper.title(), ""])
            continue

        # Leading short line (the candidate name) -> "# "
        if not seen_section and len(stripped.split()) <= 4:
            out.append("# " + stripped)
            continue

        out.append(stripped)

    return "\n".join(out).rstrip() + "\n"


def experience_entries(text):
    """Count dated experience/education entries (e.g. '2024 - Present')."""
    return len(DATE_RANGE_RE.findall(text))


def numbers_in(text):
    """Unique numbers, percentages and multiples, in order of appearance."""
    found = []
    for m in SIMPLE_NUMBER_RE.finditer(text):
        tok = m.group(0).strip()
        if len(tok) > 1 and tok not in found:
            found.append(tok)
    return found


def main():
    print("=" * 70)
    print("sync_resumes.py - mirrors + facts inventory")
    print("=" * 70)

    try:
        check_voice = load_linter()
    except Exception as exc:  # noqa: BLE001
        print("FATAL: could not import check_voice.py: %s" % exc)
        return 0

    for base in BASES:
        name = base["name"]
        print("\n" + "#" * 70)
        print("# BASE: %s" % name)
        print("#" * 70)
        print("source dir: profile/resumes/%s" % name)

        text, note, warn = extract_text(base)
        if text is None:
            print("SKIPPED: %s" % note)
            continue
        print("text origin: %s" % note)
        if warn:
            print("!! %s" % warn)

        md = to_markdown(text, name)
        mirror = os.path.join(base["dir"], "resume-%s.md" % name)
        with open(mirror, "w", encoding="utf-8") as fh:
            fh.write(md)
        print("mirror written: profile/resumes/%s/resume-%s.md (%d bytes)"
              % (name, name, len(md.encode("utf-8"))))

        # Voice lint. check_voice.main() only lints paths under /applications/,
        # so call lint_file() directly. Report only: sources are never modified.
        print("\n-- voice lint (REPORT ONLY; sources are not modified) --")
        findings = check_voice.lint_file(mirror)
        if findings:
            for line_no, line, label in findings:
                print("   L%-4d [%-18s] %s"
                      % (line_no, label, line.strip()[:88]))
            print("   -> %d finding(s). Fix these in the SOURCE, then re-run."
                  % len(findings))
        else:
            print("   clean")

        words = len(re.findall(r"[A-Za-z0-9']+", text))
        years = sorted(set(YEAR_RE.findall(text)))
        nums = numbers_in(text)

        print("\n-- facts inventory (feeds profile/facts.md) --")
        print("   word count          : %d" % words)
        print("   experience entries  : %d" % experience_entries(text))
        print("   years found         : %s" % ", ".join(years))
        print("   numbers/percentages : %d found" % len(nums))
        for n in nums:
            print("      %s" % n)

    print("\n" + "=" * 70)
    print("Done. Sources untouched. Mirrors are generated - do not hand-edit.")
    print("=" * 70)
    return 0


def extract_text(base):
    """Return (text, note, warn) for a base.

    Preference order: the base PDF. If it is absent, fall back to the
    transcription and warn that the PDF is not ATS-readable yet.
    """
    pdf_path = os.path.join(base["dir"], base["pdf"])
    warn = None

    if os.path.exists(pdf_path):
        try:
            from pypdf import PdfReader
        except ImportError:
            return None, "pypdf not installed (pip install pypdf)", None
        reader = PdfReader(pdf_path)
        text = "\n".join((pg.extract_text() or "") for pg in reader.pages)
        if len(text.strip()) < 500:
            warn = ("WARNING: %s extracted %d characters (< 500): not "
                    "ATS-readable. Re-export it with a text layer."
                    % (base["pdf"], len(text.strip())))
        return text, "extracted from %s" % base["pdf"], warn

    # Preferred PDF missing: fall back, and say so loudly.
    if not base["fallback"]:
        return None, "source PDF missing: %s" % base["pdf"], None
    fb = os.path.join(base["dir"], base["fallback"])
    if not os.path.exists(fb):
        return None, ("source PDF missing: %s (and no fallback %s)"
                      % (base["pdf"], base["fallback"])), None
    with open(fb, "r", encoding="utf-8") as fh:
        text = fh.read()
    warn = ("WARNING: %s is not ATS-readable yet - the AI PDF has no text "
            "layer. Using the %s transcription instead. Re-export the AI "
            "resume as a text-layer PDF to fix this."
            % (base["pdf"], base["fallback"]))
    return text, "fallback %s (preferred PDF %s absent)" % (
        base["fallback"], base["pdf"]), warn



if __name__ == "__main__":
    sys.exit(main())
