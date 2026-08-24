# CCG Crawl — Local Copy, Curriculum Coverage, and Mock-Test Verdict

**Date:** 2026-08-14
**Trigger:** `anthropic sites.md` (11 URLs)
**Mirror:** `Outputs/ccg-mirror/` — 57 pages, 72,486 words, 0 failures
**Scope of this report:** what was crawled, whether our curriculum covers it, and whether the mock-exam pipeline should be regenerated because of it.

---

## 0. One correction up front

The file is called `anthropic sites.md`, but all 11 URLs point to **claudecertificationguide.com**, a third-party community study site. Nothing in it is published by Anthropic. Its own footer links out to "Anthropic Docs" as a separate destination.

This matters for the mock-test question at the end: our exam corpus is explicitly grounded on the **official Exam Guide PDF v1.0** as primary authority, with live Anthropic docs second and the community guide `source/guide_en.md` third (`prep with quiz/CCA-Prep_Corpus-Index_v2.md`, lines 4–7). This site enters at the same tier as `guide_en.md` — depth and cross-check, never authority.

---

## Part A — Crawl manifest

### What was fetched

| Group | Pages | Words | In `anthropic sites.md`? |
|---|---:|---:|---|
| `/learn` index | 1 | 199 | Yes |
| Domain index pages (5 domains) | 5 | 226 | Yes |
| Exercise pages (5 domains) | 5 | 2,233 | Yes |
| **Lesson pages** | **30** | **57,856** | **No — added** |
| Quick reference (per domain) | 5 | 6,043 | No — added |
| Glossary (per domain) | 5 | 5,154 | No — added |
| Interactive app shells (diagnostic, drill, progress) | 6 | 775 | Partly |
| **Total** | **57** | **72,486** | |

**All 11 listed URLs are mirrored.** I added 40 more pages for a specific reason: the five listed domain pages carry **39–48 words each**. They are tables of contents. The teaching content lives on 30 lesson pages one level down, which the listed URLs only link to. Crawling only the 11 would have produced a local copy containing almost no material.

### Fidelity

Lesson, quick-reference and glossary pages are server-rendered, so the capture is exact — raw HTML in `html/`, `<main>` converted to markdown in `md/`, both retained. Spot-checked `1-1-agentic-loops`: full prose, all four `stop_reason` branch descriptions, both "Exam Trap" panels and the "Current state" note all present.

The five domain index pages and the interactive apps (`/learn/drill`, `/learn/diagnostic`, `/learn/progress`) render their bodies client-side. For those the mirror holds what the server actually returns — the shell plus the task-statement link list. The site's own `/llms-full.txt` (saved to `_site/`) supplies the same index in full, so nothing is lost.

**Not crawled:** the 15 `/blog/*` pages and `/mock-exam` (the site's 254-question bank). Neither appeared in `anthropic sites.md`.

---

## Part B — Coverage matrix against our curriculum

The site's 30 lessons map one-to-one onto the 30 official task statements. I checked them against **`CURRICULUM.md`** (the 8-module training course, v1.0, 2026-06-04).

Legend: ✅ covered · 🟡 partial · ❌ missing.

### Domain 1 — Agentic Architecture (27%) → CURRICULUM Module 1

| Site lesson | CURRICULUM | Evidence |
|---|:--:|---|
| 1.1 Agentic Loops | ✅ | "Agent loop anatomy", "Tool result injection" (CURRICULUM.md:81, 84) |
| 1.2 Multi-Agent Orchestration | ✅ | "Orchestrator pattern" (CURRICULUM.md:82) |
| 1.3 Subagent Invocation & Context Passing | 🟡 | Has "Subagent delegation"; no `Task`/`Agent` tool, no `allowedTools` gate, no `fork_session` (0 hits for `fork_session` in CURRICULUM.md) |
| 1.4 Workflow Enforcement & Handoff | ❌ | No prerequisite gates, no programmatic-vs-prompt enforcement anywhere in Module 1 |
| 1.5 Agent SDK Hooks | ❌ | PreToolUse / PostToolUse appear nowhere in CURRICULUM.md |
| 1.6 Task Decomposition Strategies | 🟡 | "When to delegate" only; no fixed-vs-adaptive split, no attention dilution |
| 1.7 Session State & Resumption | 🟡 | "What to keep, summarise, discard"; 0 hits for `resume` or `fork_session` |

### Domain 2 — Tool Design & MCP (18%) → CURRICULUM Module 4

| Site lesson | CURRICULUM | Evidence |
|---|:--:|---|
| 2.1 Tool Interface Design | ✅ | "Tool description quality", "Tool input schema" (CURRICULUM.md:212–213) |
| 2.2 Structured Error Responses | 🟡 | "Error surface design"; no `isError`, no four error categories, no recovery metadata |
| 2.3 Tool Distribution & `tool_choice` | ❌ | **0 hits for `tool_choice` in CURRICULUM.md.** See Part D — this is the single highest-priority item |
| 2.4 MCP Server Integration | 🟡 | "MCP server anatomy" yes; `.mcp.json` scoping and env-var substitution absent |
| 2.5 Built-in Tools | ✅ | Covered, though filed under Module 2 rather than Module 4 (CURRICULUM.md:127) |

### Domain 3 — Claude Code Config (20%) → CURRICULUM Module 2

| Site lesson | CURRICULUM | Evidence |
|---|:--:|---|
| 3.1 CLAUDE.md Hierarchy & Modular Organisation | 🟡 | Hierarchy yes; `@path` imports and `/memory` absent |
| 3.2 Custom Slash Commands **and Skills** | 🟡 | Slash commands yes; **0 hits for "skills" or "SKILL"** — the entire unified Skills system is missing |
| 3.3 Path-Specific Rules | 🟡 | CURRICULUM says "`[path]` blocks" (line 124). The actual mechanism is `.claude/rules/` with YAML glob frontmatter — **the named mechanism is wrong** |
| 3.4 Plan Mode vs Direct Execution | 🟡 | Plan mode yes; Explore subagent absent (0 hits) |
| 3.5 Iterative Refinement | ❌ | 0 hits for "iterative refinement" |
| 3.6 CI/CD Integration | ✅ | "Non-interactive mode, `--output-format json`, exit codes" (CURRICULUM.md:128) |

### Domain 4 — Prompt Engineering (20%) → CURRICULUM Module 3

| Site lesson | CURRICULUM | Evidence |
|---|:--:|---|
| 4.1 System Prompts with Explicit Criteria | ✅ | "System prompt structure" (CURRICULUM.md:172) |
| 4.2 Few-Shot Prompting | ✅ | (CURRICULUM.md:168) |
| 4.3 Structured Output **with Tool Use** | 🟡 | JSON schema design covered; the `tool_use` + `tool_choice` guarantee mechanism — the actual answer to "what *guarantees* structured output" — is absent |
| 4.4 Validation, Retry & Feedback Loops | ✅ | (CURRICULUM.md:170) |
| 4.5 Batch Processing Strategies | 🟡 | Generic "1000 documents, sampling"; Message Batches API absent (0 hits) |
| 4.6 Multi-Instance & Multi-Pass Review | ❌ | 0 hits for "multi-pass" |

### Domain 5 — Context Management (15%) → CURRICULUM Module 5

| Site lesson | CURRICULUM | Evidence |
|---|:--:|---|
| 5.1 Context Window Management | 🟡 | Compaction yes; "lost in the middle" absent (0 hits); progressive-summarisation trap absent |
| 5.2 Escalation & Ambiguity Resolution | 🟡 | Escalation appears 6× but only as scenario framing, never as valid-vs-unreliable triggers |
| 5.3 Error Propagation in Multi-Agent Systems | 🟡 | "Failure modes" list in Module 1; no structured error context |
| 5.4 Codebase Exploration & Context Degradation | ❌ | 0 hits for "scratchpad"; no crash-recovery manifest |
| 5.5 Human Review & Confidence Calibration | ❌ | One incidental "confidence fields in schema"; no aggregate-metrics trap, no stratified sampling |
| 5.6 Information Provenance | ❌ | 0 hits for "provenance" |

### Tally

**30 lessons: 8 covered, 14 partial, 8 missing.**

### And the reverse direction — four things CURRICULUM teaches that no source supports

This is the more serious finding, because these are not gaps but errors.

1. **The "CALM framework" (Compress, Anchor, Layer, Monitor)** — CURRICULUM.md:255, and Module 5 quiz Q1 asks Ram to recite it from memory. Zero hits across all 57 crawled pages and zero hits across all five corpus domain files. The only "calm" matches anywhere are the ordinary English adjective ("a calm, polite customer"). **This framework does not exist in any source we hold.**
2. **"Choose between stdio and SSE transport"** (CURRICULUM.md:202, 211, and Module 4 quiz Q1) — the official out-of-scope list bars *"Streaming API or server-sent events"* and *"Deploying or hosting MCP servers (infrastructure, networking, containers)"* (`CCA-Prep_Exam-Mechanics_v2.md`). Separately, the site's own glossary now names the second transport **"streamable HTTP"**, not SSE — so the term is stale as well as out of scope.
3. **"Design authentication patterns for MCP servers" / "OAuth, API keys, service accounts"** (CURRICULUM.md:204, 214, quiz Q3) — the out-of-scope list bars *"OAuth, API key rotation, or authentication protocol details"*.
4. **"Implement prompt caching correctly using `cache_control` breakpoints"** (CURRICULUM.md:247, 256, quiz Q2) — the site's D5 glossary states the guide's out-of-scope list caps this at *"knowing it exists"*, so depth beyond static-then-dynamic ordering is not tested. Our curriculum makes it a quizzed implementation skill.

Two smaller ones: Module 1's **"observe-think-act-respond cycle"** (CURRICULUM.md:72) has 0 hits anywhere — the sourced framing is send → inspect `stop_reason` → execute + append → terminate. And Module 0's **"three Claude primitives: Messages API, Tool Use, Streaming"** (CURRICULUM.md:50) includes an out-of-scope topic as a foundational primitive.

### What this actually means

`CURRICULUM.md` is dated 2026-06-04, its progress table stops at 2026-06-06, every score in it is flagged `⚠ synthetic`, and Modules 6 and 7 were never run. The project's real operating curriculum is the corpus under `prep with quiz/` — 73 sections, audited against all 30 task statements, re-verified 2026-08-09. **`CURRICULUM.md` is a superseded artefact that is still sitting in the project root looking current.**

So the honest read is not "our curriculum has 22 gaps." It is: the corpus is in good shape, and `CURRICULUM.md` should be either revised or explicitly marked superseded — because right now it is the only document in the project that would teach you a framework that does not exist and quiz you on three out-of-scope topics.

---

## Part C — What the crawl adds to the mock-exam corpus

I checked the site against the actual generation corpus (`prep with quiz/CCA-Prep_Domain-1..5_v2.md`, `CCA-Prep_Key-Distinctions_v1.md`, `CURRENT-DOCS-DELTA_v1.md`), not against `CURRICULUM.md`.

**New task statements: zero.** The site's 30 lessons are the 30 official task statements. Our corpus covers all 30 at exam depth (audit 2026-07-06, re-verified 2026-08-09) across 73 sections — more granular than the site's 30.

**Where our corpus is already ahead:**

- `stop_reason` — the site adds `pause_turn`, `refusal`, `model_context_window_exceeded` as a "current state" note. `CURRENT-DOCS-DELTA_v1.md` item D2 already carries all three **plus** the `stop_details` object the site omits, with a retrieved-2026-08-09 source URL.
- `tool_choice` — site lesson 2.3 covers `auto` / `any` / `tool`. Corpus covers the same in D2 §2.5, D4 §4.6, and delta item D7.
- Everything in the site's quick-reference and glossary pages maps to existing corpus sections.

**Three genuine deltas:**

| # | Delta | Verified where | Value |
|---|---|---|---|
| 1 | **`Task` tool renamed `Agent`** in current Claude Code (v2.1.63; `Task` still works as an alias) | Site lesson 1.3; corpus D1 §1.2 says only `` `Task` ``, and 0 hits for a rename in any corpus or delta file | Small but real. Add as a delta item, not a corpus rewrite — official framing still says `Task` |
| 2 | **156 "Exam Trap" blocks** across the 30 lessons, versus our **29** Key Distinctions | `grep -c 'Exam Trap'` over the mirror; `CCA-Prep_Key-Distinctions_v1.md` section count | The largest single find. Even with heavy overlap, this is a 5× trap inventory written by an independent author against the same task statements |
| 3 | **11 "Current state" currency notes** flagging where the guide's framing has drifted from live docs | `grep -ic 'current state'` over the mirror | A free cross-check on our own delta file before the 2026-09-08 re-verification deadline |

**One thing to explicitly reject:** the site's D2 glossary says *"The exam may ask about transport selection for specific deployment scenarios."* Our official out-of-scope list bars server-sent events and MCP hosting. **Official framing wins** — this is exactly the [CONFLICT-RISK] situation the generator rule in `CURRENT-DOCS-DELTA_v1.md` exists to handle. Do not let a community source reopen a settled out-of-scope call.

---

## Part D — Mock-test verdict

**Recommendation: do not regenerate. Patch the corpus, then sit Exam 14.**

- **You are not failing on coverage.** Exam 12 scored 53/60 (895), Exam 13 scored 57/60 (955) against a 720 pass line, with D1 at a clean 16/16. Nothing found in 72,486 crawled words changes what is on the exam.
- **The crawl adds no new topic.** Site lessons = the 30 official task statements = what our 73-section corpus already covers. A regeneration triggered by "new material" would be triggered by material we already have.
- **Three exams are already built and unattempted** — 14, 15 and 16, all generated 2026-08-11. Regenerating before sitting any of them discards work the pipeline has already gated.
- **Your actual failure mode is question geometry, not corpus breadth.** `SESSION-STATE.md` names it precisely: five of Exam 12's seven misses are one error — reaching for a compensating mechanism instead of the deterministic fix — spanning four of five domains, which is why *"no domain-weighted quota can target it."* More corpus does not touch that.
- **The `tool_choice` miss is the one thing worth acting on, and it is a repeat.** Exam 13 Q46 repeats Exam 12 Q33 exactly — both ask which configuration *guarantees* a tool call, both offer `auto` + a prompt instruction as the trap and `any` as the key, and the trap was picked both times, 14 hours apart, after reading the full rationale. Site lesson 2.3 and lesson 4.3 teach exactly this distinction from a different author's angle. **Read those two pages before Exam 14** — that is a 15-minute action with a better expected return than a new 60-question paper.
- **The 156 trap blocks are the real deliverable for the generator**, and they feed Exam 17, not a regeneration of anything existing. Mine them for *shapes* — the geometry where a plausible workaround sits attractively beside the correct fix — which is precisely the lever `SESSION-STATE.md` identified and the one the archetype banlist is built to enforce.
- **Two corpus patches, both small:** add the `Task`→`Agent` rename as a new `CURRENT-DOCS-DELTA` item, and add the site to `CCA-Prep_Corpus-Index_v2.md` as a tier-3 depth source alongside `guide_en.md`.
- **One cross-check worth running:** the site's 11 currency notes against our delta file, before the 2026-09-08 re-verification deadline the corpus index already sets.
- **The drill deck remains the real blocker,** and this crawl does not touch it. Its mock map still covers only Exams 2, 3, 4 and the Exam-2 retrofit, so a twice-repeated `tool_choice` miss still cannot become spaced repetition. That is the highest-value fix in the system right now, and it is a plumbing job, not a content job.

### If you want a regeneration anyway

The defensible version is **not** re-running Exams 14–16. It is generating **Exam 17 after sitting Exam 14**, with the `tool_choice` guarantee distinction promoted to the top corpus item (which the Professor's Note for Exam 17 already does) and a block of items whose distractor geometry is drawn from the site's trap inventory. That respects the pipeline's own dedup, quota and archetype gates instead of bypassing them.

---

## Files produced

| Path | What |
|---|---|
| `Outputs/ccg-mirror/` | The local copy — `html/` (57 raw), `md/` (57 converted), `_site/` (llms.txt, llms-full.txt, sitemap, robots), `manifest.json`, `README.md` |
| `Outputs/CCA-Prep_CCG-Crawl-Coverage-Report_v1.md` | This report |

Nothing in `prep with quiz/` was modified. The two corpus patches recommended in Part D are proposals, not applied changes.
