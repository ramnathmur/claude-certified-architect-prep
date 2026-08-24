import json, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))

blocks, questions = [], []
for i in range(1, 5):
    b = json.load(open(os.path.join(HERE, f"block{i}.json"), encoding="utf-8"))
    blocks.append({"label": b["label"], "narrative": b["narrative"]})
    for q in b["questions"]:
        q["blockLabel"] = b["label"]
        questions.append(q)

questions.sort(key=lambda q: q["g"])

DATA = {
    "exam_n": 15,
    "format": "FULL60",
    "generated": "2026-08-11",
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

# ---- structural sanity before anything else ----
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

mr = [q for q in questions if q.get("selectN")]
print(f"questions: {len(questions)}  MR: {len(mr)}  SA: {len(questions)-len(mr)}")
print(f"MR select-2: {sum(1 for q in mr if q['selectN']==2)}  select-3: {sum(1 for q in mr if q['selectN']==3)}")
print(f"domain tally: {dict(sorted(dom.items()))}")

sa_letters = collections.Counter(chr(65+q["correct"]) for q in questions if not q.get("selectN"))
print(f"SA letter tally: {dict(sorted(sa_letters.items()))}")
per_block = collections.defaultdict(collections.Counter)
for q in questions:
    if not q.get("selectN"):
        per_block[q["block"]][chr(65+q["correct"])] += 1
for b in range(4):
    print(f"  block {b+1}: {dict(sorted(per_block[b].items()))}")

if errs:
    print("\nSTRUCTURAL ERRORS:")
    for e in errs:
        print("  -", e)
    raise SystemExit(1)

out = os.path.join(HERE, "exam15-data.json")
json.dump(DATA, open(out, "w", encoding="utf-8"), ensure_ascii=False)
print(f"\nOK -> {out}")
