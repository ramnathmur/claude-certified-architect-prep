"""Check new stems against every prior stem (EXAM-LOG Exams 2-16 + the 76 community stems).

Jaccard over content words, reported against the project's 0.40 reskin threshold.
Usage: python dedup_check.py <exam-data.json> <stem_ledger.json>
"""
import json, re, sys, collections

STOP = set("""a an the and or but if then than that this these those of in on at to for with from by
as is are was were be been being it its it's do does did not no nor so such very can could should would
will shall may might must have has had you your yours we our they their there here what which who whom
when where why how all any both each few more most other some only own same too s t just now over under
again further once about into during before after above below up down out off between against""".split())


def toks(s):
    s = re.sub(r"`[^`]*`", " ", s)
    return {w for w in re.findall(r"[a-z][a-z0-9_]{2,}", s.lower()) if w not in STOP}


def jac(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


data = json.load(open(sys.argv[1], encoding="utf-8"))
ledger = json.load(open(sys.argv[2], encoding="utf-8"))
prior = [(r["src"], r["text"], toks(r["text"])) for r in ledger]

print(f"new stems: {len(data['questions'])}   prior stems: {len(prior)}")
worst, flagged = [], []
for q in data["questions"]:
    nt = toks(q["stem"])
    best = max(((jac(nt, pt), src, txt) for src, txt, pt in prior), default=(0, "", ""))
    worst.append((best[0], q["g"], best[1], best[2]))
    if best[0] >= 0.40:
        flagged.append((best[0], q["g"], best[1], best[2], q["stem"]))

worst.sort(reverse=True)
print("\nhighest similarity per new stem (top 12):")
for score, g, src, txt in worst[:12]:
    print(f"  Q{g:<3d} {score:.3f}  [{src}] {txt[:88]}")

print(f"\nmean max-similarity: {sum(w[0] for w in worst)/len(worst):.3f}")
print(f"stems at or above the 0.40 reskin threshold: {len(flagged)}")
if flagged:
    print("\nCOLLISIONS TO REWRITE:")
    for score, g, src, txt, stem in flagged:
        print(f"\n  Q{g} ({score:.3f}) vs [{src}]")
        print(f"    prior: {txt[:200]}")
        print(f"    new:   {stem[:200]}")
    raise SystemExit(1)
print("\nOK - no stem reaches the reskin threshold against any prior stem.")
