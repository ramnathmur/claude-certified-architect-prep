import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LOG = os.path.join(ROOT, "EXAM-LOG.md")
DATA = json.load(open(os.path.join(HERE, "exam14-data.json"), encoding="utf-8"))

if "## Exam 14" in open(LOG, encoding="utf-8").read():
    sys.exit("Exam 14 entry already present in EXAM-LOG.md — refusing to append a duplicate.")


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


mr = [q for q in DATA["questions"] if q.get("selectN")]

entry = f"""

---

## Exam 14 — Generated 2026-08-11

**File:** `mock-exams/CCA-Prep_MockTest-14_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions) — 47 single-answer + 13 multiple-response
**Scenarios drawn:** Multi-Agent Research System; Developer Productivity with Claude; Claude Code for Continuous Integration; Structured Data Extraction
**Attempt date:** Not yet attempted
**Score source:** Pending
**Total score:** Pending

**Purpose:** a calibration paper. Ram asked for a fresh set of scenarios after sensing the mock exams
had begun repeating themselves. A cold audit of all 720 questions across Exams 2–13 confirmed it — not
in the scenario rotation or the block narratives, which vary correctly, but one layer down, in the
question archetypes. Nine reskinned families were found and are now banned (see
`QUESTION-ARCHETYPE-BANLIST.md`). This paper is the first written under that ban, and its purpose is to
test whether the 49–55/60 band survives when no question shape is recognisable.

**Audit findings that produced this paper:**

| Finding | Measure |
|---|---|
| Scenario rotation | Healthy — all six official scenarios at exactly 8 draws across Exams 2–13 |
| Block narrative variety | Healthy — same-scenario narratives average 0.12–0.16 Jaccard |
| Archetype reskinning | **9 families.** Worst: the dry-run/token-binding question in 7 exams (4, 5, 6, 7, 10, 11, 13); the paired-tool-calls question in 4 (6, 8, 10, 11) at 0.717 Jaccard |
| Closing-line monoculture | **247 of 720 (34.3%)** closed on a "most effective" construction; **81** closed on the byte-identical sentence "What is the most effective fix?" |
| Named-world texture | Collapsed after Exam 3 — correctly, since Phase 4.e.6 check 1 bans invented names and all 12 official samples are generic. Freshness here comes from new industry territory, not proper nouns |
| Item-format gap | **0 multiple-response items in 720 questions**, though the official guide §2 names the format |

**Quota:** base weights — D1 16 / D2 11 / D3 12 / D4 12 / D5 9. No confirmed-weakness adjustment: by
attempt chronology the two most recent scored papers are Exam 9 (weakest D2) and Exam 11 (weakest D5),
different domains, so the two-consecutive-exam gate is not met.

**Scenario rotation:** all six scenarios stood at exactly 8 draws, so the rotation rule could not
discriminate. Selection fell to the never-used-combination rule: of the 15 possible 4-of-6 draws, 8 had
already been used and 7 had not. Four of those 7 are infeasible against this quota — {{CG,DP,CI,SDE}} and
{{CS,CG,CI,SDE}} cannot carry D1 16 with a single D1-primary block, and {{CS,CG,MARS,DP}} has no D4 carrier
at all. Of the four feasible unused draws, this one is the only one where every domain has two carrier
blocks, and it rests both Customer Support and Code Generation from Exam 13.

**Block x domain allocation:**

| Block | Scenario | Primary domains | Allocation | Margin |
|---|---|---|---|---|
| 1 | Multi-Agent Research System | D1, D2, D5 | D1 8 / D2 4 / D5 3 | 3 (no non-primary) |
| 2 | Developer Productivity with Claude | D2, D3, D1 | D1 8 / D2 3 / D3 4 | 3 (no non-primary) |
| 3 | Claude Code for Continuous Integration | D3, D4 | D3 8 / D4 5 / D2 2 | 3 |
| 4 | Structured Data Extraction | D4, D5 | D4 7 / D5 6 / D2 2 | 4 |

**Item formats — new on this paper.** The official exam guide's §2 specification table states the exam
uses "Multiple-choice and multiple-response items; each item states how many responses to select."
None of the guide's 12 sample questions demonstrates the format, and no question across Exams 2–13 used
it, so Ram had never practised it seven days before sitting. This paper carries 13: nine select-2-of-5
and four select-3-of-6, scored all-or-nothing (the guide does not describe partial credit, so the
stricter reading is the safer preparation). This is a deliberate, Ram-approved deviation from
orchestration-prompt v10 Phase 4.e, which specifies "exactly 4 options — 1 correct".

**Multiple-response items:** {', '.join('Q%d (select %d of %d, %s)' % (q['g'], q['selectN'], len(q['options']), q['domain']) for q in mr)}

**Correct-answer letter pre-plan** (single-answer items only — multiple-response items have no single
letter and are excluded from the tally):

| Block | Single-answer items | Tally |
|---|---|---|
| 1 | 12 | A3 B3 C3 D3 |
| 2 | 12 | A3 B3 C3 D3 |
| 3 | 11 | A3 B3 C3 D2 |
| 4 | 12 | A3 B3 C3 D3 |
| **Exam-wide** | **47** | **A12 B12 C12 D11** |

**Fidelity gates — computed, not estimated.** Every prior exam's gates were tallied by hand because
orchestration-prompt v10 assumes no code execution is available. This session had code execution, so the
checks were mechanised as `tools/archetype_gate.py` and run against the shipped HTML:

| # | Check | Computed value | Threshold | Result |
|---|---|---|---|---|
| 1 | No invented names | 0 flagged | 0 | PASS |
| 2 | Letter tally (SA only) | A12 B12 C12 D11 | within 1 of even | PASS |
| 3 | Word counts | stem 42/50/59, option max 21 | median 50–55, caps 95/35 | PASS |
| 4 | Block vs primary domains | margins 3, 3, 3, 4 | every primary > every non-primary | PASS |
| 5 | Inline token rate | 56/257 = 21.8% | 20–25% target | PASS |
| 6 | Multiple-response validity | 13 items, all well-formed | counts stated, whyWrong complete | PASS |
| 7 | Archetype collision (new) | 0 vs 773 prior stems, 0 intra-paper | 0 at/above 0.40 Jaccard | PASS |

The gate caught two real defects during authoring that would otherwise have shipped: Q52 was a 0.431
Jaccard reskin of Exam 12 Q50 (same section, same "two hand-maintained definitions drift apart" shape)
and was rewritten onto §4.8's other half; and the whole paper's stem median was 41 words against a 50–55
band, so all 60 stems were lengthened with concrete situational detail. Validating the gate against the
back catalogue also surfaced three defects in Exam 13 that the by-hand process shipped: one 0.435
collision with Exam 10 Q55, one option at 36 words over the 35 cap, and three repeated closing sentences
inside a single block.

**Industry territory (all new to the project):** clinical-evidence synthesis for a treatment-guideline
panel (block 1); hospital patient-flow tooling — bed allocation, transfers, discharge scheduling (block
2); telecom service-provisioning CI (block 3); agricultural commodity trade documents — inspection
certificates, phytosanitary declarations, weighbridge tickets (block 4). Framing stays generic
throughout: no invented company, product or persona names.

**The four-time miss.** D2 §2.8 (composite tool vs prompt bundling) has been missed on Exams 5, 8, 10
and 11. The audit showed why it never closed: Exam 10 Q6 and Exam 11 Q9 measure 0.717 Jaccard — it was
substantially the same question each time, so a wrong mental model was re-tested rather than re-taught.
It appears here as Q26, a select-3-of-6 built from the opposite end: the composite tool has already been
built and works, and the question is what it costs when a new access pattern arrives. The recalled
slogan does not carry the item.

**QUESTIONS USED (deduplication ledger for Exam 15+):**

"""

for q in DATA["questions"]:
    tag = f"[{q['domain']}]" + (f"[select-{q['selectN']}]" if q.get("selectN") else "")
    entry += f"{q['g']}. {tag} {plain(q['stem'])}\n"

with open(LOG, "a", encoding="utf-8") as fh:
    fh.write(entry)

print(f"appended Exam 14 entry to {LOG}")
print(f"  log size now: {os.path.getsize(LOG)/1024:.1f} KB")
