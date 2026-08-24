"""Fence-aware scan of guide_en.md. Establishes the exact heading list the build depends on."""
import os, re, json

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "source", "guide_en.md")
lines = open(SRC, encoding="utf-8").read().split("\n")

heads, in_fence, fences = [], False, 0
for i, ln in enumerate(lines, 1):
    if ln.lstrip().startswith("```"):
        in_fence = not in_fence
        fences += 1
        continue
    if in_fence:
        continue
    m = re.match(r"^(#{1,6})\s+(.*)$", ln)
    if m:
        heads.append({"line": i, "level": len(m.group(1)), "text": m.group(2).strip()})

naive = len([l for l in lines if re.match(r"^#{1,6}\s+", l)])
print(f"lines {len(lines)} | fences {fences} (=> {fences//2} blocks) | headings: fence-aware {len(heads)} vs naive {naive}")
print(f"headings the naive regex would have invented: {naive-len(heads)}\n")

h1 = [h for h in heads if h["level"] == 1]
print(f"H1 count fence-aware: {len(h1)}")
for h in h1:
    print(f"  {h['line']:>5}  {h['text']}")

# Part I chapter sub-sections = the 65 concepts
ch = [h for h in heads if h["level"] == 1 and h["text"].startswith("Chapter ")]
p2 = next(h for h in heads if h["text"].startswith("PART II"))
concepts = [h for h in heads if h["level"] == 2 and ch[0]["line"] < h["line"] < p2["line"]]
print(f"\nPART I concept sub-sections (H2 between Ch1 and PART II): {len(concepts)}")
for c in concepts:
    print(f"  {c['line']:>5}  {c['text']}")

json.dump({"headings": heads, "concepts": concepts},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "scan.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
