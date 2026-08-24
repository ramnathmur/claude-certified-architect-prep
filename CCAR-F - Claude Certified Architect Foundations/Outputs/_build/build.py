# -*- coding: utf-8 -*-
"""Inject 'How this gets asked' drawers into the cheat sheet, sourced from the mock-exam bank."""
import re, io, json, os, sys, html, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from map import CARDS, FRESH

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(BASE, "_build")
SRC = os.path.join(BASE, "CCA-F_Professors-Cheat-Sheet_v1.html")

bank = json.load(io.open(os.path.join(BUILD, "bank.json"), encoding="utf-8"))
QS, IDX = bank["questions"], bank["index"]
MISS = json.load(io.open(os.path.join(BUILD, "misses.json"), encoding="utf-8"))


def esc(t):
    t = html.escape(t or "", quote=False)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", t)


def trim(t, n=250):
    t = re.sub(r"\s+", " ", (t or "").strip())
    if len(t) <= n:
        return t
    cut = t[:n]
    p = max(cut.rfind(". "), cut.rfind("; "))
    return (cut[: p + 1] if p > 90 else cut.rstrip() + "…")


def pick(sections, limit=3):
    """Best questions for a card: completed exams first, spread across exams."""
    seen, pool = set(), []
    for sec in sections:
        for i in IDX.get(sec, []):
            if i in seen:
                continue
            seen.add(i)
            pool.append(QS[i])
    pool = [q for q in pool if 110 <= len(q["stem"]) <= 620]
    missed = set()
    for sec in sections:
        for m in MISS.get(sec, []):
            if m.get("exam") and m.get("q"):
                missed.add((m["exam"], int(m["q"])))
    for q in pool:
        q["_miss"] = (q["exam"], q["g"]) in missed
    pool.sort(key=lambda q: (not q["_miss"], not q["done"], -len(q["stem"])))
    out, used_exams = [], set()
    for q in pool:
        if len(out) >= limit:
            break
        if q["exam"] in used_exams and len(pool) > limit:
            continue
        used_exams.add(q["exam"])
        out.append(q)
    for q in pool:                      # top up if the exam-spread filter was too strict
        if len(out) >= limit:
            break
        if q not in out:
            out.append(q)
    return out, len([q for q in pool if q["done"]]), len(pool), missed


def drawer(title, sections, forms):
    qs, ndone, ntotal, missed = pick(sections)
    fresh = FRESH.get(title, [])
    if not qs and not fresh:
        return None
    nmiss = len(missed)
    shown = len(qs) + len(fresh)
    bits = ["%d shown" % shown]
    if ntotal:
        bits.append("%d in your exam bank" % ntotal)
        if ndone:
            bits.append("%d already sat" % ndone)
    if fresh:
        bits.append("%d newly written" % len(fresh))
    label = "How this gets asked"
    meta = " &middot; ".join(bits)
    missbadge = ('<span class="dmiss">missed %s</span>'
                 % ("once" if nmiss == 1 else "%d×" % nmiss)) if nmiss else ""

    h = ['<details class="drw"><summary><span class="dlab">%s</span>'
         '<span class="dmeta">%s</span>%s</summary><div class="dbody">' % (label, meta, missbadge)]
    if forms:
        h.append('<p class="dforms">%s</p>' % forms)
    for q in qs:
        tag = "Exam %s &middot; Q%s" % (q["exam"], q["g"])
        badge = '<span class="qmiss">you got this wrong</span>' if q.get("_miss") else (
            "" if q["done"] else '<span class="qnew">not sat yet</span>')
        h.append('<div class="dq"><div class="dqh"><span class="qtag">%s</span>%s</div>'
                 '<p class="qstem">%s</p><p class="qans"><b>Answer</b> &middot; %s</p></div>'
                 % (tag, badge, esc(q["stem"]), esc(trim(q["why"]))))
    for stem, ans in fresh:
        h.append('<div class="dq"><div class="dqh"><span class="qtag qtagf">Written for you</span></div>'
                 '<p class="qstem">%s</p><p class="qans"><b>Answer</b> &middot; %s</p></div>'
                 % (esc(stem), esc(ans)))
    h.append("</div></details>")
    return "\n" + "".join(h) + "\n"


def card_spans(s):
    """Yield (start, end_of_open_tag, close_index) for every .card div."""
    for m in re.finditer(r'<div class="card"[^>]*>', s):
        i, depth = m.end(), 1
        while depth:
            nxt = re.search(r"<div\b|</div>", s[i:])
            if not nxt:
                raise SystemExit("unbalanced div near %d" % m.start())
            i += nxt.end()
            depth += 1 if nxt.group(0) != "</div>" else -1
        yield m.start(), m.end(), i - len("</div>")


src = io.open(SRC, encoding="utf-8").read()
if 'class="drw"' in src:
    raise SystemExit("drawers already present - rebuild from a clean file")

spans = list(card_spans(src))
edits, hit, missmap = [], 0, []
for start, open_end, close_at in spans:
    body = src[open_end:close_at]
    m = re.search(r"<h3[^>]*>(.*?)</h3>", body, re.S)
    if not m:
        continue
    title = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    key = next((k for k in CARDS if html.unescape(re.sub(r"<[^>]+>", "", k)).strip() == title), None)
    if key is None:
        continue
    secs, forms = CARDS[key]
    d = drawer(key, secs, forms)
    if d:
        edits.append((close_at, d))
        hit += 1
        missmap.append(title)

for pos, txt in sorted(edits, reverse=True):
    src = src[:pos] + txt + src[pos:]

CSS = """
/* ---------- question drawers ---------- */
.drw{margin:12px -6px -4px;border-top:1px dotted var(--rule);padding-top:9px}
.drw>summary{
  cursor:pointer;list-style:none;display:flex;align-items:center;flex-wrap:wrap;gap:8px;
  font-size:.78rem;color:var(--ink2);padding:3px 6px;border-radius:4px;user-select:none;
}
.drw>summary::-webkit-details-marker{display:none}
.drw>summary::before{content:"\\25B8";font-size:.7em;color:var(--accent);transition:transform .15s}
.drw[open]>summary::before{transform:rotate(90deg)}
.drw>summary:hover{background:var(--paper2);color:var(--ink)}
.dlab{font-variant:small-caps;letter-spacing:.07em;font-weight:600;color:var(--accent2)}
.dmeta{font-size:.94em;font-variant-numeric:tabular-nums}
.dmiss{background:var(--accent);color:var(--paper);border-radius:10px;padding:0 8px;
  font-size:.9em;font-variant:small-caps;letter-spacing:.05em}
.dbody{padding:8px 6px 2px;border-left:2px solid var(--rule);margin:6px 0 0 8px}
.dforms{margin:0 0 12px;font-size:.92rem;color:var(--ink2);font-style:italic}
.dforms em{font-style:normal;color:var(--ink);font-weight:600}
.dq{margin:0 0 13px;padding-left:10px;border-left:2px solid transparent}
.dq:last-child{margin-bottom:2px}
.dqh{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:4px}
.qtag{font-size:.7rem;font-variant:small-caps;letter-spacing:.08em;color:var(--ink2);
  border:1px solid var(--rule);border-radius:10px;padding:0 8px;background:var(--paper2)}
.qtagf{border-style:dashed;color:var(--accent2)}
.qmiss{font-size:.7rem;font-variant:small-caps;letter-spacing:.06em;color:var(--accent);font-weight:600}
.qnew{font-size:.7rem;font-variant:small-caps;letter-spacing:.06em;color:var(--ink2);opacity:.75}
.qstem{margin:0 0 5px;font-size:.93rem}
.qans{margin:0;font-size:.88rem;color:var(--ink2)}
.qans b{font-variant:small-caps;letter-spacing:.06em;color:var(--accent2)}
@media print{.drw{display:block}.drw>summary{display:none}.dbody{display:block!important}}
"""
src = src.replace("\n/* two-column look-alike cards */", CSS + "\n/* two-column look-alike cards */", 1)

io.open(SRC, "w", encoding="utf-8").write(src)
print("cards seen: %d | drawers injected: %d | mapping entries: %d" % (len(spans), hit, len(CARDS)))
unmatched = [k for k in CARDS if html.unescape(re.sub(r"<[^>]+>", "", k)).strip() not in missmap]
print("mapping keys that matched no card:", unmatched)
