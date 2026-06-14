# GATE 1 — Content Fidelity & Correctness (Independent QA)

**Artifact:** `extensions/orchestration-patterns.html`
**Source of truth:** `extensions/source/orchestration-patterns_citations.md`
**Reviewer role:** AI Professor + Senior Research Analyst (adversarial, did not build this)
**Lesson type:** EXTENSION lesson; ground truth is the citations file (not a captured course)
**Review date:** 2026-06-05

---

## 1. Coverage — per-section table

The citations file has 11 numbered sections + a sources block. The HTML reorganizes them into 11 lesson `<section>`s across 4 dividers plus 2 quizzes and a final check. Mapping:

| Citations section | Present in HTML? | HTML location | Notes |
|---|---|---|---|
| S1 — Workflows vs. Agents | ✅ | Lesson 1 (`#l1`) | Both verbatim definitions present; "who controls the path" takeaway preserved. |
| S2 — Augmented LLM | ✅ | Lesson 2 (`#l2`) | Retrieval/tools/memory + "generate queries, select tools, decide what to retain" present. |
| S3 — Prompt Chaining | ✅ | Lesson 3 (`#l3`) | Definition, gate, when-to-use, both verbatim examples present. |
| S4 — Routing | ✅ | Lesson 4 (`#l4`) | Definition, separation-of-concerns, accuracy precondition, both examples, subagent-description mapping. |
| S5 — Parallelization (sectioning + voting) | ✅ | Lesson 5 (`#l5`) | Both variations defined verbatim; sectioning + voting examples; concurrent-subagents mapping. |
| S6 — Orchestrator-Workers | ✅ | Lesson 6 (`#l6`) | Definition, key-difference-vs-parallelization, when-to-use, examples, Agent-tool verbatim-result mapping. |
| S7 — Evaluator-Optimizer | ✅ | Lesson 7 (`#l7`) | Definition, both fit signals, literary-translation + search examples, tool-restricted-reviewer mapping. |
| S8 — Autonomous Agents (the loop) | ✅ | Lesson 8 (`#l8`) | How-they-operate, ground-truth-each-step, when-to-use, cost/compounding-error caution + sandbox/guardrails. |
| S9 — Decision Framework + ladder | ✅ | Lesson 9 (`#l9`) | Core rule, single-call default, escalation guidance, workflow-vs-agent tradeoff, 7-rung ladder (all 7 rungs, correct order). |
| S10 — Multi-Agent Research System | ✅ | Lesson 10 (`#l10`) | Lead agent, parallel subagents, CitationAgent, compression rationale, effort-scaling table, all headline numbers, economic gate. |
| S11 — Subagents implement patterns | ✅ | Lesson 11 (`#l11`) | What-a-subagent-is, 3 pattern mechanics, YAML frontmatter example, AgentDefinition fields, context-isolation, no-nesting, Workflow-tool graduation, built-in subagents, /agents + precedence. |
| Sources (5 entries) | ✅ | `#sources` | All 5 sources present incl. research-mirror; dates preserved. |

**Coverage gaps (content present in source but NOT in HTML):**

- **MINOR — "3 ways to create subagents" (S11):** The citations file lists three creation methods (programmatic via `agents` param in `query()`; filesystem markdown in `.claude/agents/`; built-in `general-purpose` via Agent tool with no definition). The HTML shows the filesystem method and built-in subagents, but does **not** explicitly enumerate the "three ways to create" trio. The `agents` parameter is mentioned only in the "What's next" teaser. Not a fidelity error — it is forward-deferred to extension S-E2 by design — but worth noting as a coverage trim.
- **MINOR — General-purpose as a creation path:** Source frames `general-purpose` both as a built-in subagent (S11) and as a creation method (no definition needed). HTML covers it only as a built-in. Cosmetic.

No section, pattern, or load-bearing concept is missing. Coverage is effectively complete.

---

## 2. Correctness — load-bearing numbers & quotes

Every flagged figure was checked character-for-character against the citations file.

| Claim | Source value | HTML value | Verdict |
|---|---|---|---|
| Multi-agent (Opus 4 lead + Sonnet 4 subagents) vs single-agent Opus 4, internal research eval | **90.2%** | 90.2% (table + L10 MCQ + Final Q distractors) | ✅ exact |
| Agents vs chat token use | ~**4×** | "about 4× more tokens" | ✅ exact |
| Multi-agent vs chat token use | ~**15×** | "about 15× more tokens" | ✅ exact |
| BrowseComp variance explained by token usage alone | **80%** | "80% (model choice & tool-call count next)" | ✅ exact; "next two factors" correctly characterized |
| Parallelism speedup for complex queries | up to **90%** | "cut research time by up to 90%" | ✅ exact |
| Tool-description rewrite | **40%** decrease in task completion time | "40% decrease in task completion time" | ✅ exact; [VERIFY] retained (see §4) |
| Effort heuristic — simple fact-finding | "1 agent with 3-10 tool calls" | "1 agent with 3-10 tool calls" | ✅ verbatim |
| Effort heuristic — direct comparisons | "2-4 subagents with 10-15 calls each" | "2-4 subagents with 10-15 calls each" | ✅ verbatim |
| Effort heuristic — complex research | "more than 10 subagents with clearly divided responsibilities" | "more than 10 subagents with clearly divided responsibilities" | ✅ verbatim |
| Workflows definition | "predefined code paths" | "predefined code paths" | ✅ verbatim |
| Agents definition | "dynamically direct their own processes and tool usage" | "dynamically direct their own processes and tool usage" | ✅ verbatim |
| Prompt chaining definition | "each LLM call processes the output of the previous one" | identical | ✅ verbatim |
| Routing definition | "classifies an input and directs it to a specialized followup task" | identical | ✅ verbatim |
| Sectioning | "Breaking a task into independent subtasks run in parallel" | "breaking a task into independent subtasks run in parallel" | ✅ verbatim |
| Voting | "Running the same task multiple times to get diverse outputs" | "running the same task multiple times to get diverse outputs" | ✅ verbatim |
| Orchestrator-workers definition | "dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results" | identical | ✅ verbatim |
| Evaluator-optimizer definition | "one LLM call generates a response while another provides evaluation and feedback in a loop" | identical | ✅ verbatim |
| No-nesting constraint | "Subagents cannot spawn their own subagents." | identical | ✅ verbatim |
| Workflow-tool graduation | "dozens to hundreds of agents" → `Workflow` tool, script outside conversation context | identical | ✅ verbatim |
| Context boundary | "The only channel from parent to subagent is the Agent tool's prompt string." | identical | ✅ verbatim |
| Scope precedence | managed(org) → `--agents` CLI → `.claude/agents/` (project) → `~/.claude/agents/` (user) → plugin `agents/` | identical order | ✅ exact |
| Built-in subagents | Explore (Haiku, read-only), Plan (inherits, read-only), General-purpose (inherits, all tools) | identical | ✅ exact |

**Correctness findings:** None. No number is distorted, rounded incorrectly, or detached from its caveat. The 7-rung ladder order in the SVG (1 single-call → 2 chaining → 3 routing → 4 parallelization → 5 orchestrator-workers → 6 evaluator-optimizer → 7 agent loop) matches the source ladder exactly.

---

## 3. Traceability / anti-hallucination

Every factual claim in the HTML was traced to the citations file. **No unlabeled hallucinations found.**

**Author analogies — correctly labeled:**
- L1 railway/taxi-driver analogy is wrapped in `<span class="analogy">Analogy</span>` and explicitly tagged "(Author analogy, not a product fact.)" ✅ Exemplary labeling.
- Footer + sources block both assert "No external facts introduced; author analogies labelled" — accurate self-description.

**Phrasings checked for over-claiming (all clear):**
- "If you remember one pattern↔subagent mapping for the exam, make it this one" (L6) — pedagogical framing, not a factual claim. OK.
- "the exam's favorite distractor" / "high-yield" / "most exam-relevant" — exam-strategy commentary, source-aligned with the citations file's own "most exam-relevant pattern for subagents" note (S6). OK.
- L10 "turns the abstract orchestrator-workers diagram into a shipped system" — paraphrase of source's "production reference architecture." OK.

**MCQ / quiz audit (28 questions total: 11 inline + 5 Quiz A + 8 Final, plus 6 reveals):**
All `data-correct` indices verified against 0-indexed `.opt` order in the JS scorer (`i===correct`). Every correct answer is source-grounded; every explanation traces to the citations file; **no distractor is presented as true.**

Spot-verified high-risk items:
- L10 MCQ (data-correct=2): options 15% / 40% / 90.2% / 4× → index 2 = **90.2%** ✅. Explanation correctly disambiguates 4×, 15×, and 40% as the other figures' meanings — no distractor mislabeled.
- Final Q6 (data-correct=1): "About 4× / About 15× / About 90.2× / About 2×" → index 1 = **15×** ✅; explanation correctly notes 90.2% is the eval improvement, not a token multiplier. The "90.2×" distractor is the right kind of trap (correctly false).
- Final Q8 (data-correct=3): poor-fit = "all agents must share the same context and have many tight dependencies" ✅ verbatim-grounded; other three options are the source's stated *excel* conditions (correctly false distractors).
- Quiz A Q3 (data-correct=3): "Parallelization — voting" for the code-vulnerability example ✅ matches the source's verbatim voting example.
- L5 reveal: same-prompt-thrice-flag-if-any = "Voting" ✅ correct against source.

No traceability defects.

---

## 4. [VERIFY] preservation

The source carries three [VERIFY] obligations. All are preserved as **visible** notes in the rendered HTML (not just comments):

| Source [VERIFY] | Preserved? | Where |
|---|---|---|
| Point-in-time / model-version caveat (Dec-2024 + June-2025 posts >6 mo; numbers tied to Opus 4 / Sonnet 4 + one eval) | ✅ | Hero `.verifynote` (lines 237-239) with `VERIFY` badge — verbatim spirit; **repeated** at L10 verifynote (line 866) tying it to the numbers table. |
| 40% tool-description figure ("confirm the 40% figure refers to the tool-description experiment specifically") | ✅ | L10 table row carries inline `VERIFY` badge (line 862) + dedicated `.verifynote` (line 866) restating the confirmation ask. |
| `Task`→`Agent` rename in Claude Code v2.1.63 ("verify against current version if citing a specific version number") | ✅ | L11 `.verifynote` (line 970): full text — Task→Agent rename, v2.1.63, SDK emits Agent in tool_use but Task in system:init, "Verify against the current version before citing a specific version number." |

All three are rendered as styled, visible callouts (dashed-border `.verifynote` / `.verify` badge), satisfying the "visible notes" requirement. No [VERIFY] flag was dropped or buried.

---

## Severity summary

| Severity | Count | Items |
|---|---|---|
| BLOCKER | 0 | — |
| MAJOR | 0 | — |
| MINOR | 2 | (a) "3 ways to create subagents" trio not enumerated (forward-deferred to S-E2); (b) general-purpose shown only as built-in, not also as a creation path. |

Both MINORs are coverage-trim cosmetics, not fidelity errors. The deferral is explicitly signposted by the "What's next" box.

---

## Verdict

- Coverage: complete (all 11 sections + sources; 2 minor trims, both intentional/deferred).
- Correctness: every load-bearing number and verbatim definition is exact. Zero distortions.
- Traceability: zero unlabeled hallucinations; the one analogy is explicitly labeled; all 28 MCQ answers + explanations are source-grounded with no distractor presented as true.
- [VERIFY]: all three source flags preserved as visible notes.

**GATE 1: PASS**
