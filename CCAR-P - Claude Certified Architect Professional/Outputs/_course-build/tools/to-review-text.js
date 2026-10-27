'use strict';
// Converts built course pages to plain text for cold reviewers.
// Usage: node to-review-text.js <outDir> <pageId> [<pageId> ...]
// Reads fragments/<id>.html, writes <outDir>/<kind>-<id>.txt. Keeps structure, drops markup, keeps figure labels.
const fs = require('fs');
const path = require('path');
const [outDir, ...ids] = process.argv.slice(2);
if (!outDir || !ids.length) { console.error('usage: node to-review-text.js <outDir> <pageId>...'); process.exit(1); }
const FR = path.join(__dirname, '..', 'fragments');
const dec = (s) => s.replace(/&gt;/g, '>').replace(/&lt;/g, '<').replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#8217;/g, "'");
const tx = (s) => dec(s.replace(/<[^>]+>/g, '')).replace(/[ \t]+/g, ' ').trim();

function convert(html) {
  let h = html.replace(/^<!--meta[\s\S]*?-->\n?/, '');
  h = h.replace(/<figure class="fig">([\s\S]*?)<\/figure>/g, (_, f) => {
    const title = (f.match(/<title[^>]*>([\s\S]*?)<\/title>/) || [])[1] || '';
    const desc = (f.match(/<desc[^>]*>([\s\S]*?)<\/desc>/) || [])[1] || '';
    const labels = [...f.matchAll(/<text[^>]*>([\s\S]*?)<\/text>/g)].map((m) => tx(m[1])).filter(Boolean).join(' / ');
    const cap = (f.match(/<figcaption>([\s\S]*?)<\/figcaption>/) || [])[1] || '';
    return `\n[FIGURE. Title: ${tx(title)} Description: ${tx(desc)} Labels in the drawing: ${labels}. Caption: ${tx(cap)}]\n`;
  });
  h = h.replace(/<li class="rh"[\s\S]*?<\/li>/g, '');
  h = h.replace(/<li data-facet="([^"]+)"><span class="when">([\s\S]*?)<\/span><span class="then">([\s\S]*?)<span class="why">([\s\S]*?)<\/span><\/span><\/li>/g,
    (_, id, w, t, y) => `\n[${id}] RULE. If: ${tx(w)} | Then: ${tx(t)} | Because: ${tx(y)}`);
  h = h.replace(/<li class="(ok|no)"><span class="mark">[^<]*<\/span><span>([\s\S]*?)<\/span><\/li>/g, (_, k, t) => `\n  ${k === 'ok' ? 'CORRECT' : 'WRONG'} option: ${tx(t)}`);
  h = h.replace(/<h[23][^>]*>([\s\S]*?)<\/h[23]>/g, (_, t) => `\n\n## ${tx(t)}\n`);
  h = h.replace(/<aside class="remember"[^>]*>([\s\S]*?)<\/aside>/g, (_, a) => `\n\nREMEMBER BOX (sits in the margin beside the text):${[...a.matchAll(/<li>([\s\S]*?)<\/li>/g)].map((m, i) => `\n  ${i + 1}. ${tx(m[1])}`).join('')}\n`);
  h = h.replace(/<details class="say"[^>]*>\s*<summary>([\s\S]*?)<\/summary>\s*<div class="ans">([\s\S]*?)<\/div>\s*<\/details>/g, (_, s, a) => `\n\nSAY IT BACK (optional self-check). Question: ${tx(s.replace(/<b>[\s\S]*?<\/b>/, ''))} Answer shown on click: ${tx(a)}\n`);
  h = h.replace(/<details class="deeper"[^>]*>\s*<summary>([\s\S]*?)<\/summary>([\s\S]*?)<\/details>/g, (_, s, b) => `\n\n[OPTIONAL FOLD: ${tx(s)}]\n${b.replace(/<\/p>/g, '\n').replace(/<[^>]+>/g, '')}\n[END FOLD]\n`);
  h = h.replace(/<p class="stem">([\s\S]*?)<\/p>/g, (_, t) => `\nEXAM-STYLE STEM: ${tx(t)}`);
  h = h.replace(/<span class="lbl">([^<]*)<\/span>/g, '[$1] ');
  const defs = [];
  h = h.replace(/<dfn data-def="([^"]*)">([^<]*)<\/dfn>/g, (_, d, t) => { defs.push(`${t}: ${d}`); return t; });
  h = h.replace(/<\/(p|li|div|section|ul|ol|nav|tr|figcaption)>/g, '\n').replace(/<\/t[dh]>/g, ' | ');
  h = dec(h.replace(/<[^>]+>/g, ''));
  const body = h.split('\n').map((l) => l.replace(/[ \t]+/g, ' ').trim()).filter((l, i, a) => l || (a[i - 1] && a[i - 1] !== '')).join('\n').trim() + '\n';
  return process.env.NODEFS || !defs.length ? body : body + '\nGLOSSARY ENTRIES DEFINED IN THIS PAGE (shown on the glossary page, not inline):\n' + defs.map((d) => '  ' + dec(d)).join('\n') + '\n';
}
fs.mkdirSync(outDir, { recursive: true });
const G = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', 'guide-objectives.json'), 'utf8'));
const PLAN_TEXT = '[FLOOR PLAN, a drawing of seven rooms whose floor area is proportional to exam weight: D3 Integration 19% (8 objectives, about 12 items), D1 Solution design 17% (6 objectives, about 11 items), D4 Evaluation and testing 16% (6, about 10), D5 Governance and safety 14% (5, about 9), D6 Stakeholders and lifecycle 14% (5, about 9), D2 Models and prompting 13% (5, about 8), D7 Developer productivity 7% (3, about 4). Each room opens that domain. Small squares inside a room are its objective sheets. Four doors between rooms mark cross-domain links, listed in the text below. A line under the plan reads: 100% of the 63 scored items. Floor area = exam weight.]';
for (const id of ids) {
  const p = path.join(FR, id + '.html');
  const isObj = /^o\d/.test(id);
  let body = convert(fs.readFileSync(p, 'utf8')).replace(/\{\{FLOORPLAN\}\}/g, PLAN_TEXT).replace(/\{\{WRITTEN\}\}/g, '2');
  if (isObj) {
    const o = G.objectives.find((x) => x.id.toLowerCase() === id);
    const d = G.domains[o.dom];
    body = `SHEET HEADING (the objective, in the guide's own words): ${o.text}\nDomain ${o.dom}: ${d.name}, ${d.weight}% of the exam. Corpus sections taught: ${o.sections.join(', ')}.\n\n` + body;
  }
  fs.writeFileSync(path.join(outDir, `${isObj ? 'chapter' : 'page'}-${id.toUpperCase()}.txt`), body, 'utf8');
}
console.log('wrote', ids.length, 'file(s) to', outDir);
