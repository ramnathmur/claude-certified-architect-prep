"""Render the five CCA-Prep domain corpus files into one paged, self-contained HTML."""
import io, os, re, html as H

SRC = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz"
OUT = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\Claude-Certified-Architect-Foundations_Exam-Prep_v1\Learning corpus\CCA-F_Corpus_v1.html"

DOMAINS = [
    ("d1", "1", "Agentic Architecture & Orchestration", "Agentic", "27%", "CCA-Prep_Domain-1_v2.md"),
    ("d2", "2", "Tool Design & MCP Integration", "Tools & MCP", "18%", "CCA-Prep_Domain-2_v2.md"),
    ("d3", "3", "Claude Code Configuration & Workflows", "Claude Code", "20%", "CCA-Prep_Domain-3_v2.md"),
    ("d4", "4", "Prompt Engineering & Structured Output", "Prompts", "20%", "CCA-Prep_Domain-4_v2.md"),
    ("d5", "5", "Context Management & Reliability", "Context", "15%", "CCA-Prep_Domain-5_v2.md"),
]

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from md2blocks import render, inline
from corpus_extras import clean, INDEX_MD

# ---------- assemble ----------
pages, navtabs = [], []
idx_html, _ = render(INDEX_MD)

for did, dnum, full, short, wt, fn in DOMAINS:
    md = clean(io.open(os.path.join(SRC, fn), encoding='utf-8').read())
    body, secs = render(md)
    jump = ''.join('<a href="#%s"><b>&sect;%s</b> %s</a>' % (sid, num, H.escape(title)) for sid, num, title in secs)
    pages.append(
        '<section class="page" id="p-%s" data-title="%s">'
        '<div class="pghead"><div class="kicker">Domain %s &middot; %s of the paper</div>'
        '<h1>%s</h1>'
        '<p class="sub">%d sections. Citations elsewhere in this pack of the form '
        '<code>&sect;%s.n</code> point here.</p></div>'
        '<nav class="jump" aria-label="Sections in this domain">%s</nav>'
        '<div class="prose">%s</div></section>'
        % (did, H.escape(full), dnum, wt, H.escape(full), len(secs), dnum, jump, body))
    navtabs.append((did, short, wt))

tabs = '<a href="#index">Index</a>' + ''.join(
    '<a href="#%s">%s %s &middot; %s</a>' % (d, d.upper(), s, w) for d, s, w in navtabs)

PACKBAR = ('<nav class="packbar" aria-label="CCA-F prep pack"><span class="pb-lab">CCA-F prep pack</span>'
           '<a href="../README.html">Start here</a>'
           '<a href="Exam-Day-Guide.html">Exam Day Guide</a>'
           '<a href="CCA-F_Concept-Atlas_v2.html">Concept Atlas</a>'
           '<a href="CCA-F_Trap-Sheet_v1.html">Trap Sheet</a>'
           '<a href="CCA-F_Corpus_v1.html" aria-current="page">Corpus</a>'
           '<a href="CCA-F_One-Page-Sheet_v1.html">One-page sheet</a>'
           '<a href="../Mock%20tests/Test-1.html">Practice tests</a>'
           '<a href="../Mock%20tests/Test-MR.html">MR drill</a>'
           '<a href="../Mock%20tests/Dashboard.html">Dashboard</a></nav>')

CSS = """
:root{--ink:#1a1814;--ink2:#3d3a34;--ink3:#7a7670;--cream:#faf7f2;--cream2:#f2ede4;
--amber:#c8832a;--amber-dark:#8a5a1a;--border:#ddd8ce;--code-bg:#f4f0e8;
--sans:'DM Sans',system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
--serif:'DM Serif Display',Georgia,serif;--mono:'JetBrains Mono',ui-monospace,Consolas,monospace;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:96px}
body{font-family:var(--sans);background:var(--cream);color:var(--ink2);font-size:15.5px;line-height:1.68}
.packbar{font:500 13px/1.4 var(--sans);background:#141821;color:#c9d1e0;padding:.5rem .9rem;
 display:flex;flex-wrap:wrap;align-items:center;gap:.35rem .5rem}
.packbar .pb-lab{color:#8d97ab;font-weight:600;letter-spacing:.02em;text-transform:uppercase;font-size:11px;margin-right:.3rem}
.packbar a{color:#c9d1e0;text-decoration:none;padding:.2rem .5rem;border-radius:999px;border:1px solid transparent;white-space:nowrap}
.packbar a:hover{background:#252c3a;color:#fff}
.packbar a[aria-current="page"]{background:#3b6ef5;color:#fff;border-color:#3b6ef5}
header.top{position:sticky;top:0;z-index:40;background:rgba(250,247,242,.96);
 backdrop-filter:blur(8px);border-bottom:1px solid var(--border)}
.bar{max-width:60rem;margin:0 auto;padding:10px 28px;display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 14px}
.brand{font-family:var(--serif);font-size:17px;color:var(--ink);white-space:nowrap}
.brand span{font-family:var(--sans);font-size:12px;color:var(--ink3);margin-left:6px}
nav.tabs{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}
nav.tabs a{text-decoration:none;font-size:13px;font-weight:600;padding:6px 10px;border-radius:999px;
 color:var(--ink3);border:1px solid transparent;line-height:1;white-space:nowrap}
nav.tabs a:hover{color:var(--ink);background:var(--cream2)}
nav.tabs a.on{color:#fff;background:var(--ink)}
main{max-width:60rem;margin:0 auto;padding:30px 28px 90px}
.page{display:none}.page.on{display:block}
.pghead{border-bottom:1px solid var(--border);padding-bottom:18px;margin-bottom:22px}
.kicker{font-family:var(--mono);font-size:11px;letter-spacing:.15em;text-transform:uppercase;
 color:var(--amber-dark);margin-bottom:9px}
.pghead h1,.doc-h1{font-family:var(--serif);font-weight:400;font-size:clamp(25px,3.6vw,33px);
 color:var(--ink);line-height:1.18}
.doc-h1{margin:0 0 14px}
.pghead .sub{font-size:14px;color:var(--ink3);margin-top:9px}
nav.jump{display:flex;flex-direction:column;gap:1px;background:#fff;border:1px solid var(--border);
 border-radius:9px;padding:10px 12px;margin-bottom:30px;max-height:280px;overflow:auto}
nav.jump a{text-decoration:none;color:var(--ink2);font-size:13.5px;padding:3px 5px;border-radius:5px}
nav.jump a:hover{background:var(--cream2);color:var(--ink)}
nav.jump b{font-family:var(--mono);font-size:11.5px;color:var(--amber-dark);margin-right:7px}
.prose h2.sec{font-family:var(--serif);font-weight:400;font-size:24px;color:var(--ink);
 margin:42px 0 12px;padding-top:16px;border-top:2px solid var(--cream2);line-height:1.22}
.prose h2.sec:first-child{margin-top:0;border-top:none;padding-top:0}
.prose h2.sec .anchor{font-family:var(--mono);font-size:13px;color:var(--amber);text-decoration:none;margin-right:7px}
.prose h2.sec .anchor:hover{color:var(--amber-dark)}
.prose h3{font-family:var(--sans);font-weight:600;font-size:15.5px;color:var(--ink);
 margin:22px 0 8px;letter-spacing:-.005em}
.prose h4{font-family:var(--mono);font-weight:500;font-size:12px;letter-spacing:.06em;
 text-transform:uppercase;color:var(--ink3);margin:18px 0 7px}
.prose p{margin:0 0 12px}
.prose ul,.prose ol{margin:0 0 13px 1.25rem}
.prose li{margin-bottom:5px}
.prose li>ul,.prose li>ol{margin-top:5px;margin-bottom:6px}
.prose hr{border:0;border-top:1px solid var(--border);margin:26px 0;opacity:.55}
.prose blockquote{border-left:3px solid var(--amber);background:#fff;padding:11px 16px;
 margin:0 0 14px;border-radius:0 7px 7px 0;font-size:14.5px}
code{font-family:var(--mono);font-size:.855em;background:var(--code-bg);border:1px solid var(--border);
 padding:1px 5px;border-radius:4px;color:var(--ink)}
pre{background:#fbf8f2;border:1px solid var(--border);border-radius:8px;padding:13px 15px;
 overflow-x:auto;margin:0 0 15px}
pre code{background:none;border:0;padding:0;font-size:12.6px;line-height:1.6;color:var(--ink2)}
.tw{overflow-x:auto;margin:0 0 16px;border:1px solid var(--border);border-radius:8px;background:#fff}
table{width:100%;border-collapse:collapse;font-size:13.6px}
th{text-align:left;font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;
 color:var(--ink3);font-weight:600;padding:9px 13px;border-bottom:1px solid var(--border);background:var(--cream2)}
td{padding:9px 13px;border-bottom:1px solid var(--cream2);vertical-align:top}
tr:last-child td{border-bottom:none}
a{color:var(--amber-dark)}
footer{border-top:1px solid var(--border);max-width:60rem;margin:0 auto;padding:20px 28px 40px;
 font-size:12.5px;color:var(--ink3);line-height:1.6}
@media (max-width:680px){.bar,main,footer{padding-left:16px;padding-right:16px}
 nav.tabs{margin-left:0;width:100%}nav.tabs a{font-size:12px;padding:5px 8px}}
@media print{.packbar,header.top,nav.jump{display:none}.page{display:block!important}
 body{background:#fff;font-size:10pt}main{max-width:none;padding:0}
 .prose h2.sec{page-break-after:avoid}pre,.tw,blockquote{page-break-inside:avoid}}
"""

JS = """
(function(){
 var pages=[].slice.call(document.querySelectorAll('.page'));
 var ids=pages.map(function(p){return p.id.replace(/^p-/,'')});
 var tabs=[].slice.call(document.querySelectorAll('nav.tabs a'));
 function paint(id){
  pages.forEach(function(p){p.classList.toggle('on',p.id==='p-'+id)});
  tabs.forEach(function(t){t.classList.toggle('on',t.getAttribute('href')==='#'+id)});
  var pg=document.getElementById('p-'+id);
  if(pg)document.title=pg.getAttribute('data-title')+' \\u2014 CCA-F Corpus';
 }
 function show(h){
  if(!h)h='index';
  if(ids.indexOf(h)>=0){paint(h);window.scrollTo(0,0);return;}
  var el=document.getElementById(h);
  if(el){
   var pg=el.closest('.page');
   if(pg){paint(pg.id.replace(/^p-/,''));
    setTimeout(function(){el.scrollIntoView({block:'start'});el.classList.add('flash');
     setTimeout(function(){el.classList.remove('flash')},1500);},30);
    return;}
  }
  paint('index');window.scrollTo(0,0);
 }
 function route(){show(decodeURIComponent((location.hash||'').slice(1)));}
 window.addEventListener('hashchange',route);
 route();
 document.addEventListener('keydown',function(e){
  if(e.target&&/input|textarea/i.test(e.target.tagName))return;
  var cur=-1;
  pages.forEach(function(p,k){if(p.classList.contains('on'))cur=k});
  if(e.key==='ArrowRight'&&cur>=0&&cur<ids.length-1)location.hash='#'+ids[cur+1];
  if(e.key==='ArrowLeft'&&cur>0)location.hash='#'+ids[cur-1];
 });
})();
"""

doc = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>CCA-F Corpus \u2014 the source behind every citation</title>
<meta name="description" content="The full CCA-F study corpus: five domains, every numbered section that the practice tests and the Trap Sheet cite."/>
<link rel="icon" href="data:,"/>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>%s
h2.sec.flash{background:#fdf3dd;border-radius:6px;transition:background .5s}
</style>
</head>
<body>
%s
<header class="top"><div class="bar">
<div class="brand">CCA-F Corpus <span>&middot; the source behind every &sect; citation</span></div>
<nav class="tabs" aria-label="Domains">%s</nav>
</div></header>
<main>
<section class="page" id="p-index" data-title="Index">
<div class="pghead">
<div class="kicker">Start here</div>
<h1>The corpus</h1>
<p class="sub">Every answer explanation in the practice tests, and every card on the Trap Sheet, cites a section of this document \u2014 <code>&sect;1.6</code>, <code>&sect;4.9</code>, and so on. This is that document. Pick a domain above, or follow any citation link and it will land on the exact section.</p>
</div>
<div class="prose">%s</div>
</section>
%s
</main>
<footer>
<p><b>CCA-F Corpus</b> \u2014 the five domain study files of this project, rendered as one document. Independent study material grounded in the official <i>Claude Certified Architect \u2013 Foundations</i> Exam Guide v0.2 (30 June 2026). Not affiliated with or endorsed by Anthropic; product names belong to their owners. Verify current product behaviour against the official documentation.</p>
<p style="margin-top:8px">Single self-contained file: no network requests, no tracking, no stored data. Use your browser&rsquo;s Print for a PDF \u2014 printing expands every domain.</p>
</footer>
<script>%s</script>
</body>
</html>
""" % (CSS, PACKBAR, tabs, idx_html, '\n'.join(pages), JS)

io.open(OUT, 'w', encoding='utf-8').write(doc)
print("wrote", OUT, len(doc), "bytes")
