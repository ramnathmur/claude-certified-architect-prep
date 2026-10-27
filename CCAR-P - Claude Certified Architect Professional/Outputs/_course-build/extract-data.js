'use strict';
// Extracts the data the course build depends on, straight from the sources:
//   data/guide-objectives.json  - 38 objectives, verbatim from the official guide PDF (via pdftotext)
//   data/objective-map.json     - objective -> corpus sections (from the Objective Map)
//   data/facets.json            - corpus section -> facet IDs (from the Facet Ledger)
// Run: node extract-data.js
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execFileSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..', '..'); // the CCAR-P folder
const PDF = path.join(ROOT, 'sources', 'CCAR-P_Official-Exam-Guide_v1.0.pdf');
const MAP = path.join(ROOT, 'prep with quiz', 'CCAR-P_Objective-Map_v1.md');
const LEDGER = path.join(ROOT, 'prep with quiz', 'FACET-LEDGER.md');
const OUT = path.join(__dirname, 'data');

function pdfText() {
  const candidates = ['pdftotext', 'C:\\Program Files\\Git\\mingw64\\bin\\pdftotext.exe'];
  for (const exe of candidates) {
    try {
      return execFileSync(exe, ['-layout', PDF, '-'], { encoding: 'latin1', maxBuffer: 20 * 1024 * 1024 });
    } catch (e) { /* try next */ }
  }
  throw new Error('pdftotext not found');
}

function parseGuide(txt) {
  txt = txt.replace(/\r/g, '');
  const seg = txt.split('Detailed objectives by domain')[1].split('7. How to Prepare')[0]
    .replace(/Claude Certification Program\s+Exam guide/g, '');
  const domains = {};
  const objs = {};
  let dom = null, open = false;
  for (const line of seg.split('\n')) {
    const s = line.trim().replace(/\u00ad/g, '');
    if (!s) continue;
    const m = s.match(/^Domain (\d): (.*?) \((\d+)%\)$/);
    if (m) { dom = +m[1]; domains[dom] = { n: dom, name: m[2].replace(/\s+/g, ' '), weight: +m[3] }; objs[dom] = []; open = false; continue; }
    if (s.startsWith('\u00b7')) { objs[dom].push(s.replace(/^\u00b7\s*/, '')); open = true; continue; }
    if (open && dom) objs[dom][objs[dom].length - 1] += ' ' + s;
  }
  const list = [];
  for (const d of Object.keys(objs).map(Number).sort()) {
    objs[d].forEach((t, i) => {
      t = t.replace(/\s+/g, ' ').trim();
      // pdftotext drops the arrow glyphs in O1.2; restore them from the guide's own wording
      t = t.replace('input  processing  output  feedback loops', 'input \u2192 processing \u2192 output \u2192 feedback loops');
      t = t.replace('input processing output feedback loops', 'input \u2192 processing \u2192 output \u2192 feedback loops');
      list.push({ id: `O${d}.${i + 1}`, dom: d, n: i + 1, text: t });
    });
  }
  return { domains, list };
}

function parseMap(md) {
  md = md.replace(/\r/g, '');
  const rows = [];
  for (const line of md.split('\n')) {
    const m = line.match(/^\| \*\*(O\d\.\d)\*\* \| D(\d) \| (.*?) \| ([\d., ]+) \| (\d+) \|$/);
    if (m) rows.push({ id: m[1], dom: +m[2], mapTitle: m[3], sections: m[4].split(',').map(s => s.trim()), facets: +m[5] });
  }
  return rows;
}

function parseLedger(md) {
  md = md.replace(/\r/g, '');
  const bySection = {};
  for (const line of md.split('\n')) {
    const m = line.match(/^\| `(F-(\d+\.\d+)-\d+)` \| (\d+\.\d+) \| (O\d\.\d) \|/);
    if (m) (bySection[m[3]] = bySection[m[3]] || []).push(m[1]);
  }
  return bySection;
}

fs.mkdirSync(OUT, { recursive: true });
const guide = parseGuide(pdfText());
const map = parseMap(fs.readFileSync(MAP, 'utf8'));
const facets = parseLedger(fs.readFileSync(LEDGER, 'utf8'));
const sha = crypto.createHash('sha256').update(fs.readFileSync(PDF)).digest('hex');

if (guide.list.length !== 38) throw new Error('expected 38 objectives, got ' + guide.list.length);
if (map.length !== 38) throw new Error('expected 38 map rows, got ' + map.length);
const merged = guide.list.map(o => {
  const m = map.find(r => r.id === o.id);
  if (!m) throw new Error('no map row for ' + o.id);
  return Object.assign({}, o, { sections: m.sections, mapTitle: m.mapTitle });
});
const facetCount = Object.values(facets).reduce((a, v) => a + v.length, 0);

fs.writeFileSync(path.join(OUT, 'guide-objectives.json'), JSON.stringify({ source: 'CCAR-P_Official-Exam-Guide_v1.0.pdf', sha256: sha, domains: guide.domains, objectives: merged }, null, 1));
fs.writeFileSync(path.join(OUT, 'facets.json'), JSON.stringify(facets, null, 1));
console.log('objectives:', merged.length, '| domains:', Object.keys(guide.domains).length, '| sections with facets:', Object.keys(facets).length, '| facets:', facetCount);
console.log('weights:', Object.values(guide.domains).map(d => `D${d.n}=${d.weight}`).join(' '));
console.log('pdf sha256:', sha);
