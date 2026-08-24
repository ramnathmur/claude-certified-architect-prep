"""Lint items_d*.py against CARD-SPEC.md. Usage: python lint_items.py [d1 d2 ...]  (default: all present)
Exit 1 on any ERROR. WARNs are printed but do not fail.
"""
import importlib.util
import os
import re
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    p = os.path.join(HERE, name + ".py")
    if not os.path.exists(p):
        return None
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


inv = load("inventory")
FIELDS = ["id", "title", "concept", "tested", "remember", "analogy", "svg", "alt"]
ALLOWED_EL = {"path", "rect", "circle", "ellipse", "line", "polyline", "polygon", "g", "text"}
ALLOWED_ATTR = {"d", "x", "y", "width", "height", "r", "rx", "ry", "cx", "cy", "x1", "y1", "x2", "y2", "points",
                "class", "transform", "opacity", "text-anchor", "font-size"}
ALLOWED_CLASS = {"tint", "acc", "accfill", "paper", "thin", "dash", "no", "lbl"}
PERSONAL = re.compile(r"\b(you missed|your score|your weak|mock exam|exam \d+|ram\b|your last|you got|scored)\b", re.I)
BANNED = [(re.compile(r"!"), "exclamation mark"),
          (re.compile(r"\b(simply|the key insight|most people (think|assume)|you might think|contrary to)\b", re.I), "banned phrase"),
          (re.compile(r"\bThat is not [^.]+\. That is\b"), "diagnose-negate-reveal tricolon"),
          (re.compile(r"<[a-z]+[ >]", re.I), "raw HTML tag in prose")]


def sentences(s):
    s = re.sub(r"`[^`]*`", "X", s)
    s = re.sub(r"\b(e\.g|i\.e|vs|etc)\.", "X", s)
    return [p for p in re.split(r"(?<=[.!?])\s+(?=[A-Z\"(])", s.strip()) if p]


def words(s):
    return len(re.findall(r"\S+", s))


def lint(dom, items):
    errs, warns = [], []
    if dom.lower() in inv.PARTS:
        want = inv.part_ids(dom.lower())
    else:
        want = [c["id"] for c in inv.CARDS if c["id"].startswith(dom.upper() + "-")]
    got = [it.get("id") for it in items]
    if got != want:
        missing = [w for w in want if w not in got]; extra = [g for g in got if g not in want]
        if missing: errs.append(f"missing ids: {missing}")
        if extra: errs.append(f"unexpected ids: {extra}")
        if sorted(got) == sorted(want): warns.append("ids present but out of inventory order")
    for it in items:
        cid = it.get("id", "?")
        for f in FIELDS:
            if f not in it or not str(it[f]).strip():
                errs.append(f"{cid}: missing field {f}")
        if any(f not in it for f in FIELDS):
            continue
        if len(sentences(it["concept"])) != 1:
            errs.append(f"{cid}: concept must be ONE sentence (got {len(sentences(it['concept']))})")
        if words(it["concept"]) > 34: warns.append(f"{cid}: concept {words(it['concept'])} words (>32)")
        if words(it["remember"]) > 34: warns.append(f"{cid}: remember {words(it['remember'])} words (>30)")
        if words(it["title"]) > 10: warns.append(f"{cid}: title {words(it['title'])} words (>9)")
        n_an = len(sentences(it["analogy"]))
        if n_an < 2 or n_an > 4: warns.append(f"{cid}: analogy {n_an} sentences (want 2-3)")
        n_te = len(sentences(it["tested"]))
        if n_te > 4: warns.append(f"{cid}: tested {n_te} sentences (want 1-3)")
        if words(it["alt"]) > 14: warns.append(f"{cid}: alt {words(it['alt'])} words (>12)")
        for f in ["title", "concept", "tested", "remember", "analogy", "alt"]:
            t = it[f]
            if PERSONAL.search(t): errs.append(f"{cid}: {f} references a learner/score: {PERSONAL.search(t).group(0)!r}")
            for rx, why in BANNED:
                if rx.search(t): errs.append(f"{cid}: {f}: {why}: {rx.search(t).group(0)!r}")
        # svg
        svg = it["svg"]
        if re.search(r"#[0-9a-fA-F]{3,8}\b|rgb\(|url\(|style=|fill=|stroke=|<image|<script|<use|<defs|\bid=", svg):
            errs.append(f"{cid}: svg contains a forbidden token (colour/style/fill/stroke attr, image, url, script, use, defs, id)")
        try:
            root = ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg">{svg}</svg>')
        except ET.ParseError as e:
            errs.append(f"{cid}: svg does not parse: {e}"); continue
        for el in root.iter():
            tag = el.tag.split("}")[-1]
            if tag == "svg": continue
            if tag not in ALLOWED_EL: errs.append(f"{cid}: svg element <{tag}> not allowed")
            for a in el.attrib:
                if a not in ALLOWED_ATTR: errs.append(f"{cid}: svg attribute {a!r} on <{tag}> not allowed")
            cls = el.attrib.get("class", "")
            for c in cls.split():
                if c not in ALLOWED_CLASS: errs.append(f"{cid}: svg class {c!r} not allowed")
            if tag == "text":
                if "lbl" not in cls.split(): errs.append(f"{cid}: <text> must have class lbl")
                fs = el.attrib.get("font-size")
                if fs not in (None, "11", "12"): errs.append(f"{cid}: <text> font-size {fs} not allowed")
                if len((el.text or "").strip()) > 5: errs.append(f"{cid}: <text> label longer than 5 chars: {el.text!r}")
            op = el.attrib.get("opacity")
            if op is not None:
                try:
                    if not (0.35 <= float(op) <= 1): errs.append(f"{cid}: opacity {op} outside 0.35-1")
                except ValueError: errs.append(f"{cid}: bad opacity {op}")
        n_shapes = sum(1 for el in root.iter() if el.tag.split("}")[-1] in ALLOWED_EL - {"g", "text"})
        if n_shapes < 3: warns.append(f"{cid}: svg has only {n_shapes} shapes — likely too sparse")
        if n_shapes > 40: warns.append(f"{cid}: svg has {n_shapes} shapes — likely too busy")
    return errs, warns


if __name__ == "__main__":
    doms = sys.argv[1:] or [f"d{i}" for i in range(1, 6)]
    total_err = 0
    for d in doms:
        m = load(f"items_{d}")
        if m is None:
            print(f"[{d}] items_{d}.py not present"); continue
        errs, warns = lint(d, m.ITEMS)
        print(f"[{d}] cards={len(m.ITEMS)} errors={len(errs)} warnings={len(warns)}")
        for e in errs: print("  ERROR", e)
        for w in warns: print("  warn ", w)
        total_err += len(errs)
    sys.exit(1 if total_err else 0)
