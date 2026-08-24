"""Structural integrity check of the built atlas: every internal anchor resolves, prev/next chain covers all pages
with none orphaned, every card has all its parts, no duplicate ids. Usage: python check_html.py [path]"""
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
P = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(HERE)), "Outputs", "CCA-F_Concept-Atlas_v1.html")
s = open(P, encoding="utf-8").read()
fail = []

ids = re.findall(r'\bid="([^"]+)"', s)
dupes = [i for i, n in Counter(ids).items() if n > 1]
if dupes: fail.append(f"duplicate ids: {dupes}")
idset = set(ids)

# page ids are p-<name>; hash routing targets bare <name> or an element id
pages = [i[2:] for i in ids if i.startswith("p-")]
hrefs = sorted(set(re.findall(r'href="#([^"]+)"', s)))
unresolved = [h for h in hrefs if h not in idset and h not in pages]
if unresolved: fail.append(f"unresolved anchors: {unresolved}")

# prev/next chain
pager_links = re.findall(r'<nav class="pager">(.*?)</nav>', s, re.S)
if len(pager_links) != len(pages):
    fail.append(f"{len(pager_links)} pagers for {len(pages)} pages")
chain = []
for blk in pager_links:
    chain.append(re.findall(r'href="#([^"]+)"', blk))
# every page except first must be reachable as a "next", except last as a "prev"
nexts = [c[-1] for c in chain if c]
prevs = [c[0] for c in chain if c]
orphans = [p for p in pages if p not in nexts and p not in prevs and p != pages[0]]
if orphans: fail.append(f"pages orphaned from prev/next chain: {orphans}")

n_cards = len(re.findall(r'<article class="card"', s))
for part in ['class="concept"', 'What is tested', 'Remember', 'class="ana"', '<title id=']:
    n = s.count(part)
    if n < n_cards:
        fail.append(f'card part {part!r} appears {n}x for {n_cards} cards')

# svg hygiene inside cards
card_svgs = re.findall(r'<div class="ill">(.*?)</div>', s, re.S)
bad_svg = [i for i, g in enumerate(card_svgs) if re.search(r'style=|fill="#|stroke="#|<image|<script', g)]
if bad_svg: fail.append(f"{len(bad_svg)} card svgs contain forbidden attributes")

# print + responsive rules present
for need in ["@media print", "@media (max-width:720px)", "@media (max-width:860px)", "page-break-before"]:
    if need not in s: fail.append(f"missing CSS rule: {need}")

print(f"file: {P}")
print(f"size: {len(s)/1024:.0f} KB | pages: {len(pages)} | cards: {n_cards} | ids: {len(ids)} | internal links: {len(hrefs)} | card svgs: {len(card_svgs)}")
print("pages:", ", ".join(pages))
if fail:
    print("\nFAILURES:")
    for f in fail: print("  -", f)
else:
    print("\nSTRUCTURE: PASS")
sys.exit(1 if fail else 0)
