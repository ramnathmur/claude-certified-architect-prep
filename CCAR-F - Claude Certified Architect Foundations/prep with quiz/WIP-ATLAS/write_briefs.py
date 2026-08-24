"""Emit brief_d1.md … brief_d5.md: each authoring agent's slice — card ids, titles, gists, the exact official-guide
bullet text for each card, and the Key-Distinction sections woven into it."""
import importlib.util
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PQ = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("inventory", os.path.join(HERE, "inventory.py"))
inv = importlib.util.module_from_spec(spec); spec.loader.exec_module(inv)
data = json.load(open(os.path.join(HERE, "bullets.json"), encoding="utf-8"))
btext = {b["id"]: b["text"] for b in data["bullets"]}
TS = data["task_statements"]

kd_raw = open(os.path.join(PQ, "CCA-Prep_Key-Distinctions_v1.md"), encoding="utf-8").read()
kd_secs = {}
for m in re.finditer(r"^### (\d+)\. (.*?)$(.*?)(?=^### \d+\. |^## |\Z)", kd_raw, re.M | re.S):
    kd_secs[int(m.group(1))] = f"KD #{m.group(1)} — {m.group(2)}\n{m.group(3).strip()}"

for d in ["D1", "D2", "D3", "D4", "D5"]:
    meta = inv.DOMAINS[d]
    L = [f"# Authoring brief — {d} {meta['name']} ({meta['weight']}%) · building: {meta['world_name']}", ""]
    L.append(f"Corpus depth file: `prep with quiz/CCA-Prep_Domain-{d[1]}_v2.md`. Official guide text: `prep with quiz/source/CCA-F-Official-Exam-Guide_text.txt` (task statements {d[1]}.1–{d[1]}.x and the sample questions).")
    L.append("")
    cards = [c for c in inv.CARDS if c["id"].startswith(d + "-")]
    L.append(f"{len(cards)} cards, in this order (ids fixed):")
    L.append("")
    for c in cards:
        L.append(f"## {c['id']} — {c['title']}")
        L.append(f"Home task statement: TS {c['ts']} — {TS.get(c['ts'], '')}")
        L.append(f"Gist (the concept, to be written as one flat sentence): {c['gist']}")
        if c.get("note"): L.append(f"Note: {c['note']}")
        if c.get("xref"): L.append(f"Also serves TS {', '.join(c['xref'])}.")
        tsb = [b for b in c["bul"] if not b.startswith("APP")]
        app = [b for b in c["bul"] if b.startswith("APP")]
        if tsb:
            L.append("Official-guide bullets this card must cover:")
            for b in tsb: L.append(f"- [{b}] {btext[b]}")
        if app:
            L.append("Appendix items it also serves: " + "; ".join(f"[{b}] {btext[b][:90]}…" for b in app))
        for k in c["kd"]:
            L.append("")
            L.append("Key Distinction to weave into `tested` / `remember`:")
            L.append("```")
            L.append(kd_secs.get(k, f"KD #{k} (text not found)"))
            L.append("```")
        L.append("")
    open(os.path.join(HERE, f"brief_{d.lower()}.md"), "w", encoding="utf-8").write("\n".join(L))
    print("wrote", f"brief_{d.lower()}.md", len(cards), "cards")
