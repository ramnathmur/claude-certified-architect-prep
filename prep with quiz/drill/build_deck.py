"""build_deck.py -- deck pipeline for the CCA-F drill app.

Subcommands:
    extract-mocks  Parse mock-exam HTML into deck/gen/mock-qbank.json (+ importer cite map).
    cites          Build deck/cite-manifest.json from the corpus.
    merge          Fold deck/gen/*.gen.json into deck/*.cards.json, assigning stable ids.
    validate       Run every quality gate over deck/*.cards.json. Exits non-zero on failure.
    embed          Inject the deck into the app HTML between marker comments.
    report         Print deck statistics.

Source is deliberately pure ASCII (section signs are written as escapes) so Windows
console encodings cannot corrupt it. Run from anywhere; paths resolve off this file.
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

# Keep console output UTF-8 safe on Windows.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SECT = "§"          # section sign
EMDASH = "—"        # em dash
REPLACEMENT = "�"   # U+FFFD

HERE = os.path.dirname(os.path.abspath(__file__))
QUIZ = os.path.dirname(HERE)                     # "prep with quiz"
ROOT = os.path.dirname(QUIZ)                     # project root
DECK = os.path.join(HERE, "deck")
GEN = os.path.join(DECK, "gen")
AUDIT = os.path.join(HERE, "audit")
APP = os.path.join(HERE, "CCA-Prep_Drill_v1.html")
MOCKS_DIR = os.path.join(QUIZ, "mock-exams")

MARK_START = "/*__DECK_JSON_START__*/"
MARK_END = "/*__DECK_JSON_END__*/"

DOMAINS = ["D1", "D2", "D3", "D4", "D5", "EX"]
DOMAIN_FILES = {
    "D1": "CCA-Prep_Domain-1_v2.md",
    "D2": "CCA-Prep_Domain-2_v2.md",
    "D3": "CCA-Prep_Domain-3_v2.md",
    "D4": "CCA-Prep_Domain-4_v2.md",
    "D5": "CCA-Prep_Domain-5_v2.md",
}
DOMAIN_NAMES = {
    "D1": "Agentic Architecture & Orchestration",
    "D2": "Tool Design & MCP Integration",
    "D3": "Claude Code Configuration & Workflows",
    "D4": "Prompt Engineering & Structured Output",
    "D5": "Context Management & Reliability",
    "EX": "Exam Mechanics",
}
# Generation targets, set from the official exam weights before the deck was written.
QUOTA = {"D1": 110, "D2": 73, "D3": 81, "D4": 81, "D5": 61, "EX": 14}

# The gate is proportional, not absolute. The cold audit removed 55 cards that were
# semantic duplicates, so the deck is smaller than the generation targets by design --
# what has to hold is that each domain still occupies its exam share of the deck.
# EXAM_WEIGHTS are percentages of scored content; EX sits outside them.
EXAM_WEIGHTS = {"D1": 27.0, "D2": 18.0, "D3": 20.0, "D4": 20.0, "D5": 15.0}
WEIGHT_TOLERANCE = 3.0   # percentage points a domain may drift from its exam weight
EX_FLOOR = 10            # exam-mechanics cards are cheap marks; keep an absolute floor

# Reserved known-gap tags and their minimum card counts (see CARD-SPEC.md section 7).
# d5.2 is deliberately small: prompt caching is on the official out-of-scope list and
# appears in official samples only as a wrong option. See CARD-SPEC.md section 7.
GAP_MINIMUMS = {
    "d1.1": 10, "d2.1": 4, "d2.2": 4, "d3.6": 7,
    "d3.1": 5, "d4.5": 8, "d5.1": 6, "d5.2": 2,
}

TYPES = {"concept", "trap", "fact", "scenario"}

LEN_CAPS = {"front": 260, "front_scenario": 420, "back": 320, "trap": 200}

BANNED = [
    "leverage", "leverages", "leveraging", "robust", "robustly", "seamless", "seamlessly",
    "comprehensive", "comprehensively", "delve", "delves", "deep dive", "ecosystem",
    "holistic", "holistically", "streamline", "streamlined", "streamlines", "empower",
    "empowers", "unlock", "unlocks", "supercharge", "elevate", "crucial", "pivotal",
    "game-changing", "cutting-edge", "journey", "landscape", "realm", "harness",
    "harnesses", "foster", "fosters",
]
BANNED_PHRASES = [
    "it's important to note", "it is important to note",
    "not just", "isn't just", "is not just", "more than just",
]
# Diagnose-negate-reveal openers, banned in `back`.
RHETORIC = [
    re.compile(r"^\s*(no|nope|wrong)[,.]", re.I),
    re.compile(r"^\s*(it|that|this)\s+is\s+not\b", re.I),
    re.compile(r"^\s*(it|that|this)'s\s+not\b", re.I),
    re.compile(r"\bnot\s+\w+[,.]\s+(it|that|this)\s+is\b", re.I),
]

ID_RE = re.compile(r"^(d[1-5]|ex)-\d{3}$")
CITE_DOMAIN_RE = re.compile(r"^Domain-([1-5])_v2 " + SECT + r"(\d+\.\d+)$")
CITE_KD_RE = re.compile(r"^Key-Distinctions_v1 #(\d+)$")
CITE_MECH_RE = re.compile(r"^Exam-Mechanics_v2 (.+)$")
CITE_GUIDE_RE = re.compile(r"^Official-Guide p\.(\d+)$")

STOPWORDS = set("""a an the of to in on for with and or is are was were be been being do does did
this that these those it its as at by from not no if then than when what which who whom how why
you your i we they he she them his her our their there here can could should would will shall may
might must have has had into over under about between during without within across per via""".split())


# ---------------------------------------------------------------- helpers

def read_text(path):
    """Read a file as UTF-8, falling back to cp1252 only if strict UTF-8 fails."""
    with open(path, "rb") as fh:
        raw = fh.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        warn("non-UTF8 bytes in %s -- falling back to cp1252" % os.path.basename(path))
        return raw.decode("cp1252")


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


def load_json(path):
    return json.loads(read_text(path))


def warn(msg):
    print("  [warn] " + msg)


def normalize_text(s):
    """NFC-normalize and replace typographic look-alikes with the forms the spec allows."""
    s = unicodedata.normalize("NFC", s)
    for bad, good in (
        ("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
        ("–", EMDASH), ("→", " to "), (" ", " "),
    ):
        s = s.replace(bad, good)
    return s.strip()


def strip_code(s):
    """Remove backtick-quoted spans so identifier names never trip the prose checks."""
    return re.sub(r"`[^`]*`", " ", s)


def shingles(text):
    """Content words for similarity comparison.

    Identifiers inside backticks are KEPT here -- they are the most discriminative
    tokens a card has. Stripping them (as the prose checks do) once let two
    byte-identical fronts whose only content was stopwords plus code reduce to two
    empty sets and score 0.0 against each other.
    """
    plain = text.replace("`", " ")
    words = [w for w in re.findall(r"[a-z0-9_.\-]+", plain.lower()) if w not in STOPWORDS]
    return set(words)


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / float(len(a | b))


def norm_front(text):
    """Aggressive normalization for the exact-duplicate backstop."""
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def deck_files():
    out = []
    for d in DOMAINS:
        p = os.path.join(DECK, "%s.cards.json" % d.lower())
        if os.path.exists(p):
            out.append((d, p))
    return out


def load_deck():
    cards = []
    for _d, path in deck_files():
        cards.extend(load_json(path))
    return cards


# ---------------------------------------------------------------- extract-mocks

def extract_data_object(html):
    """Pull the single-line `const DATA = {...};` literal out of a mock exam file."""
    idx = html.find("const DATA = {")
    if idx < 0:
        return None
    start = html.index("{", idx)
    depth, in_str, esc = 0, False, False
    for i in range(start, len(html)):
        ch = html[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(html[start:i + 1])
    return None


def canonicalize_cite(c):
    """Fold the citation variants the mock exams use into the CARD-SPEC grammar.

    The mocks were written by several generations of the exam generator and about 19%
    of their citations drift from the canonical form. The importer joins cards to missed
    questions on this string, so a variant that fails to normalize silently costs coverage.
    Handles: trailing parentheticals, 'Key-Distinctions #N' without the _v1, section-sign
    instead of hash for KD entries, and three-level section numbers (only two exist).
    """
    c = normalize_text(c)
    c = re.sub(r"\s*\([^)]*\)\s*$", "", c)                       # drop "(batch vs real-time table)"
    c = re.sub(r"^Key-Distinctions(?:_v1)?\s*[#" + SECT + r"]\s*(\d+)$",
               r"Key-Distinctions_v1 #\1", c)
    m = re.match(r"^(Domain-[1-5]_v2)\s*" + SECT + r"\s*(\d+\.\d+)(?:\.\d+)*$", c)
    if m:                                                         # 3.7.3 -> 3.7
        c = "%s %s%s" % (m.group(1), SECT, m.group(2))
    return c.strip()


def split_cite(raw):
    """'Key-Distinctions_v1 #5; Domain-1_v2 SECT1.1' -> both, canonicalized.

    Splits on ';' and on ' / ', which the older mock generations used interchangeably.
    """
    if not raw:
        return []
    # Strip parentheticals before splitting: one mock writes "(tool bundling / composite
    # tools)", whose inner slash would otherwise be mistaken for a citation separator.
    raw = re.sub(r"\([^)]*\)", "", raw)
    parts = re.split(r";|\s/\s", raw)
    return [canonicalize_cite(p) for p in parts if p.strip()]


def cmd_extract_mocks(_args):
    files = sorted(f for f in os.listdir(MOCKS_DIR)
                   if f.startswith("CCA-Prep_MockTest-") and f.endswith(".html"))
    qbank, mockmap = [], {}
    for name in files:
        path = os.path.join(MOCKS_DIR, name)
        html = read_text(path)
        if REPLACEMENT in html:
            warn("%s contains U+FFFD -- source is already damaged" % name)
        data = extract_data_object(html)
        if not data or "questions" not in data:
            warn("no DATA object in %s -- skipped (legacy format?)" % name)
            continue
        exam_n = data.get("exam_n")
        # Prefer the number in the filename: one mock's payload has a stale exam_n.
        m = re.search(r"MockTest-(\d+)", name)
        if m and int(m.group(1)) != exam_n:
            warn("%s: DATA.exam_n=%s disagrees with filename -- using %s"
                 % (name, exam_n, m.group(1)))
            exam_n = int(m.group(1))
        key = str(exam_n) + ("-retrofit" if "Retrofit" in name else "")
        mockmap[key] = {}
        for q in data["questions"]:
            right = q.get("whyRight") or {}
            primary = split_cite(right.get("cite", ""))
            wrong = []
            for w in q.get("whyWrong") or []:
                wrong.extend(split_cite(w.get("cite", "")))
            all_cites = list(dict.fromkeys(primary + wrong))
            stem = normalize_text(q.get("stem", ""))
            entry = {
                "exam": key,
                "q": q.get("g"),
                "domain": q.get("domain"),
                "block": q.get("blockLabel"),
                "stem": stem,
                "cites": primary,
                "allCites": all_cites,
            }
            qbank.append(entry)
            # Importer map: keep it small -- q number to domain + cites + a short topic label.
            mockmap[key][str(q.get("g"))] = {
                "d": q.get("domain"),
                "c": primary,
                "t": stem[:90],
            }
        print("  %-40s exam %-12s %d questions" % (name, key, len(data["questions"])))
    write_json(os.path.join(GEN, "mock-qbank.json"), qbank)
    write_json(os.path.join(GEN, "mock-citemap.json"), mockmap)
    print("extract-mocks: %d questions from %d exams" % (len(qbank), len(mockmap)))
    return 0


# ---------------------------------------------------------------- cites

def build_manifest():
    manifest = {"domain": [], "kd": [], "mech": [], "guide": []}
    for dom, fname in DOMAIN_FILES.items():
        path = os.path.join(QUIZ, fname)
        if not os.path.exists(path):
            warn("missing corpus file %s" % fname)
            continue
        stem = fname.replace("CCA-Prep_", "").replace(".md", "")
        for line in read_text(path).splitlines():
            m = re.match(r"^##\s+(\d+\.\d+)\s", line)
            if m:
                manifest["domain"].append("%s %s%s" % (stem, SECT, m.group(1)))
    kd_path = os.path.join(QUIZ, "CCA-Prep_Key-Distinctions_v1.md")
    for line in read_text(kd_path).splitlines():
        m = re.match(r"^###\s+(\d+)\.\s", line)
        if m:
            manifest["kd"].append("Key-Distinctions_v1 #%s" % m.group(1))
    mech_path = os.path.join(QUIZ, "CCA-Prep_Exam-Mechanics_v2.md")
    for line in read_text(mech_path).splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            manifest["mech"].append("Exam-Mechanics_v2 %s" % m.group(1))
    guide_path = os.path.join(QUIZ, "source", "CCA-F-Official-Exam-Guide_text.txt")
    if os.path.exists(guide_path):
        pages = set(re.findall(r"===\s*PAGE\s+(\d+)\s*===", read_text(guide_path)))
        if not pages:
            pages = set(str(n) for n in range(1, 60))
            warn("no PAGE markers in the guide text -- accepting p.1-59")
        manifest["guide"] = ["Official-Guide p.%s" % n for n in sorted(pages, key=int)]
    return manifest


def manifest_lookup(manifest):
    """Return (exact_set, mech_prefixes) for cite resolution."""
    exact = set(manifest["domain"]) | set(manifest["kd"]) | set(manifest["guide"])
    mech = [m.split(" ", 1)[1].lower() for m in manifest["mech"]]
    return exact, mech


def resolve_cite(cite, exact, mech_headings):
    if cite in exact:
        return True
    m = CITE_MECH_RE.match(cite)
    if m:
        want = m.group(1).strip().lower()
        return any(h.startswith(want) or want.startswith(h) for h in mech_headings)
    return False


def cmd_cites(_args):
    manifest = build_manifest()
    write_json(os.path.join(DECK, "cite-manifest.json"), manifest)
    print("cite-manifest: %d domain sections, %d key distinctions, %d mechanics headings, %d guide pages"
          % (len(manifest["domain"]), len(manifest["kd"]), len(manifest["mech"]), len(manifest["guide"])))
    kd_max = max((int(c.rsplit("#", 1)[1]) for c in manifest["kd"]), default=0)
    print("  key distinctions run #1 to #%d" % kd_max)
    return 0


# ---------------------------------------------------------------- validation

def check_card(card, idx, where, manifest_sets, issues):
    exact, mech = manifest_sets

    def bad(kind, msg):
        issues.append({"where": where, "idx": idx, "id": card.get("id"),
                       "kind": kind, "msg": msg})

    cid = card.get("id")
    if cid is not None and not ID_RE.match(str(cid)):
        bad("schema", "bad id %r" % cid)

    dom = card.get("domain")
    if dom not in DOMAINS:
        bad("schema", "bad domain %r" % dom)

    ctype = card.get("type")
    if ctype not in TYPES:
        bad("schema", "bad type %r" % ctype)

    for field in ("front", "back"):
        val = card.get(field)
        if not isinstance(val, str) or not val.strip():
            bad("schema", "missing %s" % field)

    front = card.get("front") or ""
    back = card.get("back") or ""
    trap = card.get("trap") or ""

    cap = LEN_CAPS["front_scenario"] if ctype == "scenario" else LEN_CAPS["front"]
    if len(front) > cap:
        bad("length", "front %d chars (cap %d)" % (len(front), cap))
    if len(back) > LEN_CAPS["back"]:
        bad("length", "back %d chars (cap %d)" % (len(back), LEN_CAPS["back"]))
    if trap and len(trap) > LEN_CAPS["trap"]:
        bad("length", "trap %d chars (cap %d)" % (len(trap), LEN_CAPS["trap"]))

    # Encoding hygiene.
    for field, val in (("front", front), ("back", back), ("trap", trap)):
        if REPLACEMENT in val:
            bad("encoding", "%s contains U+FFFD" % field)
        for ch in val:
            if ord(ch) > 0x2014 and ch not in (SECT,):
                bad("encoding", "%s has unexpected char U+%04X (%r)" % (field, ord(ch), ch))
                break
        if val.count("`") % 2 != 0:
            bad("encoding", "%s has unbalanced backticks" % field)

    # Prose contract.
    for field, val in (("front", front), ("back", back), ("trap", trap)):
        plain = strip_code(val).lower()
        for word in BANNED:
            if re.search(r"\b" + re.escape(word) + r"\b", plain):
                bad("prose", "%s uses banned word '%s'" % (field, word))
        for phrase in BANNED_PHRASES:
            if phrase in plain:
                bad("prose", "%s uses banned phrase '%s'" % (field, phrase))
    for rx in RHETORIC:
        if rx.search(strip_code(back)):
            bad("prose", "back uses diagnose-negate-reveal rhetoric")
            break

    # Cites.
    cites = card.get("cites")
    if not isinstance(cites, list) or not cites:
        bad("cite", "no cites")
    else:
        if len(cites) > 2:
            bad("cite", "%d cites (max 2)" % len(cites))
        for c in cites:
            if not resolve_cite(c, exact, mech):
                bad("cite", "unresolvable cite %r" % c)
            m = CITE_KD_RE.match(c or "")
            if m and int(m.group(1)) > 25:
                bad("cite", "Key-Distinctions #%s does not exist (file ends at #25)" % m.group(1))

    # Flags.
    if not isinstance(card.get("core"), bool):
        bad("schema", "core must be boolean")
    if not isinstance(card.get("rev"), bool):
        bad("schema", "rev must be boolean")
    if card.get("rev") and ctype != "fact":
        bad("schema", "rev=true only allowed on type 'fact'")

    tags = card.get("tags")
    if not isinstance(tags, list):
        bad("schema", "tags must be a list")
    elif "known-gap" in tags and not any(t in GAP_MINIMUMS for t in tags):
        bad("schema", "known-gap without a sub-domain tag")

    # Answer leakage: a long shared shingle run between front and back.
    fs, bs = shingles(front), shingles(back)
    if fs and bs:
        overlap = len(fs & bs) / float(len(fs))
        if overlap > 0.75 and len(fs) >= 5:
            bad("leak", "front shares %.0f%% of its content words with back" % (overlap * 100))


def find_duplicates(cards, threshold=0.55):
    dups = []
    sh = [(c, shingles(c.get("front", "")), norm_front(c.get("front", ""))) for c in cards]
    for i in range(len(sh)):
        for j in range(i + 1, len(sh)):
            score = jaccard(sh[i][1], sh[j][1])
            # Backstop: identical normalized fronts are duplicates whatever the shingles say.
            if sh[i][2] and sh[i][2] == sh[j][2]:
                score = 1.0
            if score >= threshold:
                dups.append((sh[i][0].get("id"), sh[j][0].get("id"), round(score, 2),
                             sh[i][0].get("front", "")[:70]))
    return dups


def external_collisions(cards, threshold=0.5):
    """Fronts that echo a mock stem or a practice-test stem too closely."""
    refs = []
    qbank_path = os.path.join(GEN, "mock-qbank.json")
    if os.path.exists(qbank_path):
        for q in load_json(qbank_path):
            refs.append(("mock %s q%s" % (q.get("exam"), q.get("q")), shingles(q.get("stem", ""))))
    stems_path = os.path.join(QUIZ, "PRACTICE-TEST-STEMS_v1.md")
    if os.path.exists(stems_path):
        for line in read_text(stems_path).splitlines():
            m = re.match(r"^\s*\d+\.\s+(.{40,})$", line)
            if m:
                refs.append(("practice-test", shingles(m.group(1))))
    hits = []
    for c in cards:
        cs = shingles(c.get("front", ""))
        for label, rs in refs:
            score = jaccard(cs, rs)
            if score >= threshold:
                hits.append((c.get("id"), label, round(score, 2)))
    return hits


def cmd_validate(args):
    manifest_path = os.path.join(DECK, "cite-manifest.json")
    if not os.path.exists(manifest_path):
        cmd_cites(args)
    manifest = load_json(manifest_path)
    sets = manifest_lookup(manifest)

    target = args.target or "deck"
    if target == "gen":
        files = [(None, os.path.join(GEN, f)) for f in sorted(os.listdir(GEN))
                 if f.endswith(".gen.json")]
    else:
        files = deck_files()
    if not files:
        print("validate: nothing to check in %s" % target)
        return 1

    issues, all_cards = [], []
    for _dom, path in files:
        cards = load_json(path)
        label = os.path.basename(path)
        for i, card in enumerate(cards):
            check_card(card, i, label, sets, issues)
        all_cards.extend(cards)

    print("validate: %d cards across %d files" % (len(all_cards), len(files)))

    dups = find_duplicates(all_cards)
    for a, b, score, text in dups:
        issues.append({"where": "deck", "idx": -1, "id": "%s~%s" % (a, b),
                       "kind": "duplicate", "msg": "%.2f similar: %s" % (score, text)})

    for cid, label, score in external_collisions(all_cards):
        issues.append({"where": "deck", "idx": -1, "id": cid, "kind": "collision",
                       "msg": "front %.2f similar to %s" % (score, label)})

    # Quota and gap coverage (deck target only -- gen files are partial by nature).
    if target == "deck":
        counts = Counter(c.get("domain") for c in all_cards)
        scored = sum(counts.get(d, 0) for d in EXAM_WEIGHTS)
        print("  %-3s %5s %8s %8s %6s" % ("dom", "cards", "share", "exam", "drift"))
        for dom, weight in EXAM_WEIGHTS.items():
            got = counts.get(dom, 0)
            share = (got / float(scored) * 100.0) if scored else 0.0
            drift = share - weight
            bad = abs(drift) > WEIGHT_TOLERANCE
            if bad:
                issues.append({"where": "deck", "idx": -1, "id": dom, "kind": "weight",
                               "msg": "%d cards = %.1f%% of the deck, exam weight %.1f%% (drift %+.1f pts)"
                                      % (got, share, weight, drift)})
            print("  %-3s %5d %7.1f%% %7.1f%% %+6.1f %s"
                  % (dom, got, share, weight, drift, "OUT" if bad else ""))
        ex_count = counts.get("EX", 0)
        if ex_count < EX_FLOOR:
            issues.append({"where": "deck", "idx": -1, "id": "EX", "kind": "quota",
                           "msg": "%d exam-mechanics cards, floor %d" % (ex_count, EX_FLOOR)})
        print("  %-3s %5d %7s  (floor %d)" % ("EX", ex_count, "-", EX_FLOOR))
        gap_counts = Counter()
        for c in all_cards:
            for t in c.get("tags", []):
                if t in GAP_MINIMUMS:
                    gap_counts[t] += 1
        for tag, minimum in sorted(GAP_MINIMUMS.items()):
            got = gap_counts.get(tag, 0)
            if got < minimum:
                issues.append({"where": "deck", "idx": -1, "id": tag, "kind": "gap",
                               "msg": "%d cards, minimum %d" % (got, minimum)})

    by_kind = Counter(i["kind"] for i in issues)
    if not issues:
        print("validate: PASS -- no issues")
        return 0

    print("\nvalidate: %d issues" % len(issues))
    for kind, n in by_kind.most_common():
        print("  %-10s %d" % (kind, n))
    print()
    limit = args.limit
    for issue in issues[:limit]:
        print("  [%s] %s %s: %s" % (issue["kind"], issue["where"], issue["id"], issue["msg"]))
    if len(issues) > limit:
        print("  ... %d more (use --limit)" % (len(issues) - limit))
    write_json(os.path.join(AUDIT, "validate-issues.json"), issues)
    # Duplicates and collisions are advisory; everything else fails the build.
    hard = [i for i in issues if i["kind"] not in ("duplicate", "collision")]
    return 1 if hard else 0


# ---------------------------------------------------------------- merge

def cmd_merge(args):
    if not os.path.isdir(GEN):
        print("merge: no gen directory")
        return 1
    gen_files = sorted(f for f in os.listdir(GEN) if f.endswith(".gen.json"))
    if not gen_files:
        print("merge: no *.gen.json files")
        return 1

    incoming = defaultdict(list)
    for fname in gen_files:
        cards = load_json(os.path.join(GEN, fname))
        for card in cards:
            for field in ("front", "back", "trap"):
                if isinstance(card.get(field), str):
                    card[field] = normalize_text(card[field])
            card.setdefault("tags", [])
            card.setdefault("core", False)
            card.setdefault("rev", False)
            if not card.get("trap"):
                card.pop("trap", None)
            dom = card.get("domain")
            if dom not in DOMAINS:
                warn("%s: card with bad domain %r dropped" % (fname, dom))
                continue
            incoming[dom].append(card)
        print("  %-24s %4d cards" % (fname, len(cards)))

    total_new = 0
    for dom in DOMAINS:
        path = os.path.join(DECK, "%s.cards.json" % dom.lower())
        existing = load_json(path) if os.path.exists(path) else []
        by_id = {c["id"]: c for c in existing if c.get("id")}
        used = set(by_id)
        seq = max((int(i.split("-")[1]) for i in used), default=0)

        kept = list(existing)
        existing_sh = [(c.get("id"), shingles(c.get("front", ""))) for c in existing]
        for card in incoming.get(dom, []):
            sh = shingles(card.get("front", ""))
            clash = next((cid for cid, s in existing_sh if jaccard(sh, s) >= 0.75), None)
            if clash:
                warn("%s: near-identical to existing %s -- dropped" % (dom, clash))
                continue
            seq += 1
            card["id"] = "%s-%03d" % (dom.lower(), seq)
            kept.append(card)
            existing_sh.append((card["id"], sh))
            total_new += 1
        if kept:
            write_json(path, kept)
    print("merge: %d new cards added" % total_new)
    return cmd_validate(args) if args.then_validate else 0


# ---------------------------------------------------------------- embed

def cmd_embed(args):
    if not os.path.exists(APP):
        print("embed: app HTML not found at %s" % APP)
        return 1
    cards = load_deck()
    if not cards:
        print("embed: deck is empty")
        return 1

    citemap_path = os.path.join(GEN, "mock-citemap.json")
    mockmap = load_json(citemap_path) if os.path.exists(citemap_path) else {}

    payload = {
        "meta": {
            "deckVersion": args.deck_version,
            "generated": args.generated,
            "examDate": "2026-08-18",
            "count": len(cards),
        },
        "domainNames": DOMAIN_NAMES,
        "weights": {"D1": 27, "D2": 18, "D3": 20, "D4": 20, "D5": 15},
        "schedule": SCHEDULE,
        "cards": cards,
        "mockMap": mockmap,
    }

    html = read_text(APP)
    if MARK_START not in html or MARK_END not in html:
        print("embed: marker comments missing from the app HTML")
        return 1
    head, rest = html.split(MARK_START, 1)
    _old, tail = rest.split(MARK_END, 1)
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    new_html = head + MARK_START + "\nconst DATA = " + blob + ";\n" + MARK_END + tail
    with open(APP, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(new_html)

    # Self-check: re-read, re-extract, deep compare, and confirm the offline guarantee.
    check = read_text(APP)
    got = extract_data_object(check)
    if got is None:
        print("embed: FAILED -- could not re-extract DATA")
        return 1
    if got != json.loads(blob):
        print("embed: FAILED -- round-trip mismatch")
        return 1
    problems = []
    if 'charset="utf-8"' not in check.lower() and "charset=utf-8" not in check.lower():
        problems.append("no charset meta")
    for pattern, label in ((r"https?://(?!www\.w3\.org)", "external URL"),
                           (r"\bfetch\s*\(", "fetch() call"),
                           (r"api[_-]?key", "api key reference")):
        if re.search(pattern, check, re.I):
            problems.append(label)
    if REPLACEMENT in check:
        problems.append("U+FFFD in output")
    if problems:
        print("embed: FAILED offline/encoding guarantee -- " + ", ".join(problems))
        return 1
    print("embed: %d cards, deckVersion %d, %d KB"
          % (len(cards), args.deck_version, len(new_html) // 1024))
    return 0


SCHEDULE = [
    {"date": "2026-08-10", "label": "Sun", "plan": "Deck build + first session"},
    {"date": "2026-08-11", "label": "Mon", "plan": "Drill + sit Mock 2 + import"},
    {"date": "2026-08-12", "label": "Tue", "plan": "Drill (catch-up)"},
    {"date": "2026-08-13", "label": "Wed", "plan": "Drill + sit Mock 3 + import"},
    {"date": "2026-08-14", "label": "Thu", "plan": "Drill"},
    {"date": "2026-08-15", "label": "Fri", "plan": "Drill + sit Mock 4 + import"},
    {"date": "2026-08-16", "label": "Sat", "plan": "Held-out mock as dress rehearsal"},
    {"date": "2026-08-17", "label": "Sun", "plan": "Final sweep only, no new cards"},
    {"date": "2026-08-18", "label": "Mon", "plan": "Exam"},
]


# ---------------------------------------------------------------- report

def cmd_report(_args):
    cards = load_deck()
    if not cards:
        print("report: deck is empty")
        return 1
    print("Deck: %d cards\n" % len(cards))

    by_dom = Counter(c["domain"] for c in cards)
    core = Counter(c["domain"] for c in cards if c.get("core"))
    print("%-4s %-40s %6s %6s %6s" % ("dom", "name", "cards", "quota", "core"))
    for d in DOMAINS:
        print("%-4s %-40s %6d %6d %6d"
              % (d, DOMAIN_NAMES[d][:40], by_dom.get(d, 0), QUOTA[d], core.get(d, 0)))
    print("%-4s %-40s %6d %6d %6d"
          % ("all", "", len(cards), sum(QUOTA.values()), sum(core.values())))

    print("\ntypes: " + ", ".join("%s=%d" % kv for kv in
                                  sorted(Counter(c["type"] for c in cards).items())))
    print("reversible facts: %d" % sum(1 for c in cards if c.get("rev")))

    gap = Counter()
    for c in cards:
        for t in c.get("tags", []):
            if t in GAP_MINIMUMS:
                gap[t] += 1
    print("\nknown-gap coverage")
    for tag, minimum in sorted(GAP_MINIMUMS.items()):
        got = gap.get(tag, 0)
        print("  %-6s %3d  (minimum %d) %s" % (tag, got, minimum, "" if got >= minimum else "SHORT"))

    days = 7
    print("\nprojected load: %d cards over %d intro days = %d new/day"
          % (len(cards), days, -(-len(cards) // days)))
    print("                core-only subset = %d cards, %d new/day"
          % (sum(core.values()), -(-sum(core.values()) // days)))
    return 0


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="CCA-F drill deck pipeline")
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("extract-mocks")
    sub.add_parser("cites")

    p_val = sub.add_parser("validate")
    p_val.add_argument("--target", choices=["deck", "gen"], default="deck")
    p_val.add_argument("--limit", type=int, default=40)

    p_mrg = sub.add_parser("merge")
    p_mrg.add_argument("--then-validate", action="store_true")
    p_mrg.add_argument("--target", choices=["deck", "gen"], default="deck")
    p_mrg.add_argument("--limit", type=int, default=40)

    p_emb = sub.add_parser("embed")
    p_emb.add_argument("--deck-version", type=int, default=1)
    p_emb.add_argument("--generated", default="2026-08-10")

    sub.add_parser("report")

    args = ap.parse_args()
    handlers = {
        "extract-mocks": cmd_extract_mocks,
        "cites": cmd_cites,
        "validate": cmd_validate,
        "merge": cmd_merge,
        "embed": cmd_embed,
        "report": cmd_report,
    }
    if args.cmd not in handlers:
        ap.print_help()
        return 2
    return handlers[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
