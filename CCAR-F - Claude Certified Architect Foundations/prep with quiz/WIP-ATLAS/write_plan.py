"""Emit Outputs/CCA-F_Concept-Atlas-Plan_v1.md from inventory.py + bullets.json (Phase 1 checkpoint doc)."""
import importlib.util
import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(PROJECT, "Outputs", "CCA-F_Concept-Atlas-Plan_v1.md")
spec = importlib.util.spec_from_file_location("inventory", os.path.join(HERE, "inventory.py"))
inv = importlib.util.module_from_spec(spec); spec.loader.exec_module(inv)
data = json.load(open(os.path.join(HERE, "bullets.json"), encoding="utf-8"))
btext = {b["id"]: b["text"] for b in data["bullets"]}
TS = data["task_statements"]

mapped = defaultdict(list)
for c in inv.CARDS:
    for b in c["bul"]:
        mapped[b].append(c["id"])

n_cards = len(inv.CARDS)
n_dom = sum(1 for c in inv.CARDS if not c["id"].startswith("M-"))
n_ts_b = sum(1 for b in data["bullets"] if b["ts"] != "APP")

L = []
w = L.append
w("# CCA-F Concept Atlas — Plan & Concept Inventory (v1)")
w("")
w("**Purpose:** Phase-1 checkpoint for the single-file, globally shareable exam refresher. This document is the")
w("contract the authoring and audit phases build against. Regenerate with `prep with quiz/WIP-ATLAS/write_plan.py`.")
w("**Date:** 2026-08-15 · **Exam:** Claude Certified Architect – Foundations (CCAR-F) · **Deliverable:** `Outputs/CCA-F_Concept-Atlas_v1.html`")
w("")
w("## 1. Source of truth")
w("")
w("- **Official Exam Guide** (`prep with quiz/source/CCA-F-Official-Exam-Guide_text.txt`, v0.2 text; v1.0 is content-identical for domains, task statements, scenarios and scope) — 5 domains → 30 task statements → **240 Knowledge/Skills bullets**, plus Appendix lists: 14 *Technologies and Concepts*, 18 *In-Scope Topics*, 16 *Out-of-Scope Topics*. `extract_bullets.py` parses every one into an ID (`1.1-K1`, `2.5-S5`, `APP-T7`, `APP-I12`, `APP-O3`) — **288 IDs**.")
w("- **Key Distinctions** (`CCA-Prep_Key-Distinctions_v1.md`, 29 traps) — woven into cards as trap callouts.")
w("- **Depth for authoring:** `CCA-Prep_Domain-1…5_v2.md`, `CCA-Prep_Exam-Mechanics_v2.md`, the 12 official sample questions.")
w("- **Deliberately not sourced:** any mock-exam result, `EXAM-LOG.md`, `GAPS.md`, drill progress — the reader is cold.")
w("")
w("## 2. Coverage guarantee (verified, not asserted)")
w("")
w(f"`check_coverage.py` result: **{n_cards} cards** ({n_dom} concept cards + 5 meta cards) · **288/288 IDs mapped, 0 unmapped, 0 unknown references** · **29/29 Key Distinctions covered**. The gate re-runs before authoring and again in the cold audit against the built HTML.")
w("")
w("Cards per domain: " + ", ".join(f"{d} {sum(1 for c in inv.CARDS if c['id'].startswith(d+'-'))}" for d in ["D1","D2","D3","D4","D5"]) + ". Card count follows the guide's bullet count per domain, not the exam weight — D5 has the most bullets.")
w("")
w("## 3. Card contract (what every concept card carries)")
w("")
w("| Field | Rule |")
w("|---|---|")
w("| **Concept** | One flat sentence. No setup, no invented misconception to negate. |")
w("| **What is tested** | The question shape the exam uses for it, and the distractor it is paired against (from the official samples / Key Distinctions). |")
w("| **Remember** | The rule, at most two lines; inline code for names, flags and paths. |")
w("| **Visual analogy** | Inline SVG, drawn in the domain's metaphor world (below), one idea per picture, no text under 11 px, stroke-based so it prints. |")
w("| **Real-world analogy** | Two or three sentences set in the same world — the same characters recur across a domain so the pictures reinforce each other. |")
w("| **Cite** | `TS x.y` (+ `KD #n` when a trap is woven in). |")
w("")
w("Prose rule for every field: a plain, checkable fact gets one flat sentence; say each idea once; no diagnose-negate-reveal tricolons; no dramatic one-liners.")
w("")
w("## 4. Metaphor system — one town, five civic buildings (clean sheet)")
w("")
w("The document frame is a town map; each domain is a building on it. Every card's picture and text analogy live inside its building, so a reader can locate a concept by *where it happens*.")
w("")
w("| Domain | Building | Why it fits |")
w("|---|---|---|")
w("| D1 Agentic Architecture & Orchestration | **The control tower** | Pilots never talk to each other — everything routes through the tower (hub-and-spoke); a plane on the ground has no idea what happened in the air before it (empty subagent context); clearances vs radio requests (code gates vs prompt guidance); flight strips and hand-overs (sessions, resume, fork). |")
w("| D2 Tool Design & MCP Integration | **The library** | The reference librarian picks a database from its blurb (description = interface); look-alike database names misroute (analyze_content vs analyze_document); the catalogue (MCP resources); institutional subscription vs personal card (.mcp.json vs ~/.claude.json); full-text search vs finding by title (Grep vs Glob). |")
w("| D3 Claude Code Configuration & Workflows | **The office** | Company handbook (project CLAUDE.md), your own sticky notes (user-level), floor notices (directory), cross-referenced binders (@import), rules that apply only on the shop floor (path-scoped rules), playbooks pulled off the shelf (skills), an architect's drawing before knocking a wall down (plan mode), the overnight audit robot (CI with -p). |")
w("| D4 Prompt Engineering & Structured Output | **The courthouse** | Elements of an offence vs \"be reasonable\" (explicit criteria); precedents (few-shot); the clerk's standard form (schema) that can be filled correctly and still be wrong (semantic errors); the appeal sent back with specific grounds (retry with feedback) that cannot rule on evidence not in the record (retry limits); night-court docket (batch); a fresh judge for the appeal (independent review). |")
w("| D5 Context Management & Reliability | **The hospital ward** | Vitals chart at the foot of the bed survives every shift summary (case-facts block); a negative test is not a failed test (empty result vs access failure); call the consultant on written criteria, not on how the patient sounds (escalation); timestamps on every lab value (temporal data); the chart lets the next doctor resume after a crash (manifests). |")
w("")
w("Cover / Start page: the town map with the five buildings; exam facts (M-01…M-05) sit on the map, not in a building.")
w("")
w("## 5. Document structure (paged, one file)")
w("")
w("Sticky top nav + prev/next; pages: **Start** (how to read, exam at a glance, town map) · **The exam** (format, weights, six scenarios, tie-breakers, will-not-appear) · **D1** · **D2** · **D3** · **D4** · **D5** · **Trap index** (all 29 Key Distinctions, each linking to its card) · **Coverage** (the 30 task statements → cards, so a reader can check nothing is missing). Self-contained: inline CSS/SVG, no fonts or scripts fetched, no localStorage, print stylesheet for PDF export.")
w("")
w("## 6. Build pipeline")
w("")
w("1. `extract_bullets.py` → `bullets.json` (done). 2. `inventory.py` + `check_coverage.py` (done, PASS). 3. Phase 2: `CARD-SPEC.md` + palette validation + `build_atlas.py` renderer skeleton. 4. Phase 3: five authoring subagents write `items_d1…d5.py` against this inventory (card ids fixed; agents may not add or drop cards without flagging); renderer emits the HTML. 5. Phase 4: blind auditors (official guide + built HTML only) check coverage of all 288 IDs, factual fidelity, prose rules, no personal data, both analogies present per card. 6. Phase 5: browser verification, screenshots, delivery.")
w("")
w("## 7. Decisions flagged for the checkpoint")
w("")
w("- **Four cards come from the practice test, not the official task statements** (Key Distinctions with no guide bullet): D1-19 two-tool token binding vs `dry_run`; D5-06 behavioural drift vs overflow; D5-07 retrieval vs summarisation for months of history; D5-12 state assumptions vs many clarifying questions. Included by default (the official samples are drawn from that practice test); say the word to drop them.")
w("- **Corpus-only depth not carded** (community guide facts outside the official task statements): `tool_result` carrying `tool_use_id`, prefilling the assistant turn, system prompt as the home of persistent behaviour, bundling requests vs composite tools, the `PreToolUse` name (the guide says \"tool call interception\" without naming the hook — the card uses the guide's wording and mentions the name). Not carded by default to keep the file to what the exam states it tests.")
w("- **KD #4 vs official wording:** the community guide says a same-name personal skill overrides the project skill; the official guide says to create personal variants *with different names*. The card follows the official framing and notes the community claim.")
w("")
w("## 8. Concept inventory")
w("")
for d in ["D1", "D2", "D3", "D4", "D5"]:
    meta = inv.DOMAINS[d]
    w(f"### {d} — {meta['name']} ({meta['weight']}%) · {meta['world_name']}")
    w("")
    w("| Card | Title | Concept (gist) | Guide bullets | KD | Notes |")
    w("|---|---|---|---|---|---|")
    for c in inv.CARDS:
        if not c["id"].startswith(d + "-"):
            continue
        bul = ", ".join(b for b in c["bul"] if not b.startswith("APP")) or "—"
        app = ", ".join(b for b in c["bul"] if b.startswith("APP"))
        if app:
            bul += f" · {app}"
        kd = ", ".join(f"#{k}" for k in c["kd"]) or ""
        note = c.get("note", "")
        if c.get("xref"):
            note = (note + " " if note else "") + "also serves TS " + ", ".join(c["xref"])
        w(f"| {c['id']} | {c['title']} | {c['gist']} | {bul} | {kd} | {note} |")
    w("")
w("### Meta cards (Start / The exam pages)")
w("")
w("| Card | Title | Content |")
w("|---|---|---|")
for c in inv.CARDS:
    if c["id"].startswith("M-"):
        w(f"| {c['id']} | {c['title']} | {c['gist']} |")
w("")
w("## Appendix A — Bullet → card matrix (all 288 IDs)")
w("")
for ts_id, ts_title in TS.items():
    w(f"**TS {ts_id} — {ts_title}**")
    w("")
    w("| ID | Official bullet | Card(s) |")
    w("|---|---|---|")
    for b in data["bullets"]:
        if b["ts"] == ts_id:
            w(f"| {b['id']} | {b['text']} | {', '.join(mapped[b['id']])} |")
    w("")
for label, prefix in [("Appendix — Technologies and Concepts", "APP-T"), ("Appendix — In-Scope Topics", "APP-I"), ("Appendix — Out-of-Scope Topics", "APP-O")]:
    w(f"**{label}**")
    w("")
    w("| ID | Official item | Card(s) |")
    w("|---|---|---|")
    for b in data["bullets"]:
        if b["id"].startswith(prefix):
            w(f"| {b['id']} | {b['text']} | {', '.join(mapped[b['id']])} |")
    w("")

open(OUT, "w", encoding="utf-8").write("\n".join(L))
print("wrote", OUT, "lines", len(L))
