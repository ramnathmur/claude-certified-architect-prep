# -*- coding: utf-8 -*-
import json, re, itertools

BLOCKS = ["block-1.json", "block-2.json", "block-3.json", "block-4.json"]
DOMAIN_QUOTA = {"D1": 16, "D2": 11, "D3": 12, "D4": 12, "D5": 9}
PRIMARY = {
    0: {"D1", "D2", "D5"},   # Customer Support Resolution Agent
    1: {"D1", "D2", "D3"},   # Developer Productivity with Claude
    2: {"D3", "D4"},         # Claude Code for Continuous Integration
    3: {"D4", "D5"},         # Structured Data Extraction
}

blocks = []
for f in BLOCKS:
    blocks.append(json.load(open(f"WIP-EXAM11/{f}", encoding="utf-8")))

all_q = []
for b in blocks:
    all_q.extend(b["questions"])
all_q.sort(key=lambda q: q["g"])

print(f"Total questions: {len(all_q)}")
assert [q["g"] for q in all_q] == list(range(1, 61)), "g numbering gap/dup!"

# ---------- Check 1: No invented names ----------
NAME_PATTERN = re.compile(
    r"\b(Acme|TechCorp|GlobalTech|InnovateCo|Contoso|Fabrikam|"
    r"[A-Z][a-z]+(?:Corp|Inc|LLC|Systems|Solutions|Technologies)\b|"
    r"\b(?:Sarah|John|Mike|Emily|David|Jane|Bob|Alice|Priya|Raj)\b)"
)
name_hits = []
for q in all_q:
    text = q["stem"] + " " + " ".join(q["options"]) + " " + q["whyRight"]["text"] + " " + " ".join(w["text"] for w in q["whyWrong"])
    for m in NAME_PATTERN.finditer(text):
        name_hits.append((q["g"], m.group(0)))
print(f"\nCHECK 1 - Invented names: {len(name_hits)} hits -> {name_hits[:10]}")

# ---------- Check 2: Correct-answer letter tally ----------
print("\nCHECK 2 - Letter tally:")
overall_tally = {"A": 0, "B": 0, "C": 0, "D": 0}
for bi, b in enumerate(blocks):
    tally = {"A": 0, "B": 0, "C": 0, "D": 0}
    for q in b["questions"]:
        letter = "ABCD"[q["correct"]]
        tally[letter] += 1
        overall_tally[letter] += 1
    vals = list(tally.values())
    ok = all(3 <= v <= 5 for v in vals)
    print(f"  Block {bi} ({b['label']}): {tally}  {'PASS' if ok else 'FAIL'}")
overall_ok = all(14 <= v <= 16 for v in overall_tally.values())
print(f"  EXAM-WIDE: {overall_tally}  {'PASS' if overall_ok else 'FAIL'}")

# ---------- Check 3: Word counts ----------
def wc(s):
    return len(s.split())

stem_wcs = [wc(q["stem"]) for q in all_q]
opt_wcs = [wc(o) for q in all_q for o in q["options"]]
stem_median = sorted(stem_wcs)[len(stem_wcs)//2]
print(f"\nCHECK 3 - Word counts:")
print(f"  Stems: min={min(stem_wcs)} median={stem_median} max={max(stem_wcs)}  (target median 50-55, cap 95)")
print(f"  Options: min={min(opt_wcs)} max={max(opt_wcs)}  (cap 35)")
stem_cap_viol = [(q["g"], wc(q["stem"])) for q in all_q if wc(q["stem"]) > 95]
opt_cap_viol = [(q["g"], i, wc(o)) for q in all_q for i, o in enumerate(q["options"]) if wc(o) > 35]
print(f"  Stem cap violations: {stem_cap_viol}")
print(f"  Option cap violations: {opt_cap_viol}")

# ---------- Check 4: Block domain tally vs primary domains ----------
print("\nCHECK 4 - Block domain tally vs primary:")
for bi, b in enumerate(blocks):
    dom_tally = {}
    for q in b["questions"]:
        dom_tally[q["domain"]] = dom_tally.get(q["domain"], 0) + 1
    primary = PRIMARY[bi]
    primary_min = min((dom_tally.get(d, 0) for d in primary), default=0)
    nonprimary_max = max((v for d, v in dom_tally.items() if d not in primary), default=0)
    ok = primary_min > nonprimary_max
    print(f"  Block {bi}: {dom_tally}  primary_min={primary_min} nonprimary_max={nonprimary_max}  {'PASS' if ok else 'FAIL'}")

exam_dom_tally = {}
for q in all_q:
    exam_dom_tally[q["domain"]] = exam_dom_tally.get(q["domain"], 0) + 1
print(f"  EXAM-WIDE domain tally: {exam_dom_tally}  target: {DOMAIN_QUOTA}  {'PASS' if exam_dom_tally == DOMAIN_QUOTA else 'FAIL'}")

# ---------- Check 5: Inline code/config token rate ----------
CODE_PATTERN = re.compile(r"`[^`]+`")
opts_with_code = sum(1 for q in all_q for o in q["options"] if CODE_PATTERN.search(o))
total_opts = len(opt_wcs)
rate = opts_with_code / total_opts * 100
print(f"\nCHECK 5 - Code/config token rate: {opts_with_code}/{total_opts} options = {rate:.1f}%  (target 20-25%, acceptable 15-30%)")

# ---------- Check 6: manual (landing card disclosure line) - flagged for HTML build step ----------
print("\nCHECK 6 - Scenario-rotation disclosure line: MUST be added verbatim during HTML build (Slice G).")

# ---------- KD budget check ----------
kd_count = sum(1 for q in all_q if q.get("kd"))
kd_list = [q["kd"] for q in all_q if q.get("kd")]
print(f"\n--- KD budget check (Session 13 tightened target: 4-6) ---")
print(f"KD count: {kd_count}  KDs: {sorted(kd_list)}  {'PASS (within 4-6 target)' if 4 <= kd_count <= 6 else 'NOTE: outside 4-6 target'}")

# ---------- Citation-collision tally (PB-19) ----------
print("\n--- Citation-collision tally (PB-19) ---")
primary_cite_map = {}
for q in all_q:
    m = re.search(r"D\d\s*\xa7\d+\.\d+", q["whyRight"]["cite"]) or re.search(r"D\d\s*§\d+\.\d+", q["whyRight"]["cite"])
    key = m.group(0) if m else q["whyRight"]["cite"]
    primary_cite_map.setdefault(key, []).append(q["g"])

collisions = {k: v for k, v in primary_cite_map.items() if len(v) > 1}
print(f"Sections tested as PRIMARY (whyRight) more than once: {len(collisions)}")
for k, v in sorted(collisions.items()):
    print(f"  {k}: questions {v}")

# ---------- Structural section-repeat check ----------
print("\n--- Section-repeat structural check ---")
from collections import defaultdict
by_domain_section = defaultdict(list)
for q in all_q:
    by_domain_section[(q['domain'], q.get('section'))].append(q['g'])
dupes = {k:v for k,v in by_domain_section.items() if len(v) > 1}
print("Sections used more than once (should be ONLY the pre-declared D2 §2.3/§2.8 repeats):")
for k,v in sorted(dupes.items(), key=lambda x: str(x[0])):
    print(f"  {k}: {v}")

# ---------- Internal Jaccard near-duplicate scan ----------
print("\n--- Internal Jaccard near-duplicate scan (threshold 0.30) ---")
def tokens(s):
    return set(re.findall(r"[a-z]{3,}", s.lower()))

stem_tokens = {q["g"]: tokens(q["stem"]) for q in all_q}
near_dups = []
for g1, g2 in itertools.combinations(sorted(stem_tokens), 2):
    t1, t2 = stem_tokens[g1], stem_tokens[g2]
    if not t1 or not t2:
        continue
    j = len(t1 & t2) / len(t1 | t2)
    if j >= 0.30:
        near_dups.append((g1, g2, round(j, 3)))
print(f"Near-duplicate pairs (internal, this exam only): {near_dups}")

print("\n=== GATE SCRIPT COMPLETE ===")
