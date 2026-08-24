#!/usr/bin/env python3
"""
archetype_gate.py -- mechanised fidelity + archetype-dedup gate for CCA-F mock exams.

Implements Phase 4.e.6 checks 1-5 of CCA-Orchestration-Prompt_v10.md, plus check 7
(ARCHETYPE COLLISION) defined in QUESTION-ARCHETYPE-BANLIST.md.

Prior sessions computed these by hand because the orchestration prompt assumed no code
execution was available. This script computes them from the shipped artifact instead.

Usage
-----
    python tools/archetype_gate.py mock-exams/CCA-Prep_MockTest-14_v1.html
    python tools/archetype_gate.py path/to/questions.json --priors mock-exams

Exit code 0 if every gate passes, 1 otherwise.
"""

import argparse
import collections
import glob
import itertools
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PRIORS = os.path.join(os.path.dirname(HERE), "mock-exams")

# Stems at or above this Jaccard against any prior-exam stem are treated as reskins.
ARCHETYPE_JACCARD_THRESHOLD = 0.40
CLOSING_FORMULA_CAP = 0.20
OPENING_FORMULA_CAP = 0.15

PRIMARY_DOMAINS = {
    "Customer Support Resolution Agent": {"D1", "D2", "D5"},
    "Code Generation with Claude Code": {"D3", "D5"},
    "Multi-Agent Research System": {"D1", "D2", "D5"},
    "Developer Productivity with Claude": {"D2", "D3", "D1"},
    "Claude Code for Continuous Integration": {"D3", "D4"},
    "Structured Data Extraction": {"D4", "D5"},
}

# Proper nouns that are legitimate: real products, real tools, real config keys.
ALLOWED_PROPER = set("""
Claude Code Agent SDK MCP JSON CI CD API Read Write Edit Bash Grep Glob Task WebSearch
CLAUDE SKILL AgentDefinition Python TypeScript JavaScript Node React Docker GitHub GitLab
Jenkins ISO UTC SQL OCR PDF CSV XML YAML HTTP URL Jira Slack Pydantic Explore Sonnet Opus
Haiku Batches Messages PostToolUse PreToolUse Select Excel Unix Linux Windows Java Ruby Rust
Kubernetes Terraform Postgres Redis Kafka Swagger OpenAPI Markdown None Finance Legal Support
Engineering Operations Compliance Security Platform Infrastructure Kotlin Swift Scala Certainly
January February March April June July August September October November December
""".split())

SENTENCE_START_OK = set("""
The A An In You Your Which What When Where How Why This That It If For But And After Before
During Each Both Every Only Most Best First Next Last They There These Those Their Some Same
Other Since Rather Nothing With Across Today Step Policy Production Early Message Logs
Engineers Reviewers Developers Telemetry Its Team Teams Tool Tools Model Models Server
Servers System Systems Context Window Prompt Prompts Session Sessions Schema Schemas Tokens
Token Subagent Subagents Hooks Hook Slash Plan Mode Files File Repo Repos Branch PR PRs
Analysts Auditors Inspectors Operators Two Three Four Five Six Seven Eight Nine Ten Once
Running Adding Setting Moving Switching Because Although While Given Under Over Between
Audit Coverage Latency Cost Accuracy Throughput Reviewers Support Nightly Weekly Overnight
Half Both Neither Either Several Many Few
""".split())


# ----------------------------------------------------------------------------- loading

def extract_data(path):
    """Pull the DATA object out of an exam HTML file, or load a bare JSON file."""
    if path.endswith(".json"):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    with open(path, encoding="utf-8", errors="replace") as fh:
        txt = fh.read()
    m = re.search(r"const DATA\s*=\s*(\{)", txt)
    if not m:
        raise ValueError(f"no `const DATA` object found in {path}")
    start = m.start(1)
    depth, instr, esc, end = 0, False, False, None
    for i in range(start, len(txt)):
        c = txt[i]
        if instr:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                instr = False
            continue
        if c == '"':
            instr = True
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    return json.loads(txt[start:end])


def clean(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s or "")).strip()


def toks(s):
    return set(re.findall(r"[a-z][a-z_\.\-]{2,}", s.lower()))


def words(s):
    return len(clean(s).split())


# ------------------------------------------------------------------------------ checks

def check_no_invented_names(qs):
    """Check 1 -- zero invented company/product/persona names.

    A capitalised mid-sentence word is only evidence of an invented name if the same
    word never appears in lower case anywhere else in the paper. "Attribution" in
    "Source Attribution" is a common noun that shows up lower-cased elsewhere;
    "Meridian" or "Aria" never would. This is what separates a real detection from the
    false positives a bare capitalisation regex produces.
    """
    corpus = " ".join(
        clean(q["stem"]) + " " + " ".join(q["options"]) +
        " " + q.get("whyRight", {}).get("text", "") +
        " " + " ".join(w.get("text", "") for w in q.get("whyWrong", []))
        for q in qs
    )
    # NOTE: do not lower-case the corpus first -- we want words that already appear in
    # lower case somewhere, which is what distinguishes a common noun from a coined name.
    lower_vocab = set(re.findall(r"\b[a-z]{3,}\b", corpus))

    hits = []
    for q in qs:
        # Strip inline code spans; tool and config names live there legitimately.
        bare = re.sub(r"`[^`]*`", " ", clean(q["stem"]))
        for sent in re.split(r"(?<=[.?!])\s+", bare):
            for j, raw in enumerate(sent.split()):
                w = re.sub(r"['’]s$", "", raw.strip('.,;:()"’'))
                if not re.fullmatch(r"[A-Z][a-z]{3,}", w):
                    continue
                if w in ALLOWED_PROPER or w.rstrip("s") in ALLOWED_PROPER:
                    continue
                if j == 0 and w in SENTENCE_START_OK:
                    continue
                # Sentence-initial inflected verb/adverb forms ("Migrating", "Relayed",
                # "Analyses", "Rapidly") are never coined product names.
                if j == 0 and re.search(r"(ing|ed|es|ly)$", w):
                    continue
                # The discriminator: an ordinary word capitalised by position also
                # appears lower-cased elsewhere in the paper. An invented name never does.
                if w.lower() in lower_vocab:
                    continue
                hits.append((q["g"], w))
    return len(hits) == 0, hits


def check_letter_tally(qs, nblocks=4):
    """Check 2 -- correct-answer letter balance, single-answer items only."""
    per_block = collections.defaultdict(collections.Counter)
    overall = collections.Counter()
    for q in qs:
        if q.get("selectN"):
            continue
        L = chr(65 + q["correct"])
        per_block[q["block"]][L] += 1
        overall[L] += 1
    problems = []
    for b in range(nblocks):
        c = per_block[b]
        n = sum(c.values())
        lo, hi = (n // 4) - 1, (n + 3) // 4 + 1
        for L in "ABCD":
            if not (lo <= c[L] <= hi):
                problems.append(f"block {b+1} letter {L}={c[L]} outside [{lo},{hi}]")
    n = sum(overall.values())
    target = n / 4
    for L in "ABCD":
        if abs(overall[L] - target) > 2:
            problems.append(f"exam-wide letter {L}={overall[L]} far from {target:.1f}")
    return not problems, {"per_block": {k: dict(v) for k, v in per_block.items()},
                          "overall": dict(overall), "problems": problems}


def check_word_counts(qs):
    """Check 3 -- stem median 50-55, stem cap 95, option cap 35."""
    stems = sorted(words(q["stem"]) for q in qs)
    opts = sorted(words(o) for q in qs for o in q["options"])
    med = stems[len(stems) // 2]
    over_stem = [(q["g"], words(q["stem"])) for q in qs if words(q["stem"]) > 95]
    over_opt = [(q["g"], i, words(o)) for q in qs for i, o in enumerate(q["options"])
                if words(o) > 35]
    ok = (50 <= med <= 55) and not over_stem and not over_opt
    return ok, {"stem_min": stems[0], "stem_median": med, "stem_max": stems[-1],
                "opt_min": opts[0], "opt_median": opts[len(opts) // 2], "opt_max": opts[-1],
                "over_stem": over_stem, "over_opt": over_opt}


def check_block_domains(qs, blocks):
    """Check 4 -- every primary domain outnumbers every non-primary domain, per block."""
    problems, table = [], {}
    for bi, b in enumerate(blocks):
        prim = PRIMARY_DOMAINS.get(b["label"])
        if prim is None:
            problems.append(f"block {bi+1}: unknown scenario {b['label']!r}")
            continue
        tally = collections.Counter(q["domain"] for q in qs if q["block"] == bi)
        table[b["label"]] = dict(tally)
        pv = [tally.get(d, 0) for d in prim]
        npv = [tally.get(d, 0) for d in ("D1", "D2", "D3", "D4", "D5") if d not in prim]
        if pv and npv and min(pv) <= max(npv):
            problems.append(
                f"block {bi+1} ({b['label']}): min primary {min(pv)} <= max non-primary {max(npv)}")
    return not problems, {"table": table, "problems": problems}


def check_inline_tokens(qs):
    """Check 5 -- 15-30% of options carry an inline code/config token; 20-25% target."""
    total = sum(len(q["options"]) for q in qs)
    hits = sum(1 for q in qs for o in q["options"] if "`" in o)
    rate = hits / total if total else 0
    return 0.15 <= rate <= 0.30, {"hits": hits, "total": total, "rate": rate}


def closing_sentence(q):
    """The rhetorical ask of a stem.

    Multiple-response items end on a mandatory "Select two."/"Select three."
    instruction, which is a format requirement rather than a rhetorical choice. For
    those, the real ask is the sentence before it.
    """
    sents = re.split(r"(?<=[.?!])\s+", clean(q["stem"]))
    if q.get("selectN") and len(sents) > 1 and re.fullmatch(r"select\s+\w+\.?", sents[-1], re.I):
        return sents[-2].lower()
    return sents[-1].lower()


def check_archetypes(qs, prior_stems):
    """Check 7 -- no reskins of prior questions, no formula monoculture."""
    problems = []

    new = [(q["g"], clean(q["stem"]), toks(clean(q["stem"]))) for q in qs]
    collisions = []
    for g, stem, t in new:
        worst = (0.0, None)
        for pg, ptext, pt in prior_stems:
            u = t | pt
            if not u:
                continue
            j = len(t & pt) / len(u)
            if j > worst[0]:
                worst = (j, pg)
        if worst[0] >= ARCHETYPE_JACCARD_THRESHOLD:
            collisions.append((g, round(worst[0], 3), worst[1]))
    if collisions:
        problems.append(f"{len(collisions)} stem(s) at/above {ARCHETYPE_JACCARD_THRESHOLD} vs priors")

    # intra-paper duplicates
    intra = []
    for (ga, sa, ta), (gb, sb, tb) in itertools.combinations(new, 2):
        u = ta | tb
        if not u:
            continue
        j = len(ta & tb) / len(u)
        if j >= ARCHETYPE_JACCARD_THRESHOLD:
            intra.append((ga, gb, round(j, 3)))
    if intra:
        problems.append(f"{len(intra)} intra-paper stem pair(s) at/above threshold")

    # closing-formula rate
    closes = collections.Counter()
    for q in qs:
        closes[closing_sentence(q)] += 1
    n = len(qs)
    top_close, top_close_n = closes.most_common(1)[0]
    if top_close_n / n > CLOSING_FORMULA_CAP:
        problems.append(f"closing formula {top_close!r} at {top_close_n}/{n}")

    # same closing sentence twice inside one block
    per_block_close = collections.defaultdict(collections.Counter)
    for q in qs:
        per_block_close[q["block"]][closing_sentence(q)] += 1
    for b, c in per_block_close.items():
        for sent, k in c.items():
            if k > 1:
                problems.append(f"block {b+1} repeats closing sentence {sent[:50]!r} x{k}")

    # opening-formula rate
    opens = collections.Counter(" ".join(clean(q["stem"]).split()[:2]).lower() for q in qs)
    top_open, top_open_n = opens.most_common(1)[0]
    if top_open_n / n > OPENING_FORMULA_CAP:
        problems.append(f"opening formula {top_open!r} at {top_open_n}/{n}")

    return not problems, {
        "collisions": collisions, "intra": intra,
        "top_closing": (top_close, top_close_n), "top_opening": (top_open, top_open_n),
        "problems": problems,
    }


def check_multi_response(qs):
    """Exam-14 addition -- validate select-N items are well formed."""
    problems = []
    mr = [q for q in qs if q.get("selectN")]
    for q in mr:
        n = q["selectN"]
        if not isinstance(q["correct"], list):
            problems.append(f"Q{q['g']}: selectN set but `correct` is not a list")
            continue
        if len(q["correct"]) != n:
            problems.append(f"Q{q['g']}: selectN={n} but {len(q['correct'])} correct indices")
        if len(set(q["correct"])) != len(q["correct"]):
            problems.append(f"Q{q['g']}: duplicate indices in `correct`")
        if any(i >= len(q["options"]) for i in q["correct"]):
            problems.append(f"Q{q['g']}: correct index out of range")
        if len(q["options"]) < n + 2:
            problems.append(f"Q{q['g']}: only {len(q['options'])} options for select-{n}")
        if not re.search(r"select\s+(two|three|2|3)\b", clean(q["stem"]), re.I):
            problems.append(f"Q{q['g']}: stem does not state how many to select")
        wrong = {w["option"] for w in q["whyWrong"]}
        expected = set(range(len(q["options"]))) - set(q["correct"])
        if wrong != expected:
            problems.append(f"Q{q['g']}: whyWrong covers {sorted(wrong)}, expected {sorted(expected)}")
    for q in qs:
        if not q.get("selectN"):
            if not isinstance(q["correct"], int):
                problems.append(f"Q{q['g']}: single-answer item has non-int `correct`")
            if len(q["options"]) != 4:
                problems.append(f"Q{q['g']}: single-answer item has {len(q['options'])} options")
    return not problems, {"count": len(mr), "problems": problems}


# -------------------------------------------------------------------------------- main

def load_priors(priors_dir, exclude_exam):
    out, seen = [], set()
    for path in sorted(glob.glob(os.path.join(priors_dir, "CCA-Prep_MockTest-*.html"))):
        try:
            d = extract_data(path)
        except Exception:
            continue
        if d.get("exam_n") == exclude_exam:
            continue
        key = d.get("exam_n")
        for q in d.get("questions", []):
            s = clean(q.get("stem", ""))
            if s in seen:
                continue
            seen.add(s)
            out.append((f"e{key}Q{q.get('g')}", s, toks(s)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--priors", default=DEFAULT_PRIORS)
    args = ap.parse_args()

    data = extract_data(args.target)
    qs, blocks = data["questions"], data.get("blocks", [])
    priors = load_priors(args.priors, data.get("exam_n"))

    print(f"Exam {data.get('exam_n')} · {len(qs)} questions · {len(priors)} prior stems loaded\n")

    results = []
    ok, d = check_no_invented_names(qs)
    results.append(("1 · no invented names", ok, f"{len(d)} flagged" + (f" -> {d[:6]}" if d else "")))
    ok, d = check_letter_tally(qs, len(blocks) or 4)
    results.append(("2 · letter tally (SA only)", ok, f"{d['overall']}" + ("; " + "; ".join(d["problems"]) if d["problems"] else "")))
    ok, d = check_word_counts(qs)
    results.append(("3 · word counts", ok, f"stem {d['stem_min']}/{d['stem_median']}/{d['stem_max']}, opt max {d['opt_max']}"
                    + (f"; OVER stem {d['over_stem']}" if d["over_stem"] else "")
                    + (f"; OVER opt {d['over_opt']}" if d["over_opt"] else "")))
    ok, d = check_block_domains(qs, blocks)
    results.append(("4 · block vs primary domains", ok, "; ".join(d["problems"]) or json.dumps(d["table"])))
    ok, d = check_inline_tokens(qs)
    results.append(("5 · inline token rate", ok, f"{d['hits']}/{d['total']} = {d['rate']*100:.1f}%"))
    ok, d = check_multi_response(qs)
    results.append(("6 · multiple-response validity", ok, f"{d['count']} MR items" + ("; " + "; ".join(d["problems"]) if d["problems"] else "")))
    ok, d = check_archetypes(qs, priors)
    detail = (f"max-vs-prior collisions={len(d['collisions'])}, intra={len(d['intra'])}, "
              f"top close {d['top_closing'][1]}x, top open {d['top_opening'][1]}x")
    if d["collisions"]:
        detail += f"\n      collisions: {d['collisions'][:8]}"
    if d["problems"]:
        detail += "\n      " + "\n      ".join(d["problems"])
    results.append(("7 · archetype collision", ok, detail))

    width = max(len(r[0]) for r in results)
    allok = True
    for name, ok, detail in results:
        allok &= ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {name.ljust(width)}  {detail}")
    print("\n" + ("ALL GATES PASS" if allok else "GATE FAILURES PRESENT"))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
