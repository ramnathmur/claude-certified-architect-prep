"""Seat each single-answer question's correct option at its pre-planned letter.

The blueprint (CLAUDE.md Step 4) makes the per-block letter pre-plan the primary
balance mechanism and sanctions reshuffling an affected question's OPTIONS ONLY —
content and rationales unchanged — when a drafted question drifts from its assigned
letter. This performs exactly that repair: it swaps the correct option into its
planned position, leaves every option string byte-identical, and remaps the
whyWrong option indices so they still point at the same text.

Multiple-response items are skipped; they carry no letter assignment.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PREPLAN = json.load(open(os.path.join(HERE, "preplan.json"), encoding="utf-8"))

changed_total = 0
for n in range(1, 5):
    path = os.path.join(HERE, f"block{n}.json")
    if not os.path.exists(path):
        continue
    b = json.load(open(path, encoding="utf-8"))
    seq = PREPLAN[str(n)]
    si, changed = 0, []
    for q in b["questions"]:
        if q.get("selectN"):
            continue
        if si >= len(seq):
            sys.exit(f"block{n}: more single-answer items than pre-planned letters")
        want = ord(seq[si]) - 65
        si += 1
        have = q["correct"]
        if want == have:
            continue
        opts = q["options"]
        opts[want], opts[have] = opts[have], opts[want]
        swap = {have: want, want: have}
        for w in q["whyWrong"]:
            w["option"] = swap.get(w["option"], w["option"])
        q["correct"] = want
        q["whyWrong"].sort(key=lambda w: w["option"])
        changed.append(f"Q{q['g']} {chr(65+have)}->{chr(65+want)}")
    if si != len(seq):
        sys.exit(f"block{n}: {si} single-answer items but {len(seq)} pre-planned letters")

    # verify the repair
    got = "".join(chr(65 + q["correct"]) for q in b["questions"] if not q.get("selectN"))
    assert got == seq, f"block{n}: {got} != {seq}"
    for q in b["questions"]:
        n_opts = len(q["options"])
        correct = q["correct"] if isinstance(q["correct"], list) else [q["correct"]]
        assert {w["option"] for w in q["whyWrong"]} == set(range(n_opts)) - set(correct), \
            f"block{n} Q{q['g']}: whyWrong indices broken"

    json.dump(b, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    changed_total += len(changed)
    print(f"block{n}: {seq}  repositioned {len(changed)}"
          + (f"  [{', '.join(changed)}]" if changed else ""))

print(f"total repositioned: {changed_total}")
