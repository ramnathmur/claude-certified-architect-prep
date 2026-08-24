"""Coverage gate: every official-guide bullet ID must map to at least one card; every referenced ID must exist;
every Key Distinction 1-29 must be woven into at least one card. Exit code 1 on any failure.
Run: python check_coverage.py
"""
import importlib.util
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("inventory", os.path.join(HERE, "inventory.py"))
inv = importlib.util.module_from_spec(spec); spec.loader.exec_module(inv)
data = json.load(open(os.path.join(HERE, "bullets.json"), encoding="utf-8"))

ids = {b["id"] for b in data["bullets"]}
mapped = defaultdict(list)
unknown = []
for c in inv.CARDS:
    for b in c["bul"]:
        if b not in ids:
            unknown.append((c["id"], b))
        mapped[b].append(c["id"])

unmapped = sorted(i for i in ids if i not in mapped)
kd_seen = Counter(k for c in inv.CARDS for k in c["kd"])
kd_missing = [k for k in range(1, 30) if k not in kd_seen]
dup_ids = [k for k, v in Counter(c["id"] for c in inv.CARDS).items() if v > 1]

per_dom = Counter(c["id"].split("-")[0] for c in inv.CARDS)
ts_bul = [b for b in data["bullets"] if b["ts"] != "APP"]
print(f"cards: {len(inv.CARDS)}  by domain: {dict(per_dom)}")
print(f"bullet ids: {len(ids)}  (task-statement {len(ts_bul)}, appendix {len(ids)-len(ts_bul)})")
print(f"mapped: {len(mapped)}  unmapped: {len(unmapped)}  unknown refs: {len(unknown)}")
print(f"KD covered: {len(kd_seen)}/29  missing: {kd_missing}")
multi = {b: cs for b, cs in mapped.items() if len(cs) > 1 and not b.startswith('APP')}
print(f"task-statement bullets served by >1 card: {len(multi)}")
if unmapped:
    print("\nUNMAPPED:")
    for u in unmapped:
        t = next(b["text"] for b in data["bullets"] if b["id"] == u)
        print(f"  {u}: {t[:120]}")
if unknown:
    print("\nUNKNOWN REFS:", unknown)
if dup_ids:
    print("\nDUPLICATE CARD IDS:", dup_ids)
ok = not unmapped and not unknown and not kd_missing and not dup_ids
print("\nGATE:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
