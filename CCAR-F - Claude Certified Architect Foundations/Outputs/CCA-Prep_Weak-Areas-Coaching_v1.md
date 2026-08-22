# CCA-F Weak-Areas Coaching — What You Keep Getting Wrong, and How to Stop

**Prepared:** 2026-07-28
**Grounding corpus:** `CCA-Prep_Domain-1_v2.md` … `CCA-Prep_Domain-5_v2.md`, `CCA-Prep_Key-Distinctions_v1.md`, `CCA-Prep_Exam-Mechanics_v2.md` — all in `C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz\`
**Scoring records read:** `EXAM-LOG.md`, `DASHBOARD-DATA.jsonl`, `GENERATION-INTELLIGENCE.md`

Every factual claim below carries a corpus file and section citation. Where the corpus and general knowledge diverge, the corpus wins and the divergence is named in place. Where the scoring records are ambiguous, that is stated rather than filled in by inference.

---

## 1. Score Trajectory

| Exam | Attempt date | Raw | Scaled (`round((c/60)×900+100)`) | Weakest domain that paper |
|---|---|---|---|---|
| 4 | 2026-07-11 | 45 / 60 | 775 | D2 Tool Design & MCP — 5/11 (45%) |
| 5 | 2026-07-11 | 52 / 60 | 880 | D2 Tool Design & MCP — 8/11 (72.7%) |
| 6 | 2026-07-12 | 49 / 60 | 835 | D5 Context Management — 5/7 (71.4%) |
| 7 | 2026-07-16 | 55 / 60 | 925 | D3 and D4, tied — 10/12 each (83.3%) |
| 8 | 2026-07-28 | 52 / 60 | 880 | D3 and D4, tied — 9/12 each (75.0%), 2nd consecutive |

Exams 1, 2, 3 and 9 carry null scores in `DASHBOARD-DATA.jsonl` and contribute no miss data.

You have cleared the 720 pass line on all five scored attempts, and your worst attempt (45/60) still sat three marks above the 42/60 that 720 requires. So the question is not survival — it is margin, and the margin has stopped growing. The trajectory is 775 → 880 → 835 → 925 → 880: strong, but non-monotonic, and Exam 8 gave back 45 points. The reason the earlier climb happened is visible in the domain columns: D2 went 45% → 72.7% → 73.3% → 100% → 90.9%, which is the single largest recovery in your history and is essentially finished as a project. The reason the climb stalled is also visible: D3 and D4 have been jointly the weakest domain for two consecutive papers and both **declined** between them, from 83.3% to 75.0%, despite Exam 8 deliberately re-testing the exact sections you missed in Exam 7. One caveat on comparability — Exam 6 ran under an adjusted quota (D1 14 / D2 15 / D3 12 / D4 12 / D5 7) rather than the base 16/11/12/12/9, so its D2 and D5 percentages sit on different denominators than the others.

The most important single line in the whole log is Exam 8's Observations: of the four sections deliberately re-tested from a fresh angle, "**D3 §3.1 (Q12) missed again, D3 §3.6 (Q13) missed again, D4 §4.6 (Q17) missed again — and only D4 §4.4 (Q16, prefilling) recovered to correct.**" Three of four survived a fresh re-test in a different scenario. That is what a real gap looks like, as opposed to noise. The log also notes those three were not rushed (77s, 37s, 37s against a 120s/question budget) — so this is a knowledge problem, not a pacing problem.

---

## 2. Miss Inventory

<miss_inventory>

Every miss recorded across the five scored exams. Wording in the "Miss as the log records it" column is quoted from `EXAM-LOG.md`.

**Ambiguity flagged in place:** Exams 4, 5, 6 and 7 each carry an explicit "Traps missed (by question, with the corpus fact each one tested)" block. **Exam 8 does not.** Its eight misses are named inline inside the Observations prose and inside the Professor's Note instead. Rows 40–47 below are therefore quoted from those passages, not from a traps block. One consequence: Exam 8's single D1 miss is identified only by section (§1.8), with **no question number recorded anywhere in the log** — row 47 is marked accordingly.

| # | Exam | Q | Domain | Corpus § | KD # | Miss as the log records it |
|---|---|---|---|---|---|---|
| 1 | 4 | Q2 | D2 | Domain-2_v2 §2.4 | #11 / #12 | "two-tool token-binding pattern (`preview_X`/`execute_X` split) vs. a single-tool `dry_run:boolean` the model can skip" |
| 2 | 4 | Q8 | D2 | Domain-2_v2 §2.2 | #10 | "tool description must state scope/boundary to disambiguate near-duplicate tools (two independent misses, same corpus section, different scenarios)" |
| 3 | 4 | Q47 | D2 | Domain-2_v2 §2.2 | #10 | (same entry as Q8 — logged as a single paired bullet, "two independent misses, same corpus section, different scenarios") |
| 4 | 4 | Q14 | D1 | Domain-1_v2 §1.12 | — | "high-stakes ambiguity is an escalation trigger even absent an explicit policy prohibition" |
| 5 | 4 | Q17 | D1 | Domain-1_v2 §1.10 | — | "partial subagent failure should produce coverage-annotated synthesis, not an error-out or a silent omission" |
| 6 | 4 | Q19 | D2 | Domain-2_v2 §2.1 / §2.5 | — | "`tool_choice:{\"type\":\"any\"}` forces a tool call; a prompt instruction alone does not" |
| 7 | 4 | Q22 | D3 | Domain-3_v2 §3.1 | — | "`@import` max nesting depth is 5" |
| 8 | 4 | Q32 | D2 | Domain-2_v2 §2.9 | — | "`Edit` anchor uniqueness: a shorter anchor is MORE likely non-unique, not less; sanctioned fallback is Read+Write" |
| 9 | 4 | Q34 | D1 | Domain-1_v2 §1.3 | — | "`AgentDefinition.allowed_tools` is the structural least-privilege enforcement; a prompt instruction is not" |
| 10 | 4 | Q35 | D3 | Domain-3_v2 §3.3 | #13 | "`context: fork` isolates a skill's large/exploratory output from the main session" |
| 11 | 4 | Q39 | D1 | Domain-1_v2 §1.6 | — | "when subagents all succeed but coverage is wrong, the root cause is the coordinator's task decomposition, not subagent execution" |
| 12 | 4 | Q46 | D3 | Domain-3_v2 §3.1 | — | "root and subdirectory `CLAUDE.md` concatenate; neither overrides the other" |
| 13 | 4 | Q51 | D4 | Domain-4_v2 §4.7 | — | "schema validation guarantees syntax only, never semantic/business-rule correctness" |
| 14 | 4 | Q52 | D2 | Domain-2_v2 §2.3 | — | "permission errors are non-retryable regardless of attempt count; timeouts are transient/retryable — conflating the two wastes retries" |
| 15 | 4 | Q54 | D4 | Domain-4_v2 §4.19 | #19 | "for ambiguous automated requests, proceed with a stated assumption rather than blocking to ask or silently guessing" |
| 16 | 5 | Q13 | D4 | Domain-4_v2 §4.14 | — | "chose a clearer prompt instruction over splitting citation-identification and drafting into a sequential chain" |
| 17 | 5 | Q21 | D1 | Domain-1_v2 §1.6 | — | "misattributed a coverage gap to a tool-description problem instead of the coordinator's own narrow task decomposition (all subagents succeeded; the decomposition never assigned the missing category)" |
| 18 | 5 | Q35 | D2 | Domain-2_v2 §2.1 | — | "missed that the calling application, not Claude, must execute the `tool_use` block and write the file; picked a `PostToolUse` hook instead of the actually-missing execution step" |
| 19 | 5 | Q36 | D3 | Domain-3_v2 §3.4 | — | "fell for a fabricated-obsolescence distractor: believed legacy `.claude/commands/` files 'stopped working' once skills were introduced" |
| 20 | 5 | Q42 | D4 | Domain-4_v2 §4.17 | — | "chose the slow, eventual few-shot fix over surgically disabling the two noisy finding categories immediately — correct general direction, wrong urgency for a trust-bleed already in progress" |
| 21 | 5 | Q54 | D2 | Domain-2_v2 §2.4 | #12 | "chose a still-bypassable confirmation-string parameter over the architecturally-guaranteed two-tool token-binding redesign — the same 'sounds like the fix, isn't' pattern … recurring across two consecutive exams" |
| 22 | 5 | Q57 | D2 | Domain-2_v2 §2.9 | #26 | "chose Grep (content search) over Glob (path-pattern match) for file-name enumeration, on this corpus's first-ever citable use of a built-in-tool Key Distinction" |
| 23 | 5 | Q60 | D4 | Domain-4_v2 §4.2 | — | "swapped a few-shot format-consistency fix for a step-by-step reasoning-depth cue — two techniques aimed at two different failure modes" |
| 24 | 6 | Q2 | D2 | Domain-2_v2 §2.1 | — | "`tool_result` must reference the originating `tool_use`'s `id`; the harness skipped actually executing the tool and returning a matched result" |
| 25 | 6 | Q3 | D2 | Domain-2_v2 §2.2 | — | "tool description must specify the exact accepted input format with an example, not just name the tool's purpose" |
| 26 | 6 | Q5 | D5 | Domain-5_v2 §5.1 | #25 | "stateless-API misconception: chose a fabricated `persist_context`/`session_id`-style parameter over 'the application must resend the full prior messages array'" |
| 27 | 6 | Q12 | D2 | Domain-2_v2 §2.4 | #12 | "two-tool token-binding vs. a bypassable confirmation parameter for a destructive `close_account` call — the third consecutive exam this exact concept has been missed" |
| 28 | 6 | Q24 | D2 | Domain-2_v2 §2.8 | — | "the corpus favors a prompt instruction to bundle two habitually-paired tool calls into one turn over a composite tool that hides the two steps" |
| 29 | 6 | Q25 | D1 | Domain-1_v2 §1.8 | — | "the coordinator's refinement loop needs a defined sufficiency criterion, not an open-ended 'keep re-delegating' or an arbitrary re-delegation cap" |
| 30 | 6 | Q35 | D4 | Domain-4_v2 §4.2 | — | "a step-by-step reasoning cue is the fix for multi-step numeric extraction (tax-rate calculation), not more few-shot examples or a lower temperature" |
| 31 | 6 | Q42 | D4 | Domain-4_v2 §4.20 | #23 | "accumulated assistant responses dilute system-prompt influence over a long session; not a context-window overflow or a per-document overwrite" |
| 32 | 6 | Q44 | D5 | Domain-5_v2 §5.13 | — | "the hybrid context window (recent verbatim + running summary + a never-dropped structured facts block) fixes a sliding-window's loss of an early, still-relevant correction — a bigger fixed window only delays the same problem" |
| 33 | 6 | Q50 | D3 | Domain-3_v2 §3.3 | — | "`allowed-tools` in skill frontmatter restricts tool access during execution (official exam framing); `context: fork` isolates output, it does not restrict tool access" |
| 34 | 6 | Q51 | D3 | Domain-3_v2 §3.5 | — | "a personal skill of the same name overrides a project skill only for that individual, without editing the shared version-controlled file" |
| 35 | 7 | Q3 | D1 | Domain-1_v2 §1.3 | — | "a coordinator with fully-described subagent types but no `Task` tool in its `allowed_tools` cannot spawn subagents at all, regardless of prompt wording — a structural tool-grant gap, not a prompt problem" |
| 36 | 7 | Q16 | D3 | Domain-3_v2 §3.1 | — | "`/memory` is the diagnostic for CLAUDE.md behavior that's inconsistent across otherwise-identical sessions; it shows exactly which memory files loaded, turning a guess into a fact" |
| 37 | 7 | Q19 | D3 | Domain-3_v2 §3.6 | — | "a single-file, fully-scoped one-line fix with an already-identified solution is the textbook case for direct execution; plan mode adds unneeded overhead when there is no ambiguity to resolve" |
| 38 | 7 | Q50 | D4 | Domain-4_v2 §4.4 | — | "prefilling (a partial assistant message the model continues from) reliably suppresses one specific recurring filler phrase; a system-prompt instruction is less reliable for this narrow a fix" |
| 39 | 7 | Q51 | D4 | Domain-4_v2 §4.6 | — | "`tool_choice: {\"type\":\"any\"}` forces a tool call while letting the model pick the best-fitting one of several defined tools, guaranteeing structured output on every run including clean cases with no findings; a specific forced-tool choice would block the 'no issues' path" |
| 40 | 8 | Q11 | D2 | Domain-2_v2 §2.8 | — | "Q11 (§2.8) chose a `PreToolUse` hook over the simpler prompt-bundling fix" |
| 41 | 8 | Q12 | D3 | Domain-3_v2 §3.1 | — | "Q12 (§3.1) chose re-typing the instruction over running the `/memory` diagnostic"; also "D3 §3.1 (`/memory` diagnostic vs. re-typing the instruction) … missed AGAIN on a fresh re-test" |
| 42 | 8 | Q13 | D3 | Domain-3_v2 §3.6 | — | "Q13 (§3.6) chose plan mode over direct execution on an already-fully-scoped one-line change"; also "D3 §3.6 (direct execution vs. plan mode on a fully-scoped one-liner) … missed AGAIN" |
| 43 | 8 | Q51 | D3 | Domain-3_v2 §3.11 | — | "Q51 (§3.11) chose a half-measure partial split over the clean full split"; listed under "D3 §3.11 rules-modularization" as one of the "fresh sections" |
| 44 | 8 | Q17 | D4 | Domain-4_v2 §4.6 | — | "D4 §4.6 (forcing a *specific* tool via `tool_choice` vs. `\"any\"`, which only guarantees *some* tool)" — "missed AGAIN on a fresh re-test" |
| 45 | 8 | Q19 | D4 | Domain-4_v2 §4.2 | — | "D4 §4.2 (Q19, chain-of-thought for N-item comparison)" — logged as a "fresh section" miss |
| 46 | 8 | Q22 | D4 | Domain-4_v2 §4.9 | — | "§4.9 (Q22, nullable-when-absent)" — logged as a "fresh section" miss |
| 47 | 8 | **not recorded** | D1 | Domain-1_v2 §1.8 | — | "the D1 miss (§1.8 re-delegate-vs-ship-with-caveat)" — **the log names the section but no question number; the exam's Observations block gives no Q reference for this item** |

**Total recorded misses: 47.** Cross-check against `DASHBOARD-DATA.jsonl`: Exam 4 = 15 (60−45), Exam 5 = 8, Exam 6 = 11, Exam 7 = 5, Exam 8 = 8. Sum = 47. The inventory is complete.

</miss_inventory>

---

## 3. Ranked Themes

Ranking metric, as specified: **times missed × the number of the 60 exam questions that domain carries** (base FULL-60 quota from `CCA-Prep_Exam-Mechanics_v2.md`: D1 16, D2 11, D3 12, D4 12, D5 9). Cross-domain themes sum the per-domain products. Ties break by recency of the most recent miss.

| Rank | Theme | Misses | Domain split | Corpus sections | Ranking arithmetic |
|---|---|---|---|---|---|
| 1 | **Prompt/parameter-level fix chosen over the structural guarantee** *(the log's own named cross-cutting pattern — "sounds like the fix, isn't")* | 7 | D2 ×5, D1 ×2 | D2 §2.1, §2.3, §2.4, §2.5; D1 §1.3; KD #11, #12 | (5 × 11) + (2 × 16) = 55 + 32 = **87** |
| 2 | **Over-engineering / symptom-patch chosen over the proportionate direct move** *(the log's own named Exam-8 meta-pattern)* | 7 | D3 ×5, D2 ×2 | D3 §3.1, §3.6, §3.11; D2 §2.8 | (5 × 12) + (2 × 11) = 60 + 22 = **82** |
| 3 | **Coordinator ownership: decomposition, sufficiency criteria, and partial coverage** | 5 | D1 ×5 | D1 §1.6, §1.8, §1.10 | 5 × 16 = **80** |
| 4 | **What a schema and each `tool_choice` value actually guarantee** | 5 | D4 ×5 | D4 §4.5, §4.6, §4.7, §4.9 | 5 × 12 = **60** |
| 5 | **Matching the prompt technique to the failure mode** | 4 | D4 ×4 | D4 §4.1, §4.2, §4.14 | 4 × 12 = **48** |
| 6 | **What a tool description must contain** | 3 | D2 ×3 | D2 §2.2, §2.6; KD #10, #29 | 3 × 11 = **33** |
| 7 | **Who runs the loop: tool-use protocol and API statelessness** | 3 | D2 ×2, D5 ×1 | D2 §2.1; D5 §5.1; KD #5, #25 | (2 × 11) + (1 × 9) = 22 + 9 = **31** |
| 8 | **Skill frontmatter: `allowed-tools` vs `context: fork`** | 2 | D3 ×2 | D3 §3.3; KD #13 | 2 × 12 = **24** — tie with rank 9, wins on recency (latest miss Exam 6 Q50 vs Exam 4 Q46) |
| 9 | **CLAUDE.md hierarchy mechanics: concatenation and `@import` depth** | 2 | D3 ×2 | D3 §3.1; KD #1 | 2 × 12 = **24** — tie with rank 8, loses on recency (latest miss Exam 4 Q46) |
| — | *(not taught)* Built-in tool selection — Grep/Glob, Edit anchor | 2 | D2 ×2 | D2 §2.9; KD #26, #27 | 2 × 11 = 22 |
| — | *(not taught)* Seven single-instance misses | 7 | mixed | D1 §1.12; D3 §3.4, §3.5; D4 §4.17, §4.19, §4.20; D5 §5.13 | one miss each |

**Coverage:** Themes 1–9 account for 7+7+5+5+4+3+3+2+2 = **38 of 47 recorded misses = 80.9%**, clearing the 80% bar.

**One thing the arithmetic cannot see, and you must:** Theme 1 ranks first on volume, but its core trap has since been cleared. `GENERATION-INTELLIGENCE.md`'s Key Distinctions tracker marks KD #12 "**strong — CORRECT two consecutive exams (Exam 7 both facets, Exam 8 again), durably cleared**," and records zero remaining "weak" rows across all 29 Key Distinctions. Themes 2, 4 and 5 are the *live* ones — they sit in D3 and D4, the two domains that have been joint-weakest for two consecutive papers and that failed three of four fresh re-tests. Read Theme 1 as a maintenance pass on a habit of mind that is still worth naming; read Themes 2, 4 and 5 as the actual marks on the table.

---

## 4. The Teaching

### Theme 1 — Rank 1 · 7 misses · ~87 marks-recovered index
## Prompt/parameter-level fix chosen over the structural guarantee

**(a) The misconception, in your own error terms.** You keep believing that if the instruction is written clearly enough — in the system prompt, in worked examples, or as a boolean the agent is supposed to set — the required behaviour will actually happen; so you pick the better-worded instruction over the mechanism that makes the wrong behaviour impossible.

**(b) The correct mental model.** The corpus operates a strict two-tier hierarchy, stated as a heuristic in `CCA-Prep_Exam-Mechanics_v2.md` ("Answer Pattern Heuristics"): *"Deterministic over probabilistic — Hooks/gates for guaranteed compliance; prompts for guidance"* and *"Programmatic enforcement for critical sequences … never prompt-only (prompt compliance is probabilistic)."* Four mechanisms sit on the deterministic tier:

- **Two-tool token binding** (`Domain-2_v2 §2.4`, KD #12). `preview_X` returns impact details plus a single-use confirmation token; `execute_X` requires that token as a parameter. §2.4 words the guarantee precisely: this makes it *"architecturally impossible to execute without a prior preview — the token only exists after a preview call."* The single-tool `dry_run: boolean` fails because *"agent bypasses dry run by calling with `dry_run=false` directly."* §2.4 also pre-rejects the two near-miss fixes by name: a server-side timing heuristic is *"fragile to timing conditions"*, and an orchestration-layer confirmation prompt *"requires extra infrastructure."*
- **`tool_choice`** (`Domain-2_v2 §2.5`; `Domain-4_v2 §4.6`). `auto` guarantees nothing. `any` guarantees the model calls *some* tool. `{"type":"tool","name":X}` guarantees *that* tool. §2.5 supplies the failure number for the prompt route: a prompt instruction to always call a tool first is *"only followed ~90% of the time."*
- **`allowed_tools`** (`Domain-1_v2 §1.3`). The whitelist is the enforcement, not a suggestion. §1.3's decisive sentence for a coordinator that never delegates: *"the prompt cannot grant a tool the configuration withholds."* A coordinator's `allowedTools` **must include `"Task"`** or it cannot spawn subagents at all — adding subagent descriptions to the system prompt does not help, because *"descriptions don't enable spawning; the `Task` tool does."*
- **Constrained tools and preconditions** (`Domain-2_v2 §2.5`; `Domain-1_v2 §1.11`, §1.14). Replacing a generic `fetch_url` with a `load_document` that validates the target *"enforces the boundary at the interface level"*; a prompt instruction not to misuse it is rejected as *"probabilistic."* For mandatory sequencing, §1.14 says block the second call until the first succeeds, never instruct.

The log also files **error-taxonomy** here (Exam 4's Professor's Note groups Q52 with Q34 and Q19 as *"all share the same shape: a probabilistic prompt-level fix chosen over the structural/configuration-level guarantee"*). The deterministic move there is `Domain-2_v2 §2.3`'s four categories — transient / validation / business / permission — returned as machine-readable `errorCategory` and `isRetryable` fields, so the agent never has to infer retryability from prose. §2.3: permission failures mean *"retrying is wasted effort"*; business-rule denials are *"not a failure of the tool — it is a valid answer that the requested action is disallowed."*

**(c) The shape of the trap on the page.** The wrong option is a *better-written version of the thing that is already failing*: "Strengthen the system prompt to always call X first, and add three worked examples." "Add a `confirmed: true` parameter the agent must set." "Add the subagent descriptions to the coordinator's prompt." It is attractive for three reasons — it is the cheapest change, it is genuinely good practice in non-critical contexts, and the corpus itself endorses "fix the description first" elsewhere (KD #10), which you over-generalise into "fix the text first, always."

**(d) The decision rule under time pressure.** Ask one question of every option: **"After this change, can the model still do the wrong thing?"** If yes, it is guidance, not enforcement. And read the stem for a compliance number — "8% of blocking statuses", "~90% of the time", "15% of the time", "9% of calls". A percentage in the stem is the exam telling you the probabilistic layer has already been tried and failed; the answer is the option that removes the possibility, not the one that reduces the likelihood. Corollary you missed twice (Exam 4 Q34, Exam 7 Q3): **a prompt can never grant a capability the configuration withholds.**

**(e) Practice — Theme 1**

**Q1.1** Your triage agent's `bulk_reassign_tickets` tool moves every ticket matching a filter into a different queue and cannot be undone from the agent's side. Policy requires the requesting engineer to see the affected count and a sample before anything moves. A proposal keeps the single tool and adds an `impact_reviewed: true` parameter the agent must set, backed by a prompt rule and three worked examples. Audit logs from an analogous tool show the flag was set without any impact output produced in 9% of calls. Which design most reliably enforces the policy?

- **A.** Keep the single tool with `impact_reviewed: true` and strengthen the system prompt with additional worked examples.
- **B.** Add a server-side rule rejecting an execute call unless a preview call for the same filter was logged within the previous 60 seconds.
- **C.** Split it into `preview_bulk_reassign`, returning the impact summary plus a single-use confirmation token, and `execute_bulk_reassign`, which requires that token.
- **D.** Route every bulk reassignment through an orchestration-layer confirmation prompt before the tool is invoked.

**Answer: C.** `Domain-2_v2 §2.4` — the token cannot exist without a prior preview, making the skip architecturally impossible.
*A fails:* the agent can set the boolean without ever producing a preview — §2.4's exact `dry_run` failure mode, prompt-level hope rather than a code-level guarantee. *B fails:* §2.4 names the server-side timing heuristic explicitly as "fragile to timing conditions." *D fails:* §2.4 rejects the orchestration-layer confirmation as extra infrastructure the two-tool split makes unnecessary.

**Q1.2** Your reporting subagent was given a `run_sql` tool accepting arbitrary SQL against the analytics warehouse so it could answer ad-hoc questions; its defined scope is read-only summaries. Over the last month it has issued three `UPDATE` statements against a metrics table while "correcting" rows it judged to be bad. What is the most effective fix?

- **A.** Add a system-prompt line forbidding write statements, plus two examples of correctly refused write requests.
- **B.** Replace `run_sql` with a `run_report_query` tool that accepts only named, parameterised read-only queries.
- **C.** Keep `run_sql` and maintain a blocklist of write keywords (`UPDATE`, `DELETE`, `INSERT`) the tool rejects.
- **D.** Give the reporting subagent the full warehouse tool catalog so it has a proper write tool for legitimate corrections.

**Answer: B.** `Domain-2_v2 §2.5` and `Domain-1_v2 §1.11` — replacing a generic tool with a constrained alternative enforces the boundary at the interface level.
*A fails:* §1.11 rejects the prompt instruction for exactly this scenario as "probabilistic, not deterministic." *C fails:* §2.5 rejects the structurally identical blocklist fix (blocking known search-engine domains) as "fragile, not future-proof." *D fails:* §2.5 warns that "agents with tools outside their specialization tend to misuse them" — this widens the breach rather than closing it.

**Q1.3** Your ingestion agent's `fetch_partner_feed` tool applies identical exponential backoff to every failure. One week of telemetry: 340 timeouts (all eventually succeeded), 61 expired-credential failures (all five attempts failed, every time), and 28 rejections for feeds the partner has permanently withdrawn. Retry traffic is now nearly 40% of the tool's total call volume. What should its error handling do instead?

- **A.** Lengthen the backoff interval so the same five attempts stretch further apart.
- **B.** Return `isError: true` with a descriptive prose message for every failure and let the agent decide from the text whether to retry.
- **C.** Return a structured error carrying `errorCategory` and `isRetryable`, retry only the transient category inside the tool, and surface permission and business failures immediately with an explanation.
- **D.** Return an empty result set on every failure so the agent stops retrying and proceeds.

**Answer: C.** `Domain-2_v2 §2.3` — the four categories plus "Error Handling at the Right Level": handle transient failures inside the tool, surface only what needs an agent decision.
*A fails:* §2.3 — a permission failure and a withdrawn feed can never succeed; longer waits still waste every attempt. *B fails:* §2.3's stated principle is that a `retryable` flag "is BETTER than forcing the agent to guess from error text." *D fails:* §2.3 — an empty result is a *successful* query with zero matches; masking an access failure as "no data" makes the agent report absent data that may exist.

---

### Theme 2 — Rank 2 · 7 misses · ~82 marks-recovered index
## Over-engineering / symptom-patch chosen over the proportionate direct move

**(a) The misconception, in your own error terms.** When something misbehaves you reach for the heavier mechanism — a hook, a mode, a composite tool, a louder reminder — instead of the smallest move that addresses the actual cause. Exam 8's Observations name this directly: *"All four reach for a heavier or symptom-level response where the corpus wants the proportionate, direct one."*

**(b) The correct mental model.** `CCA-Prep_Exam-Mechanics_v2.md` carries two heuristics that decide these items: *"Fix the root cause, not the symptom"* and *"Proportionate first response — Try the prompt/description fix before adding infrastructure (classifiers, routing layers, bigger models)."* Four corpus rulings sit under them:

- **Bundling beats a composite tool** (`Domain-2_v2 §2.8`). Verbatim: *"The preferred approach … is to **prompt the agent to bundle tool requests into one turn** rather than creating composite tools, as the agent can naturally request multiple tools simultaneously."* Building `get_customer_with_orders` is listed as "Not preferred" because it *"hides the composition."* Hooks are for something else entirely: `PreToolUse` is threshold enforcement, `PostToolUse` is output normalisation (`§2.7`).
- **Diagnose before you re-instruct** (`Domain-3_v2 §3.1`). `/memory` is *"the first diagnostic step whenever 'Claude follows rule X sometimes but not always': check whether the file holding rule X is actually in the loaded set."* The named wrong answer is *"Repeat the instruction louder in the prompt each session (treats symptom, not root cause)."*
- **Plan mode is for ambiguity, not for caution** (`Domain-3_v2 §3.6`). Planning mode is for *"large scope, architectural decisions, multiple approaches possible, complex changes across many files."* Direct execution is for *"scope is clear, approach is defined, changes are routine."* The scenarios table lists **"Single-file bug fix with a clear stack trace"** and **"Implement function with well-defined input/output spec"** under direct execution. §3.6 also rejects the hedge: *"Start in direct execution and switch to planning when it gets hard → Wrong. Reactive switching is expensive."*
- **Modularise by trigger condition, and do it completely** (`Domain-3_v2 §3.11`, §3.2, §3.3). Three destinations, chosen by *when the content needs to load*: content that must be present **every session** → keep in CLAUDE.md, or split into separate files pulled back in by `@import` (§3.11: *"`@import` … is the complementary approach when content should remain part of the concatenated CLAUDE.md context but live in separate files"*). Content scoped to **file paths** → `.claude/rules/` with glob frontmatter (§3.2). **Workflow-specific** guidance invoked on demand → Skills (§3.11). Exam 8 Q51 is logged as *"a half-measure partial split over the clean full split"* — the log records the verdict but not the option text, so treat the takeaway as: pick one destination on the trigger-condition test and split *all* the content that belongs there, rather than moving some of it and leaving the rest.

**(c) The shape of the trap on the page.** The distractor names a real, powerful, corpus-endorsed mechanism — a `PreToolUse` hook, plan mode, a composite tool, a routing classifier, a larger model — applied to a problem a smaller move already solves. It is attractive because the mechanism *is* correct somewhere in the corpus, because "more rigorous" feels safer when you are unsure, and because in real engineering work the heavier option often is defensible. On this exam it is not.

**(d) The decision rule under time pressure.** **Name the cause in one clause before you read the options.** Then match:
- Cause is "*we do not know what is actually loaded / happening*" → diagnose (`/memory`), never re-instruct.
- Cause is "*it is doing the right thing across two turns instead of one*" → prompt-level bundling, not new machinery.
- Cause is "*the change is single-file, fully specified, and already decided*" → execute directly; there is nothing to plan.
- Cause is "*one file is carrying content with different load triggers*" → split by trigger condition, completely.

And hold this against Theme 1, because the two rules point in opposite directions and the exam tests both. **Heavy/structural wins when the requirement is a guarantee** — irreversible action, mandatory ordering, capability grant, safety threshold. **Light/proportionate wins when the requirement is diagnosis, quality, efficiency, or organisation.** Ask which of those two the stem is describing before you decide how much machinery to buy.

**(e) Practice — Theme 2**

**Q2.1** A team convention — every new endpoint gets a contract test before merge — is followed by Claude Code in three engineers' sessions and ignored in a fourth engineer's, on the same repository at the same commit. For two weeks she has re-pasted the rule at the top of each session; it holds for a few turns and then lapses. What is the most effective first step?

- **A.** Run `/memory` in her session to list which memory files are actually loaded, and compare against a session where the convention holds.
- **B.** Re-state the convention at the top of every prompt and again after each long tool output.
- **C.** Move the convention into a `.claude/rules/` file globbed to the API directory so it loads on matching paths.
- **D.** Have her run `/compact` at the start of each session so the convention is not pushed out of context.

**Answer: A.** `Domain-3_v2 §3.1` — `/memory` shows which memory files are loaded and is the named first diagnostic for behaviour that is inconsistent across otherwise-identical sessions.
*B fails:* §3.1 names repeating the instruction as treating the symptom rather than the root cause. *C fails:* it is a remedy applied before the cause is known — §3.1 makes `/memory` the first step, and the convention may already sit in a project file that simply is not being discovered. *D fails:* `/compact` compresses context (§3.12) and has no bearing on which memory files load.

**Q2.2** A failing nightly job traces to a single off-by-one in a date-window helper. The stack trace names the file and line, and the ticket already specifies the corrected boundary condition. The change touches one function in one file. An engineer's habit is to open planning mode for anything touching scheduled jobs. How should the team handle this change?

- **A.** Open planning mode so Claude explores the job's dependencies before touching the helper.
- **B.** Start in direct execution and switch to planning mode if the fix turns out to touch more than one file.
- **C.** Execute directly — the file, the cause, and the intended fix are all already known.
- **D.** Open planning mode but restrict it to Read and Grep so the exploration stays cheap.

**Answer: C.** `Domain-3_v2 §3.6` — the scenarios table lists "Single-file bug fix with a clear stack trace" under direct execution.
*A fails:* §3.6 reserves planning mode for large scope, architectural decisions, or multiple viable approaches; none is present. *B fails:* §3.6 explicitly rejects reactive switching — "Reactive switching is expensive. Plan upfront when the task demands it." *D fails:* planning mode is already read-only (Read/Grep/Glob, no side effects) per §3.6, so the restriction changes nothing about the fact that there is nothing to plan.

**Q2.3** Generating a release summary always needs both the merged-change list and the linked issue titles, yet your agent requests the change list in one turn and the issue titles in the next, on essentially every run. One engineer proposes a `PreToolUse` hook that intercepts the first call and injects the second; another proposes a combined `get_summary_inputs` tool. What is the corpus-preferred fix?

- **A.** Add the `PreToolUse` hook to inject the second call automatically.
- **B.** Instruct the agent in its prompt to bundle related tool requests into a single turn.
- **C.** Build the combined `get_summary_inputs` tool returning both payloads.
- **D.** Accept the extra round-trip as the cost of keeping every tool single-purpose.

**Answer: B.** `Domain-2_v2 §2.8` — prompting the agent to bundle related requests into one turn is stated as the preferred approach, since the agent can naturally request multiple tools simultaneously.
*A fails:* §2.7 scopes `PreToolUse` to validating, blocking, or modifying parameters; using it to synthesise a second call adds machinery for a problem the prompt solves. *C fails:* §2.8 lists the composite tool as "Not preferred" because it hides the composition. *D fails:* a documented, cheaper fix exists — bundling keeps the tools single-purpose *and* removes the round-trip.

---

### Theme 3 — Rank 3 · 5 misses · ~80 marks-recovered index
## Coordinator ownership: decomposition, sufficiency criteria, and partial coverage

**(a) The misconception, in your own error terms.** When a multi-agent run comes back incomplete or thin, you look at the subagents — their queries, their tools, their descriptions — or you settle for shipping with a caveat, instead of holding the coordinator responsible for what it asked for and what it does next.

**(b) The correct mental model.** Three sections, and one discriminator that decides between two of them.

- **Decomposition is the coordinator's most critical responsibility** (`Domain-1_v2 §1.6`). Verbatim: *"If the coordinator decomposes a task too narrowly, subagents execute correctly but cover the wrong ground. Root cause = coordinator prompt, not subagent performance."* §1.6 names the wrong answers for its worked scenario too: *"Not: web-search agent query quality, synthesis agent gap detection, document analysis filters."* `Exam-Mechanics_v2`'s heuristic table encodes the tell: *"Coverage gaps trace upstream — Complete-looking subagent outputs + missing topics → check the coordinator's decomposition."* §1.6 also gives the preventive form: the coordinator must *"explicitly partition the research space before delegating"* — partition first, do not deduplicate after.
- **The refinement loop, when the gap is recoverable** (`Domain-1_v2 §1.8`). The coordinator evaluates synthesis output for gaps, **re-delegates targeted queries aimed at the specific gaps** to the search/analysis subagents, then re-invokes synthesis. §1.8 rejects three alternatives by name: having the synthesis agent search the web itself (breaks separation of responsibilities and least-privilege tooling, §1.11); shipping with "further research needed" *"when re-delegation is available"*; and looping *"indefinitely without a sufficiency criterion"* — the coordinator needs defined quality criteria (§1.4) to know when to stop. Exam 6 Q25 is exactly that last one: an arbitrary re-delegation cap is not a sufficiency criterion either.
- **Coverage annotation, when the gap is unrecoverable** (`Domain-1_v2 §1.10`). Complete the synthesis from available data, *"annotate coverage — mark which conclusions are well-supported vs where gaps exist"*, and propagate uncertainty upward. Both failure modes are named: *"Return error because input is incomplete"* and *"Proceed without noting the gaps."*

The discriminator between §1.8 and §1.10 is the single thing that cost you Exam 4 Q17 and Exam 8's unnumbered D1 miss, in opposite directions: **is the missing data still obtainable?** §1.8's own wording settles it — *"coverage annotation is for **unrecoverable** gaps (§1.10) — not a substitute for the refinement loop."*

**(c) The shape of the trap on the page.** Two families. First, an option that blames a subagent — "the search agent's queries were too narrow", "the tool description did not distinguish the categories" — which is attractive because it names a real corpus concept (KD #10) that happens to be the wrong diagnosis here. Second, the *other half* of the §1.8/§1.10 pair, offered in a stem that carefully specifies whether the missing sources are still reachable. The tell for the first family is that **every subagent reported success**.

**(d) The decision rule under time pressure.** Two questions, in order. **"Did every subagent succeed?"** If yes and the output is still the wrong shape, the fault is upstream at the coordinator — never at the subagent, and never at a tool description. Then: **"Can the missing data still be fetched?"** Yes → re-delegate targeted queries and re-invoke synthesis (§1.8). No → coverage-annotate and ship (§1.10). Never ship with a caveat while re-delegation is available; never error out merely because the input is partial.

**(e) Practice — Theme 3**

**Q3.1** Asked to inventory every place a deprecated authentication header is still produced, your coordinator splits the work into three subtasks, all scoped to the service's HTTP handlers. All three subagents report success with complete, correct results for their assigned subtasks. The shipped inventory misses the header's use in a background job and in a client SDK the same repository publishes. What is the most likely root cause?

- **A.** The subagents' search queries were too narrow within their assigned areas.
- **B.** The coordinator's task decomposition partitioned the search space too narrowly.
- **C.** The synthesis step failed to detect that whole categories were missing from the aggregated findings.
- **D.** The subagents lacked a tool capable of searching non-HTTP code paths.

**Answer: B.** `Domain-1_v2 §1.6`, and the `Exam-Mechanics_v2` heuristic "Coverage gaps trace upstream."
*A fails:* each subagent covered its assigned ground correctly; §1.6 places the fault upstream precisely when subagents succeed. *C fails:* §1.6 names "synthesis agent gap detection" among the wrong root causes for this exact pattern. *D fails:* nothing indicates a tool gap — the subagents were never assigned that ground in the first place.

**Q3.2** Your coordinator reviews a synthesis draft and finds it says nothing about one of the four regions the brief named. The document-analysis subagent's logged findings do contain records for that region; they were simply never surfaced in the draft. All source systems remain online. What should the coordinator do?

- **A.** Ship the draft with a note that the fourth region needs further research.
- **B.** Re-invoke the synthesis subagent with the same findings plus an instruction to cover all four regions.
- **C.** Re-delegate a targeted query aimed specifically at the missing region, then re-invoke synthesis with the enriched findings.
- **D.** Give the synthesis subagent its own search access so it can fill gaps like this itself.

**Answer: C.** `Domain-1_v2 §1.8` — the refinement loop: evaluate, re-delegate targeted queries at the specific gaps, re-invoke synthesis.
*A fails:* §1.8 rules out shipping with a caveat "when re-delegation is available"; coverage annotation (§1.10) is for unrecoverable gaps. *B fails:* re-invoking on unchanged input adds emphasis, not evidence — §1.8 has the coordinator re-delegate for enriched findings first. *D fails:* §1.8 and §1.11 — the synthesis agent searching for itself breaks separation of responsibilities and least-privilege tooling.

**Q3.3** Two of the five source archives your research pipeline draws on have been decommissioned and will return nothing this cycle or any future one. The synthesis subagent has a complete, well-evidenced draft from the other three. It currently returns an error because its input is incomplete. What should it do instead?

- **A.** Complete the synthesis and present all conclusions with uniform confidence, since the available evidence is sound.
- **B.** Complete the synthesis from available data and annotate coverage, marking which conclusions are well-supported and where gaps remain.
- **C.** Keep returning the error so the coordinator can retry the two archives on a longer timeout.
- **D.** Hold the draft until the coordinator re-delegates the two missing categories.

**Answer: B.** `Domain-1_v2 §1.10` — complete synthesis using available data, annotate coverage, propagate uncertainty upward.
*A fails:* §1.10 names "Proceed without noting the gaps" as a wrong response. *C fails:* §1.10 names "Return error because input is incomplete" as the other wrong response, and a decommissioned source cannot be retried into existence. *D fails:* §1.8's refinement loop applies to recoverable gaps; these sources are permanently gone, which is the §1.10 case by definition.

---

### Theme 4 — Rank 4 · 5 misses · ~60 marks-recovered index
## What a schema and each `tool_choice` value actually guarantee

**(a) The misconception, in your own error terms.** You treat "it validated" as "it is right", and you treat the three `tool_choice` values as interchangeable ways of "making it use a tool." This is the theme that failed its fresh re-test in Exam 8 (§4.6, Q17), so it is live.

**(b) The correct mental model.** Read each mechanism as a promise with an exact scope.

- **`tool_use` + a schema promises *shape*, nothing more** (`Domain-4_v2 §4.6`). Defining a tool whose input schema is your desired output structure and reading the `tool_use` block is *"the **most reliable** way to get schema-compliant structured output"* and *"eliminates JSON syntax errors."* §4.6's own misconception box is the trap: *"'tool_use with a strict JSON schema guarantees the output is **correct**.' — It guarantees the output is **syntactically valid and schema-shaped**."*
- **The three `tool_choice` values promise three different things** (`Domain-4_v2 §4.6`; `Domain-2_v2 §2.5`). `auto` → *"no structure guarantee"*, the model may answer in text. `any` → the model **must call some tool**; §4.6 makes it the right answer when *"multiple extraction schemas exist and document type is unknown — model picks the best-fitting tool, but you always get structured output."* `{"type":"tool","name":X}` → the model must call **that** tool; §4.6's line for the contrast case is blunt: *"`tool_choice: "any"` (guarantees *a* tool call, not *that* tool)."* And §2.5 supplies the cost of over-forcing: *"Leave `tool_choice` forced on every turn — the model can then never call the enrichment tools at all."* The forced-first-step pattern is force on turn one, relax to `auto`/`any` afterwards.
- **Syntax versus semantics** (`Domain-4_v2 §4.7`). *"Semantic errors sail through schema validation by definition: the JSON is valid, the content is wrong."* When parse failures hit zero but reconciliation still fails, that is the **expected** outcome, not a schema defect: §4.7 rejects *"The schema must be wrong — tighten it further"* (*"no schema constraint can verify that numbers sum correctly"*) and *"Tool use is unreliable, revert to prompt-based JSON"* (*"would reintroduce the syntax error class on top of the semantic one"*). The semantic layer is cross-field validation in code (§4.8), retry carrying the *specific* error (§4.9), and structural self-correction fields — `stated_total` / `calculated_total` / `conflict_detected` (§4.10), which §4.10 stresses is structural, *not* asking the model "are you sure?".
- **Nullable prevents fabrication; retries cannot conjure absent data** (`Domain-4_v2 §4.5`, §4.9). §4.5: *"A required, non-nullable field pushes the model to **fabricate values** to satisfy the schema when the data is missing."* §4.9, for information genuinely absent from the source: *"Make the field nullable; accept `null`; stop retrying"*, rejecting "increase max retries from 3 to 10" (*"absent information stays absent"*), "strengthen the retry feedback message" (*"no feedback can conjure missing data"*), and keeping the field required "for data quality" (*"guarantees fabricated values"*).

**(c) The shape of the trap on the page.** Three recurring silhouettes: (i) an option that tightens the schema in response to a semantic failure — attractive because tightening is what you do to a schema; (ii) `any` offered where the stem requires a *specific* step, or forced-specific offered where a clean "nothing to report" run must still produce structure — the two are near-identical on the page and only the stem decides; (iii) "raise max retries" or "sharpen the retry wording" when the stem has already told you the data is not in the document.

**(d) The decision rule under time pressure.** **Say out loud what each option guarantees, then match it to what the stem demands.** Schema or validator → shape only. `auto` → nothing. `any` → *a* tool. `{"type":"tool","name":X}` → *that* tool. Then: "must be structured every run, several document classes, including the no-findings path" → `any`. "Step X must run before step Y" → forced specific, **first turn only**, then relax. "Parses fine, values wrong" → semantic layer, never a tighter schema. "The value is not in the source" → nullable, accept `null`, stop the loop.

**(e) Practice — Theme 4**

**Q4.1** A compliance-check step must return schema-valid JSON on every run, including runs where it finds nothing to report. Three tools are defined, one per document class, and the class is not known before the call. Logs show the step sometimes answers in prose — "no issues identified in this filing" — and the ingestion parser fails on those runs. Which configuration fixes this?

- **A.** `tool_choice: {"type": "auto"}` plus a prompt line requiring JSON output.
- **B.** `tool_choice: {"type": "tool", "name": "check_filing"}`, naming the most common of the three tools.
- **C.** `tool_choice: {"type": "any"}`.
- **D.** Keep `auto` and pass every free-text response through a JSON repair library.

**Answer: C.** `Domain-4_v2 §4.6` — `any` guarantees a tool call; with several extraction schemas the model still picks the best fit, so structure is guaranteed on every run, clean ones included.
*A fails:* §4.6 — `auto` carries "no structure guarantee" and a prompt request for JSON "may or may not" be honoured. *B fails:* forcing a specific tool blocks the runs whose document class matches a different tool; §4.6 reserves the forced form for guaranteeing a particular step. *D fails:* §4.6 — post-processing "treats the symptom; tool_use removes the problem at the source."

**Q4.2** Since your extraction step moved to `tool_use` with a strict schema, parse failures have been zero for a month and every field passes its type check. A downstream audit still finds records where the `shipped_quantity` and `ordered_quantity` values are transposed — both integers, both in range, both valid. An engineer concludes the schema is too permissive. How should the team respond?

- **A.** This is expected: the schema eliminated the syntax class, and transposition is a semantic error needing cross-field validation plus a retry carrying the specific error.
- **B.** Tighten the schema further — narrow the field types and expand the field descriptions until the transposition stops.
- **C.** Revert to prompt-based JSON output, since `tool_use` is evidently not reliable.
- **D.** Add a "review your extraction carefully before returning it" line to the prompt.

**Answer: A.** `Domain-4_v2 §4.7`, with the remediation in §4.8 and §4.9.
*B fails:* §4.7 — no schema constraint can verify that a valid value landed in the right field; this is the exact "tighten it further" distractor the corpus names. *C fails:* §4.7 — reverting "would reintroduce the syntax error class on top of the semantic one." *D fails:* §4.10 — self-correction in this corpus is structural (extract a stated value and an independently derived one with a conflict flag), not a conversational reminder.

**Q4.3** Your extraction schema marks `contract_effective_date` as required and non-nullable. Validation rejects it on 12% of documents; sampling those documents shows the effective date is genuinely not printed on them — it lives in a separate signature packet the pipeline never receives. An engineer proposes raising max retries from 3 to 8 and sharpening the retry message. What should the team do?

- **A.** Raise max retries to 8 and sharpen the retry feedback wording.
- **B.** Keep the field required for data quality and route every rejection to a manual-entry queue.
- **C.** Add a stricter format constraint to the date field so invalid values are caught earlier.
- **D.** Make the field nullable, accept `null` as a legitimate outcome, and stop retrying those documents.

**Answer: D.** `Domain-4_v2 §4.9` and §4.5 — for information genuinely absent from the source, nullable is the fix and retries are pure waste.
*A fails:* §4.9 — "absent information stays absent" and "no feedback can conjure missing data." *B fails:* §4.5 — a required non-nullable field "pushes the model to fabricate values"; the schema, not the queue, is the defect. *C fails:* the values are not malformed, they are absent — a format constraint addresses a different failure class entirely.

---

### Theme 5 — Rank 5 · 4 misses · ~48 marks-recovered index
## Matching the prompt technique to the failure mode

**(a) The misconception, in your own error terms.** You pick the technique you trust rather than the one that targets the failure the stem describes — and the log shows you doing it in both directions: Exam 5 Q60 *"swapped a few-shot format-consistency fix for a step-by-step reasoning-depth cue"*, while Exam 6 Q35 needed the step-by-step cue and you reached for few-shot or temperature. Two opposite errors, one root cause: you are not reading the failure noun.

**(b) The correct mental model.** `Domain-4_v2` is effectively a failure-mode → technique lookup table. Commit the mapping, not the techniques:

| The failure the stem describes | The corpus's technique | Citation |
|---|---|---|
| Output shape differs run to run; instructions already tried and failing | Few-shot examples showing the exact required format | §4.1; KD #16 |
| Misrouting between similar tools | 4–6 examples targeted at the **ambiguous** cases with rationale — *not* 10–15 clear ones | §4.1; KD #18 |
| Multi-step maths, multi-stage analysis, **comparison across N items**, step-wise transformation | A reasoning cue ("think step by step"); explicitly **not** for single-step tasks | §4.2 |
| One pass doing two jobs; the later job degrades | Prompt chaining — identify first, then act on the identified list | §4.14; §1.7 |
| Judgments inconsistent because the criterion is abstract | Replace vague intent with an explicit, testable criterion | §4.16 |
| One specific recurring phrase or opening | Prefilling — a partial assistant message it continues from | §4.4 |
| Attention diluted across many files in one pass | Per-file passes plus a separate integration pass — **not** a bigger context window | §4.12; KD #17 |
| Behaviour drifts after many turns at low token counts | Accumulated assistant responses diluting the system prompt | §4.20; KD #23 |

Two boundary facts worth memorising because they are the distractors: §4.1 says more instruction text does not fix a format problem, because *"instructions are already failing"*; §4.2 says do **not** add a reasoning cue for single-step tasks; and §4.12 says the larger context window is wrong because *"Larger context does not fix attention quality."*

**(c) The shape of the trap on the page.** Two options both name real, corpus-endorsed techniques. Neither is a bad idea in general. Only the failure described in the stem decides. That is why this theme is invisible if you evaluate options on quality — you must evaluate them on *fit*.

**(d) The decision rule under time pressure.** **Underline the failure noun in the stem before you read a single option.** "Different shape each run / inconsistent format" = format → few-shot. "Misses steps / gets arithmetic wrong / compares N things and skips some" = reasoning → step-by-step cue. "Does two jobs in one pass and one goes shallow" = decomposition → chaining or separate passes. "Nobody can predict what it will flag" = criteria → concrete testable definition. "Same phrase every time" = prefilling. Then pick the option that names *that* technique, even if another option names a technique you like better.

**(e) Practice — Theme 5**

**Q5.1** A migration assistant is asked to compare a source table's 14 columns against a target schema's 14 columns and report every type, nullability, and default mismatch. It reliably catches mismatches in the first few columns and the last one or two, and silently passes over several in between. Its output format is already consistent every run. Which prompting change most reliably improves accuracy?

- **A.** Add three few-shot examples showing the exact mismatch-report format.
- **B.** Add a reasoning cue instructing it to work through the comparison column by column before reporting.
- **C.** Lower the temperature so the comparison becomes more deterministic.
- **D.** Split the comparison into 14 separate single-column requests.

**Answer: B.** `Domain-4_v2 §4.2` — "Comparison across N items" is named among the cases that require a reasoning cue.
*A fails:* §4.1 targets format inconsistency; the format is already correct and the failure is reasoning coverage. *C fails:* temperature controls randomness, not reasoning depth — §4.4 makes the same point when rejecting temperature as a fix for a specific behaviour. *D fails:* §4.12's split-pass remedy addresses attention dilution across many large items; 14 isolated requests also discard the cross-column context a schema comparison depends on.

**Q5.2** A support agent's case-closure note is meant to follow a fixed shape: resolution category, action taken, follow-up needed (yes/no). The instruction has been rewritten three times, each version more explicit than the last. Notes still come back in four different shapes — sometimes a bulleted sub-list, sometimes prose, sometimes with the follow-up field omitted. The content of every note is factually accurate. Which change is most effective?

- **A.** Rewrite the instruction once more, spelling out each field's exact placement and ordering.
- **B.** Add a reasoning cue asking it to think step by step before writing each note.
- **C.** Add 3–4 few-shot examples showing the exact required note format.
- **D.** Prefill each response with the opening of the resolution-category line so the shape is set.

**Answer: C.** `Domain-4_v2 §4.1` and KD #16 — few-shot examples are the corpus's fix when prose instructions produce inconsistent output format.
*A fails:* §4.1/KD #16 — "More detailed / explicit instructions (already failing; adding more text doesn't help)." *B fails:* §4.2 scopes reasoning cues to multi-step reasoning; the content is already correct and the failure is format. *D fails:* §4.4 scopes prefilling to suppressing a specific recurring phrase or seeding one opening — it does not enforce a repeating structure across every field of every note.

**Q5.3** One prompt asks your agent both to find every place a legacy config key is read *and* to rewrite each of those call sites, in the same pass. The first two or three rewrites are careful and correct; the remainder are shallow or skipped, and a second run surfaces call sites the first run never mentioned. Which restructuring most improves this?

- **A.** Chain the work: one prompt identifies every call site, a second acts on the identified list.
- **B.** Add a reasoning cue instructing it to think step by step through each rewrite.
- **C.** Add few-shot examples of correctly rewritten call sites.
- **D.** Move to a model with a larger context window so the whole job fits comfortably.

**Answer: A.** `Domain-4_v2 §4.14` — the corpus's own worked example is "Step 1: Identify issues in code / Step 2: Generate fixes for identified issues", yielding "more focused, consistent output at each stage."
*B fails:* the failure is two distinct jobs sharing one pass; a reasoning cue does not separate them. *C fails:* §4.1 — examples fix format inconsistency, whereas this output is degrading in depth and coverage. *D fails:* §4.12 — "Larger context does not fix attention quality. More tokens available ≠ consistent attention per token."

---

### Theme 6 — Rank 6 · 3 misses · ~33 marks-recovered index
## What a tool description must contain

**(a) The misconception, in your own error terms.** You accept a description that states the tool's *purpose* as complete, and when misrouting happens you look for a mechanism that routes around the ambiguity rather than removing it.

**(b) The correct mental model.** `Domain-2_v2 §2.2` opens with the priority ruling: descriptions are *"the **primary input** Claude uses to decide which tool to call. When misrouting occurs, **check descriptions first** before adding classifiers or few-shot examples."* A complete description has four parts, and you have missed two of them across three exams:

1. **What it does** — purpose, not just the name.
2. **What input it accepts** — *"formats, ID types, examples"*. This is Exam 6 Q3: an example of the accepted format is part of the requirement, not a nicety.
3. **When to use it** versus similar tools.
4. **When NOT to use it** — boundary cases. This is Exam 4 Q8 and Q47: the scope/boundary clause is what disambiguates near-duplicates.

KD #10 supplies the rule of order: *"Fix the signal (description) before adding a new layer that compensates for the bad signal"* — and rejects the pre-routing classifier as *"adds infrastructure without fixing the underlying ambiguity."* §2.2 separately rejects the merge: combining `get_customer` and `lookup_order` into a single `lookup_entity` *"loses semantic precision."* The same principle extends to MCP versus built-in tools (`§2.6`, KD #29): when an agent keeps falling back to `Grep` instead of a more capable MCP tool, *"Enhance the MCP tool's description"* — do **not** remove the built-in (*"breaks legitimate content-search use cases"*) and do **not** add an "always prefer MCP tools" rule (*"blunt, keyword-sensitive"*).

One genuine exception, worth holding separately so you do not over-apply the description rule: `§2.5` says when an agent has far too many tools (the guide's numbers: **18 instead of 4–5**), the tool *count* is the root cause and more detailed descriptions on all 18 is the wrong answer — *"reduce the decision space first."*

**(c) The shape of the trap on the page.** The "add a layer" option — a classifier, a router, an always-prefer rule — and the "merge the tools" option. Both read as decisive engineering. Both leave the ambiguous signal exactly where it was.

**(d) The decision rule under time pressure.** **When two tools get confused, the fix lives in the text the model reads to choose between them.** Add the boundary clause ("use this when…, do NOT use this when…") and an input-format example before adding any layer, and never merge two semantically distinct tools to dodge the ambiguity. The one exception: if the stem's problem is the sheer number of tools, cut the count first.

**(e) Practice — Theme 6**

**Q6.1** Two MCP tools — `get_schema_version` (returns the deployed schema revision for an environment) and `get_migration_status` (returns whether a pending migration has been applied) — are each described only as "Returns database state information." Logs show the agent calls `get_schema_version` on roughly a third of requests that needed `get_migration_status`. An engineer proposes a pre-routing classifier that inspects each request and picks the tool. What is the most effective fix?

- **A.** Add the pre-routing classifier ahead of tool selection.
- **B.** Expand both descriptions to state what each returns, what input each accepts with an example, and explicitly when *not* to use it.
- **C.** Merge the two into a single `get_database_state` tool returning both payloads.
- **D.** Add several few-shot examples of clear, unambiguous requests for each tool.

**Answer: B.** `Domain-2_v2 §2.2` — the four description requirements, with boundary cases as the disambiguator.
*A fails:* KD #10 — a classifier "adds infrastructure without fixing the underlying ambiguity." *C fails:* §2.2 — merging semantically distinct tools "loses semantic precision" (the `lookup_entity` anti-pattern). *D fails:* `Domain-4_v2 §4.1` requires examples targeted at the *ambiguous* cases, not clear ones; and §2.2 says check descriptions first regardless.

**Q6.2** Your `lookup_shipment` tool accepts either a 12-character tracking code or an internal shipment UUID. Its description reads, in full: "Looks up a shipment." The agent frequently passes a customer's order number instead, and the tool returns not-found on roughly one call in five. What change most directly reduces these failures?

- **A.** Add a system-prompt rule listing which identifier belongs to which tool.
- **B.** Extend the tool to accept order numbers as well and resolve them internally.
- **C.** Rewrite the description to state the exact accepted input formats with an example of each, and note that order numbers are not accepted.
- **D.** Return a structured error naming the expected format so the agent can retry.

**Answer: C.** `Domain-2_v2 §2.2` — a description must specify what input it accepts, including formats, ID types and examples, plus its boundary cases.
*A fails:* §2.2 — descriptions are the primary input for tool selection and argument construction; a separate prompt rule is a second, weaker signal. *B fails:* widening the interface to absorb a description defect; §2.2 fixes the signal. *D fails:* it improves recovery, not selection — one call in five is still wasted, and §2.2 makes description quality the root-cause fix.

**Q6.3** An MCP server exposes `find_symbol_definition`, which resolves a symbol to its definition using a maintained cross-repository index that includes generated and vendored code. Its description reads "Searches code." Logs show the agent reaches for built-in `Grep` on about 80% of definition lookups and misses definitions in generated files `Grep` never sees. An engineer proposes removing `Grep` from the agent's tool list. What is the most effective fix?

- **A.** Remove `Grep` so the agent has no alternative.
- **B.** Add a system-prompt rule that MCP tools are always preferred over built-in tools.
- **C.** Enhance the MCP tool's description to spell out its index coverage, its outputs, and what built-in search cannot provide.
- **D.** Wrap `Grep` so every invocation transparently calls the MCP tool instead.

**Answer: C.** `Domain-2_v2 §2.6` and KD #29 — make the superior capability explicit in the description the model actually reads.
*A fails:* KD #29 — removing the built-in "breaks legitimate content-search use cases; the root cause is an under-specified description, not the built-in tool's existence." *B fails:* KD #29 — a blanket preference rule is "blunt, keyword-sensitive" and misroutes cases where the built-in genuinely is right. *D fails:* it hides tool selection behind a wrapper rather than fixing the signal, and removes the agent's ability to do plain content search at all.

---

### Theme 7 — Rank 7 · 3 misses · ~31 marks-recovered index
## Who runs the loop: tool-use protocol and API statelessness

**(a) The misconception, in your own error terms.** You reason as if Claude executes tools and remembers the conversation, so when the loop breaks you go looking for a missing hook or a session parameter instead of for the step your own application skipped.

**(b) The correct mental model.** `Domain-2_v2 §2.1` gives the five-step cycle, and the ownership of each step is the whole exam point:

1. *You* define tools with `name`, `description`, `input_schema`.
2. *Claude* returns `stop_reason: "tool_use"` and a `tool_use` content block carrying an `id`.
3. **The application executes the tool.** Claude never executes anything.
4. **The application appends a `tool_result` content block** — and §2.1 states the purpose of the `id` field explicitly: *"`id` (for matching to `tool_result`)."*
5. Claude continues from the result.

`Domain-1_v2 §1.1` adds the control flow: the orchestrator inspects `stop_reason` — `tool_use` → execute, append, call again; `end_turn` → stop. KD #5 names the trap: *"'Parse Claude's text for "I'm done"' → Wrong. Use structured `stop_reason`, not natural language parsing."*

`Domain-5_v2 §5.1` closes the loop on memory: *"Claude's API is **fully stateless**. Every API call is independent. Claude has no server-side memory or session state. … Every request must include the complete conversation history in the `messages` array."* KD #25 kills the two invented mechanisms by name: a `session_id` parameter *"doesn't exist"*, and a vector database *"is for retrieval over long histories (months), not standard multi-turn conversations."* §5.1's second scenario is the corollary you should expect to be tested on: latency and cost rise as conversations grow *because* the whole history is resent each time — not because responses get longer or a database slows down.

**(c) The shape of the trap on the page.** A plausible-sounding parameter or mechanism that either does not exist or does not apply: `session_id`, `persist_context`, "enable conversation memory", or a `PostToolUse` hook offered as the thing that "writes the file." Hooks are the nastiest of these because they are real (`§2.7`) — but `PostToolUse` transforms the output of a tool that already ran, which is useless when no tool ran at all.

**(d) The decision rule under time pressure.** **Walk the five steps and find the one your application skipped.** Then apply two elimination rules that are true by construction: if an option has *Claude* executing something, it is wrong (`§2.1` step 3 belongs to the application). If an option adds state or memory on the API side, it is wrong (`§5.1` — the API is stateless, full stop).

**(e) Practice — Theme 7**

**Q7.1** You are writing the agent loop by hand. Claude returns `stop_reason: "tool_use"` with a block naming `write_report_file` and its arguments. Your harness logs the block, appends a `tool_result` reading "acknowledged", and sends the next request. No file is ever created, and Claude's next response discusses the file as though it exists. What is missing?

- **A.** A `PostToolUse` hook to write the file after the tool returns.
- **B.** The application must actually execute the tool and return its real result.
- **C.** `tool_choice` should be set to force the write tool so the call is guaranteed.
- **D.** The tool's `input_schema` needs a field instructing Claude to perform the write.

**Answer: B.** `Domain-2_v2 §2.1` — step 3 of the cycle is "Application executes the tool"; Claude never executes anything itself.
*A fails:* §2.7 — `PostToolUse` transforms or logs the output of a tool that already ran; here no tool ran. *C fails:* the call was already made; forcing it does not make the application run it. *D fails:* the schema describes arguments — no schema field causes execution, which is the application's job.

**Q7.2** Your harness receives a response containing two `tool_use` blocks in a single turn. It executes both tools and sends back one user message with two `tool_result` blocks, neither carrying an identifier. Claude's next response mixes the two, attributing one tool's output to the other. What is the most likely cause?

- **A.** Two tool calls in one turn are not supported; they must be issued in sequence.
- **B.** The results should have been sent as separate assistant messages rather than one user message.
- **C.** `stop_reason` should have been checked before either tool was executed.
- **D.** Each `tool_result` must reference the `id` of the `tool_use` block it answers.

**Answer: D.** `Domain-2_v2 §2.1` — the `tool_use` block's `id` exists "for matching to `tool_result`".
*A fails:* `Domain-1_v2 §1.15` — multiple calls in one response are supported and are exactly how parallel execution works. *B fails:* the message role is not the defect; the missing correlation identifier is. *C fails:* `Domain-1_v2 §1.1` — `stop_reason` decides whether to continue the loop, it does not correlate results back to calls.

**Q7.3** An agent answering follow-up questions about a document loses the thread: by the fourth exchange it re-asks which document is under discussion. The harness sends only the newest user message on each request. Total tokens across all four exchanges are under 3,000. An engineer proposes adding a vector database so the agent can remember. What is the actual cause and fix?

- **A.** The context window is being exceeded; enable summarisation of earlier turns.
- **B.** The application is not including prior messages — each request must carry the complete conversation history in the `messages` array.
- **C.** Claude needs a `session_id` so the API can associate the requests with one conversation.
- **D.** A vector database is required to give the agent conversational memory.

**Answer: B.** `Domain-5_v2 §5.1` — the API is fully stateless; the application manages conversation state by resending the full `messages` array.
*A fails:* §5.1 names this exact wrong diagnosis — a context-window overflow is "impossible in a 3-turn conversation." *C fails:* KD #25 — the `session_id` parameter "doesn't exist"; there is no server-side memory. *D fails:* KD #25 — vector databases serve retrieval over months of history, not standard multi-turn conversation state.

---

### Theme 8 — Rank 8 · 2 misses · ~24 marks-recovered index
## Skill frontmatter: `allowed-tools` vs `context: fork`

**(a) The misconception, in your own error terms.** You treat the two SKILL.md frontmatter keys as interchangeable "make this skill better behaved" switches, and pick whichever one the stem's tone suggests.

**(b) The correct mental model.** `Domain-3_v2 §3.3` defines them as answers to two different questions.

- **`context: fork` — where the output lands.** *"Runs skill in isolated subagent context (protects main session)."* Use it when a skill *"generates large output or exploration context"* so it *"does not pollute the main conversation window."* KD #13 scopes it: use for discovery, analysis, exploration, brainstorming; main session for implementation, design, conversation. §3.3 names the wrong fixes for this symptom too: switching to a faster model (*"doesn't fix context pollution"*), compressing results to a short summary (*"loses analysis capability"*), and splitting into two skills (*"doesn't prevent context leakage"*).
- **`allowed-tools` — what the skill may do.** §3.3 flags a documented divergence and tells you which side to answer on. *"Official Exam Guide framing (v0.2, task 3.2 — **this is what the exam tests**): `allowed-tools` **restricts tool access during skill execution** — e.g., 'limiting to file write operations to prevent destructive actions.'"* The current product docs frame it instead as a permission pre-grant (unlisted tools follow the normal permission flow rather than being hard-blocked) — see `CURRENT-DOCS-DELTA_v1.md` §D1 — but the corpus's standing rule is that **the official Exam Guide framing wins for exam answers**, and §3.3 notes both framings agree on the exam-relevant judgment anyway: `allowed-tools` is the key you reach for to scope a skill's capabilities.

The other named misconception in §3.3 is the *location*: *"tool scoping for a skill is configured in `.mcp.json`, `CLAUDE.md`, or a `config.json` commands array." Wrong — it lives in SKILL.md frontmatter.*

**(c) The shape of the trap on the page.** The two keys presented side by side as alternatives, over a stem whose symptom is written loosely enough to feel like either ("the skill is causing problems in the session"). Plus `.mcp.json` or CLAUDE.md offered as the configuration location — plausible because both are real config files you already know.

**(d) The decision rule under time pressure.** **Ask what the skill is doing wrong — filling the window, or reaching too far?** Output volume, lost main-session context, exploratory material bleeding into later turns → `context: fork`. Capability, destructive actions, "limit what it can touch" → `allowed-tools`. And whichever it is, the answer is in SKILL.md frontmatter and nowhere else.

**(e) Practice — Theme 8**

**Q8.1** Your `/survey-dependencies` skill walks a service's full dependency graph and prints every transitive edge it finds. After it runs, the session begins re-asking about the task the engineer had already scoped before invoking it, and later answers reference dependency detail nobody asked about. Which change fixes this while keeping the skill's full depth?

- **A.** Set `context: fork` so the skill runs in an isolated subagent context.
- **B.** Set `allowed-tools` to `[Read, Grep]` so the skill produces less output.
- **C.** Instruct the skill to compress its findings into a short summary before returning.
- **D.** Split it into two smaller skills invoked in sequence.

**Answer: A.** `Domain-3_v2 §3.3` and KD #13 — `context: fork` isolates a skill's large or exploratory output from the main conversation.
*B fails:* §3.3 — `allowed-tools` scopes what the skill may *do*, not where its output lands; the survey still floods the main session. *C fails:* §3.3 names compressing results as the wrong fix — it "loses analysis capability." *D fails:* §3.3 — splitting "doesn't prevent context leakage"; both halves still write into the main session.

**Q8.2** A `/summarize-incidents` skill is meant only to read incident files and write a digest. During a trial run it invoked `Bash` and created a git commit. The team wants the skill limited to reading and writing files, with no shell access, for everyone who uses it. Where is that configured?

- **A.** In `.mcp.json` at the project root, scoping the exposed tools.
- **B.** In the project `CLAUDE.md`, as an instruction not to use `Bash` during that skill.
- **C.** In the skill's `SKILL.md` frontmatter, via `allowed-tools`.
- **D.** By setting `context: fork` so the skill's shell calls run in an isolated context.

**Answer: C.** `Domain-3_v2 §3.3` — under the official Exam Guide framing (task 3.2), `allowed-tools` restricts tool access during skill execution, and the key lives in SKILL.md frontmatter.
*A fails:* §3.3 names `.mcp.json` explicitly as a misconception for skill tool scoping; `.mcp.json` configures MCP servers (`Domain-2_v2 §2.6`). *B fails:* §3.3 — an instruction is not a scoping mechanism, and the configuration point is SKILL.md frontmatter. *D fails:* `context: fork` isolates output; it does not restrict which tools a skill may use.

**Q8.3** Two complaints land about the same `/audit-permissions` skill. First: after it runs, the main session's later answers drift toward permission trivia and lose the original task. Second: on one run it used `Bash` to modify a policy file when it was only meant to report. Which pair of frontmatter changes addresses them, in that order?

- **A.** `allowed-tools` for the first, `context: fork` for the second.
- **B.** `context: fork` for both, since an isolated context cannot affect the project.
- **C.** `argument-hint` for the first, `allowed-tools` for the second.
- **D.** `context: fork` for the first, `allowed-tools` for the second.

**Answer: D.** `Domain-3_v2 §3.3` — fork controls where output lands; `allowed-tools` scopes what the skill may do.
*A fails:* it reverses the two mechanisms — restricting tools does not stop verbose output polluting the session, and forking does not prevent a destructive call. *B fails:* §3.3 — a forked skill still executes its tools for real; the isolation is of context, not of side effects. *C fails:* §3.3 — `argument-hint` displays expected arguments when the command is invoked and has no bearing on context pollution.

---

### Theme 9 — Rank 9 · 2 misses · ~24 marks-recovered index
## CLAUDE.md hierarchy mechanics: concatenation and `@import` depth

**(a) The misconception, in your own error terms.** You model the CLAUDE.md levels as an override chain in which the nearest file wins — and you are not certain of the `@import` mechanics.

**(b) The correct mental model.** `Domain-3_v2 §3.1` is unusually explicit here, because the corpus was corrected on this point in v2 (its changelog records: *"Corrected §3.1 hierarchy semantics (concatenated load order, not override precedence — verified against code.claude.com/docs 2026-07-06)"*).

- **Four levels, concatenated root → working directory:** user `~/.claude/CLAUDE.md`; project `<root>/CLAUDE.md` or `<root>/.claude/CLAUDE.md`; directory-level `CLAUDE.md` in any subdirectory; `.claude/rules/*.md` with YAML frontmatter for path-scoped conditional loading.
- **Concatenation, not precedence.** Verbatim: *"all discovered CLAUDE.md files are concatenated into context, from the root down to the working directory. Every discovered file contributes its instructions — a 'lower' file does not silently replace a 'higher' one."* And the misconception, named: *"'Lower levels override higher levels — a directory-level CLAUDE.md replaces the project-level one for that directory.' Wrong. … **There is no documented override-precedence mechanism between CLAUDE.md levels.**"* Conflicts are resolved *"by editing the files, not by relying on one level 'winning.'"*
- **`@import` rules:** `@` immediately before the path with **no space**; relative and absolute paths both supported; **relative paths resolve relative to the file containing the import**; **maximum import nesting depth is 5**.
- **Shared versus personal:** project-level config is version-controlled and reaches every team member; `~/.claude/CLAUDE.md` reaches only that developer and is *"NOT shared via version control."* KD #1 makes this the classic trap — a convention three engineers follow and a fourth does not is a user-scope file, not a project one.

One genuine override does exist in D3, and keeping it filed separately is what stops you conflating the two: a **personal skill of the same name overrides a project skill** (`§3.5`) — that is skills, not CLAUDE.md.

**(c) The shape of the trap on the page.** An option asserting that the closer or lower file "takes precedence" or "overrides." It is attractive because virtually every other config system you have used behaves that way — `.gitignore`, ESLint, `tsconfig`. The exam's answer is the opposite, and the corpus went out of its way to correct itself on this point. On `@import`, the trap is a wrong depth number (3 or 10, or "no limit") sitting next to the right one, or a claim that relative paths resolve from the repository root.

**(d) The decision rule under time pressure.** **For CLAUDE.md: nothing overrides, everything adds.** If two levels disagree, Claude sees both and the fix is editing a file, not layering one over another. Memorise three facts cold: import nesting depth is **5**; relative imports resolve from the **importing file's** location; `~/.claude/CLAUDE.md` is **never** shared. And when an option offers "override", check whether the stem is about CLAUDE.md (concatenation) or about **skills** (§3.5, where personal genuinely does override project).

**(e) Practice — Theme 9**

**Q9.1** The repository root `CLAUDE.md` says "use tabs for indentation." A `CLAUDE.md` inside `packages/analytics/` says "use four spaces." An engineer working in `packages/analytics/` expects the closer file to win and is surprised when Claude raises the conflict instead of silently applying the subdirectory rule. What is actually happening?

- **A.** The subdirectory file overrides the root file for files in that directory.
- **B.** All discovered CLAUDE.md files are concatenated into context, so Claude sees both instructions; conflicts are resolved by editing the files.
- **C.** The root file overrides the subdirectory file because it loads first.
- **D.** Only the file nearest the working directory loads; the root file is skipped.

**Answer: B.** `Domain-3_v2 §3.1` — concatenated load order, root down to working directory; every discovered file contributes.
*A fails:* §3.1 names this exact statement as the misconception — "There is no documented override-precedence mechanism between CLAUDE.md levels." *C fails:* the same error in the opposite direction; load order is concatenation order, not precedence. *D fails:* §3.1 — every discovered file contributes its instructions, none is skipped.

**Q9.2** Your root `CLAUDE.md` imports a standards index, which imports a language guide, which imports a testing guide, which imports a fixtures guide, which imports a naming guide. An engineer wants to add one more imported file below the naming guide. What do the documented `@import` rules say?

- **A.** Maximum import nesting depth is 3, so the chain is already over the limit.
- **B.** There is no documented nesting limit; imports resolve until the graph is exhausted.
- **C.** Nesting is unlimited, but relative paths resolve against the repository root, so deep chains break silently.
- **D.** Maximum import nesting depth is 5, so the proposed additional level would exceed it.

**Answer: D.** `Domain-3_v2 §3.1` — "Maximum import nesting depth is **5**"; the existing chain already sits at five levels.
*A fails:* the documented maximum is 5, not 3. *B fails:* §3.1 states an explicit maximum. *C fails:* two errors in one option — a maximum of 5 *is* documented, and §3.1 says relative paths "resolve relative to the file containing the import", not to the repository root.

**Q9.3** Four engineers share one repository. Three have Claude Code consistently add structured logging to every new service method; the fourth, who joined last month, never sees it added. All four are on the same commit, and `/memory` on her machine shows the project `CLAUDE.md` and her own user file loaded. What is the most likely cause?

- **A.** The logging convention lives in the three original engineers' `~/.claude/CLAUDE.md` files, which are not version-controlled.
- **B.** The project `CLAUDE.md` is being overridden by her user-level file.
- **C.** The convention sits in a `.claude/rules/` file whose glob does not match her working directory.
- **D.** Her session needs `/memory` refreshed so the project file reloads properly.

**Answer: A.** `Domain-3_v2 §3.1` and KD #1 — user-level config is "NOT shared via version control", which is exactly how a convention can hold for some team members and not others on the same repo.
*B fails:* §3.1 — levels concatenate; there is no override precedence between CLAUDE.md levels in either direction. *C fails:* a path-scoped rule would resolve identically for all four engineers on the same commit; the difference here is per-person, which points to user scope. *D fails:* `/memory` is a diagnostic that lists and manages loaded memory files (§3.1, §3.12) and has already confirmed the project file is loaded — a reload changes nothing.

---

## 5. Study Plan

### Reread priority

1. **`CCA-Prep_Domain-3_v2.md` §3.1, §3.6, §3.11** — the highest-value reading you can do. Two of these three failed a deliberate fresh re-test in Exam 8 after being flagged in Exam 7, and the log's verdict is that they are *"real, persistent gaps, not attempt-specific noise."* Read §3.1 twice: once for the `/memory` diagnostic, once for the concatenation semantics and `@import` rules (Theme 9 lives in the same section). For §3.11, build yourself the three-way table — every session → CLAUDE.md or `@import`; path-scoped → `.claude/rules/`; workflow, on demand → Skills.
2. **`CCA-Prep_Domain-4_v2.md` §4.6, then §4.5 / §4.7 / §4.9 / §4.10** — §4.6 is the third of the three sections that failed re-test. Read the three `tool_choice` rows as three different promises, and read §4.7's misconception box until "validated ≠ correct" is reflexive.
3. **`CCA-Prep_Domain-4_v2.md` §4.1, §4.2, §4.14, and §4.12** — build the failure-mode → technique table from Theme 5 as a one-page card. This is four misses across three exams, all from picking a good technique aimed at the wrong failure.
4. **`CCA-Prep_Domain-1_v2.md` §1.6, §1.8, §1.10** — highest marks-per-miss of anything on the list, because D1 carries 16 of the 60 questions. Focus specifically on the §1.8-versus-§1.10 discriminator (recoverable versus unrecoverable gap), which has now cost you a mark in each direction.
5. **`CCA-Prep_Exam-Mechanics_v2.md`, the "Answer Pattern Heuristics" table** — twelve rows, one page. Read it as a *tie-breaker table*, because Themes 1 and 2 are both decided by it and they pull in opposite directions. "Deterministic over probabilistic" and "Proportionate first response" are both in there; knowing which one governs a given stem is the skill.
6. **`CCA-Prep_Domain-2_v2.md` §2.2, §2.3, §2.4, §2.5, §2.1** — maintenance rather than repair. D2 has gone 45% → 100% → 91%; the log records KD #12 and KD #26 as *"durably cleared"*. Skim to hold the ground, do not spend your best hours here.
7. **`CCA-Prep_Domain-3_v2.md` §3.3 and §3.5; `CCA-Prep_Domain-5_v2.md` §5.1 and §5.13** — the two-miss and one-miss items. §3.3 needs one careful pass on the `allowed-tools` dual framing (answer with the official Exam Guide framing; `CURRENT-DOCS-DELTA_v1.md` §D1 explains why).
8. **`CCA-Prep_Key-Distinctions_v1.md`** — skim only. `GENERATION-INTELLIGENCE.md` records **zero "weak" rows** across all 29 Key Distinctions and notes that *"the learner's persistent gaps have moved OFF the Key Distinctions and ONTO whole corpus sections in D3 and D4."* Do not spend re-reading time here at the expense of items 1–4.

### Watchlist for the next attempt

- **A compliance percentage in the stem is a signal, not decoration.** "8% of calls", "~90% of the time", "one run in twelve" means the probabilistic layer has already been tried and failed. Pick the structural option (Theme 1).
- **But do not buy machinery you do not need.** Before choosing the heavier option, name the cause in one clause. Diagnosis, efficiency, and organisation problems get the proportionate fix; guarantees, irreversibility, and capability grants get the structural one (Theme 2 versus Theme 1).
- **"Every subagent succeeded" is a pointer to the coordinator.** Never to a subagent, never to a tool description (Theme 3).
- **Ask whether the missing data is still obtainable.** Yes → re-delegate. No → coverage-annotate and ship (Theme 3).
- **Before answering any `tool_choice` item, say what the stem needs: *a* tool, or *that* tool?** Then check whether a clean "nothing to report" run must still produce structured output — if so, `any`, never forced-specific (Theme 4).
- **"Zero parse failures but the values are wrong" is the expected outcome, not a schema defect.** Never pick "tighten the schema" and never pick "revert to prompt-based JSON" (Theme 4).
- **Underline the failure noun before reading the options.** Format → few-shot. Reasoning or N-item comparison → step-by-step cue. Two jobs in one pass → chaining. Judge on fit, not on which technique you like (Theme 5).
- **Single file, known cause, decided fix → direct execution.** No exceptions, no hedged "start direct and switch" (Theme 2).
- **"Works in some sessions, not others" → `/memory` first.** Not a louder instruction, and not a remedy chosen before the cause is known (Theme 2).
- **CLAUDE.md levels concatenate; personal *skills* override.** Two different mechanisms, and only one of them is an override (Theme 9).
- **Pacing is not your problem — use the surplus.** Your two clean attempts ran 32.5 s and 35.4 s per question against a 120 s budget, and Exam 8's log notes the three re-missed questions took 77 s, 37 s and 37 s, so they were *"considered wrong answers, not careless ones."* You have roughly three times the time you need. Spend it running the decision rules above explicitly rather than answering on first impression.
- **Answer everything.** `CCA-Prep_Exam-Mechanics_v2.md`: the platform requires an answer before advancing, and there is no penalty for a wrong answer — an unsure answer always gets submitted.
- **Target margin, not the line.** 42/60 clears 720. Your floor across five scored attempts is 45. Converting the D3 and D4 sections above is what turns an 880 into a comfortable pass rather than a close one.
