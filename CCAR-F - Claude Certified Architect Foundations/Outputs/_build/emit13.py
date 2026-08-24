# -*- coding: utf-8 -*-
"""Clone the Exam 12 shell (AI Oracle Quiz v2 design system) and swap in Exam 13's data + landing card."""
import re, io, os, json

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(BUILD))
MOCKS = os.path.join(ROOT, "prep with quiz", "mock-exams")
SRC = os.path.join(MOCKS, "CCA-Prep_MockTest-12_v1.html")
OUT = os.path.join(MOCKS, "CCA-Prep_MockTest-13_v1.html")

s = io.open(SRC, encoding="utf-8").read()
data = json.load(io.open(os.path.join(BUILD, "exam13.json"), encoding="utf-8"))

# ---- swap the DATA payload -------------------------------------------------
i = s.find("const DATA")
j = s.find("{", i); d = 0
for k in range(j, len(s)):
    if s[k] == "{": d += 1
    elif s[k] == "}":
        d -= 1
        if d == 0:
            end = k + 1
            break
s = s[:j] + json.dumps(data, ensure_ascii=False) + s[end:]

# ---- storage key -----------------------------------------------------------
s = s.replace('const KEY = "cca-mock-12"', 'const KEY = "cca-mock-13"')

# ---- hero + landing card ---------------------------------------------------
s = re.sub(r"<h1>Mock Test <em>\d+</em></h1>", "<h1>Mock Test <em>13</em></h1>", s)
s = re.sub(r'<h3>Exam \d+ · Generated [\d-]+</h3>',
           "<h3>Exam 13 · Generated 2026-08-11 · your last paper before the real one</h3>", s, count=1)

s = re.sub(r'(<div class="sf"><div class="k">Domain quota[^<]*</div><div class="v">)[^<]*(</div></div>)',
           r"\g<1>D1 16 · D2 11 · D3 12 · D4 12 · D5 9 (base weights)\g<2>", s, count=1)
s = re.sub(r'(<div class="sf"><div class="k">Last scored exam</div><div class="v">)[^<]*(</div></div>)',
           r"\g<1>Exam 11: 55/60 (925), attempted 2026-08-10 — your joint best\g<2>", s, count=1)

# scenario list
scen = "".join("<li>%s</li>" % b["label"] for b in data["blocks"])
s = re.sub(r'<ul class="scen-list">.*?</ul>', '<ul class="scen-list">%s</ul>' % scen, s, count=1, flags=re.S)

# targeting note
target = (
 "This is a confidence paper, not a trap paper. The domain quota is the base weighting — no weakness "
 "adjustment applies, because Exam 9 and Exam 11 named different weakest domains, so nothing is confirmed. "
 "What is targeted is section choice inside that fixed quota. Every concept you have missed more than once "
 "across eight scored papers appears here at least once: composite-tool versus prompt bundling (missed five "
 "papers running), two-tool token binding (three), the tool_use/tool_result loop (three), CLAUDE.md "
 "concatenation (three), tool-description scope, Grep versus Glob, coordinator decomposition, "
 "AgentDefinition tool restriction, allowed-tools versus context: fork, and the reasoning-cue versus "
 "few-shot distinction. Two single misses from Exam 11 get their second formal test: over-escalation of a "
 "resolvable ambiguity, and evaluator-optimizer versus context isolation. Scenario draw rests Developer "
 "Productivity and CI/CD, the two most-used blocks, and brings all six to equal usage.")
s = re.sub(r'(<div class="sf" style="margin-top:12px;background:rgba\(255,255,255,0\.6\)"><div class="k">)'
           r'Targeting this paper[^<]*(</div><div class="v"[^>]*>)[^<]*(</div>)',
           lambda m: m.group(1) + "Targeting this paper — sat 2026-08-11, one week before the real exam" +
                     m.group(2) + target + m.group(3), s, count=1)

io.open(OUT, "w", encoding="utf-8").write(s)
print("wrote", OUT)
print("size %.0f KB" % (os.path.getsize(OUT) / 1024.0))
