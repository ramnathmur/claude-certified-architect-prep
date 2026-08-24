#!/usr/bin/env python3
"""Independent verification of the built pack. Deliberately does not import build_pack --
it re-reads the shipped files and checks them from scratch, so a bug in the builder's own
assertions cannot hide a defect."""
import os, re, sys, glob, json

PACK = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\Outputs\CCA-F-Prep-Pack_v1"
papers = sorted(glob.glob(os.path.join(PACK, "01-mock-exams", "Paper-*.html")))
fail = []

print(f"papers found: {len(papers)}\n")
print(f"{'file':<16} {'title':>6} {'hero':>6} {'KEY':>6} {'exam_n':>7}  personal  panels  stray")
print("-" * 78)

for p in papers:
    name = os.path.basename(p)
    n = int(re.search(r"Paper-(\d+)", name).group(1))
    s = open(p, encoding="utf-8").read()

    title = re.search(r"<title>CCA-F Practice Paper (\d+)", s)
    hero = re.search(r"<h1>Practice Paper <em>(\d+)</em></h1>", s)
    key = re.search(r'const KEY\s*=\s*"ccaf-paper-(\d+)"', s)
    exam = re.search(r'"exam_n"\s*:\s*(\d+)', s)
    nums = [title and int(title.group(1)), hero and int(hero.group(1)),
            key and int(key.group(1)), exam and int(exam.group(1))]
    consistent = all(x == n for x in nums)
    if not consistent:
        fail.append(f"{name}: identity mismatch {nums} vs expected {n}")

    # personal-data sweep, with JS template expressions stripped so arithmetic is not a hit
    scan = re.sub(r"\$\{[^{}]*\}", " ", s)
    # "0 / 60 answered" is the progress meter's initial state, not a score.
    scan = scan.replace("0 / 60 answered", "progress-meter")
    personal = []
    for pat, label in [(r"\b\d{1,2}\s*/\s*60\b", "NN/60"),
                       (r"\b(?!720\b)\d{3}\s*/\s*1000\b", "NNN/1000"),
                       (r"\byour (?:joint best|last paper|weak|exams)", "personal phrasing"),
                       (r"18 August", "exam date"), (r"\bRam\b", "name"),
                       (r"attempted 2026", "attempt date"),
                       (r"Last scored exam", "scored-exam panel"),
                       (r"Targeting this paper", "targeting panel"),
                       (r"Prior score", "prior-score panel")]:
        for h in re.finditer(pat, scan):
            ctx = re.sub(r"\s+", " ", scan[max(0, h.start()-70):h.end()+70])
            personal.append(f"{label}: ...{ctx.strip()[:120]}...")

    # landing-card panels that should remain
    kept = re.findall(r'<div class="k">([^<]+)</div>', s)
    has_weighting = any("How this paper is weighted" in k for k in kept)
    has_scenarios = any("Scenarios drawn" in k for k in kept)
    has_passline = any("Pass line" in k for k in kept)
    panels_ok = has_weighting and has_scenarios and has_passline
    if not panels_ok:
        fail.append(f"{name}: expected panels missing (weighting={has_weighting} scenarios={has_scenarios} pass={has_passline})")

    stray = "tSec/60/60" in s
    if stray:
        fail.append(f"{name}: stray total-time artifact still present")

    # PB-20 guard: any bare numeric exam_n literal outside the DATA payload means the
    # exported JSON would disagree with the paper's own identity. Must be dynamic.
    for lit in re.findall(r"\bexam_n\s*:\s*(\d+)", s):
        fail.append(f"{name}: hardcoded exam_n:{lit} literal in the export payload (PB-20)")
    if personal:
        fail.extend(f"{name}: {x}" for x in personal)

    # old identity must be entirely gone
    if re.search(r"cca-mock-\d+", s):
        fail.append(f"{name}: an old cca-mock-N key survived")
    if re.search(r"Mock Test", s):
        fail.append(f"{name}: the phrase 'Mock Test' survived")

    print(f"{name:<16} {str(nums[0]):>6} {str(nums[1]):>6} {str(nums[2]):>6} {str(nums[3]):>7}"
          f"  {len(personal):>8}  {'ok' if panels_ok else 'MISS':>6}  {'YES' if stray else 'no':>5}")

# rotation-disclosure line must survive (it is honest framing colleagues need)
missing_disc = [os.path.basename(p) for p in papers
                if "real exam draws 4 of 6 at random" not in open(p, encoding="utf-8").read().lower()
                .replace("the real exam draws 4 of 6 at random", "real exam draws 4 of 6 at random")]
print(f"\nrotation-disclosure line present: {len(papers)-len(missing_disc)}/{len(papers)}")
if missing_disc:
    print("  missing in:", ", ".join(missing_disc))
    fail.extend(f"{m}: rotation-disclosure line absent" for m in missing_disc)

# question integrity: every paper still has 60 questions and a valid DATA payload
print("\nquestion payloads:")
for p in papers:
    s = open(p, encoding="utf-8").read()
    m = re.search(r"const DATA = (\{)", s)
    depth, instr, esc, end = 0, False, False, None
    for i in range(m.start(1), len(s)):
        c = s[i]
        if instr:
            if esc: esc = False
            elif c == "\\": esc = True
            elif c == '"': instr = False
            continue
        if c == '"': instr = True
        elif c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0: end = i+1; break
    try:
        d = json.loads(s[m.start(1):end])
        mr = sum(1 for q in d["questions"] if q.get("selectN"))
        ok = len(d["questions"]) == 60
        if not ok: fail.append(f"{os.path.basename(p)}: {len(d['questions'])} questions, expected 60")
        print(f"  {os.path.basename(p):<16} exam_n={d['exam_n']:<3} questions={len(d['questions'])}  MR={mr}")
    except Exception as e:
        fail.append(f"{os.path.basename(p)}: DATA payload unparseable ({e})")

print("\n" + "=" * 78)
if fail:
    print(f"{len(fail)} FAILURE(S):")
    for f in fail[:25]:
        print("  -", f)
    sys.exit(1)
print("ALL CHECKS PASS")
