# SOP: Mock-Exam Engine — design stance, seeding, dashboard, verification

**Status:** Established. **Reference implementation:** `CCDV-F - Claude Certified Developer
Foundations/prep with quiz/mock-exams/` (template, one generated paper, dashboard) — read that
folder's own `README.md` and `GENERATION-INTELLIGENCE.md` for the full worked history, this SOP is
the extracted, exam-agnostic methodology only. **Origin:** the exam-mode mechanism and item-shape were
first built for CCAR-F; CCDV-F ported them, found and fixed two real defects in the port (below), and
is now the cleaner reference to build from.

**Read this before generating a mock-exam engine, a paper, or a dashboard for any exam folder in this
repo.** Every rule below exists because a plausible alternative was tried and produced a real,
documented defect — the `GENERATION-INTELLIGENCE.md` finding number is cited so you can read the full
account, not just the rule.

---

## 0. What this SOP does and does not cover

**Covers:** the mock-exam *engine* — the HTML/JS mechanics, the item schema, the interaction-mode
design stance, the dashboard, the JSON export format, and the build/verification discipline for all of
it. This is exam-agnostic machinery.

**Does not cover, and must never be used to bypass:** each exam folder's own corpus-verification gate.
Root `CLAUDE.md` §2 ("The verification rule") and §3 ("Corpus discipline") govern what content may
become a question, separately from and prior to anything in this SOP. **Adopting this engine does not
grant permission to generate items.** If the target folder's `EXAM-FACTS_v1.md` has no VERIFIED weight
table, or its `prep with quiz\CCAR-P_Domain-N_v1.md`-equivalent corpus files don't exist yet, build the
engine and its template with demo items only (the three-official-samples pattern, §3 below) and stop
there until the corpus gate clears.

---

## 1. The design stance: Practice Mode is the default, Exam Mode is the exception

**The rule, verbatim from where it was first decided** (CCAR-F `prep with quiz/CLAUDE.md`, "Design
stance," Ram, 2026-07-06):

> per-question feedback is deliberate. The tool optimizes learning-per-question, not exam-condition
> realism. Realism lives in question STYLE, DIFFICULTY, TOPIC COVERAGE, and STRUCTURE — not in
> withholding feedback.

Every paper you generate defaults to **Practice Mode**: full explanation immediately after each
question — right or wrong, why, and the source citation. **Exam Mode** (no per-question feedback, no
live score, 120:00 countdown, no auto-submit at zero) is a **documented, narrow exception** — reserve
it only for a genuine final dress-rehearsal paper close to the real sitting, generated deliberately
that way. There is no runtime toggle by design: pick the mode once, per paper, at generation time, the
same way CCAR-F's own Tests 19–20 were the only two files built with it, out of roughly twenty.

**The failure this prevents (CCDV-F `GENERATION-INTELLIGENCE.md` DV-12):** CCDV-F's first engine build
read the Exam Mode spec, ported the mechanism faithfully, and then hardcoded it as the *only*,
permanent behavior for every future paper — inverting the actual design stance. The mechanism was
built correctly; the mechanism was applied outside the scope its own source document named for it.
**When porting this engine into a new exam folder, port the stated scope with the same rigor as the
mechanism** — a spec that says "exception, these files only" is not evidence that the exception should
become the new default just because it's the fullest documentation available at build time.

Practical checklist when building a template or a paper:
- `const EXAM_MODE = false;` by default, with a comment quoting the design-stance line above.
- The landing-card mode description is rendered from the live `EXAM_MODE` value at boot (via a
  function like `paintChrome()`), never hardcoded static prose — so it can't silently drift out of
  sync with whichever mode a given paper actually runs in.
- The timer, live-score-pill visibility, answer-locking, and post-submit review all branch on
  `EXAM_MODE` too; none of that logic needs to be reinvented — copy it from the CCDV-F reference
  implementation's `CONFIG`, `RENDER`, and `BOOT` anchors.

---

## 2. Item schema and engine mechanics

One item object per question, inside `DATA.questions[]`:

| Field | Notes |
|---|---|
| `g` | 1-based position. Must equal the array index + 1 |
| `domain` | `"D1"`..`"Dn"`, matching the exam's own published domain codes |
| `section` | Skill section `"N.M"`, must sit inside its own domain. **This project's inference, not a published fact** — the guide names domains for sample items, never sections |
| `reviewStatus` | `"gate-verified"` \| `"partial-review"` \| `"unreviewed"` — the source material's own review status, if the corpus has mixed quality (see §4). Omit only when every source is uniformly reviewed |
| `stem` | The scenario. **Multiple-response stems must state their count** — "(Select two.)" — every real exam item does this, so every generated one must too |
| `options` | Array of option strings |
| `correct` | Single-answer: option index. Multiple-response: sorted array of indexes |
| `selectN` | Multiple-response only: how many to select |
| `whyRight` | `{text, cite}` |
| `whyWrong` | `[{option, text, cite}]` — one entry per non-correct option, no exceptions |

**Build the engine's own `validateItems()` self-check and run it on every generated paper.** It should
verify: item count matches the declared `format` (e.g. a `FULL53` paper has exactly 53 items), `g`
sequential with no duplicates, every `domain`/`section` pair resolves and agrees with each other, every
multiple-response stem states its count, every non-correct option has a `whyWrong` entry, every item
has a `whyRight`. This is not optional scaffolding — it is the thing that turns "the paper looks right"
into "the paper is provably not malformed," and it is cheap: CCDV-F Paper 1 ran it via a Node `vm`
harness with zero source changes needed, since the check was already in the file.

**Build discipline for the HTML file itself (DV-01, first found on the CCAR-F reference, confirmed
again on CCDV-F):** any artifact over roughly 40 KB is built as a skeleton first — head, complete CSS,
body structure, empty anchor comments (`/* ==== ITEMS ==== */` etc.) — then filled anchor by anchor
with separate `Edit` calls, roughly 300 lines maximum each. A single large `Write` attempting the whole
file at once has killed the generating agent before with no recovery. Report which anchors were filled,
so a partial failure is visible rather than silent.

---

## 3. Seeding methodology — domain-weighted selection from a mixed-quality corpus

1. **Compute the per-domain item target** from the exam's own published weights applied to the total
   item count (e.g. CCDV-F: 14.7/33.1/3.1/2.6/16.8/11.0/8.1/10.6% of 53 → 8/17/2/1/9/6/4/6 items).
   Round to whole items; the sum should land on the total or within one of it.
2. **Verify the corpus-unit → domain/section mapping against the project's own source-of-truth table
   before dispatching a selection agent — not after.** This is the single most important step in this
   section. CCDV-F `GENERATION-INTELLIGENCE.md` DV-11 documents a real bug: an item-selection brief
   misfiled one chapter into the wrong domain, the selection agent executed that wrong brief perfectly
   (verbatim transcription, correct quota math, zero structural errors), and the defect would have
   shipped silently if nobody had cross-checked the finished selection against the coverage-contract
   table after the fact. **Structural validation (§2) does not catch this class of bug** — it catches
   shape errors, not scope errors. Check the mapping first.
3. **Transcribe items verbatim from the corpus.** Never paraphrase, shorten, or invent wording — this
   is a curation task, not an authoring task. If a corpus unit is missing something a real item needs
   (e.g. an answer key), derive it traceably from the unit's own stated content and flag the item's
   `cite` field explicitly as derived, not source-native (see CCDV-F Paper 1's one Ch13-sourced item
   for the pattern). Never leave a gap silently filled.
4. **Tag `reviewStatus` per item and show it on the item card** whenever the corpus itself has mixed
   review depth (some chapters/domain-files gate-reviewed, others author-only or unreviewed). Prefer
   pulling from higher-review-status sources first when a domain has both available; document in the
   generation log when a domain's quota required reaching into lower-review-status material, and why.
5. **Rotate distractor families** rather than three flavours of the same wrong-answer shape inside one
   item. The CCDV-F reference carries a ten-family rotation (six general, four extracted from the
   exam's own official sample rationales — OVERSPEC, DISCARD, REPAIR, ARCHITECTED, HALF-MOVE,
   WRONG-AXIS, IRRELEVANT-LEVER, UNENFORCEABLE, BIGGER-HAMMER, FALSE-CAPABILITY). Extract a fresh
   family list per exam from that exam's own official sample question rationales when available —
   don't just copy CCDV-F's list wholesale, since the specific families a guide's own samples reject
   are the strongest available signal for what that exam actually tests.

---

## 4. Dashboard

One `mock-exams/DASHBOARD.html` per exam folder, reading `prep with quiz/DASHBOARD-DATA.jsonl`. Static
snapshot baked in at build time (`BAKED_DATA` in the script) because `file://` pages can't reliably
fetch local files — refresh either by asking Claude Code to regenerate `BAKED_DATA` from the current
`.jsonl` + the latest Professor's Note, or by pasting the current `.jsonl` contents into the page's own
"Refresh this view" panel (parses client-side, saves to `localStorage`, nothing uploaded).

Shows, per exam: overview stats (papers generated/attempted/scored, latest estimated scaled score), a
status callout (nothing-scored-yet vs. above/below pass line), the paper list with launch links, a
domain-readiness grid (one card per domain, weight + quota + a percent bar once scored, an honest
"No data yet" state when not), the latest Professor's Note (or an empty-state explanation of what one
is), and a trend chart once 3+ papers are scored — matching each project's own every-3rd-paper insights
cadence.

`DASHBOARD-DATA.jsonl` schema — one JSON object per line, one line per generated paper, written with
nulls at generation time and updated in place when scored. Each exam folder's own `DASHBOARD-SCHEMA.md`
is authoritative for its exact field list (domain codes and count vary by exam), but the shape is
fixed: `paper_n`, `format`, `generated_date`, `attempted_date` (null until sat — **all chronology uses
this field, never `paper_n`**), `score_source`, `total_correct`, `total_questions`, `estimated_scaled`,
`total_seconds`, `single_answer`/`multi_response` as `[correct, of]` pairs, `domain_scores` as
`{"D1": [correct, of], ...}`, `weakest_domain`, `confirmed_weakness`, `insight_round_due`, `mode`
(`"exam"` or `"practice"`, matching §1). Use `[correct, of]` arrays consistently — a prior project drifted
between that and `{"correct": n, "of": m}` mid-build and broke every downstream reader.

**Domain codes, weights, and item counts in `DASHBOARD.html` must be copied from that exam's own
VERIFIED `EXAM-FACTS_v1.md`, never estimated or carried over from a sibling exam.** CCDV-F's dashboard
uses 8 domains at 14.7–33.1% each; a different exam's domain count and weights will differ completely.

---

## 5. Verification discipline in this environment

**The Browser pane's preview server may not see files written in the current session at all** — this
is a real, confirmed environment limitation (CCDV-F `GENERATION-INTELLIGENCE.md` DV-06, extended
2026-08-25), not a file defect. It was caught by navigating to a just-edited file and finding the
server still serving content from a prior session. Do not assume a failed browser check means the file
is broken; do not assume a successful-looking browser check proves the file is fully correct either,
since screenshots have separately been unavailable in this environment (original DV-06).

**What to run instead, every time, before calling a paper or a dashboard done:**
1. JS syntax check: extract the `<script>` block, run it through `new Function(script)` in Node.
2. Run the engine's own `validateItems()` (or equivalent) inside a Node `vm` context with minimal
   `document`/`window`/`localStorage` stubs — this exercises the *actual* production check, not a
   reimplementation of it, and it is the single highest-value verification step available.
3. For a dashboard, simulate its `render()` function the same way, against both an empty-state
   `BAKED_DATA` and a fake scored line pasted through its own refresh path — confirms both branches
   execute without runtime errors.
4. If a real browser check does become available (a working local server, a teammate's machine), still
   do it — it is the one check nothing above can substitute for, particularly for anything visual.

---

## 6. The generation-intelligence ledger

Keep one `GENERATION-INTELLIGENCE.md` per exam folder — an AI-to-AI learning log distinct from
`EXAM-LOG.md` (which is the audit trail of what was *scored*). Findings are numbered permanently
(`DV-NN` for CCDV-F, prefix per exam so numbers never collide when both are read together), never
renumbered, and a closed finding stays in the ledger marked **CLOSED, with what closed it** — the
record of a mistake being fixed is worth more than a tidy list. Add a Session Reflection after every
generation session: what went well, what went wrong and was caught, what's ready for next session.

---

## 7. Adoption checklist for a new or sibling exam folder

1. Confirm `EXAM-FACTS_v1.md` has a real VERIFIED weight table before generating any item — if not,
   stop after step 2 and wait for the corpus gate to clear (root `CLAUDE.md` §2).
2. Copy the CCDV-F reference template's structure (`CONFIG`/`VALIDATE`/`STATE`/`RENDER`/`SCORING`/
   `REVIEW`/`EXPORT`/`BOOT`/`ITEMS` anchors), replacing only: `KEY`, `DOMAIN_NAMES`, `DOMAIN_WEIGHTS`,
   `SECTIONS`, and the landing-card prose — not the mode logic, not `validateItems()`, not the
   dashboard-export shape. Ship it with the exam's own three official sample items (if published) as
   demo content, `EXAM_MODE = false`.
3. Build `mock-exams/README.md` for the new folder, adapted from CCDV-F's — same "Never change these"
   section, same item-shape table, same generation steps.
4. Build `DASHBOARD-SCHEMA.md` and an empty `DASHBOARD-DATA.jsonl` if they don't already exist (both
   already exist for CCAR-P as of the 2026-08-19 restructure — verify their field list against §4
   before reusing).
5. Build `mock-exams/DASHBOARD.html` per §4, baked with whatever `DASHBOARD-DATA.jsonl` actually
   contains at build time (a single null-valued generation line if no paper exists yet).
6. Start `GENERATION-INTELLIGENCE.md` per §6, Session 1 = the engine build, same as CCDV-F's.
7. Only once the corpus gate clears: generate the first real paper following §3, verify per §5, commit.

---

## Changelog

- **2026-08-25** — established, extracted from CCDV-F's mock-exam engine (`mock-exams/README.md`,
  `GENERATION-INTELLIGENCE.md` DV-01/DV-06/DV-09/DV-11/DV-12) after Ram asked for the methodology to be
  reusable from CCAR-P. First adoption target: CCAR-P, gated on its own corpus verification per §0.
