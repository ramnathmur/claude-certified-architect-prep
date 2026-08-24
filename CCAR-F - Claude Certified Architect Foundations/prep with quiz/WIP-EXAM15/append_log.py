import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LOG = os.path.join(ROOT, "EXAM-LOG.md")
DATA = json.load(open(os.path.join(HERE, "exam15-data.json"), encoding="utf-8"))

if "## Exam 15" in open(LOG, encoding="utf-8").read():
    sys.exit("Exam 15 entry already present in EXAM-LOG.md — refusing to append a duplicate.")


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


mr = [q for q in DATA["questions"] if q.get("selectN")]

entry = f"""

---

## Exam 15 — Generated 2026-08-11

**File:** `mock-exams/CCA-Prep_MockTest-15_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions) — 47 single-answer + 13 multiple-response
**Scenarios drawn:** Customer Support Resolution Agent; Code Generation with Claude Code; Developer Productivity with Claude; Structured Data Extraction
**Attempt date:** Not yet attempted
**Score source:** Pending
**Total score:** Pending

**Purpose:** the companion to Exam 14, generated the same day because Ram had compute expiring. Exam 14
covers the four scenarios it drew; this paper covers the two it rested, so the pair spans the entire
official scenario bank in the final week before the 2026-08-18 sitting. Same difficulty, same ban-list,
same base weighting — its value is breadth, not novelty.

**Quota:** base weights — D1 16 / D2 11 / D3 12 / D4 12 / D5 9. No confirmed-weakness adjustment (Exam 9
weakest D2, Exam 11 weakest D5 — different domains, gate not met).

**Scenario rotation:** Exam 13 had brought all six scenarios level at 8 draws, and Exam 14 left them at
8/8/9/9/9/9, so rotation again offered no tiebreaker. Selection used the never-used-combination rule
introduced for Exam 14. Requiring both of Exam 14's rested scenarios narrows the field hard: of the 15
possible 4-of-6 sets, only two unused ones contain both Customer Support and Code Generation, and
`{{CS, CG, CI, SDE}}` is **infeasible** — Customer Support would be the sole D1-primary block and D1 needs
16 questions in a 15-question block. That leaves exactly one candidate, which is the draw used here.

**Known structural cost of that draw.** Any set containing both Customer Support and Code Generation has
only one D4 carrier, because CS, CG, MARS and Developer Productivity are all non-D4. Structured Data
Extraction therefore absorbs **all twelve** D4 questions in a fifteen-question block. It passes gate 4
comfortably (D4 12 vs D5 3, no non-primary), but that block is 80% one domain, and the arithmetic then
squeezes the rest: Code Generation carries one non-primary D2 question so that Developer Productivity's
D3 count does not fall to 1. Ram was shown this trade-off and chose to accept the skew rather than deviate
from the official weighting or drop Code Generation for a third consecutive paper.

**Block x domain allocation:**

| Block | Scenario | Primary domains | Allocation | Margin |
|---|---|---|---|---|
| 1 | Customer Support Resolution Agent | D1, D2, D5 | D1 8 / D2 5 / D5 2 | 2 (no non-primary) |
| 2 | Code Generation with Claude Code | D3, D5 | D3 10 / D5 4 / D2 1 | 3 |
| 3 | Developer Productivity with Claude | D2, D3, D1 | D1 8 / D2 5 / D3 2 | 2 (no non-primary) |
| 4 | Structured Data Extraction | D4, D5 | D4 12 / D5 3 | 3 (no non-primary) |

**Item formats:** 13 multiple-response (nine select-2-of-5, four select-3-of-6), matching Exam 14's share
so the two papers stay comparable on format. Scored all-or-nothing.

**Correct-answer letter pre-plan** (single-answer items only):

| Block | Single-answer items | Tally |
|---|---|---|
| 1 | 12 | A3 B3 C3 D3 |
| 2 | 12 | A3 B3 C3 D3 |
| 3 | 11 | A3 B3 C3 D2 |
| 4 | 12 | A3 B3 C3 D3 |
| **Exam-wide** | **47** | **A12 B12 C12 D11** |

**Fidelity gates — computed by `tools/archetype_gate.py` on the shipped HTML:**

| # | Check | Computed value | Threshold | Result |
|---|---|---|---|---|
| 1 | No invented names | 0 flagged | 0 | PASS |
| 2 | Letter tally (SA only) | A12 B12 C12 D11 | within 1 of even | PASS |
| 3 | Word counts | stem 46/51/59, option max 23 | median 50–55, caps 95/35 | PASS |
| 4 | Block vs primary domains | margins 2, 3, 2, 3 | every primary > every non-primary | PASS |
| 5 | Inline token rate | 41/257 = 16.0% | 15–30% (target 20–25%) | PASS |
| 6 | Multiple-response validity | 13 items, all well-formed | counts stated, whyWrong complete | PASS |
| 7 | Archetype collision | 0 vs 833 prior stems, 0 intra-paper | 0 at/above 0.40 Jaccard | PASS |

**Note on check 5.** At 16.0% this paper sits in the acceptable band but below Exam 14's 21.8% and below
the 20–25% target. The cause is the draw, not carelessness: inline code and config tokens live naturally
in D2 and D3 options, and this paper's largest block is 12 D4 + 3 D5 with almost no configuration content.
Tokens were not forced into D1/D4/D5 options to raise the number, per the standing rule.

**THE GATE'S BIGGEST CATCH YET — 16 of 60 stems were reskins.** The first assembled draft failed check 7
with **sixteen** stems at or above 0.40 Jaccard against prior exams, two of them at **0.841** (Q21 vs
Exam 13's `/regen-fixtures` skill-scoping question) and **0.821** (Q26 vs Exam 13's context-reduction
question). The cause is PB-23 in its purest form and it is worth recording precisely: this session read
Exam 13's **full 60-stem header ledger** early on, while studying the HTML template in order to extend it
for multiple-response items. Those framings then reappeared in drafting, hours later, without the
authoring step ever consulting them deliberately. All 16 were rebuilt around genuinely different
situations — the corpus point kept, the situation discarded — and the final state is 0 collisions.

**What this proves about PB-23's recommendation (b).** The proposal was to draft from corpus section text
alone and consult prior stems only inside the scan. This session did exactly that at the authoring step
and still produced 16 collisions, because the ledger had entered context earlier for an unrelated reason.
**Recommendation (b) is therefore insufficient on its own and recommendation (a) — the mechanised scan —
is what actually holds the line.** A future session cannot rely on discipline about when it reads the
ledger; it must run the gate.

**Industry territory (all new to the project):** a household energy retailer — billing disputes, meter
readings, tariff switches (block 1); a public-transit ticketing platform — fares, concessions, gate
validation (block 2); a museum collections platform — accession records, conservation logs, loan
agreements (block 3); pharmaceutical batch manufacturing records — executed batch records, deviation
reports, certificates of analysis (block 4). Generic framing throughout; no invented company names.

**Also caught during generation:** Q57's correct answer drifted from its pre-planned letter D to C while
the options were being written. The per-block structural check found it and the options were reordered
without touching content or rationale text, per Phase 4.e.5's method. This is the second exam running in
which the pre-plan caught a real drift, which is the argument for keeping it as a pre-commitment rather
than a post-hoc tally.

**QUESTIONS USED (deduplication ledger for Exam 16+):**

"""
for q in DATA["questions"]:
    tag = f"[{q['domain']}]" + (f"[select-{q['selectN']}]" if q.get("selectN") else "")
    entry += f"{q['g']}. {tag} {plain(q['stem'])}\n"

with open(LOG, "a", encoding="utf-8") as fh:
    fh.write(entry)

print(f"appended Exam 15 entry to {LOG}")
print(f"  log size now: {os.path.getsize(LOG)/1024:.1f} KB")
