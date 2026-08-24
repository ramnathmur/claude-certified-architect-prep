#!/usr/bin/env python3
"""Builds CCA-F_Bible_v1.html — the single pre-exam reinforcement document.

Data lives in items_*.py. This file is the renderer + design system only.
Run:  python WIP-BIBLE/build_bible.py [--force]
"""
import os, sys, html, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(PROJECT, "Outputs", "CCA-F_Bible_v1.html")


def load(mod):
    spec = importlib.util.spec_from_file_location(mod, os.path.join(HERE, mod + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


meta = load("items_meta")
D1, D2, D3, D4, D5 = (load(f"items_d{i}").ITEMS for i in range(1, 6))

# ---------------------------------------------------------------- world palette
WORLDS = {
    "kitchen":  ("#E8552F", "#FFE8E1", "The restaurant pass"),
    "workshop": ("#B8791C", "#FDF0D8", "The workshop"),
    "house":    ("#2E7D5B", "#DFF2E7", "The house"),
    "post":     ("#2F5FBF", "#E1EAFB", "The post office"),
    "form":     ("#7A3FA8", "#F0E4F9", "The form"),
    "bay":      ("#0E7C8C", "#DBF1F4", "The loading bay"),
    "news":     ("#C0326B", "#FCE3ED", "The newsroom"),
}

PAGES = [
    ("start",  "Start here",   "Tuesday protocol"),
    ("worlds", "The 7 worlds", "Your visual key"),
    ("red",    "Live errors",  "What is still open"),
    ("d1",     "D1 · 27%",     "Agentic architecture &amp; orchestration"),
    ("d2",     "D2 · 18%",     "Tool design &amp; MCP"),
    ("d3",     "D3 · 20%",     "Claude Code config &amp; workflows"),
    ("d4",     "D4 · 20%",     "Prompt engineering &amp; structured output"),
    ("d5",     "D5 · 15%",     "Context management &amp; reliability"),
    ("rules",  "Tiebreakers",  "The 12 answer heuristics"),
    ("scope",  "Not on it",    "Out of scope — do not panic"),
]

FLAG = {
    "live":  ("LIVE ERROR",  "flag-live"),
    "clear": ("YOU FIXED IT", "flag-clear"),
    "watch": ("WATCH",       "flag-watch"),
}


def card(it):
    """One concept card: bespoke SVG + story + the tell."""
    ink, tint, _ = WORLDS[it["world"]]
    flag = ""
    if it.get("flag"):
        label, cls = FLAG[it["flag"]]
        flag = f'<span class="flag {cls}">{label}</span>'
    cite = f'<span class="cite">{html.escape(it["cite"])}</span>' if it.get("cite") else ""
    extra = it.get("extra", "")
    return f"""
<article class="card{' wide' if extra else ''}" style="--ink:{ink};--tint:{tint}">
  <div class="art">{it['svg']}</div>
  <div class="body">
    <h3>{html.escape(it['title'])}{flag}</h3>
    <p class="story">{it['story']}</p>
    <p class="tell"><span class="tell-k">The tell</span>{it['tell']}</p>
    {extra}
    {cite}
  </div>
</article>"""


def domain_page(key, title, blurb, items):
    cards = "\n".join(card(i) for i in items)
    return f"""<section class="page" id="{key}">
  <header class="page-head">
    <div class="eyebrow">{title}</div>
    <h2>{blurb}</h2>
    <p class="count">{len(items)} things to hold</p>
  </header>
  <div class="cards">{cards}</div>
</section>"""


def build():
    if os.path.exists(OUT) and "--force" not in sys.argv:
        sys.exit(f"REFUSING TO OVERWRITE: {OUT}. Bump the version or pass --force.")

    body = []
    body.append(meta.page_start())
    body.append(meta.page_worlds(WORLDS))
    body.append(meta.page_red(card))
    for key, title, blurb, items in [
        ("d1", "Domain 1 · 27% of the paper", "Agentic architecture &amp; orchestration", D1),
        ("d2", "Domain 2 · 18% of the paper", "Tool design &amp; MCP integration", D2),
        ("d3", "Domain 3 · 20% of the paper", "Claude Code configuration &amp; workflows", D3),
        ("d4", "Domain 4 · 20% of the paper", "Prompt engineering &amp; structured output", D4),
        ("d5", "Domain 5 · 15% of the paper", "Context management &amp; reliability", D5),
    ]:
        body.append(domain_page(key, title, blurb, items))
    body.append(meta.page_rules())
    body.append(meta.page_scope())

    total = sum(len(x) for x in (D1, D2, D3, D4, D5))
    nav = "".join(
        f'<button class="chip" data-go="{k}"><b>{t}</b><i>{s}</i></button>' for k, t, s in PAGES
    )

    html_out = SHELL.format(nav=nav, pages="\n".join(body), total=total,
                            pagekeys=",".join(f'"{k}"' for k, _, _ in PAGES))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html_out)

    print(f"wrote {OUT}")
    print(f"  size: {os.path.getsize(OUT)/1024:.1f} KB")
    print(f"  concept cards: {total}  (D1 {len(D1)} · D2 {len(D2)} · D3 {len(D3)} · D4 {len(D4)} · D5 {len(D5)})")
    live = sum(1 for x in (D1+D2+D3+D4+D5) if x.get("flag") == "live")
    clear = sum(1 for x in (D1+D2+D3+D4+D5) if x.get("flag") == "clear")
    print(f"  flagged: {live} live · {clear} cleared")
    missing_svg = [x["title"] for x in (D1+D2+D3+D4+D5) if "<svg" not in x.get("svg", "")]
    print(f"  cards missing an SVG: {missing_svg or 'none'}")
    return 0 if not missing_svg else 1


SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>CCA-F Bible — everything, one read</title>
<style>
:root{{
  --paper:#FBF7EF; --ink:#15130F; --ink2:#413A31; --ink3:#7A6E60;
  --line:#15130F; --rule:#E2D8C6;
  --sans:"Inter",-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:"SF Mono",ui-monospace,"Cascadia Code",Consolas,monospace;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}}

/* ---------- top bar ---------- */
.bar{{position:sticky;top:0;z-index:60;background:var(--paper);
  border-bottom:3px solid var(--line);box-shadow:0 3px 0 rgba(21,19,15,.08)}}
.bar-in{{max-width:1120px;margin:0 auto;padding:9px 18px;display:flex;align-items:center;gap:14px}}
.brand{{font-weight:900;font-size:15px;letter-spacing:-.02em;white-space:nowrap;
  display:flex;align-items:center;gap:8px}}
.brand .dot{{width:11px;height:11px;border-radius:50%;background:#E8552F;border:2.5px solid var(--line)}}
.chips{{display:flex;gap:6px;overflow-x:auto;flex:1;padding:2px 0;scrollbar-width:thin}}
.chips::-webkit-scrollbar{{height:5px}}
.chips::-webkit-scrollbar-thumb{{background:var(--rule);border-radius:9px}}
.chip{{flex:0 0 auto;font-family:var(--sans);background:#fff;border:2.5px solid var(--line);
  border-radius:11px;padding:5px 11px;cursor:pointer;text-align:left;line-height:1.15;
  box-shadow:2px 2px 0 var(--line);transition:transform .09s,box-shadow .09s}}
.chip b{{display:block;font-size:12px;font-weight:800;letter-spacing:-.01em}}
.chip i{{display:block;font-size:10px;font-style:normal;color:var(--ink3);margin-top:1px;
  max-width:150px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.chip:hover{{transform:translate(-1px,-1px);box-shadow:3px 3px 0 var(--line)}}
.chip.on{{background:#15130F;color:#FBF7EF;box-shadow:2px 2px 0 #E8552F}}
.chip.on i{{color:#C9BEAC}}

/* ---------- page ---------- */
.wrap{{max-width:1120px;margin:0 auto;padding:26px 18px 90px}}
.page{{display:none;animation:pop .16s ease-out}}
.page.on{{display:block}}
@keyframes pop{{from{{opacity:0;transform:translateY(5px)}}to{{opacity:1;transform:none}}}}
.page-head{{margin-bottom:22px;padding-bottom:14px;border-bottom:3px solid var(--line)}}
.eyebrow{{font-size:11px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;color:#E8552F}}
.page-head h2{{font-size:clamp(24px,4vw,34px);font-weight:900;letter-spacing:-.03em;margin-top:3px;line-height:1.05}}
.count{{font-size:12px;color:var(--ink3);margin-top:5px;font-weight:600}}

/* ---------- cards ---------- */
.cards{{display:grid;gap:14px}}
.card{{display:grid;grid-template-columns:104px 1fr;gap:16px;background:#fff;
  border:3px solid var(--line);border-radius:16px;padding:15px 17px;
  box-shadow:4px 4px 0 var(--line)}}
.card .art{{background:var(--tint);border:2.5px solid var(--line);border-radius:12px;
  width:104px;height:104px;display:flex;align-items:center;justify-content:center;align-self:start}}
.card .art svg{{width:78px;height:78px;display:block}}
.card h3{{font-size:17px;font-weight:900;letter-spacing:-.02em;line-height:1.2;
  display:flex;align-items:center;gap:9px;flex-wrap:wrap}}
.story{{margin-top:6px;color:var(--ink2);font-size:14.5px}}
.story b{{color:var(--ink);font-weight:800}}
.tell{{margin-top:9px;background:var(--tint);border:2.5px solid var(--ink);border-radius:10px;
  padding:8px 12px;font-size:14.5px;font-weight:650;color:#15130F}}
.tell-k{{display:block;font-size:9.5px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;
  color:var(--ink);opacity:.55;margin-bottom:2px}}
.cite{{display:inline-block;margin-top:7px;font-family:var(--mono);font-size:10.5px;color:var(--ink3)}}
/* grid/flex children default to min-width:auto, which lets a wide table push the page.
   Pin them to 0 so the table scrolls inside its own box instead. */
.card,.card .body,.note{{min-width:0}}
.card.wide table{{margin-top:10px;font-size:13px;min-width:440px}}
.card.wide th,.card.wide td{{padding:6px 9px}}
.card.wide td:first-child{{font-weight:750;color:var(--ink)}}
.card.wide td:last-child{{color:var(--ink)}}
.card.wide .scroller{{overflow-x:auto;max-width:100%;
  border:2px solid var(--rule);border-radius:9px;padding:2px 8px}}
code{{font-family:var(--mono);font-size:.9em;background:#F1EADC;border:1.5px solid #DDD1BC;
  border-radius:5px;padding:.5px 4px;white-space:nowrap}}
.tell code{{background:rgba(255,255,255,.75);border-color:rgba(21,19,15,.22)}}

.flag{{font-size:9.5px;font-weight:900;letter-spacing:.09em;padding:2.5px 7px;border-radius:99px;
  border:2px solid var(--line);white-space:nowrap}}
.flag-live{{background:#FF4757;color:#fff}}
.flag-clear{{background:#2E7D5B;color:#fff}}
.flag-watch{{background:#F5C518;color:#15130F}}

/* ---------- generic blocks ---------- */
.note{{background:#fff;border:3px solid var(--line);border-radius:16px;padding:17px 19px;
  box-shadow:4px 4px 0 var(--line);margin-bottom:14px}}
.note h3{{font-size:18px;font-weight:900;letter-spacing:-.02em;margin-bottom:7px}}
.note p+p{{margin-top:8px}}
.note.hot{{background:#FFF1F0;border-color:#FF4757;box-shadow:4px 4px 0 #FF4757}}
.note.cool{{background:#EAF7F0;border-color:#2E7D5B;box-shadow:4px 4px 0 #2E7D5B}}
.big{{font-size:19px;font-weight:800;letter-spacing:-.02em;line-height:1.35}}
ul.tick{{list-style:none;margin-top:9px}}
ul.tick li{{position:relative;padding-left:25px;margin-top:6px;font-size:14.5px;color:var(--ink2)}}
ul.tick li::before{{content:"";position:absolute;left:0;top:7px;width:11px;height:11px;
  border:2.5px solid var(--line);border-radius:3.5px;background:#F5C518}}
ul.cross li::before{{background:#FF4757}}
.grid2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(255px,1fr));gap:13px}}
.stat{{background:#fff;border:3px solid var(--line);border-radius:14px;padding:12px 14px;
  box-shadow:3px 3px 0 var(--line)}}
.stat .k{{font-size:10px;font-weight:900;letter-spacing:.11em;text-transform:uppercase;color:var(--ink3)}}
.stat .v{{font-size:21px;font-weight:900;letter-spacing:-.03em;margin-top:2px}}
.stat .s{{font-size:12.5px;color:var(--ink2);margin-top:3px}}
table{{width:100%;border-collapse:collapse;margin-top:11px;font-size:14px}}
th,td{{text-align:left;padding:8px 10px;border-bottom:2px solid var(--rule);vertical-align:top}}
th{{font-size:10.5px;font-weight:900;letter-spacing:.09em;text-transform:uppercase;color:var(--ink3)}}
tr:last-child td{{border-bottom:none}}
.worldrow{{display:flex;align-items:center;gap:13px;padding:11px 0;border-bottom:2px solid var(--rule)}}
.worldrow:last-child{{border-bottom:none}}
.swatch{{width:46px;height:46px;border:2.5px solid var(--line);border-radius:11px;flex:0 0 auto;
  display:flex;align-items:center;justify-content:center;font-size:22px}}

/* ---------- footer nav ---------- */
.pager{{max-width:1120px;margin:26px auto 0;padding:0 18px;display:flex;
  justify-content:space-between;gap:11px}}
.pbtn{{font-family:var(--sans);font-size:13px;font-weight:800;background:#fff;color:var(--ink);
  border:3px solid var(--line);border-radius:12px;padding:10px 17px;cursor:pointer;
  box-shadow:3px 3px 0 var(--line);transition:transform .09s}}
.pbtn:hover:not(:disabled){{transform:translate(-1px,-1px)}}
.pbtn:disabled{{opacity:.32;cursor:default;box-shadow:none}}
@media(max-width:620px){{
  .card{{grid-template-columns:1fr}}
  .card .art{{width:100%;height:92px}}
  .brand i{{display:none}}
}}
</style>
</head>
<body>
<div class="bar"><div class="bar-in">
  <div class="brand"><span class="dot"></span>CCA-F BIBLE</div>
  <div class="chips" id="chips">{nav}</div>
</div></div>
<div class="wrap" id="wrap">
{pages}
</div>
<div class="pager">
  <button class="pbtn" id="prev">← Back</button>
  <button class="pbtn" id="next">Next →</button>
</div>
<script>
const KEYS=[{pagekeys}];
let idx=0;
function go(k,push){{
  const i=typeof k==="number"?k:KEYS.indexOf(k);
  if(i<0||i>=KEYS.length)return;
  idx=i;
  document.querySelectorAll(".page").forEach(p=>p.classList.toggle("on",p.id===KEYS[i]));
  document.querySelectorAll(".chip").forEach(c=>c.classList.toggle("on",c.dataset.go===KEYS[i]));
  document.getElementById("prev").disabled=(i===0);
  document.getElementById("next").disabled=(i===KEYS.length-1);
  const on=document.querySelector(".chip.on");
  if(on&&on.scrollIntoView)on.scrollIntoView({{block:"nearest",inline:"center",behavior:"smooth"}});
  window.scrollTo({{top:0,behavior:"instant"}});
  if(push!==false&&location.hash!=="#"+KEYS[i])history.pushState(null,"","#"+KEYS[i]);
}}
document.getElementById("chips").addEventListener("click",e=>{{
  const b=e.target.closest(".chip"); if(b)go(b.dataset.go);
}});
document.getElementById("prev").onclick=()=>go(idx-1);
document.getElementById("next").onclick=()=>go(idx+1);
addEventListener("popstate",()=>go((location.hash||"#start").slice(1),false));
addEventListener("keydown",e=>{{
  const t=e.target;
  if(t&&typeof t.matches==="function"&&t.matches("input,textarea"))return;
  if(e.key==="ArrowLeft")go(idx-1);
  if(e.key==="ArrowRight")go(idx+1);
}});
go((location.hash||"#start").slice(1),false);
</script>
</body>
</html>"""

if __name__ == "__main__":
    sys.exit(build())
