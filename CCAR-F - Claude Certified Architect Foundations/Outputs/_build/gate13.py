# -*- coding: utf-8 -*-
"""Exam 13 fidelity gates. Everything is computed, nothing is hand-counted."""
import re, io, os, sys, json, collections, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exam13_a as A
import exam13_b as Bm

BUILD = os.path.dirname(os.path.abspath(__file__))
QS = A.Q + Bm.Q
BLOCKS = [A.BLOCK1, A.BLOCK2, Bm.BLOCK3, Bm.BLOCK4]
PRIMARY = {0: {"D1", "D2", "D5"}, 1: {"D1", "D2", "D5"}, 2: {"D3", "D5"}, 3: {"D4", "D5"}}
QUOTA = {"D1": 16, "D2": 11, "D3": 12, "D4": 12, "D5": 9}
PLAN = {0: "CADBACBDABCABCD", 1: "BDACDABCADBACBD", 2: "DACBADCABDCBACD", 3: "CBDACDBCADBCDAB"}
ok = True
def check(name, cond, detail=""):
    global ok
    print(("  PASS  " if cond else "  FAIL  ") + name + ((" -- " + detail) if detail else ""))
    if not cond: ok = False

print("\n=== STRUCTURE ===")
check("60 questions", len(QS) == 60, "got %d" % len(QS))
check("g numbering 1..60 contiguous", [q["g"] for q in QS] == list(range(1, 61)))
check("4 options everywhere", all(len(q["options"]) == 4 for q in QS))
check("3 whyWrong everywhere", all(len(q["whyWrong"]) == 3 for q in QS))
bad = [q["g"] for q in QS if sorted([w["option"] for w in q["whyWrong"]] + [q["correct"]]) != [0, 1, 2, 3]]
check("whyWrong covers exactly the 3 non-correct options", not bad, str(bad))
check("every rationale carries a citation",
      all(q["whyRight"]["cite"] and all(w["cite"] for w in q["whyWrong"]) for q in QS))
check("15 questions per block", all(sum(1 for q in QS if q["block"] == b) == 15 for b in range(4)))

print("\n=== DOMAIN QUOTA (exam-wide) ===")
dom = collections.Counter(q["domain"] for q in QS)
for d in ["D1", "D2", "D3", "D4", "D5"]:
    check("%s = %d" % (d, QUOTA[d]), dom[d] == QUOTA[d], "got %d" % dom[d])

print("\n=== BLOCK DOMAIN PRIMACY (no non-primary may outnumber a primary) ===")
for b in range(4):
    c = collections.Counter(q["domain"] for q in QS if q["block"] == b)
    prim = [c[d] for d in PRIMARY[b] if c[d]]
    nonp = {d: n for d, n in c.items() if d not in PRIMARY[b]}
    worst = max(nonp.values()) if nonp else 0
    check("block %d (%s): %s" % (b + 1, BLOCKS[b]["label"][:28], dict(c)),
          (not nonp) or (worst < min(prim)), "non-primary %s vs primary min %s" % (nonp, min(prim) if prim else "-"))

print("\n=== CORRECT-ANSWER LETTER PLAN ===")
letters = "ABCD"
for b in range(4):
    seq = "".join(letters[q["correct"]] for q in QS if q["block"] == b)
    c = collections.Counter(seq)
    check("block %d follows its pre-plan" % (b + 1), seq == PLAN[b], "%s vs plan %s" % (seq, PLAN[b]))
    check("block %d spread %s" % (b + 1, dict(c)), max(c.values()) - min(c.values()) <= 1, str(dict(c)))
whole = collections.Counter(letters[q["correct"]] for q in QS)
check("exam-wide 15/15/15/15", all(whole[x] == 15 for x in letters), str(dict(whole)))
runs = max(len(m.group(0)) for m in re.finditer(r"(.)\1*", "".join(letters[q["correct"]] for q in QS)))
check("no run of identical letters > 3", runs <= 3, "longest run %d" % runs)

print("\n=== INLINE CODE TOKEN RATE (target 20-25% of options) ===")
opts = [o for q in QS for o in q["options"]]
withcode = sum(1 for o in opts if "`" in o)
rate = 100.0 * withcode / len(opts)
check("rate %.1f%% within 20-25%%" % rate, 20.0 <= rate <= 25.0, "%d of %d options" % (withcode, len(opts)))

print("\n=== NO INVENTED COMPANY / PRODUCT / PERSONA NAMES ===")
# Only mid-sentence capitalised words can be proper nouns; sentence-initial words prove nothing.
TECH = set("""Claude Code Task Read Write Edit Bash Grep Glob WebSearch API MCP JSON YAML PDF HTML
VAT ISO Python TypeScript Go Finance QA Agent SDK Batches Message Exam Block Domain Schema""".split())
suspects = collections.Counter()
for q in QS:
    for sent in re.split(r"(?<=[.!?][\"'”’])\s+|(?<=[.!?])\s+", q["stem"]):
        body = re.sub(r"`[^`]*`", " ", sent)
        body = " ".join(body.split()[1:])
        for w in re.findall(r"(?<![\w`'])[A-Z][a-z]{2,}(?![\w`])", body):
            if w not in TECH:
                suspects[w] += 1
check("no fictional entity names mid-sentence", not suspects, str(dict(suspects)))

print("\n=== DEDUPLICATION vs 720 prior mock stems + practice-test ledger ===")
prior = []
bank = json.load(io.open(os.path.join(BUILD, "bank.json"), encoding="utf-8"))
prior += [(("Exam " + q["exam"] + " Q" + str(q["g"])), q["stem"]) for q in bank["questions"]]
led = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                   "prep with quiz", "PRACTICE-TEST-STEMS_v1.md")
if os.path.exists(led):
    txt = io.open(led, encoding="utf-8").read()
    for m in re.finditer(r"^\s*\d+\.\s+(?:\[[^\]]*\]\s*)?(.{60,})$", txt, re.M):
        prior.append(("practice-ledger", m.group(1).strip()))
print("  comparing against %d prior stems" % len(prior))

def norm(t):
    t = re.sub(r"`[^`]*`", " ", t.lower())
    return re.sub(r"[^a-z0-9 ]", " ", t)

worst = []
for q in QS:
    a = norm(q["stem"])
    best, who = 0.0, ""
    for src, p in prior:
        r = difflib.SequenceMatcher(None, a, norm(p)).quick_ratio()
        if r < 0.55: continue
        r = difflib.SequenceMatcher(None, a, norm(p)).ratio()
        if r > best: best, who = r, src
    worst.append((best, q["g"], who))
worst.sort(reverse=True)
top = worst[0]
check("no stem >= 0.70 similarity to any prior stem", top[0] < 0.70,
      "highest = Q%d at %.3f vs %s" % (top[1], top[0], top[2]))
print("  five closest:", ", ".join("Q%d %.2f (%s)" % (g, s, w) for s, g, w in worst[:5]))

print("\n=== TARGETED SECTIONS (from the miss record) ===")
cites = collections.Counter()
for q in QS:
    for c in [q["whyRight"]["cite"]] + [w["cite"] for w in q["whyWrong"]]:
        for s in re.findall(r"D\d\s*§\s*\d+\.\d+", c): cites[s.replace(" ", "")] += 1
want = {"D2§2.8": "5 straight misses", "D2§2.4": "3 misses", "D2§2.1": "3 misses",
        "D3§3.1": "3 misses", "D2§2.2": "2 misses", "D2§2.9": "2 misses", "D1§1.6": "2 misses",
        "D1§1.3": "2 misses", "D3§3.3": "2 misses", "D4§4.2": "2 misses", "D5§5.8": "over-escalation",
        "D1§1.18": "pattern confusion", "D5§5.1": "stateless", "D4§4.17": "trust urgency",
        "D4§4.14": "prompt chaining", "D5§5.13": "hybrid window", "D3§3.4": "fabricated obsolescence"}
missing = [k for k in want if cites.get(k, 0) == 0]
check("every targeted section appears", not missing, str(missing))
for k in sorted(want): print("   %-9s %-22s cited %dx" % (k, want[k], cites.get(k, 0)))

print("\n" + ("ALL GATES PASSED" if ok else "GATES FAILED"))
if ok:
    io.open(os.path.join(BUILD, "exam13.json"), "w", encoding="utf-8").write(json.dumps(
        {"exam_n": 13, "format": "FULL60", "generated": "2026-08-11", "quota": QUOTA,
         "domainNames": {"D1": "Agentic Architecture & Orchestration",
                         "D2": "Tool Design & MCP Integration",
                         "D3": "Claude Code Configuration & Workflows",
                         "D4": "Prompt Engineering & Structured Output",
                         "D5": "Context Management & Reliability"},
         "blocks": BLOCKS, "questions": QS}, ensure_ascii=False))
    print("wrote exam13.json")
sys.exit(0 if ok else 1)
