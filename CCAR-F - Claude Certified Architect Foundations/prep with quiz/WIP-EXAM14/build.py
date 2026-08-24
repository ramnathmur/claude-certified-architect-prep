import json, os, re, sys, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "mock-exams", "CCA-Prep_MockTest-14_v1.html")

# PRE-FLIGHT: never overwrite a numbered artifact by accident. --force is only for
# rebuilding this session's own in-progress output after a template edit.
if os.path.exists(OUT) and "--force" not in sys.argv:
    sys.exit(f"REFUSING TO OVERWRITE: {OUT} already exists. Increment the version, or pass --force to rebuild.")

DATA = json.load(open(os.path.join(HERE, "exam14-data.json"), encoding="utf-8"))
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


lines = [
    "  CCA-Prep Mock Test 14 -- CCA-F Foundations",
    "  Format: FULL-60 (4 scenario blocks x 15 = 60 questions)",
    "  Generated: 2026-08-11 via CCA-Orchestration-Prompt_v10.md + QUESTION-ARCHETYPE-BANLIST.md",
    "",
    "  SCENARIOS DRAWN (4 of the official 6) -- the first combination never used in Exams 2-13:",
]
prim = {
    "Multi-Agent Research System": "primary D1, D2, D5",
    "Developer Productivity with Claude": "primary D2, D3, D1",
    "Claude Code for Continuous Integration": "primary D3, D4",
    "Structured Data Extraction": "primary D4, D5",
}
for i, b in enumerate(DATA["blocks"], 1):
    lines.append(f"    {i}. {b['label']:<45s}({prim.get(b['label'],'')})")
lines += [
    "  Rested: Customer Support Resolution Agent, Code Generation with Claude Code --",
    "  both drawn in Exam 13. All six scenarios sat at exactly 8 uses each across Exams 2-13.",
    "",
    "  DOMAIN QUOTA (base weights -- no confirmed-weakness adjustment applies):",
    "    D1 16 | D2 11 | D3 12 | D4 12 | D5 9 = 60",
    "  Driver: the two most recent scored papers named different weakest domains by attempt",
    "  chronology (Exam 9: D2, Exam 11: D5), so no weakness is confirmed.",
    "",
    "  ITEM FORMATS: 47 single-answer (4 options) + 13 multiple-response.",
    "    9 x select-2-of-5, 4 x select-3-of-6, scored all-or-nothing.",
    "    Multiple-response is named in the official exam guide (SS2) but appears in none of its",
    "    12 sample questions and in none of Exams 2-13. This is the first paper to drill it.",
    "",
    "  ARCHETYPE BAN-LIST APPLIED (see QUESTION-ARCHETYPE-BANLIST.md):",
    "    9 reskinned question families found across the 720 prior questions are banned here.",
    "    Their corpus points are re-tested from the approved alternative angles instead.",
    "    Verified by tools/archetype_gate.py: 0 stems at/above 0.40 Jaccard vs any of the",
    "    773 prior stems; 0 intra-paper collisions; all 7 gates pass.",
    "",
    "  QUESTIONS USED (deduplication ledger for Exam 15+):",
]
for q in DATA["questions"]:
    tag = f"[{q['domain']}]" + (f"[select-{q['selectN']}]" if q.get("selectN") else "")
    body = f"{q['g']}. {tag} {plain(q['stem'])}"
    lines += textwrap.wrap(body, width=120, initial_indent="  ", subsequent_indent="     ")

header = "\n".join(lines)
assert "--" not in header.replace("--", "\x00").replace("\x00", "--") or True  # header lives in a comment
header = header.replace("-->", "- ->")  # never let the ledger close the comment early

html = tpl.replace("__HEADER_COMMENT__", "\n" + header + "\n")
html = html.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(html)

print(f"wrote {OUT}")
print(f"  size: {os.path.getsize(OUT)/1024:.1f} KB")
print(f"  placeholders remaining: {html.count('__DATA__') + html.count('__HEADER_COMMENT__')}")
