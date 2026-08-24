#!/usr/bin/env python3
"""Builds Outputs/CCA-F_Concept-Atlas_v1.html — one self-contained, paged, printable HTML file.

Data: inventory.py (ids, citations, KDs, structure) + items_d1..d5.py (card content) + bullets.json (task statements).
This file is the renderer + design system only. Run:  python build_atlas.py [--force] [--out PATH]
If an items file is missing, its cards render as placeholders (for layout testing) and the build reports it.
"""
import html
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PQ = os.path.dirname(HERE)
PROJECT = os.path.dirname(PQ)
OUT = os.path.join(PROJECT, "Outputs", "CCA-F_Concept-Atlas_v1.html")
if "--out" in sys.argv:
    OUT = sys.argv[sys.argv.index("--out") + 1]


def load(name):
    p = os.path.join(HERE, name + ".py")
    if not os.path.exists(p):
        return None
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


inv = load("inventory")
data = json.load(open(os.path.join(HERE, "bullets.json"), encoding="utf-8"))
TS_TITLE = data["task_statements"]
BUL = {b["id"]: b["text"] for b in data["bullets"]}
DOMS = ["D1", "D2", "D3", "D4", "D5"]
DEF = inv.DOMAINS

items = {}
missing_files = []
for d in DOMS:
    m = load(f"items_{d.lower()}")
    if m is None:
        missing_files.append(d)
        items[d] = {}
    else:
        items[d] = {it["id"]: it for it in m.ITEMS}

# Key Distinctions: number -> title
kd_title = {}
kd_raw = open(os.path.join(PQ, "CCA-Prep_Key-Distinctions_v1.md"), encoding="utf-8").read()
for m in re.finditer(r"^### (\d+)\. (.*?)$", kd_raw, re.M):
    kd_title[int(m.group(1))] = m.group(2).strip()

# ------------------------------------------------------------------ helpers
def esc(s):
    return html.escape(str(s), quote=True)


def prose(s):
    """Escape, then backticks -> <code>, **x** -> <b>."""
    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return s


def md_inline(s):
    """For KD titles etc. (already markdown with backticks)."""
    return prose(s)


BUILDING_LABEL = {"D1": "In the tower", "D2": "In the library", "D3": "In the office",
                  "D4": "In the courthouse", "D5": "On the ward"}

# ------------------------------------------------------------------ CSS
CSS = r"""
:root{
  --paper:#FAF7F1; --surface:#FFFFFF; --ink:#1D1B17; --muted:#5F5A52; --rule:#E3DCCF; --rule2:#EFEAE0;
  --trap:#7A5C00; --trapbg:#FBF3DC;
  --d1:#2456A6; --d1t:#E3EAF7; --d2:#2E6B4A; --d2t:#E1EEE6; --d3:#B24A0F; --d3t:#F9E6DA;
  --d4:#6A3D95; --d4t:#ECE3F4; --d5:#B0304A; --d5t:#F8E1E5;
  --acc:var(--ink); --tint:var(--rule2);
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,"Times New Roman",serif;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --mono:ui-monospace,"Cascadia Code",Consolas,Menlo,"Liberation Mono",monospace;
  --maxw:1080px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.55 var(--sans);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
a{color:inherit}
code{font:0.92em var(--mono);background:var(--rule2);padding:.08em .38em;border-radius:5px;white-space:pre-wrap;overflow-wrap:anywhere}
h1,h2,h3{font-family:var(--serif);font-weight:600;letter-spacing:-.01em;margin:0}
.dom-d1{--acc:var(--d1);--tint:var(--d1t)} .dom-d2{--acc:var(--d2);--tint:var(--d2t)} .dom-d3{--acc:var(--d3);--tint:var(--d3t)}
.dom-d4{--acc:var(--d4);--tint:var(--d4t)} .dom-d5{--acc:var(--d5);--tint:var(--d5t)}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}

/* ---- sticky top nav */
.top{position:sticky;top:0;z-index:20;background:rgba(250,247,241,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--rule)}
.top .wrap{display:flex;align-items:center;gap:18px;min-height:56px;flex-wrap:wrap;padding-top:6px;padding-bottom:6px}
.brand{font-family:var(--serif);font-size:19px;font-weight:600;white-space:nowrap;text-decoration:none;display:flex;align-items:center;gap:10px}
.brand svg{width:26px;height:26px}
.tabs{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}
.tabs a{text-decoration:none;font-size:14px;font-weight:600;padding:7px 11px;border-radius:999px;color:var(--muted);border:1px solid transparent;line-height:1}
.tabs a:hover{color:var(--ink);background:var(--rule2)}
.tabs a.on{color:var(--surface);background:var(--acc,var(--ink))}
.tabs a[data-d]{--acc:var(--ink)}
.tabs a[data-d="d1"]{--acc:var(--d1)} .tabs a[data-d="d2"]{--acc:var(--d2)} .tabs a[data-d="d3"]{--acc:var(--d3)}
.tabs a[data-d="d4"]{--acc:var(--d4)} .tabs a[data-d="d5"]{--acc:var(--d5)}

/* ---- pages */
.page{display:none;padding:34px 0 60px}
.page.on{display:block}
.pager{display:flex;justify-content:space-between;gap:16px;margin:48px 0 0;padding-top:24px;border-top:1px solid var(--rule)}
.pager a{text-decoration:none;font-weight:600;font-size:15px;padding:12px 16px;border:1px solid var(--rule);border-radius:12px;background:var(--surface);max-width:48%}
.pager a small{display:block;font-weight:500;color:var(--muted);font-size:12px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:2px}
.pager a:hover{border-color:var(--acc)}
.pager .spacer{flex:1}

/* ---- typographic blocks */
.kicker{font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}
.h1{font-size:44px;line-height:1.08;margin:8px 0 14px}
.lede{font-size:20px;line-height:1.5;color:var(--ink);max-width:56ch;margin:0 0 26px}
.h2{font-size:28px;line-height:1.2;margin:44px 0 10px;scroll-margin-top:80px}
.h3{font-size:21px;margin:26px 0 8px}
p{margin:0 0 12px}
.muted{color:var(--muted)}
.small{font-size:14px}
hr{border:0;border-top:1px solid var(--rule);margin:36px 0}

/* ---- domain header band */
.band{display:grid;grid-template-columns:1fr 340px;gap:28px;align-items:center;background:var(--tint);border:1px solid var(--rule);border-radius:20px;padding:28px 30px;margin-bottom:8px}
.band .h1{font-size:38px}
.band .pill{display:inline-block;background:var(--acc);color:#fff;font-size:12.5px;font-weight:700;letter-spacing:.06em;padding:4px 10px;border-radius:999px;margin-right:8px}
.band svg{width:100%;height:auto;display:block}
.tsnav{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 6px}
.tsnav a{text-decoration:none;font-size:13.5px;font-weight:600;color:var(--acc);border:1px solid var(--rule);background:var(--surface);border-radius:999px;padding:5px 11px}
.tsnav a:hover{border-color:var(--acc)}
.tshead{display:flex;align-items:baseline;gap:14px;margin:46px 0 14px;padding-top:6px;border-top:3px solid var(--acc);scroll-margin-top:80px}
.tshead .n{font-family:var(--mono);font-size:14px;font-weight:700;color:var(--acc);white-space:nowrap}
.tshead h2{font-size:24px}

/* ---- cards */
.card{display:grid;grid-template-columns:200px 1fr;gap:22px;background:var(--surface);border:1px solid var(--rule);border-radius:18px;padding:22px;margin:0 0 18px;scroll-margin-top:84px;box-shadow:0 1px 0 rgba(29,27,23,.03)}
.card:target{outline:3px solid var(--acc);outline-offset:3px}
.ill{background:var(--tint);border-radius:14px;padding:12px;align-self:start}
.ill svg{width:100%;height:auto;display:block}
.ill svg *{fill:none;stroke:var(--ink);stroke-width:3;stroke-linecap:round;stroke-linejoin:round;vector-effect:non-scaling-stroke}
.ill svg .tint{fill:var(--tint)} .ill svg .paper{fill:var(--surface)}
.ill svg .acc{stroke:var(--acc)} .ill svg .accfill{fill:var(--acc);stroke:var(--acc)}
.ill svg .thin{stroke-width:2} .ill svg .dash{stroke-dasharray:5 5} .ill svg .no{stroke-width:4.5}
.ill svg text,.ill svg .lbl{fill:var(--ink);stroke:none;font:600 11px var(--mono)}
.ill svg g{fill:none}
.card .head{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center;margin-bottom:8px}
.card h3{font-size:22.5px;line-height:1.25;flex:1 1 auto;min-width:60%}
.chip{font:600 11.5px/1 var(--mono);padding:5px 8px;border-radius:7px;white-space:nowrap;text-decoration:none}
.chip.ts{color:var(--acc);background:var(--tint)}
.chip.kd{color:var(--trap);background:var(--trapbg)}
.chip.xr{color:var(--muted);background:var(--rule2)}
.chip.pt{color:var(--muted);background:var(--rule2);border:1px dashed var(--rule);cursor:help}
.alsoc{margin:2px 0 18px;padding:12px 16px;border:1px dashed var(--rule);border-radius:12px;font-size:14.5px;color:var(--muted)}
.alsoc .cards{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.chip.card.xdom{outline:1px dashed var(--acc);outline-offset:-1px}
.concept{font-size:18.5px;line-height:1.5;margin:0 0 14px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px}
.box{border:1px solid var(--rule);border-radius:12px;padding:12px 14px;font-size:15.5px;line-height:1.5}
.box .lab{display:block;font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;font-weight:700;color:var(--muted);margin-bottom:5px}
.box.rem{background:var(--tint);border-color:transparent}
.box.rem .lab{color:var(--acc)}
.ana{font-family:var(--serif);font-size:16.5px;line-height:1.55;border-left:3px solid var(--acc);padding:2px 0 2px 14px;color:var(--ink)}
.ana .lab{font-family:var(--sans);display:block;font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;font-weight:700;color:var(--acc);margin-bottom:4px}
.card.placeholder{opacity:.7;border-style:dashed}

/* ---- start page */
.hero{display:grid;grid-template-columns:1.4fr .6fr;gap:36px;align-items:end;margin-bottom:22px}
.mapwrap{background:var(--surface);border:1px solid var(--rule);border-radius:22px;padding:14px;margin-bottom:8px}
.mapwrap svg{width:100%;height:auto;display:block}
.mapwrap svg *{stroke-linecap:round;stroke-linejoin:round}
.mapwrap a{cursor:pointer}
.facts{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin:26px 0}
.fact{background:var(--surface);border:1px solid var(--rule);border-radius:14px;padding:14px 14px 12px}
.fact b{display:block;font-family:var(--serif);font-size:30px;line-height:1;margin-bottom:6px}
.fact span{font-size:13px;color:var(--muted);line-height:1.35;display:block}
.legend{display:grid;grid-template-columns:200px 1fr;gap:22px;background:var(--surface);border:1px dashed var(--rule);border-radius:18px;padding:22px;margin:22px 0}
.legend .lg{font-size:14.5px;line-height:1.5}
.legend .lg b{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--acc)}
.legend .lg li{margin-bottom:6px}
.districts{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin:8px 0 26px}
.district{display:block;text-decoration:none;background:var(--surface);border:1px solid var(--rule);border-radius:16px;padding:16px 14px;color:var(--ink)}
.district:hover{border-color:var(--acc)}
.district .w{font-family:var(--serif);font-size:15px;color:var(--acc);font-weight:600}
.district .n{font-size:14px;line-height:1.35;margin:4px 0 8px}
.district .pct{font:700 12px var(--mono);color:var(--acc);background:var(--tint);padding:3px 7px;border-radius:6px}

/* ---- exam page */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.tile{background:var(--surface);border:1px solid var(--rule);border-radius:16px;padding:18px 18px 14px}
.tile h3{font-size:19px;margin-bottom:6px}
.tile p{font-size:15px;line-height:1.5;color:var(--ink)}
.tile .prim{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.prim span{font:700 11.5px var(--mono);color:#fff;padding:4px 8px;border-radius:6px}
.bars{background:var(--surface);border:1px solid var(--rule);border-radius:16px;padding:18px}
.bar{display:grid;grid-template-columns:150px 1fr 48px;align-items:center;gap:12px;margin:8px 0;font-size:14.5px}
.bar i{display:block;height:14px;border-radius:7px;background:var(--acc)}
.bar b{font:700 13px var(--mono);text-align:right}
table.t{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--rule);border-radius:14px;overflow:hidden;font-size:15px}
table.t th,table.t td{padding:10px 14px;border-bottom:1px solid var(--rule2);text-align:left;vertical-align:top}
table.t th{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);background:var(--rule2)}
table.t tr:last-child td{border-bottom:0}
ul.plain{list-style:none;padding:0;margin:0}
ul.plain li{padding:8px 0;border-bottom:1px solid var(--rule2);font-size:15.5px}
ul.plain li:last-child{border-bottom:0}
ol.tb{padding-left:22px;font-size:15.5px} ol.tb li{margin-bottom:8px}
.oos{columns:2;column-gap:28px;font-size:15px}
.oos li{break-inside:avoid;margin-bottom:6px}

/* ---- traps & coverage */
.trap{display:grid;grid-template-columns:52px 1fr;gap:12px;align-items:baseline;padding:12px 0;border-bottom:1px solid var(--rule2)}
.trap .num{font:700 14px var(--mono);color:var(--trap);background:var(--trapbg);padding:6px 0;text-align:center;border-radius:8px}
.trap .tt{font-size:16.5px;font-weight:600;font-family:var(--serif)}
.trap .pt{font-size:15px;line-height:1.5;color:var(--ink);margin:4px 0 6px;max-width:80ch}
.trap .cards{margin-top:4px;display:flex;flex-wrap:wrap;gap:6px}
.covts{margin:0 0 14px;padding:14px 16px;background:var(--surface);border:1px solid var(--rule);border-radius:14px}
.covts .n{font:700 13px var(--mono);color:var(--acc)}
.covts .cards{margin-top:8px;display:flex;flex-wrap:wrap;gap:6px}
.chip.card{display:inline-block;color:var(--acc);background:var(--tint);border-radius:7px;padding:5px 8px;font:600 11.5px var(--mono);text-decoration:none;box-shadow:none;border:0;margin:0}
.chip.card:hover{filter:brightness(.92)}
footer{border-top:1px solid var(--rule);margin-top:20px;padding:24px 0 40px;font-size:13.5px;color:var(--muted)}

@media (max-width:860px){
  .band{grid-template-columns:1fr} .band svg{max-width:360px}
  .hero{grid-template-columns:1fr} .facts{grid-template-columns:repeat(2,1fr)} .districts{grid-template-columns:1fr 1fr}
  .grid2,.grid3{grid-template-columns:1fr} .oos{columns:1}
}
@media (max-width:720px){
  body{font-size:16px} .wrap{padding:0 16px} .h1{font-size:34px} .band .h1{font-size:30px}
  .card{grid-template-columns:1fr;gap:14px;padding:16px} .ill{max-width:260px}
  .two{grid-template-columns:1fr} .legend{grid-template-columns:1fr}
  .tabs a{padding:6px 9px;font-size:13px}
  .pager{flex-direction:column} .pager a{max-width:none}
}
@media print{
  .top,.pager,.tsnav,.noprint{display:none!important}
  .page{display:block!important;page-break-before:always;padding:0 0 20px}
  .page:first-of-type{page-break-before:auto}
  body{background:#fff;font-size:12.5px}
  .card{break-inside:avoid;box-shadow:none;page-break-inside:avoid;grid-template-columns:150px 1fr;padding:14px;margin-bottom:12px}
  .concept{font-size:14px} .box,.ana{font-size:12px} .card h3{font-size:16px} .h1{font-size:30px} .band .h1{font-size:26px}
  .band{grid-template-columns:1fr 220px} a{text-decoration:none}
}
"""

# ------------------------------------------------------------------ big illustrations (authored here, one hand)
S3 = 'stroke-width="3"'


def svg_wrap(inner, vb="0 0 160 120", cls=""):
    return f'<svg viewBox="{vb}" role="img" aria-hidden="true" class="{cls}">{inner}</svg>'


BUILDING = {
"D1": """<path class="tint" d="M150 190 L158 96 H182 L190 190 Z"/><rect class="tint" x="126" y="72" width="88" height="26" rx="6"/><path d="M132 72 L140 52 H200 L208 72"/><line x1="170" y1="30" x2="170" y2="52"/><circle class="accfill" cx="170" cy="26" r="4"/>
<path class="dash acc thin" d="M120 60 a54 54 0 0 1 100 0"/><path class="dash acc thin" d="M136 66 a36 36 0 0 1 68 0"/>
<path class="tint" d="M28 120 h50 l14 -6 v12 l-14 -6"/><path d="M46 120 l-9 -16 h9 l12 16 M46 120 l-9 16 h9 l12 -16"/>
<path class="tint" d="M232 150 h50 l14 -6 v12 l-14 -6"/><path d="M250 150 l-9 -16 h9 l12 16 M250 150 l-9 16 h9 l12 -16"/>
<line x1="20" y1="190" x2="300" y2="190"/><line class="thin dash" x1="30" y1="182" x2="290" y2="182"/>
<circle class="accfill" cx="60" cy="182" r="3"/><circle class="accfill" cx="120" cy="182" r="3"/><circle class="accfill" cx="200" cy="182" r="3"/><circle class="accfill" cx="260" cy="182" r="3"/>""",
"D2": """<rect class="tint" x="40" y="40" width="240" height="140" rx="6"/><path d="M40 40 L160 16 L280 40"/><line x1="160" y1="16" x2="160" y2="40"/>
<line x1="60" y1="70" x2="140" y2="70"/><line x1="60" y1="104" x2="140" y2="104"/><line x1="60" y1="138" x2="140" y2="138"/>
<rect class="paper" x="66" y="52" width="10" height="18"/><rect class="paper" x="80" y="56" width="12" height="14"/><rect class="acc paper" x="96" y="50" width="10" height="20"/><rect class="paper" x="110" y="54" width="14" height="16"/>
<rect class="paper" x="66" y="86" width="12" height="18"/><rect class="paper" x="82" y="90" width="10" height="14"/><rect class="paper" x="96" y="88" width="14" height="16"/><rect class="acc paper" x="114" y="84" width="10" height="20"/>
<rect class="paper" x="66" y="122" width="14" height="16"/><rect class="paper" x="84" y="118" width="10" height="20"/><rect class="acc paper" x="98" y="120" width="12" height="18"/><rect class="paper" x="114" y="124" width="10" height="14"/>
<rect class="paper" x="176" y="60" width="86" height="100" rx="4"/><rect class="thin" x="188" y="72" width="62" height="18"/><rect class="thin" x="188" y="98" width="62" height="18"/><rect class="thin acc" x="188" y="124" width="62" height="18"/>
<line class="thin" x1="212" y1="81" x2="226" y2="81"/><line class="thin" x1="212" y1="107" x2="226" y2="107"/><line class="thin acc" x1="212" y1="133" x2="226" y2="133"/>
<line x1="20" y1="180" x2="300" y2="180"/>""",
"D3": """<rect class="tint" x="60" y="30" width="200" height="150"/><line x1="60" y1="80" x2="260" y2="80"/><line x1="60" y1="130" x2="260" y2="130"/>
<rect class="paper" x="78" y="44" width="26" height="22"/><rect class="paper" x="118" y="44" width="26" height="22"/><rect class="paper" x="158" y="44" width="26" height="22"/><rect class="paper" x="198" y="44" width="26" height="22"/>
<rect class="paper" x="78" y="94" width="26" height="22"/><rect class="acc paper" x="118" y="94" width="26" height="22"/><rect class="paper" x="158" y="94" width="26" height="22"/><rect class="paper" x="198" y="94" width="26" height="22"/>
<rect class="paper" x="78" y="144" width="26" height="22"/><rect class="paper" x="118" y="144" width="26" height="22"/><rect class="paper" x="158" y="144" width="26" height="22"/><rect class="acc paper" x="198" y="144" width="26" height="22"/>
<rect class="paper" x="228" y="150" width="20" height="30"/><line x1="20" y1="180" x2="300" y2="180"/>
<rect class="tint" x="264" y="52" width="34" height="34" rx="2" transform="rotate(7 281 69)"/><line class="thin" x1="270" y1="64" x2="290" y2="66"/><line class="thin" x1="270" y1="72" x2="288" y2="74"/>""",
"D4": """<rect class="tint" x="50" y="70" width="220" height="110"/><path d="M40 70 L160 22 L280 70 Z" class="tint"/>
<rect class="paper" x="70" y="88" width="16" height="92"/><rect class="paper" x="112" y="88" width="16" height="92"/><rect class="paper" x="154" y="88" width="16" height="92"/><rect class="paper" x="196" y="88" width="16" height="92"/><rect class="paper" x="238" y="88" width="16" height="92"/>
<line x1="20" y1="180" x2="300" y2="180"/>
<line class="acc" x1="160" y1="30" x2="160" y2="60"/><line class="acc" x1="136" y1="40" x2="184" y2="40"/><path class="acc" d="M136 40 l-8 14 h16 z"/><path class="acc" d="M184 40 l-8 14 h16 z"/>""",
"D5": """<rect class="tint" x="40" y="60" width="240" height="120" rx="6"/><line x1="40" y1="100" x2="280" y2="100"/>
<rect class="paper" x="132" y="24" width="56" height="56" rx="8"/><line class="acc" x1="160" y1="36" x2="160" y2="68"/><line class="acc" x1="144" y1="52" x2="176" y2="52"/>
<rect class="paper" x="56" y="120" width="70" height="30" rx="4"/><rect x="56" y="104" width="10" height="46"/><rect class="paper" x="112" y="106" width="20" height="24" rx="2"/><polyline class="acc thin" points="115,124 119,116 123,122 127,112"/>
<rect class="paper" x="194" y="120" width="70" height="30" rx="4"/><rect x="194" y="104" width="10" height="46"/><rect class="paper" x="250" y="106" width="20" height="24" rx="2"/><polyline class="acc thin" points="253,124 257,116 261,122 265,112"/>
<line x1="20" y1="180" x2="300" y2="180"/>""",
}

TOWN_MAP = """
<rect x="0" y="0" width="800" height="440" rx="18" fill="var(--paper)" stroke="none"/>
<path d="M0 300 C120 260 200 340 320 300 S560 250 800 300" fill="none" stroke="var(--rule)" stroke-width="26"/>
<path d="M0 300 C120 260 200 340 320 300 S560 250 800 300" fill="none" stroke="var(--surface)" stroke-width="3" stroke-dasharray="14 12"/>
<path d="M400 0 C380 120 460 200 400 440" fill="none" stroke="var(--rule)" stroke-width="22"/>
<path d="M400 0 C380 120 460 200 400 440" fill="none" stroke="var(--surface)" stroke-width="3" stroke-dasharray="14 12"/>
<g stroke="var(--ink)" stroke-width="3" fill="none">
 <!-- D1 tower (top-left) -->
 <a href="#d1"><g class="dom-d1">
  <rect x="40" y="40" width="300" height="200" rx="16" fill="var(--d1t)" stroke="var(--rule)"/>
  <path d="M182 220 L188 152 H212 L218 220 Z" fill="var(--surface)"/><rect x="160" y="130" width="80" height="22" rx="6" fill="var(--surface)"/><path d="M166 130 L172 114 H228 L234 130"/>
  <line x1="200" y1="104" x2="200" y2="114"/><circle cx="200" cy="101" r="4" fill="var(--d1)" stroke="none"/>
  <path d="M162 148 a38 38 0 0 1 76 0" stroke="var(--d1)" stroke-dasharray="6 6" stroke-width="2"/>
  <path d="M62 190 h44 l12 -6 v12 l-12 -6" fill="var(--surface)"/><path d="M78 190 l-8 -14 h8 l10 14 M78 190 l-8 14 h8 l10 -14"/>
  <path d="M256 174 h44 l12 -6 v12 l-12 -6" fill="var(--surface)"/><path d="M272 174 l-8 -14 h8 l10 14 M272 174 l-8 14 h8 l10 -14"/>
  <line x1="60" y1="222" x2="320" y2="222" stroke-width="2"/>
  <text x="60" y="72" font-family="var(--serif)" font-size="22" font-weight="600" fill="var(--d1)" stroke="none">The control tower</text>
  <text x="60" y="94" font-family="var(--sans)" font-size="13" fill="var(--muted)" stroke="none">D1 · Agentic architecture &amp; orchestration · 27%</text>
 </g></a>
 <!-- D2 library (top-right) -->
 <a href="#d2"><g class="dom-d2">
  <rect x="460" y="40" width="300" height="200" rx="16" fill="var(--d2t)" stroke="var(--rule)"/>
  <rect x="540" y="130" width="140" height="80" rx="4" fill="var(--surface)"/><path d="M540 130 L610 106 L680 130"/>
  <line x1="556" y1="152" x2="606" y2="152"/><line x1="556" y1="176" x2="606" y2="176"/>
  <rect x="560" y="140" width="6" height="12" fill="var(--surface)"/><rect x="570" y="142" width="8" height="10" fill="var(--surface)"/><rect x="582" y="138" width="6" height="14" fill="var(--surface)" stroke="var(--d2)"/><rect x="592" y="141" width="8" height="11" fill="var(--surface)"/>
  <rect x="560" y="164" width="8" height="12" fill="var(--surface)"/><rect x="572" y="166" width="6" height="10" fill="var(--surface)"/><rect x="582" y="163" width="8" height="13" fill="var(--surface)"/><rect x="594" y="162" width="6" height="14" fill="var(--surface)" stroke="var(--d2)"/>
  <rect x="624" y="146" width="44" height="52" rx="3" fill="var(--surface)"/><rect x="632" y="154" width="28" height="10" stroke-width="2"/><rect x="632" y="170" width="28" height="10" stroke-width="2" stroke="var(--d2)"/>
  <text x="480" y="72" font-family="var(--serif)" font-size="22" font-weight="600" fill="var(--d2)" stroke="none">The library</text>
  <text x="480" y="94" font-family="var(--sans)" font-size="13" fill="var(--muted)" stroke="none">D2 · Tool design &amp; MCP integration · 18%</text>
 </g></a>
 <!-- D3 office (bottom-left) -->
 <a href="#d3"><g class="dom-d3">
  <rect x="40" y="260" width="200" height="160" rx="16" fill="var(--d3t)" stroke="var(--rule)"/>
  <rect x="120" y="318" width="90" height="82" fill="var(--surface)"/><line x1="120" y1="346" x2="210" y2="346"/><line x1="120" y1="374" x2="210" y2="374"/>
  <rect x="132" y="326" width="12" height="10" fill="var(--surface)"/><rect x="154" y="326" width="12" height="10" fill="var(--surface)"/><rect x="176" y="326" width="12" height="10" fill="var(--surface)"/>
  <rect x="132" y="354" width="12" height="10" fill="var(--surface)" stroke="var(--d3)"/><rect x="154" y="354" width="12" height="10" fill="var(--surface)"/><rect x="176" y="354" width="12" height="10" fill="var(--surface)"/>
  <rect x="132" y="382" width="12" height="10" fill="var(--surface)"/><rect x="154" y="382" width="12" height="10" fill="var(--surface)"/><rect x="176" y="382" width="12" height="10" fill="var(--surface)" stroke="var(--d3)"/>
  <rect x="58" y="330" width="34" height="34" rx="2" fill="var(--surface)" transform="rotate(7 75 347)"/><line x1="66" y1="342" x2="86" y2="344" stroke-width="2"/><line x1="66" y1="350" x2="84" y2="352" stroke-width="2"/>
  <text x="58" y="292" font-family="var(--serif)" font-size="22" font-weight="600" fill="var(--d3)" stroke="none">The office</text>
  <text x="58" y="312" font-family="var(--sans)" font-size="13" fill="var(--muted)" stroke="none">D3 · Claude Code · 20%</text>
 </g></a>
 <!-- D4 courthouse (bottom-middle) -->
 <a href="#d4"><g class="dom-d4">
  <rect x="300" y="260" width="200" height="160" rx="16" fill="var(--d4t)" stroke="var(--rule)"/>
  <rect x="356" y="344" width="90" height="56" fill="var(--surface)"/><path d="M350 344 L401 316 L452 344 Z" fill="var(--surface)"/>
  <rect x="366" y="354" width="8" height="46" fill="var(--surface)"/><rect x="384" y="354" width="8" height="46" fill="var(--surface)"/><rect x="402" y="354" width="8" height="46" fill="var(--surface)"/><rect x="420" y="354" width="8" height="46" fill="var(--surface)"/>
  <line x1="401" y1="322" x2="401" y2="338" stroke="var(--d4)"/><line x1="389" y1="326" x2="413" y2="326" stroke="var(--d4)"/>
  <text x="318" y="292" font-family="var(--serif)" font-size="22" font-weight="600" fill="var(--d4)" stroke="none">The courthouse</text>
  <text x="318" y="312" font-family="var(--sans)" font-size="13" fill="var(--muted)" stroke="none">D4 · Prompt engineering · 20%</text>
 </g></a>
 <!-- D5 ward (bottom-right) -->
 <a href="#d5"><g class="dom-d5">
  <rect x="560" y="260" width="200" height="160" rx="16" fill="var(--d5t)" stroke="var(--rule)"/>
  <rect x="616" y="350" width="120" height="50" rx="4" fill="var(--surface)"/><line x1="616" y1="368" x2="736" y2="368"/>
  <rect x="660" y="318" width="32" height="32" rx="6" fill="var(--surface)"/><line x1="676" y1="326" x2="676" y2="342" stroke="var(--d5)"/><line x1="668" y1="334" x2="684" y2="334" stroke="var(--d5)"/>
  <rect x="626" y="378" width="30" height="14" rx="2" fill="var(--surface)"/><rect x="696" y="378" width="30" height="14" rx="2" fill="var(--surface)"/>
  <text x="578" y="292" font-family="var(--serif)" font-size="22" font-weight="600" fill="var(--d5)" stroke="none">The hospital ward</text>
  <text x="578" y="312" font-family="var(--sans)" font-size="13" fill="var(--muted)" stroke="none">D5 · Context &amp; reliability · 15%</text>
 </g></a>
</g>
"""

# ------------------------------------------------------------------ page builders
PAGES = [("start", "Start", "Start here"), ("exam", "The exam", "The exam"),
         ("d1", "D1 · 27%", DEF["D1"]["name"]), ("d2", "D2 · 18%", DEF["D2"]["name"]),
         ("d3", "D3 · 20%", DEF["D3"]["name"]), ("d4", "D4 · 20%", DEF["D4"]["name"]),
         ("d5", "D5 · 15%", DEF["D5"]["name"]), ("traps", "Traps", "The 29 traps"), ("coverage", "Coverage", "Coverage map")]
PAGE_IDX = {p[0]: i for i, p in enumerate(PAGES)}


def pager(pid):
    i = PAGE_IDX[pid]
    prev = PAGES[i - 1] if i > 0 else None
    nxt = PAGES[i + 1] if i < len(PAGES) - 1 else None
    a = f'<a href="#{prev[0]}"><small>Previous</small>{esc(prev[2])}</a>' if prev else '<span class="spacer"></span>'
    b = f'<a href="#{nxt[0]}" style="text-align:right"><small>Next</small>{esc(nxt[2])}</a>' if nxt else '<span class="spacer"></span>'
    return f'<nav class="pager">{a}{b}</nav>'


def card_html(c, d):
    it = items[d].get(c["id"])
    ph = it is None
    if ph:
        it = {"title": c["title"], "concept": c["gist"], "tested": "(authoring in progress)",
              "remember": "(authoring in progress)", "analogy": "(authoring in progress)",
              "svg": '<rect class="tint" x="20" y="20" width="120" height="80" rx="8"/><line class="dash" x1="20" y1="20" x2="140" y2="100"/>',
              "alt": "placeholder"}
    chips = [f'<a class="chip ts" href="#ts-{c["ts"]}" title="{esc(TS_TITLE.get(c["ts"], ""))}">TS {c["ts"]}</a>']
    for k in c["kd"]:
        chips.append(f'<a class="chip kd" href="#kd-{k}" title="{esc(kd_title.get(k, ""))}">Trap #{k}</a>')
    for x in c.get("xref", []):
        chips.append(f'<a class="chip xr" href="#ts-{x}">also TS {x}</a>')
    if "Practice-test" in c.get("note", ""):
        chips.append('<span class="chip pt" title="This distinction comes from the practice test the official sample questions are drawn from, not from a task-statement bullet in the exam guide.">practice test</span>')
    svg = f'<svg viewBox="0 0 160 120" role="img" aria-labelledby="{c["id"]}-t"><title id="{c["id"]}-t">{esc(it["alt"])}</title>{it["svg"]}</svg>'
    return f'''<article class="card{' placeholder' if ph else ''}" id="{c["id"]}">
  <div class="ill">{svg}</div>
  <div class="body">
    <div class="head"><h3>{prose(it["title"])}</h3>{"".join(chips)}</div>
    <p class="concept">{prose(it["concept"])}</p>
    <div class="two">
      <div class="box"><span class="lab">What is tested</span>{prose(it["tested"])}</div>
      <div class="box rem"><span class="lab">Remember</span>{prose(it["remember"])}</div>
    </div>
    <div class="ana"><span class="lab">{BUILDING_LABEL[d]}</span>{prose(it["analogy"])}</div>
  </div>
</article>'''


def domain_page(d):
    meta = DEF[d]
    cards = [c for c in inv.CARDS if c["id"].startswith(d + "-")]
    ts_ids = []
    for c in cards:
        if c["ts"] not in ts_ids: ts_ids.append(c["ts"])
    out = [f'<section class="page dom-{d.lower()}" id="p-{d.lower()}" data-title="{esc(meta["name"])}"><div class="wrap">']
    out.append(f'''<div class="band">
  <div><span class="pill">{d} · {meta["weight"]}% of the exam</span><span class="kicker">{esc(meta["world_name"])}</span>
    <h1 class="h1">{esc(meta["name"])}</h1>
    <p class="lede">{len(cards)} concepts across {len(ts_ids)} task statements. Every picture and every analogy on this page happens inside {esc(meta["world_name"].lower())}.</p>
    <div class="tsnav">{"".join(f'<a href="#ts-{t}">{t}</a>' for t in ts_ids)}</div>
  </div>
  <div class="ill" style="background:transparent;padding:0">{svg_wrap(BUILDING[d], "0 0 320 200")}</div>
</div>''')
    for t in ts_ids:
        out.append(f'<div class="tshead" id="ts-{t}"><span class="n">TS {t}</span><h2>{esc(TS_TITLE.get(t, ""))}</h2></div>')
        for c in cards:
            if c["ts"] == t:
                out.append(card_html(c, d))
        ext = [c for c in inv.CARDS if t in c.get("xref", []) and not c["id"].startswith(d + "-")]
        if ext:
            links = "".join(f'<a class="chip card dom-{c["id"][:2].lower()}" href="#{c["id"]}">{c["id"]} · {esc(c["title"])}</a>' for c in ext)
            out.append(f'<div class="alsoc">This task statement is also covered on {"another page" if len(ext) == 1 else "other pages"}:<div class="cards">{links}</div></div>')
    out.append(pager(d.lower()))
    out.append('</div></section>')
    return "\n".join(out)


def start_page():
    n_cards = sum(1 for c in inv.CARDS if not c["id"].startswith("M-"))
    legend = svg_wrap("""<rect class="tint" x="14" y="16" width="132" height="88" rx="10"/>
<circle class="accfill" cx="80" cy="60" r="10"/><circle class="paper" cx="34" cy="34" r="8"/><circle class="paper" cx="126" cy="34" r="8"/><circle class="paper" cx="34" cy="86" r="8"/><circle class="paper" cx="126" cy="86" r="8"/>
<line x1="41" y1="39" x2="72" y2="55"/><line x1="119" y1="39" x2="88" y2="55"/><line x1="41" y1="81" x2="72" y2="65"/><line x1="119" y1="81" x2="88" y2="65"/>
<line class="dash thin" x1="44" y1="34" x2="116" y2="34"/><line class="no" x1="74" y1="26" x2="86" y2="42"/><line class="no" x1="86" y1="26" x2="74" y2="42"/>""")
    districts = "".join(
        f'<a class="district dom-{d.lower()}" href="#{d.lower()}"><span class="w">{esc(DEF[d]["world_name"])}</span>'
        f'<div class="n">{esc(DEF[d]["name"])}</div><span class="pct">{d} · {DEF[d]["weight"]}%</span></a>' for d in DOMS)
    return f'''<section class="page" id="p-start" data-title="Start here"><div class="wrap">
<div class="hero">
  <div>
    <span class="kicker">Claude Certified Architect – Foundations</span>
    <h1 class="h1">The Concept Atlas</h1>
    <p class="lede">Every concept the exam tests, on one map. {n_cards} concept cards in five buildings — one per domain — each with the concept, what the exam asks about it, the rule to remember, and a picture and a story from the same building so it stays with you.</p>
  </div>
  <p class="small muted" style="max-width:38ch;margin:0">Read it front to back on the day before, or open the building you are least sure of. Nothing here needs a login, a network, or prior notes; it prints cleanly. Click a building on the map to go there.</p>
</div>
<div class="mapwrap">{svg_wrap(TOWN_MAP, "0 0 800 440")}</div>
<div class="facts">
  <div class="fact"><b>60</b><span>questions, single answer, four options each</span></div>
  <div class="fact"><b>120</b><span>minutes — two minutes a question</span></div>
  <div class="fact"><b>4 of 6</b><span>production scenarios frame the questions</span></div>
  <div class="fact"><b>720</b><span>to pass on a 100–1,000 scaled score</span></div>
  <div class="fact"><b>0</b><span>skips — the platform requires an answer to advance</span></div>
</div>
<h2 class="h2">The five buildings</h2>
<p class="muted">Each domain is a building in the same town. Learn where a concept lives and you can find it under a two-minute clock.</p>
<div class="districts">{districts}</div>
<h2 class="h2">How to read a card</h2>
<div class="legend dom-d1">
  <div class="ill">{legend}</div>
  <div class="lg"><ul class="plain">
    <li><b>Picture</b> — one idea, drawn in the domain's building. The accent colour marks the thing the card is about; a crossed-out shape is the anti-pattern the exam pairs against it.</li>
    <li><b>Title and concept</b> — the fact, in one sentence.</li>
    <li><b>What is tested</b> — the situation the exam sets, the decision it asks for, and the wrong option it places beside the right one.</li>
    <li><b>Remember</b> — the rule and the tell that identifies the correct option.</li>
    <li><b>In the building</b> — a two-sentence real-world analogy from the same building, so a domain reads as one story.</li>
    <li><b>Chips</b> — <span class="chip ts" style="display:inline-block">TS 1.2</span> is the official task statement; <span class="chip kd" style="display:inline-block">Trap #6</span> links to the trap index.</li>
  </ul></div>
</div>
{pager("start")}
</div></section>'''


SCENARIOS = [
    ("Customer Support Resolution Agent", "An Agent SDK agent handles returns, billing disputes and account issues through custom MCP tools (`get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`), targeting 80%+ first-contact resolution while knowing when to escalate.", ["D1", "D2", "D5"]),
    ("Code Generation with Claude Code", "Claude Code for generation, refactoring, debugging and documentation — custom slash commands, `CLAUDE.md` configuration, and plan mode versus direct execution.", ["D3", "D5"]),
    ("Multi-Agent Research System", "A coordinator delegates to web-search, document-analysis, synthesis and report subagents to produce comprehensive, cited reports.", ["D1", "D2", "D5"]),
    ("Developer Productivity with Claude", "An Agent SDK agent that explores unfamiliar codebases, explains legacy systems, generates boilerplate and automates chores, using the built-in tools (Read, Write, Bash, Grep, Glob) and MCP servers.", ["D2", "D3", "D1"]),
    ("Claude Code for Continuous Integration", "Claude Code in CI/CD: automated code review, test generation and PR feedback, with prompts that give actionable feedback and few false positives.", ["D3", "D4"]),
    ("Structured Data Extraction", "Extraction from unstructured documents, validated against JSON schemas, accurate, graceful on edge cases, integrated downstream.", ["D4", "D5"]),
]
TIEBREAKERS = [
    ("Fix the root cause, not the symptom", "misrouting between two tools → rewrite the descriptions, not add a classifier"),
    ("Proportionate first response", "the prompt or description fix comes before new infrastructure — routing layers, separate models, bigger context windows"),
    ("Code for guarantees, prompts for guidance", "a sequence that must hold (verify identity before a refund) is a hook or prerequisite gate; prompt compliance is probabilistic"),
    ("Least privilege", "give the synthesis agent a scoped `verify_fact` tool, not the whole web-search toolset"),
    ("Structured over generic", "errors, handoffs and subagent outputs carry typed fields; a bare \"failed\" or a free-text summary loses what the next decision needs"),
    ("Match the API to the latency", "blocking pre-merge checks stay synchronous; overnight or weekly work goes to the Message Batches API"),
    ("Independence for review", "a second instance without the generator's reasoning context, and per-file passes plus an integration pass for large reviews"),
    ("Coverage gaps trace upstream", "every subagent succeeded and topics are still missing → look at the coordinator's decomposition"),
    ("The signal, not a proxy", "read `stop_reason`, not the text; escalate on written criteria, not sentiment or self-reported confidence"),
]
OOS = [BUL[f"APP-O{i}"] for i in range(1, 17)]


def exam_page():
    dchips = lambda ds: "".join(f'<span style="background:var(--{d.lower()})">{d}</span>' for d in ds)
    sc = "".join(f'<div class="tile"><span class="kicker">Scenario {i+1}</span><h3>{esc(n)}</h3><p>{prose(t)}</p><div class="prim">{dchips(ds)}</div></div>'
                 for i, (n, t, ds) in enumerate(SCENARIOS))
    bars = "".join(f'<div class="bar dom-{d.lower()}"><span>{d} · {esc(inv.SHORT[d])}</span><i style="width:{DEF[d]["weight"]/27*100:.0f}%"></i><b>{DEF[d]["weight"]}%</b></div>' for d in DOMS)
    tb = "".join(f'<li><b>{esc(a)}</b> — {prose(b)}</li>' for a, b in TIEBREAKERS)
    oos = "".join(f'<li>{esc(o)}</li>' for o in OOS)
    return f'''<section class="page" id="p-exam" data-title="The exam"><div class="wrap">
<span class="kicker">The paper</span>
<h1 class="h1">The exam</h1>
<p class="lede">What the paper looks like, how the questions are built, and what the sample answers reward.</p>
<div class="grid2">
  <table class="t"><tr><th>Item</th><th>Value</th></tr>
    <tr><td>Credential</td><td>Claude Certified Architect – Foundations</td></tr>
    <tr><td>Questions</td><td>60, multiple choice — one correct answer and three incorrect options</td></tr>
    <tr><td>Time</td><td>120 minutes</td></tr>
    <tr><td>Structure</td><td>4 scenarios presented, drawn at random from a bank of 6; each frames a block of questions</td></tr>
    <tr><td>Scoring</td><td>Scaled 100–1,000; minimum passing score 720; result reported as pass or fail</td></tr>
    <tr><td>Answering</td><td>The platform requires an answer to every question before you can advance — nothing is left blank</td></tr>
    <tr><td>Validity</td><td>12 months from award; delivered online proctored or at a test centre; fee US$125</td></tr>
  </table>
  <div class="bars"><span class="kicker">Domain weights</span>{bars}
    <p class="small muted" style="margin-top:12px">Weights are of scored content; scaled scoring equates forms of slightly different difficulty. The platform requires an answer to every question before you can advance.</p></div>
</div>
<h2 class="h2">The six scenarios</h2>
<p class="muted">Every sitting shows four of these. Each scenario's questions lean on the domains marked; the weights above are of total scored content.</p>
<div class="grid3">{sc}</div>
<h2 class="h2">How a question is built</h2>
<div class="grid2">
  <div class="tile"><h3>The stem</h3><p>Two to five sentences of situation with concrete telemetry — "in 12% of cases", "55% first-contact resolution", "a PR touching 14 files" — then one decision question: <i>most effective first step</i>, <i>most likely root cause</i>, <i>how should you evaluate this proposal</i>.</p></div>
  <div class="tile"><h3>The options</h3><p>Four full clauses, grammatically parallel, each plausible to someone with partial knowledge. The wrong ones fall into families: a symptom-level fix, over-engineering, a feature that does not exist, a solution to a different problem, or a probabilistic control where a deterministic one is available.</p></div>
</div>
<h2 class="h2">The tie-breakers the sample answers reward</h2>
<p class="muted">Distilled from the guide's task statements and the rationales of its twelve sample questions. When two options both sound reasonable, these decide.</p>
<ol class="tb">{tb}</ol>
<h2 class="h2">Will not appear</h2>
<p class="muted">The guide's own out-of-scope list. If an option turns on one of these, it is not the answer.</p>
<ul class="oos">{oos}</ul>
{pager("exam")}
</div></section>'''


def traps_page():
    by_kd = {}
    for c in inv.CARDS:
        for k in c["kd"]:
            by_kd.setdefault(k, []).append(c)
    rows = []
    for k in range(1, 30):
        cards = by_kd.get(k, [])
        chips = "".join(f'<a class="chip card dom-{c["id"][:2].lower()}" href="#{c["id"]}">{c["id"]} · {esc(c["title"])}</a>' for c in cards)
        rows.append(f'<div class="trap" id="kd-{k}"><span class="num">#{k}</span><div><div class="tt">{md_inline(kd_title.get(k, ""))}</div><div class="pt">{prose(inv.KD_POINT.get(k, ""))}</div><div class="cards">{chips}</div></div></div>')
    return f'''<section class="page" id="p-traps" data-title="The 29 traps"><div class="wrap">
<span class="kicker">Look-alike pairs</span>
<h1 class="h1">The 29 traps</h1>
<p class="lede">Each trap is a pair of options that look similar and differ on one decisive point. Every trap lives on at least one card; the card carries the distinction in its <i>What is tested</i> and <i>Remember</i> fields.</p>
{"".join(rows)}
{pager("traps")}
</div></section>'''


def coverage_page():
    out = []
    for d in DOMS:
        cards = [c for c in inv.CARDS if c["id"].startswith(d + "-")]
        ts_ids = []
        for c in cards:
            if c["ts"] not in ts_ids: ts_ids.append(c["ts"])
        out.append(f'<h2 class="h2 dom-{d.lower()}" style="color:var(--acc)">{d} · {esc(DEF[d]["name"])} · {DEF[d]["weight"]}%</h2>')
        for t in ts_ids:
            n_b = sum(1 for b in data["bullets"] if b["ts"] == t)
            own = [c for c in cards if c["ts"] == t]
            ext = [c for c in inv.CARDS if t in c.get("xref", []) and not c["id"].startswith(d + "-")]
            chips = "".join(f'<a class="chip card" href="#{c["id"]}">{c["id"]} · {esc(c["title"])}</a>' for c in own)
            chips += "".join(f'<a class="chip card xdom dom-{c["id"][:2].lower()}" href="#{c["id"]}">{c["id"]} · {esc(c["title"])}</a>' for c in ext)
            out.append(f'<div class="covts dom-{d.lower()}"><span class="n">TS {t}</span> {esc(TS_TITLE.get(t, ""))} <span class="small muted">· {n_b} official bullets</span><div class="cards">{chips}</div></div>')
    n_ts = sum(1 for b in data["bullets"] if b["ts"] != "APP")
    n_cards = sum(1 for c in inv.CARDS if not c["id"].startswith("M-"))
    return f'''<section class="page" id="p-coverage" data-title="Coverage map"><div class="wrap">
<span class="kicker">Proof of coverage</span>
<h1 class="h1">Coverage map</h1>
<p class="lede">The official guide lists 30 task statements with {n_ts} knowledge and skill bullets, plus appendix lists of technologies, in-scope and out-of-scope topics. Every task statement bullet, technology and in-scope item maps to at least one of the {n_cards} cards below, checked by script before this file is built. The out-of-scope list is reproduced on the exam page rather than carded, because none of it is examinable.</p>
{"".join(out)}
{pager("coverage")}
</div></section>'''


# ------------------------------------------------------------------ assemble
JS = r"""
(function(){
  var pages=[].slice.call(document.querySelectorAll('.page'));
  var ids=pages.map(function(p){return p.id.replace(/^p-/,'')});
  var tabs=[].slice.call(document.querySelectorAll('.tabs a'));
  function show(id,scrollTo){
    if(ids.indexOf(id)<0){ // maybe a card / anchor id
      var el=document.getElementById(id);
      if(!el){id='start';}else{
        var pg=el.closest('.page'); if(!pg){id='start';} else {
          pages.forEach(function(p){p.classList.toggle('on',p===pg)});
          tabs.forEach(function(t){t.classList.toggle('on',t.getAttribute('href')==='#'+pg.id.replace(/^p-/,''))});
          setTimeout(function(){el.scrollIntoView({block:'start'});},0);
          document.title=el.closest('.page').getAttribute('data-title')+' — CCA-F Concept Atlas';
          return;
        }
      }
    }
    pages.forEach(function(p){p.classList.toggle('on',p.id==='p-'+id)});
    tabs.forEach(function(t){t.classList.toggle('on',t.getAttribute('href')==='#'+id)});
    var pg=document.getElementById('p-'+id);
    document.title=pg.getAttribute('data-title')+' — CCA-F Concept Atlas';
    if(scrollTo!==false) window.scrollTo(0,0);
  }
  function route(){var h=(location.hash||'#start').slice(1); show(h);}
  window.addEventListener('hashchange',route);
  route();
  document.addEventListener('keydown',function(e){
    if(e.target&&/input|textarea/i.test(e.target.tagName))return;
    var cur=ids.indexOf((location.hash||'#start').slice(1));
    if(cur<0){var el=document.getElementById((location.hash||'#start').slice(1)); if(el&&el.closest('.page')) cur=ids.indexOf(el.closest('.page').id.replace(/^p-/,''));}
    if(e.key==='ArrowRight'&&cur<ids.length-1) location.hash='#'+ids[cur+1];
    if(e.key==='ArrowLeft'&&cur>0) location.hash='#'+ids[cur-1];
  });
})();
"""

BRAND_SVG = '<svg viewBox="0 0 26 26" aria-hidden="true"><rect x="2" y="2" width="22" height="22" rx="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M7 17 L13 8 L19 17 Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><circle cx="13" cy="15" r="1.6" fill="currentColor"/></svg>'


def build():
    tabs = "".join(f'<a href="#{pid}" data-d="{pid if pid.startswith("d") and len(pid)==2 else ""}">{esc(label)}</a>' for pid, label, _ in PAGES)
    body = [start_page(), exam_page()] + [domain_page(d) for d in DOMS] + [traps_page(), coverage_page()]
    n_cards = sum(1 for c in inv.CARDS if not c["id"].startswith("M-"))
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CCA-F Concept Atlas — every concept the Claude Certified Architect – Foundations exam tests</title>
<meta name="description" content="A single-file, illustrated refresher for the Claude Certified Architect – Foundations exam: {n_cards} concept cards across the five domains, each with what is tested, what to remember, a picture and a real-world analogy.">
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="#start">{BRAND_SVG}CCA-F Concept Atlas</a>
  <nav class="tabs" aria-label="Pages">{tabs}</nav>
</div></header>
<main>
{"".join(body)}
</main>
<footer><div class="wrap">
  <p><b>CCA-F Concept Atlas</b> · Independent study material grounded in the official <i>Claude Certified Architect – Foundations</i> Exam Guide (its five domains, thirty task statements and appendix scope lists). Not affiliated with or endorsed by Anthropic; product names belong to their owners. Verify current product behaviour against the official documentation — the exam follows the guide's framing.</p>
  <p class="small">Single self-contained file: no network requests, no tracking, no stored data. Use your browser's Print for a PDF; every page prints in order.</p>
</div></footer>
<script>{JS}</script>
</body>
</html>'''
    return doc


if __name__ == "__main__":
    doc = build()
    if os.path.exists(OUT) and "--force" not in sys.argv and "--out" not in sys.argv:
        print("refusing to overwrite", OUT, "— pass --force"); sys.exit(1)
    if os.path.dirname(OUT):
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(doc)
    n_ph = sum(1 for d in DOMS for c in inv.CARDS if c["id"].startswith(d + "-") and c["id"] not in items[d])
    print(f"wrote {OUT}  ({len(doc)/1024:.0f} KB)  placeholders: {n_ph}  missing item files: {missing_files or 'none'}")
