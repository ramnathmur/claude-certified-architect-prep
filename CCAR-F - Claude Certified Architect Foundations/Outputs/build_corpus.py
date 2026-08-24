"""Assemble the 7 source corpus files into one self-contained grounding corpus.

Verbatim body extraction. The only edits are:
  - drop each file's project-metadata header (everything before its first '---')
  - render section headings as '## SECTION N.M Title' -> '## \u00a7N.M Title'
  - rewrite cross-file refs ('CCA-Prep_Domain-2_v2.md \u00a72.9') to bare '\u00a72.9'
  - drop pointers to files that do not travel
No content is summarised, reworded, or reordered.
"""
import re
import os

SRC = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz"
OUT = (r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\Outputs"
       r"\CCA-F_Generator-Corpus_v1.md")

PARTS = [
    ("CCA-Prep_Exam-Mechanics_v2.md",  "Part 0 - Exam mechanics"),
    ("CCA-Prep_Domain-1_v2.md",        "Part 1 - Domain 1: Agentic Architecture & Orchestration (27%)"),
    ("CCA-Prep_Domain-2_v2.md",        "Part 2 - Domain 2: Tool Design & MCP Integration (18%)"),
    ("CCA-Prep_Domain-3_v2.md",        "Part 3 - Domain 3: Claude Code Configuration & Workflows (20%)"),
    ("CCA-Prep_Domain-4_v2.md",        "Part 4 - Domain 4: Prompt Engineering & Structured Output (20%)"),
    ("CCA-Prep_Domain-5_v2.md",        "Part 5 - Domain 5: Context Management & Reliability (15%)"),
    ("CCA-Prep_Key-Distinctions_v1.md","Part 6 - Key Distinctions: high-yield exam traps"),
]

SECTION = "\u00a7"   # section sign


def strip_header(text):
    """Return everything after the file's first '---' rule, plus a kept Purpose line."""
    lines = text.split("\n")
    purpose = [l for l in lines[:12] if l.startswith("**Purpose:**")]
    for i, l in enumerate(lines):
        if l.strip() == "---":
            body = "\n".join(lines[i + 1:]).lstrip("\n")
            return (("\n".join(purpose) + "\n\n") if purpose else "") + body
    raise SystemExit("no '---' header terminator found")


def clean(text):
    # heading '## 1.1 Title' -> '## §1.1 Title' (domain files only; harmless elsewhere)
    text = re.sub(r"^## (\d+\.\d+) ", r"## " + SECTION + r"\1 ", text, flags=re.M)
    # cross-file section refs -> bare section refs
    text = re.sub(r"`?CCA-Prep_Domain-\d_v2\.md`?\s*" + SECTION, SECTION, text)
    text = re.sub(r"`?CCA-Prep_Exam-Mechanics_v2\.md`?\s*" + SECTION, SECTION, text)
    text = re.sub(r"`?CCA-Prep_Key-Distinctions_v1\.md`?\s*#?", "Part 6", text)
    # "see CCA-Prep_Domain-4_v2.md and CCA-Prep_Domain-5_v2.md" -> "see Domain 4 and Domain 5"
    text = re.sub(r"`?CCA-Prep_Domain-(\d)_v2\.md`?", r"Domain \1", text)
    # pointers to files that do not travel
    text = re.sub(r"\s*\(?See `?CURRENT-DOCS-DELTA_v1\.md`?[^.)]*\.?\)?", "", text)
    text = re.sub(r"`?CURRENT-DOCS-DELTA_v1\.md`?", "the currency notes", text)
    text = re.sub(r"`?PRACTICE-TEST-STEMS_v1\.md`?[^.]*\.", "the shipped practice tests.", text)
    text = re.sub(r"`?source/CCA-F-Official-Exam-Guide[^`]*`?", "the official Exam Guide", text)
    text = re.sub(r"`?source/guide_en\.md`?", "the community study guide", text)
    text = re.sub(r"guide_en\.MD", "the community study guide", text)
    # dead pointer into a log file that does not travel; the rule itself is kept
    text = re.sub(r"\s*\(see `?EXAM-LOG\.md`? line \d+\)", "", text)
    return text


FRONT = """# CCA-F Grounding Corpus

**What this is.** The complete subject-matter corpus for the Anthropic Claude Certified
Architect - Foundations exam (official exam code CCAR-F), in one file. It is the source of
truth for generating practice questions: every question written from it must trace to a
numbered section here.

**How sections are numbered.** Sections run """ + SECTION + """1.1 through """ + SECTION + """5.x, grouped by exam domain,
plus a final set of high-yield traps. Cite them in the form `Corpus """ + SECTION + """1.6`. Keep the
""" + SECTION + """ symbol - the practice-test renderer matches on it to build a live link, and a citation
without it renders as dead plain text.

**Where it comes from.** Written against Anthropic's official CCA-F Exam Guide - its five
domains and weights, its thirty task statements, its six exam scenarios, and its in-scope
and out-of-scope lists. A community study guide
(github.com/paullarionov/claude-certified-architect) was used as a depth source for
explanation, never as authority on exam facts. Where the two disagree, the official guide
wins.

**Currency.** Authored against Exam Guide v0.2 and re-checked against v1.0 (effective
July 2026). A measured diff found the domain weights, all six scenarios, all thirty task
statements and both scope lists identical between the two. Anything decision-critical
should still be confirmed against the guide currently published on the Anthropic Partner
Academy.

**Not affiliated with, endorsed by, or sponsored by Anthropic.** This is study material.
It contains no real exam questions.

---

## Contents

| Part | Covers | Sections |
|---|---|---|
| 0 | Exam mechanics - format, weights, scenario bank, scope lists, scoring | - |
| 1 | D1 Agentic Architecture & Orchestration (27%) | """ + SECTION + """1.1-""" + SECTION + """1.18 |
| 2 | D2 Tool Design & MCP Integration (18%) | """ + SECTION + """2.1-""" + SECTION + """2.9 |
| 3 | D3 Claude Code Configuration & Workflows (20%) | """ + SECTION + """3.1-""" + SECTION + """3.12 |
| 4 | D4 Prompt Engineering & Structured Output (20%) | """ + SECTION + """4.1-""" + SECTION + """4.20 |
| 5 | D5 Context Management & Reliability (15%) | """ + SECTION + """5.1-""" + SECTION + """5.14 |
| 6 | Key Distinctions - 29 documented exam traps | - |

---
"""

chunks = [FRONT]
report = []
for fname, title in PARTS:
    raw = open(os.path.join(SRC, fname), encoding="utf-8").read()
    body = clean(strip_header(raw))
    chunks.append("\n\n# " + title + "\n\n" + body.strip() + "\n")
    report.append((fname, len(raw.split()), len(body.split())))

out = "\n".join(chunks)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(out)

print("WROTE", OUT)
print("bytes:", len(out), "| words:", len(out.split()))
print()
for f, a, b in report:
    print(f"  {f:34} {a:>6}w source -> {b:>6}w kept  ({b*100//a}%)")
print()
secs = re.findall(r"^## " + SECTION + r"(\d+\.\d+)", out, flags=re.M)
print("numbered sections emitted:", len(secs))
by_dom = {}
for s in secs:
    by_dom.setdefault(s.split(".")[0], []).append(s)
for d in sorted(by_dom):
    print(f"   D{d}: {len(by_dom[d]):>2} sections  {by_dom[d][0]} .. {by_dom[d][-1]}")
leaks = re.findall(r"CCA-Prep_[\w\-]+\.md|EXAM-LOG|SESSION-STATE|GENERATION-INTELL|orchestration prompt", out)
print()
print("internal-file leaks remaining:", len(leaks), sorted(set(leaks))[:6])
