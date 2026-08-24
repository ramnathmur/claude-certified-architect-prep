"""Derive a standalone renderer shell from Ram's pack test, cutting every
dependency on the prep pack.

Three couplings are removed:
  1. <nav class="packbar"> - six links into pack files
  2. citeHref()            - linked citations into the pack's corpus HTML
  3. results 'study' links - four per-domain links into pack files

Everything else (layout, pagination, hint mode, timer, scoring, JSON export,
localStorage) is untouched. The DATA object becomes a marked placeholder.
"""
import re

SRC = (r"C:\Claude Cowork\Projects\Claude Certified Architect Prep"
       r"\Claude-Certified-Architect-Foundations_Exam-Prep_v1\Mock tests\Test-1.html")
OUT = (r"C:\Claude Cowork\Projects\Claude Certified Architect Prep"
       r"\Outputs\CCA-F_Test-Shell-Blank_v1.html")

s = open(SRC, encoding="utf-8").read()

# ---- split off the DATA object -------------------------------------------
i = s.index("const DATA = ")
start = s.index("{", i)
depth = 0
for j in range(start, len(s)):
    if s[j] == "{":
        depth += 1
    elif s[j] == "}":
        depth -= 1
        if depth == 0:
            end = j + 1
            break
pre, post = s[:start], s[end:]

checks = {}

# ---- 1. packbar nav -------------------------------------------------------
pre, n = re.subn(r'<nav class="packbar".*?</nav>\s*', "", pre, flags=re.S)
checks["packbar nav removed"] = n == 1

# ---- 2. citeHref: plain-text citations ------------------------------------
new_cite = ('function citeHref(cite){\n'
            '  // Standalone build: citations render as plain text.\n'
            '  // Look the section up in CCA-F_Generator-Corpus_v1.md by its \u00a7 number.\n'
            '  return "";\n}')
pre, n = re.subn(r"function citeHref\(cite\)\{.*?\n\}", new_cite, pre, flags=re.S)
checks["citeHref neutralised"] = n == 1

# ---- 3. results-card study links ------------------------------------------
pre, n = re.subn(r'const study=`<div class="rc-study">.*?</div>`;',
                 'const study="";', pre, flags=re.S)
checks["study links removed"] = n == 1

# ---- 4. storage key placeholder -------------------------------------------
pre, n = re.subn(r'const KEY = "cca-public-\d+";',
                 'const KEY = "cca-test-1";   // bump per generated test', pre)
checks["storage key parameterised"] = n == 1

# ---- 5. DATA placeholder ---------------------------------------------------
placeholder = ('{\n  /* REPLACE THIS ENTIRE OBJECT WITH YOUR GENERATED EXAM DATA. */\n'
               '  "exam_n": 1, "format": "FULL60",\n'
               '  "quota": {"D1": 16, "D2": 11, "D3": 12, "D4": 12, "D5": 9},\n'
               '  "domainNames": {"D1": "Agentic Architecture & Orchestration",\n'
               '    "D2": "Tool Design & MCP Integration",\n'
               '    "D3": "Claude Code Configuration & Workflows",\n'
               '    "D4": "Prompt Engineering & Structured Output",\n'
               '    "D5": "Context Management & Reliability"},\n'
               '  "blocks": [], "questions": []\n}')
out = pre + placeholder + post

open(OUT, "w", encoding="utf-8").write(out)

print("WROTE", OUT)
print("bytes:", len(out))
print()
for k, v in checks.items():
    print(f"  {'PASS' if v else 'FAIL'}  {k}")
print()
leaks = re.findall(r"\.\./Learning%20corpus/[^\"`)]*|\.\./README\.html|Test-MR\.html|Dashboard\.html", out)
print("remaining pack references:", len(leaks), sorted(set(leaks))[:6])
print("literal 60 count (should match original):", len(re.findall(r"(?<![\d.])60(?![\d])", out)))
