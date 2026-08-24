"""Export each domain's authored cards to audit/dN.cards.md (plain text of every prose field, no citations,
no bullet mapping) plus audit/dN.bullets.md (the official-guide items for that domain, unmapped) — the two inputs
a blind auditor gets. Also verifies every prose field of every card is present verbatim in the built HTML.
Usage: python export_cards.py [path-to-built-html]
"""
import html as H
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
AUD = os.path.join(HERE, "audit"); os.makedirs(AUD, exist_ok=True)


def load(name):
    p = os.path.join(HERE, name + ".py")
    if not os.path.exists(p): return None
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


inv = load("inventory")
data = json.load(open(os.path.join(HERE, "bullets.json"), encoding="utf-8"))
TS = data["task_statements"]
built = None
if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    built = open(sys.argv[1], encoding="utf-8").read()


def prose(s):
    s = H.escape(str(s), quote=True)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return s


missing_in_html = []
for d in ["D1", "D2", "D3", "D4", "D5"]:
    m = load(f"items_{d.lower()}")
    if m is None:
        print(f"{d}: items file missing"); continue
    L = [f"# {d} — {inv.DOMAINS[d]['name']} — authored cards ({len(m.ITEMS)})", ""]
    for it in m.ITEMS:
        L += [f"## {it['id']} — {it['title']}", f"**Concept:** {it['concept']}", f"**What is tested:** {it['tested']}",
              f"**Remember:** {it['remember']}", f"**Analogy:** {it['analogy']}", f"**Picture (alt):** {it['alt']}", ""]
        if built:
            for f in ["title", "concept", "tested", "remember", "analogy"]:
                if prose(it[f]) not in built:
                    missing_in_html.append((it["id"], f))
    open(os.path.join(AUD, f"{d.lower()}.cards.md"), "w", encoding="utf-8").write("\n".join(L))
    n = d[1]
    B = [f"# {d} — official Exam Guide items (task statements {n}.x)", ""]
    for ts_id, title in TS.items():
        if not ts_id.startswith(n + "."): continue
        B.append(f"## TS {ts_id} — {title}")
        for b in data["bullets"]:
            if b["ts"] == ts_id: B.append(f"- [{b['id']}] {b['text']}")
        B.append("")
    open(os.path.join(AUD, f"{d.lower()}.bullets.md"), "w", encoding="utf-8").write("\n".join(B))
    print(f"{d}: exported {len(m.ITEMS)} cards")
if built:
    print("fields missing from built HTML:", missing_in_html or "none")
