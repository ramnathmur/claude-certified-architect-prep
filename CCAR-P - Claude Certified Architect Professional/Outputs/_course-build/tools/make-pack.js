'use strict';
// Builds an author pack for one or more objectives: everything an author needs, copied verbatim from the sources.
// Usage: node tools/make-pack.js O2.1 [O2.2 ...]      writes _authoring/packs/<ID>.md
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const HERE = path.resolve(__dirname, '..');
const ROOT = path.resolve(HERE, '..', '..');
const read = (p) => fs.readFileSync(p, 'utf8').replace(/\r\n/g, '\n');
const G = JSON.parse(read(path.join(HERE, 'data', 'guide-objectives.json')));
const FAC = JSON.parse(read(path.join(HERE, 'data', 'facets.json')));
const LEDGER = read(path.join(ROOT, 'prep with quiz', 'FACET-LEDGER.md'));
const ids = process.argv.slice(2).map((s) => s.toUpperCase());
if (!ids.length) { console.error('usage: node tools/make-pack.js O2.1 [O2.2 ...]'); process.exit(1); }
const OUT = path.join(HERE, '_authoring', 'packs');
fs.mkdirSync(OUT, { recursive: true });

// ledger snippets: facet id -> truncated situation text
const snip = {};
for (const m of LEDGER.matchAll(/^\| `(F-\d+\.\d+-\d+)` \| \d+\.\d+ \| O\d\.\d \| (.*?) \| (.*?) \|/gm)) snip[m[1]] = { sit: m[2].replace(/…$/, '').trim(), ans: m[3].replace(/…$/, '').trim() };

function sectionText(dom, sec) {
  const md = read(path.join(ROOT, 'prep with quiz', `CCAR-P_Domain-${dom}_v1.md`));
  const re = new RegExp(`^## ${sec.replace('.', '\\.')} .*$`, 'm');
  const m = md.match(re);
  if (!m) return '(section not found)';
  const start = m.index;
  const next = md.slice(start + 3).search(/^## \d+\.\d+ /m);
  return md.slice(start, next < 0 ? undefined : start + 3 + next).replace(/\n---\s*$/, '').trim();
}
function tableRows(txt) {
  const rows = [];
  for (const line of txt.split('\n')) {
    if (!line.startsWith('|') || /^\|[-| ]+\|$/.test(line)) continue;
    const cells = line.split('|').slice(1, -1).map((c) => c.trim());
    if (cells.length >= 2) rows.push(cells);
  }
  return rows;
}
function facetMap(sec, txt) {
  const rows = tableRows(txt);
  return (FAC[sec] || []).map((id) => {
    const s = snip[id];
    const row = s && rows.find((r) => r[0].startsWith(s.sit.slice(0, 40)));
    return { id, row: row ? row.join(' | ') : `(no row matched; ledger says: ${s ? s.sit + ' -> ' + s.ans : 'n/a'})` };
  });
}
function lessonSection(dom, n) {
  const f = path.join(ROOT, 'Outputs', 'lessons', `CCAR-P_Lesson-Domain-${dom}_v1.md`);
  if (!fs.existsSync(f)) return '(no markdown lesson for this domain)';
  const md = read(f);
  const m = md.match(new RegExp(`^## Objective ${n} .*$`, 'm'));
  if (!m) return '(lesson section not found)';
  const rest = md.slice(m.index + 3);
  const next = rest.search(/^## /m);
  return md.slice(m.index, next < 0 ? undefined : m.index + 3 + next).trim();
}
function guideSamples() {
  let txt = '';
  for (const exe of ['pdftotext', 'C:\\Program Files\\Git\\mingw64\\bin\\pdftotext.exe']) {
    try { txt = execFileSync(exe, ['-layout', path.join(ROOT, 'sources', 'CCAR-P_Official-Exam-Guide_v1.0.pdf'), '-'], { encoding: 'latin1', maxBuffer: 1 << 25 }); break; } catch (e) { /* next */ }
  }
  const a = txt.indexOf('8. Sample Questions'), b = txt.indexOf('9. How the Exam Is Scored');
  return txt.slice(a, b).replace(/\r/g, '').replace(/\u00ad/g, '').replace(/Claude Certification Program\s+Exam guide/g, '').replace(/[ \t]+\n/g, '\n').trim();
}
function written() {
  const out = [];
  for (const f of fs.readdirSync(path.join(HERE, 'fragments'))) {
    const id = f.replace(/\.html$/, '');
    const h = read(path.join(HERE, 'fragments', f));
    const anchors = [...h.matchAll(/<section class="concept" id="(c[\d.]+)"/g)].map((m) => m[1]);
    out.push(`${id}${anchors.length ? ' (anchors: ' + anchors.join(', ') + ')' : ''}`);
  }
  return out.sort().join('\n');
}
const allTitles = (() => {
  const t = [];
  for (let d = 1; d <= 7; d++) for (const m of read(path.join(ROOT, 'prep with quiz', `CCAR-P_Domain-${d}_v1.md`)).matchAll(/^## (\d+\.\d+) (.+)$/gm)) t.push(`${m[1]}  ${m[2]}`);
  return t.join('\n');
})();
const objToSec = G.objectives.map((o) => `${o.id}  §${o.sections.join(', §')}  ${o.text}`).join('\n');

for (const id of ids) {
  const o = G.objectives.find((x) => x.id === id);
  if (!o) { console.error('unknown objective ' + id); continue; }
  const dom = G.domains[o.dom];
  let md = `# Author pack: ${o.id}\n\n`;
  md += `Objective (verbatim from the guide, this is the sheet heading): ${o.text}\nDomain ${o.dom}: ${dom.name}, ${dom.weight}% of the exam. Sheet D${o.dom}-${o.n}. Page id and fragment file: \`${o.id.toLowerCase()}\` -> \`fragments/${o.id.toLowerCase()}.html\`. Corpus sections to teach: ${o.sections.join(', ')}.\n\n`;
  md += `Figure ids to use (unique across the document): prefix \`f${o.dom}${o.n}\` then a letter, for example \`f${o.dom}${o.n}a-t\` and \`f${o.dom}${o.n}a-d\`.\n\n`;
  md += `## Facets: every one needs a rule row with its data-facet ID\n\n`;
  for (const sec of o.sections) {
    const txt = sectionText(o.dom, sec);
    const fm = facetMap(sec, txt);
    md += `### §${sec}: ${fm.length} facet(s)\n${fm.length ? fm.map((f) => `- ${f.id}: ${f.row}`).join('\n') : '- none: this section has no decision table, so teach it from its core facts and scenario; the concept block is still required.'}\n\n`;
  }
  md += `## Corpus text, verbatim (the only source for decision rules)\n\n`;
  for (const sec of o.sections) md += sectionText(o.dom, sec) + '\n\n---\n\n';
  md += `## Lesson text for this objective (a source for worked examples and numbers only; re-check every number and claim, and never copy its phrasing)\n\n${lessonSection(o.dom, o.n)}\n\n`;
  if ([2, 3, 4].includes(o.dom)) md += `## The guide's section 8 (official sample questions and rationales; Domain ${o.dom === 3 ? 3 : o.dom === 2 ? 2 : 4} has one)\n\n${guideSamples()}\n\n`;
  md += `## Live-docs facts already verified for this domain (cite with the date given; use them in Go deeper blocks or worked examples, never as a decision rule)\n\n${(() => { const f = path.join(HERE, '_authoring', 'facts', `D${o.dom}.md`); return fs.existsSync(f) ? read(f) : '(none recorded yet for this domain)'; })()}\n\n`;
  md += `## All objectives and their sections (for Connections; link only to pages and anchors that exist)\n\n${objToSec}\n\n## All corpus section titles\n\n${allTitles}\n\n## Pages already written, with their concept anchors (link to an anchor only if it is listed here)\n\n${written()}\n`;
  fs.writeFileSync(path.join(OUT, `${o.id}.md`), md, 'utf8');
  console.log('wrote', path.join('_authoring', 'packs', `${o.id}.md`), (md.length / 1024).toFixed(0) + ' KB');
}
