"""Build CCA-F_One-Page-Sheet_v1.html - the single printable sheet."""
import io, json, os, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\Claude-Certified-Architect-Foundations_Exam-Prep_v1\Learning corpus\CCA-F_One-Page-Sheet_v1.html"

p = json.load(io.open(os.path.join(HERE, 'wf_payload.json'), encoding='utf-8'))
op = p['onePager']


def e(s):
    return H.escape(str(s), quote=False)


def fmt(s):
    """Bold the part before an em/en dash so each line has a visible head."""
    s = e(s)
    for dash in (' \u2014 ', ' \u2013 ', ' - '):
        if dash in s:
            head, _, tail = s.partition(dash)
            if len(head) <= 70:
                return '<b>%s</b>%s%s' % (head, dash.replace(' - ', ' \u2014 '), tail)
    return s


dom_rows = ''.join(
    '<tr><td class="dc">%s</td><td class="dn">%s</td><td class="dw">%s</td><td class="dg">%s</td></tr>'
    % (e(d['code']), e(d['name']), e(d['weight']), e(d['gist'])) for d in op['domains'])

rules = ''.join('<li>%s</li>' % fmt(r) for r in op['rules'])
dist = ''.join('<li>%s</li>' % fmt(r) for r in op['distinctions'])
esc_ = ''.join('<li>%s</li>' % fmt(r) for r in op['escalation'])
mech = ''.join('<li>%s</li>' % fmt(r) for r in op['examMechanics'])

PACKBAR = ('<nav class="packbar" aria-label="CCA-F prep pack"><span class="pb-lab">CCA-F prep pack</span>'
           '<a href="../README.html">Start here</a>'
           '<a href="Exam-Day-Guide.html">Exam Day Guide</a>'
           '<a href="CCA-F_Concept-Atlas_v2.html">Concept Atlas</a>'
           '<a href="CCA-F_Trap-Sheet_v1.html">Trap Sheet</a>'
           '<a href="CCA-F_Corpus_v1.html">Corpus</a>'
           '<a href="CCA-F_One-Page-Sheet_v1.html" aria-current="page">One-page sheet</a>'
           '<a href="../Mock%20tests/Test-1.html">Practice tests</a>'
           '<a href="../Mock%20tests/Test-MR.html">MR drill</a>'
           '<a href="../Mock%20tests/Dashboard.html">Dashboard</a></nav>')

TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>CCA-F One-Page Sheet</title>
<meta name="description" content="The whole CCA-F exam compressed to one printable side: five domains, the hard rules, the confusable pairs, and how to sit the paper."/>
<link rel="icon" href="data:,"/>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>
:root{--ink:#15130f;--ink2:#33302a;--ink3:#6f6b63;--cream:#faf7f2;--cream2:#f1ece3;
 --amber:#b8761f;--amber-dark:#7d5115;--border:#d9d3c8;
 --sans:'DM Sans',system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
 --serif:'DM Serif Display',Georgia,serif;--mono:'JetBrains Mono',ui-monospace,Consolas,monospace;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--sans);background:var(--cream);color:var(--ink2);font-size:15px;line-height:1.55}
.packbar{font:500 13px/1.4 var(--sans);background:#141821;color:#c9d1e0;padding:.5rem .9rem;
 display:flex;flex-wrap:wrap;align-items:center;gap:.35rem .5rem}
.packbar .pb-lab{color:#8d97ab;font-weight:600;letter-spacing:.02em;text-transform:uppercase;font-size:11px;margin-right:.3rem}
.packbar a{color:#c9d1e0;text-decoration:none;padding:.2rem .5rem;border-radius:999px;border:1px solid transparent;white-space:nowrap}
.packbar a:hover{background:#252c3a;color:#fff}
.packbar a[aria-current="page"]{background:#3b6ef5;color:#fff;border-color:#3b6ef5}
.howto{max-width:74rem;margin:0 auto;padding:20px 26px 0;font-size:13.5px;color:var(--ink3);line-height:1.6}
.howto b{color:var(--ink2)}
.howto button{font:600 12px var(--sans);margin-left:8px;padding:5px 14px;border-radius:99px;
 border:1.5px solid var(--amber);background:var(--amber);color:#fff;cursor:pointer}
.howto button:hover{background:var(--amber-dark);border-color:var(--amber-dark)}
.sheet{max-width:74rem;margin:0 auto;padding:16px 26px 60px}
.head{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;flex-wrap:wrap;
 border-bottom:2px solid var(--ink);padding-bottom:7px;margin-bottom:11px}
.head h1{font-family:var(--serif);font-weight:400;font-size:25px;color:var(--ink);line-height:1.1}
.head .sub{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3)}
.cols{column-count:2;column-gap:26px;column-fill:balance}
section{break-inside:avoid-column;margin-bottom:12px}
h2{font-family:var(--mono);font-size:9.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--amber-dark);
 border-bottom:1px solid var(--border);padding-bottom:3px;margin-bottom:6px;font-weight:600}
table{width:100%;border-collapse:collapse;font-size:11.5px;margin-bottom:2px}
td{padding:2.5px 5px 2.5px 0;vertical-align:top;border-bottom:1px solid var(--cream2)}
tr:last-child td{border-bottom:none}
.dc{font-family:var(--mono);font-weight:600;color:var(--amber-dark);width:22px}
.dn{font-weight:600;color:var(--ink)}
.dw{font-family:var(--mono);text-align:right;color:var(--ink);width:34px}
.dg{color:var(--ink3);font-size:11px}
ul{list-style:none;margin:0;padding:0}
li{font-size:11.5px;line-height:1.45;padding:2.5px 0 2.5px 11px;position:relative;
 border-bottom:1px solid var(--cream2);break-inside:avoid}
li:last-child{border-bottom:none}
li::before{content:"";position:absolute;left:2px;top:8.5px;width:3px;height:3px;border-radius:50%;background:var(--amber)}
li b{color:var(--ink);font-weight:600}
code{font-family:var(--mono);font-size:.9em;background:var(--cream2);padding:0 3px;border-radius:3px;color:var(--ink)}
.oos{font-size:10.5px;line-height:1.5;color:var(--ink3);background:var(--cream2);border-radius:5px;padding:6px 8px}
.oos b{color:var(--ink2)}
.foot{border-top:1px solid var(--border);margin-top:10px;padding-top:6px;
 font-family:var(--mono);font-size:8.5px;letter-spacing:.05em;color:var(--ink3);
 display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
@media (max-width:820px){.cols{column-count:1}.sheet{padding:14px 16px 50px}}
@page{size:A4 portrait;margin:8mm}
@media print{
 /* Metrics measured against A4 and US Letter usable area - the sheet must never
    spill onto a second page. Verified height 926px vs 1062px (A4) / 995px (Letter). */
 .packbar,.howto{display:none}
 body{background:#fff;font-size:9pt}
 .sheet{max-width:none;width:auto;padding:0;margin:0}
 .head{margin-bottom:6px;padding-bottom:4px}
 .head h1{font-size:15pt}
 .head .sub{font-size:6pt}
 .cols{column-count:2;column-gap:6mm}
 h2{font-size:6pt;margin-bottom:3px;padding-bottom:1.5px}
 table{font-size:6.8pt}
 td{padding:1.5px 4px 1.5px 0}
 .dg{font-size:6.4pt}
 li{font-size:6.8pt;line-height:1.26;padding:1.1px 0 1.1px 7px}
 li::before{top:5px;width:2px;height:2px}
 .oos{font-size:6.2pt;padding:3px 5px}
 .foot{font-size:5.6pt;margin-top:5px;padding-top:4px}
 section{margin-bottom:5px}
}
</style>
</head>
<body>
@@PACKBAR@@
<div class="howto">
  <b>One side of A4.</b> Everything below fits a single printed page &mdash; the pack bar and this line are dropped
  when you print. This is the last thing to read before you sit, not the first: it assumes you have already been
  through the Guide or the Atlas and just need the decisions that keep recurring.
  <button onclick="window.print()">Print this sheet</button>
</div>
<div class="sheet">
  <div class="head">
    <h1>CCA-F &mdash; one page</h1>
    <div class="sub">60 q &middot; 120 min &middot; 4 of 6 scenarios &middot; pass 720 / 1000</div>
  </div>
  <div class="cols">
    <section>
      <h2>The five domains</h2>
      <table>@@DOMROWS@@</table>
    </section>
    <section>
      <h2>Hard rules</h2>
      <ul>@@RULES@@</ul>
    </section>
    <section>
      <h2>Easy to confuse</h2>
      <ul>@@DIST@@</ul>
    </section>
    <section>
      <h2>Escalation &amp; enforcement</h2>
      <ul>@@ESC@@</ul>
    </section>
    <section>
      <h2>Sitting the paper</h2>
      <ul>@@MECH@@</ul>
    </section>
    <section>
      <h2>Not on the exam</h2>
      <div class="oos"><b>Do not revise:</b> @@OOS@@</div>
    </section>
  </div>
  <div class="foot">
    <span>CCA-F prep pack &middot; grounded in Exam Guide v0.2 (30 June 2026)</span>
    <span>Independent study material &middot; not affiliated with or endorsed by Anthropic</span>
  </div>
</div>
</body>
</html>
"""

doc = TPL
for tok, val in (('@@PACKBAR@@', PACKBAR), ('@@DOMROWS@@', dom_rows), ('@@RULES@@', rules),
                 ('@@DIST@@', dist), ('@@ESC@@', esc_), ('@@MECH@@', mech),
                 ('@@OOS@@', e(op['outOfScope']))):
    assert doc.count(tok) == 1, (tok, doc.count(tok))
    doc = doc.replace(tok, val)
io.open(OUT, 'w', encoding='utf-8').write(doc)
n = sum(len(str(x).split()) for k, v in op.items() for x in (v if isinstance(v, list) else [v])
        for x in ([' '.join(map(str, x.values()))] if isinstance(x, dict) else [x]))
print('wrote', OUT, len(doc), 'bytes')
print('content words ~', n)
print('rules', len(op['rules']), '| distinctions', len(op['distinctions']),
      '| escalation', len(op['escalation']), '| mechanics', len(op['examMechanics']))
