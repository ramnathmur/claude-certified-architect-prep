#!/usr/bin/env python3
"""Rebuild the drill deck's `mockMap` from the twelve papers actually in the pack.

Why this is needed: the deck shipped with a mockMap covering only Exams 2, 3, 4 and the
Exam-2 retrofit -- it was generated from a git worktree that held only those three papers.
None of them is in this pack, so the deck's "Import mock results" feature would fail for
every paper a colleague could actually sit, with "No question map for exam N".

The map schema, read from the deck's own parseImport():
    mockMap = { "<paperNum>": { "<questionNum>": {d: domain, c: [cites], t: stem excerpt} } }
Matching is by citation string, lower-cased and trimmed (normCite), against each card's
`cites` array. Cards use "Domain-1_v2 §1.1"; the papers cite "CCA-Prep_Domain-1_v2.md §1.1",
so the prefix and extension are stripped. A sub-section cite such as §3.7.2 additionally
emits its parent §3.7, because cards are written at parent-section granularity.
"""
import json, os, re, sys

ROOT = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep"
PACK = os.path.join(ROOT, "Outputs", "CCA-F-Prep-Pack_v1")
DECK = os.path.join(PACK, "02-drill-deck", "drill-deck.html")
PAPERS = os.path.join(PACK, "01-mock-exams")


def brace_slice(s, start):
    """Return the balanced {...} or [...] beginning at the first bracket at/after start."""
    while s[start] not in "{[":
        start += 1
    open_c, close_c = s[start], "}" if s[start] == "{" else "]"
    depth, instr, esc = 0, False, False
    for i in range(start, len(s)):
        c = s[i]
        if instr:
            if esc: esc = False
            elif c == "\\": esc = True
            elif c == '"': instr = False
            continue
        if c == '"': instr = True
        elif c == open_c: depth += 1
        elif c == close_c:
            depth -= 1
            if depth == 0:
                return start, i + 1
    raise ValueError("unbalanced")


def paper_data(path):
    s = open(path, encoding="utf-8").read()
    i = s.index("const DATA =")
    a, b = brace_slice(s, i)
    return json.loads(s[a:b])


def to_card_cite(raw):
    """Normalise any of the four citation formats the papers use onto the deck's vocabulary.

    Papers were written by several generations of the generator, so a single field may read
    any of:
        'D1 §1.1'                            (Papers 3-10)
        'Domain-1_v2 §1.14; Key Distinction #6'  (Papers 1-2, composite)
        'CCA-Prep_Domain-1_v2.md §1.1'       (Papers 11-12)
    Cards carry 'Domain-1_v2 §1.1', 'Key-Distinctions_v1 #6', 'Official-Guide p.13',
    'Exam-Mechanics_v2 <label>'. Matching is exact after lower-casing, so every variant has
    to be folded onto the card form or the import silently matches nothing.
    """
    out = []
    for part in re.split(r"[;,]\s*", str(raw or "")):
        c = part.strip()
        if not c:
            continue

        # Domain sections, in any of the three spellings
        m = (re.match(r"(?:CCA-Prep_)?Domain-(\d)_v\d(?:\.md)?\s*§?\s*([\d.]+)", c, re.I)
             or re.match(r"\bD(\d)\s*§?\s*([\d.]+)", c, re.I))
        if m:
            dom, sec = m.group(1), m.group(2).rstrip(".")
            out.append(f"Domain-{dom}_v2 §{sec}")
            bits = sec.split(".")
            if len(bits) > 2:                        # §3.7.2 -> also the parent §3.7
                out.append(f"Domain-{dom}_v2 §{bits[0]}.{bits[1]}")
            continue

        # Key Distinctions, spelled either way
        m = re.match(r"(?:Key[-\s]?Distinctions?(?:_v\d)?|KD)\s*#?\s*(\d+)", c, re.I)
        if m:
            out.append(f"Key-Distinctions_v1 #{m.group(1)}")
            continue

        m = re.match(r"(?:CCA-Prep_)?Exam-Mechanics_v\d(?:\.md)?\s*(.+)", c, re.I)
        if m:
            out.append(f"Exam-Mechanics_v2 {m.group(1).strip()}")
            continue

        m = re.match(r"Official[-\s]Guide\s*(p\.?\s*\d+)", c, re.I)
        if m:
            out.append("Official-Guide " + m.group(1).replace(" ", ""))
            continue

        out.append(c)
    return out or [str(raw)]


def main():
    deck = open(DECK, encoding="utf-8").read()
    i = deck.index('"mockMap"')
    a, b = brace_slice(deck, i + len('"mockMap"'))
    old = json.loads(deck[a:b])

    # card citation vocabulary, so coverage can be measured rather than assumed
    j = deck.index('"cards"')
    ca, cb = brace_slice(deck, j + len('"cards"'))
    cards = json.loads(deck[ca:cb])
    card_cites = set()
    for c in cards:
        for x in (c.get("cites") or []):
            card_cites.add(x.strip().lower())

    new = {}
    print(f"{'paper':<7} {'questions':>9} {'matched':>8} {'coverage':>9}   unmatched sections")
    print("-" * 74)
    total_q = total_m = 0
    for n in range(1, 13):
        p = os.path.join(PAPERS, f"Paper-{n:02d}.html")
        d = paper_data(p)
        assert d["exam_n"] == n, f"Paper-{n:02d} exam_n is {d['exam_n']}, expected {n}"
        m, matched, missing = {}, 0, set()
        for q in d["questions"]:
            cites = to_card_cite(q["whyRight"]["cite"])
            hit = any(c.lower() in card_cites for c in cites)
            if hit: matched += 1
            else: missing.add(cites[0])
            m[str(q["g"])] = {
                "d": q["domain"],
                "c": cites,
                "t": re.sub(r"<[^>]+>", "", q["stem"])[:100],
            }
        new[str(n)] = m
        total_q += len(d["questions"]); total_m += matched
        pct = matched / len(d["questions"]) * 100
        print(f"Paper {n:<2}{len(d['questions']):>9}{matched:>9}{pct:>8.0f}%   "
              f"{', '.join(sorted(missing)[:3]) if missing else '-'}")

    print("-" * 74)
    print(f"{'TOTAL':<7}{total_q:>9}{total_m:>9}{total_m/total_q*100:>8.0f}%")
    print(f"\nold map covered exams: {sorted(old.keys())}")
    print(f"new map covers papers: {sorted(new.keys(), key=int)}")

    deck = deck[:a] + json.dumps(new, ensure_ascii=False, separators=(",", ":")) + deck[b:]
    # the error copy assumes an out-of-date deck; make it accurate for this pack
    deck = deck.replace("The deck was built before that exam existed.",
                        "This deck covers Papers 1-12 in this pack.")
    # the pack calls them Papers, not Mocks -- keep one vocabulary across the whole thing
    before = deck
    deck = deck.replace('ok-msg">Mock \' + esc(examN)', 'ok-msg">Paper \' + esc(examN)')
    deck = deck.replace("Paste the results JSON from a mock exam.",
                        "Paste the results JSON from a practice paper.")
    deck = deck.replace("Import mock exam results", "Import your paper results")
    deck = deck.replace("Import mock results", "Import paper results")
    if deck == before:
        print("  WARNING: no vocabulary replacements landed -- deck wording may have changed")
    open(DECK, "w", encoding="utf-8").write(deck)
    print(f"\nwrote {DECK}")

    if total_m / total_q < 0.80:
        sys.exit(f"COVERAGE TOO LOW: only {total_m/total_q*100:.0f}% of questions map to a card")


if __name__ == "__main__":
    main()
