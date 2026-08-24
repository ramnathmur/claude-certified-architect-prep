"""Wire the seven practice tests into the pack: nav bar, live citation links, study routes."""
import io, os, glob, re

D = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\Claude-Certified-Architect-Foundations_Exam-Prep_v1\Mock tests"

PACKBAR_CSS = """<style id="packbar-css">
.packbar{font:500 13px/1.4 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 background:#141821;color:#c9d1e0;padding:.5rem .9rem;display:flex;flex-wrap:wrap;align-items:center;gap:.35rem .5rem}
.packbar .pb-lab{color:#8d97ab;font-weight:600;letter-spacing:.02em;text-transform:uppercase;font-size:11px;margin-right:.3rem}
.packbar a{color:#c9d1e0;text-decoration:none;padding:.2rem .5rem;border-radius:999px;border:1px solid transparent;white-space:nowrap}
.packbar a:hover{background:#252c3a;color:#fff}
.packbar a[aria-current="page"]{background:#3b6ef5;color:#fff;border-color:#3b6ef5}
.fb-row .cite a{color:var(--amber-dark);text-decoration:none;border-bottom:1px dotted currentColor}
.fb-row .cite a:hover{color:var(--amber);border-bottom-style:solid}
.rc-study{margin-top:9px;padding-top:8px;border-top:1px solid rgba(250,247,242,0.13);
 font-family:var(--mono);font-size:9.5px;letter-spacing:.04em;color:rgba(250,247,242,0.45);line-height:1.9}
.rc-study a{color:rgba(250,247,242,0.78);text-decoration:none;border-bottom:1px solid rgba(250,247,242,0.25)}
.rc-study a:hover{color:#fff;border-bottom-color:#fff}
.res-card.weak{border-color:rgba(232,120,90,0.55);background:rgba(232,120,90,0.09)}
.res-card.weak .rc-study{color:rgba(250,247,242,0.6)}
@media print{.packbar{display:none}}
</style>"""

PACKBAR_NAV = ('<nav class="packbar" aria-label="CCA-F prep pack"><span class="pb-lab">CCA-F prep pack</span>'
               '<a href="../README.html">Start here</a>'
               '<a href="../Learning%20corpus/Exam-Day-Guide.html">Exam Day Guide</a>'
               '<a href="../Learning%20corpus/CCA-F_Concept-Atlas_v2.html">Concept Atlas</a>'
               '<a href="../Learning%20corpus/CCA-F_Trap-Sheet_v1.html">Trap Sheet</a>'
               '<a href="../Learning%20corpus/CCA-F_Corpus_v1.html">Corpus</a>'
               '<a href="Test-1.html" aria-current="page">Practice tests</a>'
               '<a href="Dashboard.html">Dashboard</a></nav>')

OLD_FBROW = ('function fbRow(cls,label,ref,txt,cite){\n'
             '  return `<div class="fb-row ${cls}"><div class="lbl">${label}${ref?`<span class="opt-ref">${ref}</span>`:""}</div>'
             '<div class="txt">${code(txt)}</div>${cite?`<div class="cite">Source: ${esc(cite)}</div>`:""}</div>`;\n'
             '}')

NEW_FBROW = ('function citeHref(cite){\n'
             '  const m=/\\u00a7\\s*(\\d+)\\.(\\d+)/.exec(cite||"");\n'
             '  return m?`../Learning%20corpus/CCA-F_Corpus_v1.html#s-${m[1]}-${m[2]}`:"";\n'
             '}\n'
             'function fbRow(cls,label,ref,txt,cite){\n'
             '  let citeBlock="";\n'
             '  if(cite){\n'
             '    const href=citeHref(cite);\n'
             '    citeBlock = href\n'
             '      ? `<div class="cite">Source: <a href="${href}" target="_blank" rel="noopener" title="Open this section of the corpus">${esc(cite)}</a></div>`\n'
             '      : `<div class="cite">Source: ${esc(cite)}</div>`;\n'
             '  }\n'
             '  return `<div class="fb-row ${cls}"><div class="lbl">${label}${ref?`<span class="opt-ref">${ref}</span>`:""}</div>'
             '<div class="txt">${code(txt)}</div>${citeBlock}</div>`;\n'
             '}')

OLD_GRID = ('  let grid=DOM_ORDER.map(d=>{\n'
            '    const c=perDom[d];const pct=Math.round(c.correct/c.of*100);\n'
            '    return `<div class="res-card"><div class="rc-name">${d} \u00b7 ${esc(DATA.domainNames[d])}</div>'
            '<div class="rc-score">${c.correct}/${c.of}</div><div class="rc-pct">${pct}%</div></div>`;\n'
            '  }).join("");')

NEW_GRID = ('  let grid=DOM_ORDER.map(d=>{\n'
            '    const c=perDom[d];const pct=Math.round(c.correct/c.of*100);\n'
            '    const k=d.toLowerCase();\n'
            '    const study=`<div class="rc-study">Study this: '
            '<a href="../Learning%20corpus/Exam-Day-Guide.html#${k}">Guide</a> \u00b7 '
            '<a href="../Learning%20corpus/CCA-F_Concept-Atlas_v2.html#${k}">Atlas</a> \u00b7 '
            '<a href="../Learning%20corpus/CCA-F_Trap-Sheet_v1.html#p-${k}">Traps</a> \u00b7 '
            '<a href="../Learning%20corpus/CCA-F_Corpus_v1.html#p-${k}">Corpus</a></div>`;\n'
            '    return `<div class="res-card${pct<70?\' weak\':\'\'}"><div class="rc-name">${d} \u00b7 ${esc(DATA.domainNames[d])}</div>'
            '<div class="rc-score">${c.correct}/${c.of}</div><div class="rc-pct">${pct}%</div>${study}</div>`;\n'
            '  }).join("");')

OLD_CAVEAT = ('<p class="caveat">This scaled figure is a linear approximation. The real exam uses psychometric '
              'scaling across equated forms, so treat it as a rough gauge, not a prediction.</p>')
NEW_CAVEAT = (OLD_CAVEAT +
              '\n    <p class="caveat">Any domain below 70% is marked. Follow its <b>Study this</b> links \u2014 they open '
              'that domain in the Guide, the Atlas, the Trap Sheet and the Corpus. Every <b>Source</b> line in the '
              'question feedback above is also a live link into the corpus section it cites.</p>')

report = []
for path in sorted(glob.glob(os.path.join(D, 'Test-*.html'))):
    name = os.path.basename(path)
    s = io.open(path, encoding='utf-8').read()
    orig = s
    done, missed = [], []

    if 'packbar-css' not in s:
        s = s.replace('</head>', PACKBAR_CSS + '\n</head>', 1)
        j = s.find('>', s.find('<body'))
        s = s[:j + 1] + '\n' + PACKBAR_NAV + '\n' + s[j + 1:]
        done.append('packbar')
    else:
        missed.append('packbar already present')

    for label, old, new in (('cite-links', OLD_FBROW, NEW_FBROW),
                            ('study-links', OLD_GRID, NEW_GRID),
                            ('caveat', OLD_CAVEAT, NEW_CAVEAT)):
        n = s.count(old)
        if n == 1:
            s = s.replace(old, new, 1)
            done.append(label)
        else:
            missed.append('%s x%d' % (label, n))

    if s != orig:
        io.open(path, 'w', encoding='utf-8').write(s)
    report.append((name, done, missed))

for name, done, missed in report:
    flag = 'OK  ' if not missed else 'WARN'
    print('%s %-14s applied=%s%s' % (flag, name, ','.join(done), ('  MISSED=' + ','.join(missed)) if missed else ''))
