'use strict';
// Mechanical gates for the built course file. Exit code 1 if any FAIL.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const HERE = __dirname;
const ROOT = path.resolve(HERE, '..', '..');
// COURSE_FILE points the gates at a private build; GATE_PAGES (comma-separated page ids) limits the page-level checks to those pages.
const FILE = process.env.COURSE_FILE ? path.resolve(process.env.COURSE_FILE) : path.join(ROOT, 'Outputs', 'CCAR-P_Syllabus-Course_v1.html');
const ONLY = process.env.GATE_PAGES ? new Set(process.env.GATE_PAGES.split(',').map((s) => s.trim().toLowerCase())) : null;
const sel = (p) => !ONLY || ONLY.has(p.id);
const PDF = path.join(ROOT, 'sources', 'CCAR-P_Official-Exam-Guide_v1.0.pdf');
const html = fs.readFileSync(FILE, 'utf8');
const htmlNoScript = html.replace(/<script[\s\S]*?<\/script>/g, '');
const FACETS = JSON.parse(fs.readFileSync(path.join(HERE, 'data', 'facets.json'), 'utf8'));
const GUIDE = JSON.parse(fs.readFileSync(path.join(HERE, 'data', 'guide-objectives.json'), 'utf8'));

const results = [];
const rec = (gate, status, msg) => results.push({ gate, status, msg });
const norm = (s) => s.toLowerCase().replace(/&amp;/g, '&').replace(/[^a-z0-9]+/g, ' ').trim();
const strip = (s) => s.replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#8217;/g, '\u2019').replace(/&#8776;/g, '\u2248').replace(/&nbsp;/g, ' ').replace(/&[#\w]+;/g, ' ').replace(/\s+/g, ' ').trim();

// ---------- split into pages ----------
const starts = [...html.matchAll(/<section class="page" data-id="([^"]+)"([^>]*)>/g)];
const mainEnd = html.indexOf('</main>');
const pages = starts.map((m, i) => {
  const end = i + 1 < starts.length ? starts[i + 1].index : mainEnd;
  const attrs = m[2];
  return { id: m[1], kind: (attrs.match(/data-kind="([^"]+)"/) || [])[1], dom: +(attrs.match(/data-dom="(\d+)"/) || [])[1], written: /data-written="1"/.test(attrs), html: html.slice(m.index, end) };
});
const byId = Object.fromEntries(pages.map((p) => [p.id, p]));

// ---------- 1. ANCHOR: objectives + weights vs the PDF ----------
function pdfObjectives() {
  let txt;
  for (const exe of ['pdftotext', 'C:\\Program Files\\Git\\mingw64\\bin\\pdftotext.exe']) {
    try { txt = execFileSync(exe, ['-layout', PDF, '-'], { encoding: 'latin1', maxBuffer: 20 * 1024 * 1024 }); break; } catch (e) { /* next */ }
  }
  if (!txt) throw new Error('pdftotext unavailable');
  txt = txt.replace(/\r/g, '');
  const seg = txt.split('Detailed objectives by domain')[1].split('7. How to Prepare')[0].replace(/Claude Certification Program\s+Exam guide/g, '');
  const doms = {}, objs = [];
  let d = null, open = false;
  for (const line of seg.split('\n')) {
    const s = line.trim().replace(/\u00ad/g, '');
    if (!s) continue;
    const m = s.match(/^Domain (\d): (.*?) \((\d+)%\)$/);
    if (m) { d = +m[1]; doms[d] = { name: m[2], weight: +m[3] }; open = false; continue; }
    if (s.startsWith('\u00b7')) { objs.push({ dom: d, t: s.replace(/^\u00b7\s*/, '') }); open = true; continue; }
    if (open) objs[objs.length - 1].t += ' ' + s;
  }
  return { doms, objs };
}
try {
  const pdf = pdfObjectives();
  const hObjs = [...html.matchAll(/<h1 data-objective="(O\d\.\d)">([\s\S]*?)<\/h1>/g)].map((m) => ({ id: m[1], t: strip(m[2]) }));
  const hDoms = [...html.matchAll(/<h1 data-domain="(\d)">([\s\S]*?)<\/h1>/g)].map((m) => ({ n: +m[1], t: strip(m[2]) }));
  let bad = [];
  if (hObjs.length !== 38) bad.push(`found ${hObjs.length} objective headings, expected 38`);
  pdf.objs.forEach((o, i) => { const h = hObjs[i]; if (!h || norm(h.t) !== norm(o.t)) bad.push(`#${i + 1} differs: pdf="${o.t}" html="${h ? h.t : '(missing)'}"`); });
  Object.keys(pdf.doms).forEach((n) => {
    const h = hDoms.find((x) => x.n === +n);
    if (!h || norm(h.t) !== norm(pdf.doms[n].name)) bad.push(`domain ${n} name differs`);
    const w = GUIDE.domains[n].weight;
    if (w !== pdf.doms[n].weight) bad.push(`domain ${n} weight data ${w} vs pdf ${pdf.doms[n].weight}`);
    const re = new RegExp(`Domain ${n}: [^"]*\\(${pdf.doms[n].weight}%\\)`);
    if (!re.test(html)) bad.push(`domain ${n} weight ${pdf.doms[n].weight}% not shown in the tab title`);
  });
  rec('anchor', bad.length ? 'FAIL' : 'PASS', bad.length ? bad.join(' | ') : `38 objective headings and 7 domain names and weights match the PDF`);
} catch (e) { rec('anchor', 'FAIL', String(e)); }

// ---------- 2. ids unique, links resolve ----------
{
  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1]);
  const dup = ids.filter((x, i) => ids.indexOf(x) !== i && !/^c\d+\.\d+$/.test(x)); // a section shared by two objectives (7.8) repeats its c-id; the router scopes anchors to the page
  rec('ids', dup.length ? 'FAIL' : 'PASS', dup.length ? 'duplicate ids: ' + [...new Set(dup)].join(', ') : `${ids.length} ids, all unique`);
  const bad = [];
  let nLinks = 0;
  for (const p of pages.filter(sel)) {
    for (const m of p.html.matchAll(/href="#\/([^"\/]+)(?:\/([^"]+))?"/g)) {
      const [, pid, anchor] = m;
      nLinks++;
      if (!byId[pid]) { bad.push(`${p.id}: #/${pid}`); continue; }
      if (anchor && byId[pid].html.indexOf(`id="${anchor}"`) < 0) bad.push(`${p.id}: #/${pid}/${anchor} (anchor not found; link to the page only if that chapter is not written yet)`);
    }
  }
  rec('links', bad.length ? 'FAIL' : 'PASS', bad.length ? 'unresolved: ' + [...new Set(bad)].join(', ') : `${nLinks} internal links resolve (page and anchor)`);
}

// ---------- 3. tag balance, page by page ----------
{
  const VOID = new Set(['meta', 'link', 'br', 'hr', 'img', 'input', 'source', 'path', 'rect', 'circle', 'line', 'polyline', 'polygon', 'ellipse', 'stop', 'use']);
  const errs = [];
  for (const p of pages.filter(sel)) {
    const body = p.html.replace(/<!--[\s\S]*?-->/g, '');
    const stack = [];
    for (const m of body.matchAll(/<(\/?)([a-zA-Z][\w:-]*)((?:"[^"]*"|'[^']*'|[^>"'])*)>/g)) {
      const [full, close, name, rest] = m; const t = name.toLowerCase();
      if (VOID.has(t) || /\/\s*$/.test(rest)) continue;
      if (!close) { stack.push({ t, at: m.index }); continue; }
      const top = stack.pop();
      if (!top || top.t !== t) { errs.push(`${p.id}: </${t}> closes ${top ? '<' + top.t + '>' : 'nothing'} near "${body.slice(Math.max(0, m.index - 50), m.index).replace(/\s+/g, ' ')}"`); break; }
    }
    if (stack.length && !errs.some((e) => e.startsWith(p.id + ':'))) errs.push(`${p.id}: unclosed ${stack.slice(-3).map((s) => '<' + s.t + '>').join(' ')}`);
  }
  rec('markup', errs.length ? 'FAIL' : 'PASS', errs.length ? errs.slice(0, 6).join(' | ') : 'tags balance in every page');
}

// ---------- 4. coverage for written objective chapters ----------
{
  const map = {};
  GUIDE.objectives.forEach((o) => { map[o.id.toLowerCase()] = o; });
  const bad = [], okc = [];
  pages.filter((p) => p.kind === 'obj' && p.written && sel(p)).forEach((p) => {
    const o = map[p.id];
    for (const s of o.sections) {
      if (!new RegExp(`<section class="concept" id="c${s.replace('.', '\\.')}" data-src="${s.replace('.', '\\.')}"`).test(p.html)) bad.push(`${o.id}: no concept block for ${s}`);
      for (const f of FACETS[s] || []) if (!p.html.includes(`data-facet="${f}"`)) bad.push(`${o.id}: facet ${f} missing`);
    }
    okc.push(o.id + ' (' + o.sections.map((s) => (FACETS[s] || []).length).reduce((a, b) => a + b, 0) + ' facets)');
  });
  rec('coverage', bad.length ? 'FAIL' : 'PASS', bad.length ? bad.join(' | ') : `written chapters cover every section and facet: ${okc.join(', ') || 'none yet'}`);
}

// ---------- 5. structure of written chapters ----------
{
  const bad = [];
  pages.filter((p) => p.kind === 'obj' && p.written && sel(p)).forEach((p) => {
    const rem = p.html.match(/<aside class="remember"[\s\S]*?<\/aside>/);
    const n = rem ? (rem[0].match(/<li>/g) || []).length : 0;
    if (!rem || n < 3 || n > 6) bad.push(`${p.id}: Remember has ${n} rules (need 3 to 6)`);
    if (!/<details class="say"/.test(p.html)) bad.push(`${p.id}: no "Say it back"`);
    if (!/class="bites"/.test(p.html)) bad.push(`${p.id}: no exam block`);
    if (!/<figure class="fig"/.test(p.html)) bad.push(`${p.id}: no figure`);
    if (!/<p class="src">/.test(p.html)) bad.push(`${p.id}: no sources footer`);
    for (const f of p.html.matchAll(/<figure class="fig"[\s\S]*?<\/figure>/g)) {
      if (!/<title[\s>][\s\S]*?<\/title>/.test(f[0]) || !/<desc[\s>][\s\S]*?<\/desc>/.test(f[0])) bad.push(`${p.id}: a figure lacks <title> or <desc>`);
    }
  });
  rec('structure', bad.length ? 'FAIL' : 'PASS', bad.length ? bad.join(' | ') : 'each written chapter has Remember (3-6), Say it back, exam block, figure with title and desc, sources footer');
}

// ---------- 6. voice lint ----------
{
  const BANNED = ['actionable', 'additionally', 'furthermore', 'moreover', 'alignment', 'best practice', 'bolster', 'foster', 'underscore', 'comprehensive', 'cutting-edge', 'game-changing', 'revolutionary', 'transformative', 'delve', 'deep dive', 'ecosystem', 'elevate', 'embark', 'journey', 'roadmap', 'ensure', 'ensuring', 'essentially', 'fundamentally', 'ultimately', 'harness', 'holistic', 'multifaceted', 'nuanced', 'intricate', 'in conclusion', 'to summarize', 'ever-evolving', 'important to note', 'worth noting', 'landscape', 'realm', 'tapestry', 'leverage', 'meticulous', 'myriad', 'plethora', 'treasure trove', 'wealth of', 'navigate', 'robust', 'seamless', 'testament to', 'under the hood', 'unlock', 'costume', 'in disguise', 'dressed up as', 'backbone', 'bolted on', 'scaffold', 'plumbing', 'load-bearing', 'great question'];
  const PATTERNS = [
    [/\bnot (just|only|merely)\b[^.?!]{0,90}\bbut\b/i, 'not just X but Y'],
    [/\b(it'?s|it is|this is) not about\b/i, "it's not about X"],
    [/\bwhether you'?re\b/i, "whether you're X or Y"],
    [/\bno longer\b[^.?!]{0,70}\b(it'?s|it is)\b/i, 'no longer X, it is Y'],
    [/\bThat (is|was) not [^.?!]{3,80}[.?!] That (is|was)\b/, 'diagnose-negate-reveal'],
    [/(^|[.!?]\s)(However|Specifically),/, 'However/Specifically opener'],
    [/!(\s|$)/, 'exclamation mark'],
    [/\p{Extended_Pictographic}/u, 'emoji'],
    [/CCAR-P_|Domain-\d_v|prep with quiz|(?<!CLAUDE|SKILL|AGENTS|\*)\.md\b|\/Outputs\//, 'file path or build commentary in the body'],
  ];
  const fails = [], warns = [];
  pages.filter((p) => p.written && sel(p) && (p.kind === 'obj' || p.kind === 'dom' || p.kind === 'front' || p.id === 'traps')).forEach((p) => {
    let h = p.html.replace(/<svg[\s\S]*?<\/svg>/g, ' ').replace(/<header class="head[\s\S]*?<\/header>/, ' ').replace(/<nav class="pager"[\s\S]*?<\/nav>/g, ' ').replace(/<p class="src">[\s\S]*?<\/p>/g, ' ').replace(/<code>[\s\S]*?<\/code>/g, ' ').replace(/<ul class="objlist"[\s\S]*?<\/ul>/g, ' ');
    if (p.id === 'plan') h = h.replace(/<div id="plan-app">[\s\S]*?<\/div>/, ' ');
    const t = strip(h);
    const lower = t.toLowerCase();
    BANNED.forEach((w) => { const re = new RegExp('\\b' + w.replace(/[-]/g, '[- ]') + '(s|ed|ing)?\\b', 'i'); if (re.test(lower)) fails.push(`${p.id}: banned "${w}"`); });
    PATTERNS.forEach(([re, name]) => { if (re.test(t)) fails.push(`${p.id}: ${name}`); });
    const em = (t.match(/\u2014/g) || []).length;
    const limit = p.kind === 'obj' || p.kind === 'dom' ? 2 : 3;
    if (em > limit) fails.push(`${p.id}: ${em} em dashes (limit ${limit})`);
    // paragraphs
    const paras = [...h.matchAll(/<p(?:\s[^>]*)?>([\s\S]*?)<\/p>/g)].map((m) => m[0]);
    let boldy = 0;
    paras.forEach((ph) => {
      const w = strip(ph).split(/\s+/).filter(Boolean).length;
      const lead = strip(ph).split(/\s+/).slice(0, 6).join(' ');
      if (w > 90) fails.push(`${p.id}: paragraph of ${w} words ("${lead}...")`); else if (w > 75) warns.push(`${p.id}: paragraph of ${w} words ("${lead}...")`);
      const nb = (ph.match(/<(b|strong)[\s>]/g) || []).length;
      if (nb > 1) fails.push(`${p.id}: ${nb} bold runs in one paragraph`);
      if (nb) boldy++;
    });
    if (paras.length > 6 && boldy / paras.length > 0.3) warns.push(`${p.id}: bold in ${Math.round((100 * boldy) / paras.length)}% of paragraphs`);
    // sentences (lists and tables are not sentences, so they are left out of this measure)
    const tS = strip(h.replace(/<table[\s\S]*?<\/table>/g, ' ').replace(/<ul class="(hero-meta|objlist|doors|dom-list)"[\s\S]*?<\/ul>/g, ' ').replace(/<ol class="chain"[\s\S]*?<\/ol>/g, ' ').replace(/<ul class="rules"[\s\S]*?<\/ul>/g, ' '));
    const sents = tS.split(/(?<=[.?!])\s+(?=[A-Z"\u201c(])/).filter((s) => s.split(/\s+/).length > 2);
    const lens = sents.map((s) => s.split(/\s+/).length);
    const avg = lens.reduce((a, b) => a + b, 0) / Math.max(1, lens.length);
    if (avg > 24) warns.push(`${p.id}: mean sentence ${avg.toFixed(1)} words`);
    lens.forEach((n, i) => { if (n > 48) warns.push(`${p.id}: sentence of ${n} words ("${sents[i].slice(0, 50)}...")`); });
  });
  rec('voice', fails.length ? 'FAIL' : 'PASS', fails.length ? fails.join(' | ') : 'no banned words, no banned constructions, em-dash and bold limits held');
  if (warns.length) rec('voice-warn', 'WARN', warns.join(' | '));
}

// ---------- 7. arithmetic ----------
{
  const bad = []; let n = 0;
  const numHtml = pages.filter(sel).map((p) => p.html).join('\n');
  for (const m of numHtml.matchAll(/<(\w+)((?:\s[^>]*)?\sdata-calc="[^"]+"[^>]*)>([\s\S]*?)<\/\1>/g)) {
    n++;
    const attrs = m[2], inner = m[3];
    const get = (k) => (attrs.match(new RegExp('\\sdata-' + k + '="([^"]*)"')) || [])[1];
    const expr = get('calc'), expect = get('expect'), round = get('round');
    if (!/^[\d\s+\-*/().%]+$/.test(expr)) { bad.push('unsafe expression ' + expr); continue; }
    let v; try { v = Function('"use strict"; return (' + expr.replace(/(\d+(?:\.\d+)?)%/g, '($1/100)') + ')')(); } catch (e) { bad.push('cannot evaluate ' + expr); continue; }
    if (round !== undefined) { const f = Math.pow(10, Number(round)); v = Math.round(v * f) / f; }
    if (Math.abs(v - Number(expect)) > 1e-6) bad.push(`${expr} = ${v}, page says ${expect}`);
    const shown = Number(strip(inner).replace(/[^\d.\-]/g, ''));
    if (!Number.isNaN(shown) && Math.abs(shown - Number(expect)) > 1e-6) bad.push(`${expr}: element shows ${strip(inner)}, expected ${expect}`);
  }
  rec('numbers', bad.length ? 'FAIL' : 'PASS', bad.length ? bad.join(' | ') : `${n} tagged calculations recomputed and match`);
}

// ---------- 8. contrast of tokens ----------
{
  const css = fs.readFileSync(path.join(HERE, 'src', 'head.html'), 'utf8');
  const block = (re) => { const m = css.match(re); const o = {}; if (m) for (const x of m[1].matchAll(/--([\w-]+):\s*(#[0-9A-Fa-f]{6})/g)) o[x[1]] = x[2]; return o; };
  const light = block(/:root\s*\{([\s\S]*?)\n\}/);
  const dark = Object.assign({}, light, block(/\[data-theme="dark"\]\s*\{([\s\S]*?)\n\}/));
  light['fixed-ink'] = '#16212B'; dark['fixed-ink'] = '#16212B'; // text on the yellow highlight is a fixed dark in both themes
  const lum = (h) => { const c = [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16) / 255).map((v) => (v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4))); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
  const cr = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
  const pairs = [['ink', 'sheet'], ['ink', 'film'], ['graphite', 'sheet'], ['graphite', 'film'], ['blue-ink', 'sheet'], ['blue-ink', 'blue-tint'], ['red-ink', 'sheet'], ['red-ink', 'red-tint'], ['ink', 'yellow-tint'], ['fixed-ink', 'yellow'], ['on-blue', 'blue'], ['on-red', 'red'], ['graphite', 'yellow-tint'], ['graphite', 'blue-tint']];
  for (let i = 1; i <= 7; i++) { pairs.push([`d${i}i`, 'sheet']); pairs.push([`d${i}i`, 'film']); }
  const bad = [];
  [['light', light], ['dark', dark]].forEach(([name, v]) => pairs.forEach(([a, b]) => { if (!v[a] || !v[b]) { bad.push(`${name}: missing ${a}/${b}`); return; } const r = cr(v[a], v[b]); if (r < 4.5) bad.push(`${name} ${a} on ${b} = ${r.toFixed(2)}`); }));
  rec('contrast', bad.length ? 'FAIL' : 'PASS', bad.length ? bad.join(' | ') : `${pairs.length * 2} text-colour pairs meet 4.5:1 in light and dark`);
}

// ---------- report ----------
const w = Math.max(...results.map((r) => r.gate.length));
let fail = 0;
results.forEach((r) => { if (r.status === 'FAIL') fail++; console.log(`${r.status.padEnd(4)} ${r.gate.padEnd(w)}  ${r.msg}`); });
console.log(fail ? `\n${fail} gate(s) FAILED` : '\nall gates passed');
process.exit(fail ? 1 : 0);
