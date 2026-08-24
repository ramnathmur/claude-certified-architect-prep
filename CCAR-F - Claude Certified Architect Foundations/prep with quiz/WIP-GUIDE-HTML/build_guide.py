#!/usr/bin/env python3
"""Build CCA-F_Study-Guide_v1.html from source/guide_en.md.

Faithful reproduction + 65 analogy boxes + nemesis flags + folded answers + cram mode.
Every fidelity claim in the plan is asserted here; the build fails rather than shipping a
quietly corrupted document.
"""
import html as ihtml
import json, os, re, sys
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # prep with quiz/
PROJ = os.path.dirname(ROOT)                       # project root
SRC = os.path.join(ROOT, "source", "guide_en.md")
OUT = os.path.join(PROJ, "Outputs", "CCA-F_Study-Guide_v1.html")

RAW = open(SRC, encoding="utf-8").read()
LINES = RAW.split("\n")

WORLD_NAME = {
    "post": "The postal service", "kitchen": "The restaurant", "crew": "The film crew",
    "plug": "The plug standard", "house": "The house you moved into", "intern": "Training an intern",
    "laundry": "The launderette", "road": "The road trip", "triage": "The triage desk",
    "radio": "The ship's radio", "pack": "The rucksack", "court": "Chain of custody",
    "library": "The library",
}

# ---------------------------------------------------------------- fence-aware helpers

def fence_mask():
    """True for every line that sits inside a fenced code block."""
    mask, inside = [], False
    for ln in LINES:
        if ln.lstrip().startswith("```"):
            mask.append(True); inside = not inside; continue
        mask.append(inside)
    return mask

MASK = fence_mask()

def headings():
    out = []
    for i, ln in enumerate(LINES):
        if MASK[i]:
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if m:
            out.append((i + 1, len(m.group(1)), m.group(2).strip()))
    return out

HEADS = headings()

# ---------------------------------------------------------------- section table
# (start_line, id, group, title, short, num)
SECTION_DEFS = [
    (1,    "start",     "Orientation", "Start here — format, domains, weights", "Start",   ""),
    (52,   "scenarios", "Orientation", "The 8 exam scenarios",                  "Scenarios", ""),
    (80,   "docs",      "Orientation", "Official documentation",                "Docs",    ""),
    (110,  "ch1",  "Part I · Theory", "Claude API — fundamentals",              "Ch1", "1"),
    (197,  "ch2",  "Part I · Theory", "Tools and tool_use",                     "Ch2", "2"),
    (306,  "ch3",  "Part I · Theory", "Claude Agent SDK",                       "Ch3", "3"),
    (446,  "ch4",  "Part I · Theory", "Model Context Protocol (MCP)",           "Ch4", "4"),
    (547,  "ch5",  "Part I · Theory", "Claude Code — config and workflows",     "Ch5", "5"),
    (802,  "ch6",  "Part I · Theory", "Prompt engineering",                     "Ch6", "6"),
    (1016, "ch7",  "Part I · Theory", "Message Batches API",                    "Ch7", "7"),
    (1076, "ch8",  "Part I · Theory", "Task decomposition strategies",          "Ch8", "8"),
    (1129, "ch9",  "Part I · Theory", "Escalation and human-in-the-loop",       "Ch9", "9"),
    (1230, "ch10", "Part I · Theory", "Error handling in multi-agent systems",  "Ch10", "10"),
    (1292, "ch11", "Part I · Theory", "Context management in production",       "Ch11", "11"),
    (1411, "ch12", "Part I · Theory", "Preserving provenance",                  "Ch12", "12"),
    (1477, "ch13", "Part I · Theory", "Claude Code built-in tools",             "Ch13", "13"),
    (1511, "d1", "Part II · Domains", "D1 Agent architecture (27%)",            "D1", ""),
    (1607, "d2", "Part II · Domains", "D2 Tool design and MCP (18%)",           "D2", ""),
    (1678, "d3", "Part II · Domains", "D3 Claude Code config (20%)",            "D3", ""),
    (1764, "d4", "Part II · Domains", "D4 Prompt engineering (20%)",            "D4", ""),
    (1849, "d5", "Part II · Domains", "D5 Context and reliability (15%)",       "D5", ""),
    (1938, "worked",  "Assessment", "12 worked questions with explanations",    "Worked", ""),
    (2120, "pt-mars", "Assessment", "Practice · Multi-agent research (Q1–15)",  "PT 1–15", ""),
    (2355, "pt-ci",   "Assessment", "Practice · Claude Code for CI (Q16–30)",   "PT 16–30", ""),
    (2584, "pt-code", "Assessment", "Practice · Code generation (Q31–45)",      "PT 31–45", ""),
    (2813, "pt-supp", "Assessment", "Practice · Customer support (Q46–60)",     "PT 46–60", ""),
    (3043, "pt-conv", "Assessment", "Practice · Conversational AI (Q61–76)",    "PT 61–76", ""),
    (3283, "exercises", "Closing", "Practical exercises",                       "Exercises", ""),
    (3345, "appendix",  "Closing", "Appendix — technologies and concepts",      "Appendix", ""),
    (3366, "scope",     "Closing", "Out-of-scope topics",                       "Out of scope", ""),
    (3389, "prep",      "Closing", "Preparation recommendations",               "Prep", ""),
]
QUESTION_SECTIONS = {"worked", "pt-mars", "pt-ci", "pt-code", "pt-supp", "pt-conv"}

# ---------------------------------------------------------------- analogies

def load_analogies():
    entries = []
    for p in ("analogies_p1.json", "analogies_p2.json", "analogies_p3.json"):
        entries += json.load(open(os.path.join(HERE, p), encoding="utf-8"))["entries"]
    return entries

ANA = load_analogies()
NEM = json.load(open(os.path.join(HERE, "nemesis.json"), encoding="utf-8"))

def analogy_html(a):
    flag = NEM["flags"].get(a["id"])
    nem = ""
    if flag:
        nem = (f'<div class="an-nem"><span class="lab">⚠ Your record · {ihtml.escape(flag["label"])}'
               f'</span>{flag["text"]}</div>')
    return (
        f'<div class="an{" hi" if flag else ""}" style="--acc:var(--w-{a["world"]})" data-an="{a["id"]}">'
        f'<div class="an-top"><span class="an-w">{ihtml.escape(WORLD_NAME[a["world"]])}</span>'
        f'<span class="an-t">§{a["id"]}</span></div>'
        f'<div class="an-b"><div class="an-svg">'
        f'<svg viewBox="0 0 160 160" fill="none" stroke="currentColor" stroke-width="2.6" '
        f'stroke-linecap="round" stroke-linejoin="round">{a["svg"]}</svg></div>'
        f'<div class="an-txt"><div class="an-lab">The picture</div>'
        f'<p class="an-pic">{a["picture"]}</p>'
        f'<div class="an-lab">The analogy</div><p>{a["analogy"]}</p>'
        f'<div class="an-snap"><b>So on the exam →</b> {a["snapback"]}</div>'
        f'</div></div>{nem}</div>')

for a in ANA:
    a["html"] = analogy_html(a)
    a["nemesis"] = a["id"] in NEM["flags"]

# ---------------------------------------------------------------- markdown

MD = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])

def to_html(md_text):
    MD.reset()
    out = MD.convert(md_text)
    out = re.sub(r"<table>", '<div class="tw"><table>', out)
    out = re.sub(r"</table>", "</table></div>", out)
    return out

def anchor_headings(h):
    def rep(m):
        lvl, attrs, txt = m.group(1), m.group(2), m.group(3)
        plain = re.sub(r"<[^>]+>", "", txt)
        slug = re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")[:60]
        return f'<h{lvl} id="s-{slug}"{attrs}>{txt}</h{lvl}>'
    return re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", rep, h, flags=re.S)

# ---------------------------------------------------------------- question folding

QRE = re.compile(r"^##\s+Question\s+(\d+)\b", re.M)

def fold_questions(md_text):
    """Split each `## Question N` block into a visible part and a revealed answer part.

    Nothing is deleted: the **[CORRECT]** marker moves from the option into the revealed
    panel, and the `**Why X:**` rationale moves with it.
    """
    starts = [m.start() for m in QRE.finditer(md_text)]
    if not starts:
        return to_html(md_text), 0
    head = md_text[:starts[0]]
    out = [to_html(head)] if head.strip() else []
    blocks = [md_text[a:(starts[i + 1] if i + 1 < len(starts) else len(md_text))]
              for i, a in enumerate(starts)]
    n = 0
    for blk in blocks:
        blk = re.sub(r"\n---\s*\n?\s*$", "\n", blk)
        wm = re.search(r"^\*\*Why\s+([A-F])[^:]*:\*\*", blk, re.M)
        if not wm:
            out.append(to_html(blk)); continue
        visible, answer_md = blk[:wm.start()], blk[wm.start():]
        letters = re.findall(r"^-\s*([A-F])\)[^\n]*\*\*\[CORRECT\]\*\*", visible, re.M)
        correct = letters[0] if letters else wm.group(1)
        visible = re.sub(r"\s*\*\*\[CORRECT\]\*\*", "", visible)
        vh = to_html(visible)
        vh = re.sub(r"<h2([^>]*)>(.*?)</h2>", r'<div class="qh">\2</div>', vh, count=1, flags=re.S)
        ah = to_html(f"**Correct answer: {correct}**\n\n" + answer_md)
        out.append(f'<div class="qz">{vh}<button class="rv">Reveal answer</button>'
                   f'<div class="ans">{ah}</div></div>')
        n += 1
    return "\n".join(out), n

# ---------------------------------------------------------------- assemble sections

def slice_md(start, end):
    return "\n".join(LINES[start - 1:end - 1 if end else None])

sections, total_q = [], 0
for i, (start, sid, group, title, short, num) in enumerate(SECTION_DEFS):
    end = SECTION_DEFS[i + 1][0] if i + 1 < len(SECTION_DEFS) else None
    md_text = slice_md(start, end)

    if sid in QUESTION_SECTIONS:
        body, qn = fold_questions(md_text)
        total_q += qn
        if qn:
            body = ('<button class="btn" id="revealAll" style="margin:6px 0 14px">'
                    'Reveal all answers</button>') + body
    else:
        body = to_html(md_text)

    body = anchor_headings(body)
    src_html = body          # reproduction only — fidelity gates run against this, not my additions

    # inject analogy boxes directly under their concept heading
    concepts = []
    if num:
        for a in ANA:
            if a["id"].split(".")[0] == num:
                pat = re.compile(r'(<h2[^>]*>\s*' + re.escape(a["id"]) + r'\b.*?</h2>)', re.S)
                if not pat.search(body):
                    sys.exit(f"FAIL: no <h2> for concept {a['id']} in section {sid}")
                body = pat.sub(lambda m: m.group(1) + a["html"], body, count=1)
                concepts.append(a["id"])

    sections.append({"id": sid, "group": group, "title": title, "short": short, "num": num,
                     "html": body, "src_html": src_html, "concepts": concepts,
                     "keywords": " ".join(t for ln, _, t in HEADS if start <= ln < (end or 10**9))})

# gaps callout onto the Start section
gap_rows = "".join(
    f"<tr><td>{g['corpus']}</td><td>{ihtml.escape(g['topic'])}</td>"
    f"<td style='text-align:right'>{g['misses']}×</td></tr>" for g in NEM["gaps"])
sections[0]["html"] += (
    '<div class="gaps"><h4>Six things you have actually got wrong that this guide never teaches</h4>'
    '<p style="margin:.3em 0 .7em;font-size:14px">Checked against your ten scored mocks. These sections '
    'exist in your own corpus files but have no counterpart in Part I here, so revising this document '
    'alone will not close them.</p><div class="tw"><table><tr><th>Corpus section</th><th>Topic</th>'
    f'<th style="text-align:right">Misses</th></tr>{gap_rows}</table></div></div>')

sections.append({"id": "cram", "group": "Extra", "title": "Cram mode — all 65 pictures",
                 "short": "Cram", "num": "", "html": "", "concepts": [],
                 "keywords": "cram revision analogies pictures"})

# ---------------------------------------------------------------- fidelity gates

errs = []
allhtml = "".join(s["html"] for s in sections)
# fidelity is a claim about the REPRODUCTION, so gate on src_html and never on my injections
repro = "".join(s.get("src_html", "") for s in sections)

def norm(s):
    """Normalise both sides identically.

    Three things learned the hard way here:
      * `_` must be stripped from BOTH sides -- `stop_reason` renders as <code>stop_reason</code>.
      * hrefs carry the URL tokens that markdown moves out of the visible text, so surface them
        before tags are dropped, or every link's URL reads as lost content.
      * replace tags with a SPACE, not with nothing, or adjacent tokens glue into one.
    """
    s = ihtml.unescape(s)
    # Replace the WHOLE opening <a> tag with the bare URL. Substituting just the href= attribute
    # leaves the URL inside the angle brackets, where the tag stripper on the next line eats it --
    # which is exactly what made all 24 links read as lost content.
    s = re.sub(r'<a\s[^>]*href="([^"]+)"[^>]*>', r" \1 ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[`*_]", "", s)
    return re.sub(r"\s+", " ", s)   # tags became spaces; collapse or substring checks fail

def fidelity_view(h):
    """The reproduction with my own injected UI chrome removed."""
    h = re.sub(r'<button[^>]*>.*?</button>', " ", h, flags=re.S)
    return h

probe = norm(repro)
for _, lvl, txt in HEADS:
    if norm(txt) not in probe:
        errs.append(f"heading missing from output: {txt!r}")

want_pre = sum(1 for ln in LINES if ln.lstrip().startswith("```")) // 2
got_pre = repro.count("<pre>")
if got_pre != want_pre:
    errs.append(f"code blocks: {got_pre} in output vs {want_pre} in source")

want_rows = sum(1 for i, ln in enumerate(LINES)
                if not MASK[i] and ln.lstrip().startswith("|")
                and not re.match(r"^\s*\|[\s:|-]+\|\s*$", ln))
got_rows = repro.count("<tr>")
if got_rows != want_rows:
    errs.append(f"table rows: {got_rows} in output vs {want_rows} in source")

# Prose fidelity: compare ALPHANUMERIC tokens only. Counting whitespace-split tokens instead
# measures markdown syntax (#, |, -, ---, list bullets) disappearing into tags, which is the
# conversion working correctly, not content being lost.
def words(s):
    from collections import Counter
    return Counter(re.findall(r"[A-Za-z0-9]+", s.lower()))

src_w = words(norm("\n".join(ln for i, ln in enumerate(LINES) if not MASK[i])))
out_w = words(norm(re.sub(r"<pre>.*?</pre>", " ", fidelity_view(repro), flags=re.S)))
missing = src_w - out_w                      # tokens in source that did not survive
extra = out_w - src_w                        # tokens the build introduced
n_src = sum(src_w.values())
drift = sum(missing.values()) / max(n_src, 1)
if drift > 0.005:
    errs.append(f"prose loss {drift*100:.2f}% ({sum(missing.values())} of {n_src} tokens); "
                f"worst: {missing.most_common(8)}")
elif missing:
    print(f"  note: {sum(missing.values())} token(s) differ: {missing.most_common(5)}")
extra = extra - words(("correct answer " + " ".join("abcdef")) * 90)  # relocated [CORRECT] + its letter
if sum(extra.values()) > 120:
    errs.append(f"build introduced {sum(extra.values())} unexpected tokens: {extra.most_common(8)}")

if len(ANA) != 65:
    errs.append(f"{len(ANA)} analogies, expected 65")
seen = set()
for a in ANA:
    for f in ("svg", "picture", "analogy", "snapback", "world", "title"):
        if not a.get(f):
            errs.append(f"analogy {a['id']} missing {f}")
    if a["world"] not in WORLD_NAME:
        errs.append(f"analogy {a['id']} unknown world {a['world']}")
    if a["id"] in seen:
        errs.append(f"duplicate analogy id {a['id']}")
    seen.add(a["id"])
placed = sum(len(s["concepts"]) for s in sections)
if placed != 65:
    errs.append(f"{placed} analogy boxes placed, expected 65")
if allhtml.count('class="an') < 65:
    errs.append("fewer than 65 analogy boxes in the rendered HTML")

for k in NEM["flags"]:
    if k not in seen:
        errs.append(f"nemesis flag {k} does not match any analogy")

ids = [s["id"] for s in sections]
if len(ids) != len(set(ids)):
    errs.append("duplicate section ids")

if errs:
    print("BUILD FAILED\n" + "\n".join("  - " + e for e in errs))
    sys.exit(1)

# ---------------------------------------------------------------- emit

tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
payload = [{k: s[k] for k in ("id", "group", "title", "short", "num", "html", "concepts", "keywords")}
           for s in sections]   # src_html deliberately excluded from the payload
ana_payload = [{"id": a["id"], "title": a["title"], "picture": a["picture"],
                "snapback": a["snapback"], "html": a["html"], "nemesis": a["nemesis"],
                # world name and analogy body are indexed so "the rucksack one" is findable
                "world": WORLD_NAME[a["world"]], "analogy": re.sub(r"<[^>]+>", "", a["analogy"])}
               for a in ANA]

out = (tpl.replace("__SECTIONS__", json.dumps(payload, ensure_ascii=False))
          .replace("__ANALOGIES__", json.dumps(ana_payload, ensure_ascii=False))
          .replace("__WORLDS__", json.dumps(WORLD_NAME, ensure_ascii=False)))

if "__SECTIONS__" in out or "__ANALOGIES__" in out or "__WORLDS__" in out:
    sys.exit("FAIL: placeholders remain")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(out)

print(f"OK  {OUT}")
print(f"  sections        {len(sections)} (incl. cram)")
print(f"  analogy boxes   {placed} placed, {sum(1 for a in ANA if a['nemesis'])} carrying a nemesis flag")
print(f"  questions       {total_q} folded")
print(f"  code blocks     {got_pre}/{want_pre}   table rows {got_rows}/{want_rows}")
print(f"  size            {os.path.getsize(OUT)/1024:.1f} KB")
