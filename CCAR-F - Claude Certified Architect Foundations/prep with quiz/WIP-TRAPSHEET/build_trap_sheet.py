"""Build the CCA-F Trap Sheet HTML from its markdown source.

One source of truth: Outputs/CCA-F_Trap-Sheet-Plan_v2.md
Two outputs:
  Outputs/CCA-F_Trap-Sheet_v1.html           generic, distributable (no personal data)
  Outputs/CCA-F_Trap-Sheet-Personal_v1.html  same + personal miss badges and ledger

Usage:  python build_trap_sheet.py
The generic build runs a hard gate: zero U+2691 flags and zero "Exam <n>" strings
must survive in the emitted HTML, or the script exits non-zero without writing.
"""

import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.abspath(os.path.join(HERE, "..", "..", "Outputs"))
SRC = os.path.join(OUTDIR, "CCA-F_Trap-Sheet-Plan_v2.md")
FLAG = "⚑"

# ---------------------------------------------------------------- personal ---
# Exact-string rewrites applied ONLY for the generic build. Each entry removes a
# personal reference while keeping the corpus-grounded substance of the point.
GENERIC_REWRITES = [
    # legend
    ("`[REVERSE]` the mirror-image ask · `" + FLAG + "` you have missed this in a "
     "scored paper (exam numbers on the card) · `§` jump-pointer",
     "`[REVERSE]` the mirror-image ask · `§` jump-pointer"),
    # mold table tells
    ("| 8 | DISCARD " + FLAG + " | Throw away a working mechanism (hook, session, tool) "
     "when a narrow adjustment fixes the side-effect | Exam 14 Q19/Q54 |",
     "| 8 | DISCARD | Throw away a working mechanism (hook, session, tool) when a "
     "narrow adjustment fixes the side-effect | The stem describes a side-effect, "
     "not a broken mechanism |"),
    ("| 9 | OVERSPEC " + FLAG + " | Force a *specific* mechanism when the requirement "
     "only needs *a* mechanism — `tool_choice: tool` where `any`/`auto` is right; "
     "forced on every turn | Exam 19 Q23, Exam 20 Q48 |",
     "| 9 | OVERSPEC | Force a *specific* mechanism when the requirement only needs "
     "*a* mechanism — `tool_choice: tool` where `any`/`auto` is right; forced on "
     "every turn | Read what the stem actually guarantees |"),
    ("**The ten distractor molds** (7 from the practice-test explanations, 3 from "
     "your own miss record):",
     "**The ten distractor molds** (7 from the practice-test explanations, 3 from "
     "patterns this material has seen catch candidates):"),
    # card titles + meta lines
    ("### D2-21 · Bundling vs composite tools " + FLAG + " five-paper miss",
     "### D2-21 · Bundling vs composite tools"),
    ("§2.8 · " + FLAG + " missed on Exams 5, 8, 10, 11, 14 — the oldest open trap",
     "§2.8"),
    ("§2.2 · §4.1 · " + FLAG + " Exam 19 Q53", "§2.2 · §4.1"),
    ("§3.7.4 · " + FLAG + " Exam 17; Exam 20 Q58", "§3.7.4"),
    ("### D4-21 · Batch requests can define tools; they cannot pause mid-request " + FLAG,
     "### D4-21 · Batch requests can define tools; they cannot pause mid-request"),
    ("§4.11 · " + FLAG + " Exam 20 Q42 + Q55", "§4.11"),
    # inline bullets
    ("- ✗ Discard a resumable session when a targeted note would do " + FLAG +
     " `[DISCARD — Exam 14 Q19/Q54]`.",
     "- ✗ Discard a resumable session when a targeted note would do `[DISCARD]`."),
    ("- ✗ Few-shot before descriptions are fixed " + FLAG +
     " `[wrong lever first — Exam 19 Q53]`.",
     "- ✗ Few-shot before descriptions are fixed `[wrong lever first]`."),
    ("- ✗ Forcing one named tool " + FLAG + " `[OVERSPEC — Exam 19 Q23, Exam 20 Q48]`.",
     "- ✗ Forcing one named tool `[OVERSPEC]`."),
    ("- ✗ Remove a hook because one consumer lost a field " + FLAG +
     " `[DISCARD — Exam 14 Q19/Q54; widen the field list]`.",
     "- ✗ Remove a hook because one consumer lost a field `[DISCARD — widen "
     "the field list instead]`."),
    ("- ✗ Examples first, descriptions untouched " + FLAG + " `[wrong lever]`.",
     "- ✗ Examples first, descriptions untouched `[wrong lever]`."),
    ("- ✗ " + FLAG + " The `rules/` reflex — `rules/` as the answer to \"where should "
     "this workflow live\" or \"what supplies the missing context\" (six instances: "
     "Exams 12, 13, 17, 14×2).",
     "- ✗ The `rules/` reflex — `rules/` as the answer to \"where should this "
     "workflow live\" or \"what supplies the missing context\"; the glob triggers on "
     "paths and nothing else."),
    ("- ✗ Split workflow content into `rules/` " + FLAG + " `[path-scoped, not workflow-scoped]`.",
     "- ✗ Split workflow content into `rules/` `[path-scoped, not workflow-scoped]`."),
    ("- ✗ \"Always one issue per message\" " + FLAG + " `[wrong axis]`.",
     "- ✗ \"Always one issue per message\" `[wrong axis]`."),
    ("- ✗ \"Always everything in one message\" " + FLAG + " `[wrong axis]`.",
     "- ✗ \"Always everything in one message\" `[wrong axis]`."),
    ("- ✗ Abandon a working session for a fresh one when a targeted note would do "
     + FLAG + " `[DISCARD]`.",
     "- ✗ Abandon a working session for a fresh one when a targeted note would do "
     "`[DISCARD]`."),
    ("- ✗ Examples when thin descriptions are the root cause " + FLAG + " `[D2-28]`.",
     "- ✗ Examples when thin descriptions are the root cause `[D2-28]`."),
    ("- [REVERSE " + FLAG + "] Prevention at the source (schema) beats repair after "
     "(validate + retry) — Exam 17/19 prevention-vs-repair.",
     "- [REVERSE] Prevention at the source (schema) beats repair after (validate + retry)."),
    ("- [WHICH " + FLAG + "] Which decision belongs where — schema (shape, requiredness, "
     "enums, nullability) · prompt (mapping messy input) · code (business rules) "
     "— Exam 19 Q35 select-2 schema-scope.",
     "- [WHICH] Which decision belongs where — schema (shape, requiredness, enums, "
     "nullability) · prompt (mapping messy input) · code (business rules). Often a "
     "select-2 item."),
    ("- ✗ \"Batches can't use tools\" " + FLAG + " `[outdated]`.",
     "- ✗ \"Batches can't use tools\" `[outdated]`."),
    ("- [REVERSE " + FLAG + "] Hook deployed, a downstream consumer lost a needed field "
     "→ widen the field list, don't remove the hook.",
     "- [REVERSE] Hook deployed, a downstream consumer lost a needed field → widen "
     "the field list, don't remove the hook."),
    ("bigger model `[BIGGER-CONTEXT]`; remove the hook " + FLAG + " `[DISCARD]`.",
     "bigger model `[BIGGER-CONTEXT]`; remove the hook `[DISCARD]`."),
]

# Sections dropped from the generic build entirely.
GENERIC_DROP_PAGES = {"ledger"}

# ------------------------------------------------------------------- parse ---
PAGES = [
    ("start",     "## Start page",                 "Start",       "How to read this"),
    ("toolkit",   "## The setter's toolkit",       "Toolkit",     "The setter's toolkit"),
    ("d1",        "## Domain 1 ·",            "D1",          "Agentic Architecture &amp; Orchestration · 27%"),
    ("d2",        "## Domain 2 ·",            "D2",          "Tool Design &amp; MCP Integration · 18%"),
    ("d3",        "## Domain 3 ·",            "D3",          "Claude Code Configuration &amp; Workflows · 20%"),
    ("d4",        "## Domain 4 ·",            "D4",          "Prompt Engineering &amp; Structured Output · 20%"),
    ("d5",        "## Domain 5 ·",            "D5",          "Context Management &amp; Reliability · 15%"),
    ("lookalikes","## Look-alikes (page)",         "Look-alikes", "The 29 look-alike pairs"),
    ("exam-docs", "## Exam ≠ docs (page)",    "Exam≠docs", "Where current docs and the guide differ"),
    ("ledger",    "## Your ledger (page)",         "Ledger",      "Your own miss record, ranked"),
]
STOP_AT = "## Document structure"


def split_sections(md):
    """Return {page_key: [lines]} for the pages defined above."""
    lines = md.splitlines()
    starts = []
    for i, line in enumerate(lines):
        for key, prefix, _, _ in PAGES:
            if line.startswith(prefix):
                starts.append((i, key))
    stop = next((i for i, l in enumerate(lines) if l.startswith(STOP_AT)), len(lines))
    starts.append((stop, None))
    out = {}
    for (i, key), (j, _) in zip(starts, starts[1:]):
        if key:
            out[key] = lines[i + 1:j]
    return out


# ------------------------------------------------------------------ inline ---
CARD_ID = re.compile(r"\b(D[1-5]-\d{2})\b")


def inline(text, link_cards=True):
    """Markdown inline -> HTML. Code spans are protected from other rules."""
    spans = []

    def stash(m):
        spans.append(m.group(1))
        return "\x00%d\x00" % (len(spans) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    if link_cards:
        text = CARD_ID.sub(lambda m: '<a class="xref" href="#%s">%s</a>'
                           % (m.group(1).lower(), m.group(1)), text)
    # form tags [FIX] [HOW] ... and mold tags inside brackets
    text = re.sub(r"\[(FIX|HOW|CAUSE|WHICH|WHERE|REVERSE|LOOKALIKE)([^\]]*)\]",
                  lambda m: '<span class="form">%s%s</span>' % (m.group(1), m.group(2)),
                  text)

    def unstash(m):
        code = html.escape(spans[int(m.group(1))], quote=False)
        code = CARD_ID.sub(lambda c: c.group(1), code)
        if code.startswith("[") and code.endswith("]"):
            return '<span class="mold">%s</span>' % code[1:-1]
        return "<code>%s</code>" % code
    return re.sub(r"\x00(\d+)\x00", unstash, text)


def render_table(rows):
    head, body = rows[0], rows[2:]
    cells = [c.strip() for c in head.strip().strip("|").split("|")]
    out = ['<div class="tablewrap"><table><thead><tr>']
    out += ["<th>%s</th>" % inline(c) for c in cells]
    out.append("</tr></thead><tbody>")
    for r in body:
        cs = [c.strip() for c in r.strip().strip("|").split("|")]
        out.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in cs) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render_prose(lines):
    """Prose page: paragraphs, tables, and '- ' bullet lists."""
    out, para, bullets, table = [], [], [], []

    def flush():
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            para.clear()
        if bullets:
            out.append("<ul class='plain'>%s</ul>"
                       % "".join("<li>%s</li>" % inline(b) for b in bullets))
            bullets.clear()
        if table:
            out.append(render_table(table))
            table.clear()

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("|"):
            if para or bullets:
                flush()
            table.append(line)
            continue
        if table:
            flush()
        if not line.strip():
            flush()
            continue
        if line.startswith("- "):
            if para:
                flush()
            bullets.append(line[2:])
            continue
        if bullets:
            flush()
        para.append(line.strip())
    flush()
    return "".join(out)


def render_cards(lines):
    """Domain page: '### Dn-NN · Title' cards with meta / Rule / Asked / Traps."""
    cards, cur = [], None
    for raw in lines:
        line = raw.rstrip()
        if line.startswith("### "):
            if cur:
                cards.append(cur)
            title = line[4:]
            cid, _, name = title.partition(" · ")
            cur = {"id": cid.strip(), "title": name.strip(), "meta": "",
                   "rule": "", "asked": [], "traps": [], "mode": None}
            continue
        if cur is None or not line.strip():
            continue
        if not cur["meta"] and not cur["rule"] and (
                line.startswith("§") or line.startswith("KD ") or line.startswith(FLAG)):
            cur["meta"] = line.strip()
            continue
        if line.startswith("**Rule.**"):
            cur["rule"] = line[len("**Rule.**"):].strip()
            continue
        if line.startswith("**Asked**"):
            cur["mode"] = "asked"
            continue
        if line.startswith("**Traps**"):
            cur["mode"] = "traps"
            continue
        if line.startswith("- ") and cur["mode"]:
            cur[cur["mode"]].append(line[2:].strip())
            continue
        if cur["mode"]:
            cur[cur["mode"]].append(line.strip())
    if cur:
        cards.append(cur)

    index = "".join('<a href="#%s">%s <span>%s</span></a>'
                    % (c["id"].lower(), c["id"], inline(c["title"], link_cards=False))
                    for c in cards)
    out = ['<nav class="cardindex">%s</nav>' % index]
    for c in cards:
        meta = ""
        if c["meta"]:
            bits = [b.strip() for b in c["meta"].split(" · ")]
            meta = "".join(
                '<span class="%s">%s</span>'
                % ("badge" if b.startswith(FLAG) else "tag", inline(b, link_cards=False))
                for b in bits)
        asked = "".join("<li>%s</li>" % inline(a) for a in c["asked"])
        traps = "".join("<li>%s</li>" % inline(t) for t in c["traps"])
        out.append(
            '<article class="card" id="%s">'
            '<h3><span class="cid">%s</span> %s</h3>'
            '<div class="meta">%s</div>'
            '<p class="rule">%s</p>'
            '<div class="lens"><h4>Asked</h4><ul class="asked">%s</ul></div>'
            '<div class="lens"><h4>Traps</h4><ul class="traps">%s</ul></div>'
            "</article>"
            % (c["id"].lower(), c["id"], inline(c["title"], link_cards=False),
               meta, inline(c["rule"]), asked, traps))
    return "".join(out), len(cards)


CSS = """
:root{--bg:#fbfaf7;--fg:#22201c;--mut:#6b665e;--line:#e2ddd3;--card:#fff;
--accent:#8a4b2a;--rule:#1d3d33;--trap:#8c2f2f;--form:#2b4a6f;--flag:#8a5a00;
--tagbg:#f0ece3;--moldbg:#f6ecec;}
@media(prefers-color-scheme:dark){:root{--bg:#171614;--fg:#e9e5dd;--mut:#9c968b;
--line:#33302b;--card:#1e1d1a;--accent:#d99268;--rule:#8fc9b4;--trap:#e39191;
--form:#8fb4dd;--flag:#e0b061;--tagbg:#26241f;--moldbg:#2a2120;}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.5 ui-sans-serif,system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
-webkit-text-size-adjust:100%}
code{font:0.86em/1.4 ui-monospace,"Cascadia Mono",Consolas,monospace;
background:var(--tagbg);padding:.08em .32em;border-radius:3px;word-break:break-word}
a{color:inherit}
header.top{position:sticky;top:0;z-index:9;background:var(--bg);
border-bottom:1px solid var(--line)}
.bar{max-width:1080px;margin:0 auto;padding:.55rem 1rem;display:flex;
align-items:baseline;gap:.9rem;flex-wrap:wrap}
.brand{font-weight:700;letter-spacing:-.01em;min-width:0}
.brand span{font-weight:400;color:var(--mut)}
nav.pages{display:flex;gap:.1rem;flex-wrap:wrap;margin-left:auto}
nav.pages a{text-decoration:none;color:var(--mut);padding:.2rem .5rem;
border-radius:5px;font-size:.86rem;white-space:nowrap}
nav.pages a:hover{background:var(--tagbg);color:var(--fg)}
main{max-width:1080px;margin:0 auto;padding:1.2rem 1rem 3rem}
/* Paging: JS toggles .on. The :target fallback is scoped to html:not(.js) so the
   two mechanisms never compete on specificity. Print shows every page. */
.page{display:none}
html.js .page.on{display:block}
html:not(.js) .page:target{display:block}
html:not(.js) .page.start{display:block}
html:not(.js) body:has(.page:target:not(.start)) .page.start{display:none}
h2.ph{font-size:1.5rem;margin:.2rem 0 .1rem;letter-spacing:-.02em}
p.sub{color:var(--mut);margin:0 0 1.1rem;font-size:.94rem}
p{margin:.55rem 0}
ul.plain{margin:.4rem 0 .8rem;padding-left:1.1rem}
ul.plain li{margin:.2rem 0}
.tablewrap{overflow-x:auto;margin:.7rem 0 1rem}
table{border-collapse:collapse;width:100%;font-size:.9rem;min-width:520px}
th,td{border:1px solid var(--line);padding:.4rem .55rem;text-align:left;
vertical-align:top}
th{background:var(--tagbg);font-size:.82rem;letter-spacing:.02em}
nav.cardindex{display:flex;flex-wrap:wrap;gap:.3rem;margin:.2rem 0 1.3rem;
padding-bottom:1rem;border-bottom:1px solid var(--line)}
nav.cardindex a{text-decoration:none;font-size:.78rem;background:var(--tagbg);
border-radius:5px;padding:.2rem .45rem;color:var(--mut);max-width:100%}
nav.cardindex a span{color:var(--fg)}
nav.cardindex a:hover{outline:1px solid var(--accent)}
.card{background:var(--card);border:1px solid var(--line);border-radius:8px;
padding:.85rem 1rem .9rem;margin:0 0 .85rem;scroll-margin-top:4.2rem}
.card h3{margin:0;font-size:1.02rem;letter-spacing:-.01em;line-height:1.35}
.cid{color:var(--accent);font:.78rem/1 ui-monospace,Consolas,monospace;
margin-right:.35rem;letter-spacing:.02em}
.meta{margin:.25rem 0 .1rem;display:flex;gap:.3rem;flex-wrap:wrap}
.meta:empty{display:none}
.tag,.badge{font-size:.72rem;padding:.1rem .4rem;border-radius:4px;
background:var(--tagbg);color:var(--mut)}
.badge{background:transparent;border:1px solid var(--flag);color:var(--flag)}
p.rule{margin:.45rem 0 .6rem;color:var(--rule);font-weight:500}
.lens{margin:.3rem 0}
.lens h4{margin:.35rem 0 .18rem;font-size:.74rem;text-transform:uppercase;
letter-spacing:.09em;color:var(--mut);font-weight:600}
.lens ul{margin:0;padding-left:1.05rem}
.lens li{margin:.16rem 0;font-size:.93rem}
ul.traps li{color:var(--trap)}
ul.traps li code,ul.traps li .mold{color:var(--fg)}
.form{color:var(--form);font-weight:600;font-size:.8rem;letter-spacing:.02em;
white-space:nowrap}
.mold{background:var(--moldbg);color:var(--mut);font-size:.76rem;
padding:.05rem .35rem;border-radius:3px;letter-spacing:.02em}
.xref{color:var(--accent);text-decoration:none;border-bottom:1px dotted var(--accent)}
.pager{display:flex;justify-content:space-between;gap:1rem;margin-top:1.6rem;
padding-top:.9rem;border-top:1px solid var(--line);font-size:.9rem}
.pager a{text-decoration:none;color:var(--accent)}
.pager span{color:var(--mut)}
@media(max-width:620px){.bar{padding:.5rem .7rem}main{padding:1rem .7rem 2rem}
nav.pages{margin-left:0;width:100%}.card{padding:.7rem .75rem}
.brand span{display:none}.brand{font-size:.95rem}
nav.pages a{padding:.2rem .4rem;font-size:.82rem}}
@media print{header.top{display:none}.page{display:block!important;
break-before:page}#p-start{break-before:auto}nav.cardindex{display:none}
.pager{display:none}.card{break-inside:avoid;border-color:#ccc}
body{background:#fff;color:#000;font-size:10.5pt}
:root{--card:#fff;--tagbg:#f2f2f2;--moldbg:#f2f2f2;--mut:#555;--rule:#000;
--trap:#000;--form:#000;--accent:#000;--line:#ccc}
a{text-decoration:none}}
"""


PAGER_JS = """
(function(){
 var pages=[].slice.call(document.querySelectorAll('.page'));
 var start=document.querySelector('.page.start');
 function show(scroll){
  var h=decodeURIComponent((location.hash||'').slice(1));
  var el=h?document.getElementById(h):null;
  var page=el?(el.classList.contains('page')?el:el.closest('.page')):null;
  if(!page)page=start;
  pages.forEach(function(p){p.classList.toggle('on',p===page);});
  if(scroll!==false){
   if(el&&el!==page){el.scrollIntoView({block:'start'});}
   else{window.scrollTo(0,0);}
  }
 }
 window.addEventListener('hashchange',function(){show(true);});
 show(false);
})();
"""


def build(personal):
    md = open(SRC, encoding="utf-8").read()
    if not personal:
        for old, new in GENERIC_REWRITES:
            if old not in md:
                sys.exit("BUILD FAILED: generic rewrite target not found:\n  %s"
                         % old[:110])
            md = md.replace(old, new)

    sections = split_sections(md)
    pages, total_cards = [], 0
    keys = [p for p in PAGES if p[0] in sections
            and not (not personal and p[0] in GENERIC_DROP_PAGES)]

    for idx, (key, _prefix, label, subtitle) in enumerate(keys):
        lines = sections[key]
        if key.startswith("d") and key[1:].isdigit():
            body, n = render_cards(lines)
            total_cards += n
            subtitle += " · %d cards" % n
        else:
            body = render_prose(lines)
        prev_l = ('<a href="#p-%s">← %s</a>' % (keys[idx - 1][0], keys[idx - 1][2])
                  if idx else "<span>Start of the sheet</span>")
        next_l = ('<a href="#p-%s">%s →</a>' % (keys[idx + 1][0], keys[idx + 1][2])
                  if idx + 1 < len(keys) else "<span>End of the sheet</span>")
        heading = {"start": "CCA-F Trap Sheet", "toolkit": "The setter's toolkit",
                   "lookalikes": "Look-alikes", "exam-docs": "Exam ≠ docs",
                   "ledger": "Your ledger"}.get(key)
        if heading is None:
            heading = "Domain %s" % key[1]
        pages.append(
            '<section class="page%s" id="p-%s"><h2 class="ph">%s</h2>'
            '<p class="sub">%s</p>%s'
            '<div class="pager">%s%s</div></section>'
            % (" start" if idx == 0 else "", key, heading, subtitle,
               body, prev_l, next_l))

    nav = "".join('<a href="#p-%s">%s</a>' % (k, lbl) for k, _p, lbl, _s in keys)
    title = ("CCA-F Trap Sheet" if not personal else "CCA-F Trap Sheet · personal")
    tagline = ("How every concept gets tested — and the traps set for it"
               if not personal
               else "How every concept gets tested, the traps set for it, and your own misses")
    doc = (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        "<title>%s</title><style>%s</style>"
        "<script>document.documentElement.className='js'</script></head><body>"
        "<header class=\"top\"><div class=\"bar\">"
        "<div class=\"brand\">%s <span>· %s</span></div>"
        "<nav class=\"pages\">%s</nav></div></header><main>%s</main>"
        "<script>%s</script></body></html>"
        % (title, CSS, title, tagline, nav, "".join(pages), PAGER_JS))

    name = ("CCA-F_Trap-Sheet-Personal_v1.html" if personal
            else "CCA-F_Trap-Sheet_v1.html")
    path = os.path.join(OUTDIR, name)

    if not personal:
        bad = []
        if FLAG in doc:
            bad.append("U+2691 flag")
        m = re.findall(r"Exams? \d+", doc)
        if m:
            bad.append("exam references: %s" % sorted(set(m)))
        if "SESSION-STATE" in doc or "EXAM-LOG" in doc:
            bad.append("project file names")
        if bad:
            sys.exit("BUILD FAILED (generic gate): %s" % "; ".join(bad))

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(doc)
    return path, total_cards, len(keys)


if __name__ == "__main__":
    for is_personal in (False, True):
        p, cards, pages = build(is_personal)
        print("wrote %-46s  %3d cards  %2d pages  %6.1f KB"
              % (os.path.basename(p), cards, pages, os.path.getsize(p) / 1024))
