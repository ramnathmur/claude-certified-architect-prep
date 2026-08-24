# CCA-F Mock Exam Log

Cross-exam memory. Append a new entry after each exam is generated and after each attempt is scored.  
**Read this file before generating any new exam.** The "Questions Used" lists are the deduplication source.

---

## Exam 1 — Generated 2026-06-27

**File:** `mock-exams/CCA-Prep_MockTest-1_v1.html` — **not present on disk** (checked 2026-07-07; see note)  
**Format:** LEGACY30 (30 standalone questions, pre-v2 blueprint)  
*(Note: Mock Test 1 was generated before this sub-project was set up. Stems are logged here retroactively for deduplication. Its 30 stems remain off-limits regardless of file presence. The file itself was added in a prior commit that is no longer an ancestor of `master` — a pre-existing repository-history gap, unrelated to the mock-exams/ folder reorganization done on 2026-07-07. Regenerating it is not required for deduplication purposes, since its stems are preserved below, but it is not currently openable.)*

**Attempt date:** Not yet attempted  
**Score:** Pending

### Questions Used (deduplication — do not reuse these stems in Exam 2+)

1. A web-search subagent times out mid-task — how does the agent loop know to stop or continue?
2. In a hub-and-spoke research system, two subagents investigate the same subtopics — root cause and fix?
3. PostToolUse hook vs system prompt instruction for enforcing a threshold — which is deterministic?
4. CLAUDE.md at project level vs user level — which guarantees all team members receive the guidance?
5. `-p` flag vs `CLAUDE_HEADLESS=true` for non-interactive Claude Code in CI?
6. Message Batches API for a blocking pre-merge check — why is this wrong?
7. Synthesis agent processes 75K tokens — findings from middle 50K are missed — fix?
8. `context: fork` in skill frontmatter — what does it prevent?
9. `.claude/rules/` with glob patterns vs root CLAUDE.md for path-scoped conventions?
10. Few-shot examples for ambiguous tool selection vs instructions for consistent output format?
11. `stop_reason: "end_turn"` vs `stop_reason: "tool_use"` — when to stop the loop?
12. Coordinator decomposed "AI impact on creative industries" into visual art subtasks only — root cause?
13. Document analysis agent given `fetch_url` starts doing ad-hoc web search — fix?
14. Two-tool token-binding vs `dry_run: boolean` for mandatory preview enforcement?
15. Planning mode vs direct execution for monolith-to-microservices restructure?
16. `--output-format json --json-schema` vs CLAUDE.md output section for structured CI output?
17. Transient (timeout) vs permanent (syntax error) tool failures — different retry strategies?
18. Case-facts block outside summarization vs revising summarization prompt for preserving amounts?
19. Personal skill `~/.claude/skills/commit/` vs `~/.claude/skills/my-commit/` — precedence?
20. Stateless API — why does Claude ask "What genres do you enjoy?" two turns after user said "I love jazz"?
21. Lost in the middle — synthesis agent reliably processes first 15K and last 10K but misses middle 50K?
22. Escalation criteria: competitor price matching when policy only covers own-site price drops?
23. `argument-hint` + `context: fork` + `allowed-tools` — which skill frontmatter fixes which problem?
24. Independent second Claude Code instance vs self-review instructions for catching confirmation bias?
25. Behavioral drift — contractor persona gives generic advice at turn 7, 2,500 tokens only — root cause?
26. Coverage annotations vs error return when 3/5 source categories fail?
27. Explicit per-file review passes vs single-pass full-PR review for 14-file change?
28. `get_customer` programmatic precondition vs prompt instruction for mandatory sequencing?
29. Semantic retrieval vs progressive summarization for 85K-token long-term conversation recall?
30. Explore subagent for verbose discovery vs `/compact` mid-task for preserving main session context?

---

## Exam 2 — Generated 2026-07-06

**File:** `mock-exams/CCA-Prep_MockTest-2_v1.html`  
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)  
**Scenarios drawn:** Customer Support Resolution Agent; Developer Productivity with Claude; Claude Code for Continuous Integration; Structured Data Extraction  
**Attempt date:** Not yet attempted  
**Score source:** Pending  
**Total score:** Pending  

Generated from the v2 corpus via orchestration-prompt v5 logic. Every question carries per-option rationales (whyRight + 3 whyWrong) with corpus citations. Domain quota (across the whole exam): D1 16, D2 11, D3 12, D4 12, D5 9. Dedup verified against Exam 1 (30 stems) and all 76 PRACTICE-TEST-STEMS; 4 near-clones caught in QA and replaced.

### Questions Used (deduplication — do not reuse these stems in Exam 3+)

1. [D1] During Aria's rollout, an engineer builds the agentic loop by hand. After each Claude API call the code must decide whether to run the requested tools and call Claude again, or stop and send the reply to the customer. In staging, some sessions never terminate and keep re-invoking Claude after it has clearly finished answering. What should the loop use to decide whether to continue or stop?
2. [D2] Aria's search_orders MCP tool returns {"results": [], "isError": true} in two very different situations: when a customer genuinely has no orders on file, and when the orders database is unreachable. Logs show that on days the database has brief outages, Aria confidently tells customers "you have no orders," and on legitimately empty accounts it retries and then escalates. How should the tool signal these two outcomes?
3. [D1] Meridian requires that Aria verify a caller's identity with get_customer before any refund is issued. The rule lives only in Aria's system prompt ("always call get_customer before process_refund"). Audit logs show that in roughly 7% of refunds Aria skipped get_customer and called process_refund directly off a customer-supplied order number, twice refunding the wrong account. What change most reliably guarantees the verification step precedes every refund?
4. [D2] Meridian's four support tools run as an MCP server that six engineers use locally while iterating on Aria. Each engineer authenticates to the backend with their own personal API token. The team wants one shared, version-controlled tool configuration without committing any credentials to the repository. Which configuration approach is most effective?
5. [D1] When Aria escalates mid-conversation, Meridian's human agents complain they must re-ask customers for details Aria already gathered — the customer ID, the order, what was tried. The human console shows only that escalate_to_human fired with a short free-text note; it has no access to the conversation transcript. What change most effectively fixes this?
6. [D2] Aria's process_refund tool starts rejecting some refunds because they fall outside Meridian's 30-day return window. The tool currently returns a generic {"error": "Operation failed"}, and logs show Aria retries process_refund up to three times on these rejections before finally escalating. How should the tool's error handling be changed?
7. [D5] To bound cost, Aria keeps only the last 25 message pairs of each conversation verbatim and drops everything older. On long returns cases this backfires: a customer states an accessibility requirement and an agreed store-credit arrangement early on, and 30 turns later Aria contradicts both because those turns have fallen out of the retained window. What is the most effective way to restructure the conversation state?
8. [D5] Aria's lookup_order tool returns 40+ fields per order (warehouse routing, carrier metadata, internal SKUs), but only order_id, status, total, items, and return_eligible matter for support. In long multi-issue sessions the accumulated tool output floods the window and Aria's later answers drift. What is the most effective way to conserve context?
9. [D5] In extended billing conversations, a customer says early on "apply the 15% loyalty discount I was promised," but 20+ turns later Aria quotes the wrong amount. Investigation shows the discount detail was compressed by summarization into a vague note like "promotional pricing was discussed." What fix is most effective?
10. [D5] Meridian wants to raise Aria's first-contact resolution by having it escalate the genuinely hard cases and resolve the rest. A vendor proposes running sentiment analysis on each message and escalating whenever the customer sounds angry. Aria's logs show calm messages describing tangled multi-account billing errors and irate messages about trivially fixable typos. How should escalation be triggered instead?
11. [D1] A customer messages: "This is unacceptable, I've been waiting a week!" Meridian's policy covers this delay with a standard shipping credit that Aria is authorized to issue. Aria's escalation design must decide what to do with this first expression of frustration. What is the most appropriate behavior?
12. [D1] Aria calls get_customer and lookup_order in two separate sequential turns even when a request plainly needs both up front ("refund order #1234 on my account"). This adds an extra API loop to most resolutions and inflates latency at holiday volume. What is the most effective way to reduce the number of loops?
13. [D1] A customer asks Aria to price-match a competitor's lower price. Meridian's written policy covers refunds when Meridian's own price drops after purchase, but says nothing at all about matching other retailers' prices. Aria has already run get_customer and lookup_order and has all available system data. What should Aria do?
14. [D4] Aria still misroutes borderline messages like "I need help with my recent purchase" between get_customer and lookup_order. An engineer plans to add few-shot examples to the system prompt to fix it and asks how to choose them. Which approach most effectively improves selection?
15. [D3] Meridian standardized Aria's operator runbook so every engineer's local Claude Code sessions follow the same review and safety conventions. Three engineers who set this up months ago see the conventions applied; a newly onboarded engineer reports Claude ignores them entirely, though everyone shares the same repository and up-to-date code. What is the most likely cause and fix?
16. [D2] A newly onboarded engineer asks Pathfinder to find everywhere the legacy `computeSurcharge` routine is actually called, so she can understand the billing flow. Pathfinder must decide which built-in tool to reach for first. Telemetry from earlier sessions shows engineers most often want the call sites, not the files whose names resemble the function. Which tool should Pathfinder use to locate the call sites?
17. [D2] The same engineer now wants Pathfinder to map how a shipment record flows from ingestion to invoicing across the unfamiliar integration layer. Session logs show that when Pathfinder tries to Read every file in the integration package first, it fills the context window before it reaches the invoicing code. What investigation strategy should Pathfinder follow?
18. [D2] An engineer must rename the legacy `calculateTax` function everywhere it is used. Investigation reveals that `utils/tax.ts` wraps and re-exports it as `getTax`, and `index.ts` re-exports that wrapper again. Pathfinder greps only for `calculateTax`, reports the call sites it finds, and the engineer proceeds — but a downstream module that imports `getTax` breaks in production. What should Pathfinder have done to find every caller?
19. [D2] Pathfinder is applying a boilerplate change to a large config module and calls Edit with the anchor snippet `return config;`. The Edit fails because that exact text appears in eleven places in the file, so Edit cannot decide which occurrence to modify. What is the correct fallback for a reliable modification?
20. [D2] Meridian wires a semantic, index-backed code-search MCP server into Pathfinder so engineers can find behavior by meaning, not just literal strings. In production, Pathfinder keeps falling back to built-in Grep even for conceptual queries the semantic server handles far better. The MCP tool's description currently reads only "Searches the codebase." What is the most effective fix?
21. [D3] An engineer asks Pathfinder to split the shipping-integration layer out of the Java monolith into its own service — a change that touches dozens of files and forces decisions about service boundaries and shared data models. The engineer is tempted to let Pathfinder start editing immediately. Which execution approach should Pathfinder use?
22. [D3] An engineer asks Pathfinder to generate a boilerplate carrier-integration adapter, described only in prose. After two iterations the generated adapter still shapes its output differently each time — one run nests the tracking fields, another flattens them, and timestamp formats vary. The engineer keeps re-describing the requirements in more detail. What is the most effective next step?
23. [D3] Pathfinder's project CLAUDE.md has grown into a wall of rules. Engineers want the Java files to follow the billing team's exception conventions, the Python routing files to follow async patterns, and the co-located test files to follow one shared testing convention — but only when Pathfinder is actually working on files of that kind. The test files are scattered next to the code they cover. What configuration best applies the right conventions automatically?
24. [D3] The team builds a `/audit-deps` skill that makes Pathfinder do a deep, verbose dependency and coverage scan. Engineers report that after running it mid-task, Pathfinder becomes less responsive and loses track of the original task they were working on, because the scan's large output floods the conversation. How should the skill be configured to fix this while keeping full analysis capability?
25. [D1] An engineer resumes yesterday's named Pathfinder session that had mapped the entire routing service. Overnight, three files in that service were refactored by another team. The engineer wants to continue the investigation efficiently without trusting stale analysis. What is the best way to continue?
26. [D1] After Pathfinder completes an expensive analysis of the billing monolith, the team wants to evaluate two competing refactoring strategies — one that introduces a repository layer and one that keeps direct data access — both starting from that same completed analysis, without the two explorations contaminating each other. What is the most effective approach?
27. [D1] The team asks Pathfinder to add comprehensive test coverage to the legacy shipping-integration layer, whose full scope no one knows in advance — some modules have no tests, some have partial coverage, and hidden external-API dependencies keep surfacing as work proceeds. Which decomposition strategy should Pathfinder use?
28. [D1] Pathfinder generates a batch of migration wrappers and, in its own reasoning trace, notes and then dismisses a possible edge case around null carrier IDs; the bug is only caught later when a human reviews the PR. The team wants to catch these self-dismissed issues automatically before human review. Which approach directly addresses the root cause?
29. [D5] As Pathfinder rolls out to the whole engineering org, long automation sessions start exhausting the context window. The culprit is a `get_build_status` MCP tool that returns 40+ fields per call — build logs, timestamps, runner metadata — when only the status, failing step, and commit hash matter, and every bloated result lingers in context for every later turn. What is the most effective fix?
30. [D4] Across the org, Pathfinder reliably picks the right built-in tool for clear requests, but on genuinely ambiguous asks like "help me understand the recent purchase-order changes" it inconsistently chooses between the semantic MCP search and Grep. The team wants to raise selection accuracy on exactly these ambiguous cases. What few-shot strategy is most effective?
31. [D3] Northwind's first CI job invokes `claude "Review the changed files in this PR for correctness issues"` inside a GitHub Actions step. The job never finishes; the Actions runner eventually times out at the 60-minute limit, and the step logs show Claude Code printed a prompt and then produced no further output. What is the correct way to run Claude Code in this pipeline?
32. [D3] With `-p` working, Northwind's job pipes Claude's review into a script that must open one inline GitHub comment per finding, each carrying a file path, line number, severity, and suggested fix. Claude currently returns prose paragraphs, so the script parses them with brittle regex that breaks whenever wording shifts. What is the most reliable way to get machine-parseable findings?
33. [D4] Northwind's findings are now structured, but developers say the suggested-fix field is uneven: some findings give a concrete diff-level change, others say only 'refactor the retry logic' or 'possible null issue.' The team already added the instruction 'always include a specific, concrete fix suggestion,' yet the output stays inconsistent. Which change most reliably produces consistently actionable fixes?
34. [D4] Northwind's reviewer assigns a severity to each finding, but the prompt only says "rate severity appropriately." Analytics show the same class of issue—an unchecked null dereference—is labelled critical on one PR and medium on another, and developers say the levels feel arbitrary. What change most reliably makes severity ratings consistent across PRs?
35. [D4] Adoption analytics show Northwind's finding categories have very different reliability: correctness findings are dismissed 9% of the time, performance 19%, naming 51%, and documentation 47%. Developer comments say 'half of what it posts is noise, so I skim past all of it.' Trust in the accurate categories is now eroding too. Which approach best restores developer trust while the team improves the noisy categories?
36. [D4] As Northwind fixes the noisy categories, the team wants to learn which specific code constructs drive the naming false positives rather than guessing. Developers dismiss findings frequently but the team cannot aggregate why. What change most effectively lets them analyze which finding types are noise?
37. [D3] Northwind's CI also generates test cases for changed modules. On a PR adding shipment-status tracking, Claude proposes 11 tests, but reviewers note that 7 of them re-test scenarios the existing suite already covers. The generation prompt and CLAUDE.md are thorough. What change most effectively reduces duplicate test suggestions?
38. [D3] When an author pushes follow-up commits to a Northwind PR, the CI re-runs the review from scratch. Developers complain that each re-run re-posts near-duplicate comments on code that was already addressed, with slightly reworded findings piling up on the same lines. What is the most effective way to keep re-runs consistent and stop the duplicate flood?
39. [D3] Northwind wants to cut CI cost by moving analyses to the Message Batches API's 50% discount. Three workloads exist: a style check that blocks PR merge until it completes, a nightly test-generation job for changed modules, and a weekly full-codebase security audit. Which assignment correctly matches each workload to an API approach?
40. [D4] Northwind batches the weekly security audit across 400 changed files. The batch returns with 388 files analyzed and 12 failed on context-limit errors because those files were unusually large. The team needs the results reconciled and the failures reprocessed with minimal cost. How should they handle the partial failure?
41. [D3] Northwind wants CI-invoked Claude to generate tests that match the team's fixture conventions, mock the shared HTTP client the same way every time, and use the project's assertion helpers — yet generated tests keep inventing their own fixtures and ad-hoc mocks. The pipeline invokes Claude with only the changed diff and a short prompt. What most reliably makes generated tests follow the team's conventions?
42. [D1] Northwind wants a new CI job that adds comprehensive tests to a large legacy module with no existing coverage; the full scope is unknown up front, and each area's needs depend on what earlier exploration reveals (some sub-modules have hidden external-API dependencies). An engineer proposes a fixed pipeline: enumerate every file, then generate tests for each in a predetermined order. Which decomposition strategy fits this task?
43. [D1] A Northwind PR touches 16 files in the routing engine. A single review pass over all files at once gives deep feedback on a few files and shallow feedback on the rest, misses an obvious off-by-one bug, and flags a pattern in one file while approving the identical pattern in another. How should the team restructure the review?
44. [D1] In Northwind's review flow, the same Claude session that generates a suggested refactor is then asked, in that same conversation, to 'review your change carefully for bugs before finishing.' Subtle bugs the model reasoned about during generation still reach production — its self-review consistently reaffirms its original approach. What most directly addresses this self-check limitation?
45. [D2] Northwind's CI reviewer reads Unix epoch timestamps from a `git_blame` tool, ISO 8601 dates from a `pr_metadata` tool, and numeric CI status codes (1=queued, 2=running, 3=passed) from a third-party build tool it cannot modify. The reviewer keeps misreading these mixed formats when it composes feedback. What is the most maintainable way to normalize the tool outputs?
46. [D4] Ledgerline's extraction schema marks every field — including purchase_order_number and tax_id — as required and non-nullable, reasoning that downstream ERP posting needs a complete record. In a 5,000-invoice audit, 11% of outputs carry a plausible-looking PO number that appears nowhere in the source document; those invoices simply had no PO. What schema change most directly stops this?
47. [D2] Incoming documents are a mix of invoices, receipts, and PO confirmations, and the pipeline must ALWAYS hand the ERP schema-valid JSON — never a prose reply. The team defined three extraction tools (one per document type) but sometimes Claude answers a hard-to-classify scan with an explanatory paragraph instead of calling any tool. Which configuration guarantees a structured tool call every time?
48. [D4] After moving extraction to tool_use with strict JSON schemas, Ledgerline's JSON parse failures dropped to zero. But the downstream ERP reconciliation still rejects about 3% of invoices because the extracted total does not equal the sum of the extracted line items. An engineer proposes tightening the schema further to "catch" the mismatches. How should the team interpret this?
49. [D4] The validate-then-retry loop resubmits a failed extraction with the document, the previous output, and the specific validation error. It works well for format and arithmetic errors. But on 40 documents, purchase_order_number keeps failing validation across all 3 retries; investigation shows those documents never contained a PO number at all. An engineer wants to raise max retries from 3 to 10. What should the team do instead?
50. [D4] Weeks after posting, monthly reconciliation keeps surfacing invoices where the extracted total silently disagrees with the line items — sometimes the model grabbed a subtotal, sometimes the source invoice itself was internally inconsistent. The team wants to catch these at extraction time, not weeks later. What extraction design catches this?
51. [D2] Ledgerline's process_payment_hold tool rejects a hold because the invoice amount exceeds the client's per-invoice auto-hold policy limit. The extraction agent keeps re-calling the tool, treating the rejection like a transient outage, and burns retries. How should the tool's error handling be structured?
52. [D4] Ledgerline needs to reprocess a 240,000-document monthly archive for a new client, with results due by 9 a.m. the next day — no human is waiting per-document. The team plans to use the Message Batches API for the 50% savings. Before committing all 240,000 documents, what is the most effective way to de-risk the run?
53. [D3] One client's onboarding step runs extraction from a nightly CI job that shells out to the Claude Code CLI in --print mode, then posts the parsed fields to the client's ERP via an API call. The job intermittently breaks because the CLI sometimes returns a prose preamble around the JSON, so the parser chokes. What is the most reliable way to get downstream-parseable output?
54. [D5] Ledgerline's extraction reports 97% overall accuracy on a labeled audit, and the team proposes auto-processing every high-confidence extraction with no human review. A skeptical lead notes that handwritten-receipt scans are a small fraction of volume. Before turning off review, what should the team do first?
55. [D5] To route extractions to human review, Ledgerline has the model emit a single 1–10 confidence score per document and reviews anything under 8. Reviewers report that many "high-confidence" extractions are still wrong on specific fields, while some flagged documents are perfectly fine. What is the most effective redesign of the confidence signal?
56. [D5] Each lookup_vendor call in Ledgerline's enrichment step returns 40+ fields (full address history, tax registrations, contact log), but only vendor_id, name, and remit_to matter for extraction. On long multi-invoice sessions, the context fills with these fields turn after turn, and the model starts confusing remit-to addresses. What is the most effective fix?
57. [D5] Downstream auditors need every extracted figure traced to where it came from: the source document name, the page, and the extraction date. Currently the merge step that combines multi-page invoice data into one record flattens everything to prose, and a general "sources reviewed" note is appended at the end. Auditors can no longer tie a specific total back to a specific page. What is the correct fix?
58. [D1] Ledgerline is redesigning extraction as a multi-agent pipeline: a coordinator delegates classification, extraction, and validation to specialized subagents. The validation subagent needs the extraction subagent's output to check it, but currently it receives nothing and reports "no data to validate." What is the root cause and fix?
59. [D1] When a document extraction subagent hits a password-protected PDF it cannot open, it currently returns a bare "failed" status to the coordinator, which then can't decide whether to retry, skip, or route to manual handling. The team wants the coordinator to make intelligent recovery decisions. How should the subagent report the failure?
60. [D1] A single client submits a bundled packet each night: an invoice, a matching receipt, and a delivery-confirmation report, all needing extraction plus a three-way match. The coordinator currently extracts them strictly one after another, and end-to-end latency has become the client's top complaint even though each extraction succeeds. The three documents are independent to extract. What most effectively reduces latency?

---

### Retrofit Note — Mock Test 2, Fidelity Retrofit (2026-07-09)

**File:** `mock-exams/CCA-Prep_MockTest-2-Retrofit_v1.html`  
**Not a new exam number** — deliberately NOT a `## Exam N` heading, so it does not affect the exams_generated count or the highest-N calculation Phase 1 uses to determine the next exam number. This is a standalone study copy of Exam 2's same 60 questions, retrofitted to the fidelity philosophy that also produced Orchestration Prompt v9 (see `CLAUDE.md` v2.3 changelog and `GENERATION-INTELLIGENCE.md` PB-08–PB-11). The original `CCA-Prep_MockTest-2_v1.html` is untouched and remains the historical record; the "Questions Used" list under Exam 2 above still governs deduplication.  
**Attempt date:** Not yet attempted  
**Score:** Pending

Applied fixes, verified against the live embedded JSON (not asserted): removed all invented company/agent names (Meridian/Aria/Pathfinder/Northwind/Ledgerline → generic framing, e.g. "your agent", "the team", "Claude Code"); rebalanced the correct-answer letter distribution from A=20/B=17/C=11/D=12 to an exact 15/15/15/15 exam-wide (options reordered only — content, rationales, and correctness unchanged); raised the backtick-styled inline code/config token rate from 9.6% to 20.8% by wrapping identifiers already present in the option text, no invented content; added the scenario-rotation disclosure line to the landing card. Domain-tally-vs-primary-domains and the word-count budget were already passing in the original and needed no fix. One known, accepted residual gap: stem word-count median rose from 55.5 to 57.0 words as a side effect of the name substitutions (target band 50–55; still well under the 95-word hard cap) — not chased further to avoid re-editing risk. Three grammar/logic breaks introduced by the mechanical substitution pass (a "named your agent" phrase, a false claim that the team "builds Claude Code," and a garbled "named Claude Code session" reference) were caught by a full-file scan and hand-fixed before shipping.

No separate "Questions Used" dedup list — these are the same 60 underlying questions already logged under Exam 2 above, reworded only; that entry's stem list already covers them for dedup purposes. Not written to `DASHBOARD-DATA.jsonl` for the same reason this isn't a `## Exam N` entry — that file's schema is keyed by exam_n and isn't meant to carry a second "2".

---

## Exam 3 — Generated 2026-07-07

**File:** `mock-exams/CCA-Prep_MockTest-3_v1.html`  
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)  
**Scenarios drawn:** Multi-Agent Research System; Code Generation with Claude Code; Claude Code for Continuous Integration; Structured Data Extraction  
**Attempt date:** Not yet attempted  
**Score source:** Pending  
**Total score:** Pending  

First standalone run of orchestration-prompt v6, invoked as a genuine cold `/cca-exam` execution (no shared session context) rather than hand-orchestrated by Ram's session. The dispatched agent independently delegated question-authoring to 4 parallel sub-agents -- the same architecture used for Exam 2, converged on with no awareness Exam 2 was built that way. Domain quota (across the whole exam): D1 16, D2 11, D3 12, D4 12, D5 9. Dedup verified against all 90 Exam-1+Exam-2 stems and all 76 PRACTICE-TEST-STEMS (166 total), zero overlaps at Jaccard>0.40. One defect caught and fixed before shipping: Block D (Structured Data Extraction) shipped all 15 questions with the correct answer at option A -- reshuffled to a balanced distribution (aggregate exam-wide: A=16, B=15, C=15, D=14) without altering any question content. See GENERATION-INTELLIGENCE.md Session 2 for the full account, including two coordination issues found in the nested-agent delegation itself.

### Questions Used (deduplication — do not reuse these stems in Exam 4+)

1. [D1] Compendium's coordinator, Halcyon, is being configured for a new client request: a cross-jurisdiction report on renewable-energy grid-storage policy. The current coordinator prompt reads like a script: "Step 1: query the EU, US, and Japan regulatory trackers. Step 2: open the first 10 filings from each. Step 3: summarize each filing in 150 words." QA shows the report is thin and misses a major policy shift that only became visible after the subagents' first pass. Which change to Halcyon's prompt is most effective?
2. [D1] Halcyon delegates the grid-storage research and every subagent completes successfully: Scanline (web-search) finds relevant articles, Foliant (document-analysis) summarizes filings correctly, and Weftloom (synthesis) produces a coherent draft. The final report, however, covers only lithium-ion battery chemistry advances and says nothing about interconnection permitting, financing incentives, or utility procurement rules. Halcyon's logs show it decomposed the topic into three subtasks: "battery cost trends," "battery cycle-life research," and "battery recycling policy." What is the most likely root cause?
3. [D1] Compendium's final grid-storage report states "Battery storage deployment increased 28% year-over-year" with no source attached. Tracing the pipeline shows that Scanline and Foliant both returned their findings as long free-text paragraphs, which Halcyon concatenated and forwarded to Weftloom as one merged block. What is the most effective fix for the missing citations?
4. [D2] Scanline is now working against RegTrack, a third-party regulatory-filing index covering all three jurisdictions in the grid-storage project. Telemetry shows Scanline burns 6-8 tool calls per session issuing guessed `search_filings` queries just to figure out what filing categories even exist in RegTrack before it can search productively. RegTrack exposes a filing-category index as part of its MCP server. What is the most effective way to reduce this exploratory overhead?
5. [D1] Weftloom's first synthesis draft on the grid-storage report reads as coherent but Halcyon's own review catches that it never addresses financing-incentive mechanisms at all, even though Foliant separately logged several relevant filings on the topic earlier. What should Halcyon do next?
6. [D5] Foliant is comparing two credible sources on grid-storage capacity growth: a national energy-ministry report states 34% year-over-year growth, while an independent grid-operator association study states 19% for the same period. Both documents pass Foliant's credibility checks and the discrepancy could change which policy recommendation the report ultimately makes. What should Foliant do?
7. [D2] Compendium's finance team is worried that a poorly scoped research request could trigger a paid RegTrack API tier upgrade if Scanline's cumulative document-retrieval calls exceed 5,000 in a single project — an outcome the team wants blocked outright, not merely discouraged. Halcyon's system prompt currently says "avoid excessive retrieval calls; stay mindful of cost." Which change most reliably prevents the threshold from being crossed?
8. [D1] Foliant's query against RegTrack for the Japan jurisdiction fails outright: the jurisdiction code the coordinator passed down, "JPN," doesn't match RegTrack's expected two-letter code "JP," so the query is rejected as malformed before it ever runs. Foliant currently returns only `{"status": "failed"}` to Halcyon, which then cannot tell whether retrying is worth attempting. What should Foliant's failure report include instead?
9. [D2] Foliant's document-intake step must always begin by calling `extract_filing_metadata` before any deeper analysis tool runs, because downstream steps depend on knowing the filing's jurisdiction and date first. With `tool_choice` left at its default, Foliant sometimes skips straight to an analysis tool without extracting metadata first, about 12% of the time. What configuration most reliably guarantees the correct first step?
10. [D1] Weftloom increasingly needs to verify individual facts (a filing date, a named agency, a cited percentage) while drafting synthesis text. Analysis shows 90% of these are simple, single-fact lookups and 10% require deeper cross-referencing across multiple filings. Currently every verification, simple or complex, routes back through Halcyon to Foliant and Scanline, adding a full extra loop each time. What is the most effective tool configuration for Weftloom?
11. [D2] Compendium's engineering team is scoping Scanline's tooling and discovers that a well-maintained community MCP server already exists for querying the U.S. Federal Register — the exact source Scanline needs for one jurisdiction. A team member proposes building a custom Federal Register MCP server from scratch instead, arguing it would give the team full control over the integration. What is the most effective approach?
12. [D5] Weftloom's draft states: "A 2022 industry survey found grid-storage capacity growth of 11%, while a 2024 regulatory filing puts growth at 17% — a contradiction that undermines confidence in the trend." Both figures came from credible sources that Foliant tagged with different collection years, but Weftloom's output flags them as conflicting rather than as sequential data points. What is the most effective fix?
13. [D1] Halcyon hits a policy question it cannot resolve on its own: the client's research brief is silent on whether Compendium should include proprietary industry-consortium data behind a paywall, and getting it wrong could mean a licensing violation. Halcyon escalates to a human research director who has no access to the underlying agent conversation. What must the escalation payload include to avoid the director having to reconstruct context from scratch?
14. [D2] Compendium wires a semantic, citation-aware filing-search MCP server into Foliant so it can find relevant passages by legal and regulatory meaning rather than exact keyword match. In production, Foliant keeps falling back to a generic `fetch_url` call to grab whole filing pages instead of using the semantic server, even on queries the semantic tool is built to handle far better. The MCP tool's description currently reads only "Searches filings and returns matches." What is the most effective fix?
15. [D5] Weftloom's input for the grid-storage synthesis totals 118K tokens: Scanline's raw web pages and full search reasoning make up 64K, Foliant's complete filing excerpts and analysis notes make up 54K. QA finds Weftloom's draft cites Scanline's opening search summary and Foliant's closing recommendations accurately, but omits a load-bearing interconnection-permitting finding that sat in the middle of Foliant's output. Recommended synthesis inputs top out near 45K tokens. What is the most effective fix?
16. [D3] Fernbank's expense-reconciliation platform, Ostrakon, has an engineer, Priya, who personally built a `/recon-trace` slash command at `~/.claude/commands/recon-trace.md` to trace a transaction through the matching pipeline. The rest of the eight-person team likes it after watching her demo it and wants `/recon-trace` available automatically to everyone the moment they clone or pull the repo, with no per-developer setup. Where should the command file live to achieve this?
17. [D3] Ostrakon's team maintains a shared `/close-books` skill at `.claude/skills/close-books/SKILL.md` for the month-end reconciliation checklist. A new hire, Devon, clones the repo, then also copies a `close-books` skill folder from an old personal project into his own `~/.claude/skills/`, not realizing the name collides. When Devon runs `/close-books`, he gets different behavior than the rest of the team and can't figure out why, since his repo checkout is identical to everyone else's. What is the most likely cause?
18. [D3] A merchant-data vendor Ostrakon depends on just changed its category-code rules for the third time this quarter, and Priya is asked to have Claude Code build a re-categorization layer for multi-currency transactions before the next feed lands. She has never worked in this vendor's taxonomy before and worries she doesn't know what edge cases matter. Her first attempt at a prompt just describes the goal in one paragraph and asks Claude Code to implement it directly. Which approach is most effective for her next attempt?
19. [D5] Ostrakon has accumulated fourteen vendor-feed adapter modules over two years, several written by contractors long gone, and the team suspects heavy duplicated logic across them before committing to a consolidation plan. Priya asks Claude Code to survey all fourteen directly in her main working session; the resulting comparison — module-by-module notes and overlap candidates — grows so large the context window is nearly full before she can even discuss which adapters to merge first. What is the most effective way to complete the survey while preserving context for the consolidation design conversation?
20. [D1] After Claude Code finishes a full architectural analysis of Ostrakon's settlement-retry logic, Priya's team wants to evaluate two competing designs for making retries idempotent: one based on a client-generated idempotency key stored per request, the other based on a server-side dedup window keyed on transaction hash. Both designs should start from the same completed settlement-retry analysis, and the team wants to avoid paying for that expensive analysis twice or having the two evaluations bias each other. What is the most effective way to proceed?
21. [D3] Fernbank's compliance team wants a nightly job where Claude Code reviews the day's reconciliation-engine commits and automatically opens a ticket in Ostrakon's internal tracker for every finding, with each ticket requiring a module path, line number, severity level, and a one-line remediation note as distinct fields the ticketing API expects. The team's first attempt just prompts Claude Code to "list findings in a clear, structured way," and the ticket-creation script frequently fails to parse the output into those four fields. Which approach is most effective?
22. [D2] Ostrakon's dev tools expose two MCP tools to Claude Code: `flag_ledger_entry`, for marking one transaction row as needing manual review, and `flag_reconciliation_run`, for marking an entire nightly batch as needing review. Both descriptions currently read only "Flags an item for review." Telemetry shows Claude Code calls `flag_ledger_entry` when a developer actually wants to flag the whole run about a third of the time, since both accept a numeric ID and the descriptions give no way to distinguish scope. How should this misrouting problem be fixed?
23. [D3] Ostrakon's reconciliation matcher occasionally leaves a one-cent residual unmatched when a refund is split across two partial settlements in different currencies, because the rounding happens in a different order than the original charge used. Priya has described the bug to Claude Code twice in prose ("make sure split-currency refunds round the same way the original charge did"), and each attempt fixes the specific split ratio she mentioned but leaves other split ratios still off by a cent. What is the most effective next step?
24. [D5] Ostrakon's architecture channel has hosted a running design discussion for eleven weeks about how the ledger should represent multi-currency balances, with the conversation history now well past 90,000 tokens across many sessions. A new engineer asks Claude, "Why did we settle on storing balances in minor units instead of decimal, again?" — a decision made and justified in detail back in week 3, buried among many later, unrelated tangents. What is the most effective way to answer this kind of question reliably?
25. [D3] Ostrakon's project CLAUDE.md already states universal rules the whole team follows on every task — for example, "all monetary values are integers in minor units, never floats." The team also runs a quarterly-close procedure: a specific multi-step checklist (freeze the ledger, reconcile outstanding batches, generate the compliance export, notify finance) that only applies during the close window, a few days per quarter, and nobody wants that checklist loaded into every session's context the rest of the year. Which restructuring approach is most effective?
26. [D3] Ostrakon is splitting into three packages (`ledger-core`, `recon-engine`, `finance-export`), each with its own maintainers and coding standards file. The root CLAUDE.md currently pastes the full text of all three standards documents inline, so every engineer's session loads all three regardless of which package they're touching. The `finance-export` maintainers want their package's CLAUDE.md to pull in only their own standards file, not the other two, while still keeping that content in the context Claude sees. Which approach best achieves this?
27. [D4] Ostrakon's automated code-review pass for reconciliation-matcher changes is instructed to "flag risky changes to the matching logic." Reviewing three recent PRs, the same class of change — widening a currency-comparison tolerance from 0.001 to 0.01 — is flagged as high severity in one PR and left uncommented in another, with no clear pattern to which PR gets flagged. Which change most reliably makes the flagging consistent?
28. [D3] A review of Ostrakon's settlement module turns up three issues in one function at once: a race condition in how the retry lock is acquired, a backoff calculation that assumes the old locking behavior and will misbehave once the lock logic changes, and an unrelated log message with a typo. Priya is deciding how to hand these findings to Claude Code for fixing. Which approach is most effective?
29. [D1] Claude Code fixes a flaky integration test in Ostrakon's settlement-retry suite by loosening an assertion that compared exact retry counts to a range check instead. In its own reasoning it considers whether this masks a real timing bug, and concludes the range check is safe because retries are inherently variable. The change ships; weeks later, an incident review finds the range check was hiding a real race condition that occasionally double-submits a settlement. Which approach most directly addresses this self-check limitation?
30. [D5] Ostrakon's team is migrating the settlement module off a deprecated retry library across roughly 70 call sites, a multi-day effort involving many Claude Code tool calls to locate, evaluate, and update each site. Midway through day two, Priya's laptop restarts unexpectedly and the session is lost. She doesn't want to re-discover which call sites were already migrated and which weren't, and wants to resume efficiently from wherever the work actually stood. What is the most effective way to design the migration so it survives an interruption like this?
31. [D3] Solstice Freight's engineering team runs its CI review pipeline, internally named Vanguard, as a scheduled stage in their freight-routing monorepo's build system: `claude "Review the changed files in this build for correctness issues"` is invoked as a build step rather than a one-off script. Over two weeks, the runner pool backing this stage slowly saturates — queue depth climbs from 2 to 40 pending jobs — because each Vanguard invocation never exits on its own; operators have to manually kill the process after it sits idle. What is the correct way to run Claude Code so this pipeline stage completes and releases its runner?
32. [D1] With `-p` now fixed, Vanguard runs three independent analyses on every PR to the freight-routing monorepo: a style check, a security scan, and a performance review. The pipeline currently invokes Claude Code three times in sequence within one orchestrating session — style, then security, then performance — and the stage now takes 9 minutes end to end even though none of the three analyses depends on another's output. Engineers want to cut wall-clock time without losing any of the three analyses. What is the most effective architectural change?
33. [D4] Vanguard's security-scan analysis includes a cross-service consistency check: it compares the retry-and-backoff logic across Solstice Freight's five microservices (dispatch, tracking, billing, notifications, and routing) to flag services whose retry budgets have silently diverged from the others. On PRs touching two or more of these services, the check frequently misidentifies which service is the outlier, sometimes flagging the one service that actually matches the majority pattern. The comparison genuinely requires reasoning through five services' worth of retry-budget values before concluding which ones diverge. What change would most reliably improve accuracy on this specific check?
34. [D3] Vanguard's root CLAUDE.md has grown to cover universal style conventions that apply to every PR, plus a rarely-invoked deploy-hotfix procedure (used a few times a year during incident response) and a database-migration rollback checklist (used only when a migration needs reverting). Every Vanguard invocation loads the full file, and engineers report the hotfix and rollback sections add noticeable irrelevant context to routine style-and-security PR reviews. Which restructuring most effectively keeps universal conventions always available while loading the rare procedures only when actually needed?
35. [D4] Vanguard's finding-reporting tool defines its own hand-written JSON schema for structured findings (file, line, severity, description, suggested_fix), and a separate internal validation script checks incoming findings against a second, independently maintained set of field definitions. Twice in the last quarter, someone updated one definition (adding a `detected_pattern` field) without updating the other, and findings silently failed validation in production until the mismatch was traced. What change most directly prevents this class of drift going forward?
36. [D5] Vanguard calls a `get_pr_diff` tool at the start of every review to fetch the changed files. The tool returns 50+ fields per invocation — full commit metadata, author history, CI runner IDs, branch protection settings — when only the file path, diff hunk, and change type matter for the actual review. On PRs that touch many files, engineers notice review quality degrading partway through as the accumulated tool output crowds the context, and Vanguard's later comments start referencing the wrong file. What is the most effective fix?
37. [D4] Vanguard's review currently uses one prompt that asks Claude to both identify issues in the diff and immediately propose a fix for each one in the same response. Reviewers notice that on PRs with several interacting issues, the proposed fixes are sometimes shallow or miss an issue's downstream implications, as if fix-generation is being rushed alongside issue-identification. An engineer wants Claude to reason more thoroughly about each fix without changing what issues get flagged. What is the most effective restructuring?
38. [D1] Solstice Freight assigns Vanguard a new initiative: backfill test coverage for the legacy webhook-retry module, which has no owner and no documentation. Nobody knows up front how many retry paths exist, which ones are already covered, or whether the module depends on anything external. An engineer proposes a fixed pipeline: enumerate every function in the module first, then generate a test for each one in file order. Partway through, Vanguard discovers the module silently depends on an internal rate-limiter service that must be mocked before several of the retry paths can be tested at all. Which decomposition strategy best fits this task from the outset?
39. [D1] Weeks after the webhook-retry test backfill merges, a race condition surfaces in production: two retry attempts fire concurrently under load and double-post the same webhook. The original Claude Code session that wrote the retry-and-lock fix, still open, is asked in that same conversation to "double-check your fix for any thread-safety issues before we close this out" — it re-examines its own change and reports the locking approach is sound. A human reviewer, looking at the diff cold days later, spots the race immediately. What most directly addresses why the same-session check missed it?
40. [D4] Vanguard has recently added two new finding categories beyond its original correctness and style checks: `dependency-upgrade-risk` (flagging PRs that bump a dependency with known breaking changes) and `test-coverage-gap` (flagging changed code with no corresponding new test). Three months of dismissal data show `dependency-upgrade-risk` findings are dismissed 61% of the time and `test-coverage-gap` findings 55% of the time, while the original correctness findings are dismissed only 6% and style findings 22%. Developers report they've started skimming past dependency and coverage findings entirely, and now catch themselves skimming past correctness findings too out of habit. Which approach best restores trust while the two new categories are improved?
41. [D4] Solstice Freight's five microservices share a near-identical pattern for validating incoming webhook payloads, copy-pasted years ago with minor variations. When a PR fixes a payload-validation bug in the dispatch service, Vanguard's review — running per-service as each one gets touched over the following days — independently proposes the exact same fix again on tracking, then again on billing, even though the team already applied and merged the dispatch fix using the identical approach across services deliberately. Developers say re-reviewing the same already-known fix three more times wastes time. What is the most effective way to stop Vanguard from re-suggesting a fix that has already been applied elsewhere?
42. [D3] Solstice Freight wants Vanguard's findings to auto-populate an internal engineering-metrics dashboard (tracking finding counts, categories, and resolution time per team) via a nightly ingestion job that calls a REST endpoint. Vanguard currently prints narrative prose to stdout, and the ingestion job's parser — built to expect a specific field set for the dashboard's schema — regularly throws validation errors and drops entire nights of data whenever Claude's phrasing varies. What change most reliably produces output the ingestion job can consume?
43. [D3] Solstice Freight schedules a full-repository dependency and security audit across the entire freight-routing monorepo to run weekly via the Message Batches API, taking advantage of the 50% cost savings since the audit isn't blocking anyone. Leadership wants the completed audit results available by 8 a.m. every Monday for the weekly engineering review. Given that batch processing has no latency SLA and can take up to 24 hours in the worst case, when is the latest the team can submit the batch and still safely expect results by the Monday deadline?
44. [D4] A developer opens a PR with the one-line description "add tests for the new pricing logic" and triggers Vanguard's test-generation step. The new pricing logic actually touches three distinct calculations (surcharge, discount stacking, and currency rounding), and the description doesn't specify which of the three — or whether all three — should be covered. Rather than blocking the pipeline to ask the developer for clarification, Vanguard proceeds by generating tests for all three calculations and includes a short note listing the assumption it made. Is this the right way to handle the ambiguous instruction, and why?
45. [D4] Solstice Freight is designing Vanguard's auto-approve behavior: findings above a certain bar should be auto-resolved with a suggested fix applied automatically, while others should route to a human reviewer. A vendor proposes having Vanguard self-rate its own confidence in each finding on a 1-to-10 scale and auto-apply any fix scoring 8 or above. Early testing shows several confidently-scored auto-applied fixes were actually wrong, while some fixes scored below the threshold turned out to be fine. What is the most effective way to design this routing decision instead?
46. [D2] Claimwise runs an auto-insurance claim-intake pipeline. Incoming packets are a mix of accident report forms, repair-shop estimates, and medical-visit summaries, and three separate extraction tools exist (one per document type). The pipeline must always hand the adjuster queue a schema-valid record for classification metadata before any downstream enrichment tool touches the document, but a prompt instruction telling Claude to 'always classify the document type first' is only followed on about 88% of runs. Which configuration most reliably guarantees the classification step runs before enrichment?
47. [D1] Claimwise's intake pipeline always follows the same five steps for every claim packet: document classification, field extraction, cross-field validation, coverage-limit enrichment, then adjuster-queue formatting — the template never changes regardless of claim type. An architect proposes replacing this with a dynamic decomposition step where the coordinator generates a custom subtask plan for each incoming packet based on what it discovers during initial parsing. Which structure is actually most appropriate here?
48. [D2] Claimwise's extraction agent frequently needs to check which coverage categories and per-incident limits apply to a policy while extracting a claim — information that rarely changes and would otherwise require the agent to guess at query terms for a `search_policy_rules` tool. An engineer wants the agent to see, up front, what coverage categories and limit structures exist without burning tool calls on exploratory guesses. Which MCP design best fits this need?
49. [D4] Claimwise's accident-report extraction schema marks `police_report_number` as required and non-nullable, on the reasoning that every accident should have an official filing. An audit of 3,000 extracted accident reports finds that 9% carry a police report number that traces to no real filing in the department's system — the model appears to be inventing plausible-looking numbers. Investigation confirms these claims were minor fender-benders where no police report was ever filed. What schema change most directly stops this?
50. [D5] Claimwise's intake coordinator delegates classification, extraction, and validation work across dozens of claim packets in a long-running overnight batch, tracked in-memory across many tool calls. Midway through processing claim #4,412, the orchestration host crashes and restarts. Currently, the coordinator has no way to know which claims were already fully processed, so the restart script simply reprocesses the entire overnight queue from claim #1. What is the most effective way to prevent this waste on the next crash?
51. [D2] Claimwise's adjuster-support agent, when reviewing a flagged claim, almost always needs both the policy's coverage terms and the claimant's prior claim history together — the two calls are made in sequence on nearly every review, adding a full extra API loop each time. An engineer considers building a single `get_policy_and_history` tool that fetches both in one call. What does the corpus favor instead?
52. [D1] When Claimwise's extraction pipeline cannot resolve a claim automatically — conflicting figures between the repair estimate and the medical summary, for instance — it calls `escalate_to_adjuster`. The human adjusters who receive these escalations report they must re-derive the claim's basic facts from scratch: the claimant, the policy number, which fields conflicted, and what the extraction agent already tried. The escalation console shows only that the tool fired with a one-line note, and adjusters have no access to the extraction agent's internal reasoning. What change most effectively fixes this?
53. [D4] Claimwise defines one extraction tool per document type (accident report, repair estimate, medical summary) so that every processed page always yields a schema-valid record for the adjuster queue. On a batch of scanned, low-quality faxes, Claude occasionally responds with an apologetic paragraph explaining the scan is hard to read instead of calling any of the three extraction tools — leaving that page with no structured output at all. Which configuration change most reliably eliminates this gap?
54. [D2] Claimwise's field-extraction subagent was originally scoped to five tools (extract per document type, plus a lookup helper) and selected correctly. Over several sprints, engineers kept adding convenience tools directly to this subagent — currency conversion, address standardization, a legacy OCR fallback, a duplicate-claim checker, and more — until it now has 16 tools. Selection accuracy has dropped noticeably, and the subagent now occasionally calls the wrong helper for a field it could have extracted directly. What is the most effective fix?
55. [D4] A regional carrier hands Claimwise a one-time backlog of 180,000 legacy claim packets to extract, with results due to feed a year-end reconciliation report at 8 a.m. two days from now — no adjuster is waiting on any individual document. The team plans to submit the whole backlog as a single Message Batches API run to capture the 50% discount. Given the batch has no latency SLA and can take up to 24 hours, how should the team plan the submission window to be safe?
56. [D5] Claimwise's extraction system reports 96% field-level accuracy in aggregate across all claim types, and leadership proposes ending human review for every extraction above the confidence threshold. A data scientist points out that windshield-only glass claims are a small slice of total volume and asks the team to check accuracy specifically within that segment before proceeding. The check reveals glass claims fail extraction 33% of the time, hidden inside the reassuring 96% aggregate. What should the team do before reducing human review?
57. [D1] Claimwise's extraction subagent occasionally receives a scanned repair estimate where the image is so severely truncated mid-page that the OCR layer throws a hard parsing exception. Today, the subagent simply returns the bare status `"failed"` to the coordinator, which then has no way to decide whether to request a rescan, skip the document and flag it, or route it to manual entry. What change would most effectively let the coordinator make an intelligent recovery decision?
58. [D2] Claimwise's `submit_settlement_offer` tool starts rejecting some settlement calculations because the proposed payout exceeds the claimant's policy per-incident coverage cap. The extraction agent currently treats every rejection the same way it treats a database timeout — it retries the exact same settlement calculation up to three times before finally escalating. How should the tool's error handling be restructured?
59. [D4] Claimwise's weekly reprocessing job for disputed claims uses the Message Batches API, and each request includes the claim-review tool definitions plus the full multi-turn conversation for that claim so far, because some disputes require the model to call a supplementary-document tool mid-review. A new engineer claims 'the Batches API doesn't support tool use at all, so this design is invalid and we need to move disputed-claim reprocessing to synchronous calls.' Is this assessment correct?
60. [D1] A single Claimwise policyholder submits one packet each night containing an accident report, a repair estimate, and a medical-visit summary — three genuinely independent documents that each need their own extraction before a coordinator cross-checks them against each other. The coordinator currently extracts them strictly one after another, and end-to-end turnaround for this nightly packet has become the client's top complaint even though every individual extraction succeeds. What is the most effective way to reduce turnaround here?

---

---

## Exam 4 — Generated 2026-07-09

**File:** `mock-exams/CCA-Prep_MockTest-4_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Customer Support Resolution Agent; Code Generation with Claude Code; Developer Productivity with Claude; Claude Code for Continuous Integration
**Attempt date:** 2026-07-11
**Score source:** results-JSON
**Total score:** 45 / 60 correct (estimated scaled: 775 / 1000; pass line 720)
**Total time:** 12:15:48 (irregular — see Observations; several multi-hour gaps between questions indicate breaks, not think time)

First exam generated under orchestration-prompt v9 (the six-fix fidelity system: generic scenario framing, pre-planned balanced correct-answer letters, binding word-count budget, domain-tally-vs-primary-domains check, inline code/config token-rate target, and the new Phase 4.e.6 Fidelity Verification Gate). Domain quota exact (D1 16 / D2 11 / D3 12 / D4 12 / D5 9). All six e.6 gate checks passed on the shipped file: 0 invented names; correct-answer letters 15/15/15/15 exam-wide (4/4/4/3 every block); stem word count min 35/median 51/max 62, option max 35; every block's domain tally passes primary-vs-non-primary; inline code/config token rate 22.5% (54/240); scenario-rotation disclosure present on the landing card. Verified end-to-end in a live browser render (landing card, question flow, rationale panel) before shipping, not just by static JSON inspection.

**Scenario draw deviated from pure rotation preference.** GENERATION-INTELLIGENCE.md's rotation guidance recommended the four scenarios still at count-1 (Customer Support, Code Generation, Multi-Agent Research, Developer Productivity), but that exact combination is mathematically infeasible under the new domain-tally-vs-primary-domains gate — none of the four carry D4 as a primary domain, and D4's fixed 12-question quota has no valid block to land in without a non-primary domain outnumbering a primary one somewhere. Verified via ILP solver across all 15 possible 4-of-6 draws: that combination is the *only* infeasible one. Claude Code for Continuous Integration (drawn twice already) was swapped in for Multi-Agent Research System to make the gate satisfiable; a fully solved, balanced block×domain allocation table was computed before any question was written (see Session Reflections below for the table).

**Two cross-block redundancies were found and fixed during assembly, not shipped:** (1) Q5 and an original draft Q29 both independently seeded Key Distinction #25 (stateless API / `session_id` misconception) as their primary answer with near-identical distractor logic — Q29 was rewritten around a fresh concept (Domain-5 §5.2, "lost in the middle") instead. (2) Key Distinction #12 (two-tool token-binding) and the "system-prompt dilution over many turns" pattern (KD#23) were each independently seeded as the primary answer in two and three blocks respectively — one instance of each was rewritten (Q10 → aggregate-accuracy-masking §5.9; Q57 → MCP resources-as-catalog §2.6; Q58 → batch-vs-synchronous API assignment §4.11), keeping the strongest original instance of each concept. `CCA-Orchestration-Prompt_v9.md` Phase 4.b.6 was updated to explicitly name KD-citation collision as a cross-block check the coordinating session owns, alongside the existing name-collision check (see GENERATION-INTELLIGENCE.md PB-12).

**A real corpus-integrity problem surfaced independently, not self-reported:** the Developer Productivity block's author found that `CCA-Prep_Key-Distinctions_v1.md` does not actually contain entries #26-29 (built-in-tool Key Distinctions), despite GENERATION-INTELLIGENCE.md's Open Findings Ledger row CG-01 claiming this was "FIXED... independently re-verified... confirmed on disk" on 2026-07-07. Independently re-verified again this session — the file genuinely ends at entry #25. CG-01's status has been corrected back to VERIFIED-STILL-OPEN; see GENERATION-INTELLIGENCE.md Pending Corpus Decisions. The three questions originally planned to cite KD#26-28 were instead grounded directly in `Domain-2_v2.md §2.9` (a real, verifiable corpus section), so no shipped question cites a non-existent Key Distinction.

### Questions Used (deduplication — do not reuse these stems in Exam 5+)

1. [D1] Your support agent's loop keeps calling Claude until its reply text contains the phrase 'issue resolved.' Logs show cases where Claude calls `process_refund` and returns a clear final answer, but the loop invokes Claude again anyway because the reply lacks that exact phrase, wasting a round-trip on 9% of resolved cases. What should the loop check instead?
2. [D2] Your `process_refund` tool accepts a `dry_run: boolean` parameter so the agent can preview a refund's impact before committing it. Production monitoring shows the agent sometimes calls `process_refund` with `dry_run=false` on the first attempt, skipping the preview step policy requires. Which redesign makes skipping the preview architecturally impossible?
3. [D1] Policy authorizes your agent to waive return-shipping fees for domestic returns when an item arrives damaged. A customer requests the same waiver for an international return; written policy is silent on international shipping fees entirely. `get_customer` and `lookup_order` both confirm the order and damage claim. What should the agent do?
4. [D2] A new compliance rule requires that the moment a customer explicitly asks for a manager, the agent's very next turn must call `escalate_to_human` — not offer reassurance first. Engineers want this guaranteed for that one turn only, then normal behavior resumes. Which `tool_choice` configuration guarantees it?
5. [D5] An engineer proposes fixing a bug where the agent forgets a customer's stated preference from two turns earlier by adding a session ID parameter so 'the API remembers the conversation.' A colleague pushes back. Investigation confirms the application's own request builder omits prior turns. What is the correct diagnosis?
6. [D3] Your team builds a `/audit-refund-errors` skill that runs a deep scan of weeks of refund logs, correlating `process_refund` calls with disputed charges. Engineers report that after invoking it mid-debugging-session, Claude becomes sluggish and loses track of the original bug they were investigating. How should the skill be configured to fix this?
7. [D1] A customer disputes charges on two orders in one message. `get_customer` succeeds and `lookup_order` returns full details for the first order, but times out on the second. The agent has enough to resolve one order now. What should it do with the incomplete second order?
8. [D2] Your `process_refund` tool's description reads only: 'Processes a refund for a given order.' Logs show the agent sometimes calls it for exchange requests — where the customer wants a replacement item, not money back — issuing refunds nobody asked for. What is the most effective fix?
9. [D4] When customers send vague openers like 'there's an issue with my order,' your agent currently asks up to four clarifying questions — which order, what kind of issue, email on file, preferred resolution — before doing anything. Abandonment on these openers is 37%. What should the agent do instead?
10. [D5] Your agent's resolution rate looks strong at 91% overall — cases closed without human handoff. A team member wants to broaden auto-resolution to more case types on the strength of that number. A skeptical colleague points out that billing-dispute cases are a small slice of total volume. What should the team check before broadening?
11. [D1] Policy requires that any case flagged for suspected fraud be escalated to a human before the agent marks it resolved. Today this rule lives only in the system prompt: 'always escalate fraud-flagged cases before closing.' An audit finds 6% of fraud-flagged cases closed without escalation. What change most reliably fixes this?
12. [D2] Refunds above $1,000 require manager sign-off before they execute, but today that rule lives only in a system-prompt instruction: 'route refunds over $1,000 to escalation before calling `process_refund`.' A monthly audit finds 4% of large refunds are still processed without sign-off, mostly during high-volume shifts. Which change enforces this rule deterministically?
13. [D4] The team wants the agent to stay calm under pressure, always cite the specific policy section behind a decision, and never guess at a policy point that isn't explicitly stated anywhere in the documented rules. Where should these behavioral constraints be defined so they hold for the entire conversation?
14. [D1] A customer asks the agent to refund all 42 orders on their account in one request, citing a billing error from several months ago they can't fully describe. Nothing in policy explicitly forbids a bulk refund of this kind, and `get_customer` confirms the account is legitimate. What should the agent do?
15. [D5] As holiday volume rises, multi-issue support conversations now often exceed 60 turns, mixing precise transactional details — order IDs, agreed refund amounts, promised delivery dates — with long stretches of routine back-and-forth. The team needs to manage growing token cost without losing that precision. Which context management strategy is most effective?
16. [D1] The order-fulfillment service is a 60-file legacy module the engineer has never touched. To speed up discovery, they configure a coordinator agent definition with detailed descriptions of three investigation subagents (routes, validators, retry logic) in its system prompt. In practice, Claude Code never spawns a single subagent — it investigates everything directly in the main session. What is the most likely fix?
17. [D1] With Task-spawned subagents investigating routes, validators, and retry logic in parallel, the retry-logic subagent hits a parsing exception on 2 of its 8 target files (malformed legacy syntax) and cannot read them; the other two subagents complete fully. What should the coordinator do when synthesizing the discovery report?
18. [D1] The routes-investigation subagent was scoped to Read, Grep, and Glob for its discovery task. After a teammate adds Bash to its allowed tools 'for convenience,' logs show it now runs ad hoc shell commands — including starting a local dev server — mid-investigation instead of just reading and searching files. What is the most effective fix?
19. [D2] The team's quick-fix suggestion feature, built with Claude Code, calls the Claude API directly with an `apply_fix` tool defined, expecting a tool call every time. On roughly 1 in 6 requests, the response is a prose paragraph explaining why no fix was proposed, and the automation has nothing to apply. What configuration change most reliably closes this gap?
20. [D3] The team decides to migrate the order-fulfillment service off its templating engine to a new one. The change touches views across roughly 50 files, and it's not yet settled whether migration should happen module-by-module or via a compatibility shim first. Which Claude Code approach should the engineer use to start this work?
21. [D3] Across the order-fulfillment codebase, the payments module enforces a custom validation-decorator pattern, the notifications module uses an event-emitter pattern, and a no-default-exports rule applies to utility files scattered across dozens of directories. The engineer wants each convention applied automatically based on which files Claude Code is touching. What should they configure?
22. [D3] Root CLAUDE.md imports `@./standards/coding-style.md` via `@import`, which imports another file, which imports another, continuing the chain six levels deep. Content from the sixth-level file silently doesn't appear in context. What is the most likely explanation?
23. [D3] A Claude Code session spent an afternoon mapping the order-fulfillment service's dependency graph. The next morning, five files in the inventory-sync module are rewritten before the engineer returns to the investigation. What is the most effective way to proceed?
24. [D4] Migrating the order-fulfillment service off its old logging library, a single prompt asking Claude Code to both enumerate every call site and rewrite each one in the same pass produces inconsistent results — several call sites are missed, and two are converted twice. What restructuring is most effective?
25. [D4] The engineer's CLAUDE.md instructs Claude Code to 'make sure new endpoints have good test coverage.' Generated tests for a newly scaffolded endpoint cover only the happy path — no validation errors, no empty-input case. What change most reliably improves test quality?
26. [D4] A request comes in simply as 'add export functionality to the reports module' — no format specified (CSV, PDF, or Excel are all plausible). Relayed as-is, Claude Code asks five clarifying questions before writing any code, stalling the task. What is the most effective way to handle this kind of vague request?
27. [D5] A hard-to-reproduce order-fulfillment bug investigation runs 40+ turns in one Claude Code session. Early on, the exact error code (`ERR_STALE_LOCK_409`) and the specific line where it originates were pinned down precisely. By turn 35, after summarization, Claude refers only to 'a locking-related error somewhere in the reservation path.' What fix most directly addresses this?
28. [D5] During a long refactor session, Claude Code follows the order-fulfillment service's CLAUDE.md formatting and error-handling conventions precisely for the first 15 turns, then begins drifting toward inconsistent formatting. The session is only 3,000 tokens — nowhere near any context limit. What is the most likely root cause?
29. [D5] Reviewing a 3,000-line consolidated diff spanning the templating and logging migrations, Claude Code's summary accurately covers the diff's opening import changes and its closing test updates, but never mentions a breaking API-signature change that sits in the diff's middle third. What is the most effective way to fix this pattern?
30. [D5] A single marathon Claude Code pair-programming session covering the templating migration, the logging migration, and plenty of general discussion reaches 82,000 tokens. It contains exact API-contract decisions, edge cases agreed on, and casual back-and-forth. The engineer wants to cut tokens while preserving what matters. What approach best balances this?
31. [D2] An engineer asks the agent to locate every file that still imports the deprecated helper `resolveShippingRate` before deleting it. The agent runs `Glob("**/resolveShippingRate*")` and reports two matches inside the helper's own module. A manual audit finds eleven more call sites elsewhere that the search missed. What is the most likely reason the search under-counted the callers?
32. [D2] While standardizing a logging call across the reservation module, the agent's first `Edit` attempt targets the anchor `return response`, but it matches nineteen locations and fails. The engineer suggests shortening the anchor to just `return` to make the match 'more specific.' Before trying that, what should the agent do instead?
33. [D2] A newly onboarded engineer asks the agent to trace how order-cancellation requests move through the monolith. On the first attempt, the agent reads all 60+ files under `order/` before producing any output, and its summary ends up conflating the cancellation flow with an unrelated returns-processing flow living in the same directory. What investigation strategy would have avoided this?
34. [D1] The platform team defines a dedicated investigation subagent, spawned via the coordinator's `Task` tool, to map unfamiliar corners of the monolith. They want a guarantee that this subagent can explore freely but can never modify a file while doing so, even if a prompt asks it to. Which configuration most reliably enforces this?
35. [D3] The team builds a `/trace-dependents` skill that catalogs every module depending on a legacy interface before a breaking change. After running it against a module's forty downstream modules, the engineer starts refactoring only that module itself — but the agent's next several suggestions keep proposing edits to downstream modules the trace merely catalogued. What fixes this?
36. [D1] The investigation subagent is asked to map every consumer of the monolith's `PricingEngine` module. Three of the eleven files it needs to read return a permission-denied error — they belong to a legacy team's locked-down directory — while the other eight read successfully. What should the subagent do with its findings?
37. [D3] The team plans to replace the monolith's decade-old job scheduler with a maintained open-source alternative — a change touching roughly 40 modules, with several viable target libraries and no agreement on which fits the monolith's retry semantics. An engineer is ready to implement against the first library that looks reasonable. Which execution approach should be used?
38. [D4] The agent now drafts boilerplate PRs for new monolith modules, but engineers report it sometimes writes a module's tests directly into the module file instead of a separate test file — almost always on modules that don't yet follow the repo's usual `module/tests/test_module.py` layout. Which prompting change most effectively fixes this specific pattern?
39. [D1] The coordinator asks three subagents to map how a fulfillment order moves from cart to shipment. Each finishes cleanly, but the combined map never covers inventory reservation or payment settlement, though all three report success. Coordinator logs show it decomposed the work into checkout UI, shipping label generation, and email notifications. What is the most likely root cause?
40. [D5] Late in a long mapping session, the agent's summaries start drifting — vague phrases like 'the relevant handler' instead of the file and line it cited accurately an hour earlier. Logs show the semantic-search MCP tool has returned full method bodies and relevance-score metadata for every hit all session. What is the most effective fix?
41. [D3] Two of the monolith's dozen modules handle payment adjustments and are subject to a compliance rule requiring an audit-log entry on every change — a rule that applies nowhere else. Pasting it into root `CLAUDE.md` means every session, even ones nowhere near payment code, loads it anyway. Which configuration applies the requirement automatically only where it's needed?
42. [D1] The coordinator's prompt for the boilerplate-PR subagent is procedural: create the module file, then create `tests/test_<name>.py`, then create `docs/<name>.md`. On the twelve modules that don't yet have a `tests/` folder at all, the subagent halts with a path-not-found error instead of creating one. Which change to the prompt would most effectively prevent this class of failure?
43. [D5] Partway through debugging a slow order-cancellation endpoint, the agent's investigation into why it calls `PricingEngine` three times expands into tracing all nineteen of `PricingEngine`'s callers across the monolith, filling most of the session's context before the engineer can start on the actual fix. What should the agent have done once the investigation began expanding this far?
44. [D4] The same agent session that drafts a boilerplate refactor for `inventory/reservation.py` is then asked, in that conversation, to 'review your own change before we merge it.' It reports the refactor is safe. A human reviewer looking at the diff days later spots a locking bug within minutes. What most directly explains why the same-session check missed it?
45. [D1] Once the investigation subagent maps the reservation module, its findings pass to a second subagent that drafts a refactor plan. The report is one free-text paragraph blending file names, line numbers, and reasoning together. The resulting plan cites structural issues but can't say which file or line each came from. What is the most effective fix?
46. [D3] The review job runs `claude -p` from the monorepo's `services/billing/` directory on every PR touching that service, so review context stays scoped locally, but engineers worry the subdirectory `CLAUDE.md` there will silently replace the root `CLAUDE.md`'s org-wide review criteria for those PRs. What actually happens to the two files' instructions?
47. [D2] The review job's finding layer exposes `flag_line_finding` (single line) and `flag_file_finding` (whole file, e.g. missing coverage) — both described only as "Flags an issue for review." Across roughly 40 PRs a week, logs show file-wide issues get filed via `flag_line_finding` attached to line 1 in 30% of cases. What should the team check first?
48. [D4] The team added 12 few-shot examples to the review prompt to fix inconsistent severity labels — all obviously-critical security bugs or obviously-trivial style nits. On a 200-finding audit sample, misclassification at the high/medium boundary (e.g., a null-dereference behind an already-checked guard) stays around 35%. Which change most reliably improves boundary accuracy?
49. [D1] The pipeline now routes large PRs through a coordinator that delegates security, performance, and style analysis to separate subagents. On a PR flagged for a possible injection risk, logs show the coordinator's own reasoning states it should hand off to the security subagent, but no subagent ever runs. What should the team check?
50. [D3] To cut startup overhead on a branch now receiving 6-8 PRs a day, an engineer proposes having the review job `--resume` the same named session across every PR opened against that fast-moving feature branch, instead of starting a new session per PR. What is the most effective way to evaluate this idea?
51. [D4] Since the review job adopted `--json-schema` output three weeks ago, zero findings have failed schema validation. A 500-finding sampling audit still finds 6% are labeled "critical" for issues that are demonstrably low-risk under the team's own rubric. How should the team interpret this?
52. [D2] The job's `post_finding` tool fails two different ways: on fork-originated PRs the CI token lacks comment-write permission (never succeeds no matter the retry count); on internal-branch PRs, failures are occasional network timeouts (succeed on retry). Both currently return an identical generic error, and the job retries every failure 3 times. How should the tool's error handling be restructured?
53. [D1] On a 22-file PR, the review job's analysis pass times out on 4 large generated files but completes normally on the other 18. The job currently posts its summary exactly as if the review were complete, with no mention that 4 files went unanalyzed. What should the output do differently?
54. [D4] On PR #4,821, a developer comments "/review focus on the risky parts," on a change touching both a payment-retry function and an unrelated formatting-only edit to a config file. "Risky" is undefined. Rather than pausing the pipeline to ask what counts as risky, how should the review job proceed?
55. [D3] On PR #2,203, the review job posts three findings on one function: a retry-lock race condition, a backoff calculation that assumes the current locking behavior, and an unrelated log-message typo. The developer will hand all three to Claude Code to fix. How should the findings be batched into prompts?
56. [D1] The test-generation subagent started with Read, Write, and the repo's test runner. Over several months, engineers added a deploy-script trigger and direct database-seed access "for convenience." It then ran the deploy trigger against shared staging while generating tests for an unrelated PR, disrupting another team. What is the most effective fix?
57. [D2] The review job's coordinator burns 5-8 tool calls each run issuing guessed `list_open_findings` queries just to discover which finding categories currently exist, before it can search productively. The finding-tracker MCP server could expose this information without an exploratory call. What is the most effective fix?
58. [D4] The pipeline runs three CI-triggered analyses: a pre-merge style check that blocks the PR until it completes, a nightly test-generation job for changed modules, and a weekly full-repo security audit. The team wants to cut cost by moving eligible work onto the Message Batches API's 50% discount. Which assignment is correct?
59. [D3] An engineer on the eight-person platform team built `/pr-checklist` at `~/.claude/commands/pr-checklist.md`, used by both her local sessions and a CI step. The team wants it available to the CI job and to every developer automatically on clone, with no per-machine setup. Where should the command file live to achieve this?
60. [D4] Weeks after a "critical" mislabeling incident on a payment-retry finding, the team wants findings to self-flag disagreements between the model's free-text severity judgment and a rubric-derived score computable from the same evidence, instead of catching mismatches only in periodic manual audits. Which schema design most directly achieves this?

### Exam 4 — Scored 2026-07-11

**Score source:** results-JSON (full per-question data — `selected`, `correct`, `seconds` for all 60 items)

#### Domain Breakdown
| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 12 | 75% | no |
| D2 Tool Design & MCP | 11 | 5 | 45% | no |
| D3 Claude Code Config | 12 | 9 | 75% | no |
| D4 Prompt Engineering | 12 | 10 | 83% | no |
| D5 Context Management | 9 | 9 | 100% | no |

#### Scenario Block Breakdown
| Block | Questions | Correct | % |
|---|---|---|---|
| Customer Support Resolution Agent | 15 | 12 | 80% |
| Code Generation with Claude Code | 15 | 12 | 80% |
| Developer Productivity with Claude | 15 | 11 | 73% |
| Claude Code for Continuous Integration | 15 | 10 | 67% |

#### Observations
- **Strongest domain:** D5 (Context Management), 9/9 — zero misses, no traps caught.
- **Weakest domain:** D2 (Tool Design & MCP), 5/11 (45%) — well below the academy's 70% domain floor. This is the clearest signal in the run: 6 independent misses spread across all 4 scenario blocks, touching 6 different specific facts (not one repeated misconception), which argues for a genuine breadth gap in D2 rather than one narrow trap.
- **Weakest scenario block:** Claude Code for Continuous Integration, 10/15 (67%), also below the scenario floor. Overlaps with the D2 weakness (2 of its 5 misses are D2) but also picked up 2 D4 misses and 1 D3 miss — likely some end-of-exam fatigue compounding the domain gap, given irregular timing data (see below).
- **Timing irregularity:** several questions show implausible elapsed times (Q7: 3827s / 64min, Q12: 3045s / 51min, Q55: 29835s / ~8.3 hours) consistent with breaks taken mid-exam rather than genuine think time. The passive per-question timer has no way to distinguish a pause from active reasoning. Total elapsed (12:15:48) is not comparable to the real exam's 120-minute window — treat the domain/scenario accuracy as the reliable signal from this attempt, not the pacing data.
- **Traps missed (by question, with the corpus fact each one tested):**
  - Q2 — two-tool token-binding pattern (`preview_X`/`execute_X` split) vs. a single-tool `dry_run:boolean` the model can skip. Domain-2_v2 §2.4; Key-Distinctions #11/#12.
  - Q8, Q47 — tool description must state scope/boundary to disambiguate near-duplicate tools (two independent misses, same corpus section, different scenarios). Domain-2_v2 §2.2; Key-Distinctions #10.
  - Q14 — high-stakes ambiguity is an escalation trigger even absent an explicit policy prohibition. Domain-1_v2 §1.12.
  - Q17 — partial subagent failure should produce coverage-annotated synthesis, not an error-out or a silent omission. Domain-1_v2 §1.10.
  - Q19 — `tool_choice:{"type":"any"}` forces a tool call; a prompt instruction alone does not. Domain-2_v2 §2.1/§2.5.
  - Q22 — `@import` max nesting depth is 5. Domain-3_v2 §3.1.
  - Q32 — `Edit` anchor uniqueness: a shorter anchor is MORE likely non-unique, not less; sanctioned fallback is Read+Write. Domain-2_v2 §2.9.
  - Q34 — `AgentDefinition.allowed_tools` is the structural least-privilege enforcement; a prompt instruction is not. Domain-1_v2 §1.3.
  - Q35 — `context: fork` isolates a skill's large/exploratory output from the main session. Domain-3_v2 §3.3; Key-Distinctions #13.
  - Q39 — when subagents all succeed but coverage is wrong, the root cause is the coordinator's task decomposition, not subagent execution. Domain-1_v2 §1.6.
  - Q46 — root and subdirectory `CLAUDE.md` concatenate; neither overrides the other. Domain-3_v2 §3.1.
  - Q51 — schema validation guarantees syntax only, never semantic/business-rule correctness. Domain-4_v2 §4.7.
  - Q52 — permission errors are non-retryable regardless of attempt count; timeouts are transient/retryable — conflating the two wastes retries. Domain-2_v2 §2.3.
  - Q54 — for ambiguous automated requests, proceed with a stated assumption rather than blocking to ask or silently guessing. Domain-4_v2 §4.19; Key-Distinctions #19.

### Questions Used
Already logged under the Exam 4 generation entry above — no new stems from scoring.

---

### Professor's Note — Intent for Exam 5

**2–3 misconceptions the wrong answers revealed:**
1. **D2 tool-design breadth gap** (Key-Distinctions #10, #11/#12; Domain-2_v2 §2.2, §2.3, §2.4, §2.9) — 6 misses across 6 distinct facts (description boundary clarity, ×2; token-binding; tool_choice forcing; Edit-anchor uniqueness; retryable-vs-permanent errors). Not one repeated trap — a genuine coverage gap across the domain's tool-design mechanics, not a single misconception to re-teach once.
2. **CLAUDE.md hierarchy mechanics** (Domain-3_v2 §3.1) — two independent misses in one sitting (import nesting depth; multi-level concatenation/no-override). Both are mechanical facts of the same feature, missed together.
3. **"Sounds like the fix, isn't" pattern recurring across domains** — Q34 (prompt instruction chosen over `allowed_tools` whitelist), Q19 (prompt instruction chosen over `tool_choice:any`), Q52 (uniform backoff chosen over categorized retryable/non-retryable) all share the same shape: a probabilistic prompt-level fix chosen over the structural/configuration-level guarantee the corpus favors.

**Weakest domain:** D2 (Tool Design & MCP), 45% — **suspected, first scored data point.** This is Exam 4's first-ever attempt with real per-domain data (Exams 1–3 remain unattempted), so per this file's own insight-generation rule (3-exam trend layer), this is not yet a confirmed cross-exam trend — but a single 45% score against a 70% floor, spread across 6 distinct facts, is strong same-sitting evidence worth acting on before waiting for two more data points.

**One sentence of deliberate next-paper intent:** Exam 5 should weight its D2 question selection toward the specific §2.2/§2.3/§2.4/§2.9 facts missed here (respecting the fixed D2=11 quota — bias WHICH sections fill it, not the count) so the next attempt directly re-tests whether the gap closes.

**One thing to watch:** whether the D2 miss pattern is genuine domain weakness or an artifact of encountering several "sounds like the fix, isn't" traps back-to-back late in a long, break-interrupted sitting (block 4, Continuous Integration, carried the CI scenario floor breach) — Exam 5 drawing a different scenario mix for D2's primary domain would help separate content weakness from fatigue/scenario-position effects.

---

*Next exam: Exam 5. Next deduplication check: all 30 Exam-1 stems + all 60 Exam-2 stems + all 60 Exam-3 stems + all 60 Exam-4 stems above + all 76 practice-test stems are off-limits.*

---

## Exam 5 — Generated 2026-07-11

**File:** `mock-exams/CCA-Prep_MockTest-5_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Multi-Agent Research System; Structured Data Extraction; Code Generation with Claude Code; Developer Productivity with Claude
**Attempt date:** 2026-07-11
**Score source:** results-JSON (full per-question data — see "Exam 5 — Scored 2026-07-11" below)
**Total score:** 52 / 60 correct (estimated scaled: 880 / 1000; pass line 720)
**Total time:** 32:29 (1,949s; ~32.5s/question — clean, no break-interrupted outliers)

> *Status lines corrected 2026-08-11. This entry read "Not yet attempted / Pending / Pending" until then, even though the exam was scored the same day it was generated — the scored section below, and Insights Round 1, both record it. The generation entry was simply never updated the way Exam 4's was. Totals derived from the domain breakdown below (15+8+11+9+9 = 52); scaled score per the standard `round((correct/60) × 900 + 100)`.*

Four scenario blocks delegated to parallel sub-agents against a centrally pre-planned block×domain allocation table and a pre-planned correct-answer-letter sequence per block (Phase 4.d.5), per Orchestration Prompt v9's sanctioned delegation pattern. Domain quota exact (D1 16/D2 11/D3 12/D4 12/D5 9); no confirmed-weakness adjustment applied — only one scored exam exists (Exam 4), so the two-consecutive-exam confirmed-weakness gate is not yet eligible. Scenario draw: Multi-Agent Research System (least-used, count 1) paired with Structured Data Extraction (the other D4-primary carrier, satisfying the standing D4-carrier rule from GENERATION-INTELLIGENCE.md) plus Code Generation and Developer Productivity (both count 2), resting Customer Support and Claude Code CI (count 3, most-used) — leaves all 6 scenarios within a count-of-1 spread afterward. This draw gave KD#6 (coordinator-vs-direct subagent communication) its first seeding ever, and gave D2 — this learner's confirmed-weak domain from Exam 4 at 45% — a different scenario framing (Multi-Agent Research + Developer Productivity, not Customer Support) per Exam 4's Professor's Note.

All six Phase 4.e.6 Fidelity Verification Gate checks passed on the shipped file, computed programmatically (not hand-counted): 0 invented names; correct-answer letters exact 15/15/15/15 exam-wide (every block's actual sequence verified position-by-position against its d.5 pre-plan — all four followed their plan exactly, zero reshuffling needed); stem word count min 43/median 53/max 66, all options ≤35 words; every block's domain tally passes primary-vs-non-primary with real margins (min primary count exceeds max non-primary count in all four blocks); inline code/config token rate 28.7% (69/240 options, within the 25–30% acceptable band); scenario-rotation disclosure line present on the landing card. Verified end-to-end in a live browser render (landing card, a correct-pick question, a wrong-pick question, jump-map block grouping and answered-state tracking) — not just static JSON inspection.

**Three genuine cross-block collisions were found and fixed by the coordinating session, none visible to any individual block's own self-check:** (1) SDE-Q2 and MAR-Q4 both independently landed on D2 §2.2 (a heavy-capped section, max 1/exam) — SDE-Q2 rewritten around `tool_choice:any` vs. a forced single tool (§2.1); a first rewrite attempt itself collided with MAR-Q7's §2.3 and had to be redone a second time. (2) CG-Q5 and MAR-Q9 both independently landed on D2 §2.6 — CG-Q5 rewritten around the "application must actually execute the `tool_use` and return a `tool_result`" step (§2.1). (3) CG-Q12 and SDE-Q13 both independently seeded the same D4 §4.19 "state an explicit assumption" concept as their primary answer — CG-Q12 rewritten around category-level trust restoration (§4.17). A fourth, self-inflicted defect was also caught before shipping: the CG-Q12 rewrite was first transcribed into the wrong array position (g44 instead of g42), which silently dropped the original Q14 (system-prompt dilution, KD#23) from the exam and broke the block's domain-vs-primary check (D5 tied D4 at 2 apiece instead of beating it) — caught by an automated post-write verification script, not visual inspection, and fixed by restoring Q14 to g44 and moving the trust-restoration content to its intended g42 slot.

**The exam-wide Key-Distinction-seeding count also came in over cap:** 21 against the binding 15-question limit (Phase 4.b.5) once all four blocks returned. Six questions' formal "Key Distinction #N" cross-references (MAR-Q9, SDE-Q13, CG-Q2, DP-Q2, DP-Q3, DP-Q5) were trimmed back to their corpus-section citation alone — the citation, correctness, and rationale text were otherwise unchanged, only a redundant secondary reference was removed — bringing the count to exactly 15. The first editing pass only actually applied the trim to one of the six (MAR-Q9); the other five silently failed to apply and were caught only by a second automated grep-based count, not by re-reading the diff — a second pass then closed all six out at exactly 15, re-verified programmatically.

### Questions Used (deduplication — do not reuse these stems in Exam 6+)

1. [D1] A document-analysis subagent starts sending findings straight to the synthesis subagent over a shared queue, skipping the coordinator, to save a round-trip. Within a week, synthesis output silently omits findings the coordinator never sees, and a subagent failure goes unnoticed until the report is missing a whole subtopic. What is the most effective fix?
2. [D2] An engineer wires a custom `verify_citation` tool into the synthesis subagent's request. When the subagent issues two tool calls in the same turn, the application's tool-execution code appends both results to the conversation, but Claude occasionally treats the second result as belonging to the first call. What is the most likely cause?
3. [D1] The team wants a research system that always follows the same steps for standard competitive-landscape briefs: search, extract company profiles, validate figures, then format. Separately, they're prototyping open-ended requests like "assess this emerging technology's societal impact," where nobody knows the relevant subtopics until initial findings come in. Which decomposition strategy fits each case?
4. [D2] The web-search subagent's `search_web` tool is described only as "searches the web for a query and returns results." When a researcher pastes a specific article URL into a request, the subagent calls `search_web` with the URL as the query instead of handing it to the document-analysis subagent's fetch tool. What is the most effective fix?
5. [D1] The web-search subagent's external search API returns a quota-exceeded response mid-task. Today the subagent simply reports `{"status": "failed"}` to the coordinator, which cannot tell whether to wait and retry, switch source categories, or continue with partial findings. What change would most effectively let the coordinator make an intelligent recovery decision?
6. [D5] Before delegating research subtasks, the coordinator must survey an internal document repository of several thousand files to see what topics and date ranges exist. Doing this directly in the coordinator's own session returns hundreds of summaries and nearly fills its context before delegation starts. What is the most effective way to run this survey?
7. [D2] The document-analysis subagent's `query_source_archive` tool sometimes returns `{"results": [], "isError": true}` and sometimes `{"results": [], "isError": false}` for what production logs show are actually two different situations: a genuinely empty archive section, and an archive index that is temporarily unreachable. How should the tool signal these two outcomes?
8. [D1] Policy requires every source be checked for license restrictions before use in synthesis, since paywalled data can't be quoted verbatim. Today this rule lives only in the synthesis subagent's system prompt. An audit finds 8% of drafts quote paywalled sources unchecked. What change most reliably guarantees the check happens every time?
9. [D2] The research team wires a shared MCP server for a paid market-data API into everyone's Claude Code setup, but each researcher holds a separate personal subscription key. Leadership wants one configuration file everyone pulls from version control, with no working key ever committed to the repo. Which configuration approach is most effective?
10. [D1] For a request needing both fresh news and analysis of an uploaded filing, the coordinator issues one `Task` call to web-search, waits for its full response, then issues a separate `Task` call to document-analysis next turn — though neither depends on the other. What most effectively reduces latency here?
11. [D3] Months ago, a researcher created a personal `/cite-check` skill at `~/.claude/skills/` to tweak citation formatting to their taste. The team has since updated the shared project skill to a new house style, and every teammate's output reflects it — except this researcher's, even though their repo checkout is current. What is the most likely cause and fix?
12. [D2] When a request needs both current news and an uploaded filing summarized, the coordinator's `Task` calls to web-search and document-analysis now run in parallel, but inside the web-search subagent, `search_web` and `fetch_snippet_details` still run in separate turns even when both are clearly needed. What most effectively reduces this?
13. [D4] The synthesis subagent's one prompt asks it to both identify which claims need a citation and write the full narrative in the same pass. Reviewers find citation coverage inconsistent — some well-supported claims go uncited while marginal ones get cited. An engineer wants more thorough citation identification without changing which claims make the report. What is the most effective restructuring?
14. [D1] While configuring the three research subagents, an engineer proposes giving each one the full tool catalog — web search, document fetch, citation verification, and formatting — reasoning that any subagent could then substitute for another during a bottleneck. What is the most effective response to this proposal?
15. [D5] The research team's system also maintains an archive of every completed research project going back months, totaling well over 100K tokens. A researcher asks the coordinator to recall a specific caveat one project's synthesis flagged about a data source's methodology three months ago. What is the most effective way to support this kind of recall?
16. [D4] The extraction pipeline's review-flagging step is instructed to 'flag any document with an unclear or possibly incorrect field appropriately for manual review.' Audit of 200 documents shows a missing `tax_id` field is flagged in some documents but not others with the identical gap, and reviewers say the flagging feels arbitrary. What change most reliably makes flagging consistent?
17. [D2] Your extraction pipeline has three tools — one each for invoices, receipts, and PO confirmations — and an upstream classifier tags each file's type. To guarantee a structured call every time, an engineer hard-codes `tool_choice: {"type": "tool", "name": "extract_invoice"}` on every request, ignoring the classifier's tag. Receipts and PO confirmations now come back with invoice-only fields full of nulls and guesses. What should the team change?
18. [D4] One legacy onboarding path still requests JSON via prompt instructions only, without `tool_use`. Responses often open with "Certainly! Here is the extracted data:" before the JSON body, and the downstream parser — which expects the response to start with `{` — throws on roughly 8% of calls. Migrating this path to `tool_use` is scheduled for next quarter. What should the team do in the meantime?
19. [D5] A single prompt call extracts obligations from a 45-page merger agreement concatenated into one document. Party names and the closing signature block extract reliably every time, but financial covenants embedded in pages 20–25 are frequently missed or returned with generic placeholder values. What is the most effective way to restructure the extraction input?
20. [D4] The extraction pipeline handles three workloads: a single-document lookup a support rep waits on live during a call, a nightly re-run of the previous day's failed extractions, and a one-time 300,000-document historical backlog with no one waiting on results. Which assignment of each workload to an API approach is correct?
21. [D1] The extraction pipeline's classification, extraction, and validation subagents each report success on every document, yet the coordinator's logs show it routes only `invoice` and `receipt` categories to those subagents, even though roughly 20% of the incoming stream is purchase-order confirmations that silently fall through unclassified. What is the most likely root cause?
22. [D4] Since moving to `tool_use` with a strict JSON schema, extraction responses always parse and every field passes type validation. But reconciliation still flags 4% of invoices where `total_due` holds the pre-tax subtotal instead of the tax-inclusive total the schema description asked for. How should the team respond?
23. [D5] A vendor sends periodic amendments to the same service contract. The extraction pipeline pulls a price clause from the original contract and, months later, a different price from an amendment covering the same clause. Downstream reconciliation flags this as a data conflict requiring manual reconciliation. What extraction design change most directly prevents this false conflict?
24. [D4] A classification step routes each intake document to one of three extraction tools by type. Clear invoices and clear receipts route correctly nearly every time; documents that are simultaneously a receipt and a tax-deductible donation acknowledgment are misrouted about 40% of the time. An engineer plans to add few-shot examples to fix this. Which set of examples is most effective?
25. [D4] A due-diligence run cross-checks a bundle of 12 related loan documents for consistency in a single prompt call. QA finds thorough, accurate flags on the first two or three documents, but shallow coverage after that — and an identical missing-signature pattern is flagged in document 3 while the same pattern is missed in document 9. What is the most effective restructuring?
26. [D5] An extraction system routes low-confidence fields to human review and auto-processes everything else. Six months after launch, no auto-processed extraction has been re-examined. A new invoice layout was introduced by a major vendor three months ago. What should the team implement to catch a hidden failure mode in that auto-processed stream?
27. [D4] The validate-then-retry loop resubmits failed extractions with only the message "Extraction failed, please retry" — no specifics. On documents with wrong-format dates and misplaced currency symbols, all three retries still fail, though the source clearly contains the correct data. What is the most effective fix?
28. [D4] An intake document arrives as a one-page scan with ambiguous formatting — it plausibly matches either the receipt schema or the invoice schema, and nothing in the document definitively resolves which. The pipeline currently pauses and queues the document for a human to specify the type before continuing. Backlog on these ambiguous scans is now three days deep. What should the pipeline do instead?
29. [D5] A reconciliation specialist works an extended interactive session correcting a batch of vendor credit notes, one after another, in a single long-running conversation. Early on, an agreed $12,450 credit adjustment is confirmed. Forty exchanges later, the session's summary of that adjustment reads only "a credit adjustment was discussed," and the final reconciliation entry uses the wrong amount. What is the most effective fix?
30. [D4] A long interactive extraction session processes a stream of scanned invoices one at a time in the same conversation. The system prompt states that a missing purchase-order number must be returned as `null`, never invented. Through the first 14 documents this holds; by document 15, with the session still only 4,000 tokens, the model starts fabricating plausible-looking PO numbers. What is the most likely root cause?
31. [D3] An engineer wants Claude Code to always run an extra local formatting pass before finishing, a habit the rest of the eight-person team doesn't want imposed on their sessions. They want it active only in their own use, with no change to what teammates see after cloning the same repo. Where should this instruction go?
32. [D3] Your team wants a stricter commit-message format enforced automatically whenever Claude Code touches files inside the `release/` branch-prep directory, but nowhere else — most sessions never open that directory and shouldn't load the extra convention. Which configuration achieves this without adding the rule to every session's context?
33. [D1] A coordinator spawns subagents via Task to migrate a codebase off a deprecated logging library. Its prompt reads: 'Step 1: find files importing old-logger. Step 2: replace with new-logger. Step 3: run tests.' Migration stalls whenever a file uses old-logger in a way the fixed steps didn't anticipate. What change to the prompt fixes this?
34. [D3] Your team's `/scaffold-endpoint` skill writes new API endpoint files and explains its naming choices so the developer can keep refining them in the same conversation. An engineer proposes adding `context: fork` to the skill's frontmatter "to keep the main session clean." What is the effect of doing this, and is it appropriate here?
35. [D2] Your team's `generate-component` CI script calls the Claude API directly with a `write_component_file` tool so Claude can scaffold new React components. A new engineer's version sends the request and marks the run complete as soon as the response contains a `tool_use` block, but no file ever appears on disk. What is missing from the script?
36. [D3] An engineer wrote `/scaffold-endpoint` as a plain file at `.claude/commands/scaffold-endpoint.md`, predating the team's skills. It reads the endpoint name typed after the command. A teammate insists this legacy file no longer works and must become a `.claude/skills/` folder first. Is the teammate correct, and what holds the typed text?
37. [D5] During a multi-day session migrating a payment SDK, the team agreed to pin the library to v4.2.1 (not v4.3.0, a known regression) and keep a 750ms retry-timeout override. Forty exchanges and several summarization rounds later, Claude proposes pinning v4.3.0 and drops the override. What is the most effective fix?
38. [D3] Adding multi-currency checkout support touches pricing, cart, and receipt modules, and the team hasn't settled whether amounts should be integer minor units or decimals, or how per-currency rounding should work. An engineer is ready to have Claude Code start implementing immediately and adjust once problems surface. What should they do instead?
39. [D3] A developer unfamiliar with tax rules asks Claude Code to implement a discount-stacking calculator. The first attempt applies discounts in the wrong order; the second fixes that but ignores a tax-exempt category; the third fixes that but mishandles a coupon-plus-loyalty combination. Each fix only addresses the most recently discovered gap. What should the developer do on the next attempt?
40. [D5] Asked to bump a feature-flag timeout, Claude Code finds the flag defined in three config files — `dev.yaml`, `staging.yaml`, and `prod.yaml` — with different existing values, and the request doesn't say which environment(s) to change. Rather than guessing, what should Claude Code do?
41. [D3] An engineer wraps Claude Code in a nightly script that regenerates typed client bindings: `claude "Regenerate the TypeScript client from openapi.yaml"`. Cron logs show the process starts, prints the prompt, and produces no further output until it's killed two hours later. What is the correct way to invoke Claude Code so the script completes on its own?
42. [D4] Your team wired an automated review step into the Claude Code CI pipeline to flag issues in every merged PR. Three months of data show null-dereference findings dismissed only 5% of the time and resource-leak findings 11%, but import-ordering findings are dismissed 44% and variable-shadowing findings 49% — and developers now skim past every finding, including the reliable ones. What should the team do first?
43. [D3] A nightly automation invokes Claude Code to propose refactor suggestions for stale utility modules, then feeds the output into a script that opens one ticket per suggestion with `module_path`, `suggested_change`, and `estimated_effort` as separate fields. The script currently regex-parses Claude's prose output and breaks whenever the wording shifts. Which invocation most reliably gives the script parseable fields?
44. [D5] A long Claude Code session refactoring authentication middleware follows a stated instruction — 'never remove backward-compatible parameter names, only deprecate them' — for the first eight exchanges. By the eleventh exchange, at just under 3,400 tokens total, it silently drops a legacy parameter in a suggested diff. What is the most likely explanation?
45. [D3] Your team runs three workloads: (1) generating docstrings interactively while a developer pairs with Claude Code, (2) a nightly job drafting a changelog from the day's merged PRs, and (3) a one-time bulk pass documenting 50,000 legacy functions with no deadline pressure. Which assignment to the Message Batches API is correct?
46. [D1] Your repository automation must always run `format_code` before `commit_changes` fires, so every commit is consistently formatted. Today this rule lives only in the system prompt: 'always format before committing.' A monthly audit finds 5% of automated commits skip formatting, mostly during high-volume batch runs. Which change most reliably closes this gap?
47. [D1] Your boilerplate-generation harness always invokes Claude Code exactly three times per request, then stops. On simple scaffolds, the third call is wasted after Claude already finished with a clean final answer; on complex scaffolds needing four tool calls, the harness cuts off before Claude finishes. What should the harness check instead?
48. [D1] An engineer asks Claude Code to scaffold 12 new module files from a boilerplate template, then review all 12 in one pass for consistency. The single pass gives detailed feedback on the first few files, misses a naming-convention violation repeated in three others, and never checks whether the generated files agree with each other. How should the review be restructured?
49. [D1] A coordinator investigating an unfamiliar payment-authorization module is given only a goal: 'produce a complete map of how authorization requests flow end to end, noting any external dependencies discovered along the way.' No steps are scripted. Which named pattern does this coordinator prompt exemplify, and why does it outperform a scripted investigation checklist here?
50. [D1] An investigation subagent scanning legacy modules for a deprecated API pattern hits two kinds of failure: some files are on a network-mounted share that occasionally times out, others are binary artifacts that can never be parsed as text. Today both failures return a bare 'failed' status, and the coordinator retries the binary-artifact failures three times before giving up. What should the subagent report instead?
51. [D1] A coordinator investigating three independent legacy modules — authentication, billing, and notifications — for a deprecation audit spawns one investigation subagent via `Task` per module, but issues each `Task` call in its own separate coordinator turn, one after another. Investigation latency triples versus running them together. What is the most effective fix?
52. [D1] An automation renaming a deprecated config key across the codebase discovers the key is also referenced inside a third-party vendor plugin directory that sits outside version control, with no record of whether anything in production still depends on it. Nothing in the runbook addresses vendor-owned code. What should the automation do?
53. [D1] Two investigation subagents mapping a legacy service each hit a permission-denied error on a locked directory. One subagent silently skips the files and continues; the other halts entirely and returns nothing. Both report to the same coordinator. Which architectural principle, if followed, prevents this kind of inconsistent handling?
54. [D2] Your `cleanup_stale_branches` automation exposes a `dry_run: boolean` flag so engineers can preview which branches would be deleted before anything actually runs. Logs show the automation sometimes invokes it with `dry_run=false` on the very first call, skipping the preview step policy requires. Which redesign makes skipping the preview architecturally impossible?
55. [D2] A documentation-generation subagent frequently needs to check the linter's current rule configuration while writing code examples, adding a full round-trip through the coordinator to the linting subagent nearly every time. Complex linting-policy questions are rare. What is the most effective tool configuration for the documentation subagent?
56. [D2] An automation uses Bash-driven search-and-replace across the codebase for repetitive cleanup tasks. Engineers want a guarantee that any single Edit or Write operation touching more than 50 files triggers mandatory human confirmation first — not just a reminder the agent might follow. What should they configure?
57. [D2] Before migrating snapshot tests to a new format, an engineer asks Claude Code to enumerate every snapshot test file across a mixed monorepo. The agent greps file contents for the word 'snapshot' and misses dozens of snapshot files that never contain that literal word, while also matching unrelated files that mention it in a comment. What tool should it use instead?
58. [D3] Your project's CLAUDE.md now mixes two things: coding conventions every session should follow, and a lengthy checklist for scaffolding new boilerplate modules that only matters when creating one. Engineers scaffolding a new module say the checklist is essential then; engineers doing ordinary bug fixes say it's dead weight cluttering every session. How should this content be split?
59. [D3] An engineer is centralizing scattered session-token-reading logic spread across 45 files into one shared helper. Locating every call site first produces a long list with surrounding context that fills most of the session's window before the design conversation about the helper's interface can even start. What is the most effective way to complete this discovery phase?
60. [D4] An engineer asks Claude Code to generate a boilerplate adapter that maps a legacy record format to a normalized schema through several conditional field transformations and unit conversions — a genuinely multi-step reasoning task. Which prompting addition most reliably improves accuracy here, and is it worth adding to a separate one-line boilerplate rename task too?

---

### Exam 5 — Scored 2026-07-11

**Score source:** results-JSON (full per-question data — `selected`, `correct`, `seconds` for all 60 items)

#### Domain Breakdown
| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 15 | 93.8% | no |
| D2 Tool Design & MCP | 11 | 8 | 72.7% | no |
| D3 Claude Code Config | 12 | 11 | 91.7% | no |
| D4 Prompt Engineering | 12 | 9 | 75.0% | no |
| D5 Context Management | 9 | 9 | 100% | no |

#### Scenario Block Breakdown
| Block | Questions | Correct | % |
|---|---|---|---|
| Multi-Agent Research System | 15 | 14 | 93.3% |
| Structured Data Extraction | 15 | 14 | 93.3% |
| Code Generation with Claude Code | 15 | 12 | 80.0% |
| Developer Productivity with Claude | 15 | 12 | 80.0% |

#### Observations
- **Strongest domain:** D5 (Context Management), 9/9 — zero misses, the second exam running at 100% for this domain.
- **Strongest overall:** D1 (Agentic Architecture), 15/16 (93.8%) — near-perfect on the exam's heaviest-weighted domain.
- **Weakest domain:** D2 (Tool Design & MCP), 8/11 (72.7%) — **CONFIRMED weakness** (same domain unambiguously weakest in both Exam 4, 45%, and Exam 5, 72.7%, both non-estimated, no tie either time). This is the project's first-ever confirmed cross-exam weakness. The underlying signal is genuinely positive, though: D2 improved 27 points from Exam 4 to Exam 5 — it's confirmed-weak only because every other domain is now even stronger (D4 is the next-lowest at 75%), not because D2 regressed.
- **Weakest scenario blocks:** Code Generation with Claude Code and Developer Productivity with Claude, tied at 80% (12/15 each). Code Generation's three misses (Q35 D2, Q36 D3, Q42 D4) spread across three domains; Developer Productivity's two misses (Q54 D2, Q57 D2) are both D2 — concentrating exactly on this exam's weakest domain within a single block.
- **Timing:** fast and even — 32:29 total (1949s), ~32.5s/question average, well under the ~2 min/question real-exam budget. No break-interrupted outlier gaps this time (unlike Exam 4's irregular 12+ hour total) — treat this attempt's pacing data as reliable, not just its accuracy.
- **Traps missed (by question, with the corpus fact each one tested):**
  - Q13 — chose a clearer prompt instruction over splitting citation-identification and drafting into a sequential chain. Domain-4_v2 §4.14.
  - Q21 — misattributed a coverage gap to a tool-description problem instead of the coordinator's own narrow task decomposition (all subagents succeeded; the decomposition never assigned the missing category). Domain-1_v2 §1.6.
  - Q35 — missed that the calling application, not Claude, must execute the `tool_use` block and write the file; picked a `PostToolUse` hook instead of the actually-missing execution step. Domain-2_v2 §2.1.
  - Q36 — fell for a fabricated-obsolescence distractor: believed legacy `.claude/commands/` files "stopped working" once skills were introduced. Domain-3_v2 §3.4.
  - Q42 — chose the slow, eventual few-shot fix over surgically disabling the two noisy finding categories immediately — correct general direction, wrong urgency for a trust-bleed already in progress. Domain-4_v2 §4.17.
  - Q54 — chose a still-bypassable confirmation-string parameter over the architecturally-guaranteed two-tool token-binding redesign — the same "sounds like the fix, isn't" pattern (probabilistic/parameter-level fix chosen over a structural guarantee) flagged in Exam 4's Professor's Note, recurring across two consecutive exams. Domain-2_v2 §2.4; Key-Distinctions #12.
  - Q57 — chose Grep (content search) over Glob (path-pattern match) for file-name enumeration, on this corpus's first-ever citable use of a built-in-tool Key Distinction. Domain-2_v2 §2.9; Key-Distinctions #26.
  - Q60 — swapped a few-shot format-consistency fix for a step-by-step reasoning-depth cue — two techniques aimed at two different failure modes. Domain-4_v2 §4.2.

### Questions Used
Already logged under the Exam 5 generation entry above — no new stems from scoring.

---

### Professor's Note — Intent for Exam 6

**2–3 misconceptions the wrong answers revealed:**
1. **The "sounds like the fix, isn't" pattern persists in D2** (Q54, Key-Distinctions #12) — a bypassable, parameter-level fix chosen over an architecturally-guaranteed redesign. This is the same misconception class Exam 4's Professor's Note named (Q34/Q19/Q52's prompt-level-fix-over-structural-guarantee pattern), now recurring across two consecutive scored exams — worth explicit, repeated emphasis rather than assuming one pass through the corpus fixed it.
2. **Built-in-tool selection (Domain-2_v2 §2.9, Key-Distinctions #26) missed on its first-ever citable appearance** (Q57) — chose Grep over Glob for file-name-pattern enumeration. This is freshly-seeded content (the corpus gap CG-01 was only resolved this cycle), so the miss is a genuine first-exposure data point, not evidence of a settled strength or weakness yet.
3. **A "trust the more dramatic-sounding wrong explanation" pattern in D1/D3**, not a domain-level weakness (D1 is 93.8%, D3 is 91.7%) — Q21 blamed a tool description instead of the coordinator's own decomposition, and Q36 believed a real, still-supported mechanism was fabricated-obsolete. Worth a light touch next paper, not a section reweight.

**Weakest this paper:** D2 (Tool Design & MCP), 72.7% — **confirmed** across two consecutive scored exams (45% in Exam 4, 72.7% in Exam 5). Triggers the standard confirmed-weakness adjustment for Exam 6 generation: +4 D2, −2 D1, −2 D5 (D2-collision rule), giving a base distribution of D1 14 / D2 15 / D3 12 / D4 12 / D5 7.

**One sentence of deliberate next-paper intent:** Within D2's larger 15-question quota, Exam 6 should weight toward §2.4 (two-tool token-binding, Key-Distinctions #12 — now missed twice, across Exam 4 and Exam 5) and §2.9 (built-in tools, Key-Distinctions #26 — missed on its first appearance), while still giving fair coverage to D2 sections this learner hasn't been tested on yet.

**One thing to watch:** whether the D2 gap keeps closing (45% → 72.7% → ?) now that it gets a bigger, more targeted slice of Exam 6, or plateaus around 70–75% — a plateau would suggest the remaining gap is the specific "sounds like the fix, isn't" conceptual pattern rather than general D2 unfamiliarity, and would argue for a dedicated reinforcement pass on that one pattern rather than more raw D2 question volume.

*Next exam: Exam 6. Next deduplication check: all 30 Exam-1 stems + all 60 Exam-2 stems + all 60 Exam-3 stems + all 60 Exam-4 stems + all 60 Exam-5 stems above + all 76 practice-test stems are off-limits.*

## Exam 6 — Generated 2026-07-11

**File:** `mock-exams/CCA-Prep_MockTest-6_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Customer Support Resolution Agent; Multi-Agent Research System; Structured Data Extraction; Developer Productivity with Claude
**Attempt date:** 2026-07-12
**Score source:** results-JSON (full per-question data — see "Exam 6 — Scored 2026-07-12" below)
**Total score:** 49 / 60 correct (estimated scaled: 835 / 1000; pass line 720)
**Total time:** 4:20:25 (15,625s; irregular — Q18, Q10 and Q32 account for ~70% of elapsed time and read as breaks, not think time; 82.7s/question excluding them)

> *Status lines corrected 2026-08-11 — same defect as Exam 5's entry: scored on 2026-07-12 per the scored section below and Insights Round 1, but the generation entry was never updated. No separate attempt date is recorded anywhere, so the scored date is used. Totals derived from the domain breakdown below (13+11+10+10+5 = 49); scaled score per the standard `round((correct/60) × 900 + 100)`.*

First exam generated under the confirmed-weakness quota adjustment: D2 (Tool Design & MCP) was confirmed weak across two consecutive scored exams (45% Exam 4, 72.7% Exam 5), triggering the standard FULL-60 rule (+4 the confirmed domain, −2 D1, −2 D5 per the D2-collision pattern) to give D1 14 / D2 15 / D3 12 / D4 12 / D5 7 (base 16/11/12/12/9). Scenario draw followed GENERATION-INTELLIGENCE.md's own stated preference: Customer Support Resolution Agent and Multi-Agent Research System were tied as least-used (count 2 each); pairing them with Structured Data Extraction (satisfying the standing D4-carrier rule) and Developer Productivity with Claude lets this exam close out Key Distinctions #27–29 immediately via the built-in-tool-selection theme, rather than deferring them another cycle. Rests Code Generation with Claude Code and Claude Code for Continuous Integration (both at count 3) for a round.

Four scenario blocks delegated to parallel sub-agents against a centrally pre-planned block×domain allocation table and a pre-planned correct-answer-letter sequence per block (Phase 4.d.5). Block×domain allocation (primary domains bold): Customer Support — **D1 7, D2 5**, D3 1, D4 0, **D5 2**; Multi-Agent Research — **D1 5, D2 6**, D3 1, D4 1, **D5 2**; Structured Data Extraction — D1 0, D2 1, D3 1, **D4 10, D5 3**; Developer Productivity — **D1 2, D2 3, D3 9**, D4 1, D5 0. All four blocks pass the primary-vs-non-primary domain-tally check (Phase 4.e.6 check 4), verified programmatically.

**One real cross-block collision was found and fixed during assembly, not shipped:** the Multi-Agent Research block's D3 question was assigned §3.4 ("project vs personal skill precedence") by the coordinating session, but that concept actually lives at Domain-3_v2 §3.5 — a coordinating-session section-numbering error, not a sub-agent error. The Multi-Agent Research sub-agent, reasonably trying to honor its assignment's *intent*, substituted §3.5 on its own initiative — which collided directly with the Developer Productivity block's own, correctly-assigned §3.5 question (both landed on the same "personal skill override to trial a change" narrative). Fixed by rewriting the Multi-Agent Research question around the real §3.4 content (Custom Slash Commands — a `/cite-check` command needing automatic team-wide availability on clone/pull), restoring full 12-of-12 D3 section coverage with zero repeats exam-wide.

**A second, necessary (not accidental) section-reuse pattern was resolved deliberately:** D2's quota (15 questions, post-adjustment) exceeds its own corpus breadth (9 sections, §2.1–§2.9, all already "heavy" from 3+ prior-exam uses). The standing "max 1 heavy section per exam" cap cannot literally hold when a domain's confirmed-weakness-adjusted quota exceeds its section count — this is the first exam where D2's quota (15) has exceeded D2's section count (9). Resolved this cycle by allowing up to 2 uses per D2 section (spread evenly: §2.2, §2.4, §2.5, §2.6 each used twice), except §2.9 (built-in tools) at 3 uses, since it alone carries Key Distinctions #27, #28, and #29 — the three that had never been seeded in any prior exam. Logged as new process finding PB-17 (see GENERATION-INTELLIGENCE.md Open Findings Ledger) rather than silently absorbed.

All six Phase 4.e.6 Fidelity Verification Gate checks passed on the shipped file, computed programmatically via a Node script (not hand-tally): 0 invented names; correct-answer letters exact 15/15/15/15 exam-wide (each block's actual sequence verified position-by-position against its d.5 pre-plan — all four followed their plan exactly, zero reshuffling needed); stem word count min 40/median 55/max 82 (options all ≤29 words, both well inside their hard caps — eight of the longest stems were tightened during assembly specifically to bring the exam-wide median from 56.5 down to exactly 55, the top edge of the 50–55 target band); every block's domain tally passes primary-vs-non-primary with real margins; inline code/config token rate 24.6% (59/240), within the 20–25% target band; scenario-rotation disclosure line present on the landing card. Verified end-to-end in a live browser render (landing card, a correct-pick question, a wrong-pick question, jump-map block grouping, full results/export flow, and localStorage resume-on-reload), not just static JSON inspection.

**Key Distinction budget:** 7 of 60 questions carry an explicit "Key Distinction #N" citation (well under the 15 cap) — KD#25 (Q5), KD#12 seeded intentionally twice per the Professor's Note (Q12, Q22 — two different facets: fix-selection vs. defending-the-pattern-against-an-alternative), KD#17 (Q38), KD#23 (Q42), and KD#27/#28/#29 (Q47/Q46/Q48 respectively, the three previously-unseeded Key Distinctions, now closed out). KD coverage stands at 29 of 29 after this exam — every Key Distinction in the corpus has now been seeded at least once.

### Questions Used (deduplication — do not reuse these stems in Exam 7+)

1. [D1] Your support bot's agentic loop stops the moment any reply includes a `process_refund` or `escalate_to_human` tool_use block, treating those tool names as always final. Logs show cases where Claude calls `get_customer` first, expecting a follow-up `lookup_order` call, but the loop already returned a raw tool result instead of continuing. What should the loop check instead?
2. [D2] A harness defines `get_customer`, `lookup_order`, `process_refund`, and `escalate_to_human` as tools. When a response arrives with `stop_reason: "tool_use"` naming `escalate_to_human`, the harness marks the case escalated in its own database and ends the request, without calling the handler or sending anything back to Claude. If the session continues, it repeats the same escalation attempt. What step is missing?
3. [D2] Your `process_refund` tool's description reads only: 'Issues a refund for a given order.' It expects an order_id formatted as ORD-12345. Production logs show 9% of calls fail validation because the agent instead passes the raw digits a customer types in chat, like '12345', or the subject line of the customer's order-confirmation email. What is the most effective fix?
4. [D2] `process_refund` accepts a list of order IDs to refund several at once. Policy requires any single call refunding more than 5 orders to be routed to a human for sign-off before it executes. Today the rule lives only in the system prompt. A monthly audit finds 3% of bulk refund calls above that threshold execute anyway, mostly during high-volume shifts. Which change enforces this deterministically?
5. [D5] The support widget now lets a customer refresh the page mid-conversation while your backend keeps the same conversation ID in its own database. After a refresh, the agent has no memory of anything said before, even though the conversation ID hasn't changed. An engineer proposes fixing this with a persist_context: true field on the Claude API request so the API retains prior turns server-side.
6. [D1] As your support bot scales, it splits into a coordinator plus billing-disputes and returns subagents, both able to call process_refund. The returns subagent is wired to notify the billing subagent directly once it approves a refund, bypassing the coordinator. A damaged-item return and a separate double-billing dispute on the same order each independently approve a refund, and the order is refunded twice before anyone notices. What is the most effective fix?
7. [D1] The returns subagent's AgentDefinition is configured with all four tools — get_customer, lookup_order, process_refund, and escalate_to_human — though its scope is only to evaluate return eligibility and issue refunds. Over several weeks it starts unilaterally escalating billing disputes that belong to the billing subagent's scope, since nothing in its configuration stops it. What is the most effective fix?
8. [D1] The billing subagent's coordinator prompt reads like a fixed script: call get_customer, then lookup_order, then if the discrepancy exceeds $50 call process_refund, then done. On disputes spanning three related orders with a mix of overcharges and a missing discount, the subagent follows the steps correctly but produces a shallow, incomplete resolution. Which change to the coordinator prompt is most effective?
9. [D1] The billing subagent resolves disputes by checking exactly two things: the charge amount and the discount code applied. Every check completes and reports correctly, yet disputes caused by a duplicate transaction charge keep coming back unresolved, since neither check was ever designed to look for a duplicate charge. What is the most likely root cause?
10. [D1] The team is scoping how the coordinator should investigate multi-year loyalty-point disputes, where the relevant orders, transfers, and promotions only become clear once the first lookup runs. An engineer proposes a fixed pipeline: always run get_customer, then lookup_order for every order on the account, then check point-expiration rules, in that exact order, for every case. Which decomposition strategy is actually more appropriate, and why?
11. [D1] The coordinator now merges the billing subagent's overcharge findings and the returns subagent's already-processed-refund findings into one free-text paragraph before building an escalation handoff summary. A human agent receiving an escalation on a case touching both subagents finds the refund amount attributed to the wrong order number, since the merge lost track of which subagent's output supplied which figure. What is the most effective fix?
12. [D2] The team adds a close_account tool with a dry_run: boolean parameter so an engineer can preview which subscriptions and open orders would be affected before permanently closing an account. Production logs show the agent sometimes calls close_account with dry_run=false on the very first attempt, closing an account with no preview ever generated. Which redesign makes skipping the preview architecturally impossible?
13. [D2] The returns subagent frequently needs a customer's current loyalty-tier discount percentage while evaluating a return — a simple, high-frequency lookup. Today every check routes through the coordinator to a separate loyalty-program subagent, adding a full extra loop. Complex disputes, like a contested retroactive tier change, are rare but still need that subagent's deeper investigation. What is the most effective tool configuration?
14. [D3] The root CLAUDE.md pastes the full billing-dispute and returns conventions inline, so every subagent's session loads both regardless of which it's running. The billing subagent's maintainers want their config to load only the billing conventions file, without deleting the returns content from version control or maintaining two copies by hand. Which approach best achieves this?
15. [D5] A 55-turn conversation about a delayed shipment includes the customer's updated delivery address and a gate code needed for access, buried among long stretches of routine back-and-forth about tracking updates and carrier delays. The team needs to cut token cost as these threads grow without losing the address and gate-code precision. Which context management strategy is most effective?
16. [D1] To reduce round-trips through the coordinator, the report-generation subagent was given full `web_search` access so it could 'double-check a stat while formatting the final report.' Production logs show it now independently re-researches topics the web-search and synthesis subagents already covered, tripling report latency without improving accuracy. What is the most effective fix?
17. [D2] The web-search subagent's `extract_snippets` tool and the document-analysis subagent's `extract_excerpts` tool are both described only as 'extracts relevant text from a source.' Synthesis requests route to `extract_snippets` for downloaded PDFs 38% of the time, when `extract_excerpts` was needed. How should this misrouting be fixed?
18. [D2] The team connects three separate MCP servers to the web-search subagent: a news-archive server, a patent-database server, and a regulatory-filing-index server. An engineer worries the subagent will only see tools from whichever server it 'attaches to' last, and plans to write orchestration code to merge each server's tool list manually before every request. What should the engineer expect instead?
19. [D1] The document-analysis subagent processes scanned regulatory filings; roughly 40% fail: some are permanently unreadable low-resolution scans, others failed only because the file-storage endpoint briefly timed out. Every failure returns the same generic `{"status": "failed"}`, so the coordinator retries all identically, wasting cycles on scans that will never parse. What should the subagent report instead?
20. [D1] The web-search subagent returns full results for 4 of 6 requested source categories; the other two — patent filings and conference proceedings — time out entirely. The document-analysis subagent has processed everything it was given without issue. What should the synthesis subagent do with this mixed-completeness input?
21. [D2] The report-generation subagent's `submit_report_draft` tool starts rejecting drafts that exceed the client's contracted page-limit policy. The tool currently returns the same generic `{"error": "Operation failed"}` for this as for a genuine service outage, and logs show the subagent retries the rejected submission up to three times before escalating. How should the tool's error handling be restructured?
22. [D2] The research system's `archive_source_cache` operation permanently deletes a completed project's raw document cache. An architect proposes an orchestration-layer confirmation dialog that pops up before the call reaches Claude, requiring a human click before execution. A teammate argues the two-tool preview/execute token pattern (`preview_archive_source_cache` returning a token, `execute_archive_source_cache` requiring it) is still preferable. Why?
23. [D2] The web-search subagent has accreted 14 tools over eight months of piecemeal additions — separate tools for each source type, format converters, and a legacy fallback nobody removed. It now calls the wrong retrieval tool 22% of the time, while a peer synthesis subagent with 5 role-scoped tools selects correctly almost every time. What is the most effective fix?
24. [D2] The report-generation subagent calls `format_report` and then `attach_citations` in two separate sequential turns, even though every report needs both together. This adds a full extra API loop to every research task the system completes. What is the most effective way to reduce this overhead?
25. [D1] The coordinator has already re-delegated targeted queries and re-invoked synthesis twice because the draft kept omitting implementation-timeline details the document-analysis subagent had actually logged earlier. A third synthesis pass still lacks the timelines. Should the coordinator re-delegate a fourth time?
26. [D1] A client's research brief is silent on whether a report about current grid-storage incentives should include regulations that were superseded last year — omitting them could miss important historical context, but including them could make the report read as describing rules that no longer apply. Nothing in the brief or house style guide resolves this. What should the coordinator do?
27. [D3] The coordinator's citation-formatting checks have grown into a `/cite-check` command that every research subagent's output should pass before a report ships. One team member built it locally and now wants it invoked identically by all six teammates the moment they pull the latest repo changes, with zero manual setup on each machine. Where should the command file live?
28. [D5] The document-analysis subagent finds two credible sources disagreeing on a grid-storage rollout timeline: a government energy agency projects full deployment by 2030, while an industry consortium report projects 2035. Both sources pass the subagent's credibility checks. What should it do?
29. [D4] The coordinator's citation schema marks `publication_year` as required and non-nullable for every source, reasoning that every citation needs a year for the report's timeline section. An audit of 5,000 citations finds 9% carry a plausible-looking year that traces to no actual publication date — many are working papers and preprints that never listed one. What schema change most directly stops this?
30. [D5] Across 14 months and dozens of completed research projects for a recurring client, a researcher wants to know whether the team has ever covered a specific niche subtopic — floating offshore wind subsidy structures — without manually rereading every past report. What is the most effective way to support this kind of recall?
31. [D4] The extraction pipeline must, on every document, render dates as ISO-8601, return null instead of fabricating any missing field, and never wrap the JSON payload in explanatory prose. An engineer needs these three rules to hold for every document processed in a session, not just the first one. Where should the rules be defined?
32. [D4] The pipeline must call `extract_metadata` before any of its three type-specific extraction tools run, since downstream steps depend on knowing a document's source and page count first. A prompt instruction saying 'always call `extract_metadata` first' is followed only about 85% of the time. Which `tool_choice` configuration reliably guarantees the metadata step runs first?
33. [D2] The pipeline's enrichment step needs to validate vendor tax IDs against a national business registry. A well-maintained community MCP server already wraps this exact registry, but a colleague proposes building a custom, in-house MCP server from scratch instead, arguing it gives the team full control. What is the most effective approach?
34. [D4] The extraction team hand-writes the JSON schema used in the tool definition, while a different engineer separately maintains a validation module checking rules like `sum(line_items) == total`. Twice this quarter, a field was added to one but not the other, and validation failures slipped through undetected until traced. What change most directly prevents this drift?
35. [D4] A new extraction field requires computing an invoice's effective tax rate: summing several line-item tax codes, applying jurisdiction exemptions, and cross-checking the result against the stated total. The current prompt states only the target field name, with no other guidance. Which prompting addition most reliably improves accuracy here?
36. [D4] During an interactive review session, a specialist corrects a misread vendor name on document 14. That correction must be available to the model when it processes document 15 moments later, without restructuring the system prompt or restarting the session. What is the most effective way to make the correction available?
37. [D3] The extraction team is building internal tooling: a nightly `claude -p` job reviewing the day's failed extractions that must hand a ticketing script exactly four fields per failure — `document_id`, `failure_category`, `suggested_fix`, `retry_count`. Which CLI configuration most reliably produces output the ticketing script can parse every night?
38. [D4] To catch cross-document inconsistencies, the pipeline validates a bundle of 8 related vendor statements for account reconciliation in one prompt call. QA finds detailed, accurate flags on the first two or three statements, but a duplicate-line-item pattern is caught in statement 2 and missed in statement 6 of the same bundle. How should this review be restructured?
39. [D4] For documents flagged low-confidence, the workflow re-asks the same model instance, in the same conversation, to 'double-check this extraction carefully' before routing to a human. An audit later finds several of these self-confirmed extractions were still wrong on the exact fields the model claimed to have re-checked. What most directly addresses this?
40. [D4] Onboarding a new vendor's document template, a schema-suggestion step proposes 9 new field-mapping rules. Developers find 6 of them duplicate mappings already defined in the existing vendor-mapping config, because the prompt generating suggestions doesn't include that config. What change most effectively reduces duplicate mapping suggestions?
41. [D4] The pipeline escalates straightforward duplicate-invoice matches to human review while attempting genuinely ambiguous multi-currency reconciliations autonomously. Auto-resolution sits at 58% against an 80% target, and no written criteria distinguish which cases should route where. What is the most effective way to improve this calibration?
42. [D4] The system prompt requires ISO-8601 dates and two-decimal currency on every extraction. During an interactive correction session reprocessing flagged documents one by one, this holds for about 20 documents; by document 22 the model reverts to source-document date formats and single-decimal currency, though the session is only 2,800 tokens. What is the most likely root cause?
43. [D5] The pipeline extracts clauses from a 300-page agreement, page by page, across many sequential tool calls in one long session. By page 200, the model gives inconsistent answers about clauses found on early pages, referencing 'typical contract language' instead of the specific text extracted earlier. What sustains accuracy across a task this long?
44. [D5] The interactive correction session for flagged documents keeps only the last 15 exchanges verbatim, dropping everything earlier. An early correction about how to round multi-currency line items falls outside that window by exchange 30, and the model reintroduces the original rounding error on a later document. What is the most effective restructuring?
45. [D5] In the enrichment step, three lookup tools return dates in three different formats — Unix epoch, DD/MM/YYYY, and MM-DD-YYYY — and the model occasionally misreads a country-ambiguous date when composing the final record. What is the most maintainable way to fix this?
46. [D2] The reporting pipeline spans 85 files across three modules. To trace why a duplicate-suppression flag sometimes fails to propagate, the engineer Globs all three modules, then has the agent Read all 85 files before writing a single line of analysis. By the time it reaches the delivery module — the only place the flag is actually consumed — most of the context budget is already spent on files that never reference the flag. What investigation strategy should the engineer have used instead?
47. [D2] Standardizing error handling, the engineer has Claude Code call Edit on `transform-utils.js` with the anchor `wrapError(err)`. Edit fails: that exact snippet appears in 15 places in the file, so Edit cannot determine which occurrence to change. A teammate suggests shortening the anchor to just `wrapError(` to make the match more specific. What should happen instead?
48. [D2] The team wires in an MCP server that returns typed caller/callee call-graph relationships, distinct from plain text matching. Its description reads only "Finds references in the codebase." When tracing how a config key propagates across module boundaries, the agent still reaches for built-in Grep roughly 70% of the time, even on queries the call-graph server answers more precisely. What is the most effective fix?
49. [D3] The engineer wants the ingestion module's Python files to follow a type-hints convention, the transformation module's Go files to follow a specific error-wrapping pattern, and the delivery module's TypeScript files to follow a strict-lint convention — plus a shared testing convention for test files, which sit scattered next to the code they cover across all three modules. Which configuration applies the right convention automatically regardless of which module is being worked on?
50. [D3] The engineer builds a `/purge-orphan-configs` skill meant only to identify orphaned config files for review. Its SKILL.md frontmatter sets no tool restrictions, and during a run the skill unexpectedly deletes two files it was only supposed to flag. What frontmatter change most directly prevents this kind of destructive action?
51. [D3] A developer wants to customize the shared `/format-report` skill — adding a personal pre-commit formatting pass — without changing what the rest of the eight-person team sees when they run the same command after cloning the repo. What should they do?
52. [D3] The engineer is asked to restructure the ingestion module to support streaming ingestion instead of batch files — a change touching all 32 ingestion files and requiring decisions about how partial records should be buffered and replayed. Multiple valid designs exist. Which execution approach should the engineer use?
53. [D3] A currency-conversion bug in the transformation module mishandles null exchange-rate values on certain lookups. The engineer describes the bug in prose to Claude Code three times, each time getting a fix that handles only the specific null case just described, leaving other null-rate scenarios unfixed. What is the most effective next step?
54. [D3] A nightly CI job invokes Claude Code to generate tests for changed files in the delivery module. Generated tests consistently invent their own fixtures and ad-hoc mocks instead of using the team's existing fixture helpers and shared HTTP-client mock already used throughout the suite. The job's prompt is just the changed diff and a short instruction. What most reliably makes generated tests follow the team's conventions?
55. [D3] Three candidate workloads: a pre-deploy compatibility check blocking the release pipeline until it completes, a nightly job regenerating yesterday's failed reports, and a one-time backfill of 500,000 legacy reports with no one waiting. Which assignment of API approach is correct?
56. [D3] The pipeline's root CLAUDE.md has grown to 350+ lines: universal formatting and error-handling conventions, plus a lengthy delivery-outage escalation checklist used only a handful of times a year. Every session loads the full file, and engineers say the checklist adds irrelevant bulk to routine work. Which restructuring keeps the universal conventions always available while loading the rare checklist only when needed?
57. [D3] After Claude Code completes a full analysis of the delivery module's retry behavior, the team wants to evaluate two competing designs for safer retries: exponential backoff with a shared circuit breaker, versus a per-request idempotency key. Both should start from the same completed analysis, without re-running the expensive analysis twice or letting either evaluation bias the other. What is the most effective way to proceed?
58. [D1] A dependency-upgrade automation hits a version conflict it cannot resolve — two teams pin incompatible major versions of the same library — and escalates with only a generic 'needs manual review' flag. The on-call engineer has no access to the automation's session and must re-discover which packages were touched, what versions were tried, and where the conflict lives. What change most effectively fixes this?
59. [D1] The release automation must confirm a prior deploy's lock file has cleared before starting a new deploy, since deploying while the lock is held corrupts the release. Today this rule exists only as a prompt comment. During a high-traffic release window, the automation deployed while the previous lock was still present, corrupting that release. What change most reliably prevents a recurrence?
60. [D4] The dependency-upgrade automation's summary reports `stated_packages_updated: 47` after each run, self-counted as it works. Engineers now suspect this self-reported figure sometimes diverges from the actual number of package-manifest diffs produced, but nobody notices until a much later audit. What extraction design change most directly catches this at the time of the run?

---

### Exam 6 — Scored 2026-07-12

**Score source:** results-JSON (full per-question data — `selected`, `correct`, `seconds` for all 60 items)

#### Domain Breakdown
| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 14 | 13 | 92.9% | no |
| D2 Tool Design & MCP | 15 | 11 | 73.3% | no |
| D3 Claude Code Config | 12 | 10 | 83.3% | no |
| D4 Prompt Engineering | 12 | 10 | 83.3% | no |
| D5 Context Management | 7 | 5 | 71.4% | no |

#### Scenario Block Breakdown
| Block | Questions | Correct | % |
|---|---|---|---|
| Customer Support Resolution Agent | 15 | 11 | 73.3% |
| Multi-Agent Research System | 15 | 13 | 86.7% |
| Structured Data Extraction | 15 | 12 | 80.0% |
| Developer Productivity with Claude | 15 | 13 | 86.7% |

#### Observations
- **Strongest domain:** D1 (Agentic Architecture), 13/14 (92.9%) — one miss (Q25, D1 §1.8, refinement-loop stopping criterion).
- **Weakest domain:** D5 (Context Management), 5/7 (71.4%) — a sharp reversal, not yet confirmed. D5 had scored a perfect 9/9 in both Exam 4 and Exam 5; this is its first miss in three exams, and two misses out of only seven questions is a real drop. Single-exam signal only — cannot be confirmed as a trend until Exam 7.
- **D2 update:** 11/15 (73.3%), essentially flat from Exam 5's 72.7% despite the larger 15-question allocation. D2 is no longer this paper's weakest domain (D5 edges it out at 71.4% vs. 73.3%) — the standing two-exam confirmed weakness on D2 is broken this cycle. The 4 D2 misses (Q2 §2.1, Q3 §2.2, Q12 §2.4/KD#12, Q24 §2.8) are spread across 4 different sections, not concentrated — consistent with Exam 4's original "genuine breadth gap" diagnosis persisting at a much lower but still-present level.
- **Standout repeated trap:** Key Distinction #12 (two-tool token-binding vs. a bypassable `dry_run`/confirmation-parameter, D2 §2.4) was missed for the third exam running (Exam 4 Q2, Exam 5 Q54, Exam 6 Q12) — the single most persistent misconception in this learner's history. Every instance shares the identical shape: picking a probabilistic, still-bypassable parameter-level fix over the architecturally-guaranteed two-tool split.
- **Timing:** irregular — 15,625s total (260.4s/question average), but three extreme outliers (Q18: 5,114s / ~85min; Q10: 3,861s / ~64min; Q32: 1,936s / ~32min) account for ~70% of total elapsed time and are consistent with breaks, not think time. Excluding those three, the remaining 57 questions average 82.7s/question — still above Exam 5's clean 32.5s/question pace but nowhere near as extreme as the raw total suggests. Treat accuracy as the reliable signal from this attempt; timing is break-confounded, the same caveat Exam 4's irregular pacing carried.
- **Traps missed (by question, with the corpus fact each one tested):**
  - Q2 — `tool_result` must reference the originating `tool_use`'s `id`; the harness skipped actually executing the tool and returning a matched result. Domain-2_v2 §2.1.
  - Q3 — tool description must specify the exact accepted input format with an example, not just name the tool's purpose. Domain-2_v2 §2.2.
  - Q5 — stateless-API misconception: chose a fabricated `persist_context`/`session_id`-style parameter over "the application must resend the full prior messages array." Domain-5_v2 §5.1; Key Distinction #25 (first-ever miss of this KD).
  - Q12 — two-tool token-binding vs. a bypassable confirmation parameter for a destructive `close_account` call — the third consecutive exam this exact concept has been missed. Domain-2_v2 §2.4; Key Distinction #12.
  - Q24 — the corpus favors a prompt instruction to bundle two habitually-paired tool calls into one turn over a composite tool that hides the two steps. Domain-2_v2 §2.8.
  - Q25 — the coordinator's refinement loop needs a defined sufficiency criterion, not an open-ended "keep re-delegating" or an arbitrary re-delegation cap. Domain-1_v2 §1.8.
  - Q35 — a step-by-step reasoning cue is the fix for multi-step numeric extraction (tax-rate calculation), not more few-shot examples or a lower temperature. Domain-4_v2 §4.2.
  - Q42 — accumulated assistant responses dilute system-prompt influence over a long session; not a context-window overflow or a per-document overwrite. Domain-4_v2 §4.20; Key Distinction #23 (first-ever miss of this KD).
  - Q44 — the hybrid context window (recent verbatim + running summary + a never-dropped structured facts block) fixes a sliding-window's loss of an early, still-relevant correction — a bigger fixed window only delays the same problem. Domain-5_v2 §5.13.
  - Q50 — `allowed-tools` in skill frontmatter restricts tool access during execution (official exam framing); `context: fork` isolates output, it does not restrict tool access. Domain-3_v2 §3.3.
  - Q51 — a personal skill of the same name overrides a project skill only for that individual, without editing the shared version-controlled file. Domain-3_v2 §3.5.

### Questions Used
Already logged under the Exam 6 generation entry above — no new stems from scoring.

---

### Professor's Note — Intent for Exam 7

**2–3 misconceptions the wrong answers revealed:**
1. Key Distinction #12 (two-tool token-binding, D2 §2.4) missed for the third exam running (Exam 4 Q2, Exam 5 Q54, Exam 6 Q12) — the single most persistent trap in this learner's history. Every instance shares the identical shape: a bypassable, parameter-level "fix" (a boolean flag, a confirmation string) chosen over the architecturally-guaranteed two-tool preview/execute split. Three consecutive misses of the identical concept is a stronger signal than any confirmed-weakness domain check can capture on its own.
2. D5 (Context Management), a sharp single-exam reversal — after two consecutive perfect 9/9 scores (Exam 4, Exam 5), D5 dropped to 5/7 this exam, missing a first-ever Key Distinction #25 instance (stateless API / fabricated `persist_context` parameter, D5 §5.1) and a hybrid-context-window design question (D5 §5.13). Not confirmable as a trend yet — could be a genuine emerging gap or an artifact of this attempt's break-interrupted pacing (D5's misses, Q5 and Q44, were both answered quickly at 31s and 27s respectively, not among the slow/break-affected questions, which argues mildly against pure fatigue as the explanation).
3. D2's breadth gap persists at a much lower level. D2 held roughly flat (72.7% → 73.3%) despite a larger 15-question allocation deliberately spread across all 9 corpus sections; its 4 misses this exam (§2.1, §2.2, §2.4, §2.8) are spread across 4 different sections rather than concentrated on one trap — echoing Exam 4's original "genuine breadth gap, not one narrow misconception" diagnosis, just at a far less severe scale than Exam 4's 45%.

**Weakest this paper:** D5 (Context Management), 71.4% — suspected, single-exam signal, NOT yet confirmed. D2's prior two-exam confirmed weakness is broken this cycle (D2 is no longer the weakest domain, though it remains second-weakest and still elevated relative to D1/D3/D4). No domain currently meets the two-consecutive-exam confirmed-weakness bar.

**One sentence of deliberate next-paper intent:** With no domain confirmed weak, Exam 7 reverts to the base FULL-60 distribution (D1 16 / D2 11 / D3 12 / D4 12 / D5 9, no confirmed-weakness adjustment) — but within that base quota, bias section selection toward D5 §5.1 and §5.13 (this exam's two D5 misses) to test whether the drop was real or a fluke, and toward D2 §2.4 specifically (Key Distinction #12) for a fourth attempt at the corpus's single most persistent trap.

**One thing to watch:** whether D5 returns to its prior near-perfect form (suggesting Exam 6's dip was attempt-specific, not a real gap) or scores weak again (confirming a genuine D5 weakness for the first time in this project) — and separately, whether Key Distinction #12 is finally answered correctly on its fourth appearance, since three consecutive misses of one specific concept is now the single strongest individual signal in this learner's full exam history.

---

## Insights Round 1 — 2026-07-12
*(Triggered automatically: exams_scored reached 3, a non-zero multiple of 3, after this session's Exam 6 scoring — the first Insights Round in this project's history.)*

**Exams covered:** Exam 4 (2026-07-11), Exam 5 (2026-07-11), Exam 6 (2026-07-12) — all three scored via results-JSON, fully non-estimated.

### Domain Trend
| Domain | Exam 4 | Exam 5 | Exam 6 | Trend |
|---|---|---|---|---|
| D1 Agentic Architecture | 75.0% | 93.8% | 92.9% | Strong and stable at a high level; slight dip from Exam 5's peak, still excellent. |
| D2 Tool Design & MCP | 45.0% | 72.7% | 73.3% | Sustained improvement, now plateauing around 73% — the sharpest single-domain trend in the project so far. |
| D3 Claude Code Config | 75.0% | 91.7% | 83.3% | Dipped this exam after peaking in Exam 5; no clear directional trend across all three, comfortably above the 70% floor throughout. |
| D4 Prompt Engineering | 83.3% | 75.0% | 83.3% | Oscillating, no clear trend — stable in the high-70s/low-80s range across all three exams. |
| D5 Context Management | 100% | 100% | 71.4% | Sharp reversal this exam, breaking a two-exam streak of perfection — the standout trend-break of this round. |

### Pace Trend
| Exam | Total time | Avg s/question | Note |
|---|---|---|---|
| Exam 4 | 44,148s | 735.8s | Irregular — flagged as break-interrupted at the time (12+ hour total elapsed). |
| Exam 5 | 1,949s | 32.5s | Clean — no interruption flagged; the only reliable pacing baseline of the three. |
| Exam 6 | 15,625s | 260.4s (82.7s excl. 3 outliers) | Irregular — three extreme outliers (Q18, Q10, Q32) account for ~70% of total elapsed time. |

Two of the three exams in this round show break-confounded timing; only Exam 5 is a clean pacing data point. No domain shows a reliable, non-outlier-driven pattern of exceeding the ~2min/question exam budget once break-affected questions are set aside — pace trend is inconclusive over this round and should not be treated as a reliable signal until more clean attempts accumulate.

### Repeated Missed Traps (Key Distinctions missed in 2+ of these 3 exams)
- Key Distinction #12 (two-tool token-binding vs. bypassable parameter, D2 §2.4) — missed in all three exams (Exam 4 Q2, Exam 5 Q54, Exam 6 Q12). No other Key Distinction repeats across 2+ exams in this round.

### Focus Recommendation
Domain: D5 (Context Management & Reliability). Study `Domain-5_v2.md` §5.1 (stateless API / message-history reconstruction — the exact misconception missed this exam) and `Domain-5_v2.md` §5.13 (hybrid context-window design for long-running correction sessions). D5 was flawless for two exams running before this round's sudden drop; closing these two specific sections before Exam 7 will show whether the reversal was real or attempt-specific. Secondary priority, given its three-exam-running miss streak: `Domain-2_v2.md` §2.4 (two-tool token-binding, Key Distinction #12).

---

## Exam 7 — Generated 2026-07-13

**File:** `mock-exams/CCA-Prep_MockTest-7_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Customer Support Resolution Agent; Code Generation with Claude Code; Multi-Agent Research System; Claude Code for Continuous Integration
**Attempt date:** 2026-07-16
**Score source:** results-json
**Total score:** 55 / 60 correct (estimated scaled: 925 / 1000; pass line 720)

First exam generated under orchestration-prompt v10 (CLAUDE.md v2.4) — the only change from v9/v2.3 is a live running-accuracy percentage in the sticky nav (`round(correct/answered×100)`, "—%" at answered=0, red below / green at-or-above the pass-equivalent raw threshold 620/900 = 31/45 ≈ 68.89%, derived precisely from `round((correct/60)×900+100) ≥ 720` rather than assumed); the exam-generation pipeline itself is unchanged from v9. Verified live in browser at three states — 0 answered ("—%"), a partial run at exactly the 31/45 boundary (68.89%, correctly green/pass), and just below it at 30/44 (68.18%, correctly red/fail) and 30/45 (66.67%, correctly red/fail) — plus 60/60 (100%, green).

No domain met the two-consecutive-exam confirmed-weakness bar going into this exam: D2's two-exam streak (Exam 4 45%, Exam 5 72.7%) broke in Exam 6 (held flat at 73.3%, no longer weakest), and D5's Exam 6 drop (100% → 100% → 71.4%) is only a single-exam signal. Exam 7 therefore reverts to the **base FULL-60 distribution, D1 16 / D2 11 / D3 12 / D4 12 / D5 9**, with no confirmed-weakness adjustment — the first time in this project's history no domain triggered the +4/−2/−2 rule. Per Exam 6's Professor's Note, section selection within that fixed base quota was biased toward D5 §5.1 and §5.13 (Exam 6's two D5 misses, both retested in the Customer Support block, Q11/Q12) and D2 §2.4 (Key Distinction #12, seeded twice more — Customer Support Q7 fix-selection facet, Multi-Agent Research Q38 defend-the-pattern facet — a fourth and fifth attempt at the single most persistent trap in this learner's history, missed Exam 4/5/6).

Scenario draw followed GENERATION-INTELLIGENCE.md's rotation guidance after Exam 6: Customer Support, Code Generation, Multi-Agent Research, and Claude Code CI were tied as least-used (count 3 each); Developer Productivity and Structured Data Extraction (count 4 each) rested for a round, bringing the six-scenario spread to a tight 4/4/4/4/3/4 (only Structured Data Extraction now one behind).

Four scenario blocks delegated to parallel sub-agents against a centrally pre-planned block×domain allocation table, solved as a constraint-satisfaction problem before dispatch (every block's primary-domain minimum count exceeds its non-primary maximum; exam-wide quota lands exactly on target) and a pre-planned correct-answer-letter sequence per block (Phase 4.d.5). Block×domain allocation (primary domains bold): Customer Support — **D1 6, D2 4, D5 3**, D3 1, D4 1; Code Generation — **D3 7, D5 3**, D1 2, D2 2, D4 1; Multi-Agent Research — **D1 7, D2 4, D5 3**, D3 1; Claude Code CI — **D3 3, D4 10**, D1 1, D2 1. All four blocks pass the primary-vs-non-primary domain-tally check (Phase 4.e.6 check 4), verified programmatically. Three of four block sub-agents stalled mid-stream on a transient API error during generation and were resumed from their own transcripts (a documented, non-defective property of nested background dispatch — see Phase 4.b.7) rather than restarted from scratch; all four ultimately returned clean, complete blocks.

**One real cross-block citation collision was found and fixed during assembly, not shipped:** the Customer Support block's Q1 ("which named pattern does this exemplify," testing recognition of the "Fresh-plus-summary" named pattern) was drafted correctly against Domain-1_v2 §1.18's named-pattern catalog, but its `whyRight`/`whyWrong` citations were typed as §1.16 instead of §1.18 — colliding with the Code Generation block's independent, correctly-cited §1.16 question (a session-continuity mechanics question, a genuinely different facet: what to do, not what the pattern is called). Fixed by correcting the Customer Support question's three citations to §1.18; content and both questions' text were unchanged, since they test distinct facets of the same underlying concept — no reshuffling needed.

All six Phase 4.e.6 Fidelity Verification Gate checks passed on the shipped file, computed programmatically via a Node script (not hand-tally): 0 invented names exam-wide; correct-answer letters exact 15/15/15/15 exam-wide (each block within 1 of the balanced 4/4/4/3 split — Customer Support A4/B4/C4/D3, Code Generation A4/B4/C3/D4, Multi-Agent Research A4/B3/C4/D4, Claude Code CI A3/B4/C4/D4); stem word count min 38/median 53/max 68 (options min 8/median 16/max 31, both comfortably inside their hard caps, no tightening needed); every block's domain tally passes primary-vs-non-primary with real margins; inline code/config token rate 22.9% (55/240), within the 20–25% target band, concentrated naturally in D2 (25/44 = 56.8%) and D3 (17/48 = 35.4%) options; scenario-rotation disclosure line present on the landing card. A supplementary Jaccard-similarity near-duplicate scan across all 60 stems (threshold 0.35) found zero close pairs. Verified end-to-end in a live browser render (landing card with all new-copy fields, the running-accuracy percentage at multiple boundary states, no console errors), not just static JSON inspection.

**Key Distinction budget:** 5 of 60 questions carry an explicit "Key Distinction #N" citation (well under the 15 cap) — KD#12 seeded twice per the Professor's Note (Q7 fix-selection facet, Q38 defend-the-pattern facet — the fourth and fifth attempts at this project's most persistent trap), KD#25 (Q11, second appearance — Exam 4 correct, Exam 6 missed, this its third test), KD#26 (Q29, Grep vs. Glob, first Code Generation appearance), and KD#28 (Q60, incremental Grep→Read investigation). KD coverage remains 29 of 29 seeded at least once; this exam's seeding priority followed GENERATION-INTELLIGENCE.md's post-29/29 guidance of re-testing weak/unknown learner-signal KDs rather than chasing unused ones.

### Questions Used (deduplication — do not reuse these stems in Exam 8+)

1. [D1] Weeks ago, your coordinator's investigation into two customer accounts suspected of being duplicates stalled pending legal sign-off, and that session was set aside. Sign-off finally arrives, but order histories and refund policy have both changed since then. Rather than resuming the old session, an engineer starts a brand-new one and pastes in a three-sentence summary of the original findings. Which named pattern does this exemplify?
2. [D1] Separately, a fraud-review subagent and a billing subagent are wired to message each other directly on suspected-stolen-card cases, skipping the coordinator, to place holds faster. When a customer disputes a hold, the escalation handoff is missing the fraud subagent's original reasoning, because the coordinator's own logs never captured the exchange. What is the most effective fix?
3. [D1] Engineers notice the coordinator never delegates account-merge verification work, even though billing and verification subagent types are fully described in its system prompt with clear scopes. Instead it tries to resolve every merge case itself in one long response. Inspecting its AgentDefinition, the only tool listed is get_customer. What most reliably fixes this?
4. [D1] The verification subagent's findings return, and the coordinator's synthesis recommends the merge is safe to proceed. Reviewing the draft, the coordinator itself notices it never checked whether either account has an active subscription that a merge would silently double-bill. What should the coordinator do next?
5. [D1] Drafting a structured JSON handoff summary for a complex escalation, one API call hits the token limit partway through the payload, returning a max_tokens stop reason. The loop's current logic treats any stop reason other than tool_use as done, so it forwards the truncated, half-written JSON straight to the human queue. What should the loop check instead?
6. [D1] With the merge complete, a customer asks for the two accounts' loyalty-tier progress to be combined retroactively into one higher tier. Policy defines tier calculation only for a single continuous account history and says nothing about merged accounts. The agent has already confirmed both accounts and their order histories. What should it do?
7. [D2] Your new merge_duplicate_accounts tool accepts a dry_run: boolean so engineers can preview which subscriptions and order histories would combine before committing. Production logs show the agent sometimes calls it with dry_run=false on the very first attempt, merging accounts with no preview ever generated. Which redesign makes skipping the preview architecturally impossible?
8. [D2] Verifying identity for a merge case, the agent calls get_customer and lookup_order in the same turn. When get_customer needs a retry after a transient failure, the harness appends the retried result before the original lookup_order result, and Claude's next response attributes order details to the wrong customer. What is the most effective fix?
9. [D2] The fraud case in the loyalty-tier dispute needs `escalate_to_human` for a live handoff, but a newer `flag_for_review` tool — which only queues the case for later, asynchronous review — keeps getting called instead when the customer explicitly asks for a person right now. Both descriptions read only a one-line purpose. What is the most effective fix?
10. [D2] Your reissue_shipping_label tool fails two ways: some accounts have hit their monthly reissue cap, others fail because the carrier API credential expired. Both currently return an identical generic error, and the agent retries both the same way — wasting attempts on the cap case and never refreshing credentials on the other. How should the tool's error handling be restructured?
11. [D5] A new reliability mechanism retries any support message that times out by resending it through a background queue, but the retry payload carries only that single message, not the conversation so far. The agent treats the merge case as brand new, though the case ID is unchanged. An engineer proposes adding a session_id field so the API can look up prior turns itself. What is the correct diagnosis?
12. [D5] The merged account's loyalty-tier dispute runs long. Early on, the customer states a corrected tier level, but the team's sliding window keeps only the last 20 message pairs — 25 turns later, the correction has dropped out, and the agent quotes the original, wrong tier again. Which restructuring is most effective?
13. [D5] To route merge-dispute cases, a team proposes having the agent self-rate its confidence 1–10 and auto-escalate anything below 7. Early testing shows several confidently-scored cases were resolved incorrectly, while some cases scored below the threshold turned out to be straightforward. What is the most effective way to design this routing decision instead?
14. [D3] In the support bot's own repository, the billing subagent's Python files follow one validation pattern, the returns subagent's TypeScript files follow another, and both subagents' test files sit scattered next to the code they cover. Engineers want the right convention applied automatically based on which files are being touched. Which configuration best achieves this?
15. [D4] A customer writes only "the merge thing still isn't right" — it could mean the loyalty tier, the combined order history display, or a duplicate charge from before the accounts merged. Asking which of the three they mean, plus follow-up details for each, would take several more messages. What should the agent do?
16. [D3] Your coding agent applies a required commit-message convention during some Claude Code sessions but skips it in others, even though every developer's repo checkout is identical and up to date. Two developers working on the same branch see opposite behavior in the same afternoon. What is the most effective first diagnostic step?
17. [D3] Your team's `/cleanup-artifacts` skill deletes stale build outputs after each release. A typo in one invocation modified source files outside the build directory. The team wants the skill hard-restricted to file-write operations only — no shell access, no reads elsewhere. Which configuration change is most effective?
18. [D3] A developer on your team wants a personal `/tidy-imports` slash command for their own pre-commit habit. Teammates haven't asked for it and shouldn't see it appear automatically after cloning the repo. Where should the developer create the command file so it stays personal to them?
19. [D3] A stack trace pinpoints a missing null check in exactly one function, in one file, with a clear one-line fix already identified. Before asking Claude Code to make the change, an engineer debates opening plan mode first to review the surrounding file. Which approach is most effective?
20. [D3] You asked Claude Code to fix a date-parsing helper that mishandles daylight-saving transitions. Prompted only with 'make sure daylight saving is handled correctly,' each of two attempts fixes the specific transition date you mentioned but breaks a different one you didn't mention. What is the most effective approach for the next iteration?
21. [D3] Your CI pipeline already invokes the coding assistant with `--output-format json` so a downstream dashboard can ingest findings automatically. Roughly one run in twenty returns a valid JSON object that's simply missing the `severity` field, and the ingestion job crashes whenever that happens. What is the most effective fix?
22. [D3] Your project CLAUDE.md holds two things: general coding conventions every session should follow, and a lengthy checklist for the recurring security-review pass that only a fraction of sessions ever run. Engineers doing routine feature work say the security checklist clutters every session's context for no benefit. Which restructuring is most effective?
23. [D5] A pairing session redesigning a search endpoint's caching layer reaches 60,000 tokens. It contains an agreed cache TTL value, the chosen invalidation-key format, several long tangents comparing caching libraries, and the last few exchanges finalizing the implementation. You need to cut tokens while keeping the session useful. Which context management strategy is most effective?
24. [D5] Your team wants to retire a deprecated authentication middleware used across roughly 90 API route handlers. Mapping every route that imports it produces a long list of file paths and call context, and running that discovery in the main session threatens to fill the context window before the replacement design conversation starts. What is the most effective way to proceed?
25. [D5] Your coding assistant runs three separate static-analysis tools during review, and each reports severity differently: one uses `1`/`2`/`3`, another uses `low`/`medium`/`high`, and a third uses `info`/`warn`/`error`. Findings from all three accumulate in the session, and the assistant's own severity summaries have started contradicting each other. What is the most effective fix?
26. [D1] A Claude Code investigation into a legacy billing module ran three weeks ago and is saved as a named session. Since then, a different team has substantially rewritten the module across dozens of files, and the original investigation's tool results no longer reflect the current code at all. What is the most effective way to continue the work?
27. [D1] Claude Code writes a CSV-export function and, in its own reasoning, confirms it streams rows instead of loading the full result set into memory. Asked in that same conversation to review its own change, it reports the approach is sound. Weeks later, a memory spike in production traces back to this function silently buffering the entire result set. What most directly addresses why the same-session check missed this?
28. [D2] Your team wires an internal component-library MCP server into Claude Code so it can scaffold new UI components from existing design-system pieces. Before scaffolding, the assistant burns several tool calls issuing guessed `search_components` queries just to discover what components and props even exist. What is the most effective fix?
29. [D2] Before renaming a widely-used validation helper, `sanitizeInput`, across the codebase, the coding assistant runs `Glob("**/sanitizeInput*")` and reports two matches, both inside the helper's own module. A manual check turns up a dozen more files that call the helper but don't have that string in their file name. What should the assistant have used instead?
30. [D4] Your CI pipeline extracts structured findings from static-analysis output using a retry-with-feedback loop against a JSON schema. A `cve_id` field is marked required, and extraction retries up to five times whenever it's missing. Investigation shows 30% of findings are genuinely novel issues with no CVE assigned yet. What is the most effective fix?
31. [D1] The coordinator's prompt for the drone-delivery project is a fixed checklist: search three trade-press sites, open the top six results from each, summarize each in 80 words. Shipped reports keep excluding a newly announced airspace-corridor rule the subagents' own searches already surfaced, since nothing in the checklist calls for pursuing it. Which change to the coordinator's prompt is most effective?
32. [D1] After the coordinator's prompt is rewritten to be goal-oriented, the web-search and document-analysis subagents each hand back long write-ups, which the coordinator stitches into one block before passing it to synthesis. A fact-check later finds the shipped report's "340% pilot-volume growth" claim can't be traced to either subagent's notes. What is the most effective fix?
33. [D1] Every subagent completes successfully on the drone-delivery project: web-search finds relevant articles, document-analysis summarizes filings correctly, synthesis produces coherent text. Yet the report covers only airspace rules and omits noise-ordinance disputes, insurance-liability questions, and neighborhood-acceptance surveys. The coordinator's logs show it decomposed the topic into three airspace-only subtasks. What is the most likely root cause?
34. [D1] For the drone-delivery project's exploratory phase, nobody yet knows whether regulation, cost, or public acceptance will be the binding constraint on adoption — that only becomes clear once initial findings arrive. An engineer proposes a fixed pipeline with steps set up front: search, extract, validate, format. Which decomposition strategy actually fits better, and why?
35. [D1] Investigating insurance-liability precedents in one state, the web-search subagent's query gets rate-limited mid-search and returns nothing further. It reports back only `{"status": "failed"}`, leaving the coordinator no way to judge whether to retry, switch source category, or move on with what it has. What should the failure report include instead?
36. [D1] Two of the five drone-delivery source categories assigned to the web-search subagent — municipal-ordinance archives and insurance bulletins — are down for scheduled maintenance and return nothing; the other three come back complete. Document-analysis processes everything it was handed without trouble. What should the synthesis subagent do given this gap?
37. [D1] While drafting the drone-delivery report, the synthesis subagent keeps needing to confirm isolated details — a statistic, a named regulator, a date — before finishing a paragraph. An audit finds roughly 78% of these are one-off lookups; the remaining 22% require tracing a claim across several filings. Which tool configuration handles this most effectively?
38. [D2] The report-generation subagent's citation-retraction action permanently deletes an excerpt and unlinks it from every section citing it — irreversible. The team built two tools: `preview_retract_citation`, returning a single-use token, and `execute_retract_citation`, which requires it. A teammate argues one tool with a strengthened prompt and few-shot examples would be simpler. Why is the two-tool design still preferable?
39. [D2] Every filing the document-analysis subagent processes needs its jurisdiction, date, and source type extracted before any deeper analysis tool runs. A prompt instruction saying "always call `extract_source_metadata` first" still lets the subagent skip straight to analysis on roughly one run in ten. Which configuration most reliably guarantees the metadata step runs first?
40. [D2] The web-search subagent's ranking tool returns reliability as a 0-1 float, the document-analysis subagent's tool returns a 1-100 integer, and a third-party fact-checking MCP server you cannot modify returns a letter grade A-F. Synthesis occasionally misreads these mismatched scales when choosing which findings to feature. What is the most maintainable fix?
41. [D2] The report-generation subagent calls `compile_report_body`, then in a separate turn calls `append_source_index` — though every finished report always needs both, one right after the other. This doubles the API calls needed per deliverable. What is the most effective way to cut down on this back-and-forth?
42. [D5] The document-analysis subagent now outputs a field-level confidence score for every extracted regulatory fact. Aggregate accuracy across the drone-delivery project sits at 91%, and the team proposes ending human review for every extraction above the confidence threshold. What should the team do before making that change?
43. [D5] The document-analysis subagent pulls two credible readings on drone-corridor safety: a municipal aviation-safety office logs 2.4 near-misses per 10,000 flights; an industry safety consortium puts the same corridor at 0.6 per 10,000. Both pass credibility checks, and the gap could change the report's safety conclusion. What should the subagent do?
44. [D5] Two figures in the drone-delivery report seem to clash: one filing reports a 22% delivery-window reduction, another reports 31%. The synthesis subagent's structured input carries each filing's collection date — the numbers actually come from filings gathered fourteen months apart. Which provenance practice most effectively prevents this from reading as a contradiction while keeping every claim traceable?
45. [D3] The team's shared `/source-audit` skill at project scope loads automatically for every researcher. One researcher wants to pilot a stricter citation-format rule in her own sessions for a week before proposing it team-wide, without changing what the other five see after pulling the same repo. Where should she place the modified skill file, and why does it take effect automatically?
46. [D3] The CI job invokes Claude Code fresh on every PR with only the diff and a generic 'review this code' prompt, no other project context. It repeatedly flags the team's deliberate module-level mutable-state pattern as a bug, even though it is an established, documented convention. What single change would most reduce this recurring false positive?
47. [D3] The team wants to move an iterative review workload to the Message Batches API for the 50% discount: for each file, the review bot fetches related files via tool calls mid-analysis before writing its finding. Is this workload a good fit for the Batches API, and why?
48. [D3] A named pipeline session mapped a service's dependency graph yesterday. Overnight, a separate merge rewrote several files inside that service. This morning's run needs to continue the investigation without reasoning over now-incorrect tool results. What should it do?
49. [D4] The team wants the review bot's terse tone, its requirement to always cite a specific line number, and its finding format to hold consistently across an entire CI run, not just the first response. Where should these constraints be defined?
50. [D4] Developers complain that every PR comment the review bot posts opens with a variant of 'Sure, happy to review this!' before the actual finding. The team wants the filler gone without touching what findings get flagged. What is the most effective fix?
51. [D4] The pipeline must always receive a schema-valid finding object — file, line, severity, fix — even when a PR has no issues, so the ingestion script never parses free text. Two tools are defined: `flag_finding` and `report_no_issues`. Which configuration guarantees structured output on every run?
52. [D4] After the review bot moved to `tool_use` with a strict JSON schema, malformed-JSON failures in the pipeline's ingestion step dropped to zero. Developers still occasionally see a finding that cites the wrong line number for the file it's attached to. What is the most accurate way to interpret this?
53. [D4] The pipeline hand-maintains the finding tool's JSON schema in one config file and a separate Pydantic class validates results afterward. When the team added a new `blocking` severity level, they updated the tool schema but forgot the Pydantic class — every `blocking` finding silently failed validation and was dropped from the PR status for two weeks. What most directly prevents this?
54. [D4] A CI run reviews an 11-file PR in one pass. The bot's comments run long and specific for the first three files, then shrink to one-line 'no issues found' notes for the remaining eight — including a file that actually has an unguarded array index. An engineer proposes moving to a model with a much larger context window. What should the team do instead?
55. [D4] The review bot is asked, within the same conversation that generated a proposed fix, to 'review this change carefully for bugs before finishing.' It reports the fix is safe. A subtle race condition ships anyway and is caught only when a person reviews the diff cold days later. What most directly addresses this?
56. [D4] The review bot should auto-resolve routine flaky-test findings but escalate genuinely ambiguous ones. Logs show it escalates obvious, single-assertion flakiness while trying to resolve complex multi-service timing issues on its own. Auto-resolution sits at 52%, target 80%. What is the most effective fix?
57. [D4] On a PR's third review round, the bot re-flags the exact same 'extract this into a helper' suggestion on a line a developer already replied to, explaining why the duplication is intentional here. Each round's prompt receives only the current diff. What change most effectively stops the bot from re-raising an already-addressed suggestion?
58. [D4] The review bot's 2,600-token system prompt states clear severity-calibration rules. On a long overnight run reviewing PR after PR in one continuous session, by the 12th PR it assigns severities that ignore those rules, drifting toward whatever pattern its own recent comments established. The session is nowhere near a context-window limit. What is the root cause?
59. [D1] Pipeline policy requires a finding only auto-post as a blocking status via `post_blocking_status` after the classification tool has confirmed it as a real defect. Today this rule lives only in the system prompt: 'always classify before blocking.' Audit logs show 11% of blocking statuses were posted without classification ever running. What most reliably fixes this?
60. [D2] A finding flags a possible unhandled null case in a function inside a 40-file service. Before commenting, the review bot needs to confirm whether the same unguarded pattern shows up elsewhere in the service. What is the most effective way for it to investigate?

#### Domain Breakdown
| Domain | Total Q | Correct | % | Confirmed weak? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 15 | 93.8% | no |
| D2 Tool Design & MCP | 11 | 11 | 100% | no |
| D3 Claude Code Config | 12 | 10 | 83.3% | no |
| D4 Prompt Engineering | 12 | 10 | 83.3% | no |
| D5 Context Management | 9 | 9 | 100% | no |

#### Scenario Block Breakdown
| Block | Questions | Correct | % |
|---|---|---|---|
| Customer Support Resolution Agent | 15 | 14 | 93.3% |
| Code Generation with Claude Code | 15 | 13 | 86.7% |
| Multi-Agent Research System | 15 | 15 | 100% |
| Claude Code for Continuous Integration | 15 | 13 | 86.7% |

#### Observations
- **Strongest domains:** D2 (100%, 11/11) and D5 (100%, 9/9). D5's full recovery confirms Exam 6's 71.4% dip was attempt-specific, not a real weakness — exactly what the prior Professor's Note's "watch next" asked to confirm. D2 is the more significant result: this is D2's first-ever perfect score, and critically, **Key Distinction #12 (two-tool token-binding) — this project's single most persistent trap, missed for three consecutive exams (Exam 4, 5, 6) — was answered correctly on BOTH seeded facets this exam** (Q7 fix-selection framing, Q38 defend-the-pattern framing), breaking the streak for the first time.
- **Weakest this paper:** D3 and D4, tied at 83.3% (10/12 each) — the first time either domain has been this paper's weakest. Neither confirms a weakness (Exam 6's weakest was D5, an unrelated domain), so this is a fresh, single-exam signal only.
- **Block breakdown:** Multi-Agent Research perfect (15/15); Customer Support strong (14/15); Code Generation and Claude Code CI both at 86.7% (13/15) — the same two blocks that carried this exam's D3 and D4 misses respectively.
- **Timing:** irregular — 19,489s total (324.8s/question average), but three extreme outliers (Q41: 10,415s / ~2.9h; Q11: 1,835s / ~30.6min; Q39: 1,597s / ~26.6min) account for the bulk of total elapsed time and are consistent with breaks, not think time — the same pattern Exam 4 and Exam 6 showed. Excluding those three, the remaining 57 questions average 99.0s/question, a moderate, unremarkable pace.
- **Traps missed (by question, with the corpus fact each one tested):**
  - Q3 — a coordinator with fully-described subagent types but no `Task` tool in its `allowed_tools` cannot spawn subagents at all, regardless of prompt wording — a structural tool-grant gap, not a prompt problem. Domain-1_v2 §1.3.
  - Q16 — `/memory` is the diagnostic for CLAUDE.md behavior that's inconsistent across otherwise-identical sessions; it shows exactly which memory files loaded, turning a guess into a fact. Domain-3_v2 §3.1.
  - Q19 — a single-file, fully-scoped one-line fix with an already-identified solution is the textbook case for direct execution; plan mode adds unneeded overhead when there is no ambiguity to resolve. Domain-3_v2 §3.6.
  - Q50 — prefilling (a partial assistant message the model continues from) reliably suppresses one specific recurring filler phrase; a system-prompt instruction is less reliable for this narrow a fix. Domain-4_v2 §4.4.
  - Q51 — `tool_choice: {"type":"any"}` forces a tool call while letting the model pick the best-fitting one of several defined tools, guaranteeing structured output on every run including clean cases with no findings; a specific forced-tool choice would block the "no issues" path. Domain-4_v2 §4.6.
  - Note: Q50 and Q51 are adjacent, back-to-back misses in the Claude Code CI block, both in the D4 structured-output-guarantee mechanism family (prefilling vs. system-prompt instructions; `tool_choice: "any"` vs. a specific forced tool) — worth watching as a possible clustered gap rather than two unrelated misses.

### Questions Used
Already logged under the Exam 7 generation entry above — no new stems from scoring.

---

### Professor's Note — Intent for Exam 8

Written after Exam 7 (2026-07-16). Based on results-json.
- **Misconceptions revealed:**
  1. D3 §3.6 (plan mode vs. direct execution) — reached for plan mode on a single-file, fully-scoped one-line fix that needed no planning at all; the same block also missed §3.1's `/memory` diagnostic, a different D3 concept, so D3's two misses are NOT one narrow trap but two distinct gaps.
  2. D4's two misses (Q50 §4.4 prefilling, Q51 §4.6 `tool_choice: "any"`) landed back-to-back in the same block and both sit in the structured-output-guarantee mechanism family — conflated a system-prompt instruction with prefilling, and a specific forced-tool choice with the "any" configuration that also permits a no-issues response. Worth watching as a possible clustered gap in this specific family, not two unrelated misses.
  3. D1 §1.3 (Task tool grant) — mistook a coordinator's missing `Task` tool grant (a structural, `allowed_tools`-level gap) for a prompt-wording problem.
- **Positive signal worth naming explicitly:** Key Distinction #12 (two-tool token-binding), missed for three consecutive exams (Exam 4, 5, 6) and this project's single most persistent trap, was answered CORRECTLY on BOTH seeded facets this exam — the streak is broken for the first time. D5 also fully recovered to 9/9 (100%), confirming Exam 6's 71.4% dip was attempt-specific, exactly as the prior note's "watch next" anticipated.
- **Weakest this paper:** D3 and D4, tied at 83.3% — suspected, NOT confirmed (first time either has been weakest; Exam 6's weakest domain, D5, is unrelated to both).
- **Intent for next paper:** With neither D3 nor D4 meeting the two-consecutive-exam confirmed-weakness bar (this is each domain's first time as weakest), Exam 8 keeps the base FULL-60 quota (D1 16/D2 11/D3 12/D4 12/D5 9). Within it, bias section selection toward D3 §3.1 (CLAUDE.md/memory diagnostics) and §3.6 (plan mode vs. direct execution) — this exam's two D3 misses — and D4 §4.4 (prefilling) and §4.6 (tool_choice guarantees) — this exam's two clustered D4 misses.
- **Watch next:** whether D3 and/or D4 repeat as weakest (the first step toward a confirmed weakness — neither domain has ever reached that bar in this project) or whether this exam's dip was attempt-specific noise, the same pattern D5 just demonstrated recovering from after Exam 6.

---

## Exam 8 — Generated 2026-07-17

**File:** `mock-exams/CCA-Prep_MockTest-8_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Developer Productivity with Claude; Structured Data Extraction; Customer Support Resolution Agent; Claude Code for Continuous Integration
**Attempt date:** 2026-07-28
**Score source:** results-json
**Total score:** 52 / 60 correct (estimated scaled: 880 / 1000; pass line 720)

Second exam generated under orchestration-prompt v10 (CLAUDE.md v2.4) — no blueprint changes this cycle, same running-accuracy percentage feature as Exam 7. Neither D3 nor D4 met the two-consecutive-exam confirmed-weakness bar going into this exam: both were Exam 7's weakest domains (tied at 83.3%), but that was each domain's first time as weakest, with no prior-exam confirmation to compare against. Exam 8 therefore again uses the **base FULL-60 distribution, D1 16 / D2 11 / D3 12 / D4 12 / D5 9**, with no confirmed-weakness adjustment. Per Exam 7's Professor's Note, section selection within that fixed base quota was biased toward D3 §3.1 (CLAUDE.md/memory diagnosis) and §3.6 (plan mode vs. direct execution) — Exam 7's two D3 misses — and D4 §4.4 (prefilling) and §4.6 (tool_choice guarantees) — Exam 7's two clustered D4 misses. Both bias pairs were re-tested from fresh concrete angles in different scenarios than where they were originally missed (Developer Productivity carries the D3 pair; Structured Data Extraction carries the D4 pair — Exam 7's misses were in Code Generation and Claude Code CI respectively). Key Distinction #23 (behavioral drift: accumulated responses vs. context-window overflow), missed on its first-ever scored appearance in Exam 6, was opportunistically re-seeded a third time at D4 §4.20 in the Claude Code CI block, again with a genuinely different concrete scenario (a PR-description generator's format drift, not a severity-calibration drift).

Scenario draw: with all six official scenarios reaching a perfectly even 4-of-each spread after Exam 7 (see GENERATION-INTELLIGENCE.md Scenario Block Rotation), this draw was chosen on structural grounds instead of rotation-count pressure — every domain lands as primary in exactly two of the four blocks (D1: Developer Productivity + Customer Support; D2: Developer Productivity + Customer Support; D3: Developer Productivity + Claude Code CI; D4: Structured Data Extraction + Claude Code CI; D5: Structured Data Extraction + Customer Support), and Developer Productivity + Claude Code CI jointly carry the D3 bias while Structured Data Extraction + Claude Code CI jointly carry the D4 bias. Rests Code Generation with Claude Code and Multi-Agent Research System for a round.

Four scenario blocks delegated to parallel sub-agents against a centrally pre-planned block×domain allocation table, solved as a constraint-satisfaction problem before dispatch. Block×domain allocation (primary domains bold): Developer Productivity — **D1 7, D2 4, D3 3**, D5 1; Structured Data Extraction — **D4 8, D5 4**, D2 1, D3 2; Customer Support — **D1 9, D2 5, D5 1**; Claude Code CI — **D3 7, D4 4**, D2 1, D5 3. All four blocks pass the primary-vs-non-primary domain-tally check (Phase 4.e.6 check 4), verified programmatically. All four block sub-agents hit a transient API stall mid-generation this session — a broader infrastructure issue affecting the whole batch, not per-agent randomness — and were resumed from their own transcripts rather than restarted (Phase 4.b.7); one block had split its response across two turns after resuming and needed a follow-up message to consolidate into one self-contained JSON array. All four ultimately returned complete, valid blocks.

**One real cross-block issue was found and fixed during assembly, not shipped — the first exam where the newly-added citation-collision tally (recommended after Exam 7's PB-19 finding) caught something before shipping, not after:** the Structured Data Extraction block's jurisdiction-code-validation question and the Customer Support block's policy-catalog question both independently cited D2 §2.6, both testing the identical underlying lesson (guessed exploratory queries fixed by exposing an MCP resource) with only the surface scenario reskinned (jurisdiction codes vs. policy categories) — a genuine near-duplicate the individual blocks' own dedup checks couldn't see across each other. Both section assignments were correct per the coordinating session's pre-dispatch plan; only the content overlapped. Fixed by rewriting the Structured Data Extraction question around a different §2.6 facet (community vs. custom MCP server build-vs-buy) instead of moving its citation — Jaccard similarity between the two questions dropped from a near-duplicate level to 0.10 after the rewrite. A second D2 §2.1 pair (Customer Support's missing-`tool_result`-block defect vs. Claude Code CI's missing-full-conversation-history defect) was reviewed and kept as an intentional dual-facet seed, consistent with Exam 7's Key Distinction #12 precedent — Jaccard similarity 0.31, testing genuinely distinct API mechanics, not a reskin of the same lesson. A full-exam Jaccard near-duplicate scan found no other pair above a 0.30 threshold.

All six Phase 4.e.6 Fidelity Verification Gate checks passed on the shipped file, computed programmatically via a Node script (not hand-tally): 0 invented names exam-wide; correct-answer letters exact 15/15/15/15 exam-wide (each block within 1 of the balanced 4/4/4/3 split — Developer Productivity A4/B4/C4/D3, Structured Data Extraction A4/B4/C3/D4, Customer Support A4/B3/C4/D4, Claude Code CI A3/B4/C4/D4); stem word count min 40/median 55/max 62 (options min 10/median 18/max 34, both comfortably inside their hard caps); every block's domain tally passes primary-vs-non-primary with real margins (Customer Support's D5 margin is thin — 1 primary question vs. 0 non-primary — but still a real, valid pass since no non-primary domain appears in that block at all); inline code/config token rate 24.6% (59/240), within the 20–25% target band, concentrated naturally in D2 (21/44 = 47.7%) and D3 (15/48 = 31.3%) options. Scenario-rotation disclosure line present on the landing card. Verified end-to-end in a live browser render (landing card with all new-copy fields, the running-accuracy percentage at pass/fail states, no console errors), not just static JSON inspection.

**Key Distinction budget:** 3 of 60 questions carry an explicit or clearly-matching Key Distinction citation (well under the 15 cap) — KD#23 (Q53, explicitly tagged, third appearance, first-ever scored miss was Exam 6), KD#12 (Q41, two-tool token-binding for a subscription-cancellation redesign — the section landed in Customer Support's quota naturally, not a deliberate Professor's-Note re-seed this exam), and KD#26 (Q43, Grep vs. Glob, second Code-Generation-adjacent... actually Customer Support appearance, reversing nothing since Q29 in Exam 7 already reversed the original Exam 5 miss). This is a lighter KD load than Exam 7's 5, reflecting that this exam's design was driven by the Professor's Note's D3/D4 section bias rather than a KD-retest sweep.

### Questions Used (deduplication — do not reuse these stems in Exam 9+)

1. [D1] Your onboarding coordinator spawns a mapping subagent to chart a legacy monolith's structure with Grep, Glob, and Read, and a separate test-generation subagent to draft tests for whatever it finds. The test-generation subagent never learns what the mapping subagent discovered unless the coordinator copies those findings into its prompt. Which named architecture pattern does this reflect?
2. [D1] The migration subagent runs a standard agentic loop: it calls Bash to run a codemod script against the legacy monolith, inspects the result, and either continues or stops. On one turn, the response carries no `tool_use` block, only prose summarizing the change just made. What should the orchestrator check to decide whether to stop?
3. [D1] The mapping subagent discovers that the legacy monolith's checkout flow depends on an undocumented internal pricing service, then times out before finishing the rest of its scan. The coordinator tells the test-generation subagent only to 'write tests for the checkout module.' The generated tests never mock the undocumented dependency. What is the most likely root cause?
4. [D1] The coordinator's prompt to the mapping subagents reads like a fixed script: 'Step 1: Grep for exported functions. Step 2: open the first 10 matches. Step 3: summarize each in 50 words.' The resulting map consistently misses modules exporting functions through a non-standard pattern the script never anticipated. Which change to the prompt is most effective?
5. [D1] Asked to map every way the legacy monolith's checkout flow reads and writes data, the coordinator splits the work into subtasks covering only direct SQL queries. All three subagents complete their subtasks correctly. The final map never mentions the caching layer or the billing API the checkout flow also uses. What is the most likely root cause?
6. [D1] Tracing call sites across module boundaries, the dependency-tracing subagent's connection to an internal metadata service times out after it has confirmed 6 of 9 call sites. Per the architecture's error-propagation design, what should its failure report to the coordinator include?
7. [D1] During an automated migration, the coordinator finds 12 modules marked deprecated in code comments but never scheduled for removal, several still with live callers elsewhere in the monolith. Team conventions say nothing about whether deprecated-but-referenced modules should be deleted, archived, or left alone during a migration. What should the coordinator do?
8. [D2] Production logs show the onboarding coordinator's `lookup_symbol` tool (source-code definitions) gets called for roughly 38% of requests that actually needed `lookup_reference` (internal documentation). Both tools are described only as 'looks up information for a given name.' What is the most effective fix?
9. [D2] The `generate_migration_script` tool starts rejecting requests for one legacy module because it exceeds the team's file-size limit for automatic migration — a policy limit, not a service problem. The tool returns a bare `{"error": "failed"}`, and the migration subagent retries the identical call three times before giving up. How should its error handling be restructured?
10. [D2] The mapping subagent pulls each module's owner from three sources: a wiki export returning a full name string, a build-metadata service returning a numeric team ID, and a ticketing system returning an email address. Its onboarding report has started grouping the same team under three different labels. What is the most maintainable fix?
11. [D2] The mapping subagent calls `get_module_metadata` and, in a separate later turn, `get_test_coverage` — even on requests where the onboarding report always needs both together. This adds a full extra API round-trip to nearly every module the subagent covers. What is the most effective way to reduce this overhead?
12. [D3] An engineer's Claude Code sessions investigating the legacy monolith reliably flagged undocumented external dependencies throughout last month's onboarding sprint. Picking the same investigation back up this week, on the same machine and repository checkout, Claude no longer mentions dependency risk at all, even on modules it flagged before. What is the most effective first step?
13. [D3] The mapping subagent's dependency scan flags exactly one call site — a single line in the notifications module — still using a helper the team deprecated last quarter, and confirms no other file references it. The team's migration notes give the exact one-line replacement call. Before making the change, should the engineer open planning mode first?
14. [D3] The team's `/map-legacy-module` skill runs a deep dependency and coverage scan of one module at a time. After it runs mid-investigation, the coordinator's replies slow down and re-explain basics of the onboarding task the engineer already established, as if earlier context had been pushed out. Which fix keeps the skill's full depth while preventing this?
15. [D5] The migration subagent has been converting the legacy monolith's data-layer modules to a new schema one at a time across a multi-day run — 40 of 120 modules done — when the coordinator's host process crashes and restarts. The migration plan itself hasn't changed. What should the architecture do to avoid re-converting the 40 completed modules?
16. [D4] The extraction pipeline sends any document that doesn't fit its three extraction tools to an on-call queue with a free-text status note. Every note opens with 'I apologize for the inconvenience, but...' before the actual problem, and the queue's ticket list truncates each note at 80 characters, so the real detail rarely shows. What is the most effective fix?
17. [D4] Before any of the three extraction tools can run, the pipeline must call `redact_sensitive_fields` on every document, since downstream storage may never hold unredacted PII. With `tool_choice` left at its default, logs show the model sometimes calls an extraction tool directly on raw text, skipping redaction. Which `tool_choice` configuration most reliably closes this gap?
18. [D4] `extract_invoice`'s `payment_terms` field must normalize wildly varied source phrasing — 'net thirty days,' '30D,' 'due within 30 days of invoice date,' 'COD' — into a fixed enum. Prose instructions alone leave these phrasings inconsistent, though already-standard phrasing like 'Net 30' normalizes correctly every time. How should the team select few-shot examples to fix this?
19. [D4] `extract_invoice` must also flag duplicate line items — same SKU, matching or near-matching unit price, listed more than once on the same document. Prompted with only the target field name, duplicate detection misses roughly a third of true duplicates once an invoice has more than eight line items. Which prompting addition most reliably improves accuracy here?
20. [D4] `extract_invoice`'s schema marks `vat_registration_number` as required and non-nullable, reasoning that every business-to-business invoice needs one for tax filing. An audit of 4,000 extracted invoices finds 13% carry a plausible-looking VAT number that traces to no real registration — those vendors were below the VAT threshold and never had one. What schema change most directly stops this?
21. [D4] Since `extract_invoice` moved to `tool_use` with a strict schema, every response parses cleanly and every field passes its type check — zero validation failures for three straight weeks. Auditors still occasionally find invoices where `invoice_date` and `due_date` are swapped: both are valid dates, just in the wrong field. How should the team interpret this?
22. [D4] The retry loop resubmits failed extractions with the document, prior output, and validation error. On a batch of `extract_delivery_confirmation` documents, `carrier_tracking_number` keeps failing every retry; investigation shows the number only appears on the shipping label, a separate document the pipeline never receives. An engineer wants to raise max retries to 8. What should the team do instead?
23. [D4] The pipeline also processes vendor contracts alongside invoices. A contract's cover page states 'This agreement includes 8 exhibits,' and extraction separately lists each exhibit heading found in the body. Weeks later, a compliance review finds a contract with only 6 actual exhibit headings — the stated count was simply wrong. What design change most directly catches this?
24. [D5] During a long correction session, an analyst states early on: 'Documents from this vendor should always route to `extract_receipt`, never `extract_invoice`.' Sixty exchanges later, after several rounds of summarization, the pipeline routes a new document from that same vendor to `extract_invoice` again — the summarized history now reads only 'a vendor-specific routing exception was discussed.' What fix is most effective?
25. [D5] Before documents reach the three extraction tools, `run_ocr_pass` returns page-level bounding boxes, per-character confidence scores, and font metadata — 60+ fields per page — when only the plain text and overall page confidence matter downstream. On multi-page scans, this bulk accumulates in context and later pages' extractions start drifting. What is the most effective fix?
26. [D5] A submission bundle includes an invoice and its matching delivery confirmation for the same order. `extract_invoice` reports 500 units of a line item; `extract_delivery_confirmation` reports 480 units for the identical item. Both documents are legible and internally consistent. How should the pipeline handle this discrepancy?
27. [D5] The pipeline's monthly reconciliation report merges extracted due dates, amounts, and payment references from dozens of vendor statements into one continuous narrative paragraph per vendor, done for a more uniform reading style. Auditors say the report is now hard to scan and cross-check line by line against the source statements. What is the most effective fix?
28. [D2] The pipeline needs jurisdiction-code validation for cross-border shipments. A well-maintained community MCP server already wraps the international registry this requires, but an engineer proposes building a custom in-house server instead, arguing it gives the team full control over the validation logic. What is the most effective approach?
29. [D3] A nightly `claude -p` job writes one JSON record per batch — `batch_id`, `exceptions_found`, `flagged_document_ids` — to a ledger file a compliance script parses. On batches with zero exceptions, the job sometimes replies with a line like 'No exceptions were found' instead of the record, and the parser throws. What is the most reliable fix?
30. [D3] The pipeline's nightly run submits 3,000 document-extraction requests through the Message Batches API. An engineer's first implementation leaves every request's `custom_id` set to the same placeholder value. Results return the next morning in a different order than submitted, and the pipeline can't tell which record belongs to which document. What is the most effective fix?
31. [D1] Your coordinator's subagent roster lists a `returns_agent` and a `billing_agent`, both with the `description` field set to the same generic text: 'Handles customer requests.' Both subagents already have correctly scoped `allowed_tools` and accurate system prompts for their roles. Logs show the coordinator routes billing-dispute cases to `returns_agent` roughly a third of the time. What change most effectively fixes the routing?
32. [D1] Investigating a loyalty-tier dispute, two subagents return conflicting data: the account-history subagent reports Gold tier reached March 3, while the billing subagent's audit log shows the upgrade posting March 18. Both cite their own tool calls confidently, and the discrepancy changes which perks apply. What should the coordinator do?
33. [D1] Every standard refund case follows the same sequence: verify identity, confirm eligibility, check the return window, then process the refund — identical steps across roughly 40,000 cases last quarter. An engineer proposes replacing this scripted flow with dynamic decomposition that re-plans the investigation from scratch on every case. What is the most effective decomposition strategy?
34. [D1] Your coordinator delegates a three-charge billing dispute to the billing subagent, which returns a resolution draft addressing two of the three disputed charges and says nothing about the third. This is the coordinator's first evaluation of the draft. What should the coordinator do?
35. [D1] A refund-eligibility check on a disputed high-value order runs three verification calls in parallel: payment-method match, shipping-address match, and prior-dispute-history lookup. The prior-dispute-history call times out; the other two return clean results confirming legitimacy. The agent must produce a recommendation for the human reviewer queue. How should this output be structured?
36. [D1] Your `update_shipping_address` tool was built as a general-purpose order-modification endpoint: beyond address fields, it also accepts optional `refund_amount` and `cancel_order` parameters 'for convenience.' The returns subagent, scoped only to handle address corrections, has started passing `refund_amount` through this same tool to issue refunds directly. What is the most effective fix?
37. [D1] Your escalation handoff payload already includes `customer_id`, `order_id`, and `issue_summary`, so human agents no longer re-ask customers for basic details. Agents still report spending several minutes per case re-reading raw tool outputs to figure out what the bot already tried and what it thinks should happen next. What is the most effective fix?
38. [D1] Once `escalate_to_human` fires on a case, a human takes over review — but your support bot's loop has no way to know that and keeps running. Logs show 8% of escalated cases get an automatic `process_refund` call from the same session minutes later, occasionally issuing a refund the human was still reviewing for denial. What change most reliably prevents this?
39. [D1] A customer's message raises three independent issues: a shipping delay on one order, an unrelated loyalty-tier question, and a request to update the email on file. Your coordinator emits one `Task` call, waits for the result, then emits the next `Task` call in a following response — tripling wall-clock latency versus a similar single-issue case. What is the most effective fix?
40. [D2] A first implementation of your support bot's tool-calling harness gets a response with `stop_reason: 'tool_use'` naming `lookup_order`, executes the tool, then sends a new user-role text message describing the result instead of a proper tool result. Claude's next reply is confused and sometimes repeats the call. What is the most effective fix?
41. [D2] Your `cancel_subscription` action is irreversible once it runs, so it was split into `preview_cancel_subscription` (returns impact details plus a single-use confirmation token) and `execute_cancel_subscription` (requires that token). A teammate calls this over-engineered and proposes one `cancel_subscription` tool with a `confirmed: boolean` parameter, backed by a strengthened prompt and worked examples. Why keep the two-tool design?
42. [D2] Your returns subagent currently selects correctly among its 5 role-scoped tools nearly every time. A product manager wants to fold in 13 more tools — order-modification variants, loyalty adjustments, and shipping overrides — so the same subagent can handle anything a customer might ask in one place. What is the most effective response to this proposal?
43. [D2] An engineer investigating why `process_refund` sometimes computes the wrong discount wants to find every file in the codebase that references a deprecated `legacyDiscountRate` variable, regardless of what the containing file happens to be named. Which built-in tool should they reach for first?
44. [D2] Your coordinator burns 4-6 tool calls per session issuing guessed `search_policies` queries just to discover what refund-policy categories even exist, before it can search productively for the one relevant to a case. The policy-lookup MCP server could expose a category index without requiring a tool call. What is the most effective fix?
45. [D5] Your support bot's system prompt states a firm rule: never promise a specific refund timeline beyond 'within our standard processing window.' This holds reliably in short conversations. In extended, multi-issue conversations running 30+ turns — still well within the token limit throughout — logs show the agent increasingly gives specific day-counts instead. What is the most effective fix?
46. [D3] The pipeline's review bot must apply stricter conventions to files under services/payments/, relaxed conventions to services/notifications/, and a shared testing convention to test files scattered next to the code they cover. What configuration makes the right convention load automatically based on which files are in a PR's diff?
47. [D3] The pipeline's `/triage-failure` command should take a CI job's failure category as an argument, invoked as `/triage-failure flaky-test`. Inside the command file, an engineer references the typed text as `$INPUT`. Every invocation instead produces a note containing the literal string `$INPUT`, never the category actually typed. What is the most effective fix?
48. [D3] An engineer copies the shared `/review-checklist` skill into `~/.claude/skills/review-checklist/` on their laptop to trial a stricter severity rule before proposing it to the team. The same `/review-checklist` skill also runs inside the CI job on every pull request. What happens when the review bot runs inside the CI job?
49. [D3] An engineer asks Claude Code to fix a bug in the pipeline's finding-formatter script: PR titles containing an ampersand or embedded quote break the JSON payload the ingestion API expects. Each prose re-description ('handle special characters') fixes only the character just mentioned, leaving others broken. What converges on a complete fix?
50. [D3] The pipeline re-runs the review bot from a blank prompt on every commit pushed to an open PR. A PR with five findings on push one gets, after push two fixes three, a review reporting only two new nits — the two unaddressed findings go unmentioned. What is the most effective fix?
51. [D3] The pipeline's shared CLAUDE.md has grown past 600 lines covering linting, commit-message format, security-review criteria, and release-notes formatting in one file. Because every engineer edits the same file for unrelated changes, PRs touching it now collide in merge conflicts weekly. Which restructuring most reduces these conflicts while keeping all content available every session?
52. [D3] Reviewing twelve PRs in one long session, an engineer runs `/compact` as the context nears its limit. Afterward, the review bot describes test coverage as 'roughly a third' — the tool output with the exact figure, 34.2%, was part of what got compressed away. What does this show about `/compact`, and what should the team do for sessions where exact figures matter?
53. [D4] A nightly job feeds the pipeline's PR-description generator one merged PR after another in a single long-running session. It reliably writes the required three-part format for the first several PRs, then by the ninth PR, in a session still under 4,000 tokens, drops the 'Risk' section and writes one free-flowing paragraph instead. What is the most likely root cause?
54. [D4] The team wants to move the pipeline's nightly dependency-vulnerability scan, which processes roughly 8,000 files, onto the Message Batches API for the 50% discount. An engineer proposes submitting all 8,000 files in one batch tonight and refining the extraction prompt based on tomorrow's results if needed. What is the most effective way to de-risk this rollout?
55. [D4] The pipeline's nightly test-generation step uses one prompt that both decides which scenarios a function needs and writes the test code for each in the same pass. Only the two or three most obvious scenarios get real depth; the rest get a one-line test or are skipped. What restructuring gives scenario identification its own full attention?
56. [D4] The pipeline's cross-service impact check is instructed only to 'flag changes that might affect other services.' Reviewing a shared authentication helper, it flags a same-file variable rename as cross-service risk while missing an actual signature change to a function three other services call directly. What change would most reliably fix this inconsistent flagging?
57. [D2] The review bot's response returns `stop_reason: 'tool_use'` requesting a `fetch_file_contents` call. The harness runs the tool, then sends only a new message with the `tool_result` block back — omitting the original conversation and the `tool_use` block. The next response comes back confused, as if it never asked for the file. What is the most likely cause?
58. [D5] The review bot ingests one consolidated 60,000-token diff bundle for a large PR in a single pass. Its summary covers the diff's opening version bumps and closing test updates, but never mentions a breaking return-type change sitting in the bundle's middle third — exactly what downstream callers need to know. What is the most effective fix?
59. [D5] A Claude Code session debugging a flaky nightly pipeline job runs long, reaching 70,000 tokens. Early on, the failing test's name, the commit SHA that introduced the flake, and a config value already ruled out get established; most of the rest is exploratory back-and-forth chasing false leads. Which context management strategy best cuts token cost from here?
60. [D5] Before generating tests for a legacy billing module with almost no coverage, the pipeline's test-generation step first surveys all 90 functions directly in its own session, reading each one and cataloging dependencies. By the time the survey finishes, the session's context is nearly full, leaving little room to write the new tests. What is the most effective restructuring?

#### Domain Breakdown
| Domain | Total Q | Correct | % | Confirmed weak? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 15 | 93.8% | no |
| D2 Tool Design & MCP | 11 | 10 | 90.9% | no |
| D3 Claude Code Config | 12 | 9 | 75.0% | no (mechanically) — see note |
| D4 Prompt Engineering | 12 | 9 | 75.0% | no (mechanically) — see note |
| D5 Context Management | 9 | 9 | 100% | no |

#### Scenario Block Breakdown
| Block | Questions | Correct | % |
|---|---|---|---|
| Developer Productivity with Claude | 15 | 12 | 80.0% |
| Structured Data Extraction | 15 | 12 | 80.0% |
| Customer Support Resolution Agent | 15 | 14 | 93.3% |
| Claude Code for Continuous Integration | 15 | 14 | 93.3% |

#### Observations
- **The targeted re-test worked as a diagnostic — and the verdict is decisive.** Exam 8 deliberately biased section selection toward Exam 7's four flagged misses (D3 §3.1, §3.6; D4 §4.4, §4.6), each re-tested from a fresh concrete angle. Of the four: **D3 §3.1 (Q12) missed again, D3 §3.6 (Q13) missed again, D4 §4.6 (Q17) missed again — and only D4 §4.4 (Q16, prefilling) recovered to correct.** This is exactly the "watch next" question Exam 7's note posed, now answered: three of these four are **real, persistent gaps, not attempt-specific noise** — they survived a fresh re-test in a different scenario. Only prefilling cleared.
- **D3 and D4 are the joint-weakest domains for the SECOND consecutive scored exam** (Exam 7: tied at 83.3%; Exam 8: tied at 75.0%) — and both got *worse*, not better, despite the bias. Same two domains, two exams running. See the confirmed-weakness note below for why the mechanical +4 quota adjustment still does not fire (and structurally cannot) on a two-domain tie, and why the section-bias mechanism is the right lever instead.
- **The weakness is domain-wide breadth, not four narrow traps.** Beyond the three re-tested misses, the other D3/D4 misses landed on *fresh* sections: D3 §3.11 (Q51, CLAUDE.md → `.claude/rules/` modularization) and D4 §4.2 (Q19, chain-of-thought for N-item comparison) and §4.9 (Q22, nullable-when-absent). D3's three misses span §3.1/§3.6/§3.11; D4's span §4.2/§4.6/§4.9. This is the same "genuine breadth gap, not one misconception" diagnosis Exam 4 first made about D2 — now recurring in D3 and D4.
- **A discernible meta-pattern in roughly half the misses: over-engineering / symptom-patching over the proportionate root-cause move.** Q11 (§2.8) chose a `PreToolUse` hook over the simpler prompt-bundling fix; Q12 (§3.1) chose re-typing the instruction over running the `/memory` diagnostic; Q13 (§3.6) chose plan mode over direct execution on an already-fully-scoped one-line change; Q51 (§3.11) chose a half-measure partial split over the clean full split. All four reach for a heavier or symptom-level response where the corpus wants the proportionate, direct one — the "try the simple fix / fix the root cause first" heuristic from the Answer Pattern Heuristics table. The remaining D4 misses (§4.2 few-shot-vs-CoT, §4.9 nullable-vs-required) and the D1 miss (§1.8 re-delegate-vs-ship-with-caveat) are more specific-mechanism confusions than instances of this thread.
- **Strong positive signals:** D5 perfect (9/9) for the fourth time in five scored exams. D1 (94%) and D2 (91%) both strong. **All three Key-Distinction-seeded questions were correct** — KD#12 (Q41, two-tool token-binding, now correct two exams running after its three-exam miss streak — durably cleared), KD#26 (Q43, Grep vs. Glob, correct again), and **KD#23 (Q53, behavioral drift) answered correctly after its first-ever-appearance miss in Exam 6 — recovered.** The learner's Key Distinction record is now clean: zero "weak" KDs remain.
- **Timing:** the cleanest, fastest exam since Exam 5 — 2,121s total, 35.4s/question average, no break-confounding outliers (slowest five: 95s, 79s, 77s, 58s, 56s, all consistent with genuine think-time). Notably, the three re-missed sections were not rushed (Q12 took 77s, the second-slowest question on the paper; Q13 37s; Q17 37s) — these are considered wrong answers, not careless ones, which strengthens the "real gap" reading.

### Questions Used
Already logged under the Exam 8 generation entry above — no new stems from scoring.

---

### Professor's Note — Intent for Exam 10

Written after Exam 8 (2026-07-28). Based on results-json. **Note the numbering: this is titled "Intent for Exam 10," not Exam 9, because Exam 9 was already generated (2026-07-19) while Exam 8 sat unscored — and Exam 9 was correctly generated as a broad representative paper precisely because no scored signal existed for it to consume. This Exam 8 result is what re-arms the targeting mechanism, and Exam 10 is the first ungenerated paper that can act on it.**

- **Misconceptions revealed (all traced to this exam's 8 actual wrong answers):**
  1. **Three of Exam 7's four flagged sections missed AGAIN on a fresh re-test** — D3 §3.1 (`/memory` diagnostic vs. re-typing the instruction), D3 §3.6 (direct execution vs. plan mode on a fully-scoped one-liner), and D4 §4.6 (forcing a *specific* tool via `tool_choice` vs. `"any"`, which only guarantees *some* tool). These are now confirmed real, not attempt-specific. D4 §4.4 (prefilling) recovered.
  2. **A domain-wide breadth gap in D3 and D4, not four narrow traps** — the other misses hit fresh sections (D3 §3.11 rules-modularization, D4 §4.2 chain-of-thought-for-N-item-comparison, D4 §4.9 nullable-when-data-absent), so re-testing only the three known-missed sections would under-serve the actual gap.
  3. **A recurring over-engineering / symptom-patch reflex in ~half the misses** — reaching for a hook, a re-typed reminder, plan mode, or a half-split where the corpus wants the proportionate direct fix (Q11 §2.8, Q12 §3.1, Q13 §3.6, Q51 §3.11). Worth a deliberate cluster of "proportionate first response" items across D3.
- **Weakest this paper:** D3 and D4, tied at 75.0% — **now the joint-weakest domain for the second consecutive scored exam** (Exam 7 also tied them, at 83.3%), and both declined rather than recovered. This is a genuine, strengthening two-exam signal.
- **Confirmed-weakness determination:** confirmed_weakness = **false in the mechanical sense**, and deliberately so. The orchestration-prompt rule requires a *single* domain "unambiguously weakest in both consecutive exams"; a two-domain tie in both exams has no single unambiguous weakest, so the +4/−2/−2 quota adjustment has no unambiguous target and structurally cannot apply (you cannot +4 two domains at once). BUT this must NOT be read as "no real weakness" — the two-exam co-weakness plus the 3-of-4 failed re-tests is a stronger real signal than the single-domain mechanical rule was built to capture. The correct response is the section-bias mechanism (Phase 4c.5), which targets WHICH sections without changing HOW MANY questions and can therefore serve both D3 and D4 at once.
- **Intent for next paper (Exam 10):** keep the base FULL-60 quota (no confirmed-weakness adjustment — a two-domain tie has no single quota target). Within it, bias D3's 12 and D4's 12 questions hard toward: (a) a THIRD re-test of the three still-missed sections — D3 §3.1, D3 §3.6, D4 §4.6 — since two attempts have now failed and the third decides whether this is a stubborn gap or slowly closing; (b) broad representative coverage of the *rest* of D3 and D4 including the fresh misses §3.11, §4.2, §4.9, since the gap is domain-wide breadth; and (c) a deliberate 2–3 question "proportionate response vs. over-engineering" cluster in D3, since that reflex showed up repeatedly. Do NOT re-narrow to only the four originally-flagged sections.
- **Watch next:** whether the third re-test of D3 §3.1/§3.6 and D4 §4.6 finally lands (closing the gap) or misses a third time (a genuinely stubborn misconception warranting a corpus-study recommendation, not just more exam exposure) — and whether D3/D4 as domains climb back toward the ~90%+ that D1/D2/D5 now sit at, or stay stuck in the mid-70s.

---

*Next exam: Exam 9 (already generated — score it next). Next deduplication check: all 30 Exam-1 stems + all 60 Exam-2 stems + all 60 Exam-3 stems + all 60 Exam-4 stems + all 60 Exam-5 stems + all 60 Exam-6 stems + all 60 Exam-7 stems + all 60 Exam-8 stems above + all 76 practice-test stems are off-limits.*

---

## Exam 9 — Generated 2026-07-19

**File:** `mock-exams/CCA-Prep_MockTest-9_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Code Generation with Claude Code; Multi-Agent Research System; Developer Productivity with Claude; Claude Code for Continuous Integration
**Attempt date:** 2026-08-09
**Score source:** results-json
**Total score:** 49 / 60 correct (estimated scaled: 835 / 1000; pass line 720)

**Note on scoring order:** Exam 9 was generated 2026-07-19 but sat unattempted for three weeks — Exam 10 (2026-07-29) and Exam 11 (2026-07-29) were both attempted/generated before this score arrived. Per orchestration-prompt v10 Phase 2e, the confirmed-weakness check compares against "the most recent PRIOR SCORED entry" — by scoring chronology (not generation number) that is **Exam 10** (attempted 2026-07-29), not Exam 8. This has a real consequence below.

**Generated with NO new learner signal — the first time this has happened.** Exam 8 was generated but has not been attempted, so no Professor's Note was written after it. The most recent scored exam remains Exam 7 (55/60, 925/1000), and its note was already fully consumed by Exam 8 (the D3 §3.1/§3.6 and D4 §4.4/§4.6 section bias). Re-applying that same bias to Exam 9 would double down on two domains on the basis of a single unconfirmed result whose follow-up has not yet been measured — so Exam 9 is deliberately a **broad representative paper**: base FULL-60 distribution (D1 16 / D2 11 / D3 12 / D4 12 / D5 9), no confirmed-weakness adjustment (no domain meets the two-consecutive-exam bar), and no section bias. This mirrors the orchestration prompt's own rule for a uniformly-good result — maintain full representative coverage rather than manufacture a target. Scoring Exam 8 is what will re-arm the targeting mechanism for Exam 10.

Scenario draw: Code Generation and Multi-Agent Research were the two least-used (count 4 each) after Exam 8, so both were drawn per the standing rotation guidance. This also rests Customer Support Resolution Agent, which had appeared in **three consecutive exams** (6, 7, 8) and was well overdue a break — the longest consecutive run any scenario has had in this project. Post-Exam-9 spread: Code Generation 5, Multi-Agent Research 5, Developer Productivity 6, Claude Code CI 6, Customer Support 5, Structured Data Extraction 5.

Four scenario blocks delegated to parallel sub-agents against a centrally pre-planned block×domain allocation table, solved as a constraint-satisfaction problem before dispatch, and a pre-planned correct-answer-letter sequence per block. Block×domain allocation (primary domains bold): Code Generation — **D3 6, D5 4**, D1 3, D2 2; Multi-Agent Research — **D1 5, D2 4, D5 3**, D3 1, D4 2; Developer Productivity — **D1 7, D2 5, D3 2**, D5 1; Claude Code CI — **D3 3, D4 10**, D1 1, D5 1. All four blocks pass the primary-vs-non-primary domain-tally check, verified programmatically. All four sub-agents returned complete blocks on the first attempt with no stalls — the first clean parallel dispatch since Exam 6.

**Collision pre-emption — the process change this exam introduced.** With the corpus fully saturated since Exam 8 (every section Heavy), D2's 11 questions cannot cover 9 sections without two repeats — the exact structural condition that produced Exam 8's near-duplicate pair. Rather than let two blind sub-agents converge again and catch it afterward, the two repeat sections were chosen **before dispatch** and each block was told explicitly which facet it owned AND which facet its sibling owned, with hard do-not-write-about constraints: D2 §2.9 split into the `Edit`-anchor/`Read`+`Write`-fallback facet (Code Generation, KD#27) vs. the MCP-tool-vs-built-in-preference facet (Developer Productivity, KD#29); D2 §2.3 split into transient-vs-permanent retryability (Multi-Agent Research) vs. business-rule-vs-permission categories (Developer Productivity). **Both splits held cleanly** — the shipped pairs measure 0.063 and 0.068 Jaccard similarity.

**One real collision still occurred, and it was a new variant again.** The Multi-Agent Research block's D2 §2.6 question and the Developer Productivity block's D2 §2.9 question independently landed on the *same underlying lesson* — a vague MCP tool description losing to a familiar built-in, fixed by rewriting the description — with the same four option archetypes, **despite carrying different citations**. This is the third distinct form of this failure across three exams: Exam 7 was a citation typo on correct content; Exam 8 was two correct citations to the same section with overlapping content; Exam 9 was two *different* sections whose content overlapped, which a citation-collision tally cannot see at all. Caught only by the coordinating session reading the returned blocks against each other before assembly. Fixed by rewriting the Multi-Agent Research question onto a different, unused §2.6 facet (`.mcp.json` project scope with `${VAR}` credential substitution vs. per-developer `~/.claude.json` entries); post-fix similarity 0.065. A second defect was caught by the schema check: the Developer Productivity block's §3.2 question indexed its third `whyWrong` entry to the correct option rather than the remaining distractor — corrected before assembly.

All six Phase 4.e.6 Fidelity Verification Gate checks passed on the shipped file, computed programmatically: 0 invented names exam-wide; correct-answer letters exact 15/15/15/15 (each block within 1 of the balanced 4/4/4/3 split — Code Generation A4/B4/C4/D3, Multi-Agent Research A4/B4/C3/D4, Developer Productivity A4/B3/C4/D4, Claude Code CI A3/B4/C4/D4, every question landing on its centrally assigned letter); stem word count min 43/median 53/max 65 (options min 10/median 17/max 27, both inside their hard caps); every block's domain tally passes primary-vs-non-primary and the exam-wide quota matches target exactly; inline code/config token rate 23.8% (57/240), inside the 20–25% band, concentrated in D2 (23/44) and D3 (23/48); scenario-rotation disclosure present on the landing card. Supplementary: a full-exam Jaccard near-duplicate scan found **zero pairs above a 0.25 threshold** across all 60 stems, and the citation tally found exactly the two intentional double-seeds with no unintentional repeats (58 distinct sections cited). Verified end-to-end in a live browser render — landing card content, and the running-accuracy percentage at five states including the exact 31/45 = 68.89% pass boundary (correctly green) and 30/45 just below it (correctly red) — with zero console errors.

**Key Distinction budget:** 3 of 60 questions carry a clearly-matching Key Distinction citation (well under the 15 cap) — KD#27 (Q14, `Edit` anchor non-unique → `Read`+`Write` fallback), KD#29 (Q41, MCP tool vs. built-in preference), and KD#12 (Q39, two-tool token-binding, framed as a pre-rollout design choice rather than the over-mined `dry_run`-bypass diagnosis). A deliberately light KD load, consistent with this exam's broad-coverage rather than targeted-retest design.

### Questions Used (deduplication — do not reuse these stems in Exam 10+)

1. [D3] Your team splits standards per package. `services/booking/CLAUDE.md` contains the line `Booking conventions: @standards/booking-conventions.md`, and that file sits at the repository root under `standards/`. Sessions in that package never apply the booking conventions, and `/memory` lists the package CLAUDE.md as loaded but not the standards file. What is the most likely cause and fix?
2. [D3] Your `/scaffold-module` skill takes the new module's name as its argument and uses it to name every generated file. Developers frequently invoke it bare, producing placeholder-named files, and the slash-command menu gives no sign that an argument is expected. Which SKILL.md frontmatter key addresses this?
3. [D3] An engineer objects that planning mode is limited: on a cross-module change it explored with Read, Grep, and Glob but would not run the test suite or make a scratch edit to check an assumption. The proposal is to drop planning mode and start every task in direct execution. How should the team respond?
4. [D3] The availability-rules module has a written spec that names its edge cases precisely: overlapping windows, bookings straddling a timezone change, and blackout dates. Your workflow generates the module first, then writes tests against what was produced. Each round surfaces another spec case the code misses, and fixing one regresses another. Which change converges fastest?
5. [D3] A wrapper around `claude -p` scaffolds modules and must hand the module registry four fields per artifact: file path, module type, exported symbols, and follow-up TODOs. An engineer proposes documenting the required shape in CLAUDE.md. Registry ingestion currently fails on roughly one run in twelve. Which change is most reliable?
6. [D3] Your project CLAUDE.md has grown to roughly 380 lines: naming and error-handling conventions every session must follow, plus a release-cut checklist and a data-backfill procedure each used a few times a quarter. An engineer proposes converting the entire file into Skills so nothing loads unless invoked. How should the team evaluate this proposal?
7. [D5] Long modernization sessions now run past 80,000 tokens. They hold exact values the work depends on — the agreed migration batch size, two schema column names, a retry budget in milliseconds — plus long exploratory stretches that led nowhere and recent implementation exchanges. An engineer proposes summarizing everything before the last ten exchanges. Which approach is most effective?
8. [D5] Auditing which nightly jobs still write to the legacy availability table means enumerating every job definition and its queries — output that fills the main session before the team can discuss the replacement write path. An engineer proposes splitting the audit across several sessions joined with `--continue`. How should the team evaluate this?
9. [D5] Dozens of Claude Code session transcripts from this quarter total well past 100,000 tokens. An engineer needs the tradeoff the team accepted when it chose between two locking strategies for the booking module in week three. A teammate proposes tagging every future decision so it can be found later. What is most effective?
10. [D5] Converting the reminders module off a deprecated notification client spans several days and many tool calls, with a different engineer picking it up each morning. Each day starts by re-running the same call-site discovery, because the prior day's findings lived only in that session. What is most effective?
11. [D1] After an expensive analysis of the booking module, the team used `fork_session` to evaluate two migration approaches from that shared baseline. The branch evaluating the first approach then discovers an undocumented dependency on an internal pricing call. An engineer assumes the other branch already knows. What actually happens, and what should the team do?
12. [D1] Your team added a second Claude Code instance to review generated changes before human review, and passes it the generating session's full reasoning transcript along with the diff. Across 40 reviews it has concurred with the generator every time, including on a change a human later flagged as unsafe. What is most effective?
13. [D1] Two workloads run against the scheduling service. New modules are always scaffolded by the same five steps: generate, wire routes, add fixtures, run the suite, update the registry. Separately, a dead-code sweep must find and remove unused helpers whose scope nobody knows until the search runs. Which assignment is correct?
14. [D2] Standardizing an error wrapper, the assistant's `Edit` call fails: the anchor `catch (err) {` appears in fourteen places, so `Edit` cannot tell which occurrence to change. The engineer runs a Bash `sed` substitution instead, which rewrites all fourteen — including two that should have been left alone. What is the sanctioned approach?
15. [D2] Your codegen MCP server exposes `fetch_template`, returning the empty house boilerplate for a module type, and `fetch_reference_module`, returning a production module as a worked example. Both are described only as "Returns example code for a module type." When an engineer asks for a real working example, logs show `fetch_template` is called 40% of the time. What is most effective?
16. [D1] The coordinator's prompt for the antimicrobial-resistance report has grown to forty numbered steps — one added after each incident review, naming exact databases to query and how many results to open. Shipped reports now read as checklists and consistently miss findings the subagents' own searches surfaced. Which change to the coordinator's prompt is most effective?
17. [D1] Findings now reach the synthesis subagent as JSON, but each finding is a single string with the source folded into the sentence: 'Carbapenem resistance rose 18% (hospital-network bulletin).' Synthesis rewrites and merges those sentences, and a spot check finds 1 in 5 shipped citations attached to the wrong document. What is the most effective fix?
18. [D1] The coordinator reviews a synthesis draft and finds it never covers pediatric wards, though the document-analysis subagent logged relevant records earlier. It re-invokes the synthesis subagent with the same findings plus 'also cover pediatric wards.' The redraft adds two hedged sentences and no new evidence. What should the coordinator do instead?
19. [D1] Two of six source categories — a national surveillance archive and a hospital-network bulletin series — are offline for the whole project window and will return nothing this cycle. The synthesis subagent completes a draft from the other four and presents every conclusion with equal confidence. What should its output do instead?
20. [D1] The report-generation subagent has a general-purpose `fetch_resource` tool for pulling excerpts from the project store. Because it accepts any record identifier, the subagent has started quoting raw source material the document-analysis subagent never reviewed. Roughly 7% of shipped paragraphs contain such material. What is the most effective fix?
21. [D2] The research pipeline's MCP server for a licensed surveillance database is configured in each researcher's own `~/.claude.json`, since every researcher holds a personal access credential. New team members routinely have no working database access for days, and two researchers are pointed at a stale endpoint nobody noticed. What is the most effective configuration?
22. [D2] Every retrieval call must carry a date-range parameter bounded to the project's approved study window; records outside it contaminate the trend analysis. A system-prompt rule states this, and an audit finds 6% of calls omit the parameter. An engineer proposes a `PostToolUse` hook that discards results from non-compliant calls. What is the most effective enforcement?
23. [D2] `fetch_surveillance_record` returns `isError: true` with a prose `description` only. The coordinator reads that text to decide retries: it spends the full retry budget on records permanently retracted from the archive — a state no retry can change — while abandoning genuine index timeouts after one attempt. How should the tool's error response be restructured?
24. [D2] To guarantee `extract_study_metadata` runs before any analysis tool, the team set `tool_choice` to that specific tool. It now stays forced on every turn of the document-analysis subagent's loop, and production logs show the subagent calls the metadata tool repeatedly and never reaches its analysis tools. What is the correct configuration?
25. [D5] The document-analysis subagent now emits field-level confidence per extracted fact. After per-segment validation, high-confidence facts are auto-accepted and only low-confidence ones reach a reviewer. Six months on, a reviewer stumbles on a systematic error in an auto-accepted field class nobody had been checking. What should the oversight design add?
26. [D5] A house rule tells the document-analysis subagent that when two credible sources disagree it should keep the figure from the official agency and drop the other. Audit shows 11% of reports now carry a single figure where the pipeline held two, and reviewers cannot see what was discarded. What is the most effective change?
27. [D5] For a consistent house voice, the report-generation subagent renders every finding as narrative prose — including per-ward resistance rates for twelve hospitals and a five-year trend series. Reviewers say they can no longer cross-check figures against the sources and the chronology is hard to follow. What is the most effective fix?
28. [D3] The team's shared `/draft-lint` skill lives at `.claude/skills/draft-lint/SKILL.md`. A researcher built a stricter personal version at `~/.claude/skills/my-draft-lint/SKILL.md`, but typing `/draft-lint` out of habit still runs the team's checks. She wants her own version on that command, with teammates unaffected when they pull. What is the cause and fix?
29. [D4] The synthesis subagent drafts the report, then in the same request is asked to re-read its draft and flag any claim the findings do not fully support. It reports none. A human reviewer later finds three claims that overreach what the underlying records actually said. What most directly addresses this?
30. [D4] The coordinator escalates to a human research lead. The lead's queue shows 62% of escalations are routine calls she simply hands back — which citation form fits a preprint, for instance — while two of the last five genuinely ambiguous scope decisions were made autonomously and had to be redone. What is the most effective fix?
31. [D1] Your team's chore-automation assistant runs a coordinator plus specialist workers. To save a hop, engineers wired the scaffold worker to write results into a shared file the flag-cleanup worker reads directly. Since then the coordinator's run summary no longer reflects what actually happened, and one worker silently consumed a malformed handoff. What should the team change?
32. [D1] The scaffold worker's AgentDefinition sets allowed_tools to Read, Write, and Grep, and its system prompt ends with 'always run the module's test suite before reporting completion.' Across three weeks of runs it has never run the suite once, though it scaffolds files correctly. What is the most effective fix?
33. [D1] The coordinator hands two cleanup workers the same instruction — 'retire the stale feature flags in this repo' — without dividing the flag list. Logs show both workers opened edits on the same three files, one flag was removed twice, and the run took twice as long with no additional flags retired. What is the most effective fix?
34. [D1] A nightly chore run covers 30 repositories. On repository 4, the scaffold worker's template render fails and returns a bare failed status. The coordinator ends the entire run there, so the remaining 26 repositories go untouched and no one learns what the render was attempting. How should the failure be handled?
35. [D1] For three consecutive nightly runs the cleanup worker has failed the same chore on one module: the repo's pre-commit hook rejects its change with a message the worker cannot interpret, and it has exhausted every remedy its instructions describe. Nothing in the team's runbook covers this hook. What is the most appropriate next behavior?
36. [D1] When the assistant escalates a blocked chore, the on-call engineer's queue entry carries only the chore name and a one-line note, and the engineer cannot open the assistant's session. Surveys show engineers routinely re-run the same searches the assistant already ran before they can act. What change most effectively fixes this?
37. [D1] The assistant's client-regeneration chore always runs the same four steps in the same order: fetch the API spec, regenerate the client, run the codegen linter, then open a pull request. Nothing about the sequence depends on what any step discovers. Which named architecture pattern does this design exemplify?
38. [D2] You are building the assistant's own API loop by hand. Claude returns a response with stop_reason 'tool_use' and a tool_use block naming the template renderer. Your code runs the renderer and now holds its output. What must the next request to Claude contain?
39. [D2] The team is designing the flag-retirement tool before rollout. Retiring a flag deletes its code paths across dozens of files and cannot be undone from the assistant's side, so policy requires an impact preview the engineer sees first. A reviewer notes that the assistant chooses its own call sequence. Which design guarantees the preview always precedes execution?
40. [D2] Scaffolding a module always needs both the template manifest and the team's lint profile, yet the assistant requests the manifest in one turn and the lint profile in the next, adding a round-trip to nearly every scaffold. An engineer proposes building a single combined tool that returns both. How should the team evaluate this proposal?
41. [D2] An MCP server exposes a tool that maps a changed file to the exact tests covering it from a maintained index. Logs show the assistant instead shells out through `Bash` to run the whole suite on roughly 70% of chores. The MCP tool's description reads only 'Returns test information.' What is the most effective fix?
42. [D2] The flag-retirement tool fails two ways, neither of which a repeat call can change: some flags are locked pending a compliance review, and some repositories sit outside the assistant's write scope. Both return the same generic 'unable to retire flag' error, so the assistant treats them identically and never surfaces the second for credential escalation. How should the tool's error responses be restructured?
43. [D3] Files the assistant generates under a generated/ path must carry a do-not-edit header and must never be reformatted by the team's usual style pass. That instruction currently sits in root CLAUDE.md, so it loads into every session, and the assistant has begun applying the do-not-edit rule to hand-written files that merely resemble generated ones. Which configuration applies it only where it belongs?
44. [D3] The team ships a `/retire-flag` command from `.claude/commands/` so everyone gets it on clone. Engineers type the command followed by a flag name, but the command file has no placeholder for that name, so the assistant asks which flag is meant on nearly every invocation. What is the most effective fix?
45. [D5] An interactive chore session that began at roughly two seconds per assistant turn is noticeably slower and several times more expensive per turn by exchange 60. The assistant's replies are the same length as at the start, and the session is still well within the context window. What is the primary cause?
46. [D4] The review bot gets its behavior rules — stay terse, never speculate beyond the diff, one finding per comment — in the first user message of each CI run; the system prompt is one generic line. Early comments obey all three; late in a long run the bot writes multi-issue paragraphs and speculates freely. What is the most effective fix?
47. [D4] Each finding carries a `category` field constrained to the enum `correctness`, `security`, `performance`, `style`. A quarterly audit finds that findings fitting none of the four — an expired license header, a banned transitive dependency — are filed confidently as `style`, where triage buries them. What schema change most directly fixes this?
48. [D4] Since findings moved to `tool_use` with a strict schema, the ingestion step has not failed to parse a response in six weeks. Reviewers still report that roughly 5% of findings carry a `suggested_fix` patch that edits a line the pull request never touched. An engineer concludes the schema must still be too loose. How should the team interpret this?
49. [D4] The pipeline validates every finding in code after receiving it — types, enum membership, and rules such as `line` falling inside a changed hunk. An engineer proposes deleting that layer, arguing the tool's JSON schema already guarantees the shape and a second check is dead weight. How should the team respond?
50. [D4] Validation rejects a finding when its `line` falls outside the pull request's changed hunks. On rejection the pipeline resends the diff and prompt with one sentence appended: "The previous output was invalid. Try again." Roughly half of retries fail again, and logs show the bot rewrites the description while leaving the line untouched. What change most improves retry success?
51. [D4] The bot's dependency-upgrade check emits `breaking_changes_found: false` plus a free-text notes field. A post-incident review finds a pull request that merged green while that same finding's notes described a public method the upgrade had removed. The verdict and the evidence contradicted each other and nothing caught it. What design change most directly catches this?
52. [D4] After the review was split into one focused pass per changed file, per-file feedback became uniformly detailed. One defect class still survives: a helper's return type changes in one file and three callers in other files go unflagged, because no pass sees beyond its own file. What should the team add?
53. [D4] The bot's unused-code check is instructed to "report code that is no longer used." On one pull request it flags a new helper that has no caller yet; on another it says nothing about a function whose last caller that same diff deleted. Developers say they cannot predict what it will flag. What change most reliably fixes this?
54. [D4] Measured precision across the bot's four finding categories: security 92%, correctness 88%, style 46%, documentation 44%. Developers now resolve every bot comment without opening it, security findings included. The team needs security findings taken seriously again within this sprint, while the weak categories get fixed. What is the most effective approach?
55. [D4] Developers request a deep-dive review by labelling a pull request and adding a one-line note. On ambiguous notes — "look at the concurrency work" on a diff touching three concurrent paths — the bot asks a clarifying question and waits. Telemetry shows 40% of authors never reply; the job then times out after six hours, holding the merge queue. How should it handle these instead?
56. [D3] A second CI job is added to generate tests for changed modules. Its step invokes Claude Code with the prompt as a positional argument and no flags; the step never returns, and the nightly window closes with no tests generated. Teammates propose four ways to make it run unattended. Which is the documented approach?
57. [D3] Finance asks the team to capture the Message Batches API's 50% discount on its most expensive job: the pre-merge review that blocks a pull request from merging until it posts a status. An engineer notes that in testing every batch came back in under an hour. What should the team do?
58. [D3] To compare two test-generation strategies against one expensive repository-wide analysis, the pipeline resumed the analysis session, ran the first strategy, then continued that same session with the second. Reviewers note the second write-up echoes the first's conclusions and reuses its ordering almost verbatim. What should the pipeline have done?
59. [D1] An audit of last quarter's pull requests finds that 9% of the bot's own blocking findings were dismissed without the file ever being re-read — several on lines no later commit had touched. The requirement to re-read and confirm the lines changed before dismissing exists only as a sentence in the system prompt. What most reliably closes this gap?
60. [D5] Before writing tests, the nightly job calls a coverage tool returning per-line hit counts for every file in the repository plus ninety days of trend history — when only the current module's uncovered ranges matter. Twelve modules in, the window is nearly full and the last modules get one-line placeholder tests. What is the most effective fix?

#### Domain Breakdown
| Domain | Total Q | Correct | % | Confirmed weak? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 14 | 87.5% | no |
| D2 Tool Design & MCP | 11 | 7 | 63.6% | **yes — see below** |
| D3 Claude Code Config | 12 | 11 | 91.7% | no |
| D4 Prompt Engineering | 12 | 10 | 83.3% | no |
| D5 Context Management | 9 | 7 | 77.8% | no |

#### Scenario Block Breakdown
| Block | Questions | Correct | % |
|---|---|---|---|
| Code Generation with Claude Code | 15 | 12 | 80.0% |
| Multi-Agent Research System | 15 | 13 | 86.7% |
| Developer Productivity with Claude | 15 | 11 | 73.3% |
| Claude Code for Continuous Integration | 15 | 13 | 86.7% |

#### Observations

- **D2 is CONFIRMED weak — the second time this domain has crossed the two-consecutive-exam bar in this project's history** (the first was Exam 4→5, which fed Exam 6's quota adjustment). D2 sat at 100% (Exam 7) and 90.9% (Exam 8), looked strong, then declined to 81.8% (Exam 10) and now **63.6% here** — and because Exam 10 is the most recent *prior scored* entry by attempt chronology (not Exam 8), the two-consecutive comparison is Exam 10 (weakest: D2) vs. this exam (weakest: D2, by a wide margin — D5 is next-lowest at 77.8%, a 14-point gap, unambiguous). Confirmed_weakness = **true**, domain = **D2**.
- **The miss is domain-wide breadth, not one trap.** D2's four misses hit four different sections — §2.3 (business vs. permission error categories), §2.6 (shared-server scope: picked per-developer `~/.claude.json` when the answer was project `.mcp.json` with `${VAR}` substitution — the inverse of the intended lesson), §2.8 (built a composite tool instead of prompting the agent to bundle — the same misconception independently missed in Exam 8 Q11 and Exam 10 Q6, now a third instance across three different exams), and §2.9 (**Key Distinction #27** — `Edit` anchor non-unique → `Read`+`Write` fallback — missed on its *second* appearance after being correct on its first, Exam 6).
- **A real tracker gap surfaced while reconciling this score:** Exam 9's three KD-seeded questions (KD#27 Q14, KD#29 Q41, KD#12 Q39) were never added to GENERATION-INTELLIGENCE.md's Key Distinctions Coverage Tracker at generation time, and no later session's rewrite caught the omission — they simply didn't exist in the tracker until this scoring session added them retroactively. Logged as PB-21.
- **Non-D2 misses, no pattern beyond isolated first-exposure gaps:** D1 §1.8 (re-invoked synthesis without gathering new evidence — hedged filler instead of re-delegating to gather what was actually missing), D1 §1.12 (escalation trigger met three retries over, delayed), D3 §3.7 (chose generate-then-patch over test-driven iteration), D4 §4.5 (missed the enum-plus-`other`-field schema pattern for a mostly-known-but-occasionally-new field), D4 §4.17 (chose the slow eventual fix over immediately disabling the two noisy finding categories to stop trust bleed), D5 §5.1 (missed that the stateless API's full-history requirement is the root cause of rising per-turn cost/latency), D5 §5.7 (chose tag-everything over semantic retrieval for a one-off historical lookup).
- **Timing:** 2,529s total, 42.2s/question average, no extreme break-confounding outliers (slowest: Q19 at 156s, Q4 at 87s, Q54 at 106s — all plausible think-time on genuinely harder questions, not gaps).

### Questions Used
Already logged under the Exam 9 generation entry above — no new stems from scoring.

---

### Professor's Note — Intent for Exam 12

Written after Exam 9 (2026-08-09). Based on results-json. **Note the numbering: this is titled "Intent for Exam 12," not Exam 10, because Exam 10 and Exam 11 were both already generated (and Exam 10 already scored) before this result arrived — Exam 9 sat unattempted for three weeks after its 2026-07-19 generation. This mirrors the Exam 8→10 skip precedent exactly: the score that re-arms targeting always aims at the first ungenerated paper that can act on it, which is Exam 12.**

- **Misconceptions revealed:**
  1. **D2 is CONFIRMED weak** (second time in this project's history for this domain) — same domain unambiguously weakest in the two most recent scored exams by attempt chronology (Exam 10: 81.8%; this exam: 63.6%).
  2. **The gap is domain-wide breadth** — four different D2 sections missed (§2.3, §2.6, §2.8, §2.9), not one narrow trap.
  3. **A specific, now three-exam-running misconception**: composite tool over prompt-bundling for habitually-paired calls (§2.8) — missed independently in Exam 8, Exam 10, and this exam.
  4. **Key Distinction #27 broke its clean streak** — correct on its Exam 6 debut, missed on this, its second appearance.
- **Weakest this paper:** D2, 63.6% — **CONFIRMED** (two consecutive scored exams by attempt order: Exam 10, then this one).
- **Confirmed-weakness quota adjustment (orchestration-prompt v10 Phase 4c, D2-collision rule):** FULL-60 base is D1 16/D2 11/D3 12/D4 12/D5 9. Confirmed domain is D2 itself, which triggers the collision rule: **+4 D2, −2 D5, −2 D1** (not the default −2 D2/−2 D5, since D2 can't donate to itself). **Exam 12's quota: D1 14 / D2 15 / D3 12 / D4 12 / D5 7.**
- **Intent for next paper (Exam 12):** within D2's enlarged 15-question quota, spread broadly across all 9 sections (the gap is breadth, not depth) while guaranteeing coverage of this exam's four missed sections (§2.3, §2.6, §2.8, §2.9) and giving §2.8's three-exam-running composite-tool misconception a dedicated, unambiguous test. Re-test KD#27 once more to see if the Exam 9 miss was a one-off or a genuine reversal.
- **Watch next:** does D2 recover meaningfully with the larger, more targeted quota, or does the 100%→90.9%→81.8%→63.6% decline continue even with more attention — the latter would suggest a real, deepening gap rather than an artifact of small-sample section luck.

---

## Exam 10 — Generated 2026-07-28

**File:** `mock-exams/CCA-Prep_MockTest-10_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Customer Support Resolution Agent; Code Generation with Claude Code; Multi-Agent Research System; Structured Data Extraction
**Attempt date:** 2026-07-29
**Score source:** results-json
**Total score:** 54 / 60 correct (estimated scaled: 910 / 1000; pass line 720)

**Note on the pasted results-JSON:** the payload's own `exam_n` field read `9`, not `10` — traced to a real bug in the shipped HTML, not a scoring error. The generating session's build script (which stamps each exam's `DATA` object from a template) correctly set `DATA.exam_n = 10`, but missed a *separate*, redundant hardcoded literal (`exam_n:9`) inside the results-export function, carried over unedited from the `MockTest-9` file it was built from. The block scenarios in the pasted JSON (Customer Support, Code Generation, Multi-Agent Research, Structured Data Extraction) match Exam 10's draw exactly, not Exam 9's (Code Generation, Multi-Agent Research, Developer Productivity, Claude Code CI) — confirming this is unambiguously Exam 10's result. The bug has been fixed in the shipped file (`exam_n:DATA.exam_n, format:DATA.format`, no longer a hardcoded literal, so it cannot recur). Logged as PB-20 in GENERATION-INTELLIGENCE.md.

**Generated consuming the Professor's Note — Intent for Exam 10** (written above, after Exam 8 was scored 2026-07-28: 52/60, 880/1000 scaled). Base FULL-60 distribution unchanged (D1 16 / D2 11 / D3 12 / D4 12 / D5 9) — a two-domain D3/D4 tie has no single unambiguous weakest, so the mechanical +4/−2/−2 quota adjustment structurally could not apply. The section-bias mechanism (Phase 4c.5) carried the targeting instead: D3's 12 and D4's 12 were biased toward (a) a **third re-test** of D3 §3.1, D3 §3.6, and D4 §4.6 — each missed in both Exam 7 and Exam 8 — with fresh facets confirmed non-overlapping against both prior attempts; (b) broad coverage of the rest of D3/D4 including the fresh Exam-8 misses §3.11, §4.2, §4.9; (c) a deliberate 3-question "proportionate response vs. over-engineering" cluster in D3 (g16, g23, g27), targeting the over-engineering/symptom-patch reflex the Exam 8 Professor's Note identified in roughly half that exam's misses.

**Scenario draw:** all four drawn scenarios (Customer Support, Code Generation, Multi-Agent Research, Structured Data Extraction) were tied at count 5 (the four least-used) after Exam 9. Structured Data Extraction was the natural anchor — the only scenario not used in either of the last two exams — while Developer Productivity with Claude and Claude Code for Continuous Integration (count 6 each) were rested per the standing rotation guidance. Post-Exam-10 spread: Customer Support 6, Code Generation 6, Multi-Agent Research 6, Structured Data Extraction 6, Developer Productivity 6, Claude Code CI 6 — **the rotation reaches its first fully even spread (6 each) in this project's history.**

**Serial dispatch — a deliberate process change this exam.** The learner's weekly usage limit was near exhaustion at the start of this session (94%, ~4h to reset), so the four scenario blocks were authored **serially** rather than in parallel, each block's JSON written to disk before the next was dispatched. This traded wall-clock time for resilience: the session limit did in fact interrupt generation mid-Block-2 (before that block had written any output), and because Block 1 was already saved, resuming lost zero completed work — only the in-flight block needed re-dispatch. Recommend formalizing "serial dispatch when usage risk is flagged" as a documented fallback to the standard 4.b.6/4.b.7 parallel-delegation pattern.

Block×domain allocation (primary domains bold): Customer Support — **D1 7, D2 4, D5 2**, D3 1, D4 1; Code Generation — **D3 9, D5 3**, D1 1, D2 1, D4 1; Multi-Agent Research — **D1 7, D2 5, D5 2**, D3 1; Structured Data Extraction — **D4 10, D5 2**, D1 1, D2 1, D3 1. All four blocks pass the primary-vs-non-primary domain-tally check, verified programmatically.

**Collision pre-emption held again.** D2's 11 questions cannot cover its 9 assigned sections without two repeats given full corpus saturation; the two repeat sections were declared before dispatch with disjoint facets: D2 §2.3 split into business-error-vs-protocol-error semantics (Customer Support, g4) vs. machine-readable structured-error content for retry-with-feedback (Structured Data Extraction, g49); D2 §2.6 split into MCP primitive capability-category taxonomy (Customer Support, g3) vs. `.mcp.json` project scope vs. `~/.claude.json` user scope (Multi-Agent Research, g32). Both pairs were independently re-verified after assembly by reading all four full question texts side by side (not just their citations) — confirmed genuinely distinct lessons. No unplanned section repeats occurred anywhere else in the exam (every other domain's assigned sections each used exactly once, confirmed programmatically).

All six Phase 4.e.6 Fidelity Verification Gate checks passed on the shipped file, computed programmatically: 0 invented names exam-wide; correct-answer letters exact 15/15/15/15 (each block within 1 of the balanced split — Customer Support A4/B4/C4/D3, Code Generation A4/B4/C3/D4, Multi-Agent Research A4/B3/C4/D4, Structured Data Extraction A3/B4/C4/D4); stem word count min 36/median 53/max 69 (options min 9/max 27, both inside their hard caps); every block's domain tally passes primary-vs-non-primary and the exam-wide quota matches target exactly; inline code/config token rate 26.7% (64/240), at the top of the acceptable 15–30% band (no rewrite required); scenario-rotation disclosure present on the landing card. Supplementary: a full-exam Jaccard near-duplicate scan found **zero pairs above a 0.30 threshold** across all 60 stems, and the citation tally found exactly the two pre-declared double-seeds with no unintentional repeats.

**Key Distinction budget:** 10 of 60 questions carry a KD citation (within the 15 cap) — KD#23 (g13, behavioral drift vs. context overflow — periodic re-confirmation after its Exam 6 miss/Exam 8 recovery), KD#11 (g7), KD#9 (g5), KD#29 (g18, MCP tool vs. built-in preference), KD#10 (g34), KD#12 (g37, two-tool token-binding — durably cleared, periodic confirmation), KD#14 (g44, Message Batches API), KD#8 (g49), KD#20 (g58, lost-in-the-middle), KD#19 (g60, proceed-vs-ask clarification strategy).

### Questions Used (deduplication — do not reuse these stems in Exam 11+)

1. [D1] Your support agent's harness receives a response with `stop_reason: "tool_use"` containing two tool_use blocks — `get_customer` and `lookup_order`. The loop executes only the first block, appends that single result, and re-invokes Claude, which then re-requests the ignored lookup, adding an extra round-trip to most multi-tool turns. How should the loop handle these responses?
2. [D2] The same harness assumes every response includes a tool call. When a customer opens with a greeting or sends a thank-you, Claude replies with plain text and `stop_reason: "end_turn"`, and the harness throws an exception and drops the conversation. `tool_choice` is left at its default. What should the harness do instead?
3. [D2] Designing the support agent's MCP server, the team must expose three things: refund and escalation actions the agent performs, a return-policy document set the agent only ever reads, and a reusable escalation-summary template. They are deciding which MCP primitive should carry each. Which assignment matches the protocol's capability categories?
4. [D2] Your `process_refund` tool returns a bare `isError: true` whenever a final-sale item is ineligible for refund under written policy. The agent treats these as outages — apologizing for technical difficulties and promising to retry later — and the ops dashboard counts them as tool failures, inflating error rates. How should the tool represent this outcome?
5. [D1] On multi-issue cases, the coordinator runs billing, returns, and delivery subagents in parallel. Today, any subagent hitting a transient database timeout reports a failure upward, and the coordinator aborts the entire case — discarding the other subagents' completed work — before a human restarts it from scratch. Where should this error handling live instead?
6. [D2] Telemetry shows the agent calls `lookup_order`, waits a full turn, then calls `check_return_eligibility` with the same order identifier on nearly every return case — two round-trips where one would do. An engineer has already sketched a combined `lookup_order_with_eligibility` tool and asks you to review the design. What should you recommend?
7. [D1] Privacy rules require verifying identity via `get_customer` before the agent discloses any order detail. After two rounds of system-prompt strengthening, violations fell from 12% to 3% of conversations, then stopped improving — audits still find disclosures to unverified callers every week. The team asks how to reach zero. What should you advise?
8. [D1] To speed up eligibility checks, an engineer gave the returns subagent a general `run_report_query` tool accepting free-form queries against the support database. Logs now show it querying unrelated customer-PII tables mid-case for extra context. A prompt line restricting it to return tables cut the misuse roughly in half. What is the most effective fix?
9. [D5] Mid-conversation, the agent offers a policy-compliant store credit for a damaged item. The customer replies: 'No — I want to talk to a person.' Following its three-attempts-before-escalation instruction, the agent offers a replacement instead, and the customer repeats the demand, now angrier. What behavior should the escalation design enforce here?
10. [D1] A customer reports a package missing. Confirming the claim needs a warehouse-scan lookup, but that system has returned errors for two hours. The agent has silently retried nine times while the customer waits, and no policy covers proceeding without the scan record. What should the agent do now?
11. [D4] A quarterly audit of escalation routing finds the human queue dominated by routine warranty lookups the agent was authorized to resolve, while two goodwill-credit edge cases the agent settled autonomously were later reversed on appeal. No written guidance defines which cases route where. Which change most effectively fixes this calibration?
12. [D1] Escalations currently arrive with a one-line note, and human agents keep re-asking customers for details the agent already gathered. An engineer proposes wiring the human console to display the full conversation transcript at handoff so nothing is lost. How should you evaluate this proposal?
13. [D5] The agent's system prompt requires restating the confirmed order ID whenever any monetary amount is quoted. In long multi-issue conversations this holds for roughly eight turns, then stops — affected sessions measure only about 2,700 tokens, and no summarization or trimming is configured. What is the most likely root cause?
14. [D3] A nightly support-ops job runs `claude -p` to triage the day's unresolved tickets and flag handling errors. Every night it flags the documented under-$5 automatic goodwill credit as an unauthorized refund, because the job receives only the ticket dump and a two-line prompt. What change would most reduce this recurring false positive?
15. [D1] A named Claude Code session spent three days tracing a recurring refund miscalculation through the support tooling. Overnight, teammates rewrote only the tax-and-fees configuration module; everything else the session analyzed is untouched. The team wants to continue this morning without stale conclusions or needless re-analysis. What is the most effective way to continue?
16. [D3] An engineer's Claude Code sessions in the demand-forecasting module reliably flagged missing changelog entries on every commit for weeks. After setting up a new laptop and restoring their project checkout, the same convention never fires again, even on files it used to catch. Rather than investigate, the engineer starts appending 'remember the changelog rule' to every prompt. What is the most effective first step instead?
17. [D3] The inventory-forecasting service is growing: demand-forecasting's Python files need a strict type-hints convention, supplier-sync's Go files need a specific retry-wrapping pattern, and test files scattered across both modules need one shared testing convention. The team wants each convention applied automatically based on which files Claude Code is actually touching, with no engineer needing to remember to mention it. What configuration best achieves this?
18. [D2] The team wires a semantic, embedding-backed code-search tool into Claude Code, expecting it to replace ad-hoc text search for finding conceptually related code across the reporting module. Sessions keep calling `Grep` instead, missing renamed or refactored call sites the semantic tool would have caught. The new tool's description reads only 'Searches code.' What is the most effective fix?
19. [D3] The team's `/backfill-supplier` skill needs a supplier-region code as its argument to scope which records it touches. Nothing in the slash-command menu signals that an argument is required, so engineers regularly invoke it bare, and the skill silently backfills every region at once. Which SKILL.md frontmatter key most directly fixes this?
20. [D1] Claude Code implements a rate limiter for the reporting module's export endpoint, reasons through concurrent-request edge cases in its own response, and concludes the sliding-window logic is correct. Asked in the same conversation to review its own change before merge, it reports no issues. Days later, a burst of concurrent requests reveals the window can double-count under specific timing. What most directly addresses why the same-session check missed this?
21. [D3] A legacy `/rollback-migration` command was written before the team adopted Skills, as a plain file at `.claude/commands/rollback-migration.md` that reads the typed target version as `$ARGUMENTS`. A new hire argues it will stop working soon and must be converted into a `.claude/skills/` folder with a SKILL.md. Is the new hire correct?
22. [D3] A developer wants to skip the slow style pass inside the shared `/lint-check` skill during their own iterative work, without changing what the other six teammates run after pulling the same repo. They are deciding where to put a modified version. Where should they create it, and why does it take effect automatically?
23. [D3] The reporting module needs a new `region_code` field added to the export-request struct, three call sites already identified, and the exact type and default value already agreed in the design doc. Before starting, an engineer opens planning mode so Claude Code can explore the module's structure first. What is the most effective approach?
24. [D5] A debugging session tracing an intermittent supplier-sync failure reaches 55,000 tokens. It holds the exact error code that reproduces the bug, the specific config flag that was ruled out, several dead-end theories chased and abandoned, and the last few exchanges narrowing down the actual cause. The team needs to cut tokens while keeping the session useful going forward. Which strategy is most effective?
25. [D3] A prompt asks Claude Code to convert raw supplier invoices into a normalized export format, described only in prose. Successive runs disagree on how to represent invoice status — one emits `pending`, another `PENDING` — and unit prices sometimes appear as decimals, sometimes as integer minor units. Rewriting the prose with more detail each time hasn't converged the output. What is the most effective next step?
26. [D4] The team wants Claude Code to both flag issues in a changed module and generate fixes for each one it finds, currently handled in a single combined prompt. Output quality is inconsistent — some genuine issues go unflagged, and some generated fixes address problems the pass never explicitly called out. What restructuring would most likely improve both stages?
27. [D3] The reporting module's CLAUDE.md covers formatting conventions every session must follow, plus a lengthy quarterly data-reconciliation procedure and an equally long incident-postmortem template, each invoked only a few times a year. An engineer proposes moving just the reconciliation procedure into a Skill and leaving the postmortem template inline to limit the change's scope. How should the team evaluate this proposal?
28. [D5] The team is retiring a deprecated pagination helper referenced somewhere across the reporting module's roughly 120 files. Mapping every call site and how each one uses the helper produces a long, detailed inventory — and running that mapping in the main session leaves little room for the follow-up conversation about the replacement interface. What is the most effective way to proceed?
29. [D3] A named Claude Code session spent two days investigating recurring timeout errors in the supplier-sync module, mapping its retry-and-connection-pooling logic in detail. Before the team resumes this morning, that entire layer is swapped for a different retry library as part of an unrelated migration — nothing the session mapped still describes how retries actually work. What is the most effective way to continue?
30. [D5] A single long-running Claude Code session is migrating 200 legacy endpoints to a new validation library, one at a time, holding every discovered quirk in conversation history alone. By endpoint 140, its suggestions start referencing generic 'typical' validation patterns instead of the specific quirks it identified for earlier endpoints. What is the most effective way to prevent this?
31. [D1] The coordinator issues three parallel `Task` calls — web-search, filing document-analysis, and internal-report document-analysis — for a packaging-waste compliance review. The web-search subagent returns first, with partial early findings. An engineer wants the coordinator to forward those findings straight to report-generation immediately, without waiting on the other two calls. What should the architecture require instead?
32. [D2] An engineer evaluating a new citation-checking MCP server for personal use adds it to the project's version-controlled `.mcp.json` so 'everyone can see what I'm testing,' even though no teammate uses it yet and it isn't ready to be a shared dependency. What is the most effective correction?
33. [D1] The document-analysis subagent keeps calling `draft_report_section`, a formatting tool meant only for report-generation, even after its `system_prompt` is rewritten twice to say 'only extract and summarize, never draft report text.' Its `AgentDefinition` still lists `draft_report_section` among its `allowed_tools`, left over from an early prototype. What is the most effective fix?
34. [D2] The web-search subagent's `extract_key_findings` tool and the document-analysis subagent's `extract_citations` tool are each described only as 'extracts relevant text from a source.' When a request could plausibly involve either a web page or a filing PDF, selection between the two tools is close to a coin flip. What is the most effective fix?
35. [D1] The coordinator delegates synthesis by telling the subagent to 'use the compliance-cost findings from the filing-review step,' without including those findings in the prompt itself. The synthesis subagent, whose context holds nothing from that step, writes plausible-sounding cost figures that trace to no actual filing. What is the most effective fix?
36. [D5] Mid-batch, the document-analysis subagent finds two credible sources reporting different compliance-cost estimates for the same regulation. Rather than finish analyzing the current filing, it pauses the entire review and messages the coordinator asking which figure to use before it will continue to the next document. What should the design require instead?
37. [D2] The report-generation subagent's `finalize_and_distribute_report` tool accepts a `send_now: boolean` so an internal QA pass can run before external distribution. Logs show it is sometimes called with `send_now=true` on the very first attempt, skipping the QA preview entirely. Which redesign makes skipping the preview architecturally impossible?
38. [D1] Investigating packaging-waste compliance costs, the coordinator delegates 'financing and grant mechanisms' to both the web-search subagent and the document-analysis subagent without distinguishing their scopes. Both independently research the same grant programs, and token usage nearly doubles with no added coverage. What is the most effective fix?
39. [D2] The report-generation subagent has two formatting tools, `render_as_table` and `render_as_narrative`. On some requests it instead writes a plain-text paragraph describing how it would format the data, without calling either tool. What is the most effective fix?
40. [D1] Investigating packaging-waste compliance costs across several regions, the coordinator's adaptive plan discovers mid-investigation that one region's cost data sits behind a specialized industry-report subscription no assigned source provides. The coordinator revises the remaining subtasks to substitute an accessible regulatory-filing source for that region instead. Which decomposition pattern does this exemplify, and why does it suit this task?
41. [D2] Policy requires that any single citation-purge action affecting more than 25 sources at once route to human sign-off before it runs. Today this rule exists only as a system-prompt instruction. During a high-volume cleanup pass, a purge affecting 60 sources executed without sign-off. What change most reliably closes this gap?
42. [D5] To speed up report assembly, the report-generation subagent stops carrying a source mapping for each individual claim through the pipeline, instead appending one consolidated bibliography section listing every source used somewhere in the document. Reviewers can no longer trace any specific claim back to the source that supports it. What is the most effective fix?
43. [D1] Frustrated by the round-trip cost of the coordinator's refinement loop, an engineer grants the synthesis subagent its own web-search tool so it can independently fill small gaps it notices while drafting, without reporting back to the coordinator first. What is the most effective response to this change?
44. [D3] The research team runs two workloads through Claude: a live fact-check a researcher waits on mid-call, and a nightly regeneration of source-credibility summaries for that day's newly ingested documents, with no one waiting on the output. Which API approach fits each, and why?
45. [D1] Two of five assigned source categories time out entirely; the other three return complete, usable findings. Rather than pass anything forward, the synthesis subagent halts and reports a failure, reasoning the input set is too incomplete to work from. What should the design require instead?
46. [D4] The pipeline extracts equipment-inspection reports into a fixed schema. Source reports write dates as "3/14," "14 March," and "2024-03-14," and technician hours as "3.5 hrs," "3h30m," and "210 min." The schema defines `inspection_date` as ISO-8601 and `labor_hours` as a decimal. Where should normalization guidance for these varied source formats live?
47. [D4] A new extraction field asks the model to copy `defect_severity` directly from the report's explicit "Severity:" label into the output — no computation, comparison, or multi-step inference required. An engineer proposes adding "think step by step before extracting this field" to improve accuracy. What is the most effective response?
48. [D4] A pipeline's retry step resubmits a failed document within the same conversation, needing the model to call `resubmit_correction`. The conversation's tool list still includes the original `extract_fields` tool. With `tool_choice` left at `{"type": "any"}`, logs show the model sometimes re-calls `extract_fields` instead of submitting the correction. What configuration most reliably fixes this?
49. [D2] A `run_document_ocr` tool sometimes fails to produce usable text — for example, on a low-quality scan — and currently returns only `{"isError": true}`. The pipeline's retry-with-feedback step is supposed to resubmit with a corrective instruction, but has nothing specific to change, so it resends the identical request and gets the identical failure. What should the tool's error response include instead?
50. [D4] Since the parts-replacement pipeline moved to `tool_use` with a strict schema, every response parses cleanly and every field passes its type check. Auditors still occasionally find records where `part_number` holds a value that matches the expected format but was actually copied from an adjacent line item, not the part the record describes. What is the most accurate way to interpret this?
51. [D4] An inspection record's schema requires `inspection_date` and `next_due_date`, both valid ISO-8601 strings — the schema itself has no way to express that `next_due_date` must fall after `inspection_date`. A recent batch shipped several records where the two dates were reversed, undetected until a downstream audit caught them. What should the team add?
52. [D4] The retry-with-feedback loop for defect-code extraction resubmits each failure with the specific validation error, and most retries eventually succeed. The team wants to know, across thousands of retries, which recurring source-document construct — an abbreviation, a merged table cell, a handwritten annotation — drives most first-pass failures, so they can fix the prompt or schema at the source. What should they add?
53. [D4] A parts-replacement record states `total_parts_cost: $340.00`, but a later billing audit finds the four listed part prices actually sum to $310.00 — a $30 discrepancy nobody caught at extraction time. What design change most directly catches this class of error at the moment of extraction, rather than in a later audit?
54. [D1] A batch of three unrelated inspection reports arrives needing extraction, and none depends on another's results. The coordinator currently issues one `Task` call for the first report, waits for its result, then issues the next `Task` call for the second report in a following response, and so on. What most effectively reduces this latency?
55. [D4] A nightly batch of 200 inspection-report extractions runs through the Message Batches API. Results return the next morning: 188 succeed, and 12 fail because those particular scans were long enough to exceed a per-request limit. The team needs to fix and reprocess only the 12 failures. What is the most effective way to proceed?
56. [D3] A nightly `claude -p` step summarizes each night's extraction batch into a compliance ledger, needing exactly three fields every run: `batch_id`, `records_processed`, `flagged_for_review`. On batches with zero flagged records, the step sometimes replies with a sentence like "No records required review" instead of the record, and the ledger parser throws. What is the most reliable fix?
57. [D4] The review step for extracted inspection records is instructed only to "flag anything that looks unusual." On a 300-record sample, it flags a technician working a rare but legitimate double-shift and misses a genuinely fabricated-looking part number in a different record. Reviewers say the flagging feels arbitrary. What change would most reliably fix this?
58. [D5] A single extraction call processes one lengthy compiled inspection binder — several individual site reports concatenated into one long document. The pipeline reliably captures the binder's cover-sheet summary and its final sign-off section, but a defect noted only in a site report buried in the binder's middle is consistently missed. What is the most effective fix?
59. [D5] The pipeline's `run_document_ocr` tool returns 50+ fields per page — bounding boxes, per-character confidence, font metadata — when only the plain text and an overall page-confidence score matter downstream. On multi-page inspection binders, this bulk accumulates in context, and extraction quality on later pages starts to drift. What is the most effective fix?
60. [D4] A request for the pipeline reads only "just pull the important stuff out of these inspection files," with no target schema or field list specified. Rather than asking which fields count as "important" before doing anything, what should the pipeline do?

#### Domain Breakdown
| Domain | Total Q | Correct | % | Confirmed weak? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 15 | 93.8% | no |
| D2 Tool Design & MCP | 11 | 9 | 81.8% | no (single-exam signal — see note) |
| D3 Claude Code Config | 12 | 10 | 83.3% | no |
| D4 Prompt Engineering | 12 | 11 | 91.7% | no |
| D5 Context Management | 9 | 9 | 100% | no |

#### Scenario Block Breakdown
| Block | Questions | Correct | % |
|---|---|---|---|
| Customer Support Resolution Agent | 15 | 13 | 86.7% |
| Code Generation with Claude Code | 15 | 13 | 86.7% |
| Multi-Agent Research System | 15 | 14 | 93.3% |
| Structured Data Extraction | 15 | 14 | 93.3% |

#### Observations

- **The third re-test of Exam 7/8's flagged sections returned a split verdict — two closed, one now confirmed stubborn.** D3 §3.1 (Q16, `/memory` diagnostic vs. re-typing the instruction) and D3 §3.6 (Q23, plan mode vs. direct execution on a fully-scoped change) both **recovered to correct** after missing twice each — the gap the Exam 8 Professor's Note asked this exam to decide is now resolved for both. **D4 §4.6 (Q48, forcing a specific tool via `tool_choice` vs. `"any"`) missed a THIRD consecutive time** (Exam 7, Exam 8, Exam 10) — per the Exam 8 note's own stated criterion, three straight misses across three different concrete situations is no longer "attempt-specific noise," it is a genuinely stubborn misconception. Recommend Ram read `Domain-4_v2.md` §4.6 directly before the next attempt rather than relying on further exam exposure alone.
- **D3 §3.11 (Q27, CLAUDE.md-vs-Skills half-split trap) missed for the SECOND time** (first missed fresh in Exam 8, now missed again on its first formal re-test) — this is a real, still-open section-level gap distinct from the now-closed §3.1/§3.6 pair, and becomes D3's priority item for Exam 11.
- **D3 and D4 both recovered domain-wide**, breaking their two-exam co-decline: D3 75.0% → 83.3%, D4 75.0% → 91.7% (D4's best score in this project's history). Combined with the §3.1/§3.6 recoveries, this reads as real, broad improvement, not just the two targeted sections clearing.
- **D2 is this paper's sole weakest domain (81.8%, 9/11)** — a new signal, since Exam 8's weakest was the D3/D4 tie, not D2 (which sat at 90.9% then). Two D2 misses: Q4 (§2.3, business-error vs. protocol-error semantics — treating a valid policy denial as a tool failure) and Q6 (§2.8, prompt-bundling vs. a combined tool — recommending the *simpler* bundling fix over building a new composite tool). Not yet confirmed weak (different domain than Exam 8's weakest, so the two-consecutive-exam bar isn't met), but see Insights Round 2 below for a 3-exam trend that makes this more than a one-off.
- **The remaining miss:** Q35 (D1 §1.5) — told a synthesis subagent to "use the findings from the filing-review step" without including those findings in the prompt; subagents have isolated context and cannot see prior findings by reference alone. A fresh, first-time miss for this specific facet of §1.5.
- **All 10 Key-Distinction-seeded questions were answered correctly** (KD#8, #9, #10, #11, #12, #14, #19, #20, #23, #29) — none of the 6 misses fell on a KD-seeded question. KD#23 (behavioral drift, periodic-confirmation target) cleared its second consecutive correct appearance.
- **Timing:** clean and fast — 2,357s total, 39.3s/question average, no break-confounding outliers (slowest: Q27 at 114s — notably one of the two D3 misses, considered rather than rushed; next-slowest 94s, 82s, 74s, 69s, all consistent with genuine think-time on harder questions).

### Questions Used
Already logged under the Exam 10 generation entry above — no new stems from scoring.

---

### Professor's Note — Intent for Exam 11

Written after Exam 10 (2026-07-29). Based on results-json (with a template-bug caveat on the `exam_n` field — see the note under Exam 10's header; the result is unambiguously Exam 10's, confirmed via block-scenario matching).

- **Misconceptions revealed:**
  1. **D4 §4.6 is now a confirmed-stubborn trap, three exams running (Exam 7, 8, 10), each a genuinely different concrete situation.** This has moved past "needs more exam exposure" — recommend Ram directly re-read `Domain-4_v2.md` §4.6 before the next attempt, in addition to a fourth exam re-test.
  2. **D3 §3.11 (CLAUDE.md-vs-Skills half-split) is now 2-for-2 missed** (Exam 8 fresh miss, Exam 10 re-test miss) — a real, unresolved section-level gap that inherits D3's priority-item slot now that §3.1/§3.6 have cleared.
  3. **D2 shows a 3-exam declining domain trend** (100% Exam 7 → 90.9% Exam 8 → 81.8% Exam 10) and a repeated miss on §2.8 (tool-bundling vs. prompt-bundling, missed in both Exam 8 and Exam 10) — not yet mechanically confirmed (different domain than Exam 8's weakest), but a real pattern per Insights Round 2 below.
- **Positive signal worth naming explicitly:** D3 §3.1 and §3.6 both recovered after two straight misses each — a genuinely closed chapter, not just a lucky attempt (both questions were answered promptly, not guessed under time pressure). D3 and D4 both climbed to their strongest-ever levels this paper (83.3% and 91.7%).
- **Weakest this paper:** D2, alone, at 81.8% — a new signal (Exam 8's weakest was the D3/D4 tie). **Not mechanically confirmed** — the two-consecutive-exam rule needs D2 to also be sole-weakest in Exam 11 to fire the +4/−2/−2 adjustment.
- **Intent for next paper (Exam 11):** keep the base FULL-60 quota (no confirmed-weakness adjustment — D2's decline is real but only a single exam as sole-weakest so far). Within it, bias section selection toward: (a) a fourth re-test of D4 §4.6, explicitly flagged to Ram as possibly warranting direct corpus review rather than pure exam exposure if it misses again; (b) a second formal re-test of D3 §3.11 (now 2-for-2 missed); (c) broader D2 coverage biased toward §2.3 and §2.8 (this exam's two D2 misses, §2.8 now a repeat) plus D2 sections not recently tested, since the 3-exam decline suggests a breadth gap forming, similar to how D3/D4's gap first surfaced.
- **Watch next:** does D4 §4.6 finally land on a fourth attempt, or does the stubborn-trap read solidify further? Does D2 confirm as weakest for a second consecutive exam (triggering the mechanical adjustment for the first time this project has seen it apply to D2 alone), or does the decline reverse the way D3/D4 just did? Does D3 §3.11 clear on its second formal re-test the way §3.1/§3.6 just did?

---

## Insights Round 2 — 2026-07-29
*(Triggered automatically: exams_scored reached 6, a non-zero multiple of 3, after this session's Exam 10 scoring — the second Insights Round in this project's history.)*

**Exams covered:** the 3 most recent SCORED exams — Exam 7 (2026-07-16), Exam 8 (2026-07-28), Exam 10 (2026-07-29). Exam 9 (generated 2026-07-19) remains unscored and is excluded from this window; the round is defined by scoring recency, not exam number.

### Domain Trend
| Domain | Exam 7 | Exam 8 | Exam 10 | Trend |
|---|---|---|---|---|
| D1 Agentic Architecture | 93.8% | 93.8% | 93.8% | Rock-solid — identical (15/16) three exams running, the most stable domain in the project. |
| D2 Tool Design & MCP | 100% | 90.9% | 81.8% | **Clear 3-exam decline** (100% → 90.9% → 81.8%), now this paper's sole weakest domain for the first time. Not yet mechanically confirmed (different domain than Exam 8's weakest), but the smoothest, most consistent downward trend this Insights Round found. |
| D3 Claude Code Config | 83.3% | 75.0% | 83.3% | V-shaped: dipped then fully recovered to its Exam 7 level — the §3.1/§3.6 recoveries are the direct cause. |
| D4 Prompt Engineering | 83.3% | 75.0% | 91.7% | V-shaped and then some: dipped, then climbed past its Exam 7 level to this domain's best score in the project's history. |
| D5 Context Management | 100% | 100% | 100% | Perfect three exams running — the strongest, most durable signal in the project. |

### Pace Trend
| Exam | Total time | Avg s/question | Note |
|---|---|---|---|
| Exam 7 | 19,489s | 324.8s (99.0s excl. 3 outliers) | Break-confounded — three extreme outliers (Q41, Q11, Q39) dominate total elapsed time. |
| Exam 8 | 2,121s | 35.4s | Clean — no break-confounding, the fastest exam in the project to that point. |
| Exam 10 | 2,357s | 39.3s | Clean — no break-confounding outliers; slowest question (Q27, 114s) was a considered miss, not a rushed one. |

Two of the three exams in this round (8, 10) are clean, fast, unconfounded pacing data — a real improvement in attempt hygiene over Round 1, where only one of three exams was clean. Both clean exams sit in the same 35-40s/question band, suggesting this is now the learner's genuine steady-state pace, not noise.

### Repeated Missed Traps (sections/Key Distinctions missed in 2+ of these 3 exams)
- **D4 §4.6 (`tool_choice` forcing a specific tool vs. `"any"`)** — missed in **all three** exams (Exam 7 Q51, Exam 8 Q17, Exam 10 Q48). The only trap in this project's history to miss three consecutive scored exams on three genuinely distinct concrete situations. No longer read as attempt-specific noise — see this round's Focus Recommendation.
- **D3 §3.1 (`/memory` diagnostic vs. re-typing) and §3.6 (plan mode vs. direct execution)** — each missed in Exam 7 and Exam 8, then **both recovered to correct in Exam 10**. Included here as a closed-loop success story: this Insights Round's window is exactly what confirms the recovery is real (two consecutive correct data points would need Exam 11 to fully close the loop, but a clean recovery after two straight misses is a strong signal on its own).
- **D2 §2.8 (composite tool vs. prompt-bundling)** — missed in Exam 8 (Q11) and Exam 10 (Q6), not tested in Exam 7. A new repeat this round surfaced that neither exam's own Professor's Note flagged in isolation (Exam 8's note was focused on D3/D4; Exam 10's note above catches it) — exactly the kind of cross-exam pattern a 3-exam window is meant to catch and a single-exam note can miss.

### Focus Recommendation
**Primary: D4 §4.6.** Three consecutive misses across three different concrete situations (a Claude Code CI structured-output-guarantee framing, a review-bot precondition-gating framing, and a retry-with-stale-tool-list framing) is this project's first genuinely stubborn single-section trap. Recommend Ram directly re-read `Domain-4_v2.md` §4.6 (`tool_choice` forcing a specific tool vs. `"any"`) before Exam 11, rather than relying on a fourth exam attempt alone to close it.
**Secondary: D2, as a domain.** The 3-exam decline (100% → 90.9% → 81.8%) plus the §2.8 repeat suggest a forming breadth gap similar to D3/D4's pattern before it became visible — worth biasing Exam 11's D2 section selection broadly, not just at §2.3/§2.8, to test whether this is domain-wide (as D3/D4's gap turned out to be) or concentrated in a couple of sections.
**Tertiary, informational only:** D1 and D5 need no attention — three exams of rock-solid and perfect performance respectively, the most reliable signal in the project.

---

## Exam 11 — Generated 2026-07-29

**File:** `mock-exams/CCA-Prep_MockTest-11_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Customer Support Resolution Agent; Developer Productivity with Claude; Claude Code for Continuous Integration; Structured Data Extraction
**Attempt date:** 2026-08-10
**Score source:** results-json
**Total score:** 55 / 60 correct (estimated scaled: 925 / 1000; pass line 720)

**Note on scoring order:** Exam 11 was generated 2026-07-29 and attempted today, 2026-08-10 — after Exam 9 (generated 2026-07-19) was scored on 2026-08-09. Per orchestration-prompt v10 Phase 2e, the confirmed-weakness comparison is against "the most recent PRIOR SCORED entry" by attempt chronology, which is **Exam 9** (weakest: D2, confirmed), not Exam 10.

**Generated consuming both the Professor's Note — Intent for Exam 11 and Insights Round 2** (both written after Exam 10 scored 54/60, 910/1000, 2026-07-29). Base FULL-60 distribution kept unchanged (D1 16 / D2 11 / D3 12 / D4 12 / D5 9) — D2's 3-exam decline is real but was only a single exam as sole-weakest, not yet meeting the two-consecutive-exam confirmed-weakness bar. Section bias: (a) D4 §4.6 re-tested a **fourth** consecutive time (missed Exam 7/8/10) via a genuinely new mechanism — a scenario where `"any"` is actually correct (a per-language test-writing tool roster where the template type isn't knowable ahead of time), testing whether the learner over-generalized "always force specific" from the last two misses rather than repeating outcome-branching, precondition-gating, or stale-tool-list framings; (b) D3 §3.11 re-tested a **second** formal time via a category-mismatch facet (path-scoped content wrongly bundled into a Skill), distinct from both priors' half-split framing; (c) D3 §3.1/§3.6 touched only for routine periodic confirmation (both recovered in Exam 10, no urgency); (d) D2 given its fullest-ever breadth — all 9 sections covered, spread across two independently-authored blocks (Customer Support 5, Developer Productivity 6) rather than concentrated in one.

**Scenario draw — the first with no rotation tiebreaker.** All six scenarios were tied at count 6 after Exam 10. Code Generation with Claude Code and Multi-Agent Research System were deliberately rested — both had been drawn in BOTH Exam 9 and Exam 10, a two-exam-running streak carrying this pool's highest convergence risk. The four drawn instead (Customer Support, Developer Productivity, Claude Code CI, Structured Data Extraction) give every domain exactly two primary-carrying blocks (D1: CS+DP · D2: CS+DP · D3: DP+CCCI · D4: CCCI+SDE · D5: CS+SDE) — the most structurally balanced draw this project has produced, directly serving both this exam's real priorities (D2 breadth, D4/§4.6 no longer concentrated in a single block). Post-Exam-11 spread: Customer Support 7, Developer Productivity 7, Claude Code CI 7, Structured Data Extraction 7, Code Generation 6, Multi-Agent Research 6.

**Parallel dispatch — back to the standard pattern.** No usage-limit risk was flagged this session, so the four scenario blocks were authored in parallel (4.b.6/4.b.7), not the serial fallback Exam 10 used. All four returned complete, valid blocks on the first attempt.

Block×domain allocation (primary domains bold): Customer Support — **D1 6, D2 5, D5 3**, D3 1; Developer Productivity — **D1 6, D2 6, D3 3**; Claude Code CI — **D3 6, D4 6**, D1 1, D5 2; Structured Data Extraction — **D4 6, D5 4**, D1 3, D3 2. All four blocks pass the primary-vs-non-primary domain-tally check, verified programmatically.

**A real content collision was found and fixed — the first time the manual cross-block content read caught something the automated citation tally and Jaccard scan both missed on the very first post-assembly pass, before any HTML shipped.** D2's 11 questions over 9 sections forced two repeats. Both original drafts — independently written by two different blocks — reskinned the *identical* underlying lesson with different tool names: §2.3's business-rule-denial facet was tested twice (a warranty-claim denial and a deploy-freeze-exception denial, same lesson), and §2.8 — whose actual corpus content is ~4 lines with exactly one teachable point (prefer prompt-bundling over a composite tool) — has no second facet available at all, so its two instances were unavoidably the same lesson twice. Neither the citation tally nor a 0.30-threshold Jaccard scan flagged either pair; both passed clean. Caught only by reading all four flagged questions' full text side by side. **Fixed directly by the coordinating session:** one §2.3 question was rewritten onto the corpus's distinct "valid empty results vs. access failure" facet; the §2.8 repeat was reassigned entirely to §2.6 (MCP primitive taxonomy), since §2.8 offered no second facet to rewrite onto. The exam's D2 repeat pair is therefore {§2.3, §2.6}, not the originally-planned {§2.3, §2.8} — a valid substitution, since the actual requirement is two genuinely distinct facets among D2's repeats, not any specific two sections. One further transcription slip (a letter-tally mismatch introduced while hand-fixing the §2.6 question) was caught by re-running the gate script and corrected before shipping.

All six Phase 4.e.6 Fidelity Verification Gate checks passed on the shipped file, computed programmatically and re-verified after the collision fix: 0 invented names exam-wide; correct-answer letters exact 15/15/15/15 (each block within 1 of the balanced split — Customer Support A4/B4/C4/D3, Developer Productivity A4/B4/C3/D4, Claude Code CI A4/B3/C4/D4, Structured Data Extraction A3/B4/C4/D4); stem word count min 43/median 54/max 67 (options min 8/max 33, both inside their hard caps); every block's domain tally passes primary-vs-non-primary and the exam-wide quota matches target exactly; inline code/config token rate 23.3% (56/240), inside the 20–25% band; scenario-rotation disclosure present on the landing card. Supplementary: a full-exam Jaccard near-duplicate scan found **zero pairs above a 0.30 threshold** across all 60 stems, both before and after the collision fix (as expected — the collision was a same-lesson-different-vocabulary case, not a lexical near-duplicate, exactly the failure mode this project's history says only a manual read catches).

**Key Distinction budget:** 8 of 60 questions carry a KD citation — KD#4 (Q22), KD#12 (Q4), KD#15 (Q33), KD#19 (Q59), KD#20 (Q49), KD#21 (Q13), KD#25 (Q44), KD#27 (Q17) — above the Session 13 tightening target of 4-6 (each of the four independently-dispatched blocks stayed within its own 1-2 instruction, but 4 blocks × 2 summed above the intended exam-wide ceiling). Still comfortably within the hard 15-question cap; every seed is a genuine natural fit, none forced.

### Questions Used (deduplication — do not reuse these stems in Exam 12+)

1. [D1] Your support agent's response sometimes pairs a short acknowledgment — 'Let me check that order for you' — with a `tool_use` block for `lookup_order`. The harness currently checks whether the response contains any text at all; whenever it does, it treats the turn as finished and returns that text to the customer without executing the tool. What should the harness check instead?
2. [D2] In one turn, your agent's response contains three `tool_use` blocks — `get_customer`, `lookup_order`, and `check_warranty_status` — all needed before Claude can continue. The harness executes and appends `tool_result` blocks for the first two, then calls Claude again, planning to supply the third result on a later turn. What is wrong with this approach?
3. [D2] Your `file_warranty_claim` tool returns a bare `isError: true` whenever a claim is denied because the product is past its warranty window — a written, final policy outcome. The agent treats every denial as an outage: it apologizes for a technical problem and retries, and the ops dashboard now counts these denials as tool failures. How should the tool represent this outcome?
4. [D2] Your `reverse_loyalty_redemption` tool permanently claws back redeemed loyalty points and cannot be undone once it runs. Policy requires the agent to show impact details and get explicit confirmation before every reversal. The team is choosing between four designs to guarantee this ordering. Which design makes skipping the preview architecturally impossible, not just discouraged?
5. [D1] Your returns-investigation coordinator's prompt is a numbered script: check `lookup_order`, then `check_return_eligibility`, then if eligible call `process_refund`, then done. On a case involving a partial shipment where only some items arrived damaged, the coordinator follows all four steps correctly but never investigates the missing items separately. Which change to the coordinator's prompt is most effective?
6. [D3] Your team ships an `/escalate-case` command so any engineer can type `/escalate-case billing-dispute` to open a pre-formatted escalation with the reason code attached. It must be available to everyone the moment they clone the repository, and the typed reason code must land inside the command's generated note. Where should the command live, and how does it read the typed text?
7. [D1] Your delivery-status subagent's carrier-tracking lookup times out. Instead of reporting the timeout, it silently falls back to a cached status from two days earlier and reports success with no indication the data may be stale. The coordinator presents this to the customer as current. What is the most effective fix?
8. [D2] Your team is adding case-escalation ticketing to the support agent's MCP tooling. A well-maintained community MCP server already integrates with your ticketing platform's standard API. An engineer proposes building a custom in-house server instead, arguing it gives the team full control over field mapping. What is the most effective approach?
9. [D2] Telemetry shows your agent calls `get_customer`, waits a full turn, then calls `fetch_loyalty_tier` with the same customer ID on nearly every loyalty-related case — two round-trips where one would do. An engineer has sketched a combined `get_customer_with_loyalty_tier` tool and asks you to review the design. What should you recommend?
10. [D1] A customer disputes a $14,000 wire-transfer-linked charge, claiming it was unauthorized. `get_customer` and `lookup_order` both return clean results, but nothing in the transaction history clearly confirms or refutes the claim, and a wrong call either way carries real financial and legal exposure. What should the agent do?
11. [D1] After an expensive investigation into a customer's disputed multi-order billing history, the team wants to evaluate two candidate resolutions — a partial refund versus a full account credit — starting from that same completed investigation, without either evaluation's reasoning influencing the other. What is the most effective way to continue?
12. [D1] Before an escalation summary reaches a human agent, your team routes it through a second Claude Code instance that has no access to the first, drafting instance's reasoning trace, and asks it to independently flag any missing context or unsupported claims before the handoff goes out. Which named architecture pattern does this design exemplify?
13. [D5] Your support agent already extracts precise transactional facts — order ID, agreed credit amount, promised delivery date — into a persistent case-facts block included in every prompt, outside the summarized conversation history. An engineer proposes replacing it with a vector-database retrieval system 'to make fact recall more robust.' How should the team evaluate this proposal?
14. [D5] A customer calls in and gives only a phone number to identify themselves. The `get_customer` tool returns three separate accounts sharing that number, since the number is registered to a shared family plan. The agent must proceed on the correct one before discussing any order or billing detail. What should it do?
15. [D5] Your agent auto-closes cases whenever its per-field confidence on the resolution details is high, and human reviewers only ever look at the low-confidence cases flagged for review. Months later, a reviewer stumbles onto a systematic error affecting a class of auto-closed cases that had never been sampled. What should the oversight design add?
16. [D1] A platform team's onboarding agent runs a code-review subagent and a test-generation subagent under one coordinator. To save a round trip, an engineer proposes letting the two subagents message each other directly with extra test scenarios, skipping the coordinator. What is the strongest reason to keep this routed through the coordinator?
17. [D2] After a schema change, an automation must regenerate a config file where nearly every line differs from the previous version. The current script issues a separate targeted-replacement call per changed line, and several calls fail because the old text no longer appears verbatim. Which approach is most appropriate?
18. [D3] A monorepo's infra/terraform/ directory requires every modified file to carry a change-justification comment — a rule that applies nowhere else in the repository, regardless of which service's code sits alongside it. Where should this rule live so it loads automatically only when Terraform files are touched, without bloating every other session?
19. [D2] The `resolve_module_owner` tool description reads only: 'Returns the current owner of a module.' It works only for actively maintained modules — for archived ones it returns stale data with no warning, and engineers now cite that output as authoritative. What is the most effective fix?
20. [D1] The automation's `generate_release_notes` tool must run only after `tag_release` finishes, since notes reference the new tag. This ordering exists only as a step in the system prompt. When a slow CI run delayed `tag_release`, the agent invoked `generate_release_notes` first, producing notes citing a tag that didn't exist yet. What change most reliably prevents this?
21. [D2] The `check_deprecated_packages` audit tool returns an empty result list both when a repository genuinely has zero deprecated packages, and when its backend vulnerability index is unreachable — the same signal either way. Engineers now can't tell a clean audit from one that silently didn't run. What should the tool's response distinguish?
22. [D3] An engineer assumes the shared `.claude/skills/commit/SKILL.md` always wins over any personal skill with the same name, reasoning project config should win since it's what the team agreed on. After the team updates the shared skill's checks, the engineer's `/commit` behavior doesn't change at all. What is going on?
23. [D1] A mapping subagent and a dependency-audit subagent independently report the same module's line count — 2,340 and 2,510 — because they ran against different commits. Both numbers reach the report-writing subagent as plain sentences, with no timestamp or commit reference attached, and it silently keeps the audit subagent's figure. What should change?
24. [D2] Three internal MCP tools return timestamps in different formats: Unix epoch from one, ISO 8601 from another, a locale-formatted string from a third. None of these tools are ones the team controls. Downstream reporting has started mis-ordering build history because of the mismatch. What is the most effective fix?
25. [D1] A dependency-scanning subagent audits every service's lockfile for outdated packages. One lockfile fails to parse after a tooling upgrade changed its schema, so the subagent silently substitutes last week's cached scan for that service instead of failing. The report lists every service's findings with identical confidence, stale data included. What should the output do instead?
26. [D3] An engineer unfamiliar with the team's job queue asks Claude Code to add deduplication so a job never runs twice concurrently. The first version misses cross-instance duplication, the second misses a dedup key that changes mid-retry, the third leaves stale locks after a crash — a different gap each time. What is the most effective next step?
27. [D2] The build-automation subagent has accumulated 18 tools across three MCP servers plus all six built-ins, added as new needs arose. It frequently calls the wrong one among near-duplicate options, even after every description was rewritten to be clearer. What is the most effective next step?
28. [D1] The boilerplate-generation subagent scaffolds new module files from a template — nothing else. Its AgentDefinition includes shell access, added at design time on the reasoning that scaffolding might someday need a shell command. It has since started running git history-rewriting commands on branches other subagents are also working on. What is the most effective fix?
29. [D2] Designing the build-automation agent's MCP server, the team must expose three things: `trigger_rebuild` and `invalidate_cache`, actions the agent performs; a build-configuration reference the agent should only ever read, never edit; and a reusable postmortem template the agent fills in after a failed build. Which MCP primitive should carry each?
30. [D1] Code generation and code review run as two separate Claude Code sessions with no shared conversation history — independent on paper. Both, however, were configured with the same few-shot example set, which happens to omit a common null-input edge case. The reviewer approves a generated function that mishandles exactly that case. What is the most effective fix?
31. [D1] Your CI coordinator runs three independent analysis subagents on every PR — correctness, style, and dependency-risk — each spawned via a separate `Task` call. Today the coordinator emits one `Task` call, waits for its subagent to finish, then emits the next `Task` call in a following response, tripling wall-clock time versus running all three together. What is the most effective fix?
32. [D3] After an incident where a `/apply-autofix` skill's Bash access let it run an unintended shell script mid-fix, the team is scoping a new `/format-pr` skill that should only ever read and edit files during PR formatting cleanup — never execute shell commands. Which SKILL.md frontmatter change most directly enforces this?
33. [D3] A new CI step must run Claude Code fully unattended to review each pull request; no one is available to answer interactive prompts. An engineer, unfamiliar with the CLI, sets `CLAUDE_HEADLESS=true` in the pipeline's environment config, expecting it to suppress interactive prompts. The step still hangs waiting for input on every run. What actually fixes this?
34. [D3] Your CI pipeline's merge gate calls `claude -p` and needs a single verdict object — a `pass_fail` flag plus a list of blocking file paths — to decide whether the queue unblocks a PR. Prose responses vary in wording enough that the gate script's parser fails on roughly one run in twenty. Which configuration most reliably guarantees parseable output?
35. [D3] Finance asks your team to move the CI pipeline's pre-merge review — the check a PR cannot merge without, while the author waits on the result — onto the Message Batches API to capture its 50% cost discount. What should the team do?
36. [D3] Your CI pipeline's CLAUDE.md holds three kinds of guidance: formatting conventions every review must follow, a security-review checklist invoked only during periodic audits, and a stricter validation rule that should apply automatically whenever Claude Code touches files under `payments/`. An engineer proposes bundling the checklist and the payments rule into one new Skill, leaving only formatting in CLAUDE.md. How should the team evaluate this?
37. [D3] A named Claude Code session spent a full day mapping how the CI pipeline's retry-and-backoff logic works, ahead of a planned refactor. Before the team picks the work back up, an unrelated migration this week rewrote that retry logic entirely. What is the most effective way to continue?
38. [D4] Your CI pipeline's test-generation step defines a separate test-writing tool per language — `write_python_test`, `write_js_test`, `write_go_test` — each shaped to that framework's assertion style. A PR's diff includes template files whose eventual language isn't determined by file extension alone, and the step must still emit one schema-valid test definition per changed file, never a prose explanation. Which `tool_choice` configuration is most effective?
39. [D4] The team adds few-shot examples teaching the review bot which findings should block a merge outright versus post as a non-blocking comment. The first draft has fifteen examples: ten obvious blocking cases (a hardcoded credential) and five obvious non-blocking ones (a naming nit). The bot still guesses inconsistently on genuinely borderline cases — a caught-but-unhandled edge case, a deprecated-but-functional call. What is the most effective revision?
40. [D4] An engineer wants the review bot to respond in a fixed JSON-only format, with no prose preamble, for the life of the CI run. They set an environment variable, RESPONSE_FORMAT=json, in the pipeline's runner config, expecting the harness to relay it to Claude before each call. Responses keep mixing in prose anyway. Where should this constraint actually be defined?
41. [D4] Mid-run, a critical CVE advisory is published for a dependency the pipeline is currently reviewing a PR against. The team wants the review bot's very next response, still in the same run, to factor in this new advisory without waiting for the pipeline's next full invocation. What is the most effective way to inject this?
42. [D4] The nightly dependency-audit job reviews 30 independent package manifests across the org's services in a single pass. Comments are detailed for the first several manifests, then shrink to one-line 'no issues' notes for the rest — including one manifest with a real license-incompatible dependency the pass missed entirely. What should the team do?
43. [D4] The team routes the independent second-instance reviewer's findings automatically: any finding it flags immediately blocks the PR. Some flagged issues are genuinely uncertain edge cases a human would want to weigh in on, while others are clear-cut. What change lets downstream routing distinguish these without adding a third review pass?
44. [D5] Each commit on an open PR triggers a fresh `claude -p` invocation to re-review the changed files. A developer replies inline on one finding, 'intentional, ignore this,' then pushes a follow-up commit. The next invocation re-flags the identical finding, with no memory of the developer's reply. An engineer proposes adding a `session_id` so the CLI can look up the earlier exchange itself. Is this the correct diagnosis?
45. [D5] Over the past year, hundreds of independent CI review sessions have each analyzed a different PR in isolation, with no shared memory between runs. A security lead wants to know whether a specific unsafe-deserialization pattern has ever been flagged before, across any of that history, without manually rereading hundreds of separate review outputs. Which approach most effectively supports this kind of recall?
46. [D4] A recruiting pipeline extracts structured candidate records from resumes and application forms. The schema marks `current_employer` required and non-nullable, reasoning every applicant needs one listed. An audit of 6,000 records finds 14% carry a plausible employer name tracing to no real company — those applicants are recent graduates or first-time job seekers with no prior employer. What schema change most directly stops this?
47. [D1] The recruiting pipeline's coordinator has `parsing_agent`, `validation_agent`, and `enrichment_agent` subagent types fully described in its system prompt, each with a clearly scoped role. Engineers notice it never delegates any of the three — it attempts every applicant's full parse-validate-enrich cycle itself in one long response. Its `AgentDefinition` lists only `read_document` among `allowed_tools`. What most reliably fixes this?
48. [D4] Since the pipeline moved to `tool_use` with a strict JSON schema, every extracted record parses cleanly and every field passes its type check. Auditors still occasionally find `years_of_experience` holding a plausible integer that turns out to be the applicant's age, copied from a birthdate line elsewhere in the resume rather than computed from listed job history. What is the most accurate way to interpret this?
49. [D5] A weekly candidate-shortlist digest concatenates all 40 candidates' extracted profiles into one long prompt so a synthesis pass can highlight standout qualifications. It reliably surfaces details for the first and last several candidates, but consistently omits a rare, relevant certification held by a candidate in the middle — even though that candidate's own record correctly includes it. What is the most effective fix?
50. [D3] The pipeline's project-root CLAUDE.md defines formatting and normalization conventions every extraction session must follow. A subdirectory-level CLAUDE.md inside the validation module adds stricter numeric-precision rules specific to that module. An engineer assumes the subdirectory file replaces the root file's guidance whenever Claude works inside `validation/`. Is this assumption correct?
51. [D3] The team wants a dedup-and-merge step for duplicate resume submissions. Several valid architectural approaches exist — deduplicating at ingestion, at validation, or as a separate reconciliation pass — and the right fit depends on tradeoffs the team hasn't worked through. An engineer wants to start implementing the ingestion-time approach immediately. What is the most effective approach?
52. [D1] Asked to extract 'every credential the candidate holds,' the coordinator decomposes the task into subtasks covering only formal degrees. The parsing, validation, and enrichment subagents all complete their assigned subtasks correctly. The final candidate record never mentions the professional certifications, licenses, or continuing-education units documented elsewhere in the same application packet. What is the most likely root cause?
53. [D4] The pipeline's extraction tool already enforces its JSON schema via `tool_use` — every response is schema-valid. An engineer argues that validating the extracted record again in application code, using a separate Pydantic model, is redundant now that the schema is enforced at generation time. Is this reasoning correct?
54. [D4] Across thousands of retry-with-feedback cycles in the extraction pipeline, the team wants to know which recurring source-document construct — a multi-column resume layout, a non-standard date abbreviation, a scanned image-only PDF — drives most first-pass validation failures, so they can fix the prompt or schema at the source instead of just retrying. What should they add?
55. [D5] A recruiter's working session correcting a batch of parsed candidate records reaches 65,000 tokens. It holds a counter-offer salary figure stated verbally, a start date reached after negotiation, tangents comparing compensation benchmarks across unrelated roles, and the last few exchanges finalizing the shortlist. Which strategy cuts tokens while keeping the session useful?
56. [D1] The enrichment pass has surfaced a licensing-verification gap on 12 candidate records — the source documents that would resolve it are available and simply weren't queried during the first extraction pass. An engineer suggests shipping the batch now with a 'verification pending' note on those records instead of re-running extraction against the available source. What should the coordinator do instead?
57. [D4] A new schema field, `duplicate_certification_flags`, requires comparing each listed certification against every other one to catch near-duplicates — up to a dozen comparisons per candidate. Prompted with only the field name, the model misses a third of true duplicates once a resume lists more than six certifications. Which prompting addition most reliably improves accuracy?
58. [D5] Each `verify_reference` call in the enrichment step returns 25+ fields — a contact's organizational history, past call logs, other candidates they've referenced — when only `reference_name`, `relationship`, and `confirmation_status` matter for the record. On long multi-candidate sessions this bulk accumulates turn after turn, and the model starts confusing which reference belongs to which candidate. What is the most effective fix?
59. [D4] A hiring manager submits a request that reads only 'just tell me if this candidate is qualified,' with no target schema or list of criteria specified. Rather than sending back several clarifying questions about which qualifications matter before doing anything, what should the pipeline do?
60. [D5] Before a schema migration, the team must survey a large archive of previously processed candidate records to catalog which legacy field-naming conventions are still in use. Running this survey in the coordinator's main session returns thousands of per-record summaries and nearly fills its context before the migration-design conversation starts. What is the most effective way to proceed?

#### Domain Breakdown
| Domain | Total Q | Correct | % | Confirmed weak? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 15 | 93.8% | no |
| D2 Tool Design & MCP | 11 | 10 | 90.9% | no |
| D3 Claude Code Config | 12 | 11 | 91.7% | no |
| D4 Prompt Engineering | 12 | 11 | 91.7% | no |
| D5 Context Management | 9 | 8 | 88.9% | no |

#### Scenario Block Breakdown
| Block | Questions | Correct | % |
|---|---|---|---|
| Customer Support Resolution Agent | 15 | 12 | 80.0% |
| Developer Productivity with Claude | 15 | 15 | 100.0% |
| Claude Code for Continuous Integration | 15 | 14 | 93.3% |
| Structured Data Extraction | 15 | 14 | 93.3% |

#### Observations

- **D5 is this paper's sole weakest domain (88.9%, 8/9)** — not confirmed: the most recent prior scored exam (Exam 9, by attempt chronology) was weakest in D2, a different domain, so the two-consecutive-exam bar isn't met. D5 was also this project's sole weakest domain once before, in Exam 6 — not consecutive with this one either.
- **D2's confirmed-weakness streak is broken.** Exam 9 scored D2 at 63.6% and confirmed it weak (two consecutive exams, Exam 10 then Exam 9). This exam recovers to 90.9%, its second-strongest domain. Caveat: Exam 11 ran the standard, non-adjusted FULL-60 quota (D2 at 11 questions) — it doesn't yet test whether D2 holds up under Exam 12's larger, weakness-adjusted 15-question D2 allocation, since Exam 12 remains unattempted.
- **A single miss repeats a four-exam pattern.** Q9 (§2.8, composite tool vs. prompt-bundling for two habitually-paired calls) was missed here exactly as it was in Exam 5, Exam 8, and Exam 10 — the same specific misconception recurring across four separate sittings despite the corpus carrying exactly one teachable point on it. This is now the single most persistent individual miss in the project's history.
- **No Key Distinction was hit among the five misses** — unusual; prior scored exams typically show at least one KD-tagged miss. All five map to plain corpus sections: §2.8 (Q9), §1.18 (Q12 — named-pattern recall, evaluator-optimizer confused with context isolation), §5.8 (Q14 — escalation/ambiguity, over-escalated a resolvable case where one clarifying question was the efficient right move, the opposite failure mode from the domain's usual guess-instead-of-ask trap), §4.13 (Q43 — confidence-calibrated routing, reached for a second review pass instead of a structured per-finding confidence signal), §3.1 (Q50 — CLAUDE.md concatenation, assumed a subdirectory file overrides root rather than adding to it; this is the drill deck's own tracked `d3.1` known-gap).
- **Timing: 2,418s total, 40.3s/question average.** Two of the three slowest questions were misses (Q43 at 108s, Q50 at 101s) — plausible genuine deliberation on harder items, not fast wrong guesses. The third slowest, Q25 (105s), was answered correctly.

### Questions Used
Already logged under the Exam 11 generation entry above — no new stems from scoring.

---

### Professor's Note — Intent for Exam 13
Written after Exam 11 (2026-08-10). Based on results-json. **Note the numbering: titled "Intent for Exam 13," not Exam 12 — Exam 12 was already generated (2026-08-10, unattempted) before this score arrived, mirroring the Exam 9→12 skip precedent.**

- Misconceptions revealed:
  1. **A four-exam-running miss on D2 §2.8** (composite tool vs. prompt-bundling for habitually-paired tool calls) — missed in Exams 5, 8, 10, and now 11, despite the corpus carrying exactly one teachable point on it.
  2. **§1.18 named-pattern confusion** (D1) — evaluator-optimizer (independent critic reviewing a draft) mistaken for context isolation (a subagent scoped to limited input); both involve "independence" but name different mechanisms.
  3. **§5.8 over-escalation** (D5) — routed a resolvable ambiguity (multiple accounts sharing one phone number) straight to a human instead of asking one clarifying question, the opposite failure mode from the domain's more common under-escalation trap.
- Weakest this paper: D5 at 88.9% — not yet confirmed (different domain than Exam 9's D2).
- Intent for next paper: within the fixed domain quota, give §2.8 a fifth test — not because it needs more depth (the corpus has only the one lesson), but because four straight misses on a single-fact section is itself the signal worth confirming isn't noise; give D5 §5.8 a second formal test to see whether this exam's over-escalation miss recurs or was a one-off; and note for whoever scores Exam 12 next that its weakness-adjusted 15-question D2 quota is the real test of whether this exam's D2 recovery holds at scale.
- Watch next: does D5 confirm as weak once Exam 12 (or whichever exam is attempted next) is scored, and does D2's recovery survive Exam 12's larger, targeted quota.

---

*Superseded 2026-08-10 — the two notes below predate both Exam 11's scoring and Exam 12's generation, both of which have since happened (see the entries above and below). Left in place as history rather than deleted; do not treat "Next exam: Exam 12" or "Exam 11 remains unscored" as current. Current state as of Exam 11's scoring: exams_scored = 8 (not a multiple of 3 — Insights Round 3 fires on the next exam scored, most likely Exam 12). Exam 12 exists, generated, unattempted. Next exam to generate after that is Exam 13.*

*Next exam: Exam 12. Next deduplication check: all 30 Exam-1 stems + all 60 Exam-2 stems + all 60 Exam-3 stems + all 60 Exam-4 stems + all 60 Exam-5 stems + all 60 Exam-6 stems + all 60 Exam-7 stems + all 60 Exam-8 stems + all 60 Exam-9 stems + all 60 Exam-10 stems + all 60 Exam-11 stems above + all 76 practice-test stems are off-limits.*

*Exam 9 was scored 2026-08-09 (49/60, 835/1000) — see its entry above. This CONFIRMED D2 as weak (two consecutive scored exams by attempt chronology: Exam 10, then Exam 9), producing the Professor's Note — Intent for Exam 12 above, which carries a confirmed-weakness quota adjustment (D1 14/D2 15/D3 12/D4 12/D5 7 — not the base 16/11/12/12/9). One exam remains generated and unscored (Exam 11, generated 2026-07-29). Scoring it would bring exams_scored to 8 — not a multiple of 3, so no Insights Round is due from that alone.*

---

## Exam 12 — Generated 2026-08-10

**File:** `mock-exams/CCA-Prep_MockTest-12_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Code Generation with Claude Code; Multi-Agent Research System; Developer Productivity with Claude; Claude Code for Continuous Integration
**Attempt date:** 2026-08-11
**Score source:** results-json
**Total score:** 53 / 60 correct (estimated scaled: 895 / 1000; pass line 720)
**Total time:** 42:40 (42.7s/question — 36% of the 120-minute allowance)

**First exam generated under a confirmed-weakness quota since Exam 6, and the first generated from a purpose-written launch prompt** (`CCA-Prep_Exam-12-Launch-Prompt_v1.md`) rather than a cold `/cca-exam` start. Domain quota is the D2-collision adjustment (+4 D2, −2 D5, −2 D1, since D2 cannot donate to itself): **D1 14 / D2 15 / D3 12 / D4 12 / D5 7**, verified to 60 before any question was written. Driver: D2 CONFIRMED weak — weakest domain in the two most recent scored exams by attempt chronology (Exam 10 at 81.8%, Exam 9 at 63.6%).

**Scenario draw — solved as a feasibility problem across all 15 possible 4-of-6 draws, and the adjusted quota changed the answer.** Under the standard 16/11/12/12/9 spread only one draw is infeasible (the one with no D4-carrier). Under Exam 12's quota **three** are infeasible, and the newly binding constraint is not D4 but **D5 shrinking to 7**, which cannot satisfy three D5-primary blocks. Of the twelve feasible draws, Code Generation + Multi-Agent Research + Developer Productivity + Claude Code CI is the only one at the minimum rotation-sum (26) containing **zero** scenarios on a two-exam streak — it rests Customer Support and Structured Data Extraction, both drawn in Exam 10 AND Exam 11. Post-Exam-12 spread: Customer Support 7, Code Generation 7, Multi-Agent Research 7, Developer Productivity 8, Claude Code CI 8, Structured Data Extraction 7.

**Authored centrally in one context rather than delegated to four parallel sub-agents.** Phase 4.b.6 makes delegation optional; PB-19 (cross-block same-lesson collision, four variants across Exams 7/8/9/11) is caused specifically by sibling sub-agents that cannot read each other's drafts. Authoring all four blocks in a single context removes that failure family structurally rather than detecting it afterward — but it introduces a different risk, realised below.

Block x domain allocation (primary domains bold): Code Generation — **D3 5, D5 4**, D1 2, D2 2, D4 2; Multi-Agent Research — **D1 5, D2 6, D5 3**, D3 0, D4 1; Developer Productivity — **D1 5, D2 6, D3 3**, D4 1, D5 0; Claude Code CI — **D3 4, D4 8**, D1 2, D2 1, D5 0. Every block clears the primary-vs-non-primary gate with a margin of 2, chosen deliberately over knife-edge margins of 1 so a later swap could not silently break it.

**D2's 15-over-9 problem was solved by reading the corpus, not by assuming.** Before any question was written, the actual section text of every D2 section was read to establish how many genuinely distinct teachable lessons it carries. Result: §2.5 and §2.6 support three or more facets; §2.1, §2.2, §2.3, §2.9 support two; **§2.4, §2.7 and §2.8 support exactly one**. So §2.8 received exactly one question — the dedicated, unambiguous test the Professor's Note asked for — and the six forced repeats were placed only where the corpus can actually carry them: §2.6 x3, and §2.2 / §2.3 / §2.5 / §2.9 x2 each. This applies PB-19's sharpened Exam 11 recommendation before the fact instead of after.

**Two real defects were caught by the gates, both worth recording.**

1. **Twenty of sixty stems drifted into close paraphrase of prior exams.** A Jaccard scan against all 630 prior mock stems plus the 76 locked practice stems found Q49 at **0.833** similarity to Exam 9 Q48 — effectively a reskin, differing only in a percentage and one field name — plus Q44 at 0.676, Q16 at 0.636, Q25 at 0.625, Q47 at 0.612, and twenty in total above 0.30. The root cause is specific to this session's central-authoring choice: writing all four blocks in one context means the prior exams' stem lists are *in* that context, and their framings get reproduced. Every stem above 0.30 was rewritten around a genuinely different situation; final state is **max similarity 0.298 with zero pairs above 0.30**, matching the standard Exams 9 and 11 shipped.

2. **A cross-block same-lesson collision the citation tally is structurally blind to.** Q19 (D2 §2.2) and Q37 (D2 §2.6) both reduced to "rewrite the tool description" — different sections, different citations, one lesson. The corpus itself confirms they are the same rule: KD#29's entry states it "mirrors #10". Q37 was reassigned to §2.6's `.mcp.json` project-scope-with-`${VAR}` facet. This is precisely the PB-19 Exam 9 variant, and it was caught only by the mandatory side-by-side read of every repeated-section pair.

Also caught and fixed: four questions whose correct option drifted from its pre-planned letter while drafting (Q5, Q11, Q26, Q29), found by the per-block structural gate and fixed by reordering options only, with `whyWrong` indices remapped and no content or rationale text changed.

All six Phase 4.e.6 Fidelity Verification Gate checks pass, computed programmatically on the shipped file: **0 invented company/product/persona names** exam-wide (three capitalised-token candidates reviewed and cleared — all sit inside quoted tool descriptions or code tokens); correct-answer letters exact **15/15/15/15**, every block within 1 of the balanced split (Code Generation A4/B4/C4/D3, Multi-Agent A4/B4/C3/D4, Developer Productivity A4/B3/C4/D4, Claude Code CI A3/B4/C4/D4), every question landing on its centrally pre-planned letter; stem word count min 45 / median 51.5 / max 65, options min 10 / median 17 / max 27, all inside the hard caps; every block passes primary-vs-non-primary and the exam-wide quota matches target exactly; inline code/config token rate **26.7% (64/240)**, inside the 25–30% acceptable band, concentrated in D2 (25/60) and D3 (23/48); scenario-rotation disclosure present on the landing card. Supplementary: the intra-exam near-duplicate scan found **zero** stem pairs above 0.30 across all 1,770 pairs, and the citation tally shows **53 distinct corpus sections** cited across 60 questions.

Verified end-to-end in a live browser: landing-card content, the block header on a block's first question, Next disabled until answered, both feedback paths (a wrong pick leads with the picked option's `whyWrong`; a right pick confirms then lists the others), the results card with per-domain and per-block breakdowns, the results-JSON export reading `"exam_n": 12` and per-domain `of` values matching the adjusted quota, and the running-accuracy pill at five states including the exact 31/45 = 68.89% pass boundary (correctly green) and 30/45 just below it (correctly red). All three localStorage resume branches confirmed: no answers routes to the landing card, 7 answered routes to Q8 (the first unanswered), all 60 answered routes to results. Zero console errors; `node --check` passes on the extracted script.

**Key Distinction budget:** **15 of 60** questions carry a clearly-matching Key Distinction — KD#2 (Q37), KD#3 (Q34), KD#4 (Q39), KD#8 (Q59), KD#10 (Q19), KD#12 (Q55), KD#14 (Q45), KD#15 (Q46), KD#16 (Q6), KD#17 (Q54), KD#20 (Q23), KD#22 (Q7), KD#23 (Q42), KD#26 (Q32), and **KD#27 (Q35 — the Professor's Note re-test)**. That is exactly at the hard 15 cap and far above the 4–6 tightened target, reached without a single deliberate seeding decision beyond KD#27. Logged as **PB-22**: an enlarged D2 quota mechanically inflates KD density, because D2 alone carries 8 of the 29 Key Distinctions.

### Questions Used (deduplication — do not reuse these stems in Exam 13+)

1. [D3] Claude applies your repository's error-handling convention in some sessions and silently ignores it in others, on the same machine and the same checkout. The convention is written down, nobody can predict when it takes effect, and it has cost two rounds of review comments this month. What is the most effective first diagnostic step?
2. [D3] Your project `CLAUDE.md` has reached 500-plus lines. Every rule in it genuinely applies to every session — naming, error handling, logging, dependency policy — but maintainers can no longer find or review anything, and edits collide. The team wants the same content to keep loading in full. What is the supported way to reorganize it?
3. [D3] A library migration will touch 45-plus files and forces decisions about how shared helpers are restructured. Your team's habit is to begin in direct execution and switch into plan mode only once a task turns out to be messy. The last two migrations each needed substantial rework after that switch. What should the team do?
4. [D1] The assistant produces a set of rule adapters. Its reasoning trace shows it considered, then set aside, a boundary condition on negative amounts. Asked in the same session to check its work thoroughly, it reports nothing. A human finds the defect a week later. What most directly addresses the cause?
5. [D3] A generated proration helper mishandles zero-length billing periods, affecting roughly one account in forty. The engineer has re-described the defect in prose three times, most recently as "really handle every zero-day case," and each regeneration fixes one reading while breaking another. Two rounds have now regressed a case that previously passed. What converges fastest?
6. [D4] Generated rule adapters must return a fixed result envelope: a status field, a decimal amount, and an array of applied rule identifiers. The prompt already states this requirement in detail, yet roughly one adapter in eight nests the identifiers under an extra object or returns the amount as a string. What most reliably fixes the format?
7. [D5] Before the team can restructure the rules engine, someone must enumerate every call site of a deprecated evaluator across roughly 200 files. Running that discovery in the working session fills most of the context window with match listings, and the design discussion that follows becomes noticeably vaguer. What is most effective?
8. [D2] Your internal API registry is exposed through an MCP server with a `find_endpoint` tool. Logs show the assistant spends several turns per task guessing endpoint names to work out what the registry even contains before it can ask anything useful. The registry publishes a stable structured index. What is most effective?
9. [D5] A refactor session is approaching its context limit. It holds a few decisions the remaining work depends on — a chosen migration order, an agreed compatibility cutoff, one field rename — plus a long abandoned exploration and the last dozen implementation turns. How should the context be reduced?
10. [D3] Your team ships a `/regen-fixtures` skill that rewrites generated test fixtures. A dry run last week left three untracked build artifacts behind, and reviewers now want the skill constrained so that while it runs it cannot reach past file reads and writes into commands that touch the working tree. Where is that constraint configured?
11. [D4] Your codegen assistant must hold three behaviours for a whole working session: never invent a rule identifier, always state which assumptions it made, and keep explanations to two sentences. These are currently written into the first user message of each session. By the tenth exchange all three have decayed. Where do they belong?
12. [D5] Each call to your `get_rule_definition` tool returns 40-plus fields — full revision history, approver metadata, localized descriptions — when only the identifier, effective dates, and formula matter. Across a long session those results accumulate turn after turn and later answers start confusing similar rules. What is most effective?
13. [D2] A maintenance tool your assistant can call rewrites rule definitions in bulk. Policy says any invocation affecting more than 50 definitions must go to a release manager instead of executing. The rule currently lives in the system prompt, and an audit found two bulk rewrites above the threshold that ran anyway. What enforcement is most effective?
14. [D1] An expensive session has finished mapping the rules engine's dependency graph. The team now wants to evaluate two restructuring approaches from that same completed analysis — one extracting a shared evaluator, one keeping evaluation inline — without either exploration influencing the other. What is most effective?
15. [D5] A three-week schema migration runs through hundreds of tool calls and is about a third complete. Twice a session has ended unexpectedly mid-run, and both times work restarted from nothing: which tables were already converted, and which were blocked on foreign keys, existed only inside that conversation. What is most effective?
16. [D1] Your coordinator delegates from a fixed script: query these four databases in this order, open the top ten results from each, summarise each in 120 words. When a subagent surfaces a promising lead outside those four sources, nothing in the system pursues it. Which change is most effective?
17. [D1] The synthesis subagent reports that it has nothing to work with, though the web-search and document-analysis subagents both completed successfully and their results sit in the coordinator's own history. This has happened on all nine cycles run so far, and re-running the upstream subagents changes nothing. What is the root cause and correct fix?
18. [D2] Your hand-built coordinator loop executes both tools Claude requested, then sends back a fresh user message describing what each returned. Claude answers as though neither tool had run and requests them both again. The loop has been in production a week and every multi-tool turn ends the same way. What is wrong with the request the loop sends?
19. [D2] The coordinator has two retrieval tools: `analyze_publication`, held by the document-analysis subagent, and `analyze_source`, held by the web-search subagent. Both descriptions read only "Analyzes a source and returns findings." Requests naming an uploaded PDF go to the web-search subagent's tool 45% of the time. What is most effective?
20. [D2] The document-analysis subagent now carries nineteen tools accumulated over successive projects — several near-duplicates for fetching, parsing, and citing. It selects the wrong one often enough that reviewers no longer trust its output. The web-search subagent, with five role-scoped tools, selects correctly. What is most effective?
21. [D1] Each subagent returns findings as plain sentences and separately lists the documents it consulted. When the report is assembled, reviewers spot-checking twenty claims find six attributed to a document that does not contain them. Four reports this quarter have come back from the review board for this same reason. What is the most effective fix?
22. [D2] Your literature tool signals a paywalled record, a malformed query string, and a temporarily unreachable index identically: `isError: true` plus one sentence of prose. The coordinator responds to all three the same way and gets it wrong two times out of three. How should the error response be restructured?
23. [D5] The synthesis subagent receives roughly 80,000 tokens of combined findings. Reviewers notice it consistently reflects the opening summaries and the closing conclusions, while substantive results sitting in the middle of the input are absent from every draft. Three cycles running, the same mid-input material has gone unmentioned. What is most effective?
24. [D2] Analysing a record always requires both its bibliographic header and its full text, yet the document-analysis subagent requests the header in one turn and the text in the next. That extra round-trip is now on nearly every record in the cycle. What most effectively removes it?
25. [D1] A synthesis draft covers four of the five material properties the brief named explicitly; corrosion behaviour is absent entirely, though the analysis subagent's logs show it processed records that discuss it at length. The coordinator must decide what to do about the missing section before the report ships. What should it do?
26. [D2] Your team needs the research pipeline to reach a widely used issue tracker and a widely used document store, plus an internal sample-registry service that exists nowhere else. An engineer proposes building all three MCP servers in-house for consistency and control. How should the team evaluate this?
27. [D5] On roughly one property in nine, two credible sources report materially different values, and the analysis subagent has no basis for adjudicating between them. Reviewers have flagged three reports this quarter where the discarded value later proved the better one. The team is deciding what the subagent should do on such a disagreement. Which behaviour is correct?
28. [D1] A supplier-datasheet archive the pipeline normally draws on has been unreachable all week, so one of the brief's five evidence streams contributed nothing this cycle. The synthesis subagent returned a complete-looking draft in which no conclusion is marked as resting on thinner evidence than any other. What should its output do instead?
29. [D4] Every field in the extraction schema is mandatory and non-nullable, on the reasoning that aggregation should never receive a partial row. An audit of 2,000 papers finds that in roughly 7% of them the grant identifier the model returned is convincing but simply not present anywhere in the text. Which schema change stops the invention at its source?
30. [D5] Extraction across the record set measures 96% accurate on a labelled audit, and the team proposes auto-accepting every high-confidence extraction with no reviewer involvement. Scanned pre-1990 proceedings make up about 4% of volume and were barely represented in that audit. Before reducing review, what should the team do first?
31. [D1] Your assistant is configured as a coordinator with specialist workers for exploration, scaffolding, and cleanup. In three weeks it has never delegated once — it attempts every chore itself, badly, while the workers sit idle. Its `AgentDefinition` sets `allowed_tools` to Read, Grep, and Glob. What is the most effective fix?
32. [D2] An engineer needs every place the legacy `resolveTenant` helper is actually invoked, so she can judge the blast radius of changing it. The monorepo holds roughly 4,000 files and the helper is referenced from several packages. The assistant must choose a built-in tool for the first step. Which should it use, and why?
33. [D2] Every chore the assistant completes must post a structured record to the team's work tracker: chore type, files touched, and outcome. Three recording tools exist, one per chore type. On roughly one chore in twelve the assistant explains what it did in prose and calls nothing, so the tracker gets no record. Which configuration guarantees a record?
34. [D3] Your monorepo needs three sets of conventions applied automatically: Go services follow one error-wrapping style, TypeScript packages follow an async style, and test files everywhere follow one shared testing convention. Tests sit beside the code they cover rather than in a dedicated tree. What configuration applies each set where it belongs?
35. [D2] Standardising a logging call, the assistant issues an `Edit` anchored on `log.Printf(`. The call fails: that text appears in nineteen places across a 900-line file, so `Edit` cannot determine which occurrence to change. Two of the nineteen sit inside a vendored block that must be left untouched. What is the sanctioned way to complete the change?
36. [D1] An engineer asks the assistant to make a neglected package deployable again. What that will take is unknown at the outset: the first pass finds an unpinned dependency, which exposes a broken build step, which in turn reveals a service call nobody documented. Which decomposition strategy fits?
37. [D2] The build-cache MCP server is about to roll out to forty engineers. Each authenticates with a personal token that must never enter the repository, but the server's endpoint and arguments should be identical for everyone and visible in code review. Which configuration meets both requirements?
38. [D1] The exploration worker was given a general `run_command` tool so it could invoke build helpers while investigating. It has begun using that tool to install packages and rewrite lockfiles mid-investigation, twice leaving the workspace in a state the engineer had to undo by hand. What is most effective?
39. [D3] Your repository ships a `/preflight` skill that every engineer receives on clone. One engineer needs a stricter local variant under that same command name, with nothing changing for the rest of the team. Her new personal version has produced a second, separate entry in the command menu instead of replacing the original. What is the cause and fix?
40. [D2] Your `find_owning_team` tool answers with `{"teams": [], "isError": true}` both when a component genuinely has no registered owner and when the ownership service is down. On outage days the assistant reports components as unowned; on genuinely unowned ones it retries and escalates. How should the tool signal these?
41. [D1] An engineer asks the assistant to prepare a service for review: check the dependency licences, regenerate the API client, and summarise open migrations. None of the three depends on the others' results. The coordinator currently issues them one after another, and the wait is now the engineers' main complaint. What is most effective?
42. [D4] The assistant's system prompt sets three standing rules: cite a file path with every claim, never propose a change outside the package under discussion, and keep summaries under five bullets. Engineers report all three hold early and decay by around turn fifteen, though the session is only about 3,000 tokens. What is the root cause?
43. [D2] The assistant has `get_service_metadata`, returning ownership and deployment configuration, and `get_service_dependencies`, returning the dependency graph. Both are called often and an engineer proposes replacing them with one `get_service` tool that returns everything, arguing fewer tools means fewer wrong choices. How should the team evaluate this?
44. [D1] Escalations reach the on-call queue as a chore name plus one free-text sentence. About a quarter are handed straight back asking for detail, the engineers who do act begin by repeating the investigation the assistant already completed, and median time to first human action now exceeds a day. What change most effectively fixes this?
45. [D3] Three assistant workloads are under cost review: an interactive dependency query an engineer waits on, an overnight sweep that regenerates API clients for every service, and a weekly licence audit across the monorepo. The team wants the Message Batches API's 50% discount wherever it fits. Which assignment is correct?
46. [D3] A new pipeline stage shells out to the Claude Code CLI with the review prompt as its only argument. The stage emits nothing and holds the runner until the job's wall-clock limit kills it. Teammates propose four ways to make it run unattended. Which is the documented approach?
47. [D3] A small service turns each review into per-line annotations and needs four fields it can rely on for every finding. Today it splits the model's prose on headings and blank lines; it broke twice last month when the phrasing shifted. What is the most reliable way to get parseable findings?
48. [D4] Developers have stopped reading the severity field: a finding marked high on one pull request looks, to them, indistinguishable from one marked low on the next. The only guidance the reviewer has is to assign a severity that fits the issue. What most reliably makes severity consistent?
49. [D4] Schema-shaped findings have eliminated every parse failure from the ingestion service. A quarterly audit still turns up findings whose `severity` is a valid enum value but plainly wrong for the defect described, plus a handful naming a file outside the change set. An engineer wants the schema tightened further. How should the team interpret this?
50. [D4] The finding tool's JSON schema is maintained by hand, and a separate validation class in the ingestion service re-checks the same fields. Twice this quarter a field was added to one and not the other, and malformed findings reached the pull request. An engineer proposes a review checklist item covering both files. How should the team respond?
51. [D4] Validation rejects any finding whose `suggested_fix` is empty, and the pipeline retries with the document and the specific error. On roughly 60 findings per week the retries exhaust all three attempts; inspection shows these are findings where the diff genuinely offers no concrete fix — a missing test, an architectural concern. An engineer wants max retries raised to ten. What should the team do instead?
52. [D4] Each review response reports `issues_found` as an integer alongside the findings array. A post-incident review turns up pull requests that merged green because `issues_found` read 0 while the array held three findings the pipeline then skipped. Nothing caught the contradiction. What design change most directly catches it?
53. [D1] The review job decomposes each pull request into per-language source passes: one for Go files, one for TypeScript. A quarterly audit finds that migration scripts, CI workflow files, and infrastructure manifests have never once been reviewed, though every pass completed successfully and reported no errors. What is the root cause?
54. [D4] A pull request touching 16 files goes through the reviewer in a single pass. Feedback is detailed on three files and cursory on the rest, an off-by-one in a loop bound goes unflagged, and the same nil-check pattern is criticised in one file and approved in another. How should the team restructure the review?
55. [D2] A pipeline tool force-expires every cached build artifact for a service. It cannot be reversed from the pipeline and silently invalidates other teams' builds, so policy requires a human to see the blast radius first. The assistant chooses its own call order. Which design makes skipping the preview impossible?
56. [D3] Engineers keep re-typing the same long prompt to reproduce the CI reviewer's behaviour locally before pushing, and six of them have each built a slightly different local version. The team wants a `/local-review` command everyone gets automatically on clone or pull, with nothing to configure. Where should the command file be created?
57. [D4] A weekly full-repository audit runs on the Message Batches API for the 50% discount. Its report must be on the platform lead's desk by Monday 09:00. In testing every batch returned within about two hours, so the team schedules submission for Monday 06:00. What is the correct submission planning rule?
58. [D4] Two of the reviewer's six finding categories were added last quarter and are wrong roughly half the time. Since they shipped, the rate at which developers open any finding at all has fallen by two-thirds — including in the four categories they used to trust. The team has one sprint. What is most effective?
59. [D1] The test-generation worker reports `status: failed` and nothing more when it cannot build a module. The coordinator therefore responds identically whether the build broke on a missing credential, a compiler error, or a flaky network mount, and the run log preserves none of that difference. What should the worker return instead?
60. [D3] A named session holds an expensive dependency analysis of the monorepo from three weeks ago. A large refactor has since moved roughly a third of the packages, and the engineer estimates that re-running the analysis outright would take most of a day. She wants to continue that investigation today. What is the best way to proceed?

---

## Exam 13 — Generated 2026-08-11

**File:** `mock-exams/CCA-Prep_MockTest-13_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions)
**Scenarios drawn:** Customer Support Resolution Agent; Multi-Agent Research System; Code Generation with Claude Code; Structured Data Extraction
**Attempt date:** 2026-08-12
**Score source:** results-json
**Total score:** 57 / 60 correct (estimated scaled: 955 / 1000; pass line 720) — best of ten
**Total time:** 35:53 (35.9s/question — 30% of the 120-minute allowance)

**Purpose:** final paper before the real exam, booked for 2026-08-18. Written to confirm the repeat-offender concepts are closed, not to introduce new difficulty.

**Quota:** base weights — D1 16 / D2 11 / D3 12 / D4 12 / D5 9. No confirmed-weakness adjustment applies: by attempt chronology the two most recent scored papers are Exam 9 (weakest D2) and Exam 11 (weakest D5), different domains, so the two-consecutive-exam gate is not met. Targeting is therefore expressed entirely through section choice inside the fixed quota, per the Professor's Note contract.

**Scenario rotation:** rests Developer Productivity with Claude and Claude Code for Continuous Integration (both at 8 draws, the joint most-used, and both in Exam 12). This draw brings all six official scenarios to 8 draws each — a perfectly level spread for the first time in the project.

**Block x domain allocation:**

| Block | Scenario | Primary domains | Allocation |
|---|---|---|---|
| 1 | Customer Support Resolution Agent | D1, D2, D5 | D1 8 / D2 5 / D5 2 |
| 2 | Multi-Agent Research System | D1, D2, D5 | D1 8 / D2 5 / D5 2 |
| 3 | Code Generation with Claude Code | D3, D5 | D3 12 / D5 2 / D2 1 |
| 4 | Structured Data Extraction | D4, D5 | D4 12 / D5 3 |

No non-primary domain outnumbers a primary domain in any block (block 3's single D2 question sits below its D5 count of 2).

**Correct-answer letter pre-plan (fixed before options were drafted):**

| Block | Short letter | Sequence | Tally |
|---|---|---|---|
| 1 | D | `CADBACBDABCABCD` | A4 B4 C4 D3 |
| 2 | C | `BDACDABCADBACBD` | A4 B4 C3 D4 |
| 3 | B | `DACBADCABDCBACD` | A4 B3 C4 D4 |
| 4 | A | `CBDACDBCADBCDAB` | A3 B4 C4 D4 |

Exam-wide tally 15 / 15 / 15 / 15. Longest run of one letter: 2.

**Sections targeted (drawn from the miss record across all eight scored papers):**

| Section | Miss history | Questions |
|---|---|---|
| D2 §2.8 composite tool vs prompt bundling | missed Exams 5, 8, 10, 11 — four straight | Q3 |
| D2 §2.4 / KD#12 two-tool token binding | missed Exams 4, 5, 6 | Q6 |
| D2 §2.1 tool_use / tool_result correlation | missed Exams 4, 5, 6 | Q17, Q46 |
| D3 §3.1 CLAUDE.md concatenation and @import | missed Exams 4 (x2), 7 | Q31, Q32 |
| D2 §2.2 description scope and boundary | missed Exams 4, 6 | Q19 |
| D2 §2.9 Grep vs Glob | missed Exams 4, 5 | Q37 |
| D1 §1.6 coordinator decomposition as root cause | missed Exams 4, 5 | Q16 |
| D1 §1.3 AgentDefinition tool restriction | missed Exams 4, 7 | Q11, Q21 |
| D3 §3.3 allowed-tools vs context: fork | missed Exams 4, 6 | Q34 |
| D4 §4.2 reasoning cue vs few-shot | missed Exams 5, 6 | Q50 |
| D3 §3.4 fabricated command obsolescence | missed Exam 5 | Q35 |
| D5 §5.1 stateless API | missed Exam 6 | Q58 |
| D4 §4.17 disable the noisy category now | missed Exam 5 | Q56 |
| D4 §4.14 prompt chaining | missed Exam 5 | Q57 |
| D5 §5.13 hybrid context window | missed Exam 6 | Q42 |
| D5 §5.8 over-escalation of a resolvable ambiguity | missed Exam 11 — second formal test | Q5 |
| D1 §1.18 evaluator-optimizer vs context isolation | missed Exam 11 — second formal test | Q20 |

**Fidelity gates (computed programmatically, not hand-counted):** 60 questions; 4 options and 3 whyWrong rationales each, every rationale carrying a corpus citation; domain quota exact; block primacy holds in all four blocks; all four letter sequences match their pre-plan exactly; inline code-token rate 22.5% of options (target band 20–25%); zero invented company, product or persona names; every one of the 17 targeted sections cited at least three times.

**Deduplication:** every stem compared against all 720 stems in Exams 2–12 plus the 76-stem practice-test ledger (732 comparisons per stem, 43,920 total). Highest similarity found: **0.355** (Q58 against a practice-ledger stem), well under the 0.70 threshold. Five closest: Q58 0.36, Q33 0.35, Q41 0.35, Q9 0.34, Q29 0.34.

### Questions Used (for deduplication)

1. [D1] Your harness treats a response as finished whenever `stop_reason` is absent from its checks: it inspects the response for a `tool_use` block, and if none is present it returns the text. A recent change added a tool that occasionally returns nothing useful, and the agent now sometimes replies with a partial sentence and stops. What should the harness key its loop control on?
2. [D1] Production logs show that in 9% of refund conversations the agent calls `process_refund` after identifying the customer only from a name and an order number the customer supplied, without `get_customer` returning a verified customer ID. Three refunds went to the wrong account last month. What change most effectively addresses this?
3. [D2] Telemetry shows `get_customer` and `lookup_order` are called back-to-back in 94% of turns that touch an order, always in that order, and never usefully apart. An engineer proposes replacing them with a single `get_customer_with_orders` tool that performs both lookups internally and returns a merged payload. What should you recommend?
4. [D1] When the agent escalates, the receiving human agent opens a ticket containing the customer's last message and a one-line reason ('customer dissatisfied with resolution'). Human agents report spending the first several minutes of every escalated call re-establishing facts the agent already had. What should the escalation payload carry?
5. [D5] A customer gives a phone number to identify themselves. `get_customer` returns two active accounts sharing that number - a personal account and a small-business account, each with recent orders. The agent immediately escalates to a human, citing ambiguous identity. Reviewers flag this as a wasted escalation. What should the agent do instead?
6. [D2] `process_refund` is irreversible once it runs. It currently accepts a `preview: boolean` parameter so the agent can inspect the calculated amount, restocking fee and account impact before committing. Audit logs show the agent has called it with `preview: false` as its first and only call on 40 occasions. Which redesign makes skipping the preview architecturally impossible?
7. [D1] A customer asks the agent to match a competitor's lower price on an item they have already received. The published policy covers price adjustments for the retailer's own listed price within 14 days and is silent on competitor matching. The agent declines the request, citing policy. What should it have done?
8. [D2] `process_refund` rejects requests above the agent's authorised limit. It currently returns `isError: true` with the message 'Operation failed'. Production shows the agent retrying these calls two or three times before giving up and telling the customer that the system is unavailable. How should the tool represent this outcome?
9. [D1] A single message reads: the delivered item is damaged, a duplicate charge appeared on the card, and the customer wants a future order redirected to a new address. The agent resolves the damaged item, replies, and waits. Two of the three matters go unaddressed until the customer writes again. How should the agent handle a message like this?
10. [D2] `lookup_order` returns a normal payload with an empty `orders` array when a verified customer genuinely has no orders in the queried window, and it returns the same empty payload when the order service times out. The agent tells customers 'I could not find any orders' in both cases. What is the most important correction?
11. [D1] The support agent delegates complex billing reconstructions to a specialist subagent. The subagent's `AgentDefinition` grants it the full tool set, and its system prompt says it should confine itself to read-only analysis. Logs show it has called `process_refund` twice during analysis runs. What is the correct fix?
12. [D1] A specialist subagent handles disputed charges. It currently receives the prompt 'resolve this dispute' and the customer's original message. Its outputs vary widely in quality and it frequently asks the coordinator for facts the coordinator already holds. What is the most effective change to the delegation?
13. [D2] The agent has grown from five tools to nineteen as new backend integrations were added. Selection accuracy has fallen: it now routinely calls a shipment-tracking tool for billing questions. An engineer proposes writing longer descriptions for all nineteen. What is the more effective response?
14. [D5] In a long billing conversation the customer states at turn 3 that they were promised a 15% loyalty adjustment on a $412.60 order. At turn 26, after two rounds of summarisation, the agent quotes a $41.26 adjustment and the customer disputes it. What is the most effective fix?
15. [D1] An account-takeover report needs investigating: the steps required depend entirely on what each check reveals - whether the email was changed, whether shipping addresses were altered, whether new payment methods were added, whether recent orders were placed. Engineers propose a fixed five-step pipeline run identically on every report. Which decomposition suits this work, and why?
16. [D1] A brief on 'the effect of automation on regional employment' returns a report covering only manufacturing. The web-search subagent returned relevant sources, the analysis subagent summarised them correctly, and synthesis produced coherent prose. The coordinator's log shows it created three subtasks: 'automation in factory assembly', 'robotics in warehousing', and 'automated quality inspection'. What is the most likely root cause?
17. [D2] The coordinator receives a response with `stop_reason: "tool_use"` containing a `tool_use` block for `search_web`. The harness reads the query, runs the search, and appends a new user message containing the results as plain text before calling the model again. The model frequently re-requests the same search. What is the harness doing wrong?
18. [D1] The coordinator evaluates each synthesis draft for gaps and re-delegates to the search and analysis subagents when it finds any. On broad topics it has run eleven refinement cycles on a single brief, each adding progressively less. An engineer proposes capping the loop at three cycles. What is the better design?
19. [D2] The document-analysis subagent has a `fetch_source` tool described as 'Retrieves a source document.' It handles PDFs and HTML pages by URL, silently returns the first 40 pages of longer PDFs, and cannot read anything behind authentication. Analysts have begun citing truncated documents as complete. What is the most effective fix?
20. [D1] You want to reduce factual errors in the final brief. The proposal is to add a second agent that receives the completed draft with no access to the drafting agent's reasoning, checks each claim against the cited sources, and returns a list of corrections that the drafting agent then applies. Which named pattern is this?
21. [D1] A newly deployed coordinator returns a plan describing which subagents it intends to invoke, then answers the research question itself from its own knowledge. It never delegates. Its `AgentDefinition` lists `allowedTools: ["WebSearch", "Read", "Write"]`. What is preventing delegation?
22. [D2] While combining findings, the synthesis subagent needs to confirm individual facts - a date, a figure, an author's affiliation. It currently returns control to the coordinator, which invokes the web-search subagent and re-invokes synthesis, adding two to three round-trips per brief. Review shows 85% of these checks are single-fact confirmations; the remainder need real investigation. What is the most effective change?
23. [D1] Two of five source repositories were unreachable throughout a research run. The coordinator proceeded with the three that responded, and the delivered brief reads as a complete survey with no indication that anything was missing. A reviewer only discovered the gap by checking the logs. What should the synthesis output have done?
24. [D1] A brief requires three independent lines of enquiry - published literature, regulatory filings, and news coverage - with no dependency between them. The coordinator currently issues one Task call, waits for the result, issues the next, and so on. Total wall-clock time is roughly the sum of the three. How should the coordinator invoke them?
25. [D2] The web-search subagent times out on a complex query. You are designing what it returns to the coordinator. Which approach best enables recovery?
26. [D1] The synthesis subagent receives from document analysis a prose paragraph per source: 'The study found a 12% reduction, though the sample was small and the authors note the period was unusual.' Attribution is routinely lost by the time the brief is written, and reviewers cannot trace claims back to sources. What should the analysis subagent output instead?
27. [D1] To cut latency, an engineer proposes that the document-analysis subagent send its findings straight to the synthesis subagent, bypassing the coordinator, and that synthesis request follow-up analysis directly when it needs more. What should you recommend?
28. [D2] Subagents repeatedly issue exploratory tool calls to discover what exists in the internal research archive - listing collections, probing for date ranges, testing whether a topic is covered - before doing any real retrieval. These discovery calls are a third of all tool traffic. Which MCP capability addresses this directly?
29. [D5] Two credible sources give different figures for the same metric: an industry association reports 34% adoption, a government survey reports 21%. The synthesis subagent currently picks the higher-quality source and reports one number. How should conflicting values be handled?
30. [D5] The final synthesis call receives all subagent outputs concatenated into one long input, ordered by the sequence in which the subagents completed. Reviewers find that findings from the first and last subagents appear reliably in the brief, while a significant finding from a subagent in the middle is repeatedly omitted - even though its output is present and correct. What is the most effective fix?
31. [D3] The repository root `CLAUDE.md` says to use four-space indentation in Python. A `CLAUDE.md` inside `services/ingest/` says to follow the project formatter's defaults, which produce four spaces. A developer working in `services/ingest/` assumes only the nearer file is in effect and deletes the root file's Python section as redundant. Formatting conventions elsewhere in the repo immediately drift. What did the developer misunderstand?
32. [D3] The root `CLAUDE.md` has grown to cover testing standards, API conventions, deployment rules, security review criteria and dependency policy - most of which is irrelevant to any one package. Maintainers of each package know which standards apply to their code. What is the most appropriate way to reorganise it?
33. [D3] Integration tests live beside the code they exercise - `client/checkout/checkout.integration.ts`, `services/ingest/parser.integration.py` - and are scattered through the tree. They share one convention set that applies nowhere else. The convention must take effect automatically whenever one is edited, without loading in unrelated sessions. Where should it live?
34. [D3] A `/scaffold-endpoint` skill generates boilerplate files. During a review of an incident where it deleted an unrelated module, you find its frontmatter contains `context: fork` and nothing else. An engineer says the fork setting should have prevented the deletion. What is the accurate assessment?
35. [D3] The team's `/review` command lives in `.claude/commands/review.md` and has been in the repository for months. A new engineer proposes rewriting it as a skill in `.claude/skills/`, on the grounds that commands in `.claude/commands/` are legacy and no longer supported. How should you respond?
36. [D3] Two tasks arrive. The first: split a shared utilities package into three packages, which changes import paths in roughly 60 files and requires deciding where several ambiguous helpers belong. The second: a null check is missing in one function, with a stack trace pointing at the exact line. How should each be approached?
37. [D2] Before deleting a deprecated helper named `normalizeCurrency`, an engineer asks the assistant to find every file that would break. The assistant runs `Glob("**/normalizeCurrency*")`, gets two matches - the helper's own module and its test - and reports that removal is safe. A manual check finds fourteen files that call it. What should the assistant have used?
38. [D3] You need generated migration scripts to follow a specific transformation: legacy date strings in several formats normalised to ISO 8601, with nulls preserved rather than defaulted. Three rounds of increasingly detailed prose instructions have produced three different interpretations. What is the most effective next step?
39. [D3] You are about to add a caching layer to a service in a domain you do not know well. You can describe the outcome you want but suspect there are considerations you have not thought of - invalidation, failure behaviour under load, consistency guarantees. What technique surfaces those before implementation?
40. [D3] The repository ships a `/commit` skill at `.claude/skills/commit/SKILL.md` enforcing the team's message format. One engineer wants an extra step in their own runs - appending a ticket reference pulled from the branch name - without changing the team's behaviour. They create `~/.claude/skills/commit/SKILL.md`. What happens, and is it the right approach?
41. [D3] A `CLAUDE.md` opens with four paragraphs on the product's history and market position, then a section on team culture, then the coding standards. Engineers report that standards buried near the end are applied inconsistently, and every session pays for the whole file. What is the most appropriate revision?
42. [D5] A long refactoring session runs for several hours. Early on you correct the assistant: the legacy adapter must keep its synchronous interface because two external consumers depend on it. Around ninety minutes later it proposes an async signature for that adapter again. A sliding window keeps the most recent turns verbatim. What design fixes this?
43. [D3] Three weeks ago you ran a named session that mapped the payment module's dependencies in detail. Since then the module has been substantially rewritten: two files split, one deleted, several interfaces changed. You need to continue the analysis. What is the more reliable approach?
44. [D5] Understanding an unfamiliar service requires tracing every caller of its event bus, enumerating its configuration surface, and mapping which modules touch persistence - all before any implementation begins. Previous attempts filled the context with file listings and search output, leaving little room for the actual work. What is the most effective approach?
45. [D3] A nightly job runs `claude "Summarise the day's dependency changes and flag risky upgrades"` and pipes stdout into a parser that expects `{"changes": [...], "risks": [...]}`. The job hangs some nights and, when it does complete, the parser fails on prose wrapped around the JSON. What combination fixes both problems?
46. [D4] The extraction step sometimes returns a conversational reply - 'This document appears to be a delivery note rather than an invoice, so I have not extracted invoice fields' - instead of calling any extraction tool. Downstream, this arrives as unparseable output. Three extraction schemas exist and the document type is not known in advance. What configuration guarantees a tool call?
47. [D4] Extraction now runs through `tool_use` with a strict JSON schema. Malformed-JSON errors have disappeared. QA still finds records where the line items sum to £4,180 while `invoice_total` reads £4,810, and occasional records where the supplier's VAT number sits in the `supplier_reference` field. An engineer concludes the schema is not being enforced. What is the accurate assessment?
48. [D4] Inspection reports vary: some record a site engineer's name and licence number, many do not. The schema marks both as required strings. QA finds the pipeline is emitting plausible-looking names and licence numbers for reports that contain neither. What is the most effective fix?
49. [D4] Two validation failures recur. In the first, `service_period_end` comes back as '31/03/26' where the schema wants ISO 8601. In the second, `parent_contract_id` is missing because the addendum references a master agreement that is not in the supplied document. Both currently trigger the same retry-with-error-feedback loop. What should change?
50. [D4] Invoices state a net amount, a VAT rate and sometimes a discount applied before tax. The pipeline must emit the gross total. Extraction is accurate on invoices where the gross is printed, and wrong on invoices where it must be derived - the discount is often applied after tax, or omitted. The schema and few-shot examples are already in place. What is the most effective addition?
51. [D4] Contract addenda cite their parent agreement in three ways: an inline reference in the opening clause, an entry in a schedule at the end, or a footnote on the signature page. Extraction is reliable for the inline form and inconsistent for the other two. Which addition most improves this?
52. [D5] Extraction accuracy is reported at 96.4% overall, and on that basis the team proposes auto-approving every record the model marks high-confidence. Reviewers object that they keep finding errors in exactly those records. What should be established before automating?
53. [D4] A nightly batch of 340 inspection reports is submitted through the Message Batches API. In the morning, 327 have succeeded and 13 have failed because those particular scans exceeded a per-request size limit. What is the most effective way to proceed?
54. [D4] Two extraction workloads exist. The first validates a supplier's invoice at the point of upload, while the supplier waits on screen for a confirmation or a correction prompt. The second reprocesses the previous quarter's archive for an audit due in three weeks. Finance asks whether both can move to the Message Batches API for the 50% saving. How should you respond?
55. [D4] Occasionally an invoice's printed total does not match the sum of its own line items - a supplier error, not an extraction error. Currently the pipeline extracts the printed total and the discrepancy surfaces weeks later in reconciliation. What extraction design surfaces it at the point of extraction?
56. [D4] The pipeline emits data-quality findings to the operations team. Dismissal rates by category: missing-VAT-number 7%, date-outside-contract-period 11%, unusual-unit-price 54%, non-standard-supplier-name 61%. The team has begun ignoring the queue wholesale, including the reliable categories. Improving the two weak categories' prompts will take a fortnight. What should you do now?
57. [D4] A single prompt asks the model to extract every obligation from a 60-page master services agreement, classify each by risk, and draft a summary memo. Output quality is uneven: obligations from the later sections are frequently missed, and the risk classifications contradict the memo. What is the most effective restructuring?
58. [D5] An operator reviews extractions through a chat interface, correcting the model over several turns. On a new deployment the model no longer recalls corrections made two turns earlier. An engineer proposes adding a `session_id` parameter to the API call so the service can maintain the thread. What is the accurate assessment?
59. [D4] A colleague asks you to 'add validation for the new supplier documents.' It is unclear which document types are in scope, whether validation means schema conformance or business-rule checking, and what should happen to records that fail. What is the most effective response?
60. [D5] Every extraction turn calls `get_document_metadata`, which returns 60-plus fields: full ingestion history, storage location, checksums, prior processing attempts, permissions. Four fields are actually used. Over a long review session the context fills with metadata and the model's answers become vague. What is the most effective fix?


---

## Exam 14 — Generated 2026-08-11

**File:** `mock-exams/CCA-Prep_MockTest-14_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions) — 47 single-answer + 13 multiple-response
**Scenarios drawn:** Multi-Agent Research System; Developer Productivity with Claude; Claude Code for Continuous Integration; Structured Data Extraction
**Attempt date:** 2026-08-15 (attempted last, after Exams 12, 13 and 17 — see "Exam 14 — SCORED 2026-08-15" below)
**Score source:** results-json
**Total score:** 49 / 60 correct (estimated scaled: 835 / 1000; pass line 720)

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
already been used and 7 had not. Four of those 7 are infeasible against this quota — {CG,DP,CI,SDE} and
{CS,CG,CI,SDE} cannot carry D1 16 with a single D1-primary block, and {CS,CG,MARS,DP} has no D4 carrier
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

**Multiple-response items:** Q6 (select 2 of 5, D1), Q11 (select 3 of 6, D1), Q14 (select 2 of 5, D5), Q21 (select 2 of 5, D1), Q26 (select 3 of 6, D2), Q29 (select 2 of 5, D1), Q35 (select 2 of 5, D4), Q40 (select 3 of 6, D3), Q43 (select 2 of 5, D2), Q45 (select 2 of 5, D3), Q49 (select 2 of 5, D5), Q54 (select 3 of 6, D5), Q59 (select 2 of 5, D5)

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

1. [D1] A brief on non-pharmacological management of chronic pain comes back covering physiotherapy in depth and nothing else. The panel expected psychological, procedural and device-based approaches as well. The run logs show four subagents dispatched, fourteen searches executed, and every result accurate and well-sourced for the query it was given. Where does the failure sit?
2. [D1] The coordinator's prompt reads: "Step 1, search the trial registry. Step 2, open the first eight results. Step 3, summarise each in 120 words." The briefs come back uniformly shallow, and when a registry search surfaces nothing useful the run still produces eight summaries of marginal trials rather than widening its search. What should change?
3. [D2] Two tools are available to the search subagent: `search_trial_registry` ("Finds studies") and `search_publication_index` ("Finds published research"). Both accept a free-text query string and both return title-and-abstract records. Logs from the past fortnight show registry lookups being routed to the publication index on roughly 40% of calls. What is the first thing to fix?
4. [D1] A panel request covers three independent questions: current first-line therapy, adverse-event rates, and cost-effectiveness. The coordinator issues one `Task` call, waits for it to return, then issues the next, and a full brief now takes about eleven minutes. All three questions need the same baseline patient-population context. Which approach uses the architecture correctly?
5. [D5] The brief's conflict section reports: "One source states prevalence at 8%, another at 13% — contradiction." On inspection the two figures come from national surveys five years apart, and both are correct for their own period. Three such false conflicts appeared last month, and the panel has begun distrusting every conflict the system flags. What is the underlying problem?
6. [D1][select-2] The full-text subagent times out on a publisher endpoint after retrying twice, having already parsed nine of the fourteen papers assigned to it. It returns `{"status": "failed"}` to the coordinator, which logs that string and abandons the entire run, discarding the nine parsed papers with it. Which two changes follow the structured error-propagation pattern? Select two.
7. [D1] The synthesis subagent returns a draft covering adult populations thoroughly and saying nothing about the paediatric subgroup the request named. Reviewing the run shows the searches that executed never targeted that subgroup, and the registry does hold paediatric trials for this indication. The coordinator now holds the draft. What should the architecture do at this point?
8. [D2] The search subagent has accumulated nineteen tools as new evidence sources were integrated over two years. It now selects the wrong source tool on roughly one call in four. The document subagent, holding five tools, almost never misroutes. Both run the same model on similarly structured prompts. What should change first?
9. [D1] The synthesis subagent's draft ignores three high-quality trials the search subagent surfaced earlier in the same run. The coordinator's own conversation history contains all three, complete with abstracts and effect sizes. The synthesis subagent's prompt instructs it to "synthesise all findings gathered so far" and says nothing further. What explains the omission?
10. [D5] Combined subagent output reaching the synthesis step runs to roughly 80,000 tokens per brief. Sampling of recent drafts shows they reliably reflect the opening sections and the closing conclusions, while findings positioned in the middle of that input are omitted or garbled. Which change addresses the cause?
11. [D1][select-3] While drafting, the synthesis subagent needs to confirm single facts — a dosage figure, a sample size — dozens of times per brief. Routing each check through the coordinator adds a full round-trip and is now the slowest part of the run, so the team proposes giving it broad search access. Which three statements are correct? Select three.
12. [D2] A registry query for trials in a rare indication legitimately returns no matches, which is itself a useful finding for the brief. The tool reports that outcome as `isError: true`. The coordinator responds by retrying the identical query twice and then escalating the whole run as blocked. What is the correct signal for this outcome?
13. [D1] Of the five evidence categories the brief requires, two came back empty because their sources were unreachable for the whole run and the retry budget is exhausted. The synthesis subagent holds usable material for the other three categories, and the review panel sits in an hour. What should it produce?
14. [D5][select-2] A six-hour brief run crashes with the search and document subagents complete and synthesis half-finished. Restarting re-executes everything from the beginning, including the ninety searches that already succeeded, and the team has now lost two afternoons this way. Which two changes let the coordinator resume from where it stopped? Select two.
15. [D2] Your evidence sources are exposed to the agent as an MCP resource listing every available registry, its coverage window and its field schema. A teammate reviewing the design argues this should have been a `list_sources` tool instead, since the agent could then request only the registries it needs. Which statement correctly distinguishes the two?
16. [D1] You ask the agent to add test coverage to the discharge-scheduling module, which currently has none and which nobody remaining fully understands. Two decomposition strategies are on the table: a predetermined sequence of steps fixed before any code is read, or subtasks generated from what each step uncovers. Which is appropriate here?
17. [D2] A deprecated `assignBedByPriority` helper is being removed, and you need every location that calls it across a repository whose naming conventions drifted years ago. An engineer proposes running Glob over `**/assignBedByPriority*` and reports that it returned two files, both of them tests. What is wrong with that, and what should run instead?
18. [D3] The agent applies your transfer-request audit-logging convention in some sessions and ignores it in others, on the same repository and the same files. The instruction is definitely written down somewhere, and a colleague working on the same codebase sees it applied every single time. What is the first diagnostic step?
19. [D1] Yesterday's named session mapped the bed-allocation call graph in depth, and that analysis is still largely valid. Overnight another team refactored three of the roughly forty files it examined. You need to continue the same investigation today without paying for the whole mapping again. What is the right way to resume?
20. [D2] The agent attempts to Edit a status constant in a 900-line scheduling file. The anchor text it selected appears in four places, and the edit fails with a non-unique-match error. The agent proposes retrying with a shorter anchor that it expects will be easier to locate. What should happen instead?
21. [D1][select-2] The agent generates a bed-reassignment routine, reasons at length about edge cases in its own output, and concludes the approach is correct. Asked in the same conversation to check its work again, it confirms the result. Two subtle defects surface in human review a week later. Which two changes address the cause? Select two.
22. [D3] A `/trace-dependencies` skill walks the scheduling module's imports and returns several thousand lines of output into the conversation. After it runs, the agent has lost track of the refactor it was carrying out beforehand and begins proposing unrelated changes. Which frontmatter change fixes this?
23. [D1] A colleague's in-house harness wraps the API and keeps calling until the response text no longer contains the word "next". It sometimes halts mid-task with tool calls still unexecuted, and sometimes keeps looping long after the work is finished. What should drive the loop instead?
24. [D3] Two tasks are queued: replacing the scheduling engine's persistence layer across roughly fifty files, where several designs are viable and the choice affects every caller, and fixing a null-dereference crash with a clear stack trace in a single file. Which pairing of modes is correct?
25. [D1] An expensive analysis of the transfer-request state machine has just completed, having taken most of an afternoon. The team wants to evaluate two migration strategies against that analysis, and wants neither evaluation coloured by the other's reasoning or conclusions. What should they do?
26. [D2][select-3] Six months ago the team replaced two frequently co-called tools with a composite `get_patient_with_transfers`, and it has worked well since. A new requirement needs patient records without any transfer history; another needs transfers for a whole ward rather than for a single patient. Which three statements are sound? Select three.
27. [D1] Adding audit hooks across the platform's 140 service files requires a discovery pass that enumerates every call site. On the last attempt the discovery output alone filled the context window before any implementation began, and the session had to be abandoned partway. What structure avoids this?
28. [D3] Conventions differ by area: scheduling services use a repository pattern, the interoperability adapters use async pipelines, and test files follow a fixture naming scheme. Files from all three areas sit side by side in most directories rather than in separate trees. Where do these conventions belong?
29. [D1][select-2] Your onboarding agent is configured with `allowed_tools=["Read", "Grep", "Glob"]` and a system prompt instructing it to delegate deep dives to specialist subagents. It never delegates — it attempts everything itself, and its sessions run long and stay shallow. Which two statements are correct? Select two.
30. [D1] The agent holds a general `run_query` tool for the reporting database so that it can answer schema questions during exploration. It has started using that tool to run ad-hoc aggregate queries against live patient tables, which the compliance team has now flagged twice. What is the durable fix?
31. [D3] The provisioning repository's review job was added last week, and every run hangs until the runner's 30-minute timeout kills it. No output is ever written to the job log. The command in the workflow file reads `claude "Review this diff for regressions"`. What is missing?
32. [D4] Six weeks of review data: style findings run at 54% false positive, documentation at 47%, security at 7%, performance at 16%. Engineers have begun dismissing every comment the job posts, security findings included, and two genuine vulnerabilities were closed unread last sprint. What should the team do?
33. [D3] Findings currently arrive as prose in the job log, and a script scrapes them with regular expressions to post inline pull-request comments. The scraper has broken three times this quarter whenever phrasing shifted. Each comment needs a file path, a line number, a severity and a suggested fix. What should replace the scraper?
34. [D3] Each time an author pushes a follow-up commit, the review job re-posts near-identical comments on code that has not changed, with slightly different wording every run. Some threads now run to dozens of comments and authors have started resolving them unread. What should the re-run prompt include?
35. [D4][select-2] A pull request touching eighteen files receives a detailed review on four of them, cursory notes on the rest, and one pattern flagged in one file yet explicitly approved in another. Re-running the job produces a different four files. Which two changes address the cause? Select two.
36. [D3] A weekly dependency-audit job runs on the Message Batches API, and its report must reach the platform lead 30 hours after submission. The schedule is being fixed now. The team is planning around batches that have so far always completed within about an hour. What submission window does the SLA actually permit?
37. [D2] The pipeline's remediation step can apply mechanical fixes automatically. Twice now it has rewritten more than 200 files in a single run after a shared formatting rule changed, and both runs reached the default branch. Policy states that any change touching over 50 files requires human approval. Where does that rule belong?
38. [D3] Generated tests for the circuit-activation service compile and pass, but they ignore the team's fixture conventions, assert on internals rather than on behaviour, and duplicate scenarios the existing suite already covers. Roughly half of each generated batch is discarded in review. What supplies the missing context to the CI-invoked run?
39. [D4] Review comments vary in shape from run to run: sometimes a bare observation, sometimes a fix, sometimes a paragraph of surrounding context. The prompt already specifies the required format across three sentences, and tightening that wording twice has changed nothing. What is the effective next move?
40. [D3][select-3] A review of the activation module raised three issues: a race in the retry path, a lock-ordering defect that the retry path depends on, and a misspelled log string. You are feeding these back for fixes and want to avoid a second round of rework. Which three statements are sound? Select three.
41. [D4] The prompt instructs the reviewer to "check that comments are accurate." It now flags every comment that is merely terse or slightly out of date — around sixty per pull request — burying the handful that actively describe the wrong behaviour. How should the criterion be rewritten?
42. [D3] The pipeline generates a migration script and then, in the same session, asks for a review of that script. Reviews come back clean; defects surface later in staging, three times this quarter. A colleague suggests adding "be more critical" to the review step's prompt. What is the actual problem?
43. [D2][select-2] The triage step must always return a structured verdict, but roughly one run in twelve comes back as a paragraph of prose instead of a tool call, and the downstream parser fails on it. Three verdict tools are defined, one per severity band. Which two statements are correct? Select two.
44. [D4] Engineers dismiss roughly a third of all findings, but the team cannot tell which kinds are noise and which are being waved through unfairly. Dismissals are currently recorded as a timestamp and a username, with no reference to what was flagged. What change makes the pattern analysable?
45. [D3][select-2] A number-porting script mishandles rows where the donor-carrier field is null. Three rounds of describing the defect in prose have produced three partial fixes, each of which broke something that previously worked. The failure reproduces reliably on a local sample. Which two moves converge fastest? Select two.
46. [D4] The schema marks `fumigation_certificate_number` as required and non-nullable, because settlement needs it. Roughly one consignment in six ships without fumigation, and those documents genuinely carry no such number. Those records now hold plausible-looking numbers that match nothing in the fumigation registry. What is the correct schema change?
47. [D5] Overall extraction accuracy sits at 97%, and the team proposes auto-processing everything above the confidence threshold from next month. Phytosanitary declarations account for about 4% of volume, arrive in three languages, and nobody has measured their accuracy separately. What should happen before the change?
48. [D4] Weighbridge tickets list individual bag weights and a stated net total. Reconciliation discovers, weeks after release and after settlement has already run, that the two sometimes disagree by several tonnes. What should the extraction produce so that the disagreement surfaces at extraction time instead?
49. [D5][select-2] High-confidence extractions are now processed without human review, and they account for roughly 80% of volume. The team wants to keep measuring the true error rate of that automated path without re-reviewing everything it emits. Which two properties should the audit sample have? Select two.
50. [D4] Validation fails on `container_seal_number` for 60 consignments, and the loop retries each of them three times before giving up. Investigation shows all 60 moved as break-bulk cargo, which uses no containers and therefore carries no seals at all. What is the right response?
51. [D5] An inspection certificate records moisture content at 12.4%. The fumigation record for the same lot, issued the same day by a different inspector, records 13.1%. Both documents are authentic, neither is obviously superseded, and settlement tolerances turn on this figure. What should the pipeline emit?
52. [D4] The pipeline validates every extracted record in code after the model returns it, on top of the `tool_use` schema that already constrains the shape. An engineer proposes deleting that validation layer as duplicated effort, noting that the schema already enforces types, required fields and enum membership. Which response is correct?
53. [D2] A `release_to_settlement` tool rejects a consignment because its inspection certificate expired 40 days ago and policy permits 30. The tool returns `"Operation failed"`. The agent retries six times over four minutes, then escalates to a human who reads the policy and declines the release. How should the tool respond instead?
54. [D5][select-3] A `PostToolUse` hook trims the OCR tool's output to plain text plus a page-confidence score. Since it shipped, context pressure has eased markedly — but the review queue can no longer show reviewers where on a page a disputed value was read from, and dispute handling has slowed. Which three statements are sound? Select three.
55. [D4] A batch of 400 consignment documents returns 388 successes and 12 failures, all of them oversized multi-page scans that exceeded the context limit. Results arrived in a different order from submission, and the settlement deadline falls tomorrow. What is the correct recovery?
56. [D5] Settlement disputes require showing which document a figure came from. Records currently carry the extracted values plus a list of the source filenames processed in that run, often twenty or more of them. Brokers cannot tell which file produced which field. What is absent from the record?
57. [D4] The `commodity_grade` field is an enum of the six grades in the current standard. Inspectors on older certificates sometimes wrote regional grade names that map to none of the six, and the model currently picks whichever of the six is closest without comment. Downstream pricing then applies the wrong band. What should the schema do?
58. [D2] Document type must be classified before any commodity-specific extraction tool runs, since the extraction tools differ by type. A prompt instruction achieves this roughly 90% of the time; the other 10% extract against the wrong schema and fail validation further downstream. What configuration guarantees the ordering?
59. [D5][select-2] A broker's clarification thread about one consignment has run to 74 turns and 62,000 tokens. It contains an agreed moisture tolerance, two amended quantities, and a great deal of scheduling chatter about vessel timings. Which two moves preserve what matters? Select two.
60. [D4] Semantic errors — a grade recorded against the wrong lot, a tonnage contradicting the weighbridge line — still reach downstream systems at roughly last year's rate, though JSON parse failures have sat at zero all year. A team lead proposes abandoning `tool_use` schemas, arguing that they plainly did not help. What is wrong with that reasoning?


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
`{CS, CG, CI, SDE}` is **infeasible** — Customer Support would be the sole D1-primary block and D1 needs
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

1. [D1] Policy requires `get_customer` to return a verified account before any credit is applied. Production logs show the agent sometimes calls `issue_credit` using only the account number a caller reads out over the phone, and on eleven occasions this quarter the credit landed on a different customer with the same surname. What change fixes this?
2. [D2] Two tools sit side by side: `lookup_meter_reading` ("Gets meter data") and `lookup_billing_period` ("Gets billing data"). Both accept an account number and a date range. Callers asking why a bill rose are routed to the billing tool, which returns totals but no consumption figures, so the agent cannot explain the increase. What is the first fix?
3. [D1] A caller asks for a tariff change to be backdated to the date they first enquired, three weeks before the switch actually completed. Policy covers backdating for retailer error and for cooling-off cancellations, and is silent on enquiry dates. The agent holds every account fact it needs. What should it do?
4. [D5] `get_customer` returns three accounts matching the name and postcode the caller gave: one closed last year and two active at neighbouring addresses on the same street. The caller is still on the line and has not volunteered any further identifier. Two of the three share a surname with the caller. What should the agent do next?
5. [D1][select-2] Cases currently reach the human queue as an account number plus a one-line free-text note. Agents there report re-asking callers for facts the bot already collected, and average handling time after transfer has risen sharply this quarter. The queue currently receives about ninety transfers a week. Which two changes address the cause? Select two.
6. [D2] A `preview_account_closure` tool returns impact details plus a confirmation token, and `execute_account_closure` requires that token as a parameter. An engineer proposes generating the token client-side from the account number and a timestamp, so the preview call can be skipped when the agent already holds both. Why does that break the guarantee?
7. [D1] One caller raises three things: a direct debit taken twice last month, a tariff change scheduled for April that never applied, and a request to close a second property's account. None of the three depends on the others. The agent works through them strictly in turn and the call runs long. Which approach should it take?
8. [D2] `issue_credit` refuses a goodwill credit because the amount exceeds the £50 ceiling the agent's tier permits. The tool returns `{"isError": true, "message": "Request failed"}`. The agent retries four times over two minutes and then tells the caller the system is unavailable. How should the tool respond instead?
9. [D1] The orchestrator returns to the caller as soon as a response contains any text block. On requests needing two lookups, callers get the agent's narration of what it intends to do, and the second tool never runs. `stop_reason` on those responses reads `tool_use`. What is the defect?
10. [D5] Forty turns into a complex billing dispute, the agent refers to "the goodwill amount we discussed" rather than the £38.50 agreed at turn six, and to "the disputed period" rather than 12 March to 4 April. Summarisation is compressing the history as the conversation grows. What preserves the detail?
11. [D1][select-3] A meter-data service times out intermittently. The billing subagent currently returns the bare string "lookup failed" to the coordinator, which cannot tell a timeout from a rejected account number and so treats both identically. The subagent has already retried twice on its own before giving up. Which three elements belong in the error it returns instead? Select three.
12. [D2] A batch-adjustment tool can apply credits across many accounts in one call. Last month a mis-scoped run credited 1,400 accounts before anyone noticed. Policy now states that any adjustment touching more than 25 accounts requires supervisor approval. The rule currently lives in the agent's system prompt. What actually enforces it?
13. [D1] Of the three issues a caller raised, the agent has resolved two. The third needs a meter reading from a service that has been unavailable for the entire call, and the retry budget is now exhausted. The caller is still holding on the line. What should the agent's response do?
14. [D2][select-2] One engineer wants to trial an experimental demand-forecast MCP server for a fortnight without changing anyone else's setup, while the team's four production servers must stay byte-identical for all forty operators and visible in code review. Tools from every configured server are discovered together at connection time. Which two statements are correct? Select two.
15. [D1] A specialist billing subagent is spawned to investigate a disputed charge. It comes back asking for the account number — which the caller supplied twenty turns earlier and which sits in the coordinator's own history. The prompt the coordinator sent read only "investigate the disputed charge on this account." What is the fix?
16. [D3] The fares package has its own `CLAUDE.md` requiring every monetary value to be handled in minor units. The repository root `CLAUDE.md` says decimals are acceptable where precision is documented. A developer assumes the nearer file wins inside that package. What actually happens when Claude works on a fares file?
17. [D3] The root `CLAUDE.md` has grown past 400 lines. It mixes naming and error-handling standards that genuinely apply everywhere with a concession-eligibility release checklist, a fare-table migration procedure, and gate-firmware deployment steps. Nobody can find anything any more, and every session pays for the whole file. What is the appropriate revision?
18. [D3] A single-file fix arrives with a stack trace pointing at the exact line and a one-line reproduction. The team's rule, written after a costly migration went wrong, is to use plan mode for everything. The fix takes twenty minutes; producing and reviewing its plan takes forty. What does the rule get wrong?
19. [D3] A `/fare-lint` command ships in the repository and every engineer receives it on clone. One wants to run it against a single fare zone at a time rather than editing the command file before each run, so the zone has to arrive at invocation. What does the command file need?
20. [D5][select-2] Standardising fare-rounding across the monorepo needs a discovery pass over roughly 200 call sites before any edit is written. Run in the working session, that pass fills most of the context with match listings, and the design discussion that follows is noticeably vaguer. Which two statements are correct? Select two.
21. [D3] A reviewer asks where a skill's tool scoping is configured. One engineer proposes the project's `.mcp.json`, alongside the server definitions; another suggests the root `CLAUDE.md`, since it loads every session. Neither is correct. The skill currently runs with no scoping at all and has `Bash` available to it. Where does it belong, and what does that key actually do?
22. [D3] The repository ships a `/commit` skill enforcing the team's message format. One engineer wants a stricter local variant under that same command name — appending the transit ticket reference from the branch — with nothing changing for anyone else. She creates `~/.claude/skills/my-commit/SKILL.md` and now sees two entries in the menu.
23. [D5] Eleven hours into cataloguing undocumented fare rules, the agent begins describing "typical rounding conventions" rather than the specific rules it identified in hour three, and two later summaries contradict its own earlier findings. Nothing has crashed and the session is still running. The scratchpad question has come up twice before and was deferred each time. What addresses this?
24. [D3] You ask for a caching layer over the concession-eligibility service, a domain you do not know well. The first three generated versions each miss a different requirement: invalidation on rule changes, behaviour when the cache is unavailable, and per-operator isolation. Each fix disturbs the last. What is the effective move?
25. [D3][select-3] Your `.claude/rules/` directory has grown to fourteen files. A developer notices that a session touching one fares-engine file loaded only two of them, and asks whether the other twelve were skipped in error. Each rule file carries a `paths:` list in its YAML frontmatter. Which three statements are correct? Select three.
26. [D5] A gate-fault investigation thread has run to ninety turns. It contains a confirmed firmware version, two station identifiers where the fault reproduces, an agreed rollback threshold, and a great deal of discussion about maintenance windows. The window is filling. Roughly sixty of the ninety turns are scheduling talk. What should be kept, and how?
27. [D3] An engineer objects to moving the overnight client-regeneration job onto the Message Batches API, arguing that batch requests cannot define tools and the job needs a schema-lookup tool partway through its analysis. The job runs unattended at 02:00 and nobody reads its output until morning. What is the accurate position?
28. [D3] A transformation converting legacy zone strings into the new fare-zone structure is described in prose. Each run produces a differently shaped result: sometimes nested objects, sometimes flat keys, sometimes zones sorted differently. Two rounds of more detailed prose have not settled it. What most effectively anchors the transformation?
29. [D5][select-2] A review pass over a 70,000-token bundle of gate-service diffs reliably comments on the first files and the concluding summary, while changes sitting in the middle of the bundle go unmentioned. Three runs have skipped the same middle material. Which two changes address the cause? Select two.
30. [D2] `calculatePeakSurcharge` is being renamed. It is re-exported from the fares package's index as `peakSurcharge`, and a compatibility module wraps it again as `applyPeakRate`. An engineer greps for the original name, finds eleven call sites, and reports that as the full blast radius. What did that miss, and what is the right approach?
31. [D1] The coordinator's prompt reads: "Step 1, list the files in the module. Step 2, open the first ten. Step 3, write one paragraph per file." Onboarding notes come back uniformly shallow, and when a module holds forty files the notes still describe exactly ten. What should change?
32. [D2] The cleanup worker has accumulated seventeen tools as successive grant projects added integrations — four that fetch records, three that write them, several near-duplicates for provenance lookups. It picks the wrong one often enough that its output is no longer trusted. The exploration worker, holding five role-scoped tools, selects correctly. What should change first?
33. [D1] Every incoming loan agreement goes through the same review: extract the parties and dates, check insurance clauses against a standard set, verify conservation requirements, then produce a fixed-format summary. The steps never vary and the museum's registrar needs identical structure each time. Roughly forty agreements arrive each month and no two describe the loan identically. Which decomposition strategy fits?
34. [D2][select-2] The coordinator spends several turns per task calling `search_accessions` with guessed department names, just to establish what collections the catalogue contains before it can ask anything useful. The catalogue publishes a stable structured index of departments, record counts and field schemas. Which two statements about the two primitives are correct? Select two.
35. [D1] The exploration worker returns findings as running prose and separately lists the files it opened. When the coordinator assembles an onboarding brief, a reviewer spot-checking twelve statements finds four attributed to a file that does not contain them. Three briefs this quarter have come back for the same reason. What is the root cause and the fix?
36. [D2] Asked to explain how conservation treatments reach the public catalogue, the agent begins by reading every file under the conservation module — 180 of them — before doing anything else. It exhausts most of its context on files unrelated to publication and its eventual answer is vague. What should it have done?
37. [D3] The cleanup worker runs from a nightly scheduled job that must exit without a terminal and emit machine-readable output for the tracker. Today the job hangs until the runner's timeout, and on the occasions it is run by hand its output is prose. Which pair of changes fixes both faults?
38. [D1][select-3] A synthesis worker returns an onboarding brief covering three of the four subsystems the request named; the digitisation pipeline is missing entirely, and the exploration logs show it was never examined. The coordinator holds the draft and the request. Which three statements describe the correct architecture? Select three.
39. [D2] The provenance service drops a connection roughly once in fifty calls and succeeds immediately on retry. The scaffolding worker currently surfaces every one of these to the coordinator, which pauses the run, inspects the error and re-dispatches. Throughput has halved. The worker's own retry succeeds on the second attempt in every observed case. Where should this be handled?
40. [D1] The team now routes generated code to a second instance for review. To improve that review, the second instance is given the generator's full conversation — reasoning, rejected alternatives and all — on the argument that context makes a reviewer better informed. Defects still reach production at the previous rate. Why?
41. [D1][select-2] Two exploration workers were dispatched to map how the catalogue reaches the public website. Both independently traced the same rendering layer in depth; neither touched the export scheduler or the image derivative service. Tokens were spent twice on one area and nothing on two others. Which two changes fix this? Select two.
42. [D2] Telemetry shows the coordinator issues `get_accession` and then, in a later turn, `get_conservation_history` for the same object on almost every cleanup task. An engineer proposes a composite tool returning both. Another argues the pairing should stay two tools. Both tools are called on nearly every task, always in the same order. Which consideration decides it?
43. [D1] The team wants a name for what it has built: one coordinator observing every interaction, specialist workers that never address each other, and all results returning through the centre for aggregation and error decisions. A new engineer asks what the arrangement is called and why it is preferred here. Which answer is correct?
44. [D3][select-2] A three-hour session has finished analysing the digitisation pipeline's dependency graph. The team now wants to compare two restructuring approaches — extracting a shared derivative service, or keeping derivation inline — with neither comparison influenced by the other's reasoning. Which two statements are correct? Select two.
45. [D1] A reviewer proposes giving all three worker types the full tool catalogue, arguing that a worker blocked for want of a tool wastes a round trip and that the coordinator can always tell each one what to use. Each worker type currently holds between four and six tools. What is wrong with that reasoning?
46. [D4] Extraction currently asks in the prompt for JSON matching a documented schema. Most outputs parse cleanly, but some arrive wrapped in a markdown fence and a few carry a preamble sentence before the object. An engineer proposes adding a JSON repair library. What removes the problem at its source?
47. [D4] Two requirements arrive together: every response in this reviewer session must stay in a formal, regulator-facing register, and this particular batch summary must come in under 200 words. An engineer puts both into the system prompt. The reviewer will process about forty more batches in the same session. What is wrong with that?
48. [D4] The prompt instructs the extractor to "flag anything unusual in the deviation narrative." It now flags every narrative containing an unfamiliar abbreviation or a long sentence — around forty per batch — burying the handful describing an unrecorded process departure. How should the criterion be rewritten?
49. [D4][select-2] A single pass over a 40-page executed batch record produces detailed extraction for the first few process steps, thin coverage of the middle, a missed out-of-range yield figure, and one in-process check flagged in one step yet accepted in another. Which two changes address the cause? Select two.
50. [D4] Validation rejects a certificate of analysis because `assay_result` came back as "98.7 %w/w" where the schema wants a number and a separate unit field. The pipeline retries with the instruction "try again, the output was invalid." Two of three attempts fail the same way. What should the retry carry instead?
51. [D5] Reviewer capacity covers about 20% of daily volume. The team wants that capacity aimed where it does the most good. Extractions currently carry a single confidence figure per document, self-reported by the model and never checked against anything. Extraction volume is roughly 1,800 documents a day across four record types. What should the routing be built on?
52. [D4] An operator works through a batch queue conversationally. The system prompt sets a formal, regulator-facing register and requires every uncertain field to be named. Both hold early. By turn fifteen the replies are chatty and uncertainties go unmentioned, though the session is only about 3,000 tokens. What is the root cause?
53. [D4] Every extraction summary returned to the review interface opens with a variation of "Certainly — I've reviewed the batch record and here is what I found." Reviewers processing 200 a day want the content to start immediately. The opener costs about fifteen words before any finding appears. Which technique removes the opener most reliably?
54. [D5][select-3] A regulator asks the pipeline to demonstrate, for one released batch, where each critical parameter came from. Records currently hold the extracted values plus a list of the documents processed for that batch. Nobody can show which document produced which value. Which three changes fix this? Select three.
55. [D4] A revised extraction prompt is ready for an archive of 9,000 historical batch records. Submitting the whole archive to the Message Batches API and iterating on the results has cost two full cycles already, each discovered a day later. What should happen before the next full submission?
56. [D5] As review conversations pass fifty turns, both latency and per-turn cost climb steadily, although the model's replies are no longer than they were at turn five and the review interface has not changed. Token usage per request has roughly tripled between turn five and turn fifty. What explains the increase?
57. [D4] A synthesis step has stalled. Two of its five input categories are ambiguous, and it has queued a clarification request to the coordinator for each before producing anything at all. Throughput across the pipeline has dropped while it waits. The coordinator has not responded to either clarification request. What should it do?
58. [D4][select-2] A single prompt asks the model to extract every deviation from a batch record, classify each by criticality, and draft a quality-review memo. Deviations from later sections are frequently missed, and the criticality ratings sometimes contradict the memo's own narrative. Which two changes address this? Select two.
59. [D4] Asked to propose validation checks for a new deviation-report schema, the assistant returns twelve. Seven duplicate checks the quality system already performs at intake, and reviewers now skim the list rather than reading it. The quality system's intake checks are documented and stable. What most effectively removes the duplication?
60. [D4] Two noisy finding categories were switched off a month ago and their prompts have since been rewritten. Reviewer engagement with the four remaining categories has recovered to its former level. The team wants the two back. The two categories accounted for about a third of all findings before they were switched off. What should govern the decision?


---

## Exam 16 — Generated 2026-08-11

**File:** `mock-exams/CCA-Prep_MockTest-16_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions) — 47 single-answer + 13 multiple-response
**Scenarios drawn:** Customer Support Resolution Agent; Multi-Agent Research System; Developer Productivity with Claude; Claude Code for Continuous Integration
**Attempt date:** Not yet attempted
**Score source:** Pending
**Total score:** Pending

**Purpose:** generated the same evening as a compute expiry, and the concern was put on the record first —
Exams 12, 13, 14 and 15 were already unattempted with the sitting on 2026-08-18. Ram's call, and generation
is cheap against losing the compute. **Five papers are now unattempted: 12, 13, 14, 15 and 16.**

What this paper adds that the others cannot: **it is the flattest domain load the scenario bank permits.**
No block carries more than five questions of any one domain. Exam 15's extraction block ran twelve of its
fifteen questions in D4, and Exam 14's margins were 3/3/3/4. A block that is 80% one domain lets the
candidate settle into a single mode for fifteen questions, which the real exam's blocks do not reward.

**Quota:** base weights — D1 16 / D2 11 / D3 12 / D4 12 / D5 9. No confirmed-weakness adjustment (Exam 9
weakest D2 attempted 2026-08-09, Exam 11 weakest D5 attempted 2026-08-10 — different domains by attempt
chronology, so the two-consecutive gate is not met).

**Scenario draw — solved as a constraint problem over all 15 possible 4-of-6 sets, not chosen by hand.**
Counts entering this paper: Structured Data Extraction 10, Developer Productivity 10, the other four 9
each. The rotation preference (the four least-used) is `{CS, CG, MARS, CI}` — but that set was already
used by Exam 7, so rotation and the never-used-combination rule conflict here for the first time. Ten of
the fifteen sets are used across Exams 2–15. Of the five unused, `{CG, CS, DP, MARS}` is **infeasible**:
it contains no D4-primary block at all, and D4 needs twelve questions. The four survivors all level the
rotation to 9–11, so rotation could not discriminate between them either; the tiebreak used was the
minimum-maximum-cell criterion — the draw in which no block must absorb more than five questions of a
single domain. Only `{CS, MARS, DP, CI}` achieves 5; the others need 6 or 7. Rests Code Generation and
Structured Data Extraction, both of which Exam 15 drew. Post-Exam-16 spread: Customer Support 10,
Multi-Agent Research 10, Developer Productivity 11, Claude Code CI 10, Code Generation 9,
Structured Data Extraction 10.

**Block x domain allocation:**

| Block | Scenario | Primary domains | Allocation | Margin |
|---|---|---|---|---|
| 1 | Customer Support Resolution Agent | D1, D2, D5 | D1 5 / D2 3 / D5 3 · D3 2 / D4 2 | 1 |
| 2 | Multi-Agent Research System | D1, D2, D5 | D1 4 / D2 3 / D5 4 · D3 2 / D4 2 | 1 |
| 3 | Developer Productivity with Claude | D2, D3, D1 | D1 4 / D2 4 / D3 4 · D4 3 / D5 0 | 1 |
| 4 | Claude Code for Continuous Integration | D3, D4 | D3 4 / D4 5 · D1 3 / D2 1 / D5 2 | 1 |

Every block satisfies gate 4 with a margin of exactly 1, which is what "flattest" costs: the allocation
sits right on the constraint rather than comfortably inside it. Totals D1 16 / D2 11 / D3 12 / D4 12 / D5 9.

**Correct-answer letter pre-plan (fixed before any option was drafted, single-answer items only):**

| Block | Short letter | Sequence | Tally |
|---|---|---|---|
| 1 | — | `BDACDBACBDCA` | A3 B3 C3 D3 |
| 2 | — | `CADBACBDABDC` | A3 B3 C3 D3 |
| 3 | — | `DBCABDCADCAB` | A3 B3 C3 D3 |
| 4 | A | `CDBCADBDCBA` | A2 B3 C3 D3 |

Exam-wide A11 B12 C12 D12 = 47. Because 13 of the 60 items are multiple-response, three blocks hold 12
single-answer items (which divide evenly by four, so no short letter is needed) and block 4 holds 11.
Achieved sequences match the pre-plan **exactly** — verified mechanically in `WIP-EXAM16/assemble.py`,
which fails the build on any divergence rather than reporting it afterwards.

**Item formats:** 47 single-answer + 13 multiple-response (9 select-2-of-5, 4 select-3-of-6), scored
all-or-nothing. Same share as Exams 14 and 15, so the three papers stay comparable on format.

**Professor's Note consumed — Intent for Exam 13** (written after Exam 11 scored 55/60 on 2026-08-10; still
the most recent note, since nothing has been scored since). All three named sections are covered, each in
a shape the learner has not seen:

| Note item | Where | Shape used |
|---|---|---|
| D2 §2.8 composite vs prompt bundling — missed on Exams 5, 8, 10, 11 | Q38 | select-3, starting from a team that **already built** the composite and is now paying a second-order cost (ban-list BF-2 approved re-frame). The corpus's own slogan is one of the options to evaluate rather than recall. |
| D1 §1.18 evaluator-optimizer vs context isolation | Q59 | select-2 direct disambiguation — two proposals, name each pattern, with the two names crossed over as distractors. |
| D5 §5.8 over-escalation of a resolvable ambiguity | Q3 | multiple-match disambiguation with "escalate to a human at once" as the trap option. |

**Fresh-section coverage:** all four D3 §3.7 subsections appear — the least-used sections in the whole
corpus at 2–3 prior uses each. §3.7.1 interview pattern Q32, §3.7.2 test-driven iteration Q49, §3.7.3
concrete I/O examples Q36, §3.7.4 batching interdependent feedback Q57. **58 distinct corpus sections**
carry the whyRight citation across 60 questions; only D2 §2.3 and §2.9 appear twice, which is forced —
D2 has nine sections and an eleven-question quota — and each pair tests a different facet (§2.3
business-rule error Q2 vs empty-result-versus-access-failure Q56; §2.9 Grep-vs-Glob Q31 vs the
Edit→Read+Write fallback Q34).

**Fidelity gates — computed by `tools/archetype_gate.py` against the shipped HTML, not hand-tallied.**
All seven pass:

| Check | Result |
|---|---|
| 1 · no invented names | 0 flagged |
| 2 · letter tally (SA only) | A11 B12 C12 D12 |
| 3 · word counts | stem min 43 / median 54 / max 62; option max 25 (caps 95 and 35) |
| 4 · block vs primary domains | holds in all four blocks |
| 5 · inline code/config token rate | 53/257 options = 20.6% (target band 20–25%) |
| 6 · multiple-response validity | 13 well-formed MR items |
| 7 · archetype collision | **0** stems at/above 0.40 Jaccard against **893** prior stems (Exams 2–15); 0 intra-paper; top closing formula 2×, top opening formula 1× |

**The gate caught six real defects before shipping**, all in one pass: four invented-name flags the
generic-framing rule should have caught during drafting (`Briefings` and `Yesterday` as sentence openers
that appear nowhere in lower case, and `Monday` twice — weekday names are not in the allowed-proper list);
a stem median of 46 against the binding 50–55 band, fixed by adding concrete situational detail to 49
stems rather than padding; an inline-token rate of 14.4% against the 15–30% floor; a multiple-response
stem (Q59) whose select-count was phrased "Select the two named patterns", which the validity check
cannot read — reworded to close on "Select two."; and two questions in block 2 closing on the identical
sentence. Every fix is recorded as an asserted fragment replacement in `WIP-EXAM16/patch_gates.py`, so
the edit set is auditable rather than a silent rewrite.

**Industry territory — all four new**, generically framed per the naming rule: university student
services (tuition instalments, enrolment, accommodation charges); fisheries stock assessment (survey
reports, quota filings); a payroll and time-and-attendance platform (award interpretation, shift
penalties, leave accrual); and online grocery fulfilment CI (picking routes, substitution rules,
chilled-chain compliance).

**Verified in a browser through the page's own event handlers** (localhost:8768): landing card with the
verbatim rotation-disclosure line; single-answer lock-and-reveal on both the correct and the wrong path,
every rationale carrying its citation; post-lock clicks ignored; multiple-response toggle on and off with
in-progress selections persisted under a `pending` key so a mid-selection resume works; commit at exactly
N; the wrong-path multiple-response feedback including the "belongs in the answer" state for correct
options that were not picked; all three resume branches (fresh → landing, partial → first unanswered,
complete → results); Back disabled on question 1, Next disabled until answered, "Show my results" in the
final slot; jump map with 60 chips across four block rows carrying answered/current/multi states; the
running-accuracy pill exact at the 620/900 threshold — 31/45 = 68.889% renders green `pass`, 30/45 =
66.7% renders red `fail`; the pass boundary exact at 42/60 = 730 "Above pass line" and 41/60 = 715 "Below
pass line"; print-all rendering all 60 questions with 4 block headers and 180 locked rationale rows before
tearing its container down; and the export JSON carrying `item_formats`, per-question `type`
(`single` / `multi-2` / `multi-3`) and comma-joined `selected` letters. Console clean on an organic
session apart from a favicon 404. `localStorage` was cleared afterwards, so the file ships unstarted.

**One cosmetic defect found in Exam 15 while building this — not fixed.** Exam 15's four block narratives
contain literal `<code>` tags in the DATA payload. The template escapes HTML before converting backticks,
so those render to the reader as visible `<code>` text rather than styled code. It affects the four
narrative cards only, never a stem, option or rationale. Left alone because Exam 15 is unattempted and Ram
may still sit it; recorded here so a future session can decide. Exam 16 uses backticks throughout and was
checked for the same fault.

### Questions Used (deduplication ledger for Exam 17+)

1. [D1] Escalations reach the adviser queue as a one-line note reading `escalate: student disputes accommodation charge`. The adviser who picks it up cannot see the chat transcript, so they re-ask for the student number, the disputed amount and what the agent already offered. Handling time after escalation averages eleven minutes. What should the escalation payload carry instead?
2. [D2] A withdrawal after the census date cannot be credited, and `apply_fee_credit` signals this by returning the bare string `operation failed`. Traces show the agent re-calling it four times, then escalating, on each of the roughly sixty late withdrawals that arrive per term. The refusal is a policy outcome that no retry can change. What is the correct tool-side fix?
3. [D5] Two records come back from `get_student` for the name given over the phone — same surname, same first initial, different entry years. The agent takes the one with more recent activity and applies a credit to it. Reconciliation later shows the credit landed on the wrong record. What should the agent have done?
4. [D1][select-2] One message contains three asks: a duplicate instalment charge, a bursary never applied, and a withdrawal from one module. The agent works them strictly in order, re-fetching the same student record before each, and spends 14 tool calls where a single-issue case of the same kind takes three. Select two changes that address this.
5. [D4] First-contact resolution sits at 57% against the 80% target, and the sampled transcripts show one consistent pattern: routine instalment-date changes get escalated, while unusual fee-waiver appeals are attempted alone and decided wrongly. The system prompt says only `escalate complex cases`, and has said so since launch, with no examples attached. Which change addresses this?
6. [D2] `lookup_enrolment` and `get_student` each accept what looks like an eight-digit identifier, and each carries a one-line description. Routing logs show `get_student` called for module-registration questions in 38% of cases. A colleague proposes a small classifier in front of the tool layer, trained on three months of routing logs. What should you do first?
7. [D1] The billing back end times out on roughly one call in twenty. When it does, the subagent handling the case returns the string `lookup unavailable` to the coordinator and nothing more, whatever the underlying cause turned out to be. The coordinator cannot tell whether to retry, proceed on partial data, or escalate. What should the subagent return?
8. [D5] A hardship arrangement agreed at turn 6 — four instalments of £310, the first due 12 October — appears at turn 40 as `a payment plan was discussed`, and the agent then quotes a different figure back to the student on the call. Raising the summarisation threshold only delays the loss. Where does the fix belong?
9. [D3][select-2] The team maintains this agent in a repo where `/audit-refunds` routinely emits several thousand lines of exploration, after which the session loses the thread of its original task. They also want that command unable to modify anything in the working tree, since it is often invoked during a live incident. Select two frontmatter settings that address these.
10. [D1] A coordinator was written to route billing questions to one subagent type and enrolment questions to another. In production it answers everything itself, competently, and has not spawned a subagent once in six weeks of traffic. Its system prompt describes both subagent types at length; its `allowed_tools` reads `[get_student, lookup_enrolment, apply_fee_credit]`. What is the root cause?
11. [D2] Fee credits above £2,000 require finance sign-off. That instruction lives in the system prompt, and a term-end audit finds four credits above the line, totalling £11,400, applied without one. Nobody disputes that the agent usually complies. What makes compliance certain rather than usual?
12. [D4] The agent opens warm and specific. By turn 9 it produces generic reassurance and ignores the plain-language rule its system prompt sets out. The whole conversation is 3,100 tokens against a window two orders of magnitude larger, and the same prompt behaves correctly in fresh sessions and in short ones. What is the most likely explanation?
13. [D5][select-3] A 90-minute session has reached 71,000 tokens and is still open. It holds a disability adjustment declared in the opening minutes, three exact instalment figures, a long stretch of general reassurance, and the last few exchanges settling the current request, which turns on one of those figures. Select three elements of the right context strategy.
14. [D3] The repo's `CLAUDE.md` has grown past 400 lines and now mixes naming standards that apply everywhere with a release checklist, a data-migration runbook and a long incident-review procedure. All of it loads in every session, so a change touching one module still carries the migration runbook. What should the team change?
15. [D1] A loop wrapping the agent occasionally hangs after a tool result comes back. The implementation decides whether to continue by scanning the response text for phrases such as `anything else` and `all set`, stopping when it finds one; the hang always follows a turn where the model was plainly mid-task. What should drive that decision instead?
16. [D1] The coordinator's prompt is a numbered script: search four named databases, open the first ten hits from each, summarise every hit in 120 words, pass the summaries on. The briefings come back uniform and shallow, and one of them missed a fishery closure that happened mid-survey and changed the picture entirely. What should change?
17. [D5] The final briefing states that recruitment has fallen 18% since the previous assessment, with nothing attached to say where that came from. Two upstream agents each saw the figure in a different filing. The report agent lists every document consulted in a bibliography at the end. What does the pipeline need?
18. [D2][select-2] The synthesis subagent carries 19 tools, three of them search tools and two document loaders it has no legitimate use for. It picks wrongly on a noticeable share of turns and has started running open-ended searches of its own instead of synthesising what it was given. It does need frequent single-fact confirmations. Select two changes.
19. [D1] Inputs reach the synthesis subagent as one concatenated block of prose. By the time the briefing is written, page numbers and survey years have disappeared, and two figures from different years end up merged into a single sentence. The coordinator still holds both figures, correctly separated and dated, in its own history. What is the fix?
20. [D4] Given the request `summarise what we know about the northern stock`, the synthesis subagent replies with five questions: which stock unit, which years, whether to include recreational catch, which assessment model, and what length. Analysts abandon the request rather than answer, and roughly a third of requests now end this way. What should it do instead?
21. [D5] Synthesis receives 78,000 tokens per run, assembled from four subagents in a fixed order. It uses the opening summaries and the closing conclusions well, but omits a gear-selectivity finding sitting around the 40,000-token mark that the analysts consider decisive. The finding is present, correctly worded, and sits under its own heading. Where should the fix be applied?
22. [D2] A maintained community MCP server already covers the unit's reference-manager integration and works well. A second server is now needed to expose an internal quota-allocation model whose rules no external product implements. A colleague argues that building anything custom repeats the mistake of reinventing standards, citing the reference-manager decision as precedent. How should you evaluate this?
23. [D1] Synthesis returns a briefing that covers biology and catch history in real depth but says nothing at all about management measures, which the coordinator's own quality criteria require. The search and document subagents are idle and available. Nothing failed, no tool errored, and every subagent reported completion. What should the coordinator do?
24. [D5][select-3] A four-hour run dies eight minutes from the end, after the search and document passes have both completed and synthesis is part-written. Restarting repeats every search and every document pass from the beginning, at full cost. The team wants a restart to resume instead. Select three elements of the right design.
25. [D3] Three researchers get consistent adherence to the unit's citation-format convention from Claude Code. A fourth, newly joined, does not. All four work in the same cloned repo on the same branch, and the convention is written down somewhere, since three of them follow it without being reminded. What is the first diagnostic step?
26. [D4] One task has the document subagent compare five survey series across three metrics and rank the stocks; it gets the arithmetic wrong on roughly a fifth of runs, usually by transposing two of the series. Another task, rendering a species name in the local vernacular, is always right. What distinguishes them?
27. [D1] Of the five source categories the coordinator asked for, three returned and two timed out. Enough arrived for a defensible briefing on those three. As written, the synthesis subagent returns an error whenever its inputs are incomplete, so nothing is produced at all. What should it do?
28. [D5][select-2] A government survey reports 40% growth in one stock; an industry analysis reports 12%. Both are credible, both were published within the last six months, and their methods differ substantially. The document subagent has to hand something to the coordinator. Select two things its output should do.
29. [D2] Three searches on different subtopics are dispatched in a single turn. The orchestrator appends the three results in whatever order they finish and carries nothing back from the originating request. The agent then attributes one result's contents to a different query, and the briefing repeats that mix-up downstream. What was omitted?
30. [D3] A long investigation session is approaching its window limit. It holds precise quota figures, three survey years, and a list of documents already ruled out; the next phase depends on those exact values. Someone proposes running `/compact` and carrying straight on in the same session rather than starting over. How should you evaluate that?
31. [D2] A deprecated `calcPenaltyRate` helper has to be located everywhere it is used before it can be removed. The agent ran `Glob` with the pattern `**/calcPenaltyRate*`, reported two matches, and the removal that followed broke eleven call sites at build time across four packages. Why did the search come back clean?
32. [D3] A request to add a leave-accrual engine has produced three generated versions. Each missed something different: pro-rata accrual for part-time staff, the carry-over cap, and the treatment of unpaid leave. The developer asking does not know the award rules well, and neither does anyone else currently on the team. What is the better next move?
33. [D1][select-2] Nobody knows which parts of the awards module lack tests, and the coverage report has not run in a year. The brief is `add comprehensive test coverage`, over eight years of accumulated history and four teams' worth of conventions. A colleague proposes a fixed six-step pipeline settled before any code is read. Select two properties the right approach has here.
34. [D2] An `Edit` call fails on a rates file: the anchor `return base * multiplier;` appears in four functions and the change is needed in exactly one of them, the overtime branch, which is the third occurrence in the file. Retrying with the identical anchor fails the same way. What is the sanctioned next step?
35. [D4] A doc-comment check in the agent raises roughly 40 findings per run. Most of what it flags is accurate but terse. The rule it works from reads `check that comments are accurate`. Developers have stopped reading the output entirely, and dismissals now run at about 90%. Which rewrite of that rule fixes the behaviour?
36. [D3] A transformation that converts legacy timesheet rows into the new shift schema produces a differently shaped result on each run — sometimes nesting breaks, sometimes flattening them, sometimes dropping zero-hour entries. The prose description has been rewritten twice and lengthened both times, without changing the variance at all. What should be added?
37. [D1] The previous session mapped how back-pay recalculation flows through six modules, and building that map took two hours of exploration. Overnight another team refactored three of those six, changing function signatures rather than behaviour. The rest of the map is still accurate. How should today's work continue?
38. [D2][select-3] Months ago the team replaced two frequently co-occurring calls with a single composite tool, and round-trips fell by about a third. A new workflow now needs only the second half of that composite; the agent calls the composite anyway and discards half the payload on every single request. Select three true statements about this situation.
39. [D3] A rates library used by 45 files must be swapped for a maintained replacement whose API differs in three places, one of them a changed return shape. A developer starts in direct execution, intending to switch into planning mode later if the work turns out messier than expected. How should you evaluate that intention?
40. [D4] Requests phrased like `show me how overtime is worked out` route to the code-search server about half the time and to a documentation tool the rest, with no pattern anyone can see. Unambiguous requests route correctly. Twelve examples of clear requests were added last sprint, with no measurable effect on the split. What should be added instead?
41. [D1] A subagent scoped to summarising module dependencies was given `Bash` so it could run one tree command. Traces show it running test suites and, on one occasion, a package install. Its summaries are good. A prompt line telling it not to run tests reduced this without stopping it. What is the fix?
42. [D2] A bulk rename across the monorepo must always be previewed first. The design has `preview_rename` return a token and `execute_rename` require one. During testing an agent ran an execute carrying a token from an earlier, unrelated preview, and the rename went through against files nobody had previewed. Which property of the token was missing?
43. [D3][select-2] Award-interpretation files require decimal-safe arithmetic, the API layer requires a shared error envelope, and test files require fixture factories rather than the inline literals they use today. All three kinds of file sit side by side in every one of the 60-odd feature folders. Select two accurate statements about using `.claude/rules/` here.
44. [D4] Every generated snippet arrives behind two sentences of preamble — `Certainly! Here is the function you asked for.` — which developers strip by hand dozens of times a day across the four teams. A system-prompt line asking for no preamble helped for a fortnight and then quietly stopped helping. What removes it reliably?
45. [D1] Two subagents — one mapping call sites, one drafting the migration — were wired to pass results to each other directly so the coordinator would not have to relay them. Latency improved. Then a failure in the mapper left the drafter working from a half-built list, and nothing in the run recorded that this had happened. What did the design give up?
46. [D3] Each time an author pushes a follow-up commit the review re-runs and posts near-identical comments on code nobody touched, worded slightly differently every time; one pull request now carries 60 of them. A maintainer argues each run should start clean so the review stays objective. How should you evaluate that?
47. [D4][select-2] Validation rejects roughly 40 findings a night because the required `suggested_fix` field comes back empty. Sampling shows these are findings where no mechanical fix exists — the reviewer is describing a design concern. Max retries was raised from 3 to 10 last week with no change. Select two correct actions.
48. [D1] The generation step writes a slot-capacity patch, reasons at length about its edge cases, and concludes the approach is sound. A `review your work carefully` step in the same session agrees. Two of the last four production defects were in code that passed both of those. What change addresses this?
49. [D3] The substitution-rules module mishandles items whose replacement is itself out of stock in the same delivery slot. Three rounds of describing that bug in prose to the generator have produced three partial fixes, each breaking a different case that had previously worked. What is the fastest way to converge on a correct one?
50. [D4] Measured false-positive rates by category: naming 54%, comment style 47%, chilled-chain safety checks 6%, concurrency 15%. Developers have started dismissing every comment the reviewer posts, safety findings included; two chilled-chain findings dismissed last month were later confirmed as real defects. Which action stops the trust bleed fastest?
51. [D5][select-2] A `PostToolUse` hook trims the pick-route lookup down to four fields, and context use per run fell by roughly 40%. Since it shipped, the reviewer no longer flags routes that breach the chilled-chain window — the temperature-band field turned out to be among those the hook drops. Select two sound responses to this.
52. [D3] Findings are emitted as markdown and parsed with a regular expression before being posted as inline comments. About one comment in fifteen lands on the wrong line, and a heading change last month broke posting outright. Each comment needs a file path, a line number, a severity and a suggested fix. What should the pipeline use?
53. [D4] A weekly dependency audit has to be on the platform team's desk by 09:00 at the start of each week, and it runs over about 4,000 packages. Someone proposes submitting it as a batch at 02:00 that same morning, reasoning that batches usually finish inside an hour. What is the correct submission planning?
54. [D1] The coordinator splits each review into three subtasks: correctness within changed files, test coverage of changed files, and style. Every subagent returns clean, thorough work. Two production incidents this quarter traced to interactions between a changed module and an untouched consumer of it, neither of them flagged by any of the three subtasks. What is the root cause?
55. [D4][select-3] The generator proposes 10 test cases per pull request, and roughly 6 of them duplicate scenarios the existing suite already covers. Across last month's 40 pull requests the duplicate share never once fell below half, and the suite itself runs to 1,900 tests. Reviewers have stopped reading the list. Select three sound elements of the fix.
56. [D2] The coverage service is briefly unreachable during a nightly run, and its client returns an empty array — indistinguishable from a genuine zero-coverage result. The review then reports that the changed module has no tests at all, and the author spends a morning proving otherwise. What should the client return?
57. [D3] A review of one queueing function raised three issues: a lock-ordering bug, a retry policy whose correctness depends on how the locking is fixed, and a typo in a log string. A teammate wants all three sent one at a time, on the principle that each request then stays focused. What should you do?
58. [D4] The tool schema for review findings is hand-maintained in one file and a validation class in the pipeline checks the same fields in another. Twice this quarter a new severity level was added to one and not the other, and findings were dropped silently. A code-review checklist item has been proposed. How should you evaluate it?
59. [D1][select-2] Two changes are proposed. First, route the generated patch to a separate critic agent that scores it against the review criteria. Second, give the test-writing subagent only the changed module and its interface, not the whole pull-request conversation. Which two of the following name these patterns correctly, in that order? Select two.
60. [D5] Suggested fixes from the reviewer are accepted 96% of the time overall, measured across eleven finding types and about 300 fixes a week, and there is a proposal to apply the high-confidence ones automatically. Nobody has broken that figure down by type or by module. What should happen before any auto-apply?


---

## Exam 12 — SCORED 2026-08-11

**Score source:** results-json (full per-question data)
**Total:** 53 / 60 correct · estimated scaled 895 / 1000 · pass line 720
**Time:** 2,560s = 42:40 across 60 questions (42.7s/question). The allowance is 120 minutes; **77 minutes
went unused.**

Note on denominators: Exam 12 ran the confirmed-weakness quota (D1 14 / D2 15 / D3 12 / D4 12 / D5 7),
not the base 16/11/12/12/9. Percentages are comparable across exams; raw counts are not.

### Domain Breakdown

| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 14 | 13 | 93% | no |
| D2 Tool Design & MCP | 15 | 13 | 87% | no |
| D3 Claude Code Config | 12 | 10 | 83% | no |
| D4 Prompt Engineering | 12 | 10 | 83% | no |
| D5 Context Management | 7 | 7 | 100% | no |

### Block Breakdown

| Block | Scenario | Correct |
|---|---|---|
| 1 | Code Generation with Claude Code | 13 / 15 |
| 2 | Multi-Agent Research System | 13 / 15 |
| 3 | Developer Productivity with Claude | 14 / 15 |
| 4 | Claude Code for Continuous Integration | 13 / 15 |

Blocks are flat — 13/13/14/13. No scenario is a weak spot.

### The seven misses

| Q | Dom | § | Picked | Key | Time | What the wrong pick was |
|---|---|---|---|---|---|---|
| 1 | D3 | §3.1 | C `.claude/rules/` | A `/memory` | 26s | a fix, before diagnosing which file loaded |
| 6 | D4 | §4.1 | D post-process output | A few-shot examples | 117s | a repair stage bolted after generation |
| 17 | D1 | §1.2 | C give it a retrieval tool | B coordinator passes findings | 93s | wider privileges instead of passing context it already holds |
| 18 | D2 | §2.1 | A missing user message | D `tool_result` keyed by `tool_use` `id` | 25s | protocol mechanics |
| 33 | D2 | §2.5 | B `auto` + prompt rule | A `{"type": "any"}` | 32s | a probabilistic control where a guarantee exists |
| 56 | D3 | §3.4 | B `.claude/rules/` | C `.claude/commands/` | 30s | wrong config location |
| 57 | D4 | §4.11 | B synchronous fallback | A deadline − 24h | 38s | a workaround instead of the planning rule |

### Observations

**1. Five of the seven misses are one error, not five.** Q1, Q6, Q17, Q33 and Q57 all reach for a
compensating mechanism rather than the root-cause fix or the available deterministic guarantee: build a
rules file rather than diagnose; post-process rather than give examples; grant a tool rather than pass
context; `auto` plus an instruction rather than `any`; a synchronous fallback rather than submitting a day
earlier. Those map onto three of the exam's own stated answer heuristics — *fix the root cause not the
symptom*, *deterministic over probabilistic*, *proportionate first response*. **This is one reusable
decision rule, and drilling it is worth more than drilling five sections.**

**2. `.claude/rules/` was chosen wrongly twice on one paper** (Q1 and Q56). It is operating as a default
answer to "where should this live?". The three-way distinction to hold: **rules** = path-scoped
conventions that auto-load on matching files; **commands/skills** = invocable by name; **CLAUDE.md** =
always-on standards. In Q1 the answer was not a location at all — it was a diagnostic.

**3. Speed is not the constraint; confidence is.** Five of the seven misses took under 40 seconds. The
two slow ones (117s, 93s) were considered at length and still wrong. 42:40 of a 120-minute allowance was
used. There is no time pressure at this pace — the errors live in fast, confident answers to
"which mechanism" questions, which is precisely where the compensating-mechanism reflex fires.

**4. The D2 experiment succeeded and should now end.** D2 was CONFIRMED weak entering this paper, which
is why Exam 12 carried +4 (15 D2 questions, the largest D2 quota ever set). Result: 13/15 = 87% — on the
biggest denominator, against a 78.4% all-time D2 mean. The targeted quota did its job.

### Professor's Note — Intent for Exam 17

Written after Exam 12 (attempted 2026-08-11). Based on results-json. **Numbering: "Intent for Exam 17",
not 13 — Exams 13, 14, 15 and 16 were all generated before this score arrived, mirroring the Exam 9→12
skip precedent. Its targeting function therefore cannot reach the papers already on disk; the actionable
part this week is the revision focus below, not the next paper.**

- Misconceptions revealed:
  1. **Compensating mechanism over root-cause fix** — the dominant shape, five of seven misses, spanning
     D1 §1.2/§1.11, D2 §2.5, D3 §3.1, D4 §4.1 and D4 §4.11. Not a domain gap; a decision-rule gap.
  2. **`.claude/rules/` as a catch-all location** (D3 §3.2 confused with §3.1 and §3.4, twice on one paper).
  3. **The tool-result protocol** (D2 §2.1) — results re-enter as `tool_result` blocks keyed to their
     `tool_use` `id`, not as narrated prose. Missed here after also being a targeted section in Exam 13.
- Weakest this paper: **D3 and D4 tied at 83%** — not confirmed, because Exam 11 (the most recent prior
  scored paper by attempt chronology) was weakest at D5. Base quota therefore applies to Exam 17.
- Intent for next paper: within the fixed quota, build items where the plausible workaround is *present
  and attractive* but the root-cause fix is available — that is the exact geometry of all five misses,
  and a paper that omits the tempting distractor will not test it. Give D3's where-does-this-live family
  (§3.1 / §3.2 / §3.3 / §3.4) a three-way discrimination rather than a single lookup. Re-test D2 §2.1 on
  the `id` correlation specifically.
- Watch next: whether the compensating-mechanism reflex disappears when the paper is unfamiliar in shape
  (Exams 14 and 16 carry no recognisable question archetypes), or whether it survives — which would make
  it a genuine reasoning habit rather than a pattern-matching artefact.

---

## Insights Round 3 — 2026-08-11 (fires at 9 scored exams)

Nine exams are now scored. Ordered by **attempt** date, not generation number.

| # | attempted | raw | scaled | mins | D1 | D2 | D3 | D4 | D5 | weakest |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 2026-07-11 | 45/60 | 775 | 736 | 75% | 45% | 75% | 83% | 100% | D2 |
| 5 | 2026-07-11 | 52/60 | 880 | 32 | 94% | 73% | 92% | 75% | 100% | D2 |
| 6 | 2026-07-12 | 49/60 | 835 | 260 | 93% | 73% | 83% | 83% | 71% | D5 |
| 7 | 2026-07-16 | 55/60 | 925 | 325 | 94% | 100% | 83% | 83% | 100% | D3/D4 |
| 8 | 2026-07-28 | 52/60 | 880 | 35 | 94% | 91% | 75% | 75% | 100% | D3/D4 |
| 10 | 2026-07-29 | 54/60 | 910 | 39 | 94% | 82% | 83% | 92% | 100% | D2 |
| 9 | 2026-08-09 | 49/60 | 835 | 42 | 88% | 64% | 92% | 83% | 78% | D2 |
| 11 | 2026-08-10 | 55/60 | 925 | 40 | 94% | 91% | 92% | 92% | 89% | D5 |
| 12 | 2026-08-11 | 53/60 | 895 | 43 | 93% | 87% | 83% | 83% | 100% | D3/D4 |

**Domain trends (all-time mean / last-3 mean):** D1 90.8 / 91.4 · D2 78.4 / 80.4 · D3 84.3 / 88.9 ·
D4 83.3 / 86.1 · D5 93.1 / 88.9.

**1. The band is stable and comfortably above the line.** The last six attempts run 49–55/60, scaled
835–925, against a 720 pass line. The lowest of the nine (775, Exam 4) still passes. Nothing in this
record suggests the exam is in doubt.

**2. D2 has genuinely recovered — retire the adjustment.** Trajectory 45 → 73 → 73 → 100 → 91 → 82 → 64
→ 91 → 87. The 64% (Exam 9, attempted 2026-08-09) reads as the outlier rather than the trend: that paper
was generated 2026-07-19, and the two attempts on either side of it scored 82% and 91%. The confirmed-
weakness quota fired once, put 15 D2 questions on Exam 12, and D2 returned 87%. **Recommendation: no
further D2 adjustment.**

**3. D3 and D4 are the standing weakness, and have been for nine exams.** They have now tied weakest
three times (Exams 7, 8, 12) and **neither has ever been the strongest domain on any paper.** All-time
means 84.3% and 83.3% — the two lowest apart from D2's recovering 78.4%. The last-3 figures (88.9%,
86.1%) are better, so this is a slow improvement rather than a stall, but it is the only place a
meaningful number of marks is still being left.

**4. D5's Exam 11 flag was a denominator artefact, and the rule that produced it needs a caveat.** Exam
11 named D5 weakest at 88.9% — one wrong answer out of 9. Exam 12 returned 100%. D5's all-time mean of
93.1% is the **highest** of any domain. On a 7–9 question domain a single miss moves the percentage by
11–14 points, which is enough to win a weakest-domain comparison outright. **Standing caveat for future
rounds: treat "weakest" on D5 (and on any domain running fewer than 10 questions) as provisional unless
the margin exceeds one question.** The two-consecutive-exam gate already protects against acting on it,
and it correctly did so here.

**5. The finding this round that is not about domains at all.** Exam 12's seven misses concentrate into
one error shape — preferring a compensating mechanism to the root-cause fix or the deterministic
guarantee — that spans four of the five domains. A domain-weighted quota cannot target it, because it is
not located in a domain. **It is targetable through question geometry instead: items where a plausible
workaround is present and attractive alongside the correct root-cause fix.** That is a generation
instruction, and it is recorded as such in the Intent for Exam 17 above.

**6. Timing has no remaining risk.** Excluding the three papers taken across multiple sittings (Exams 4,
6, 7 at 736/260/325 minutes), the five single-sitting attempts run 32–43 minutes against 120. Exam 12
used 36% of the allowance. There is no scenario in which the clock is the binding constraint, which means
slowing down on the four or five items that feel obvious costs nothing.


---

## Exam 13 — SCORED 2026-08-12

**Score source:** results-json (full per-question data)
**Total:** 57 / 60 correct · estimated scaled 955 / 1000 · pass line 720 — **the best result across ten
scored attempts**, ahead of Exams 7 and 11 at 55/60 (925).
**Time:** 2,153s = 35:53 (35.9s/question). Fastest full single sitting on record, and the highest score.
Speed and accuracy moved together, not against each other.

### Domain Breakdown

| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 16 | 100% | no |
| D2 Tool Design & MCP | 11 | 10 | 91% | no |
| D3 Claude Code Config | 12 | 11 | 92% | no |
| D4 Prompt Engineering | 12 | 11 | 92% | no |
| D5 Context Management | 9 | 9 | 100% | no |

**D1 at 16/16 is a first** — the heaviest domain (27% of the exam) clean, on a base-quota paper.

### Block Breakdown

| Block | Scenario | Correct |
|---|---|---|
| 1 | Customer Support Resolution Agent | 15 / 15 |
| 2 | Multi-Agent Research System | 14 / 15 |
| 3 | Code Generation with Claude Code | 14 / 15 |
| 4 | Structured Data Extraction | 14 / 15 |

### Weakest domain — do not act on it

Nominally D2 at 90.9%. **This is the denominator artefact Insights Round 3 warned about, one day later:**
D2, D3 and D4 each lost **exactly one question**; D2 only ranks lowest because it has 11 questions to
D3/D4's 12. A one-question difference in denominator, not performance. Prior scored paper by attempt
chronology is Exam 12 (weakest D3/D4), so the two-consecutive gate is not met and **no confirmed weakness
exists — base quota stands for Exam 17.** exams_scored = 10; the next Insights Round falls at 12.

### The three misses

| Q | Dom | § | Picked | Key | Time |
|---|---|---|---|---|---|
| 19 | D2 | §2.2 | D — return an error instead of a partial document | C — expand the description to state formats, the 40-page truncation, and the auth boundary | 35s |
| 41 | D3 | §3.11 | B — split background to README, standards to `.claude/rules/` | C — cut the background and culture prose; keep the operative instructions | 43s |
| 46 | D4 | §4.6 | A — `tool_choice: "auto"` plus a prompt instruction | C — `tool_choice: "any"` | 28s |

### Observations — both watch-items from the Exam 12 note recurred

**1. Q46 repeats Exam 12's Q33 exactly, and this is the headline result.** Both ask which configuration
*guarantees* a tool call; both offer `auto` + a prompt instruction as the trap and `any` as the key. Ram
picked the trap both times — on 2026-08-11 and again on 2026-08-12, roughly fourteen hours apart, **having
read the full rationale for Q33 in between** (the papers give per-question feedback on lock-in).

The two stems measure **0.118 Jaccard** — far below the archetype gate's 0.40 reskin threshold, and the
two questions sit in different scenarios (Developer Productivity vs Structured Data Extraction), different
domains as tagged (D2 §2.5 vs D4 §4.6), and different surface framings (posting a work-tracker record vs
extracting from an unknown document type). **He is not pattern-matching a repeated question; he holds an
actively wrong preference for `auto` + instruction over `any`.** That is the most valuable single finding
in ten scored papers, because it is precisely the kind of error that survives more practice papers and
only dies to targeted drilling.

**2. `.claude/rules/` is now a confirmed reflex — third wrong pick in two papers.** Exam 12 Q1 (where the
answer was a diagnostic, `/memory`), Exam 12 Q56 (where the answer was `.claude/commands/`), and now
Exam 13 Q41 (where the answer was to delete prose from `CLAUDE.md`). Three different correct answers, one
recurring wrong instinct: reaching for path-scoped rules whenever the question smells like "where should
this live?".

**3. The compensating-mechanism pattern survived a fresh paper — but attenuated.** The Exam 12 note asked
whether the reflex would disappear on an unfamiliar paper or persist, which would make it a genuine
reasoning habit. Verdict: **it persisted.** Q46 chose a probabilistic control over an available guarantee,
and Q19 changed the tool's runtime behaviour rather than fixing the description that is the model's only
view of scope. Notably he did *not* take Q19's obvious workaround option (a post-processing check that
flags truncated documents) — so the pull toward pure symptom-patching has weakened, while the pull away
from *fixing the signal* has not.

**4. Everything else is clean.** D1 16/16 including the whole Customer Support block; D5 9/9; no block
below 14/15. Nine of the ten scored attempts now sit at 49–57 raw.

### Professor's Note — Intent for Exam 17 (second note, after Exam 13)

Written after Exam 13 (attempted 2026-08-12). Based on results-json. Extends rather than replaces the note
written after Exam 12 — that note's targeting is unchanged, and this one narrows it. **Still numbered 17
because Exams 14, 15 and 16 were all generated before either score arrived.**

- Misconceptions revealed:
  1. **`tool_choice` `any` vs `auto` + instruction (D2 §2.5 / D4 §4.6) — missed twice in fourteen hours on
     genuinely distinct questions.** Promote this from "a section to cover" to **the single highest-priority
     item in the corpus for this learner.** It is not a coverage gap; feedback has already been read and
     the wrong preference survived it.
  2. **`.claude/rules/` as the default answer to "where should this live?" (D3 §3.2 crowding out §3.1,
     §3.4 and §3.11) — three wrong picks across two papers.**
  3. **Fixing tool behaviour rather than the tool description (D2 §2.2)** — the description is the model's
     only view of scope and boundaries.
- Weakest this paper: **nominally D2 at 91%, but disregard it** — D2, D3 and D4 each lost exactly one
  question and the ranking is a denominator effect. No confirmed weakness; base quota for Exam 17.
- Intent for next paper: give the `tool_choice` distinction **three separate items in three different
  scenarios**, including one where `auto` is genuinely correct and one where the forced-specific-tool form
  is correct, so the discrimination cannot be answered by a memorised slogan. Give the where-does-this-live
  family a three-way discrimination in one item. Keep building items where a plausible workaround sits
  beside the root-cause fix.
- Watch next: whether the `tool_choice` error survives a **third** exposure. If it does after targeted
  drilling, it is a durable mental model rather than a lapse, and warrants a written one-line rule Ram
  carries into the sitting.

### Operational note — the drill deck cannot consume this result

`prep with quiz/drill/CCA-Prep_Drill_v1.html` still carries a mock map for Exams 2, 3, 4 and the Exam-2
retrofit only. Pasting Exam 12's or Exam 13's results boosts nothing, so the mechanism that would normally
turn a repeated miss into spaced repetition is **not running at the exact moment it would pay for itself.**
Fix is recorded in SESSION-STATE.md: rebuild the deck from the main checkout, not a worktree, using
`Outputs/_packbuild/remap_deck.py` for the citation-vocabulary normalisation.


---

## Exam 17 — Generated 2026-08-14

**File:** mock-exams/CCA-Prep_MockTest-17_v1.html  
**Format:** FULL60  
**Scenarios drawn:** Customer Support Resolution Agent; Multi-Agent Research System; Claude Code for Continuous Integration; Structured Data Extraction
**Attempt date:** Not yet attempted  
**Score source:** Pending  
**Total score:** Pending  
**Total time:** Pending

### Domain Breakdown

| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | — | — | pending |
| D2 Tool Design & MCP | 11 | — | — | pending |
| D3 Claude Code Config | 12 | — | — | pending |
| D4 Prompt Engineering | 12 | — | — | pending |
| D5 Context Management | 9 | — | — | pending |

**Item formats:** 52 single-answer (4 options) + 8 multiple-response (2 per block, select-2-of-4), scored all-or-nothing.

### Observations (generation-time)

- **Seed source (new):** questions seeded from **121 "Exam Trap" blocks** extracted from the
  `claudecertificationguide.com` mirror at `Outputs/ccg-mirror/` — a second community author writing
  against the same 30 official task statements. Registered as source-authority item 4 in
  `CCA-Prep_Corpus-Index_v2.md` v2.2. The traps supplied **distractor geometry only**; every rationale
  cites the v2 corpus.
- **Both Professor's Notes for Exam 17 consumed.** `tool_choice` gets four items with four different
  correct directions, so no memorised rule answers them: **Q21** `any` is correct, **Q36** forced-specific
  is correct, **Q48** `auto` is correct, **Q14** forcing `any` is itself the defect. The
  where-does-this-live family gets a three-way discrimination at **Q9** and **Q41**. D2 §2.1
  `tool_use_id` correlation at **Q11**; D2 §2.2 fix-the-description at **Q6**.
- **Compensating-mechanism geometry** (the shape behind five of Exam 12's seven misses, which no domain
  quota can target) is built into 13 items across all four blocks.
- **Slogan-breaker:** Q29 and Q44 test D1 §1.7 in opposite directions — adaptive decomposition correct
  for the open-ended investigation, wrong for the fully-known CI sequence.
- **Site-vs-corpus conflicts found and deliberately NOT used:** the mirror's D1 traps 1.30/1.32/1.34 call
  `--resume` after file changes a trap outright; corpus D1 §1.16's worked pattern says the opposite for
  the 3-of-50-files case. The mirror also says MCP transport selection may be tested, which the official
  out-of-scope list bars. Official framing wins; no question was built on either point.
- **Gate:** all 7 checks pass. Deliberate deviation reported — inline code/config token rate 27.5%,
  inside the gate's 15–30% band, above the 20–25% target, driven by the `tool_choice`/MCP/CLI content.
- **Five questions were rewritten to a different domain** (Q13, Q28, Q40, Q43, Q59) after the first
  drafted allocation tied on the gate's strict primacy rule. Rewrites, not re-tags.

### Questions Used (deduplication ledger for Exam 19+)

1. [D5] Escalation volume is running at 31% against a 22% target. The current trigger fires when a sentiment
   classifier scores the customer's message below a negative threshold, and a review of last month's escalations finds
   that most of them were routine plan changes from irritated customers, while three genuine policy gaps stayed with
   the agent for nine turns because the customers stayed polite throughout. What should the escalation trigger key on
   instead?
2. [D1] Policy caps agent-issued credits at £200; anything above that requires specialist approval. A hook was added
   to enforce this, and the audit trail now shows fourteen credits above the cap in the last month — each one logged
   by the hook, each one already applied to the customer's account. The hook is registered on the PostToolUse event
   for `issue_credit`. What is wrong?
3. [D2] `issue_credit` rejects requests that breach the refund policy by returning `{"isError": true, "message":
   "Operation failed"}`. Logs show the agent retrying these calls three times with identical arguments before giving
   up, adding roughly forty seconds to affected conversations. The rejections are correct — the requests genuinely
   breach policy. What should the tool return instead?
4. [D5] A customer gives only a first name and a partial postcode. `find_account` returns two records that both match:
   one has been active for six years with no recent activity, the other was opened last month and has an open invoice.
   The requested action is a plan downgrade. How should the agent proceed?
5. [D1][select-2] A regulatory rule requires that identity verification completes before any plan change is applied,
   with no exceptions. The system prompt already instructs the agent to call `find_account` and confirm two
   identifiers before `change_plan`, and an audit of 900 conversations finds 34 plan changes applied without a
   completed verification step. Select TWO changes that make the requirement deterministic rather than probable.
6. [D2] Requests phrased as 'send me a copy of last month's bill' are routed to `read_invoice` about 60% of the time
   and to `find_account` the rest. The two descriptions read: `read_invoice` — 'reads account data', and
   `find_account` — 'retrieves account information'. What is the correct first fix?
7. [D1] The agent sometimes stops mid-task: it tells the customer 'Let me pull up your last invoice' and then returns
   that sentence as the final reply, with no invoice. The loop is written to finish when `response.content[0].type ==
   "text"`. Which correction fixes it?
8. [D4] A quality-review prompt asks the model to flag conversations where the agent 'handled the refund badly'. Two
   reviewers reading the same flagged set disagree with the model on roughly a third of items, and with each other on
   a similar share. The instruction currently reads: 'Be conservative and only flag clear problems.' What is the
   correct revision?
9. [D3] The support-tooling repository holds three things that need to reach Claude Code. First, a coding standard
   every session must follow regardless of what is being edited. Second, a set of conventions that apply only when
   editing the roughly 90 handler files spread across 40 directories. Third, a seven-step refund-audit procedure the
   team runs a few times a week on request. Where does each belong?
10. [D4] Post-conversation summaries are written to the ticketing system by a second model call. The instruction runs
   to eleven lines specifying section order, heading wording, date format and length, and the summaries still vary:
   some open with the resolution, some with the complaint, and dates appear in three formats. What is the most
   effective next step?
11. [D2] A developer is writing the loop by hand. After `find_account` returns, they append a user-role message
   reading 'The find_account tool returned: account 88213, status active, plan Standard' and send the conversation
   back. On multi-tool turns the model sometimes re-requests a lookup it has already been given, and sometimes
   attributes one account's status to another. What is the protocol error?
12. [D5][select-2] Conversations that run past twelve turns start to go wrong: the agent restates the disputed amount
   as a rounded figure, and occasionally offers a remedy it had already ruled out. History is currently compacted by
   re-summarising the whole conversation every four turns, and each `read_invoice` result enters history in full with
   all 40-plus fields. Select TWO changes that address this.
13. [D2] `find_account` returns `{"matches": [], "status": "ok"}` when a search runs correctly and matches nobody, and
   the same empty array with `{"status": "ok"}` when the account service is unreachable and the lookup never ran. The
   agent retries both cases three times, then tells the customer no account exists. What must change?
14. [D1] To stop the agent replying with text when a tool call was expected, a developer sets `tool_choice` to
   `{"type": "any"}` for every request in the loop. Conversations now run until the iteration cap and end without a
   closing message to the customer. What explains this?
15. [D3] One engineer built a `/refund-audit` command that the whole support-tooling team should get on clone. It
   works for its author and for nobody else, even after colleagues pull the latest commit on the same branch. The file
   sits at `~/.claude/commands/refund-audit.md`. What is the fix?
16. [D1] Asked for a review of grid-scale energy storage, the system returns a report covering only lithium-ion
   chemistries. Every subagent completed successfully and each returned well-sourced material. The coordinator log
   shows the question was split into three assignments: 'lithium-ion cost trends', 'lithium-ion safety incidents' and
   'lithium-ion supply chain'. What is the root cause?
17. [D2] The document-analysis subagent has accumulated eighteen tools as capabilities were added — several parsers,
   three retrieval variants, a summariser, a translator, a citation formatter and others. Selection accuracy has
   fallen steadily as tools were added, and it now regularly picks a parser unsuited to the file in front of it. What
   is the correct architectural response?
18. [D1] The analyst's original question specifies a five-year window and a single-region scope. The coordinator's
   prompt to the web-search subagent reads: 'Search for recent material on grid storage costs.' Returns include global
   figures spanning a decade. A developer proposes fixing this by having the subagent read the coordinator's
   conversation history to recover the constraints. Why does that not work?
19. [D2] The document-analysis subagent needs to open documents the coordinator has identified. It currently holds a
   `fetch_url` tool described as 'retrieves the content at any URL'. Review finds it has occasionally fetched search-
   result pages and an internal admin endpoint that appeared in a document's footer. What is the correct change?
20. [D1][select-2] A developer is configuring the coordinator so it can spawn the three specialists, and wants the two
   independent retrieval subagents to run at the same time rather than one after the other. Select TWO statements that
   are correct.
21. [D2] The synthesis subagent must return its findings as a structured record that the report builder parses. It has
   four extraction tools, one per source type, and the coordinator cannot tell in advance which type a given batch
   contains. Roughly one call in seven currently returns a prose paragraph instead of a tool call, and the parse
   fails. Which `tool_choice` setting is correct?
22. [D3] Analysts run a repository-wide source-mapping routine before each research cycle. It produces several
   thousand lines of file listings and match output, and after running it the main session loses track of the
   analyst's original question and has to be reminded. The routine is defined as a skill. What should change?
23. [D5] The web-search subagent exhausts its retries against one of four source categories and its wrapper returns
   `{"results": [], "status": "ok"}`. The coordinator proceeds, and the final report presents three-category coverage
   as though it were complete. What should the subagent return instead?
24. [D2] The synthesis subagent must confirm individual factual claims while drafting. Every check is currently routed
   back through the coordinator, which spawns a verification call and returns the answer. The instrumentation shows
   85% of these checks are single-fact lookups against sources already in the manifest, and each one costs two extra
   hops. How should verification be reorganised?
25. [D1] Reports read well but carry no citations: claims appear as bare assertions. The coordinator currently passes
   the document-analysis subagent's output to the synthesis subagent as a concatenated block of extracted passages. A
   reviewer proposes rewriting the synthesis subagent's prompt to require a citation after every claim. Why will that
   not work?
26. [D2] The team standardises on a hosted search MCP server that every researcher should reach on clone. An engineer
   adds the server definition to `~/.claude.json` and commits nothing, and colleagues report the tools are
   unavailable. The definition also carries the API token inline. How should the server be declared?
27. [D5][select-2] Two sources give different figures for the same metric: a regulator's dataset reports 18% and an
   industry association reports 26%. Both are credible. Select TWO things the synthesis output should do.
28. [D2] Analysts want the coordinator to know which document collections are available before it decomposes a
   question — roughly forty collections, each with a title, a coverage note and a date range, changing every few
   weeks. A developer proposes exposing a `list_collections` tool the coordinator calls at the start of every run.
   What does the MCP server offer that fits this better?
29. [D1] A new request type asks the system to investigate why a published figure differs across three regulatory
   filings. The scope is not knowable in advance: what the second filing shows determines which questions the third
   raises. The current coordinator runs a fixed four-stage pipeline for every request. What decomposition strategy
   fits?
30. [D4] Before release, each report is checked for unsupported claims. The check currently runs as a final turn in
   the same session that drafted the report, and it passes almost everything; analysts later find unsupported claims
   it did not flag. What is the most effective change?
31. [D3] The first pipeline run never completes. The job produces no output and is killed by the runner's timeout
   after fifteen minutes. Run locally with the same arguments, the same command works. What is the fix?
32. [D3] Developers report that pushing a fix-up commit produces a fresh set of review comments that repeats
   everything from the previous run, including findings already addressed. Several have started ignoring the bot. Each
   run is invoked identically on the current diff. What should change?
33. [D4] To reduce cost, an engineer proposes moving all Claude-powered analysis to the Message Batches API — the pre-
   merge review that blocks the pipeline, and a weekly architectural drift report that nobody waits on. Which
   workloads should move?
34. [D1] On pull requests touching more than fifteen files, review quality becomes uneven: early files receive
   detailed findings, later ones a sentence or two, and defects spanning a caller in one file and a signature change
   in another are missed entirely. The review runs as a single pass over the whole diff. What architecture fixes this?
35. [D3][select-2] The team is hardening the pipeline invocation. Select TWO changes that are correct for a CI review
   step.
36. [D4] The pipeline parses the review result into a fixed comment payload. Exactly one tool, `post_review`, produces
   that payload, and its schema is the contract the pipeline depends on. Occasionally the model replies with a prose
   summary, or calls the diagnostic `explain_finding` tool instead, and the step fails. Which `tool_choice` setting is
   correct?
37. [D1] The security-policy check must block a merge when a change touches the payments module without an
   accompanying test. The check is currently expressed in the review prompt, and over three months it has passed
   eleven changes that should have been blocked. Compliance requires no exceptions. What is the correct change?
38. [D3] The pipeline currently scrapes the review's printed text with a regular expression to decide whether to fail
   the job, and the expression breaks whenever the phrasing of the summary line changes. What is the correct way to
   make the decision robust?
39. [D4] Findings are returned through a tool call with a JSON schema, so the payload always parses. A validator then
   checks that every finding's `line` falls inside the changed hunks of the file it names. About 6% fail that check.
   The retry sends the identical original prompt again, and roughly the same share fails on the second attempt. What
   should the retry carry?
40. [D3] Reviewers notice the pipeline applies none of the repository's conventions: it flags naming the team has
   documented as correct and misses the error-handling rules everyone follows. The same prompt run by a developer in a
   local checkout applies all of them. The CI job clones the repository and invokes Claude Code from a scratch
   directory outside it. What is the cause?
41. [D3] The repository holds three conventions Claude Code should apply. Commit-message format applies to every
   session. A set of migration-file conventions applies to roughly 200 files matched by `db/migrations/**`. A release-
   checklist procedure is run by hand about once a fortnight. Which arrangement is correct?
42. [D4][select-2] Review output is produced through a tool call with a strict JSON schema. Select TWO defect classes
   that remain possible despite the schema.
43. [D4] On long review runs the findings change character as the run proceeds: early comments are specific and cite
   line numbers, later ones become general observations about style, and the severity labels drift upward. The system
   prompt specifying the finding format has not changed. What explains this and what fixes it?
44. [D1] Every pull request review runs the same four steps in the same order: lint-rule conformance, test coverage of
   changed lines, dependency-policy check, then a summary comment. The steps do not depend on each other's findings,
   and the set has not changed in six months. An engineer proposes replacing this with a coordinator that decides
   which checks to run from what it finds. Should the team adopt it?
45. [D1] A pull request triggers the review, and the dependency-policy step fails because the policy service is
   unreachable. The lint and coverage steps have already completed with findings. The current handler aborts the run
   and posts nothing. What should the pipeline do instead?
46. [D4] Extracted invoices carry a `line_items` array and a `total`. Every record parses cleanly against the schema,
   but reconciliation finds that on about 4% of invoices the `total` does not equal the sum of the line items — the
   model has copied a figure from a subtotal or a carried-forward balance. What catches this before posting?
47. [D5] A validation exercise reports 97% field-level accuracy across a 2,000-document sample, and the team proposes
   auto-posting every extraction above the confidence cut-off. A reviewer asks for the figure broken down. It emerges
   that invoices and credit notes score in the high nineties, while delivery advices — 6% of volume — score 61%. What
   does this show?
48. [D4] A separate assistant helps the finance team query the pipeline. Some turns are answered from the conversation
   itself — 'what did we agree the tolerance was?' — and some need a tool call against the records. It currently runs
   with `tool_choice` set to `{"type": "any"}`, and users report it now runs a pointless lookup before answering
   questions that needed no data at all. What is the correct setting?
49. [D5] Reviewer capacity covers about 3% of daily volume. The current policy sends the 3% with the lowest confidence
   scores to review and posts everything else. Two months in, a supplier changes its statement layout and a field is
   silently mis-extracted with high confidence for six weeks before anyone notices. What should the sampling policy
   include?
50. [D3][select-2] The team is refining the extraction prompt for a supplier whose credit notes are handled
   inconsistently: sometimes the credit is recorded as a negative amount, sometimes as a positive amount with a type
   flag. The prompt already describes the intended handling in three paragraphs. Select TWO techniques most likely to
   resolve this.
51. [D1] Statements arriving as 60-page documents are processed by splitting them into six-page batches, extracting
   each batch independently, and concatenating the records. Within a batch the extraction is accurate. Across the
   document, transactions that continue across a batch boundary are duplicated, and running balances no longer
   reconcile end to end. What is missing?
52. [D5] Confidence scores are used to route records. Analysis of a labelled set shows that records scoring 0.90 on
   `invoice_date` are correct about 94% of the time, while records scoring 0.90 on `net_amount` are correct about 82%
   of the time. The current policy applies one 0.85 threshold to every field. What should change?
53. [D2] An agent maintaining the extraction rules must change one occurrence of the string `tolerance = 0.02` in a
   configuration module. Edit reports that the target text is not unique — the string appears four times in the file.
   What is the correct next step?
54. [D3] A first draft of a new extraction module has four problems: the field order does not match the finance
   system's import format, one helper duplicates an existing utility, error handling swallows parse failures, and the
   module name does not follow the repository convention. Fixing the field order changes which helper is needed, and
   removing the duplicate helper changes where errors surface. How should the feedback be delivered?
55. [D4] Records are produced through a tool call with a JSON schema and then checked by hand-written validators. An
   engineer proposes replacing the validators with typed models carrying field validators — enforcing that `net + tax
   == gross`, and that `due_date` is not earlier than `issue_date`. A colleague objects that the schema already
   validates the payload. Who is right?
56. [D1] The daily batch contains four independent document types, each with its own extractor, and no type's output
   is an input to any other. The coordinator currently dispatches them one type at a time, waiting for each to
   complete. End-to-end time is roughly the sum of the four. What is the correct change?
57. [D4][select-2] The retry loop re-submits failed extractions with the validation error attached. Select TWO failure
   types where a retry can be expected to succeed.
58. [D3] The team must onboard a new document type — customs declarations — and nobody on the team has worked with
   them. They know roughly what the finance system needs but not which fields matter, how the type behaves at edge
   cases, or what usually goes wrong. How should they work with Claude Code on the extraction design?
59. [D5] The nightly run processes around 3,000 documents in one long session. Twice this month it has failed near
   document 2,400 — once on an out-of-memory kill, once on a network fault — and both times the rerun started again
   from document 1. What should the pipeline do so a failure does not cost the completed work?
60. [D1] A supplier begins sending a document type the pipeline has no extractor for. The dispatcher currently routes
   it to the invoice extractor, which returns a well-formed record with several fields wrong. The finance system
   accepts it. What should the dispatcher do instead?

---

## Exam 18 — Generated 2026-08-14

**File:** mock-exams/CCA-Prep_MockTest-18_v1.html  
**Format:** FULL60  
**Scenarios drawn:** Code Generation with Claude Code; Developer Productivity with Claude; Claude Code for Continuous Integration; Structured Data Extraction
**Attempt date:** Not yet attempted  
**Score source:** Pending  
**Total score:** Pending  
**Total time:** Pending

### Domain Breakdown

| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | — | — | pending |
| D2 Tool Design & MCP | 11 | — | — | pending |
| D3 Claude Code Config | 12 | — | — | pending |
| D4 Prompt Engineering | 12 | — | — | pending |
| D5 Context Management | 9 | — | — | pending |

**Item formats:** 52 single-answer (4 options) + 8 multiple-response (2 per block, select-2-of-4), scored all-or-nothing.

### Observations (generation-time)

- **Companion to Exam 17**, drawn from the half of the 121-block trap inventory Exam 17 left alone, and
  from the two scenarios Exam 17 rested — the two papers together cover all six official scenarios.
- **Concentration:** the configuration-location family, six items on the when-does-this-load axis —
  **Q1** user vs project scope, **Q3** `/memory` is a diagnostic not a loader, **Q6** a skill is a
  directory with `SKILL.md`, **Q23** task workflows belong in skills, **Q28** `.claude/rules/` vs a
  paths-scoped skill, **Q41** `@path` imports.
- **Session-state slogan-breaker, and the one place the mirror contradicts the corpus.** Q11 resume and
  NAME the three changed files (3 of 50 stale); Q44 start FRESH with an injected summary (a long-lived
  CI session, broadly stale); Q4 fork for comparing two approaches. Three mechanisms, three items, one
  corpus section. The mirror's traps 1.30/1.32/1.34 collapse this into "resume-after-changes is always
  wrong" — the corpus draws the line at how stale the prior context is, and the corpus wins.
- **Cross-paper slogan-breaker:** Q10 (plan mode WRONG for a one-file fix with a clear stack trace)
  against Exam 17 Q28 (plan mode RIGHT for a twelve-file restructure with two candidate designs).
- **Gate:** all 7 checks pass. Stem median 51 after a second pass extended the sixteen shortest stems
  with concrete situational detail; inline token rate 17.1%, inside the band and below the target,
  because this paper's subject matter runs to mechanisms rather than parameter values.

### Questions Used (deduplication ledger for Exam 19+)

1. [D3] Two engineers have Claude Code applying the house conventions correctly. A third joins, clones the same
   repository on the same branch, and gets none of them — no naming rules, no error-handling standard. All three run
   the same version and the same commands. The conventions live in `~/.claude/CLAUDE.md` on the two machines where
   they work. What is the fix?
2. [D5] A refactoring session runs long. Constraints stated early — that one module must keep its public signature,
   and that a particular helper is deprecated — are honoured at first and then quietly violated around turn twenty,
   even though nothing removed them from the conversation. What is the effective mitigation?
3. [D3] An engineer adds `.claude/rules/schema.md` and reports that running `/memory` afterwards 'did not activate
   it'. The rule's conventions are still not being applied when they edit a schema file, and they ask whether the
   command needs a flag to force a reload. What should they be told?
4. [D1] After an expensive codebase analysis, the team wants to evaluate two migration strategies — one incremental,
   one big-bang — and compare them fairly. Both should start from the analysis already completed, and neither
   evaluation should be coloured by the other. What is the correct mechanism?
5. [D5][select-2] An engineer is four hours into a session that has explored a large part of the codebase. Responses
   are becoming vaguer and occasionally reference files that were renamed earlier in the session. They intend to keep
   working for another two hours. Select TWO steps that fit.
6. [D3] An engineer wants a `/scaffold` command available to the team. They create `.claude/skills/scaffold.md` in the
   repository, commit it, and pull on a second machine. The command appears in neither place, and `/memory` lists no
   skill by that name. The file's contents are correct and its frontmatter parses. What is wrong?
7. [D2] Before renaming a configuration key, an engineer asks Claude Code to locate every place the string
   `retry_budget` is read. Claude runs a Glob search for `**/*retry_budget*` and reports two files, both of which
   merely have the key in their filename. The key is read in eleven places. Which tool should have been used, and why?
8. [D4] A prompt classifies each pull request as a refactor, a feature or a fix, and the label drives which review
   checklist runs. It carries six examples covering the clear cases. Those are handled well; changes that add a
   feature while restructuring the code around it are labelled inconsistently, sometimes one way and sometimes the
   other on near-identical diffs. What would most improve it?
9. [D5] A long refactoring conversation is approaching the context limit. An engineer proposes dropping the oldest
   third of the turns from every subsequent request to make room, arguing that the recent turns carry the current
   state anyway. Those early turns are where the module boundary and the deprecation list were agreed. What is wrong
   with this, and what should be done instead?
10. [D3] A test fails with a stack trace pointing at one function in one file. The cause is visible in the trace, the
   fix is a two-line change, and no other module is involved. An engineer asks whether to use plan mode. What is the
   right answer?
11. [D1] Yesterday a session analysed a 50-file module and produced a working understanding of its call graph and its
   test coverage. Overnight three of those files were refactored; the other 47 are untouched. The engineer wants to
   carry on this morning from where they left off rather than rebuild that understanding. What is the correct
   approach?
12. [D4][select-2] A generation step returns a structured change plan through a tool call, and every field in its
   schema is currently marked required. Reviewers find `rollback_step` and `owning_team` populated with confident-
   looking values on plans where the request mentioned neither, and the values are plausible enough that two of them
   were acted on. Select TWO changes that reduce this.
13. [D2] An agent must change one of six occurrences of `DEFAULT_TIMEOUT` in a settings module. Its first Edit attempt
   reports a non-unique match. It immediately reads the whole 900-line file and writes it back with the single change
   applied. What should it have done, and why does it matter?
14. [D5] An engineer delegates a broad 'find everywhere the pricing rules are applied' investigation to a subagent. A
   colleague argues this is pointless because only one investigation is running, so there is nothing to parallelise.
   What is the stronger argument for delegating?
15. [D1] Three MCP tools return timestamps in three formats — Unix epoch, ISO 8601 and a locale string. The agent
   reasons over all three and makes date-comparison errors a few times a week. A developer proposes adding a system-
   prompt paragraph explaining each tool's format and asking the model to convert before comparing. What is the better
   approach?
16. [D2] An MCP server exposes `find_issue`, described as 'issue search'. Asked to check whether a bug has already
   been reported, the agent almost always runs a Grep across the repository instead and reports what it finds in code
   comments. The MCP server is connected and its tool is available. What is the likely cause?
17. [D1] A coordinator must answer three questions before a design review: which components use a deprecated token,
   which tests cover the checkout flow, and what the issue tracker holds against this milestone. None of the three
   depends on either of the others. The coordinator currently spawns one specialist, waits, spawns the next, and so
   on. What should change?
18. [D2] Asked how a checkout total is calculated, the agent reads all 34 files in the checkout package before
   answering. The answer is correct, the main context is nearly full afterwards, and the follow-up question performs
   noticeably worse. What is the correct investigation strategy?
19. [D1] A coordinator is asked to prepare a migration plan for a shared authentication module. It splits the work
   into 'update the login handler', 'update the session handler' and 'update the token refresh handler'. The resulting
   plan says nothing about the four services that call the module, and the migration breaks two of them. Where is the
   defect?
20. [D1][select-2] A specialist is being defined to audit dependency licences against the team's approved list. It
   needs to read manifests and search the repository, must not modify anything, and will be spawned by the coordinator
   once per release. The approved list and the manifest locations are both known to the coordinator. Select TWO
   configuration choices that follow the corpus.
21. [D2] After rewriting the design-system server's tool descriptions to be precise and distinct, `get_component_spec`
   is still bypassed roughly a third of the time in favour of a repository search. The system prompt contains the
   line: 'When asked about components, search the codebase for the component definition.' What does this show?
22. [D1] To cut latency, an engineer proposes letting the test-analysis specialist send its findings straight to the
   code-generation specialist, skipping the coordinator hop and saving roughly four seconds per exchange. Both already
   run under the same coordinator, and the payload is a short structured summary. What is the objection?
23. [D3] The project `CLAUDE.md` has grown to about 700 lines. Most of it is a set of numbered procedures — how to run
   a dependency audit, how to prepare a release branch, how to triage a flaky test — each used a few times a month.
   The rest is genuinely universal. Sessions have become noticeably more expensive. What should be done?
24. [D2] The issue-tracker server returns `{"isError": true, "message": "Request could not be completed"}` for every
   failure — an expired token, a rate limit, a malformed query and an unknown project key all produce that string. The
   agent retries all of them identically and reports the same unhelpful summary to the user. What must the responses
   carry?
25. [D1] A release specialist must tag a build before publishing it. Its prompt says so, and about one release in
   twelve is published untagged. An engineer proposes a classifier in front of the coordinator that identifies release
   requests and routes them to the release specialist. Why does this not address the problem?
26. [D2] A `delete_branch` tool is occasionally called on branches that still carry unmerged commits — three times
   last month, twice recoverable from the reflog. The team wants deletion to be impossible unless the agent has first
   seen exactly what would be removed, and wants that guarantee to hold without depending on the model remembering to
   check. Which tool design achieves it?
27. [D5][select-2] The team wants Claude to recall architectural decisions made in sessions weeks earlier — why a
   queue was chosen over polling, which retry library was rejected and on what grounds, and which of two caching
   strategies was ruled out. Sessions are started fresh each morning and the decisions are currently only in old
   transcripts. Select TWO approaches that work.
28. [D3] Every file under `infra/` must carry a specific header comment and follow a naming rule, and this must apply
   automatically whenever Claude edits one of those files — without anyone remembering to ask for it. An engineer
   proposes writing it as a skill with a `paths` entry. What is the better mechanism, and why?
29. [D1] An audit of 40 modules in one pass produces detailed findings for the first several and thin ones thereafter.
   An engineer argues that a sharper prompt — explicitly requiring the same six checks on every module — makes a
   multi-pass architecture unnecessary. What is the flaw in that argument?
30. [D4] A prompt asks the agent to flag risky dependency upgrades and to attach a confidence score, with anything
   below 0.7 suppressed. False positives remain high, and inspection shows suppressed items and surfaced items are
   similar in kind. What should be done first?
31. [D3] The project `CLAUDE.md` carries three long sections of file-type conventions — Terraform, SQL migrations and
   React components. Token usage per session has climbed, and engineers editing a React component are paying for the
   Terraform and SQL sections on every request. What is the correct restructuring?
32. [D4] The reviewer emits findings in four categories. Three are accurate; the performance category is wrong roughly
   70% of the time. Developers have begun dismissing all four without reading them, and correctness findings are now
   being missed in review. What is the correct move while the performance prompt is being improved?
33. [D3] The team must migrate the pipeline off a deprecated test runner. The replacement is chosen and its basic
   invocation is documented, but the configuration mapping is unclear in three places, two custom reporters may have
   no equivalent at all, and roughly 40 spec files will need changing. How should Claude Code be used for this work?
34. [D1] The nightly job runs four analyses across the repository. On one run the dependency-graph analysis fails on a
   malformed lockfile, after the complexity, coverage and dead-code analyses have all completed and produced their
   sections. The orchestrator's current handler aborts the run and writes nothing at all. What should it do instead?
35. [D4][select-2] An engineer wants to move three Claude workloads to the Message Batches API to cut cost: an
   interactive query tool a developer waits on, a pre-merge check that blocks the pipeline, and a monthly architecture
   report nobody reads until the following week. Select TWO properties of that API that constrain which of them can
   move.
36. [D4] The reviewer attaches a confidence score to each finding, and the pipeline auto-resolves anything above 0.9
   without human review. A sample audit finds that 0.9-confidence findings about naming are right 96% of the time,
   while 0.9-confidence findings about concurrency are right 71% of the time. What does the pipeline need before it
   can keep auto-resolving?
37. [D3] The reviewer's summary block is specified in four paragraphs of prose describing what each section should
   contain and how findings should be ordered. Across runs the sections appear in different orders and the ordering
   rule is applied inconsistently. An engineer proposes rewriting the four paragraphs more precisely. What should be
   done instead?
38. [D1] A generation step writes database migration scripts and a review step checks them against the schema before
   they are applied. Both currently run as consecutive turns in one session. Across roughly ninety migrations the
   review has never rejected a script, and two migrations that reached production had to be rolled back. What change
   makes the review meaningful?
39. [D4] The nightly job emits a coverage report through a tool call with a JSON schema. Every payload parses.
   Finance-side consumers report that `lines_covered` sometimes exceeds `lines_total`, and that the reported
   percentage does not always match the two counts. What is needed?
40. [D2] The nightly job always performs the same three steps against the artefact store: fetch the manifest, verify
   its checksum, then record the result. The agent sometimes records without verifying, and sometimes verifies a
   manifest it fetched two steps earlier. An engineer proposes bundling all three into one `process_artefact` tool.
   When is that the right call?
41. [D3] The project `CLAUDE.md` has become hard to maintain: universal standards, the commit convention and the
   review checklist all sit in one file that several people edit. The team wants them in separate files while still
   loading together for every session. What supports this?
42. [D3][select-2] The same prompt against the same commit gives different verdicts on different runs — one run flags
   a naming violation the next ignores, and the pipeline's pass/fail parse sometimes fails outright because the
   summary wording changed. The team wants the CI review reproducible. Select TWO changes that address this.
43. [D4] A summarisation step must return a JSON object, and roughly one call in twelve begins with a sentence of
   preamble before the object, which breaks the parser. Tool-based structured output is not available for this step.
   What is the most direct way to constrain the response?
44. [D1] Each CI review is currently invoked with `--resume` against a long-lived session, so the reviewer 'remembers
   the repository'. The reviews have begun citing helper functions that were deleted a fortnight ago and referring to
   a directory layout that changed in the same window. What should the pipeline do?
45. [D1] The nightly job summarises each of 30 modules in a loop. Some summaries end mid-sentence, and the loop treats
   them as complete and moves on. Inspecting the responses, the truncated ones carry `stop_reason` of `max_tokens`.
   How should the loop handle this?
46. [D4] One prompt currently asks the model to identify each document in the bundle, extract the fields belonging to
   each, reconcile the repair quotes against the adjuster's narrative, and produce a settlement recommendation. Output
   quality is poor and the failures are hard to attribute to any one part. What is the correct restructuring?
47. [D5] Two reviewers can check about 120 records a day against a daily volume of roughly 1,400. The current policy
   gives each reviewer an equal share drawn at random across the whole day's output. Errors are still reaching the
   claims system, and post-hoc analysis shows most of them sat in records the model handled with visible uncertainty.
   How should the capacity be directed?
48. [D1] A summarisation agent condenses each claim pack into a paragraph for the reviewer. The paragraphs read well
   and reviewers cannot tell which document any statement came from, so they open the whole bundle anyway. The agent
   receives the extracted content as one concatenated block. What is the fix?
49. [D4] A settlement figure must be derived: sum the approved repair quotes, subtract the policy excess, apply the
   depreciation percentage for the item's age band, then cap at the policy limit. The model returns figures that are
   plausible and frequently wrong, with no way to see where the derivation went astray. What should the prompt
   require?
50. [D2][select-2] The extraction tool's input schema is being revised. `claim_type` is currently a free-text string
   and arrives with a dozen spellings of the same four categories, and reviewers cannot tell what `adjuster_ref` is
   meant to hold. Select TWO schema changes that follow the corpus.
51. [D1] The pipeline should hand a claim to a human when it cannot safely proceed. The current rule escalates
   whenever the model reports low confidence, and the escalation queue is full of straightforward claims while several
   genuinely unusual ones were processed automatically. What should trigger escalation instead?
52. [D5] The reviewer-facing output presents everything as flowing prose: the adjuster's account, the list of quoted
   repair items with amounts, and the three policy clauses that bear on the claim. Reviewers say the quotes are hard
   to check and they keep re-reading to find the clause wording. What should change?
53. [D2] A repair quote occasionally arrives as a scanned image the parser cannot read. Today the parser tool raises,
   the extraction subagent catches it and returns a record with the quote fields blank, and the coordinator posts the
   claim with a lower settlement. Where should this failure be handled?
54. [D4] A claim pack states a repair total in the narrative that does not match the sum of the attached quotes, and
   the pack gives no indication which is authoritative. The pipeline runs unattended overnight. How should the
   extraction step handle the discrepancy?
55. [D5] The harder claims are handled in a multi-turn session with a reviewer, and history is summarised every few
   turns to control length. Towards the end of these sessions the agent begins restating the policy number with a
   transposed digit and rounding the excess to the nearest ten pounds. What should be done?
56. [D2] An engineer must find every place the settlement calculation is invoked. A search for `calculateSettlement`
   returns its definition and two call sites, but the team knows it is used far more widely — most callers go through
   thin wrapper functions in a helpers module. What is the right approach?
57. [D5][select-2] The claim form gives a date of loss of 12 March and the adjuster's narrative gives 14 March. Both
   documents are part of the same pack, both are legitimate sources, and the policy's waiting period makes the two
   dates lead to different settlement outcomes. Select TWO things the extraction output should do.
58. [D3] The pipeline repository's `CLAUDE.md` opens with three paragraphs on the project's history, then covers the
   schema conventions, then returns to background on the claims domain, then states the testing requirement. Engineers
   report Claude frequently misses the testing requirement. What is the most likely problem?
59. [D1] Claims the pipeline cannot complete are handed to a specialist with a note reading `manual review required:
   extraction incomplete`. Specialists have no access to the pipeline's working context, so they open the pack and
   start over, averaging nineteen minutes per handoff. What should the handoff carry?
60. [D4] Three rules must hold on every extraction call: monetary values are returned in minor units, dates in ISO
   format, and a field absent from the pack is returned as null rather than inferred. They are currently appended to
   each per-document user message, and compliance is inconsistent across a long run. Where do they belong?


---

## Exam 17 — SCORED 2026-08-14 (51/60, 865)

**File:** mock-exams/CCA-Prep_MockTest-17_v1.html
**Attempt date:** 2026-08-14 | **Score source:** results-json | **Total time:** 37:58 of 120 (38s/question)
**Total score:** 51 / 60 correct (estimated scaled: 865 / 1000; pass line 720)
**Item formats:** single-answer 45/52 · multiple-response 6/8

### Domain Breakdown
| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 15 | 94% | no |
| D2 Tool Design & MCP | 11 | 8 | 73% | no |
| D3 Claude Code Config | 12 | 9 | 75% | no |
| D4 Prompt Engineering | 12 | 10 | 83% | no |
| D5 Context Management | 9 | 9 | 100% | no |

Blocks: Customer Support 14/15 · Multi-Agent Research 13/15 · CI 12/15 · Structured Extraction 12/15.

### Read the score against what this paper was for

51/60 is the lowest raw since Exam 9 and it is not a regression. Exam 17 was built specifically to attack
the error shapes the Exam 12 and Exam 13 notes identified, so a lower score on it carries more information
than a higher score on a paper drawn at random. The nine misses are the point of the exercise.

### THE FINDING: the tool_choice error is fixed, and a narrower one replaced it

Four items tested `tool_choice` in four different directions, so no single remembered rule could answer
them. Three landed.

| Q | Required | Picked | Result | Time |
|---|---|---|---|---|
| 21 | `any` — guarantee a tool call, model picks which | `any` | **right** | 138s |
| 48 | `auto` — mixed conversational/data workload | `auto` | **right** | 31s |
| 14 | forcing `any` every iteration is the DEFECT | identified the defect | **right** | 46s |
| 36 | forced-specific `{"type":"tool","name":"post_review"}` | `any` | **wrong** | 53s |

**Q21 is the headline.** It is the same shape as Exam 12 Q33 and Exam 13 Q46 — which configuration
*guarantees* a tool call — and those were missed twice in fourteen hours with the same wrong pick. Here it
was answered correctly, and the 138 seconds spent on it was the longest of any question on the paper. The
error the last two notes called the highest-priority item in the corpus is **resolved**, and it was
resolved by work rather than by recognition: the stem, scenario and tagged domain were all different.

What replaced it is one level finer. On Q36 the pipeline needs a *specific named tool* because that tool's
schema is the contract, and `any` was chosen — a guarantee that is real but **weaker than the
requirement**. That is a different error from preferring a probabilistic control over a guarantee. Retire
the old framing. The new one: match the strength of the guarantee to what the requirement specifies.

### Secondary: after-the-fact enforcement where prevention was available

- **Q19 (D2 §2.5)** — an over-broad `fetch_url` was reaching an internal endpoint. Picked a PostToolUse
  hook that discards the response *after* retrieval; the key was a constrained `load_document` that cannot
  reach it at all. **Q2 on the same paper was answered correctly**, and Q2 is the PostToolUse-versus-
  PreToolUse rule asked directly. So the rule is known and does not transfer when the question is framed
  as tool design rather than hook choice. That is a transfer failure, not a knowledge gap, and it needs a
  different fix from more coverage.
- **Q7 (D1 §1.1)** — chose to instruct the model to order its output so a fragile `content[0].type` check
  would keep working, rather than replacing the check with `stop_reason`. 25 seconds.
- **Q53 (D2 §2.9)** — on a non-unique Edit match, dropped to a line-anchored shell substitution instead of
  widening the anchor. 30 seconds.

The compensating-mechanism shape is **attenuated but present**: 3 clear instances of 9 misses (Q7, Q19,
Q53) against 5 of 7 on Exam 12. Q24 is a fourth if batching a round-trip counts as optimising a cost the
common case need not pay. All three clear instances were answered in under 50 seconds.

### The cleanest section-level gap: D3 §3.7 iterative refinement

Two of the three D3 misses are the same section, and each uses a wrong axis rather than missing a fact.

- **Q50** (select-2, 91s) — picked the correct examples option *and* "rewrite the three paragraphs more
  precisely". Those are not complementary: once prose has failed to produce consistency, examples
  supersede another attempt at wording. Half-right, scored zero.
- **Q54** (50s) — split the feedback into two messages on a *mechanical versus substantive* axis. The
  documented axis is *interacting versus independent*, and three of the four issues were explicitly
  coupled.

### The .claude/rules/ reflex is now speed-dependent, not absent

Q9 and Q41 are the same three-way discrimination in different scenarios. **Q9 right, 99 seconds. Q41
wrong, 32 seconds** — and the Q41 pick was "all three in `.claude/rules/`, each with a glob", the fourth
instance of `.claude/rules/` as the default answer to "where should this live?" across three papers.
Knowing it is no longer the issue. Retrieving it under time pressure is.

### Timing: the Insights Round 3 finding needs a caveat

Round 3 concluded the clock is never the binding constraint, so slowing down costs nothing. He did slow
down — 138s, 106s and 91s on three questions against a 38s paper average — and got **one of those three
right**. Meanwhile four of the nine misses took under 40 seconds. Both halves matter: the fast misses
(Q7, Q41, Q53, Q42) are cheap to recover, and the slow misses (Q24, Q50) are genuine reasoning errors that
more time alone will not fix.

### Multiple-response cost 2 marks for 2 half-right answers

6/8. Both misses were partial — Q42 had B right and added D (a schema-catchable structural violation
treated as a semantic one); Q50 had A right and added C. All-or-nothing scoring means a half-understood
item scores the same as a blank one.

### Weakest domain

**D2 at 73% (8/11), with D3 at 75% (9/12) within one-fifth of a question.** Treat them as tied rather than
ranked. D2's three misses sit in two sections (§2.5 twice, §2.9 once), so this is targetable at section
level; a domain-wide quota bump would spread effort across nine sections to reach two.

Against the two-consecutive-paper rule D2 was nominally weakest on Exam 13 as well — but that was one
question on an 11-question denominator and was ruled an artefact at the time. Three misses is a different
signal. **Recorded as confirmed-weak-with-caveat: section-level targeting is the better lever, and the
base quota should stand for Exam 19 unless Ram asks for the +4.**

### Drill deck — this result is the first that can actually be imported

The mock map was repaired earlier the same day (citation join coverage 27.7% to 99.9%, all 18 papers).
Importing this results JSON boosts **67 distinct cards with zero unmatched questions**: 18 on D1 §1.1,
19 across D2 §2.5/§2.9, 16 across D3 §3.2/§3.7, 14 across D4 §4.6/§4.7. This is the first scored paper
whose misses reach the spaced-repetition layer.

### Professor's Note — Intent for Exam 19

Written after Exam 17 (attempted 2026-08-14). Based on results-json. **Supersedes both Exam 17 notes on
the `tool_choice` question, which is now closed.**

- Misconceptions revealed:
  1. **Guarantee strength is not matched to the requirement** (D4 §4.6 / D2 §2.5). `any` chosen where a
     named tool was the contract. The old "probabilistic control over an available guarantee" framing is
     retired — that error was answered correctly three times on this paper.
  2. **Prevention versus after-the-fact enforcement does not transfer out of the hooks frame** (D2 §2.5,
     §2.7). Correct when asked as PostToolUse-vs-PreToolUse (Q2); wrong when the same distinction is
     dressed as tool design (Q19).
  3. **D3 §3.7 axis errors.** Prose refinement treated as complementary to examples rather than superseded
     by them (Q50); feedback batched on mechanical-vs-substantive instead of interacting-vs-independent
     (Q54).
- Weakest this paper: **D2 73%, D3 75% — treat as tied.** Each concentrates in two sections, so target
  sections, not domains. Base quota for Exam 19.
- Intent for next paper: build the **guarantee-strength ladder** as an explicit family — three items where
  `auto`, `any` and forced-specific are each correct, plus one where a guarantee *stronger* than needed is
  the wrong answer, so the discrimination runs in both directions. Give D2 §2.5 a prevention-versus-
  detection item that never mentions hooks. Give D3 §3.7 two items whose distractors are the wrong *axis*
  rather than a wrong fact. Keep the workaround-beside-the-root-cause geometry; it still caught three
  items in nine.
- Watch next: whether the fast misses stay fast. Four of nine came in under 40 seconds on a paper where he
  used 32% of the allowance. If Exam 18 shows the same split — long thought on the hard items, snap
  answers on the recoverable ones — the lever is a pre-answer pause on any item whose options name a file
  path or a `tool_choice` value, not more content.

---

## Exam 19 — Generated 2026-08-14

**File:** mock-exams/CCA-Prep_MockTest-19_v1.html  
**Format:** FULL60  
**Scenarios drawn:** Customer Support Resolution Agent; Code Generation with Claude Code; Claude Code for Continuous Integration; Structured Data Extraction
**Attempt date:** Not yet attempted  
**Score source:** Pending  
**Total score:** Pending  
**Total time:** Pending

### Domain Breakdown

| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | — | — | pending |
| D2 Tool Design & MCP | 11 | — | — | pending |
| D3 Claude Code Config | 12 | — | — | pending |
| D4 Prompt Engineering | 12 | — | — | pending |
| D5 Context Management | 9 | — | — | pending |

**Item formats:** 52 single-answer + 8 multiple-response (2 per block, select-2-of-4), all-or-nothing.

### Observations (generation-time)

- **Built entirely from the Professor's Note — Intent for Exam 19.** Every one of its five instructions is
  implemented and locatable.
- **THE GUARANTEE-STRENGTH LADDER — four items, four scenarios, and the discrimination runs in BOTH
  directions**, which is what Exam 17 did not test:
  | Q | Scenario | In place | Correct | Direction |
  |---|---|---|---|---|
  | 2 | Customer Support | `auto` | `any` | too weak, step **up** |
  | 23 | Code Generation | (new step) | `auto` | nothing is mandatory |
  | 32 | CI | `auto`/wrong tool | forced-specific | the rung missed on Exam 17 Q36 |
  | 46 | Structured Extraction | forced-specific | `any` | **too strong, step DOWN — new direction** |
  Q46 is the item the note asked for: a guarantee already in place that exceeds the requirement and has to
  be relaxed. Exam 17 established that the old error — preferring a probabilistic control over an available
  guarantee — is closed, so over-specifying is now tested alongside under-specifying.
- **Prevention vs after-the-fact detection, with neither hook event named anywhere on the paper.** This
  targets the Exam 17 transfer failure precisely: Q2 was right when asked as PostToolUse-vs-PreToolUse and
  Q19 wrong when the same distinction was dressed as tool design. Here it appears only as tool design —
  **Q6** (uncapped credit tool plus nightly reconciliation that reverses), **Q18** (unrestricted shell tool
  plus weekly log review that reverts), **Q15** and **Q57** (over-broad retrieval narrowed at the interface).
- **D3 §3.7 with wrong-AXIS distractors rather than wrong facts**, since both Exam 17 §3.7 misses were axis
  errors. **Q16** (technique selection — the axis is whether the target can already be stated; distractors
  offer thoroughness, breadth of change and a blanket rule) and **Q22** (feedback batching — the axis is
  whether the issues interact; distractors offer severity order, file order, and mechanical-vs-substantive,
  which is the exact wrong axis picked on Exam 17 Q54).
- **Scenario draw: the last unused feasible 4-of-6.** After this paper the only unused draw remaining is
  CS+CG+MR+DP, which is infeasible — it contains no D4-primary block against a 12-question D4 quota. The
  draw is D1-tight (CS is its only D1-primary block against a 16-question D1 quota), which is why block 1
  carries 7 D1 questions and no D4 at all.
- **A process failure worth recording, and its fix.** The first draft passed dedup against an 886-stem
  ledger and then **failed the archetype gate with 27 collisions against Exams 17 and 18** — the ledger was
  hand-built from EXAM-LOG Exams 2–16 and predated both papers, so the two most recent exams were invisible
  to the check that exists to catch exactly this. The gate caught what the check missed. **Fix: the ledger
  is now rebuilt from `drill/deck/gen/mock-qbank.json`**, which the drill pipeline parses from every
  mock-exam HTML on disk, so it cannot go stale again — 1,156 stems across Exams 2–18 plus the community 76.
  Twenty-seven stems were rewritten and **seven questions replaced outright with different corpus sections**
  (Q23, Q30, Q31, Q38, Q54, Q58, Q60) rather than reskinned.
- **Slogan-breaker worth flagging:** Q30 inverts the edit-recovery point Ram missed on Exam 17 Q53. Here
  read-plus-write **is** correct, because six byte-identical blocks leave neither a wider anchor nor
  replace-all able to isolate one. The corpus calls it the last-resort fallback, and this is the case it
  is reserved for.
- **Gate:** all 7 checks pass — 0 archetype collisions against 1,073 prior stems, 0 intra-paper, stem median
  51, inline token rate 21.7%, letters A13 B13 C13 D13.

### Questions Used (deduplication ledger for Exam 20+)

1. [D1] A developer's loop sends the conversation, reads `stop_reason`, executes the requested tool when it is
   `tool_use`, and sends the conversation again. It branches correctly on every value. Yet on multi-step requests the
   agent asks for the same lookup two or three times before giving up. The tool executes successfully each time and
   its output is logged. What is missing from the loop?
2. [D2] Every resolved conversation must end with a structured outcome record. Three tools write one —
   `record_resolution`, `record_deflection` and `record_escalation` — and which applies depends on how the
   conversation went, so the calling code cannot know in advance. About one conversation in nine ends with the agent
   summarising the outcome to the customer in prose and writing no record at all. Which `tool_choice` setting fits?
3. [D1] The triage subagent is asked to assess whether a disputed charge falls inside the contract's fair-use terms.
   It returns assessments that ignore the customer's tariff and the contract start date, both of which the main agent
   established earlier in the conversation. Its prompt reads: 'Assess whether the disputed charge is covered by fair
   use.' What is the fix?
4. [D5] Disputes that run past fifteen turns start to go wrong: the agent restates the disputed amount to the nearest
   pound and once quoted a contract start date a month out. History is compacted by re-summarising the whole
   conversation every five turns. Which change addresses the cause?
5. [D1][select-2] Releasing a PAC code so a customer can port their number away requires a recorded security check
   first — an absolute rule the regulator audits. The instruction to run that check sits in the system prompt. A
   complaint investigation this month surfaced nine codes released in the past quarter with no check against them.
   Select TWO changes that make the requirement deterministic.
6. [D2] `apply_credit` accepts any amount. Policy caps agent-issued credits at £150, and the team enforces it with a
   nightly reconciliation job that finds over-limit credits and reverses them. Last month it reversed nine, and four
   customers had already been told their account was settled. What is the correct change?
7. [D1] For disputes spanning several charges the agent spawns three triage subagents. On a dispute covering roaming,
   a handset instalment and an early-termination fee, the returned assessment addresses roaming from three angles and
   never mentions the other two. All three subagents completed and each returned a careful assessment. Where is the
   defect?
8. [D2] Requests to see a bill are split roughly evenly between `read_contract` and a billing tool. The descriptions
   read: `read_contract` — 'returns account documents', and `read_invoice` — 'returns account documents'. A developer
   proposes adding a routing step ahead of the agent that inspects the request and picks the tool. What should be done
   first?
9. [D3] Three things need to reach Claude Code in the agent's repository. A logging convention applies to every
   session. A set of redaction conventions applies only when editing the 60 transcript-handling files, which sit
   across a dozen directories. A quarterly compliance-review procedure runs about four times a year on request. Which
   arrangement is correct?
10. [D1] The retention desk receives handoffs as a single line reading `escalate: early-termination fee disputed`.
   Nobody on that desk can see the conversation, so each one opens by asking for the account number, the amount and
   what was already offered. Post-handoff handling time averages fourteen minutes against a six-minute target. What
   should the payload carry?
11. [D2] `change_plan` returns `{"isError": true, "message": "Change not permitted"}` for two unrelated situations:
   the account is inside a minimum-term commitment, and the platform's plan catalogue is temporarily unreachable. The
   agent retries both three times and then tells the customer their plan cannot be changed. What must the responses
   carry?
12. [D5][select-2] Escalation volume is 29% against a 20% target, and a review finds the queue full of routine plan
   changes while three genuine policy gaps stayed with the agent for eleven turns. Escalation currently fires on a
   sentiment score and on the agent's self-reported confidence. Select TWO triggers that should replace them.
13. [D1] A multi-charge dispute needs three assessments: fair-use coverage for roaming, the remaining instalment
   balance, and the termination fee calculation. None depends on the others' findings. The main agent currently spawns
   the first triage subagent, waits for it, spawns the second, and so on. Handling time on these disputes averages
   four minutes. What should change?
14. [D1] On a dispute needing all three assessments, the instalment-balance subagent fails because the finance
   platform is unreachable. The other two completed. The current handler abandons the dispute and escalates it with no
   findings attached. What should it do instead?
15. [D2] The triage subagent needs to read the specific contract the main agent has identified. It currently holds
   `lookup_account`, described as 'searches accounts by any field and returns matching records'. Review finds it has
   retrieved neighbouring accounts on a shared address and, once, a record matching only a partial surname. How should
   the tool be scoped?
16. [D3] Two refinement problems land in the same week. In the first, the team knows exactly what a generated
   migration file should look like and Claude keeps producing a variant ordering. In the second, they are adding
   support for a scheduling standard none of them has worked with and cannot say what the implementation should
   contain. Which techniques fit, and on what basis?
17. [D5] Two constraints are agreed in the opening minutes of a long session: one adapter keeps its public signature,
   and a particular date library is off limits. Around turn eighteen a change lands that alters the signature and
   imports the banned library. Neither constraint was removed from the conversation and the context limit is nowhere
   near. What is the effective mitigation?
18. [D2] The agent holds a `run_command` tool described as 'runs a shell command in the repository root'. A weekly log
   review flags commands that touched the deployment manifests or reached the network, and an engineer reverts
   anything inappropriate. Two reverts last month were of commands that had already pushed a manifest change to the
   staging cluster. What is the correct change?
19. [D3] A `/release-notes` command should reach the whole team on clone. Its author has it working; three colleagues
   who pulled the same branch see no such command, and `/memory` on their machines lists nothing by that name. The
   file sits at `~/.claude/commands/release-notes.md` and its frontmatter parses cleanly. What is the fix?
20. [D5][select-2] Two and a half hours into a session that has traced the booking flow across roughly sixty files,
   answers are getting vaguer and one referred to a helper renamed an hour earlier. The engineer has another two hours
   of work planned on the same area. Select TWO steps that fit.
21. [D1] An expensive trace of the booking flow has just finished. The team now wants to weigh two idempotency designs
   — a request-key table against a natural-key upsert — and needs each judged on its merits rather than against
   whichever was examined first. Both should begin from the completed trace. What mechanism fits?
22. [D3] A generated scheduler module has four problems: it uses local time where the spec requires UTC, one helper
   duplicates an existing utility, the retry count is hard-coded, and the file name breaks the repository convention.
   Switching to UTC changes which helper is appropriate, and removing the duplicate helper changes where the retry
   count is configured. How should the feedback be delivered, and on what basis?
23. [D4] A new triage step is being specified. It reads an incoming request and either points the engineer at existing
   documentation, which needs no tool, or opens a repository search to locate the relevant module. Both outcomes are
   legitimate and the split runs about even. Which `tool_choice` setting should the step be built with?
24. [D2] Before renaming a configuration key, the agent must find every place `poll_interval_ms` is read. It runs a
   path search for `**/*poll_interval*` and reports one file, whose name contains the key. The key is read in fourteen
   places. What went wrong, and what is the right approach?
25. [D5] A design conversation is approaching the context limit. An engineer proposes trimming the oldest quarter of
   turns from each subsequent request, on the reasoning that recent turns already carry the current state. The trimmed
   range contains the agreed idempotency strategy and the list of endpoints excluded from it. What is wrong, and what
   should replace it?
26. [D1] 'Trace every path that writes a booking' is handed to a subagent. A colleague objects that one investigation
   cannot be parallelised, so the delegation buys nothing. What is the stronger argument for delegating it anyway?
27. [D3][select-2] The team is deciding where three pieces of guidance should live: a naming rule that must shape
   every edit anywhere in the repository, and a six-step incident-replay procedure run a few times a month on request.
   Select TWO statements that are correct.
28. [D5] Decisions taken weeks ago keep having to be re-argued: why the upsert was chosen, which retry library was
   rejected, what ruled out the second caching layer. Sessions start fresh each morning and those decisions live only
   in old transcripts nobody opens. What works?
29. [D1] A quality sweep over 35 service modules runs as a single pass. The first several modules come back with
   specific, located findings and the rest with one or two general remarks. An engineer argues that naming the five
   required checks explicitly in the prompt removes any need for a multi-pass design. What is the flaw?
30. [D2] A generated file declares the same four-line configuration block at the top of each of its six sections, byte
   for byte, and the third one must change. Widening the anchor pulls in more of the identical block and still matches
   six times; a replace-all would change all six. What is the correct next step?
31. [D3] The repository root `CLAUDE.md` says commit messages use the imperative mood. A `CLAUDE.md` inside
   `services/` says they must carry a ticket reference. An engineer working in `services/` assumes the nearer file
   replaces the root one and drops the imperative mood. What actually happens when both files are in scope?
32. [D4] The compliance step must emit a signed attestation, and exactly one tool does that — `sign_attestation`,
   whose output the promotion gate reads. A second tool, `draft_attestation`, exists for previewing wording during
   development. Runs occasionally call the draft tool instead, or return a prose summary, and the promotion gate then
   finds nothing to read. Which `tool_choice` setting is correct?
33. [D3] The repository ships a `/review-pr` skill at `.claude/skills/review-pr/SKILL.md`. One engineer has their own
   `/review-pr` skill at `~/.claude/skills/review-pr/SKILL.md` with different checks. On their machine the pipeline's
   local dry-run produces different findings from CI. What explains it?
34. [D1] The pre-merge reviewer runs four checks. On one pull request the licence check fails because the licence
   service is unreachable, after the correctness, test-coverage and style checks have completed with findings. The
   current handler abandons the run and posts nothing. What should it do?
35. [D4][select-2] Findings come back through a tool call whose schema types every field and forbids properties it
   does not declare. The pipeline still rejects some payloads downstream. Select TWO defect classes that pass the
   schema and need separate validation.
36. [D4] A validator confirms that each finding's `line` sits inside a changed hunk of the file it names, and about 7%
   do not. The current retry re-sends the original prompt verbatim, and the second attempt fails at roughly the same
   rate. What should the retry carry?
37. [D3] The pipeline definition must move from one CI provider to another. The replacement's syntax is documented,
   but the secrets model differs in ways nobody has mapped, two custom steps may have no equivalent, and about 25
   workflow files change. How should Claude Code be used?
38. [D1] The pipeline orchestrator spawns one subagent per check. An engineer proposes letting the coverage subagent
   send its per-file numbers straight to the correctness subagent, which could then weight its findings, rather than
   both reporting up and the orchestrator passing the numbers down. What is the objection?
39. [D4] The reviewer flags pull requests for 'inadequate test coverage'. Two engineers auditing the same week's flags
   disagreed with the reviewer on about a third of them and with each other on a similar share. The instruction reads:
   'Flag anything where testing looks thin.' What is the correct revision?
40. [D3] The repository holds a set of conventions that apply only to the 30 workflow files under
   `.github/workflows/`, and a commit-message convention that applies to everything. Both currently sit in the project
   `CLAUDE.md`, and per-session token usage has climbed. What is the correct restructuring?
41. [D1] The pre-merge reviewer is configured with the same tool set as the team's development agent, which includes
   writing files and pushing branches. It has never used them. A reviewer argues that leaving them costs nothing since
   the prompt only ever asks for a review. How should the reviewer’s tool set be decided?
42. [D3][select-2] The pipeline's first attempt at running the reviewer produced no output and was killed by the
   runner's fifteen-minute timeout, and a later attempt applied none of the repository's conventions. Select TWO
   changes that address these two failures.
43. [D4] Pull requests touching more than a dozen files come back uneven: the first files get located, specific
   findings and the last get a line each, and a defect spanning a changed interface and its callers in another file
   went unreported twice last month. The review runs as one pass over the diff. What architecture fixes this?
44. [D1] The reviewer has run the same four checks in the same order for five months. None consumes another's
   findings. An engineer proposes replacing the sequence with a coordinator that reads the diff and decides which
   checks are worth running. Should the team adopt it?
45. [D2] Promotion always fetches the build manifest, verifies its signature, then records the promotion — in that
   order, every time. Logs show a promotion recorded with no verification between them, and another where the
   signature checked was from a manifest fetched two steps earlier. An engineer proposes folding all three into one
   `promote_build` tool. Is that right?
46. [D4] Four extractors exist, one per document type, and the pipeline cannot tell which type a page carries until
   the model reads it. Because a structured record is mandatory, the team set `tool_choice` to `{"type": "tool",
   "name": "extract_application"}`. Records now arrive for every page and roughly 40% of them are budget pages and
   letters parsed as application forms. What is the correct setting?
47. [D5] A validation exercise puts field-level accuracy at 96% over 2,500 records, and the team proposes auto-
   confirming everything above the confidence cut-off. Asked for the number broken down, the exercise shows
   application forms and declarations in the mid-nineties and budget exports — 7% of volume — at 58%. What does that
   establish?
48. [D4] The extraction schema marks all nine fields required, including `co_applicant_name` and
   `previous_award_reference`. Spot checks find plausible names and well-formed reference codes on applications that
   name no co-applicant and cite no previous award. What schema change addresses this?
49. [D5] The application form states a project start date of 1 April and a supporting letter from the host institution
   states 1 June. Both are legitimate parts of the pack, and the funding window makes the two dates lead to different
   eligibility outcomes. What should the extraction output do?
50. [D4][select-2] Records are produced through a tool call with a JSON schema, and a validation layer runs
   afterwards. The team is deciding what each layer should own. Select TWO checks that belong in the validation layer
   rather than the schema.
51. [D1] Applications the pipeline cannot safely complete should go to a human. The current rule sends anything the
   model reports low confidence on. The queue has filled with routine applications while two packs carrying a
   declaration format the pipeline has no extractor for went through untouched. What should trigger a handoff instead?
52. [D4] A single prompt asks the model to identify each document in the pack, pull the fields belonging to each,
   check the budget export against the amount requested on the form, and recommend an eligibility outcome. Output
   quality is poor and no failure can be traced to a particular part of the work. What is the correct restructuring?
53. [D2] The extraction tool's input schema declares `funding_stream` as a free-text string, and it arrives with
   eleven spellings of the same three streams. A separate field, `panel_ref`, is populated inconsistently because
   nobody can tell from the schema what it should hold. What is the correct pair of changes?
54. [D4] An overnight run submits 3,000 extraction requests as a batch. When the results arrive, 41 have failed and
   the team cannot tell which applications they belong to, because the reassembly step matches results to inputs by
   their position in the returned array. What discipline was missed?
55. [D5] The panel view runs everything together as prose: the institution's supporting narrative, the budget lines
   with their amounts, and the four eligibility clauses in play. Panel members report they cannot check the arithmetic
   without transcribing it and keep scrolling back to find clause wording. What should change?
56. [D3] The repository's `CLAUDE.md` opens with four paragraphs on the funding programme's history, moves to the
   record-schema conventions, returns to background on how the panel works, and closes with the rule that every
   extractor change ships with a fixture. Engineers report the fixture rule is frequently not applied. What is the
   most likely problem?
57. [D2][select-2] A reconciliation subagent must compare the budget export against the amount requested on the form.
   It currently holds a `query_records` tool described as 'runs a query against the assessment database'. Review finds
   it has read records for other applicants and, once, an internal audit table. Select TWO changes that follow the
   corpus.
58. [D4] Award dates reach the assessment system in four shapes — `2026-04-01`, `01/04/2026`, `1 Apr 2026` and `April
   2026` — depending on which document the extractor read. Downstream comparison logic handles the first and mis-
   orders the rest. Where should the normalisation happen?
59. [D1] Budget exports of around 40 pages are handled by splitting them into five-page batches, extracting each batch
   on its own, and concatenating the results. Extraction inside a batch is accurate. Across the whole export, lines
   that continue over a batch boundary appear twice and the running subtotals no longer reconcile. What is missing?
60. [D3] The team wants `/reprocess` to take an application reference and re-run the pipeline for it, so an assessor
   can type `/reprocess GR-2026-0481`. The command file currently hard-codes one reference for testing. How is the
   reference passed in?

---

## Exam 14 — SCORED 2026-08-15 (49/60, 835)

**File:** mock-exams/CCA-Prep_MockTest-14_v1.html
**Attempt date:** 2026-08-15 | **Score source:** results-json (full per-question data) | **Total time:** 36:00 of 120 (36s/question)
**Total score:** 49 / 60 correct (estimated scaled: 835 / 1000; pass line 720)
**Item formats:** single-answer 40/47 (85.1%) · multiple-response 9/13 (69.2%)

### Domain Breakdown
| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 14 | 88% | no |
| D2 Tool Design & MCP | 11 | 9 | 82% | no |
| D3 Claude Code Config | 12 | 8 | 67% | no |
| D4 Prompt Engineering | 12 | 11 | 92% | no |
| D5 Context Management | 9 | 7 | 78% | no |

### Block Breakdown
| Block | Scenario | Correct |
|---|---|---|
| 1 | Multi-Agent Research System | 14 / 15 |
| 2 | Developer Productivity with Claude | 11 / 15 |
| 3 | Claude Code for Continuous Integration | 12 / 15 |
| 4 | Structured Data Extraction | 12 / 15 |

This is the calibration paper's own reckoning — generated 2026-08-11 under the fresh archetype ban, but
attempted last, on 2026-08-15, after Exams 12, 13 and 17 were already scored. So it carries none of the
targeting those three papers' Professor's Notes asked for (Exam 19 does; Exam 14 predates all of it), and
its result reads as a clean second data point on misconceptions those notes already named, plus new
findings this paper alone could surface.

### THE FINDING: the D2 §2.8 composite-tool trade-off is now a five-time miss

The Exam 14 generation record flagged this in advance: "D2 §2.8 (composite tool vs prompt bundling) has
been missed on Exams 5, 8, 10 and 11 ... Exam 10 Q6 and Exam 11 Q9 measure 0.717 Jaccard — it was
substantially the same question each time, so a wrong mental model was re-tested rather than re-taught,"
and built Q26 from the opposite end specifically to test whether the mental model itself, not the
memorised stem, was wrong. It was.

Q26 (select-3, 105s): correct = {composite returns unneeded transfer history, prompting to bundle saves
the round-trip without fixing the composition, composite hides the composition so each new pattern needs
a new tool or an over-fetch}. Picked = {those first two, plus "composite tools are always preferable to
prompt-level bundling once a pairing is established"} — which **inverts the corpus's stated preference**
rather than merely missing a fact. The generation note's closing line — "the recalled slogan does not
carry the item" — predicted exactly this outcome. Promote D2 §2.8 from "a section to cover" to the
tool_choice-any-vs-auto tier: a five-paper error that survives reskinning needs the same treatment that
finally closed that one on Exam 17 — several items, different scenarios, testing the discrimination in
both directions (when a composite earns its keep vs. when it locks in a cost).

### THE FINDING: the `.claude/rules/` reflex — sixth instance, and doubled in one paper

Confirmed across Exam 12 (Q1, Q56), Exam 13 (Q41) and Exam 17 (Q41) as the default reach whenever a
question smells like "where should this live?". Three rounds of Professor's Notes have named it. It did
not close, and this paper is the first time it fired twice:

- **Q18** (D3 §3.1, 23s) — the agent applies a convention in some sessions and not others; the first
  diagnostic step is `/memory`, to check what actually loaded. Picked "move the convention into
  `.claude/rules/`" — choosing a destination before diagnosing what is loaded, the exact trap Exam 13's
  note named.
- **Q38** (D3 §3.8, 35s) — a CI-invoked test-generation run needs project standards plus the existing
  test suite in context; picked a `.claude/rules/` file scoped by glob. This is a **new surface** for the
  same reflex: not "where should this guidance live" but "what supplies missing context to a run", and
  `.claude/rules/` was reached for anyway.

Two of D3's four misses this paper are one misconception wearing two section tags (§3.1 and §3.8). Written
feedback after three prior papers has not moved it; the lever now needed is not more coverage but a
retrieval cue Ram can apply under time pressure — both misses here came in under 25 and 40 seconds, close
to this paper's 36s average, so it is not being caught even on unhurried items.

### THE FINDING: discard-the-mechanism instead of the narrow adjustment

Two misses, different domains, same shape — offered a working (or mostly-working) mechanism that needed a
small targeted change, and chose to throw it out instead:

- **Q19** (D1 §1.16, 19s) — a call-graph mapping is still largely valid; three of forty files changed
  overnight. Correct: resume the session and name the three changed files for targeted re-analysis.
  Picked: start fresh and inject a summary — the move reserved for when prior context is *broadly* stale,
  discarded here when it was mostly current.
- **Q54** (D5 §5.5, select-3, 42s) — a `PostToolUse` hook trims OCR output too far, losing the bounding-box
  data reviewers need. Correct: widen the hook's field list. Picked, among three right answers, "removing
  the hook is correct, since lost provenance matters more than context pressure" — trading the context
  saving back away wholesale instead of keeping it and adding the two missing fields.

Both times the available fix was a small edit to what already existed; both times the pick was full
removal or full restart.

### Secondary: reject the ambiguous record rather than encode it

**Q57** (D4 §4.5, 72s — the slowest miss on this paper) — `commodity_grade` is a six-value enum; older
certificates sometimes carry regional names matching none of the six. Correct: add an `"unclear"` member
plus a companion free-text field, preserving what the document said. Picked: keep the enum and add a
validation rule that rejects records whose grade is uncertain — turning an extractable record into a
pipeline failure. This is the same shape as Exam 13 Q19 (picked "return an error instead of a partial
document" over "expand the description"): defaulting to hard failure when a softer, informative outcome
was available. Two instances, three papers apart, is not yet a confirmed pattern on its own — worth a
single well-placed item next time rather than a full family.

### Multiple-response: every miss this paper was a majority-right answer that scored zero

4 of 13 multi-response items missed, and all four have the identical shape — most of the correct set
picked, with exactly one wrong option swapped in for the one that was missed:

| Q | Correct | Picked | Right kept | Wrong swapped in |
|---|---|---|---|---|
| 26 | A,B,C | A,B,D | A,B | D (inverts the rule) |
| 45 | A,B | A,E | A | E (verification, not TDD) |
| 49 | A,B | B,C | B | C (samples the wrong end of the distribution) |
| 54 | A,B,C | A,B,D | A,B | D (discard instead of adjust) |

Exam 17 found this shape on 2 of 2 misses; here it is 4 of 4. All-or-nothing scoring means "understood
three of four correct components" and "understood none" score identically, and on this paper that erased
what would otherwise have been 8 additional correct components across four items.

### Weakest domain — D3, confirmed on two consecutive attempts

By attempt chronology (12 → 13 → 17 → 14), the immediately preceding scored paper is Exam 17, where D2
(73%) and D3 (75%) were ruled tied and neither confirmed alone. Here D2 recovered to 82% and **D3 alone is
weakest at 67%** — the two-consecutive-attempt gate is now met for D3 specifically, on a cleaner signal
than Exam 17 produced.

It does not concentrate the way Exam 17's D2 did, though: the four D3 misses span four different sections
(§3.1, §3.7.2, §3.8, §4.11-tagged-D3) rather than two. But two of those four (§3.1, §3.8) are the same
`.claude/rules/` reflex under different tags, so the *section* spread overstates how spread out the
*misconception* actually is. Base quota stands per convention (D3 stays at 12) unless Ram asks for the
+4 bump at the next generation — recording the confirmation, not applying it.

### Professor's Note — Intent for Exam 20

Written after Exam 14 (attempted 2026-08-15, generated 2026-08-11 — a delayed sitting). Based on
results-json. Exam 19 (generated 2026-08-14, not yet attempted) already carries the prior note's asks —
the guarantee-strength ladder, hook-framed prevention-vs-detection, and D3 §3.7 axis-error items — so this
note targets what only Exam 14 surfaced, and does not re-litigate those pending checks.

- Misconceptions revealed:
  1. **D2 §2.8, composite tool vs prompt bundling — missed a fifth time, and the mental model inverted, not
     just forgot.** Give it the multi-item, both-directions treatment that closed the `tool_choice` error:
     one item where a composite earns its cost, one where a new access pattern breaks it, one where
     bundling is recommended and a composite would over-fetch.
  2. **`.claude/rules/` as the default reach — sixth instance, first double-instance in one paper, and now
     spans two distinct question surfaces** (where should this live / what supplies missing context).
     Three papers of written feedback have not closed it; the fix needed is a retrieval cue, not more
     coverage.
  3. **Discard-the-mechanism over the narrow adjustment** (Q19, Q54) — offered a small targeted edit,
     chose full restart or full removal instead, in two different domains.
  4. Secondary and not yet confirmed: **reject-the-ambiguous-record over encode-it** (Q57, echoing Exam 13
     Q19). One more instance would confirm a pattern.
- Weakest this paper: **D3 at 67%, confirmed weak two consecutive attempts** (tied on Exam 17, alone here).
  Spans four sections but two of the four misses share one misconception. Base quota stands; flagged for
  Ram to decide on the +4 bump.
- Intent for next paper: rebuild D2 §2.8 as a 3-item, both-directions family before anything else — it is
  now the corpus's oldest unresolved error at five papers, older than the `tool_choice` error was when it
  finally got that treatment. Keep `.claude/rules/` items arriving asked from an angle that is not "where
  should this live" (Q38's "what supplies context" framing already proved a fresh surface still catches
  it). Give the discard-vs-adjust shape one explicit item.
- Watch next: whether D2 §2.8 closes the way `tool_choice` did once it got dedicated, multi-directional
  treatment, or whether it is a durable habit that needs more than three items to move — the prior error
  took exactly that treatment once (Exam 17) to close.

---

## Exam 19 — SCORED 2026-08-16 (56/60, 940)

**File:** mock-exams/CCA-Prep_MockTest-19_v1.html
**Attempt date:** 2026-08-16 | **Score source:** results-json | **Total time:** 44:27 of 120 (44.5s/question)
**Total score:** 56 / 60 correct (estimated scaled: 940 / 1000; pass line 720)
**Item formats:** single-answer 49/52 (94%) · multiple-response 7/8 (88%)
**Mode:** Exam Mode — no per-question feedback taken; first sitting run under real exam conditions (see `EXAM-MODE-DESIGN_v1.md`).

### Domain Breakdown
| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 16 | 100% | no |
| D2 Tool Design & MCP | 11 | 10 | 91% | no |
| D3 Claude Code Config | 12 | 12 | 100% | no |
| D4 Prompt Engineering | 12 | 9 | 75% | no |
| D5 Context Management | 9 | 9 | 100% | no |

Blocks: Customer Support 15/15 · Code Generation 14/15 · CI 14/15 · Structured Extraction 13/15.

### Observations

Highest score on record, comfortably clear of the pass line, and the first paper taken with zero per-question
feedback — the score holds under real exam conditions, not just under the tool's usual hand-holding. All four
misses cluster in D4 (3 of 4) and D2 (1 of 4); D1, D3, D5 went clean.

1. **Q23 (D4 §4.6) — the `tool_choice` guarantee-strength ladder, over-specification direction, missed on
   first real test.** Exam 19 was built specifically to test this ladder in both directions (see its own
   generation notes) because the *under*-guarantee error (preferring `auto`/`any` when a firm guarantee was
   needed) closed cleanly on Exam 17. Q23 tested the opposite direction — a step where roughly half the
   requests need no tool call at all, so `auto` was correct — and picked `any` instead, forcing a tool call
   on every request. The under-guarantee error is closed; the over-guarantee error is now an open,
   **confirmed-on-first-look** item, not yet worked the way `tool_choice` under-guarantee was.
2. **Q58 (D4 §4.5) — prevention vs. after-the-fact repair, a repeat of the Exam 17 pattern in a new
   context.** Four date formats reaching a comparison step; the fix is typing the extraction schema so only
   one shape is well-formed, not a post-extraction pass that rewrites whatever arrived. This is the same
   shape as Exam 17 Q19 (hook choice) — pick the downstream fix-up over the upstream constraint — and this
   paper's own generation notes flagged it as a deliberate fresh-frame retest of that exact miss. It was
   missed again. Two data points, two different surfaces (hooks, schema typing) — this is now the strongest
   candidate for "durable habit, not a knowledge gap" in the corpus.
3. **Q35 (D4 §4.5/§4.7, select-2) — schema-enforced structure mistaken for semantic validation scope.**
   Correctly picked the out-of-range line number (needs cross-field validation) but also picked an
   undefined-property payload, which the schema already rejects at the boundary — swapped in for the actual
   second answer, a severity value contradicting its own explanation. The miss is not "didn't know
   semantic checks are needed," it's misjudging which defect classes a strict schema already closes off.
4. **Q53 (D2 §2.1) — parameter description vs. worked examples.** Picked enum-plus-examples over
   enum-plus-description for a field the model was filling in blind. Examples demonstrate a pattern; a
   one-line description states what the field means, at the point the model needs it. First instance of
   this specific framing in the log — not yet a repeat, flagged for one more data point.

**Weakest domain:** D4 at 75% (9/12) — **suspected, single-sitting.** Not yet a confirmed 2-exam trend: Exam
17's weakest was D2/D3 (tied, 73%/75%), and D4 was Exam 17's second-strongest domain (83%). D4 dropping to
75% here while carrying 3 of this paper's 4 misses is worth watching, not yet acting on as a domain-quota
change.

### Professor's Note — Intent for Exam 20

Written after Exam 19 (attempted 2026-08-16), superseding the Exam-14-based note above as the latest
guidance — Exam 19 has now supplied the real data the prior note was written without. Real exam sitting is
2026-08-18; this note is written for whenever a next paper is generated, not necessarily before Tuesday.

- Misconceptions revealed:
  1. **D4 §4.6, `tool_choice` over-specification (Q23) — new, first instance.** The under-guarantee
     direction is closed (Exam 17); the over-guarantee direction (a stronger-than-needed setting applied to
     a step with nothing mandatory to guarantee) is open on a single data point. Give it one more
     both-directions item before concluding anything.
  2. **D4 §4.5, prevention vs. after-the-fact repair (Q58) — second confirmed instance, two different
     surfaces (Exam 17 hooks, Exam 19 schema typing).** This is now the corpus's clearest repeat-miss
     candidate. Treat it the way the `tool_choice` under-guarantee error was treated once it had two clean
     instances: dedicated multi-item, both-directions coverage before anything else.
  3. **D2 §2.1, parameter description vs. examples (Q53) — new, first instance.** Watch for a repeat before
     treating as a pattern.
- Weakest this paper: **D4 at 75%, suspected not confirmed** (Exam 17's weakest was D2/D3, not D4). One more
  low D4 score would confirm; one clean D4 score would mark this as sitting-specific noise. Base quota
  stands either way.
- Intent for next paper: lead with D4 §4.5 prevention-vs-detection as a dedicated multi-item family (it now
  has the same two-instance, two-surface shape that got `tool_choice` closed) — this is the corpus's
  strongest open candidate, ahead of the D2 §2.8 composite-tool item this note's predecessor flagged. Give
  the `tool_choice` over-specification direction (Q23) one clean-shot retest in a different scenario before
  drawing a conclusion either way.
- Watch next: whether D4 §4.5 closes the way `tool_choice` under-guarantee did (Exam 17, one dedicated
  multi-directional treatment), given it's now shown the identical two-instances-then-treat shape.

---

## Insights Round 4 — 2026-08-16 (retroactive — was due 2026-08-15, run here as part of a full
historical review before Exam 20's generation)

**Process note, stated plainly first:** this round fires at every non-zero multiple of 3 scored exams. By
attempt chronology the count reached 12 when Exam 14 was scored on 2026-08-15 — the round was due that
day and no session ran it. Nothing downstream was corrupted by the gap (each exam's own Professor's Note
still fired on schedule), but the deeper 3-exam trend layer went dark for one cycle. Caught and run now as
part of the review this session was asked to do. Window: **Exam 13 → Exam 17 → Exam 14**, in attempt
order (12→13→17→14; Exam 9 and Exam 11's earlier out-of-order attempts don't affect this window).

| # | attempted | raw | scaled | mins | D1 | D2 | D3 | D4 | D5 | weakest |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 2026-07-11 | 45/60 | 775 | 736 | 75% | 45% | 75% | 83% | 100% | D2 |
| 5 | 2026-07-11 | 52/60 | 880 | 32 | 94% | 73% | 92% | 75% | 100% | D2 |
| 6 | 2026-07-12 | 49/60 | 835 | 260 | 93% | 73% | 83% | 83% | 71% | D5 |
| 7 | 2026-07-16 | 55/60 | 925 | 325 | 94% | 100% | 83% | 83% | 100% | D3/D4 |
| 8 | 2026-07-28 | 52/60 | 880 | 35 | 94% | 91% | 75% | 75% | 100% | D3/D4 |
| 10 | 2026-07-29 | 54/60 | 910 | 39 | 94% | 82% | 83% | 92% | 100% | D2 |
| 9 | 2026-08-09 | 49/60 | 835 | 42 | 88% | 64% | 92% | 83% | 78% | D2 |
| 11 | 2026-08-10 | 55/60 | 925 | 40 | 94% | 91% | 92% | 92% | 89% | D5 |
| 12 | 2026-08-11 | 53/60 | 895 | 43 | 93% | 87% | 83% | 83% | 100% | D3/D4 |
| 13 | 2026-08-12 | 57/60 | 955 | 36 | 100% | 91% | 92% | 92% | 100% | D2 (nominal — see below) |
| 17 | 2026-08-14 | 51/60 | 865 | 38 | 94% | 73% | 75% | 83% | 100% | D2/D3 (tied) |
| 14 | 2026-08-15 | 49/60 | 835 | 36 | 88% | 82% | 67% | 92% | 78% | D3 |

**All-time mean / this-round's-last-3 mean (Exam 13, 17, 14):** D1 91.8 / 94.0 · D2 79.3 / 82.0 ·
D3 82.7 / 78.0 · D4 84.7 / 89.0 · D5 93.0 / 92.7.

**1. D3 is confirmed weak across this window, and the confirmation is real, not a tie artefact.**
Exam 17 tied D2/D3 at 73%/75%; Exam 14 broke the tie cleanly with D3 alone at 67% (D2 recovered to 82%).
Per the tie-handling rule (exactly one of the tied domains matches the next exam's unambiguous weakest →
confirmed), **D3 crossed the confirmed-weakness bar on 2026-08-15.** It does not concentrate in one
section — the four Exam 14 misses span §3.1, §3.7.2, §3.8, and a D3-tagged §4.11 item — but two of those
four (§3.1, §3.8) are the same misconception under different tags (see finding 2), so the section spread
overstates how spread out the actual misconception is.

**2. The `.claude/rules/`-as-default-reach trap is now six instances and the single most entrenched
pattern in the corpus outside D2 §2.8.** Confirmed in this window at Exam 12 (Q1, Q56), Exam 13 (Q41), and
Exam 17 (Q41); Exam 14 fired it **twice in one paper** (Q18 — reaching for a rules file before running
`/memory` to check what's actually loaded; Q38 — reaching for a rules file to supply missing run context,
a new surface for the same reflex). Three rounds of Professor's Notes named it before this round; it has
not closed. Both Exam 14 instances were answered in under 40 seconds, close to that paper's own average —
this is not a fatigue effect, it is a genuine first-instinct reflex.

**3. Correction to the record, not a score change: Exam 19's confirmed-weakness check used the wrong
comparator.** Exam 19's EXAM-LOG entry (2026-08-16) compared its weakest domain (D4) against **Exam 17's**
weakest (D2/D3, tied) to conclude "not confirmed." Per this project's own standing rule, the comparator
must be the most recent PRIOR scored exam **by attempt date**, and Exam 14 (attempted 2026-08-15) sits
between Exam 17 (08-14) and Exam 19 (08-16) — it is Exam 19's true immediate predecessor, not Exam 17.
Re-run correctly: Exam 14's weakest was D3 (67%); Exam 19's weakest was D4 (75%). **Different domains —
the "not confirmed" conclusion is unchanged.** What changes is the reasoning on record, and one real
finding this correction surfaces on its own:

**4. D3 recovered, and the recovery is unusually credible because it was accidental.** Exam 19 scored D3
at **12/12 (100%)** — a full clean sweep of the domain the confirmed-weakness rule had just flagged the
day before. Exam 19's Professor's Note (written from the Exam 17 comparison, before this correction) never
asked for D3 attention at all, and the paper still came back perfect on it. An untargeted clean score is
stronger evidence of genuine recovery than a targeted one would have been — there was no re-test bias to
discount. Read alongside D5's Exam 6 dip (recovered cleanly by Exam 7) and D2's Exam 9 dip (recovered by
Exam 10/12), this is this project's third instance of the same shape: a single-exam domain dip that
clears on the next full attempt without needing a quota adjustment. **Recommendation: no D3 quota change
for Exam 20.** The specific misconception (`.claude/rules/`-as-default-reach, finding 2) is a different
question from the domain score, though — a reflex six papers deep does not un-happen because one paper's
draw didn't trigger it. One confirmatory item, not a domain-wide push, is the right-sized response (see
Exam 20 targeting below).

**5. Pace remains a non-issue.** 36–38s/question across all three papers in this window, comfortably under
the ~120s/question budget. No domain ran slower than the paper average on any of the three.

**6. Combined with Exam 19's own note, this round changes what Exam 20 should prioritize.** Two targeting
chains were running in parallel and had not been reconciled until this round: the Exam 17→19 chain (D4
§4.5/§4.6, D2 §2.1 — already in EXAM-LOG's "Professor's Note — Intent for Exam 20") and this round's D3
finding, which the Exam 17→19 chain never surfaced because it compared against the wrong exam. Folding
both in, ranked by evidence strength:

1. **D2 §2.8 (composite tool vs. prompt bundling) — 5 misses (Exams 5, 8, 10, 11, 14), the single oldest
   unresolved trap in the corpus,** older than the `tool_choice` under-guarantee error was when it finally
   got dedicated multi-directional treatment on Exam 17. Not carried in Exam 19's note (that chain never
   named it); it belongs at the top given its age.
2. **D4 §4.5 (prevention vs. after-the-fact repair)** — 2 confirmed instances, 2 different surfaces (Exam
   17 hooks, Exam 19 schema typing). Per Exam 19's Professor's Note.
3. **D4 §4.6 (`tool_choice` over-specification direction)** — 1 instance (Exam 19 Q23), needs a clean
   second test before it can be called a pattern. Per Exam 19's Professor's Note.
4. **D2 §2.1 (parameter description vs. worked examples)** — 1 instance (Exam 19 Q53). Per Exam 19's
   Professor's Note.
5. **D3 §3.1/§3.8 (`.claude/rules/`-as-default-reach) — one confirmatory item only,** per finding 4's
   recovery read. Not a domain-wide D3 push; the domain score itself already recovered.

None of this changes the base quota (D1 16/D2 11/D3 12/D4 12/D5 9) — no domain is currently confirmed weak
against its true immediate predecessor. All five items are section-level biases within that fixed quota.

---

## Exam 20 — Generated 2026-08-16

**File:** `mock-exams/CCA-Prep_MockTest-20_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions) — 52 single-answer + 8 multiple-response
**Mode:** Exam Mode (see `EXAM-MODE-DESIGN_v1.md`) — same variant as Exam 19: no per-question feedback,
120:00 countdown, full results/rationale review only after the final question.
**Scenarios drawn:** Multi-Agent Research System; Developer Productivity with Claude; Structured Data
Extraction; Claude Code for Continuous Integration. Rested: Customer Support Resolution Agent; Code
Generation with Claude Code.
**Attempt date:** Not yet attempted
**Score source:** Pending
**Total score:** Pending

**Generation method:** 4 parallel scenario-block sub-agents (orchestration-prompt v10 Phase 4.b.6). All
four stalled simultaneously on first dispatch — a documented infrastructure failure mode, not a task
defect (the same pattern hit Exams 7 and 8; see `GENERATION-INTELLIGENCE.md`). Resumed, not restarted;
all four completed cleanly with no rework needed.

**Key Distinction budget:** none deliberately seeded. This paper was authored by corpus SECTION
(targeting the 5 priorities below), not by KD cycling — the same choice Exam 14 made once the KD tracker
degraded. Recording this explicitly per PB-24's own recommendation, so a future session doesn't have to
guess whether the line's absence means "seeded but unlogged" (Exam 13's actual failure) or "deliberately
authored by section" (this exam's actual case).

**Full historical review preceded generation**, at Ram's explicit request. It surfaced two things no
single-exam Professor's Note had caught on its own — both already fixed above, before this exam was
planned:
1. Insights Round 4 was overdue (due 2026-08-15, never ran) — run retroactively this session.
2. Exam 19's own confirmed-weakness check had compared against the wrong prior exam. Corrected; the
   correction surfaced a real, accidental finding — D3 recovered cleanly (100%) on an untargeted paper
   after being confirmed weak the exam before.

### Block × domain allocation

| Block | Scenario | Primary domains | D1 | D2 | D3 | D4 | D5 |
|---|---|---|---|---|---|---|---|
| 1 | Multi-Agent Research System | D1, D2, D5 | 7 | 4 | 1 | 0 | 3 |
| 2 | Developer Productivity with Claude | D1, D2, D3 | 8 | 5 | 2 | 0 | 0 |
| 3 | Structured Data Extraction | D4, D5 | 1 | 0 | 0 | 8 | 6 |
| 4 | Claude Code for Continuous Integration | D3, D4 | 0 | 2 | 9 | 4 | 0 |
| **Total** | | | **16** | **11** | **12** | **12** | **9** |

Every block's primary-domain minimum exceeds its non-primary maximum (verified programmatically,
`tools/archetype_gate.py` check 4).

**Scenario draw rationale:** rotation would rest both Claude Code CI and Structured Data Extraction
(tied most-used at 13 each), but D4's quota needs a primary-carrying block and D1's quota (16, >15)
needs at least 2 D1-primary blocks — only Multi-Agent Research and Developer Productivity supply those
among the 6. Deliberately drew BOTH D4 carriers despite their higher usage so the two D4 targeting
priorities (below) get genuine both-directions spread across two blocks instead of crowding one —
precedented by Exam 11 doing the same for the same reason. Code Generation stays at 11 (still the
least-used scenario), a natural anchor for Exam 21.

### Correct-answer letter pre-plan (13 single-answer questions per block; 2 multi-response items per
block, at local positions 6 and 12, are exempt)

| Block | Sequence |
|---|---|
| Multi-Agent Research System | C A B C A C B A B D D D A |
| Developer Productivity with Claude | C C B A B B B A C D D A D |
| Structured Data Extraction | C D A D D B C B C A B C A |
| Claude Code for Continuous Integration | C B B A D A C D C A B D D |

Achieved exam-wide tally: A=13, B=13, C=13, D=13 — exact.

### Professor's Note consumed (reconciled from two chains — see Insights Round 4, finding 6, above)

1. **TOP — D2 §2.8** (composite tool vs. prompt bundling), 5 misses (Exams 5, 8, 10, 11, 14), the corpus's
   oldest unresolved trap. Tested both directions: Multi-Agent Research Q7/Q12 and Developer Productivity
   Q21 (opposite polarity — bundling correct, composite would over-fetch).
2. **D4 §4.5** (prevention vs. after-the-fact repair), confirmed on 2 surfaces (Exam 17 hooks, Exam 19
   schema). Three distinct facets in Structured Data Extraction: Q32 (numeric precision), Q38
   (retry-loop-into-enum), Q41 (nullable fields) — none touching Exam 19 Q58's date-format ground.
3. **D4 §4.6** (`tool_choice` over-specification), 1 miss (Exam 19 Q23). Three distinct CI situations:
   Q48, Q53, Q60.
4. **D2 §2.2** (parameter description vs. examples), 1 miss (Exam 19 Q53). Note: the note that named this
   priority mislabeled it §2.1 — corrected during authoring; §2.2 (Tool Description Design) is the
   section that actually grounds this content. One test: Multi-Agent Research Q10.
5. **D3 §3.1/§3.8** (`.claude/rules/`-as-default-reach), one confirmatory item only (Claude Code CI Q52),
   per the D3 recovery finding — not a domain-wide push.

### Fidelity Verification Gate (`tools/archetype_gate.py`, all 7 checks — ALL PASS)

| # | Check | Result |
|---|---|---|
| 1 | No invented names | 0 flagged (2 initial false-positive flags on "Despite"/"Authors" fixed by rewording) |
| 2 | Correct-answer letter tally | Exact 13/13/13/13 exam-wide |
| 3 | Word counts | stem 40/55/78 (median in-band, cap respected); option max 35 (at cap) — 11 stems trimmed for verbosity, facts/citations unchanged |
| 4 | Block vs. primary domains | All four blocks pass with real margins |
| 5 | Inline code/config token rate | 70/240 = 29.2% (within the 15–30% band) |
| 6 | Multiple-response validity | All 8 items well-formed |
| 7 | Archetype collision | 0 collisions against 1,133 prior stems (Exams 2–19 + 76 locked practice stems), 0 intra-paper duplicates |

Each block sub-agent independently caught and rewrote several of its own near-collisions against specific
prior exams before returning (see full sub-agent reports; summarized in the HTML's top comment block).

### Questions Used (for deduplication — see the HTML's own JS comment block for the full 60-stem ledger,
domain-tagged; not duplicated here to keep this entry a reasonable length)

All 60 stems are listed in `mock-exams/CCA-Prep_MockTest-20_v1.html`'s top comment block, under
"QUESTIONS USED (deduplication ledger for Exam 21+)".

---

## Exam 20 — SCORED 2026-08-17 (56/60, 940)

**File:** `mock-exams/CCA-Prep_MockTest-20_v1.html`
**Attempt date:** 2026-08-17 | **Score source:** results-json (full per-question data) | **Total time:**
43:31 of 120:00 (2611s / 60 = 43.5s/question)
**Total score:** 56 / 60 correct (estimated scaled: 940 / 1000; pass line 720) — ties Exam 19 for
second-highest on record, 15 points behind Exam 13's 955.
**Item formats:** single-answer 49/52 (94.2%) · multiple-response 7/8 (87.5%)

### Domain Breakdown
| Domain | Questions | Correct | % |
|---|---|---|---|
| D1 Agentic Architecture | 16 | 16 | 100% |
| D2 Tool Design & MCP | 11 | 11 | 100% |
| D3 Claude Code Config | 12 | 10 | 83.3% |
| D4 Prompt Engineering | 12 | 10 | 83.3% |
| D5 Context Management | 9 | 9 | 100% |

### Block Breakdown
| Block | Scenario | Correct |
|---|---|---|
| 1 | Multi-Agent Research System | 15 / 15 |
| 2 | Developer Productivity with Claude | 15 / 15 |
| 3 | Structured Data Extraction | 14 / 15 |
| 4 | Claude Code for Continuous Integration | 12 / 15 |

Two clean blocks (1, 2 — the two D1/D2-heaviest blocks), all four misses concentrated in the two
D4-primary blocks (3, 4), the exact blocks this exam's targeting brief deliberately loaded with D4 §4.5
and §4.6 content.

### Confirmed-weakness check (comparator: Exam 19, attempted 2026-08-16 — the true immediate predecessor
by attempt date; no exam was attempted between 08-16 and 08-17, so this needs no PB-29-style correction)

Exam 19's weakest domain was **D4 alone, unambiguous, at 9/12 (75%)**. Exam 20's *nominal* weakest is
**D3/D4 tied at 10/12 (83.3%) each** — a tie fails the project's own "unambiguously weakest" bar, so per
the same convention applied to Exam 7/8/12's ties, **confirmed_weakness is recorded as `false`** in
`DASHBOARD-DATA.jsonl`. That is the literal, correct application of the rule to the nominal data — but a
data-quality finding below means the nominal read is probably wrong, and worth stating plainly rather than
letting the boundary case swallow it.

### Finding 1 — NEW, highest-priority: Batch API tool-support is missed twice in this single sitting

Q42 (Structured Data Extraction, select-2) and Q55 (Claude Code CI, single) both test the exact same
underlying fact from `CCA-Prep_Domain-4_v2.md §4.11` — the Message Batches API supports tool definitions
and multi-turn histories (a response can end in `tool_use`); what it cannot do is pause mid-request for
the client to execute a tool and feed the result back. Both were missed:
- **Q42** — correct answers were "batch requests can include tool definitions... may end in `tool_use`"
  and "each request must carry a unique `custom_id`, because results can return in a different order."
  Selected C, D — got the `custom_id`/ordering half right but also picked "results are guaranteed to come
  back in the same order," which directly contradicts the option just selected, and missed the
  tool-definitions option entirely.
- **Q55** — selected "Yes — the Batch API only accepts plain-text prompts, so `flag_license` must be
  dropped" — the exact misconception Q42's correct answer already rules out, missed again 13 questions
  later in the same sitting.

This is a clean, doubly-confirmed gap in one paper, not a coverage question: **the belief that tools
cannot be used inside a batch request at all.** Given the sitting is tomorrow (2026-08-18), this is the
single most actionable thing to review tonight — re-read `CCA-Prep_Domain-4_v2.md §4.11` directly.

### Finding 2 — CONFIRMED a second time: D4 §4.6 tool_choice over-specification

Exam 19 Q23 missed this once (new direction, logged in that Professor's Note). Exam 20 Q48 was the
deliberate clean second test the Exam 19 note asked for — a drafting step where ~60% of findings need no
tool call at all, correct answer `auto`. **Missed again**, selecting `any` (forces a tool call on every
finding, including the self-contained 60% with nothing to look up) after 92 seconds — the longest of the
four misses, so this reads as a considered-and-still-wrong choice, not a rushed guess. Two confirmed
instances now (Exam 19 Q23, Exam 20 Q48), different scenarios, different specific tool_choice values —
**this is now a genuine pattern**, not an isolated miss: over-specifying the guarantee (forcing every call)
when the requirement is "call it only when actually needed." Companion note: Q60, the third D4 §4.6 item
in this same block (targeting the opposite/adjacent facet), was answered correctly — the error is specific
to the "force it every time" direction, not tool_choice in general.

### Finding 3 — D3 §3.7 axis-confusion resurfaces, untargeted

Q58 (feedback-batching: bundle vs. one-at-a-time) was missed by applying a "prioritize by recurrence risk"
axis instead of the corpus's actual discriminator, whether the issues *interact*. This is the same D3 §3.7
area Exam 17 flagged as its "cleanest section gap" (Q50, Q54 — both wrong-axis errors), which then
recovered cleanly to 12/12 on Exam 19 (untargeted — see Insights Round 4, finding 4 above). Exam 20's D3
content was also untargeted beyond one confirmatory item (Q52, `.claude/rules/`-reach, answered correctly).
So the pattern here matches this project's established shape (Exam 19's D5 dip/Exam 6→7, D2 dip/Exam 9→10):
**a section-level gap that both closes and reopens without warning across untargeted papers** — treat one
clean sweep as encouraging, not as "resolved."

### Finding 4 — data-quality: Q55 is domain-mistagged, not a D3 miss

Q55's `domain` field reads `"D3"`, but its stem, all four options, `whyRight`, and all three `whyWrong`
entries cite **exclusively** `CCA-Prep_Domain-4_v2.md §4.11` — zero D3 content appears anywhere in the
question. This is the same underlying fact as Q42 (Finding 1), which is correctly tagged D4. Correcting
the tag moves this one miss from the D3 tally to the D4 tally:
- **D3 corrected: 10 correct / 11 questions = 90.9%** (one fewer question in the denominator; correct
  count unchanged since Q55 was a miss either way)
- **D4 corrected: 10 correct / 13 questions = 76.9%** (one more question in the denominator, still a miss)

Under the corrected read, **D4 is unambiguously alone weakest on Exam 20 at 76.9%**, which — compared
against Exam 19's unambiguous D4-alone-weakest at 75% — **would satisfy the confirmed-weakness bar for two
consecutive exams.** This is presented as a finding, not applied to the structured `confirmed_weakness`
field above, for the same reason this project never lets a generating session silently edit corpus
attribution: the mistag lives in a *shipped exam file*, not the source corpus, and a domain re-tag on a
scored exam should get the same explicit sign-off as any other correction to the record before being
treated as ground truth. Logged as **PB-30** in `GENERATION-INTELLIGENCE.md`'s Open Findings Ledger — the
underlying gap is that `tools/archetype_gate.py` check 4 verifies block-level primary-domain tallies but
never checks a single question's `domain` tag against its own citation content, so a mistag like this one
cannot fail the fidelity gate as it exists today.

### Pace

43.5s/question average, well under the ~120s budget, consistent with every prior sitting. None of the four
misses were fast/rushed (51s, 92s, 43s, 43s — all near or above the paper's own average) — these are
considered-and-wrong errors, not time-pressure errors, which is the same shape this project has found on
every prior miss cluster.

### Professor's Note — Intent for Exam 21

Ranked by evidence strength, for whenever the next paper is generated (see recommendation below on
whether that should happen before the 2026-08-18 sitting):

1. **D4 §4.11 (Batch API tool support)** — 2 misses in one sitting (Q42, Q55), the single cleanest new
   finding this exam produced. Test the "tools work in batch, ordering is not guaranteed, the real limit is
   no mid-request pause-and-resume" fact from a third, still-different angle.
2. **D4 §4.6 (`tool_choice` over-specification — "force every call")** — now 2 confirmed instances (Exam
   19 Q23, Exam 20 Q48) across 2 different scenarios. Needs a third test before calling it fully closed,
   but this is no longer provisional.
3. **D3 §3.7 (feedback-batching axis: interacting vs. independent)** — recurred untargeted after a clean
   Exam 19 sweep. One more untargeted data point (no dedicated item) would help distinguish "genuinely
   fragile" from "normal noise at this sample size."
4. **Fidelity gate gap (process, not content):** `tools/archetype_gate.py` check 4 should be extended to
   verify each question's `domain` tag against its own `whyRight`/`whyWrong` citation sections, not just
   block-level tallies — see PB-30.

**Recommendation for tonight (2026-08-17), given the sitting is 2026-08-18:** do not generate Exam 21.
This project's own repeated finding (Session 19, reaffirmed at Exam 20's generation) is that sitting
existing unattempted papers is more valuable than producing more this close to the exam — and with under
24 hours left, the higher-value use of remaining time is a direct, targeted re-read of
`CCA-Prep_Domain-4_v2.md §4.11` and §4.6, plus `CCA-Prep_Domain-3_v2.md §3.7.4`, rather than a full new
60-question sitting.
