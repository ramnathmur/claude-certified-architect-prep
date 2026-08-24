#!/usr/bin/env python3
"""Build the CCA-F Prep Pack: a distributable study package for colleagues.

Reads from the working project, writes only into Outputs/CCA-F-Prep-Pack_v1/.
No source file is modified.

Every substitution is anchored and asserted. The project's own ledger records PB-20, where a
template-substitution build missed an unanchored bare numeric literal and shipped a paper
exporting the wrong exam number; this script fails loudly rather than repeat that.
"""
import json, os, re, shutil, sys

ROOT = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep"
PREP = os.path.join(ROOT, "prep with quiz")
PACK = os.path.join(ROOT, "Outputs", "CCA-F-Prep-Pack_v1")

# Exam number -> paper number. Exams 2, 3 and the Retrofit are deliberately excluded:
# they pre-date the fidelity rules and use invented company names the current gate bans.
EXAM_TO_PAPER = {n: n - 3 for n in range(4, 16)}

FOLDERS = ["01-mock-exams", "02-drill-deck", "03-cheat-sheets", "04-reading"]

# Landing-card panels carrying Ram's personal performance data. Matched on the .k label.
PERSONAL_PANEL_RE = re.compile(
    r'<div class="sf"[^>]*>\s*<div class="k">\s*(?:'
    r'Prior score|Last scored exam|Targeting this paper[^<]*|How this paper was targeted|'
    r'A broad representative paper[^<]*|Targeting this paper[^<]*'
    r')\s*</div>.*?</div>\s*</div>',
    re.S | re.I,
)

# Replacement intro paragraphs for the two papers whose intro addresses Ram directly.
INTRO_OVERRIDES = {
    11: ("This paper is built under an anti-repetition rule. An audit of the earlier papers found the "
         "same teaching points returning in the same shapes with only the tool names changed, so nine "
         "recurring question shapes are banned here and their underlying points are tested from new "
         "angles instead. Nothing on this paper will feel familiar from the others."),
    12: ("This paper is the companion to Paper 11. Between them the two cover all six official exam "
         "scenarios, so if you sit both you have practised every context the real exam can draw. Same "
         "difficulty, same weighting, same anti-repetition rule."),
}

NEUTRAL_PANEL = ('<div class="sf" style="margin-top:12px;background:rgba(255,255,255,0.6)">'
                 '<div class="k">How this paper is weighted</div><div class="v" style="font-weight:400;'
                 'font-size:13px;line-height:1.6;">Questions are distributed across the five exam domains '
                 'in the official proportions, and the four scenario blocks below each carry roughly '
                 'fifteen questions skewed toward the domains that scenario is primarily about. Your '
                 'results screen breaks the score down both ways, by domain and by block, so you can see '
                 'where a weak score is actually coming from.</div></div>')


def read(p):
    with open(p, encoding="utf-8", errors="strict") as fh:
        return fh.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(s)


def assert_sub(before, after, label, expect_min=1):
    """Fail loudly if a substitution did not land."""
    if before == after:
        sys.exit(f"  ABORT: substitution '{label}' changed nothing")
    return after


def transform_paper(src, exam_n, paper_n):
    s = read(src)
    problems = []

    # --- 1. strip the internal generation header comment -------------------------------
    # It holds the dedup stem ledger and generation notes: useless to a reader, and the
    # place personal commentary hides.
    m = re.search(r"<!--\s*\n\s*CCA-Prep Mock Test.*?-->\s*\n", s, re.S)
    if m:
        s = s[:m.start()] + s[m.end():]
    else:
        problems.append("generation header comment not found (may already be absent)")

    # --- 1b. fix a real defect inherited from the older template -------------------------
    # Exams 4-13 render `Total time: 39:17 · 0` -- a stray hours figure from an unfinished
    # expression. Exams 14-15 already dropped it. Colleagues would see the artifact, so remove it.
    fixed = re.sub(r"(Total time: \$\{fmtTime\(tSec\)\})\s*·\s*\$\{\(tSec/60/60\)\.toFixed\(0\)\}",
                   r"\1", s)
    stray_fixed = fixed != s
    s = fixed

    # --- 2. identity renumbering (anchored) ---------------------------------------------
    s = assert_sub(s, re.sub(r"<title>CCA-F Mock Test \d+[^<]*</title>",
                             f"<title>CCA-F Practice Paper {paper_n} \u00b7 Foundations</title>", s),
                   "title")
    s = assert_sub(s, re.sub(r"<h1>Mock Test <em>\d+</em></h1>",
                             f"<h1>Practice Paper <em>{paper_n}</em></h1>", s), "hero")
    s = assert_sub(s, re.sub(r'const KEY\s*=\s*"cca-mock-\d+";',
                             f'const KEY = "ccaf-paper-{paper_n}";', s), "localStorage key")
    s = assert_sub(s, re.sub(r'"exam_n"\s*:\s*\d+', f'"exam_n": {paper_n}', s, count=1),
                   "DATA.exam_n")

    # PB-20: exams 4-9 carry a SECOND, bare exam_n literal inside the results-export payload
    # (`payload={exam_n:9, format:"FULL60", ...}`) that no quoted-key regex touches. Exams 10+
    # already use a dynamic reference because the project fixed this once before. Apply the
    # same fix here so the bug is structurally impossible rather than merely corrected.
    s = re.sub(r"\bexam_n\s*:\s*\d+", "exam_n:DATA.exam_n", s)
    s = re.sub(r'\bformat\s*:\s*"FULL60"', "format:DATA.format", s)

    # any surviving literal "Mock Test N" plus the dynamic "Mock Test ${...}" contexts
    s = re.sub(r"Mock Test \d+", f"Practice Paper {paper_n}", s)
    s = s.replace("Mock Test", "Practice Paper")

    # --- 3. landing card: heading -------------------------------------------------------
    s = assert_sub(s, re.sub(r"<h3>Exam \d+[^<]*</h3>",
                             f"<h3>Practice Paper {paper_n} \u00b7 60 questions across 4 scenario blocks</h3>",
                             s), "landing h3")

    # --- 4. landing card: remove personal panels ---------------------------------------
    removed = len(PERSONAL_PANEL_RE.findall(s))
    s = PERSONAL_PANEL_RE.sub("", s)
    if removed == 0:
        problems.append("no personal panel matched")

    # --- 5. landing card: intro paragraph ------------------------------------------------
    if paper_n in INTRO_OVERRIDES:
        s = assert_sub(s, re.sub(r"(<div class=\"kicker\">Before you begin</div>\s*<h3>.*?</h3>\s*)<p>.*?</p>",
                                 lambda m: m.group(1) + f"<p>{INTRO_OVERRIDES[paper_n]}</p>", s, count=1, flags=re.S),
                       "intro override")

    # --- 5b. rewrite the rotation-disclosure line for this audience ---------------------
    # The original reads "curated to guarantee coverage across your exams", which refers to
    # Ram's own 14-paper series and is meaningless to a colleague. The substance -- that the
    # draw is curated rather than random -- must survive.
    disc_old = re.compile(r"These 4 were curated to guarantee coverage across your exams[^<]*")
    disc_new = ("The real exam draws 4 of 6 at random each sitting. The four here were chosen "
                "deliberately rather than randomly, so that across the twelve papers in this pack "
                "you meet all six scenarios.")
    if disc_old.search(s):
        s = disc_old.sub(disc_new, s)
    else:
        problems.append("rotation-disclosure line not found")

    # --- 6. insert the neutral weighting panel before the scenarios panel ---------------
    anchor = '<div class="k">Scenarios drawn (4 of the official 6)</div>'
    i = s.find(anchor)
    if i == -1:
        problems.append("scenarios panel anchor not found; neutral panel not inserted")
    else:
        # step back to the opening <div class="sf" of that panel
        j = s.rfind('<div class="sf"', 0, i)
        s = s[:j] + NEUTRAL_PANEL + s[j:]

    # --- 7. assertions -------------------------------------------------------------------
    if re.search(rf"\bcca-mock-{exam_n}\b", s):
        problems.append(f"old localStorage key cca-mock-{exam_n} survived")
    if re.search(r'"exam_n"\s*:\s*(?!%d\b)\d+' % paper_n, s):
        problems.append("an exam_n other than the new paper number survived")
    # Strip JS template expressions before the personal-data scan: `${(tSec/60/60)...}` is
    # arithmetic, not a score, and would otherwise mask real hits behind noise.
    scan = re.sub(r"\$\{[^{}]*\}", " ", s)
    for pat, label in [(r"\d{1,2}/60\b", "score like NN/60"),
                       (r"\b\d{3}\s*/\s*1000\b", "scaled score like 925/1000"),
                       (r"\byour (?:joint best|last paper|weak)", "personal phrasing"),
                       (r"18 August", "Ram's exam date"),
                       (r"\bRam\b", "Ram by name"),
                       (r"attempted 2026", "attempt date")]:
        for hit in re.finditer(pat, s):
            ctx = s[max(0, hit.start()-60):hit.end()+60].replace("\n", " ")
            # 720/1000 is the legitimate published pass line
            if "720" in hit.group(0) or "720 / 1000" in ctx:
                continue
            problems.append(f"{label}: ...{ctx.strip()[:110]}...")

    if not stray_fixed and paper_n <= 10:
        problems.append("stray total-time artifact not found (template may differ)")
    return s, problems


def main():
    if os.path.exists(PACK):
        shutil.rmtree(PACK)
    for f in FOLDERS:
        os.makedirs(os.path.join(PACK, f), exist_ok=True)

    print("== papers ==")
    all_problems = {}
    for exam_n, paper_n in sorted(EXAM_TO_PAPER.items()):
        src = os.path.join(PREP, "mock-exams", f"CCA-Prep_MockTest-{exam_n}_v1.html")
        dst = os.path.join(PACK, "01-mock-exams", f"Paper-{paper_n:02d}.html")
        s, problems = transform_paper(src, exam_n, paper_n)
        write(dst, s)
        flag = "OK  " if not problems else "WARN"
        print(f"  [{flag}] Exam {exam_n:>2} -> Paper-{paper_n:02d}.html  ({len(s)/1024:.0f} KB)")
        for p in problems:
            print(f"          - {p}")
        if problems:
            all_problems[paper_n] = problems

    # --- straight copies -----------------------------------------------------------------
    ASSETS = os.path.join(ROOT, "Outputs", "_packbuild", "assets")
    COPIES = [
        (os.path.join(ASSETS, "progress-tracker.html"), "01-mock-exams/progress-tracker.html"),
        (os.path.join(ASSETS, "README.html"), "README.html"),
        (os.path.join(ASSETS, "START-HERE.txt"), "START-HERE.txt"),
        (os.path.join(ASSETS, "open-locally.bat"), "open-locally.bat"),
        (os.path.join(PREP, "drill", "CCA-Prep_Drill_v1.html"), "02-drill-deck/drill-deck.html"),
        (os.path.join(ROOT, "Outputs", "CCA-F_Professors-Cheat-Sheet_v2.html"), "03-cheat-sheets/the-cheat-sheet.html"),
        (os.path.join(ROOT, "EXAM-DIGEST.html"), "03-cheat-sheets/exam-cram-sheet.html"),
        (os.path.join(ROOT, "Outputs", "domain1_Reference_v1.html"), "03-cheat-sheets/domain-1-agentic-architecture.html"),
        (os.path.join(ROOT, "Outputs", "domain2_Reference_v1.html"), "03-cheat-sheets/domain-2-tool-design-mcp.html"),
        (os.path.join(ROOT, "Outputs", "domain3_Reference_v1.html"), "03-cheat-sheets/domain-3-claude-code-config.html"),
        (os.path.join(ROOT, "Outputs", "domain4_Reference_v1.html"), "03-cheat-sheets/domain-4-prompt-engineering.html"),
        (os.path.join(ROOT, "Outputs", "domain5_Reference_v1.html"), "03-cheat-sheets/domain-5-context-reliability.html"),
        (os.path.join(ROOT, "Outputs", "CCA-F_Refresher_v1.html"), "04-reading/refresher.html"),
        (os.path.join(ROOT, "Outputs", "CCA-F_Companion_v1.html"), "04-reading/companion.html"),
        (os.path.join(ROOT, "Outputs", "CCA-F_Masterclass_v1.html"), "04-reading/masterclass.html"),
        (os.path.join(ROOT, "CCA-Prep_Student-Briefing_v1.html"), "04-reading/student-briefing.html"),
        (os.path.join(PREP, "CCA-Prep_MCQ-Guide_v1.html"), "04-reading/how-the-mock-exam-works.html"),
    ]
    print("\n== straight copies ==")
    for src, rel in COPIES:
        if not os.path.exists(src):
            print(f"  [MISS] {src}")
            all_problems.setdefault("copies", []).append(f"missing source {src}")
            continue
        shutil.copy2(src, os.path.join(PACK, rel))
        print(f"  [OK  ] {rel}")

    print("\n== summary ==")
    n = sum(len(v) for v in all_problems.values())
    print(f"  papers written : {len(EXAM_TO_PAPER)}")
    print(f"  copies written : {sum(1 for s,_ in COPIES if os.path.exists(s))}")
    print(f"  problems       : {n}")
    if n:
        sys.exit("BUILD HAS PROBLEMS -- fix before continuing")


if __name__ == "__main__":
    main()
