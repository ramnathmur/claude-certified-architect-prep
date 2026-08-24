# -*- coding: utf-8 -*-
"""Build the five lessons into one paged, reading-optimised HTML file."""
import re, io, os, sys, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lessons_a import L1, L2
from lessons_b import L3, L4, L5, CLOSING

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "CCA-F_Lessons_v1.html")
PAGES = [L2, L4, L1, L3, L5, CLOSING]          # taught order: by weight, then the plan


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)
    return t


def convert(md):
    """Markdown subset -> HTML. Returns (body_html, [(anchor, heading), ...])."""
    out, toc, i = [], [], 0
    lines = md.strip("\n").split("\n")
    while i < len(lines):
        ln = lines[i]

        if ln.startswith("```"):                                    # fenced code
            lang = ln[3:].strip()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append('<pre class="code"%s><code>%s</code></pre>'
                       % ((' data-lang="%s"' % lang) if lang else "",
                          html.escape("\n".join(buf), quote=False)))
            continue

        if ln.startswith("## "):                                    # section heading
            txt = ln[3:].strip()
            anchor = re.sub(r"[^a-z0-9]+", "-", txt.lower()).strip("-")[:48]
            toc.append((anchor, txt))
            out.append('<h2 id="%s">%s</h2>' % (anchor, inline(txt)))
            i += 1; continue

        if ln.startswith("### "):
            out.append("<h3>%s</h3>" % inline(ln[4:].strip()))
            i += 1; continue

        if ln.startswith("|"):                                      # table
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], [r for r in rows[1:] if not set("".join(r)) <= set("-: ")]
            t = ["<div class='tw'><table><thead><tr>"]
            t += ["<th>%s</th>" % inline(c) for c in head]
            t.append("</tr></thead><tbody>")
            for r in body:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t)); continue

        if ln.startswith("- "):                                     # list
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:].strip()); i += 1
            out.append("<ul>" + "".join("<li>%s</li>" % inline(x) for x in items) + "</ul>")
            continue

        if not ln.strip():
            i += 1; continue

        para = []                                                   # paragraph
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{2,3} |\||- |```)", lines[i]):
            para.append(lines[i].strip()); i += 1
        out.append("<p>%s</p>" % inline(" ".join(para)))

    return "\n".join(out), toc


nav, sections = [], []
for n, p in enumerate(PAGES):
    body, toc = convert(p["body"])
    nav.append('<button data-page="%s">%s</button>' % (p["slug"], html.escape(p["nav"])))
    jump = ""
    if len(toc) > 1:
        jump = ('<nav class="jump"><span class="jl">In this lesson</span>'
                + "".join('<a href="#%s|%s">%s</a>' % (p["slug"], a, html.escape(t)) for a, t in toc)
                + "</nav>")
    prev = PAGES[n - 1] if n else None
    nxt = PAGES[n + 1] if n + 1 < len(PAGES) else None
    foot = '<div class="pfoot">%s%s</div>' % (
        ('<a class="pv" href="#%s"><span>Previous</span>%s</a>' % (prev["slug"], html.escape(prev["nav"]))) if prev else "<span></span>",
        ('<a class="nx" href="#%s"><span>Next</span>%s</a>' % (nxt["slug"], html.escape(nxt["nav"]))) if nxt else "<span></span>")
    sections.append(
        '<article class="page" id="p-%s">\n<header class="lh"><p class="kicker">Lesson %d of %d</p>'
        '<h1>%s</h1><p class="wt">%s</p></header>\n%s\n<div class="prose">%s</div>\n%s\n</article>'
        % (p["slug"], n + 1, len(PAGES), html.escape(p["title"]), html.escape(p["weight"]), jump, body, foot))

DOC = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Five Lessons &mdash; Claude Certified Architect, Foundations</title>
<style>
:root{
  --paper:#fcf8f1; --card:#fffdf9; --ink:#211d18; --ink2:#5f564a; --ink3:#6e6455;
  --rule:#e2d7c4; --accent:#8c3a1f; --accent2:#1f5c4a; --mark:#f7efd8; --code:#f2ece0;
}
@media (prefers-color-scheme:dark){
  :root{--paper:#16150f; --card:#1d1b15; --ink:#efe7d7; --ink2:#b9ae9c; --ink3:#8d8371;
    --rule:#39332a; --accent:#e08a63; --accent2:#6dc0a4; --mark:#3a3320; --code:#242019;}
}
:root[data-theme="light"]{--paper:#fcf8f1;--card:#fffdf9;--ink:#211d18;--ink2:#5f564a;--ink3:#6e6455;
  --rule:#e2d7c4;--accent:#8c3a1f;--accent2:#1f5c4a;--mark:#f7efd8;--code:#f2ece0;}
:root[data-theme="dark"]{--paper:#16150f;--card:#1d1b15;--ink:#efe7d7;--ink2:#b9ae9c;--ink3:#8d8371;
  --rule:#39332a;--accent:#e08a63;--accent2:#6dc0a4;--mark:#3a3320;--code:#242019;}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
  font:400 18px/1.75 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;}
code{font-family:"SF Mono",Consolas,"Roboto Mono",monospace;font-size:.83em;
  background:var(--code);border-radius:3px;padding:1px 5px;}

/* ---- top navigation ---- */
header.top{border-bottom:1px solid var(--rule);background:var(--card);padding:12px 24px 0}
.brand{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3);
  font-family:system-ui,sans-serif;font-weight:600;margin:0 0 8px}
nav.tabs{display:flex;flex-wrap:wrap;gap:2px}
nav.tabs button{font:600 .78rem/1 system-ui,sans-serif;background:none;border:0;color:var(--ink2);
  padding:9px 13px;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;letter-spacing:.01em}
nav.tabs button:hover{color:var(--ink)}
nav.tabs button[aria-current="page"]{color:var(--accent);border-bottom-color:var(--accent)}

/* ---- page ---- */
main{max-width:100%;padding:0}
.page{display:none;max-width:664px;margin:0 auto;padding:40px 24px 96px}
.page.on{display:block;animation:in .22s ease-out}
@keyframes in{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:none}}
.lh{margin:0 0 26px;padding-bottom:20px;border-bottom:2px solid var(--ink)}
.kicker{margin:0 0 6px;font:600 .7rem/1 system-ui,sans-serif;letter-spacing:.14em;
  text-transform:uppercase;color:var(--accent)}
.lh h1{margin:0;font-size:2.05rem;line-height:1.18;font-weight:600;letter-spacing:-.012em}
.wt{margin:9px 0 0;color:var(--ink3);font-size:.92rem;font-style:italic}

.jump{display:flex;flex-wrap:wrap;gap:6px;align-items:baseline;margin:0 0 30px;
  padding:13px 16px;background:var(--card);border:1px solid var(--rule);border-radius:4px}
.jl{font:600 .66rem/1 system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink3);margin-right:4px;flex:none}
.jump a{font:400 .84rem/1.5 system-ui,sans-serif;color:var(--ink2);text-decoration:none;
  border-bottom:1px solid var(--rule);padding-bottom:1px}
.jump a:hover{color:var(--accent);border-bottom-color:var(--accent)}
.jump a:not(:last-child)::after{content:"";}

.prose p{margin:0 0 1.15em}
.prose h2{margin:2.1em 0 .7em;font-size:1.32rem;line-height:1.3;font-weight:600;
  letter-spacing:-.008em;scroll-margin-top:76px}
.prose h2::before{content:"";display:block;width:38px;height:2px;background:var(--accent);margin-bottom:.55em}
.prose h3{margin:1.7em 0 .5em;font-size:1.06rem;font-weight:600}
.prose strong{font-weight:600;background:linear-gradient(transparent 64%,var(--mark) 64%);padding:0 1px}
.prose em{font-style:italic}
.prose ul{margin:0 0 1.15em;padding-left:1.3em}
.prose li{margin:0 0 .4em}
.prose>p:first-of-type{font-size:1.06em;color:var(--ink2)}

pre.code{background:var(--code);border:1px solid var(--rule);border-radius:4px;
  padding:14px 16px;overflow-x:auto;margin:0 0 1.3em;position:relative}
pre.code code{background:none;padding:0;font-size:.8rem;line-height:1.65;display:block}
pre.code[data-lang]::after{content:attr(data-lang);position:absolute;top:6px;right:10px;
  font:600 .6rem/1 system-ui,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3)}

.tw{overflow-x:auto;margin:0 0 1.4em}
table{border-collapse:collapse;width:100%;font:400 .87rem/1.55 system-ui,sans-serif}
th,td{border-bottom:1px solid var(--rule);padding:9px 12px;text-align:left;vertical-align:top}
th{font-weight:600;font-size:.76rem;letter-spacing:.05em;text-transform:uppercase;
  color:var(--ink3);border-bottom:2px solid var(--rule)}
tbody tr:last-child td{border-bottom:none}

.pfoot{display:flex;justify-content:space-between;gap:18px;margin-top:56px;
  padding-top:22px;border-top:1px solid var(--rule)}
.pfoot a{text-decoration:none;color:var(--ink);font-size:.95rem;font-weight:600;max-width:46%}
.pfoot a span{display:block;font:600 .64rem/1 system-ui,sans-serif;letter-spacing:.13em;
  text-transform:uppercase;color:var(--ink3);margin-bottom:5px}
.pfoot a:hover{color:var(--accent)}
.pfoot .nx{text-align:right}

@media(max-width:640px){
  body{font-size:17px}
  .page{padding:28px 18px 72px}
  .lh h1{font-size:1.6rem}
  header.top{padding:10px 16px 0}
}
@media print{
  header.top,.jump,.pfoot{display:none}
  .page{display:block!important;max-width:none;padding:0 0 30pt;page-break-after:always}
  body{font-size:11pt;background:#fff}
}
</style>
</head>
<body>
<header class="top">
  <p class="brand">Claude Certified Architect &middot; Foundations &middot; the five lessons</p>
  <nav class="tabs" id="tabs">__NAV__</nav>
</header>
<main>
__SECTIONS__
</main>
<script>
const SLUGS = __SLUGS__;
const tabs = document.getElementById("tabs");

/* Navigation drives the DOM directly. The hash is kept in sync for deep links and
   browser back/forward, but the page never depends on the hash actually changing. */
function go(slug, anchor, push){
  const page = SLUGS.includes(slug) ? slug : SLUGS[0];
  document.querySelectorAll(".page").forEach(s => s.classList.toggle("on", s.id === "p-" + page));
  tabs.querySelectorAll("button").forEach(b =>
    b.dataset.page === page ? b.setAttribute("aria-current","page") : b.removeAttribute("aria-current"));
  if (push) { try { history.replaceState(null,"","#"+page+(anchor?"|"+anchor:"")); } catch(e){} }
  if (anchor) {
    const el = document.getElementById(anchor);
    if (el) { el.scrollIntoView({behavior:"instant", block:"start"}); return page; }
  }
  window.scrollTo(0,0);
  return page;
}
function fromHash(h){
  const raw = decodeURIComponent((h || "").replace(/^#/,""));
  if (!raw) return [SLUGS[0], null];
  const [s,a] = raw.split("|");
  return [s, a || null];
}
document.addEventListener("click", e => {
  const b = e.target.closest("#tabs button");
  if (b) { e.preventDefault(); go(b.dataset.page, null, true); return; }
  const a = e.target.closest('a[href^="#"]');
  if (a) { e.preventDefault(); const [s,an] = fromHash(a.getAttribute("href")); go(s, an, true); }
});
window.addEventListener("hashchange", () => { const [s,a] = fromHash(location.hash); go(s,a,false); });
document.addEventListener("keydown", e => {
  if (e.metaKey || e.ctrlKey || e.altKey || /INPUT|TEXTAREA/.test(e.target.tagName)) return;
  const cur = document.querySelector(".page.on");
  const i = SLUGS.indexOf(cur ? cur.id.slice(2) : SLUGS[0]);
  if (e.key === "ArrowRight" && i > -1 && i < SLUGS.length-1) go(SLUGS[i+1], null, true);
  if (e.key === "ArrowLeft"  && i > 0)                        go(SLUGS[i-1], null, true);
});
(function(){ const [s,a] = fromHash(location.hash); go(s,a,false); })();
</script>
</body>
</html>
"""

doc = (DOC.replace("__NAV__", "".join(nav))
          .replace("__SECTIONS__", "\n".join(sections))
          .replace("__SLUGS__", "[" + ",".join('"%s"' % p["slug"] for p in PAGES) + "]"))
io.open(OUT, "w", encoding="utf-8").write(doc)
print("wrote %s (%.0f KB, %d pages)" % (os.path.basename(OUT), os.path.getsize(OUT)/1024.0, len(PAGES)))
