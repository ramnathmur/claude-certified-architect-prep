'use strict';
// Assembles Outputs/CCAR-P_Syllabus-Course_v1.html from src/ + fragments/ + data/.
// Run: node build.js            (build, then run the gates)
//      node build.js --no-gates (build only)
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const HERE = __dirname;
const ROOT = path.resolve(HERE, '..', '..'); // the CCAR-P folder
// COURSE_OUT lets a parallel author build to a private file; the real output is only written when it is unset.
const OUT = process.env.COURSE_OUT ? path.resolve(process.env.COURSE_OUT) : path.join(ROOT, 'Outputs', 'CCAR-P_Syllabus-Course_v1.html');
const read = (p) => fs.readFileSync(p, 'utf8').replace(/\r\n/g, '\n');
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const G = JSON.parse(read(path.join(HERE, 'data', 'guide-objectives.json')));
const FACETS = JSON.parse(read(path.join(HERE, 'data', 'facets.json')));
const SIT_DEFAULT = '2026-12-03';

const SHORT = { 1: 'Solution design', 2: 'Models & prompting', 3: 'Integration', 4: 'Evaluation & testing', 5: 'Governance & safety', 6: 'Stakeholders & lifecycle', 7: 'Developer productivity' };
const DOMAINS = [1, 2, 3, 4, 5, 6, 7].map((n) => ({ n, name: G.domains[n].name, short: SHORT[n], weight: G.domains[n].weight }));
const dom = (n) => DOMAINS[n - 1];
const OBJ = G.objectives.map((o) => Object.assign({}, o, { pid: o.id.toLowerCase() }));
const objByPid = Object.fromEntries(OBJ.map((o) => [o.pid, o]));

// ----- corpus section titles (headings only) -----
const SECTIONS = {};
for (let d = 1; d <= 7; d++) {
  const md = read(path.join(ROOT, 'prep with quiz', `CCAR-P_Domain-${d}_v1.md`));
  for (const m of md.matchAll(/^## (\d+\.\d+) (.+)$/gm)) SECTIONS[m[1]] = m[2].trim();
}

// ----- fonts -----
function fontCss() {
  const cache = path.join(HERE, 'data', 'fonts.css');
  const dir = path.join(HERE, 'fonts-src');
  if (fs.existsSync(path.join(dir, 'literata'))) {
    const lit = (f) => path.join(dir, 'literata', 'pkg', 'package', 'files', f);
    const bar = (f) => path.join(dir, 'barlow', 'pkg', 'package', 'files', f);
    const faces = [
      ['Literata Course', lit('literata-latin-wght-normal.woff2'), '200 900', 'normal'],
      ['Literata Course', lit('literata-latin-wght-italic.woff2'), '200 900', 'italic'],
      ['Barlow SC Course', bar('barlow-semi-condensed-latin-400-normal.woff2'), '400', 'normal'],
      ['Barlow SC Course', bar('barlow-semi-condensed-latin-500-normal.woff2'), '500', 'normal'],
      ['Barlow SC Course', bar('barlow-semi-condensed-latin-600-normal.woff2'), '600', 'normal'],
    ];
    let css = '/* Fonts: Literata and Barlow Semi Condensed, SIL Open Font License 1.1, via Fontsource 5.3.0 (latin subset). */\n';
    for (const [fam, file, w, st] of faces) {
      css += `@font-face{font-family:"${fam}";font-style:${st};font-weight:${w};font-display:swap;src:url(data:font/woff2;base64,${fs.readFileSync(file).toString('base64')}) format("woff2")}\n`;
    }
    fs.writeFileSync(cache, css);
    return css;
  }
  return fs.existsSync(cache) ? fs.readFileSync(cache, 'utf8') : '/* fonts unavailable: system stacks apply */';
}

// ----- fragments -----
function loadFragment(id) {
  const p = path.join(HERE, 'fragments', id + '.html');
  if (!fs.existsSync(p)) return null;
  let body = read(p), meta = {};
  const m = body.match(/^<!--meta (\{[\s\S]*?\}) -->\n?/);
  if (m) { meta = JSON.parse(m[1]); body = body.slice(m[0].length); }
  return { body, meta };
}

// ----- floor plan -----
function floorPlan(writtenSet) {
  const x0 = 10, y0 = 10, iw = 880, ih = 400;
  const rowA = [1, 3, 4], rowB = [2, 5, 6, 7];
  const wt = (n) => dom(n).weight;
  const sumA = rowA.reduce((a, n) => a + wt(n), 0);
  const hA = (ih * sumA) / 100, hB = ih - hA;
  const R = {};
  let x = x0;
  rowA.forEach((n) => { const w = (iw * wt(n)) / sumA; R[n] = { x, y: y0, w, h: hA }; x += w; });
  x = x0;
  rowB.forEach((n) => { const w = (iw * wt(n)) / (100 - sumA); R[n] = { x, y: y0 + hA, w, h: hB }; x += w; });
  const f = (v) => Math.round(v * 10) / 10;
  const items = (n) => Math.round((63 * wt(n)) / 100);
  let svg = `<svg class="fp fp-draw" viewBox="0 0 900 452" role="img" aria-labelledby="fp-t fp-d"><title id="fp-t">Floor plan of the CCAR-P exam</title><desc id="fp-d">Seven rooms, one per exam domain, with floor area proportional to exam weight: Integration 19 percent, Solution design 17, Evaluation 16, Governance 14, Stakeholders 14, Models and prompting 13, Developer productivity 7. Small squares inside each room are its objectives.</desc>`;
  // rooms
  DOMAINS.forEach((d) => {
    const r = R[d.n];
    const nobj = OBJ.filter((o) => o.dom === d.n).length;
    const twoLine = d.n === 7;
    svg += `<a class="rm" href="#/d${d.n}" style="--dc:var(--d${d.n});--dci:var(--d${d.n}i);--dh:url(#h-d${d.n})" aria-label="Domain ${d.n}, ${esc(d.name)}, ${d.weight} percent"><rect class="bg" x="${f(r.x)}" y="${f(r.y)}" width="${f(r.w)}" height="${f(r.h)}"/><rect class="hatch" x="${f(r.x)}" y="${f(r.y)}" width="${f(r.w)}" height="${f(r.h)}"/>`;
    svg += `<text class="code" x="${f(r.x + 16)}" y="${f(r.y + 32)}">D${d.n}</text>`;
    if (twoLine) svg += `<text class="nm" x="${f(r.x + 16)}" y="${f(r.y + 54)}">Developer</text><text class="nm" x="${f(r.x + 16)}" y="${f(r.y + 72)}">productivity</text>`;
    else svg += `<text class="nm" x="${f(r.x + 16)}" y="${f(r.y + 54)}">${esc(d.short)}</text>`;
    svg += `<text class="wt" x="${f(r.x + 16)}" y="${f(r.y + 116)}">${d.weight}%</text>`;
    svg += `<text class="sub" x="${f(r.x + 16)}" y="${f(r.y + 136)}">${nobj} objectives</text><text class="sub" x="${f(r.x + 16)}" y="${f(r.y + 152)}">about ${items(d.n)} items</text></a>`;
  });
  // walls with door gaps
  const yDiv = y0 + hA, wall = [];
  const bA = [R[1].x + R[1].w, R[3].x + R[3].w];
  const bB = [R[2].x + R[2].w, R[5].x + R[5].w, R[6].x + R[6].w];
  const overlap = (a, b) => { const lo = Math.max(R[a].x, R[b].x), hi = Math.min(R[a].x + R[a].w, R[b].x + R[b].w); return (lo + hi) / 2; };
  const DW = 30;
  // doors D1-D5 and D3-D5; the D3-D5 door sits at the right end of the shared wall, clear of D3's objective squares
  const hGaps = [overlap(1, 5), Math.min(R[5].x + R[5].w - DW / 2 - 6, R[3].x + R[3].w - DW / 2)].sort((a, b) => a - b);
  let hd = '', cx = x0;
  hGaps.forEach((c) => { hd += `M${f(cx)} ${f(yDiv)}H${f(c - DW / 2)}`; cx = c + DW / 2; });
  hd += `M${f(cx)} ${f(yDiv)}H${f(x0 + iw)}`;
  const yMid = y0 + hA / 2;
  let vd = '';
  bA.forEach((bx) => { vd += `M${f(bx)} ${f(y0)}V${f(yMid - DW / 2)}M${f(bx)} ${f(yMid + DW / 2)}V${f(yDiv)}`; });
  bB.forEach((bx) => { vd += `M${f(bx)} ${f(yDiv)}V${f(y0 + ih)}`; });
  svg += `<path class="wall in" d="${hd}${vd}"/>`;
  svg += `<path class="wall" pathLength="1" d="M${x0} ${y0}H${x0 + iw}V${y0 + ih}H${x0}Z"/>`;
  // door leaves + tooltips
  const door = (title, d) => `<g class="door"><title>${esc(title)}</title><path class="leaf" d="${d}"/></g>`;
  hGaps.forEach((c, i) => {
    const g1 = c - DW / 2, g2 = c + DW / 2;
    const t = i === 0 ? 'D1 and D5: redact before the model call (1.10) is the boundary rule 5.3 applies to regulated data' : 'D3 and D5: least privilege means removal (3.2) and is scoped in 5.2';
    svg += door(t, `M${f(g1)} ${f(yDiv)}L${f(g1)} ${f(yDiv - DW)}A${DW} ${DW} 0 0 1 ${f(g2)} ${f(yDiv)}`);
  });
  [[bA[0], 'D1 and D3: wrong citations after a refresh start as a feedback signal (1.9) and are diagnosed in 3.10'], [bA[1], 'D3 and D4: the same refresh failure is the diagnosis-order case in 4.10']].forEach(([bx, t]) => {
    // the leaf swings into the room on the left, whose text sits at its far left edge
    svg += door(t, `M${f(bx)} ${f(yMid - DW / 2)}L${f(bx - DW)} ${f(yMid - DW / 2)}A${DW} ${DW} 0 0 0 ${f(bx)} ${f(yMid + DW / 2)}`);
  });
  // pips (objectives)
  DOMAINS.forEach((d) => {
    const r = R[d.n];
    OBJ.filter((o) => o.dom === d.n).forEach((o, i) => {
      const px = r.x + 16 + i * 19, py = r.y + r.h - 30;
      svg += `<a href="#/${o.pid}" style="--dc:var(--d${d.n});--dci:var(--d${d.n}i)"><rect class="pip${writtenSet.has(o.pid) ? ' w' : ''}" data-id="${o.pid}" x="${f(px)}" y="${f(py)}" width="14" height="14"/><title>${o.id} ${esc(o.text)}</title></a>`;
    });
  });
  // dimension line
  svg += `<path class="dim" d="M10 438H890M10 432V444M890 432V444"/><rect x="300" y="428" width="300" height="20" class="plate" style="opacity:1"/><text class="dimt" x="450" y="442" text-anchor="middle">100% of the 63 scored items. Floor area = exam weight.</text></svg>`;
  return svg;
}
function domList() {
  return '<ul class="dom-list">' + DOMAINS.map((d) => `<li><a href="#/d${d.n}" style="--dci:var(--d${d.n}i)"><span style="color:var(--d${d.n}i)">D${d.n}</span><span>${esc(d.short)}</span><span>${d.weight}%</span></a></li>`).join('') + '</ul>';
}

// ----- page assembly -----
const swatch = (n) => `<svg class="sw" viewBox="0 0 22 22" aria-hidden="true"><rect width="22" height="22" fill="url(#h-d${n})"/></svg>`;
function titleBlockObj(o, written, mins) {
  const secs = o.sections.map((s) => (written ? `<a href="#/${o.pid}/c${s}">${s}</a>` : s)).join(' ');
  const total = OBJ.filter((x) => x.dom === o.dom).length;
  return `<dl class="tb"><div><dt>Sheet</dt><dd>${swatch(o.dom)}D${o.dom}-${o.n}</dd></div><div><dt>Exam weight</dt><dd>${dom(o.dom).weight}%</dd></div><div class="wide"><dt>Domain</dt><dd class="dn"><a href="#/d${o.dom}">${esc(dom(o.dom).name)}</a></dd></div><div class="wide"><dt>Corpus sections</dt><dd class="secs">${secs}</dd></div><div><dt>Reading time</dt><dd>${written ? '&#8776; ' + mins + ' min' : 'not written'}</dd></div><div><dt>Position</dt><dd>${o.n} of ${total} in D${o.dom}</dd></div>${written ? `<div class="wide"><button class="readbtn" type="button" data-read="${o.pid}" aria-pressed="false"><span class="bx"><svg viewBox="0 0 14 14" fill="none" stroke-width="2.4" aria-hidden="true"><path d="M2 7.5L5.5 11L12 3.5"/></svg></span>Mark as read</button></div>` : `<div class="wide"><dt>Status</dt><dd style="font-size:1rem">Not written yet</dd></div>`}</dl>`;
}
function titleBlockDom(d) {
  const n = OBJ.filter((o) => o.dom === d.n).length;
  return `<dl class="tb"><div><dt>Domain</dt><dd>${swatch(d.n)}D${d.n}</dd></div><div><dt>Exam weight</dt><dd>${d.weight}%</dd></div><div><dt>Objectives</dt><dd>${n}</dd></div><div><dt>Scored items</dt><dd>about ${Math.round((63 * d.weight) / 100)}</dd></div><div class="wide"><dt>Guide</dt><dd style="font-size:1rem">v1.0, section 6</dd></div></dl>`;
}
function objList(n) {
  return '<ul class="objlist">' + OBJ.filter((o) => o.dom === n).map((o) => `<li><a href="#/${o.pid}"><span class="oid">${o.id}</span><span>${esc(o.text)}</span><span class="st" data-st="${o.pid}">Not written yet</span></a></li>`).join('') + '</ul>';
}
function stubBody(o) {
  return `<div class="wide-col"><div class="note"><p><b>This sheet is not written yet.</b> The heading above is the guide&#8217;s own wording. When the sheet is written it will teach these corpus sections:</p></div><ul class="objlist">${o.sections.map((s) => `<li><span style="display:grid;grid-template-columns:3.4rem 1fr;gap:14px;padding:9px 6px"><span class="oid">${s}</span><span>${esc(SECTIONS[s] || '')}</span></span></li>`).join('')}</ul></div>`;
}
function stubDomBody(n) {
  return `<div class="wide-col"><div class="note"><p><b>The opening page for this domain is not written yet.</b> The objectives below are the guide&#8217;s wording, in guide order.</p></div>${objList(n)}</div>`;
}
const text = (html) => html.replace(/<details class="deeper"[\s\S]*?<\/details>/g, ' ').replace(/<svg[\s\S]*?<\/svg>/g, ' ').replace(/<[^>]+>/g, ' ').replace(/&[#\w]+;/g, ' ').replace(/\s+/g, ' ').trim();
const words = (html) => (text(html).match(/[\p{L}\p{N}][\p{L}\p{N}'’.%-]*/gu) || []).length;

const FRONT = [
  ['start', 'Start here'], ['exam', 'The exam on one page'], ['plan', 'Month plan'],
];
const BACK = [['traps', 'Trap families'], ['glossary', 'Glossary'], ['coverage', 'Coverage'], ['sources', 'Sources and version']];

const pages = []; // {id, kind, dom, title, oid?, written, html, words, sections?}
function addFront(id, title) { pages.push({ id, kind: id === 'start' || id === 'exam' || id === 'plan' ? 'front' : 'back', dom: 0, title }); }
FRONT.forEach(([id, t]) => addFront(id, t));
DOMAINS.forEach((d) => {
  pages.push({ id: 'd' + d.n, kind: 'dom', dom: d.n, title: `D${d.n} ${d.short}`, full: d.name });
  OBJ.filter((o) => o.dom === d.n).forEach((o) => pages.push({ id: o.pid, kind: 'obj', dom: d.n, title: o.text, oid: o.id, sections: o.sections }));
});
BACK.forEach(([id, t]) => addFront(id, t));

// first pass: which pages have fragments
pages.forEach((p) => { p.frag = loadFragment(p.id); p.written = !!p.frag || ['glossary', 'coverage'].includes(p.id); });
const writtenObj = new Set(pages.filter((p) => p.kind === 'obj' && p.frag).map((p) => p.id));

// helper data harvested from written fragments
const harvest = { sections: new Set(), facets: new Set(), dfns: [], dup: [] };
pages.forEach((p) => {
  if (!p.frag) return;
  for (const m of p.frag.body.matchAll(/data-src="(\d+\.\d+)"/g)) harvest.sections.add(m[1]);
  for (const m of p.frag.body.matchAll(/data-facet="(F-\d+\.\d+-\d+)"/g)) harvest.facets.add(m[1]);
  for (const m of p.frag.body.matchAll(/<dfn data-def="([^"]*)">([^<]+)<\/dfn>/g)) harvest.dfns.push({ term: m[2], def: m[1], page: p.id });
});

const FAM_DEF = {
  'f-half-move': 'HALF-MOVE: correct as far as it goes, but it leaves a stated requirement untouched.',
  'f-wrong-axis': 'WRONG-AXIS: a real technique applied to the wrong dimension of the problem.',
  'f-repair': 'REPAIR: rebuilds downstream what an earlier step should have done cleanly.',
  'f-discard': 'DISCARD: replaces or throws away something the scenario still needs.',
  'f-architected': 'ARCHITECTED: sounds like the mature, more thorough design but does not solve the problem the stem states.',
  'f-overspec': 'OVERSPEC: the strength of the guarantee does not match the requirement.',
  'f-evidence-mismatch': 'EVIDENCE-MISMATCH: offers a cause the evidence in the stem does not support or already rules out.',
  'f-detective-for-preventive': 'DETECTIVE-FOR-PREVENTIVE: detects or confirms a misuse where the requirement is to remove the capability.',
};
const LBL_DEF = {
  Known: 'Known: stated in the guide or another Anthropic source.',
  Inference: 'Inference: reasoned from known facts, not stated by a source.',
  Uncertain: 'Uncertain: not settled by any source.',
  Recommended: 'Recommended: advice, not a fact about the exam.',
  'Not published': 'Not published: the guide does not say.',
  'Design shape': 'Design shape: a scenario from this project’s corpus.',
  Ask: 'The question to ask against this family of wrong options.',
};
function macros(html, p) {
  html = html
    .replace(/<a class="fam" href="#\/traps\/(f-[a-z-]+)">/g, (m, id) => `<a class="fam" href="#/traps/${id}" title="${esc(FAM_DEF[id] || '')}">`)
    .replace(/<span class="lbl">([^<:]+)(:?)<\/span>/g, (m, t, c) => (LBL_DEF[t] ? `<span class="lbl" title="${esc(LBL_DEF[t])}">${t}${c}</span>` : m));
  return html
    .replace(/\{\{FLOORPLAN\}\}/g, () => `<div class="fp-wrap"><div class="planwrap">${floorPlan(writtenObj)}</div>${domList()}</div>`)
    .replace(/\{\{OBJLIST\}\}/g, () => objList(p.dom))
    .replace(/\{\{WRITTEN\}\}/g, String(writtenObj.size))
    .replace(/\{\{SEC:(\d+\.\d+)\}\}/g, (_, s) => esc(SECTIONS[s] || s));
}

function glossaryBody() {
  const items = harvest.dfns.slice().sort((a, b) => a.term.toLowerCase().localeCompare(b.term.toLowerCase()));
  if (!items.length) return '<p>No terms have been defined yet.</p>';
  return `<p class="muted">Each term is defined once, where it first matters. ${items.length} so far.</p><dl class="gloss">` + items.map((i) => `<dt>${esc(i.term)}</dt><dd>${esc(i.def)} <a href="#/${i.page}">${esc(pages.find((x) => x.id === i.page).oid || pages.find((x) => x.id === i.page).title)}</a></dd>`).join('') + '</dl>';
}
function coverageBody() {
  const rows = DOMAINS.map((d) => {
    const secs = Object.keys(SECTIONS).filter((s) => s.startsWith(d.n + '.') && Number(s.split('.')[0]) === d.n);
    const fac = secs.reduce((a, s) => a.concat(FACETS[s] || []), []);
    const sc = secs.filter((s) => harvest.sections.has(s)).length, fc = fac.filter((f) => harvest.facets.has(f)).length;
    const pct = fac.length ? Math.round((100 * fc) / fac.length) : 0;
    return `<tr style="--dc:var(--d${d.n})"><td>D${d.n} ${esc(d.short)}</td><td class="num">${sc} of ${secs.length}</td><td class="num">${fc} of ${fac.length}</td><td><span class="bar" style="--p:${pct}%"></span></td></tr>`;
  }).join('');
  const allSecs = Object.keys(SECTIONS), allFac = Object.values(FACETS).flat();
  const gaps = [];
  pages.filter((p) => p.kind === 'obj' && p.frag).forEach((p) => {
    const miss = p.sections.flatMap((s) => FACETS[s] || []).filter((f) => !harvest.facets.has(f));
    if (miss.length) gaps.push(`${p.oid}: ${miss.join(', ')}`);
  });
  return `<p>This page is generated by the build from the chapters themselves. A corpus section counts as covered when a chapter has a section block tagged with it. A facet is one testable decision in the corpus (a situation, the right answer and the reason), and it counts as covered when a rule in a chapter is tagged with its ID.</p>
<table class="tbl"><thead><tr><th>Domain</th><th>Sections</th><th>Facets</th><th>Done</th></tr></thead><tbody>${rows}<tr><td>All domains</td><td class="num">${harvest.sections.size} of ${allSecs.length}</td><td class="num">${harvest.facets.size} of ${allFac.length}</td><td></td></tr></tbody></table>
<h2>Anchor check</h2><p>The 38 objective headings and the 7 domain weights are copied from the official exam guide PDF by script, not typed. PDF fingerprint (SHA-256): <code>${G.sha256.slice(0, 16)}&#8230;</code>. Guide v1.0, July 2026. Built ${new Date().toISOString().slice(0, 10)}.</p>
<h2>Gaps inside written chapters</h2>${gaps.length ? `<div class="note red"><p>${gaps.map(esc).join('<br>')}</p></div>` : '<p>None. Every facet of every written chapter appears in it.</p>'}`;
}

function assemble(p) {
  const frag = p.frag;
  const isStub = !frag && p.kind !== 'back';
  let inner = frag ? frag.body : '';
  let head = '';
  const fm = frag ? frag.meta : {};
  if (p.kind === 'obj') {
    const o = objByPid[p.id];
    const wc = frag ? words(inner) : 0;
    p.words = wc; p.mins = Math.max(1, Math.round(wc / 200));
    head = `<header class="head"><h1 data-objective="${o.id}">${esc(o.text)}</h1>${titleBlockObj(o, !!frag, p.mins)}</header>`;
    if (!frag) inner = stubBody(o);
  } else if (p.kind === 'dom') {
    const d = dom(p.dom);
    const wc = frag ? words(inner) : 0;
    p.words = wc; p.mins = Math.max(1, Math.round(wc / 200));
    head = `<header class="head"><h1 data-domain="${d.n}">${esc(d.name)}</h1>${titleBlockDom(d)}</header>`;
    if (!frag) inner = stubDomBody(d.n);
  } else {
    let body = inner;
    if (p.id === 'glossary') body = `<div class="wide-col">${glossaryBody()}</div>`;
    if (p.id === 'coverage') body = `<div class="wide-col">${coverageBody()}</div>`;
    inner = body;
    const wc = words(inner);
    p.words = wc; p.mins = Math.max(1, Math.round(wc / 200));
    const h1cls = fm.xl ? ' class="xl"' : '';
    head = `<header class="head solo"><div><h1${h1cls}>${esc(fm.h1 || p.title)}</h1>${fm.lede ? `<p class="lede">${fm.lede}</p>` : ''}</div></header>`;
  }
  inner = macros(inner, p);
  p.written = !!frag || p.id === 'glossary' || p.id === 'coverage';
  const writtenAttr = p.kind === 'obj' || p.kind === 'dom' ? (frag ? '1' : '0') : '1';
  return `<section class="page" data-id="${p.id}" data-kind="${p.kind}" data-dom="${p.dom}" data-written="${writtenAttr}" data-min="${p.mins || 0}" data-title="${esc(p.title)}"><div class="sheet"><div class="sheet-in">${head}${inner}<div class="endmark" data-end="${p.id}"></div></div></div></section>\n`;
}

// glossary and coverage depend on harvest, so assemble them last-but-in-order
let main = '';
pages.forEach((p) => { main += assemble(p); });

const tabs = DOMAINS.map((d) => `<a href="#/d${d.n}" data-dom="${d.n}" style="--w:${(d.weight / 19).toFixed(3)};--dc:var(--d${d.n})" title="Domain ${d.n}: ${esc(d.name)} (${d.weight}%)">D${d.n}</a>`).join('');
const courseJson = JSON.stringify({
  domains: DOMAINS,
  sitDefault: SIT_DEFAULT,
  pages: pages.map((p) => ({ id: p.id, kind: p.kind, dom: p.dom, title: p.title, oid: p.oid || null, written: p.kind === 'obj' || p.kind === 'dom' ? !!p.frag : true, sections: p.sections || null })),
}).replace(/</g, '\\u003c');

let head = read(path.join(HERE, 'src', 'head.html')).replace('/*FONTS*/', () => fontCss()).replace('{{TABS}}', () => tabs);
let foot = read(path.join(HERE, 'src', 'foot.html')).replace('{{COURSE_JSON}}', () => courseJson);
const html = head + main + foot;
fs.writeFileSync(OUT, html, 'utf8');

const writtenN = pages.filter((p) => p.kind === 'obj' && p.frag).length;
pages.filter((p) => p.frag && p.words).forEach((p) => {
  const body = p.frag.body;
  const share = (re) => { const m = body.match(re); return m ? words(m[0]) : 0; };
  const asideW = share(/<aside class="remember"[\s\S]*?<\/aside>/), bitesW = share(/<section class="bites"[\s\S]*?<\/section>/), xlW = share(/<nav class="xlinks"[\s\S]*?<\/nav>/), sayW = share(/<details class="say"[\s\S]*?<\/details>/);
  const rulesW = (body.match(/<ul class="rules"[\s\S]*?<\/ul>/g) || []).reduce((a, r) => a + words(r), 0);
  console.log(`  ${p.id.padEnd(6)} ${String(p.words).padStart(5)} words  (rules ${rulesW}, exam block ${bitesW}, remember ${asideW}, say-it-back ${sayW}, connections ${xlW}, prose and rest ${p.words - rulesW - bitesW - asideW - sayW - xlW})`);
});
console.log(`built ${path.relative(ROOT, OUT)}  ${(html.length / 1024).toFixed(0)} KB  pages=${pages.length}  objectives written=${writtenN}/38`);
if (!process.argv.includes('--no-gates')) {
  const r = spawnSync(process.execPath, [path.join(HERE, 'gates.js')], { stdio: 'inherit', env: Object.assign({}, process.env, { COURSE_FILE: OUT }) });
  process.exit(r.status || 0);
}
