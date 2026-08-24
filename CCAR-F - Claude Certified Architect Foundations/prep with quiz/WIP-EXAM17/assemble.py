import json, os, collections, re

HERE = os.path.dirname(os.path.abspath(__file__))
EXAM_N = 17

blocks, questions = [], []
for i in range(1, 5):
    b = json.load(open(os.path.join(HERE, f"block{i}.json"), encoding="utf-8"))
    blocks.append({"label": b["label"], "narrative": b["narrative"]})
    for q in b["questions"]:
        q["blockLabel"] = b["label"]
        questions.append(q)

questions.sort(key=lambda q: q["g"])

DATA = {
    "exam_n": EXAM_N,
    "format": "FULL60",
    "generated": "2026-08-14",
    "quota": {"D1": 16, "D2": 11, "D3": 12, "D4": 12, "D5": 9},
    "domainNames": {
        "D1": "Agentic Architecture & Orchestration",
        "D2": "Tool Design & MCP Integration",
        "D3": "Claude Code Configuration & Workflows",
        "D4": "Prompt Engineering & Structured Output",
        "D5": "Context Management & Reliability",
    },
    "blocks": blocks,
    "questions": questions,
}

errs = []
if len(questions) != 60:
    errs.append(f"expected 60 questions, got {len(questions)}")
if [q["g"] for q in questions] != list(range(1, 61)):
    errs.append("question numbers are not 1..60 contiguous")

dom = collections.Counter(q["domain"] for q in questions)
if dict(dom) != DATA["quota"]:
    errs.append(f"domain tally {dict(dom)} != quota {DATA['quota']}")

blk = collections.Counter(q["block"] for q in questions)
for b in range(4):
    if blk[b] != 15:
        errs.append(f"block {b} has {blk[b]} questions, expected 15")

for q in questions:
    if q["blockLabel"] != blocks[q["block"]]["label"]:
        errs.append(f"Q{q['g']}: blockLabel/block mismatch")
    n_opts = len(q["options"])
    if q.get("selectN"):
        if not isinstance(q["correct"], list):
            errs.append(f"Q{q['g']}: MR item without list correct")
        elif len(q["correct"]) != q["selectN"]:
            errs.append(f"Q{q['g']}: selectN={q['selectN']} vs {len(q['correct'])} correct")
        expected_wrong = set(range(n_opts)) - set(q["correct"])
    else:
        if not isinstance(q["correct"], int):
            errs.append(f"Q{q['g']}: SA item with non-int correct")
        if n_opts != 4:
            errs.append(f"Q{q['g']}: SA item has {n_opts} options")
        expected_wrong = set(range(n_opts)) - {q["correct"]}
    got_wrong = {w["option"] for w in q["whyWrong"]}
    if got_wrong != expected_wrong:
        errs.append(f"Q{q['g']}: whyWrong {sorted(got_wrong)} != expected {sorted(expected_wrong)}")
    if not q["whyRight"].get("cite"):
        errs.append(f"Q{q['g']}: whyRight missing citation")
    for w in q["whyWrong"]:
        if not w.get("cite"):
            errs.append(f"Q{q['g']}: whyWrong option {w['option']} missing citation")

# ---- block x domain allocation vs the solved plan ----
PLAN = {
    0: {"D1": 4, "D2": 4, "D3": 2, "D4": 2, "D5": 3},
    1: {"D1": 5, "D2": 6, "D3": 1, "D4": 1, "D5": 2},
    2: {"D1": 4, "D2": 0, "D3": 6, "D4": 5, "D5": 0},
    3: {"D1": 3, "D2": 1, "D3": 3, "D4": 4, "D5": 4},
}
for b in range(4):
    got = collections.Counter(q["domain"] for q in questions if q["block"] == b)
    want = {k: v for k, v in PLAN[b].items() if v}
    if dict(sorted(got.items())) != dict(sorted(want.items())):
        errs.append(f"block {b+1} domain split {dict(got)} != plan {want}")

# ---- non-primary must never outnumber a primary, within each block ----
PRIM = {
    "Customer Support Resolution Agent": {"D1", "D2", "D5"},
    "Multi-Agent Research System": {"D1", "D2", "D5"},
    "Claude Code for Continuous Integration": {"D3", "D4"},
    "Structured Data Extraction": {"D4", "D5"},
}
for b in range(4):
    lab = blocks[b]["label"]
    got = collections.Counter(q["domain"] for q in questions if q["block"] == b)
    pv = [got[d] for d in PLAN[b] if d in PRIM[lab]]
    nv = [got[d] for d in PLAN[b] if d not in PRIM[lab]]
    if min(pv) <= max(nv):
        errs.append(f"block {b+1} ({lab}): non-primary {max(nv)} outnumbers primary {min(pv)}")

# ---- correct-answer letter pre-plan (single-answer items only) ----
PREPLAN = json.load(open(os.path.join(HERE, "preplan.json"), encoding="utf-8"))
for b in range(4):
    got = "".join(chr(65 + q["correct"]) for q in questions
                  if q["block"] == b and not q.get("selectN"))
    if got != PREPLAN[str(b + 1)]:
        errs.append(f"block {b+1} letter sequence {got} != pre-plan {PREPLAN[str(b+1)]}")

mr = [q for q in questions if q.get("selectN")]
print(f"questions: {len(questions)}  MR: {len(mr)}  SA: {len(questions)-len(mr)}")
print(f"domain tally: {dict(sorted(dom.items()))}")

sa_letters = collections.Counter(chr(65 + q["correct"]) for q in questions if not q.get("selectN"))
print(f"SA letter tally: {dict(sorted(sa_letters.items()))}")
for b in range(4):
    seq = "".join(chr(65 + q["correct"]) for q in questions
                  if q["block"] == b and not q.get("selectN"))
    print(f"  block {b+1}: {seq}  {dict(sorted(collections.Counter(seq).items()))}")

for b in range(4):
    got = collections.Counter(q["domain"] for q in questions if q["block"] == b)
    print(f"  block {b+1} domains: {dict(sorted(got.items()))}   [{blocks[b]['label']}]")

# ---- inline code/config token rate across options (target band 20-25%) ----
code_opts = sum(1 for q in questions for o in q["options"] if "`" in o)
tot_opts = sum(len(q["options"]) for q in questions)
print(f"\ninline code/config token rate: {code_opts}/{tot_opts} = {100*code_opts/tot_opts:.1f}% (target 20-25%)")

secs = collections.Counter()
for q in questions:
    m = re.search(r"§([\d.]+)", q["whyRight"]["cite"])
    d = re.search(r"Domain-(\d)", q["whyRight"]["cite"])
    if m and d:
        secs[f"D{d.group(1)} §{m.group(1)}"] += 1
print(f"distinct corpus sections cited as whyRight: {len(secs)}")
dupes = {k: v for k, v in sorted(secs.items()) if v > 1}
print(f"sections cited more than once: {dupes or 'none'}")

if errs:
    print("\nSTRUCTURAL ERRORS:")
    for e in errs:
        print("  -", e)
    raise SystemExit(1)

out = os.path.join(HERE, f"exam{EXAM_N}-data.json")
json.dump(DATA, open(out, "w", encoding="utf-8"), ensure_ascii=False)
print(f"\nOK -> {out}")
