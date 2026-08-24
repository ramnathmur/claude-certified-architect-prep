# -*- coding: utf-8 -*-
"""v2 drawers: own colour zone, stepped shades per question, setup/ask split."""
import re, io, json, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from map import CARDS, FRESH

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(BASE, "_build")
CLEAN = os.path.join(BUILD, "clean.bak.html")
OUT = os.path.join(BASE, "CCA-F_Professors-Cheat-Sheet_v2.html")

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


def split_ask(stem):
    """Separate the scenario setup from the question actually being asked."""
    s = re.sub(r"\s+", " ", (stem or "").strip())
    parts = re.split(r"(?<=[.!?][\"'”’])\s+|(?<=[.!?])\s+", s)
    if len(parts) < 2:
        return "", s
    last = parts[-1]
    if last.rstrip().endswith("?"):
        # pull in a preceding short interrogative fragment too (e.g. "Which A, and why B?")
        return " ".join(parts[:-1]), last
    return " ".join(parts[:-1]), last


def pick(sections, limit=3):
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
    out, used = [], set()
    for q in pool:
        if len(out) >= limit:
            break
        if q["exam"] in used and len(pool) > limit:
            continue
        used.add(q["exam"])
        out.append(q)
    for q in pool:
        if len(out) >= limit:
            break
        if q not in out:
            out.append(q)
    return out, len([q for q in pool if q["done"]]), len(pool), missed


def qblock(n, tag, badge, stem, answer, fresh=False):
    setup, ask = split_ask(stem)
    body = ""
    if setup:
        body += '<p class="q-setup">%s</p>' % esc(setup)
    body += '<p class="q-ask">%s</p>' % esc(ask)
    return ('<div class="dq dq%d"><div class="dqh"><span class="qnum">%d</span>'
            '<span class="qtag%s">%s</span>%s</div>%s'
            '<div class="qans"><span class="qans-k">Answer</span><span class="qans-t">%s</span></div></div>'
            % (min(n, 4), n, " qtagf" if fresh else "", tag, badge, body, esc(answer)))


def drawer(title, sections, forms):
    qs, ndone, ntotal, missed = pick(sections)
    fresh = FRESH.get(title, [])
    if not qs and not fresh:
        return None
    shown = len(qs) + len(fresh)
    bits = ["%d shown" % shown]
    if ntotal:
        bits.append("%d in your exam bank" % ntotal)
        if ndone:
            bits.append("%d already sat" % ndone)
    if fresh:
        bits.append("%d newly written" % len(fresh))
    nmiss = len(missed)
    missbadge = ('<span class="dmiss">missed %s</span>'
                 % ("once" if nmiss == 1 else "%d&times;" % nmiss)) if nmiss else ""
    h = ['<details class="drw"><summary><span class="dlab">How this gets asked</span>'
         '<span class="dmeta">%s</span>%s</summary><div class="dbody">' % (" &middot; ".join(bits), missbadge)]
    if forms:
        h.append('<p class="dforms">%s</p>' % forms)
    n = 0
    for q in qs:
        n += 1
        badge = ('<span class="qmiss">you got this wrong</span>' if q.get("_miss")
                 else ("" if q["done"] else '<span class="qnew">not sat yet</span>'))
        h.append(qblock(n, "Exam %s &middot; Q%s" % (q["exam"], q["g"]), badge,
                        q["stem"], trim(q["why"])))
    for stem, ans in fresh:
        n += 1
        h.append(qblock(n, "Written for you", "", stem, ans, fresh=True))
    h.append("</div></details>")
    return "\n" + "".join(h) + "\n"


def card_spans(s):
    for m in re.finditer(r'<div class="card"[^>]*>', s):
        i, depth = m.end(), 1
        while depth:
            nxt = re.search(r"<div\b|</div>", s[i:])
            i += nxt.end()
            depth += 1 if nxt.group(0) != "</div>" else -1
        yield m.start(), m.end(), i - len("</div>")


src = io.open(CLEAN, encoding="utf-8").read()
edits, hit = [], 0
for start, open_end, close_at in card_spans(src):
    body = src[open_end:close_at]
    m = re.search(r"<h3[^>]*>(.*?)</h3>", body, re.S)
    if not m:
        continue
    title = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    key = next((k for k in CARDS if html.unescape(re.sub(r"<[^>]+>", "", k)).strip() == title), None)
    if key is None:
        continue
    d = drawer(key, *CARDS[key])
    if d:
        edits.append((close_at, d))
        hit += 1
for pos, txt in sorted(edits, reverse=True):
    src = src[:pos] + txt + src[pos:]

CSS = r"""
/* ---------- base palette also responds to an explicit theme attribute,
     so the toggle and the OS preference cannot disagree ---------- */
:root[data-theme="light"]{
  --paper:#fbf6ec; --paper2:#f4ecdd; --ink:#241f1a; --ink2:#5b5147;
  --rule:#ddd0ba; --accent:#8c3a1f; --accent2:#1f5c4a; --chalk:#2f3b3a;
  --hl:#f6e07a; --card:#fffdf8; --shadow:rgba(80,60,30,.10);
}
:root[data-theme="dark"]{
  --paper:#1a1815; --paper2:#221f1b; --ink:#eee6d8; --ink2:#b3a897;
  --rule:#3b352d; --accent:#e08a63; --accent2:#6dc0a4; --chalk:#cfe3dc;
  --hl:#6b5a1f; --card:#221f1b; --shadow:rgba(0,0,0,.35);
}

/* ---------- question drawers: their own colour zone ---------- */
:root{
  --ex:#3f4a7a;            /* the exam's colour - cool indigo against the warm page */
  --ex-ink:#2b3358;
  --ex-1:#e7e9f4; --ex-2:#eef0f8; --ex-3:#f5f6fb;   /* stepped question surfaces */
  --ex-b1:#5560a0; --ex-b2:#868fc0; --ex-b3:#b3b9d8; /* matching edge bars */
  --ex-zone:#f4f5fb;
  --ans:#f7f2e4;
}
@media (prefers-color-scheme: dark){
  :root{
    --ex:#a9b2e0; --ex-ink:#c7cdec;
    --ex-1:#272c47; --ex-2:#232739; --ex-3:#202332;
    --ex-b1:#7b86c8; --ex-b2:#5b649b; --ex-b3:#434a72;
    --ex-zone:#1e2130; --ans:#2a2620;
  }
}
:root[data-theme="light"]{
  --ex:#3f4a7a; --ex-ink:#2b3358; --ex-1:#e7e9f4; --ex-2:#eef0f8; --ex-3:#f5f6fb;
  --ex-b1:#5560a0; --ex-b2:#868fc0; --ex-b3:#b3b9d8; --ex-zone:#f4f5fb; --ans:#f7f2e4;
}
:root[data-theme="dark"]{
  --ex:#a9b2e0; --ex-ink:#c7cdec; --ex-1:#272c47; --ex-2:#232739; --ex-3:#202332;
  --ex-b1:#7b86c8; --ex-b2:#5b649b; --ex-b3:#434a72; --ex-zone:#1e2130; --ans:#2a2620;
}

.drw{margin:14px -18px -14px;border-top:1px solid var(--rule)}
.drw>summary{
  cursor:pointer;list-style:none;display:flex;align-items:center;flex-wrap:wrap;gap:9px;
  font-size:.78rem;color:var(--ex);padding:9px 18px;user-select:none;
  background-color:#f4f5fb;transition:background-color .15s;
}
.drw>summary::-webkit-details-marker{display:none}
.drw>summary::before{
  content:"";width:0;height:0;border-left:5px solid var(--ex);
  border-top:4px solid transparent;border-bottom:4px solid transparent;
  transition:transform .18s ease;flex:none;
}
.drw[open]>summary::before{transform:rotate(90deg)}
.drw>summary:hover{background-color:#e7e9f4}
.drw[open]>summary{border-bottom:1px solid var(--ex-b3)}
.dlab{font-variant:small-caps;letter-spacing:.09em;font-weight:700;color:var(--ex)}
.dmeta{font-size:.94em;font-variant-numeric:tabular-nums;opacity:.78}
.dmiss{background:var(--accent);color:#fff;border-radius:11px;padding:1px 9px;
  font-size:.88em;font-variant:small-caps;letter-spacing:.06em;font-weight:600}

/* The summary bar's surface is stated literally per theme rather than through a
   custom property: it is the one element whose background must match the body it
   caps, and literal values remove any dependence on var() resolution order. */
@media (prefers-color-scheme: dark){
  .drw>summary{background-color:#1e2130}
  .drw>summary:hover{background-color:#272c47}
}
:root[data-theme="light"] .drw>summary{background-color:#f4f5fb}
:root[data-theme="light"] .drw>summary:hover{background-color:#e7e9f4}
:root[data-theme="dark"] .drw>summary{background-color:#1e2130}
:root[data-theme="dark"] .drw>summary:hover{background-color:#272c47}

.dbody{background-color:var(--ex-zone);padding:15px 18px 17px}
.dforms{
  margin:0 0 15px;font-size:.9rem;color:var(--ex-ink);line-height:1.55;
  padding-left:13px;border-left:3px solid var(--ex-b2);
}
.dforms em{font-style:normal;font-weight:700}
.dforms b{font-weight:700}

/* one stepped surface per question, so three of them never read as one wall */
.dq{border-radius:5px;padding:11px 14px 3px;margin:0 0 11px;border-left:4px solid}
.dq:last-child{margin-bottom:0}
.dq1{background:var(--ex-1);border-left-color:var(--ex-b1)}
.dq2{background:var(--ex-2);border-left-color:var(--ex-b2)}
.dq3{background:var(--ex-3);border-left-color:var(--ex-b3)}
.dq4{background:var(--ex-3);border-left-color:var(--ex-b3)}

.dqh{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:7px}
.qnum{
  flex:none;width:19px;height:19px;border-radius:50%;background:var(--ex);color:var(--paper);
  font-size:.68rem;font-weight:700;display:flex;align-items:center;justify-content:center;
  font-variant-numeric:tabular-nums;
}
.qtag{font-size:.69rem;font-variant:small-caps;letter-spacing:.09em;color:var(--ex-ink);
  border:1px solid var(--ex-b3);border-radius:10px;padding:0 8px;background:transparent;font-weight:600}
.qtagf{border-style:dashed}
.qmiss{font-size:.69rem;font-variant:small-caps;letter-spacing:.06em;color:var(--accent);font-weight:700}
.qnew{font-size:.69rem;font-variant:small-caps;letter-spacing:.06em;color:var(--ex-ink);opacity:.6}

/* the setup recedes, the actual question steps forward */
.q-setup{margin:0 0 6px;font-size:.88rem;line-height:1.55;color:var(--ex-ink);opacity:.72;max-width:74ch}
.q-ask{margin:0 0 10px;font-size:.95rem;line-height:1.5;font-weight:600;color:var(--ex-ink);max-width:74ch}

.qans{
  display:flex;gap:9px;align-items:baseline;background:var(--ans);
  border-radius:4px;padding:8px 11px;margin:0 -4px 11px;
}
.qans-k{
  flex:none;font-size:.66rem;font-variant:small-caps;letter-spacing:.09em;font-weight:700;
  color:var(--accent2);border-right:1px solid var(--rule);padding-right:9px;
}
.qans-t{font-size:.87rem;line-height:1.55;color:var(--ink2)}
.dq code{background:rgba(0,0,0,.05);border-color:var(--ex-b3)}
@media (prefers-color-scheme: dark){.dq code{background:rgba(255,255,255,.07)}}
@media(max-width:560px){
  .drw{margin-left:-14px;margin-right:-14px}
  .qans{flex-direction:column;gap:3px}
  .qans-k{border-right:none;padding-right:0}
}
@media print{.drw>summary{display:none}.dbody{display:block!important}}
"""
src = src.replace("\n/* two-column look-alike cards */", CSS + "\n/* two-column look-alike cards */", 1)
src = src.replace("<title>", "<title>", 1)
io.open(OUT, "w", encoding="utf-8").write(src)
print("drawers injected: %d -> %s (%.0f KB)" % (hit, os.path.basename(OUT), os.path.getsize(OUT) / 1024.0))
