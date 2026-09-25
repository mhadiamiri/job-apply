#!/usr/bin/env python3
"""check_voice.py — PostToolUse hook enforcing profile/voice.md.

Reads the Claude Code PostToolUse hook payload on stdin, inspects any Markdown
files that were just written or edited, and reports banned marketing language.

Exit code 0 always: advisory feedback is surfaced in the transcript, it does not
block the tool call. Run standalone to lint files:

    python .claude/hooks/check_voice.py applications/2026-09-24_acme_acme/cover-letter.md
"""

import json
import os
import re
import sys

# (pattern, label) — patterns come from the "Hard bans" list in profile/voice.md
BANNED = [
    (r"\bpassionate\b", "hollow superlative"),
    (r"\bdynamic\b", "hollow superlative"),
    (r"\bresults[- ]driven\b", "hollow superlative"),
    (r"\bdetail[- ]oriented\b", "hollow superlative"),
    (r"\bteam player\b", "hollow superlative"),
    (r"\bself[- ]starter\b", "hollow superlative"),
    (r"\bhard[- ]?working\b", "hollow superlative"),
    (r"\bproven track record\b", "hollow superlative"),
    (r"\bcutting[- ]edge\b", "hollow superlative"),
    (r"\bworld[- ]class\b", "hollow superlative"),
    (r"\bbest[- ]in[- ]class\b", "hollow superlative"),
    (r"\bsynerg", "corporate filler"),
    (r"\bspearhead", "corporate filler"),
    (r"\butiliz", "prefer 'use'"),
    (r"\brobust solution\b", "corporate filler"),
    (r"\bI am writing to (apply|express my interest)\b", "filler opener"),
    (r"\bI am excited to apply\b", "filler opener"),
    (r"\bI believe I would be a great fit\b", "filler opener"),
    (r"\bhit the ground running\b", "cliche"),
    (r"\bwear many hats\b", "cliche"),
    (r"\bthink outside the box\b", "cliche"),
    (r"\bgo[- ]getter\b", "cliche"),
    (r"\bcircle back\b", "cliche"),
    (r"\bat the end of the day\b", "cliche"),
    (r"\bincredibly\b", "weasel intensifier"),
    (r"\bextremely\b", "weasel intensifier"),
    (r"\bhighly skilled\b", "weasel intensifier"),
    (r"!", "exclamation mark"),
]

COMPILED = [(re.compile(p, re.IGNORECASE), label) for p, label in BANNED]

# Only generated application documents are linted. The rules/profile files are
# user-authored inputs, not deliverables, so they are never flagged.
TARGET_SUFFIX = ".md"
SECTIONS = ("applications",)

EM_DASH = "\u2014"
WORD_RE = re.compile(r"[A-Za-z0-9']+")
# Minimum words on each side of an em-dash before it counts as a prose crutch.
CLAUSE_WORDS = 6


def _words(text):
    return WORD_RE.findall(text)


def punctuation_findings(line):
    """Context-aware checks for the punctuation bans in voice.md.

    An em-dash is only a crutch when it joins two real clauses (several words on
    each side). Used as a field or label separator ("**Hook - one or two
    sentences.**", "Institution - year") it is formatting, not prose, and is
    left alone. Lines with no em-dash are never flagged.
    """
    out = []
    if EM_DASH in line:
        clauses = [_words(part) for part in line.split(EM_DASH)]
        if all(len(c) >= CLAUSE_WORDS for c in clauses):
            out.append((line, "em-dash crutch"))
    if "!!" in line or re.search(r"\w!\s*$", line.strip()):
        out.append((line, "double/stretched exclamation"))
    return out


def lint_file(path):
    """Return a list of (line_no, line, label) findings for one file."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
    except (OSError, UnicodeDecodeError):
        return []

    findings = []
    in_fence = False
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped or stripped.startswith("#"):
            continue
        # Generated-file notices and other HTML comments are metadata, not prose.
        if stripped.startswith("<!--"):
            continue
        for regex, label in COMPILED:
            m = regex.search(line)
            if m:
                findings.append((i, line.rstrip(), label))
                break
        else:
            for _text, label in punctuation_findings(line):
                findings.append((i, line.rstrip(), label))
    return findings


def paths_from_payload(payload):
    """Extract edited file paths from a PostToolUse hook payload."""
    found = []
    tool_input = payload.get("tool_input") or {}
    for key in ("file_path", "notebook_path"):
        if tool_input.get(key):
            found.append(tool_input[key])
    for key in ("edits",):
        for edit in tool_input.get(key) or []:
            if isinstance(edit, dict) and edit.get("file_path"):
                found.append(edit["file_path"])
    content = tool_input.get("content") or tool_input.get("new_string")
    if isinstance(content, str) and tool_input.get("file_path"):
        found.append(tool_input["file_path"])
    return found


def main():
    argv = sys.argv[1:]
    raw = sys.stdin.read() if not sys.stdin.isatty() else ""

    if argv:
        candidates = [os.path.abspath(p) for p in argv]
    else:
        try:
            payload = json.loads(raw) if raw.strip() else {}
        except ValueError:
            payload = {}
        candidates = [os.path.abspath(p) for p in paths_from_payload(payload)]

    report = []
    for path in candidates:
        if not path.lower().endswith(TARGET_SUFFIX):
            continue
        norm = path.replace("\\", "/")
        if not any("/%s/" % s in norm for s in SECTIONS):
            continue
        findings = lint_file(path)
        if not findings:
            continue
        report.append((path, findings))

    if report:
        print("check_voice: voice.md violations found\n")
        for path, findings in report:
            rel = os.path.basename(path)
            print("  %s" % rel)
            for line_no, line, label in findings:
                print("    L%-4d [%s] %s" % (line_no, label, line.strip()[:100]))
            print("")
        print("Fix these in profile/voice.md terms before exporting a .docx/.pdf.")
    else:
        print("check_voice: clean")

    return 0


if __name__ == "__main__":
    sys.exit(main())
