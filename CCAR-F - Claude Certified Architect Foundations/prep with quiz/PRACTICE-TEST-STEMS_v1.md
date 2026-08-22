# PRACTICE-TEST-STEMS_v1

Source: `prep with quiz/source/guide_en.md`, practice test section (lines ~2120–3281). Extracted 2026-07-06.

## 1. Purpose and counts

This file serves two functions:

1. **Deduplication ledger.** The mock-exam generator must NEVER reuse or closely paraphrase any stem listed in Section 2. The learner will take this practice test himself; any overlap between generated mock questions and these stems destroys the assessment value of both. Treat every stem below as a hard exclusion — no verbatim reuse, no light paraphrase, no same-scenario-same-failure-mode near-clones.
2. **Style-calibration reference.** Section 3 profiles the register, structure, and distractor conventions of this question set. Future exam generators must imitate that register without copying the stems.

**True counts (as actually present in the file — the guide's own header claims "60 questions across 4 scenarios," which is wrong):**

- **Total questions: 76**
- **Scenarios: 5**

| Scenario | Questions | Count |
|---|---|---|
| Multi-agent Research System | Q1–Q15 | 15 |
| Claude Code for Continuous Integration | Q16–Q30 | 15 |
| Code Generation with Claude Code | Q31–Q45 | 15 |
| Customer Support Agent | Q46–Q60 | 15 |
| Conversational AI Architecture Patterns | Q61–Q76 | 16 |

Domain codes used in Section 2: D1 Agentic Architecture & Orchestration · D2 Tool Design & MCP · D3 Claude Code Config & Workflows · D4 Prompt Engineering & Structured Output · D5 Context Management & Reliability. Domain assignments are the most plausible primary domain per question (many straddle two).

## 2. Stem ledger

Stems are verbatim: the full Situation text plus the question line, without the four answer options and without answers. Note: in most questions the source ends the Situation with the question and then repeats it as a separate bolded question line; both occurrences are preserved verbatim, which is why many stems below end with a repeated question.

**Q1 · Multi-agent Research System · D1**
Stem: A document analysis agent discovers that two credible sources contain directly contradictory statistics for a key metric: a government report states 40% growth, while an industry analysis states 12%. Both sources look credible, and the discrepancy could materially affect the research conclusions. How should the document analysis agent handle this situation most effectively? Which approach is most effective?

**Q2 · Multi-agent Research System · D1**
Stem: The web-search and document-analysis agents have completed their tasks and returned results to the coordinator. What is the next step for creating an integrated research report? Which next step is most appropriate?

**Q3 · Multi-agent Research System · D1**
Stem: A document analysis subagent frequently fails when processing PDF files: some have corrupted sections that trigger parsing exceptions, others are password-protected, and sometimes the parsing library hangs on large files. Currently, any exception immediately terminates the subagent and returns an error to the coordinator, which must decide whether to retry, skip, or fail the whole task. This causes excessive coordinator involvement in routine error handling. What architectural improvement is most effective? Which improvement is most effective?

**Q4 · Multi-agent Research System · D1**
Stem: After running the system on "AI impact on creative industries," you observe that every subagent completes successfully: the web-search agent finds relevant articles, the document analysis agent summarizes them correctly, and the synthesis agent produces coherent text. However, final reports cover only visual art and completely miss music, literature, and film. In the coordinator logs, you see it decomposed the topic into three subtasks: "AI in digital art," "AI in graphic design," and "AI in photography." What is the most likely root cause? What is the most likely root cause?

**Q5 · Multi-agent Research System · D1**
Stem: The web-search subagent returns results for only 3 of 5 requested source categories (competitor sites and industry reports succeed, but news archives and social feeds time out). The document analysis subagent successfully processes all provided documents. The synthesis subagent must produce a summary from mixed-quality upstream inputs. Which error-propagation strategy is most effective? Which error-propagation strategy is most effective?

**Q6 · Multi-agent Research System · D1**
Stem: The document analysis subagent encounters a corrupted PDF file that it cannot parse. When designing the system's error handling, what is the most effective way to handle this failure? Which approach is most effective?

**Q7 · Multi-agent Research System · D2**
Stem: Production logs show a persistent pattern: requests like "analyze the uploaded quarterly report" are routed to the web-search agent 45% of the time instead of the document analysis agent. Reviewing tool definitions, you find that the web-search agent has a tool `analyze_content` described as "analyzes content and extracts key information," while the document analysis agent has a tool `analyze_document` described as "analyzes documents and extracts key information." How should you fix the misrouting problem? How should you fix the misrouting problem?

**Q8 · Multi-agent Research System · D1**
Stem: A colleague proposes that the document analysis agent should send its results directly to the synthesis agent, bypassing the coordinator. What is the main advantage of keeping the coordinator as the central hub for all communication between subagents? What is the main advantage of keeping the coordinator as the central hub?

**Q9 · Multi-agent Research System · D1**
Stem: The web-search subagent times out while researching a complex topic. You need to design how information about this failure is returned to the coordinator. Which error-propagation approach best enables intelligent recovery? Which error-propagation approach best enables intelligent recovery?

**Q10 · Multi-agent Research System · D2**
Stem: In your system design, you gave the document analysis agent access to a general-purpose tool `fetch_url` so it could download documents by URL. Production logs show this agent now frequently downloads search engine results pages to perform ad hoc web search—behavior that should be routed through the web-search agent—causing inconsistent results. Which fix is most effective? Which fix is most effective?

**Q11 · Multi-agent Research System · D1**
Stem: While researching a broad topic, you observe that the web-search agent and the document analysis agent investigate the same subtopics, leading to substantial duplication in their outputs. Token usage nearly doubles without a proportional increase in research breadth or depth. What is the most effective way to address this? What is the most effective way to address this?

**Q12 · Multi-agent Research System · D1**
Stem: During research, the web-search subagent queries three source categories with different outcomes: academic databases return 15 relevant papers, industry reports return "0 results," and patent databases return "Connection timeout." When designing error propagation to the coordinator, which approach enables the best recovery decisions? Which approach enables the best recovery decisions?

**Q13 · Multi-agent Research System · D5**
Stem: Production monitoring shows inconsistent synthesis quality. When aggregated results are ~75K tokens, the synthesis agent reliably cites information from the first 15K tokens (web-search headlines/snippets) and the last 10K tokens (document analysis conclusions), but often misses critical findings in the middle 50K tokens—even when they directly answer the research question. How should you restructure the aggregated input? How should you restructure the aggregated input?

**Q14 · Multi-agent Research System · D5**
Stem: In testing, the combined output of the web-search agent (85K tokens including page content) and the document analysis agent (70K tokens including chains of thought) totals 155K tokens, but the synthesis agent performs best with inputs under 50K tokens. Which solution is most effective? Which solution is most effective?

**Q15 · Multi-agent Research System · D1**
Stem: In testing, you observe that the synthesis agent often needs to verify specific claims while merging results. Currently, when verification is needed, the synthesis agent returns control to the coordinator, which calls the web-search agent and then re-invokes synthesis with the results. This adds 2–3 extra loops per task and increases latency by 40%. Your assessment shows 85% of these verifications are simple fact checks (dates, names, stats) and 15% require deeper research. Which approach most effectively reduces overhead while preserving system reliability? Which approach is most effective?

**Q16 · Claude Code for Continuous Integration · D3**
Stem: Your CI pipeline runs the Claude Code CLI (in `--print` mode) using CLAUDE.md to provide project context for code review, and developers generally find the reviews substantive. However, they report that integrating findings into the workflow is difficult—Claude outputs narrative paragraphs that must be manually copied into PR comments. The team wants to automatically post each finding as a separate inline PR comment at the relevant place in code, which requires structured data with file path, line number, severity level, and suggested fix. Which approach is most effective? Which approach is most effective?

**Q17 · Claude Code for Continuous Integration · D1**
Stem: Your team uses Claude Code for generating code suggestions, but you notice a pattern: non-obvious issues—performance optimizations that break edge cases, cleanups that unexpectedly change behavior—are only caught when another team member reviews the PR. Claude's reasoning during generation shows it considered these cases but concluded its approach was correct. Which approach directly addresses the root cause of this self-check limitation? Which approach directly addresses the root cause?

**Q18 · Claude Code for Continuous Integration · D2**
Stem: Your code review component is iterative: Claude analyzes the changed file, then may request related files (imports, base classes, tests) via tool calls to understand context before providing final feedback. Your application defines a tool that lets Claude request file contents; Claude calls the tool, gets results, and continues analysis. You're evaluating batch processing to reduce API cost. What is the primary technical limitation when considering batch processing for this workflow? What is the primary technical limitation?

**Q19 · Claude Code for Continuous Integration · D5**
Stem: Your CI/CD system runs three Claude-based analyses: (1) fast style checks on every PR that block merging until completion, (2) comprehensive weekly security audits of the entire codebase, and (3) nightly test-case generation for recently changed modules. The Message Batches API offers 50% savings but processing can take up to 24 hours. You want to optimize API cost while maintaining an acceptable developer experience. Which combination correctly matches each task to an API approach? Which combination is correct?

**Q20 · Claude Code for Continuous Integration · D4**
Stem: Your automated reviews find real issues, but developers report the feedback is not actionable. Findings include phrases like "complex ticket routing logic" or "potential null pointer" without specifying what exactly to change. When you add detailed instructions like "always include concrete fix suggestions," the model still produces inconsistent output—sometimes detailed, sometimes vague. Which prompting technique most reliably produces consistently actionable feedback? Which prompting technique is most reliable?

**Q21 · Claude Code for Continuous Integration · D5**
Stem: Your CI pipeline includes two Claude-based code review modes: a pre-merge-commit hook that blocks PR merge until completion, and a "deep analysis" that runs overnight, polls for batch completion, and posts detailed suggestions to the PR. You want to reduce API cost using the Message Batches API, which offers 50% savings but requires polling and can take up to 24 hours. Which mode should use batch processing? Which mode should use batch processing?

**Q22 · Claude Code for Continuous Integration · D4**
Stem: Your automated review analyzes comments and docstrings. The current prompt instructs Claude to "check that comments are accurate and up to date." Findings often flag acceptable patterns (TODO markers, simple descriptions) while missing comments describing behavior the code no longer implements. What change addresses the root cause of this inconsistent analysis? What change addresses the root cause?

**Q23 · Claude Code for Continuous Integration · D5**
Stem: Your automated code review system shows inconsistent severity ratings—similar issues like null pointer risks are rated "critical" in some PRs but only "medium" in others. Developer surveys show growing distrust—many start dismissing findings without reading because "half are wrong." High-false-positive categories erode trust in accurate categories. Which approach best restores developer trust while improving the system? Which approach best restores developer trust?

**Q24 · Claude Code for Continuous Integration · D5**
Stem: Your automated review generates test-case suggestions for each PR. Reviewing a PR that adds course completion tracking, Claude suggests 10 test cases, but developer feedback shows that 6 duplicate scenarios already covered by the existing test suite. What change most effectively reduces duplicate suggestions? What change is most effective?

**Q25 · Claude Code for Continuous Integration · D5**
Stem: After an initial automated review identifies 12 findings, a developer pushes new commits to address issues. Re-running review produces 8 findings, but developers report that 5 duplicate previous comments on code that was already fixed in the new commits. What is the most effective way to eliminate this redundant feedback while maintaining thoroughness? What is the most effective way to eliminate redundant feedback?

**Q26 · Claude Code for Continuous Integration · D3**
Stem: Your pipeline script runs `claude "Analyze this pull request for security issues"`, but the job hangs indefinitely. Logs show Claude Code is waiting for interactive input. What is the correct approach to run Claude Code in an automated pipeline? What is the correct approach?

**Q27 · Claude Code for Continuous Integration · D5**
Stem: A pull request changes 14 files in an inventory tracking module. A single-pass review that analyzes all files together produces inconsistent results: detailed feedback on some files but shallow comments on others, missed obvious bugs, and contradictory feedback (a pattern is flagged in one file but identical code is approved in another file in the same PR). How should you restructure the review? How should you restructure the review?

**Q28 · Claude Code for Continuous Integration · D4**
Stem: Your automated code review averages 15 findings per pull request, and developers report a 40% false-positive rate. The bottleneck is investigation time: developers must click into each finding to read Claude's rationale before deciding whether to fix or dismiss it. Your CLAUDE.md already contains comprehensive rules for acceptable patterns, and stakeholders rejected any approach that filters findings before developers see them. What change best addresses investigation time? What change best addresses investigation time?

**Q29 · Claude Code for Continuous Integration · D5**
Stem: Analysis of your automated code review shows large differences in false-positive rates by finding category: security/correctness findings have 8% false positives, performance findings 18%, style/naming findings 52%, and documentation findings 48%. Developer surveys show growing distrust—many start dismissing findings without reading because "half are wrong." High-false-positive categories erode trust in accurate categories. Which approach best restores developer trust while improving the system? Which approach best restores developer trust?

**Q30 · Claude Code for Continuous Integration · D5**
Stem: Your team wants to reduce API costs for automated analysis. Currently, synchronous Claude calls support two workflows: (1) a blocking pre-merge check that must complete before developers can merge, and (2) a technical debt report generated overnight for review the next morning. Your manager proposes moving both to the Message Batches API to save 50%. How should you evaluate this proposal? How should you evaluate this proposal?

**Q31 · Code Generation with Claude Code · D4**
Stem: You asked Claude Code to implement a function that transforms API responses into an internal normalized format. After two iterations, the output structure still doesn't match expectations—some fields are nested differently and timestamps are formatted incorrectly. You described requirements in prose, but Claude interprets them differently each time. Which approach is most effective for the next iteration?

**Q32 · Code Generation with Claude Code · D3**
Stem: You need to add Slack as a new notification channel. The existing codebase has clear, established patterns for email, SMS, and push channels. However, Slack's API offers fundamentally different integration approaches—incoming webhooks (simple, one-way), bot tokens (support delivery confirmation and programmatic control), or Slack Apps (two-way events, requires workspace approval). Your task says "add Slack support" without specifying integration method or requiring advanced features like delivery tracking. How should you approach this task?

**Q33 · Code Generation with Claude Code · D3**
Stem: Your CLAUDE.md file has grown to 400+ lines containing coding standards, testing conventions, a detailed PR review checklist, deployment instructions, and database migration procedures. You want Claude to always follow coding standards and testing conventions, but apply PR review, deploy, and migration guidance only when doing those tasks. Which restructuring approach is most effective?

**Q34 · Code Generation with Claude Code · D3**
Stem: You're tasked with restructuring your team's monolithic application into microservices. This impacts changes across dozens of files and requires decisions about service boundaries and module dependencies. Which approach should you choose?

**Q35 · Code Generation with Claude Code · D3**
Stem: Your team created a `/analyze-codebase` skill that performs deep code analysis—dependency scanning, test coverage counts, and code quality metrics. After running the command, team members report Claude becomes less responsive in the session and loses the context of the original task. How do you most effectively fix this while keeping full analysis capabilities?

**Q36 · Code Generation with Claude Code · D3**
Stem: Your team uses a `/commit` skill in `.claude/skills/commit/SKILL.md`. A developer wants to customize it for their personal workflow (different commit message format, extra checks) without affecting teammates. What do you recommend?

**Q37 · Code Generation with Claude Code · D3**
Stem: Your team has used Claude Code for months. Recently, three developers report Claude follows the guidance "always include comprehensive error handling," but a fourth developer who just joined says Claude does not follow it. All four work in the same repo and have up-to-date code. What is the most likely cause and fix?

**Q38 · Code Generation with Claude Code · D3**
Stem: You find that including 2–3 full endpoint implementation examples as context significantly improves consistency when generating new API endpoints. However, this context is useful only when creating new endpoints—not when debugging, reviewing code, or other work in the API directory. Which configuration approach is most effective?

**Q39 · Code Generation with Claude Code · D3**
Stem: Your team created a `/migration` skill that generates database migration files. It takes the migration name via `$ARGUMENTS`. In production you observe three issues: (1) developers often run the skill without arguments, causing poorly named files, (2) the skill sometimes uses database schema details from unrelated prior conversations, and (3) a developer accidentally ran destructive test cleanup when the skill had broad tool access. Which configuration approach fixes all three problems?

**Q40 · Code Generation with Claude Code · D3**
Stem: Your codebase contains areas with different coding conventions: React components use functional style with hooks, API handlers use async/await with specific error handling, and database models follow the repository pattern. Test files are distributed across the codebase next to the code under test (e.g., `Button.test.tsx` next to `Button.tsx`), and you want all tests to follow the same conventions regardless of location. What is the most supported way to ensure Claude automatically applies the correct conventions when generating code?

**Q41 · Code Generation with Claude Code · D3**
Stem: You want to create a custom slash command `/review` that runs your team's standard code review checklist. It should be available to every developer when they clone or update the repository. Where should you create the command file?

**Q42 · Code Generation with Claude Code · D3**
Stem: Your team's CLAUDE.md grew beyond 500 lines mixing TypeScript conventions, testing guidance, API patterns, and deployment procedures. Developers find it hard to locate and update the right sections. What approach does Claude Code support to organize project-level instructions into focused topical modules?

**Q43 · Code Generation with Claude Code · D3**
Stem: You create a custom skill `/explore-alternatives` that your team uses to brainstorm and evaluate implementation approaches before choosing one. Developers report that after running the skill, subsequent Claude responses are influenced by the alternatives discussion—sometimes referencing rejected approaches or retaining exploration context that interferes with actual implementation. How should you most effectively configure this skill?

**Q44 · Code Generation with Claude Code · D2**
Stem: Your team wants to add a GitHub MCP server for searching PRs and checking CI status via Claude Code. Each of six developers has their own personal GitHub access token. You want consistent tooling across the team without committing credentials to version control. Which configuration approach is most effective?

**Q45 · Code Generation with Claude Code · D5**
Stem: You're adding error-handling wrappers around external API calls across a 120-file codebase. The work has three phases: (1) discover all call sites and patterns, (2) collaboratively design the error-handling approach, and (3) implement wrappers consistently. In Phase 1, Claude generates large output listing hundreds of call sites with context, quickly filling the context window before discovery finishes. Which approach is most effective to complete the task while maintaining implementation consistency?

**Q46 · Customer Support Agent · D2**
Stem: While testing, you notice the agent often calls `get_customer` when users ask about order status, even though `lookup_order` would be more appropriate. What should you check first to address this problem? What should you check first?

**Q47 · Customer Support Agent · D4**
Stem: Your agent handles single-issue requests with 94% accuracy (e.g., "I need a refund for order #1234"). But when customers include multiple issues in one message (e.g., "I need a refund for order #1234 and also want to update the shipping address for order #5678"), tool selection accuracy drops to 58%. The agent usually solves only one issue or mixes parameters across requests. What approach most effectively improves reliability for multi-issue requests? What approach is most effective?

**Q48 · Customer Support Agent · D1**
Stem: Production logs show that for simple requests like "refund for order #1234," your agent resolves the issue in 3–4 tool calls with 91% success. But for complex requests like "I was billed twice, my discount didn't apply, and I want to cancel," the agent averages 12+ tool calls with only 54% success—often investigating issues sequentially and fetching redundant customer data for each. What change most effectively improves handling of complex requests? What change is most effective?

**Q49 · Customer Support Agent · D4**
Stem: Your agent achieves 55% first-contact resolution, well below the 80% target. Logs show it escalates simple cases (standard replacements for damaged goods with photo proof) while trying to handle complex situations requiring policy exceptions autonomously. What is the most effective way to improve escalation calibration? What is the most effective way to improve escalation calibration?

**Q50 · Customer Support Agent · D1**
Stem: After calling `get_customer` and `lookup_order`, the agent has all available system data but still faces uncertainty. Which situation is the most justified trigger for calling `escalate_to_human`? Which situation is most justified for escalation?

**Q51 · Customer Support Agent · D2**
Stem: Production logs show that in 12% of cases your agent skips `get_customer` and calls `lookup_order` directly using only the customer-provided name, sometimes leading to misidentified accounts and incorrect refunds. What change most effectively fixes this reliability problem? What change is most effective?

**Q52 · Customer Support Agent · D1**
Stem: Production metrics show that when resolving complex billing disputes or multi-order returns, customer satisfaction scores are 15% lower than for simple cases—even when the resolution is technically correct. Root-cause analysis shows the agent provides accurate solutions but inconsistently explains rationale: sometimes omitting relevant policy details, sometimes missing timeline info or next steps. The specific context gaps vary case by case. You want to improve solution quality without adding human oversight. What approach is most effective? What approach is most effective?

**Q53 · Customer Support Agent · D2**
Stem: Production metrics show your agent averages 4+ API loops per resolution. Analysis reveals Claude often requests `get_customer` and `lookup_order` in separate sequential turns even when both are needed initially. What is the most effective way to reduce the number of loops? What is the most effective way to reduce loops?

**Q54 · Customer Support Agent · D5**
Stem: Production logs show a pattern: customers reference specific amounts (e.g., "the 15% discount I mentioned"), but the agent responds with incorrect values. Investigation shows these details were mentioned 20+ turns ago and condensed into vague summaries like "promotional pricing was discussed." What fix is most effective? What fix is most effective?

**Q55 · Customer Support Agent · D1**
Stem: Your `get_customer` tool returns all matches when searching by name. Currently, when there are multiple results, Claude picks the customer with the most recent order, but production data shows this selects the wrong account 15% of the time for ambiguous matches. How should you address this? How should you address this?

**Q56 · Customer Support Agent · D4**
Stem: Production logs show a consistent pattern: when customers include the word "account" in their message (e.g., "I want to check my account for an order I made yesterday"), the agent calls `get_customer` first 78% of the time. When customers phrase similar requests without "account" (e.g., "I want to check an order I made yesterday"), it calls `lookup_order` first 93% of the time. Tool descriptions are clear and unambiguous. What is the most likely root cause of this discrepancy? What is the most likely root cause?

**Q57 · Customer Support Agent · D2**
Stem: Production logs show the agent often calls `get_customer` when users ask about orders (e.g., "check my order #12345") instead of calling `lookup_order`. Both tools have minimal descriptions ("Gets customer information" / "Gets order details") and accept similar-looking identifier formats. What is the most effective first step to improve tool selection reliability? What is the most effective first step?

**Q58 · Customer Support Agent · D1**
Stem: You are implementing the agent loop for your support agent. After each Claude API call, you must decide whether to continue the loop (run requested tools and call Claude again) or stop (present the final answer to the customer). What determines this decision? What determines this decision?

**Q59 · Customer Support Agent · D2**
Stem: Production logs show the agent misinterprets outputs from your MCP tools: Unix timestamps from `get_customer`, ISO 8601 dates from `lookup_order`, and numeric status codes (1=pending, 2=shipped). Some tools are third-party MCP servers you cannot modify. Which approach to data format normalization is most maintainable? Which approach is most maintainable?

**Q60 · Customer Support Agent · D4**
Stem: Production logs show the agent sometimes chooses `get_customer` when `lookup_order` would be more appropriate, especially for ambiguous queries like "I need help with my recent purchase." You decide to add few-shot examples to the system prompt to improve tool selection. Which approach most effectively addresses the problem? Which approach is most effective?

**Q61 · Conversational AI Architecture Patterns · D2**
Stem: Your `remove_team_member` tool uses a `dry_run: boolean` parameter for previewing impacts before execution. Production monitoring shows the agent bypasses the preview step by calling with `dry_run=false` directly. You need to ensure every removal is preceded by a preview that the user explicitly confirms. What is the most reliable approach?

**Q62 · Conversational AI Architecture Patterns · D2**
Stem: Production monitoring shows your `search_catalog` tool fails 12% of the time: 8% are network timeouts that succeed when retried, and 4% are query syntax errors that never succeed regardless of retries. Currently both error types are returned identically, causing wasted retries. How should you modify the tool's error handling?

**Q63 · Conversational AI Architecture Patterns · D1**
Stem: Over several turns discussing investment strategy, a user stated "I have a very low risk tolerance" and later "I want to maximize my returns." They now ask: "What should I invest in?" Which approach best ensures the recommendation aligns with the user's actual priority?

**Q64 · Conversational AI Architecture Patterns · D5**
Stem: Users refine playlist preferences over multiple conversation turns. Two messages after a user said "I love jazz," Claude asks "What genres do you enjoy?" What is the most likely cause?

**Q65 · Conversational AI Architecture Patterns · D5**
Stem: After a 40-minute cooking session, the conversation reaches 78,000 tokens. History includes allergies, recipe scaling, clarified cooking terms, and general discussion. You must reduce tokens while preserving important information. What approach best balances preservation with token reduction?

**Q66 · Conversational AI Architecture Patterns · D5**
Stem: Users report that during extended conversations the assistant loses track of earlier topics and preferences. Your current implementation keeps only the last 25 message pairs. What is the most effective solution?

**Q67 · Conversational AI Architecture Patterns · D5**
Stem: Users report that latency increases and costs rise when conversations exceed 50 turns. What is the primary cause?

**Q68 · Conversational AI Architecture Patterns · D5**
Stem: After three months of weekly sessions, conversation history grows to 85,000 tokens. When a user asks "What did we conclude about the theme of isolation?", the assistant gives generic answers instead of referencing previous discussions. What is the most effective approach?

**Q69 · Conversational AI Architecture Patterns · D5**
Stem: During QA testing, Claude follows system prompt guidelines for the first 10–15 turns, but later responses deviate. The conversation is still within token limits. What is the best solution?

**Q70 · Conversational AI Architecture Patterns · D4**
Stem: Your AI tutor has a 2,800-token system prompt defining teaching methodology and adaptation rules. After 12 turns, the assistant starts ignoring proficiency levels. What is the most effective fix?

**Q71 · Conversational AI Architecture Patterns · D4**
Stem: Your assistant must maintain an enthusiastic tone, explain its reasoning, and ask clarifying questions. Where should these behavioral guidelines be defined? Where should these behavioral guidelines be defined?

**Q72 · Conversational AI Architecture Patterns · D4**
Stem: Users report repetitive response openings like "Certainly!" and "I'd be happy to help!" What is the most effective approach?

**Q73 · Conversational AI Architecture Patterns · D5**
Stem: A webhook notifies your system that a user's package has shipped while the user is actively chatting. You want the assistant to incorporate this naturally into the next response. What is the best approach?

**Q74 · Conversational AI Architecture Patterns · D4**
Stem: Users frequently send requests like "Book a venue for the party." The assistant asks 4+ clarifying questions, causing 35% abandonment. What approach best improves the trade-off?

**Q75 · Conversational AI Architecture Patterns · D5**
Stem: Your assistant uses a contractor-persona system prompt. Early turns follow the rules, but by turn 7 the assistant gives generic advice. Conversation length is only 2,500 tokens. What is the most likely cause?

**Q76 · Conversational AI Architecture Patterns · D4**
Stem: Users ask vague requests like "Can you help with the report?" The assistant responds by asking multiple questions (which report? what help? deadline?), causing 40% abandonment. What is the best solution?

## 3. Style calibration profile

This is the register reference future exam generators must imitate — without copying or closely paraphrasing any Section 2 stem. All numbers below are computed over the 76 stems (Situation + question line, per Section 2) and all 304 answer options in the source.

### Stem length and structure

- **Word counts:** min **18** (Q67), median **51.5**, max **93** (Q16), mean 53.5. The typical stem is a 2–5 sentence paragraph.
- **Structure:** **76 of 76** stems open with scenario context (every question carries a `**Situation:**` block); **0** are pure direct questions. Even the shortest stems (scenario 5) give one to two sentences of situation before asking. In most questions the question appears twice: once at the end of the Situation paragraph and again as a standalone bolded question line (often a compressed restatement, e.g., "Which prompting technique most reliably produces consistently actionable feedback?" → "Which prompting technique is most reliable?").
- **Point of view:** 35/76 stems open with "You/Your..." (second-person architect-operator voice); 6 open with "Users/A user..."; 16 open with production/testing telemetry ("Production logs show...", "Production monitoring shows...", "While testing...", "In testing...", "During QA testing...").

### Option style

- **Count and length:** always exactly 4 options (A–D), one correct. Option word counts: min 2, **median 16**, max 36, mean 15.4. Distribution: 17 options ≤5 words, 125 at 6–15, 158 at 16–30, 4 over 30.
- **Grammatical form:** options within a question are strongly parallel — either all imperative fragments/full imperative sentences ("Add few-shot examples...", "Implement a routing layer...", "Reduce the number of tools...") or all declarative statements when the question is diagnostic ("The coordinator's task decomposition is too narrow...", "Your application isn't including prior messages in the `messages` array."). 301 of 304 options end with a period; virtually all are single complete sentences or sentence-length fragments, never multi-sentence.
- **Code/config content:** 63 of 304 options (~21%) contain inline code or config tokens in backticks (`--output-format json`, `context: fork`, `~/.claude/skills/commit/SKILL.md`, `dry_run=true`, `stop_reason`, `${GITHUB_TOKEN}`). There are no multi-line code-block options — code appears inline inside a prose option.
- The correct answer is not positionally biased toward any letter and is not systematically the longest option.

### Question forms (fraction of 76)

- **Best-approach selection** ("Which/What approach/change/fix/solution/technique/combination is most effective / best / most reliable / most appropriate / most maintainable / correct"): **51/76 ≈ 67%**. This is the dominant form.
- **"How should you..."** procedural restructuring ("How should you restructure the review?", "How should you fix the misrouting problem?", "How should you evaluate this proposal?"): **9/76 ≈ 12%**.
- **Diagnosis** ("What is the most likely root cause / most likely cause / primary cause / primary technical limitation / most likely cause and fix"): **7/76 ≈ 9%** (Q4, Q18, Q37, Q56, Q64, Q67, Q75).
- **Other judgment/fact forms** ("What is the main advantage...", "What should you check first?", "What do you recommend?", "Which situation is most justified for escalation?", "What determines this decision?", "Which mode should use batch processing?"): **7/76 ≈ 9%**.
- **Placement** ("Where should you create the command file?", "Where should these behavioral guidelines be defined?"): **2/76 ≈ 3%**.
- Notably absent: no "why did X happen" phrasing (diagnosis is always cast as "what is the cause"), no negative stems ("which is NOT..."), no multi-select, no true/false.

### Scenario framing conventions

Situations are introduced as operational evidence, not abstract theory:

- **Production telemetry** is the signature device: 20/76 stems cite logs, monitoring, metrics, or developer surveys; 19/76 contain at least one percentage; 41/76 contain some number (token counts like "~75K tokens"/"155K tokens", tool-call counts "12+ tool calls", turn counts, file counts "14 files", line counts "400+ lines"). Precise paired metrics are typical: "94% accuracy ... drops to 58%", "78% of the time ... 93% of the time", "55% first-contact resolution, well below the 80% target", "8% are network timeouts ... 4% are query syntax errors".
- **Quoted user messages and quoted instructions** appear in 23/76 stems ("I need a refund for order #1234", "check that comments are accurate and up to date", "I love jazz").
- **Inline code/config identifiers** appear in 21/76 stems: tool names in backticks (`get_customer`, `lookup_order`, `fetch_url`), CLI invocations (`claude "Analyze this pull request for security issues"`), file paths (`.claude/skills/commit/SKILL.md`), skill names (`/migration`). No stem embeds a multi-line log excerpt or config block — evidence is always summarized in prose with inline tokens.
- **Three verbatim representative stem openings:**
  1. "Production logs show a persistent pattern: requests like "analyze the uploaded quarterly report" are routed to the web-search agent 45% of the time instead of the document analysis agent." (Q7)
  2. "Your agent achieves 55% first-contact resolution, well below the 80% target. Logs show it escalates simple cases (standard replacements for damaged goods with photo proof) while trying to handle complex situations requiring policy exceptions autonomously." (Q49)
  3. "Your CLAUDE.md file has grown to 400+ lines containing coding standards, testing conventions, a detailed PR review checklist, deployment instructions, and database migration procedures. You want Claude to always follow coding standards and testing conventions, but apply PR review, deploy, and migration guidance only when doing those tasks." (Q33)
- Stems frequently end by naming an explicit constraint or goal before the question ("You want to improve solution quality without adding human oversight.", "stakeholders rejected any approach that filters findings before developers see them", "without affecting teammates", "while maintaining thoroughness").

### Distractor patterns (from the answer explanations)

The explanations reveal a consistent distractor taxonomy; a generator should build wrong options from these molds:

1. **Symptom-level fix vs root cause.** The correct answer is repeatedly justified as "directly addresses/fixes the root cause," while distractors patch downstream symptoms (post-processing filters, deduplication after the fact, regenerating bad outputs, reminder injection instead of fixing the prompt — Q11, Q22, Q24, Q31, Q70).
2. **Right concept, wrong mechanism / fabricated feature.** Plausible-sounding but nonexistent flags, parameters, or behaviors: `--batch` flag and `CLAUDE_HEADLESS=true` (Q26), `override: true` frontmatter (Q36), a required `session_id` parameter or vector-DB dependency for memory (Q64), Claude Code "caching" CLAUDE.md or "learning per-user preferences" (Q37).
3. **Prompt-compliance where deterministic enforcement is needed.** Instructions/few-shot examples offered where the correct answer enforces programmatically (programmatic preconditions Q51, tool-level retry logic Q62, token-bound two-tool split Q61, PostToolUse hook Q59, CLI `--output-format json` Q16) — "relying on LLM compliance with instructions" is the stated flaw.
4. **Over-engineering / infrastructure overkill.** Preprocessing classifiers, routing layers, separate trained models, vector databases, speculative execution, shared-state mechanisms — dismissed as adding latency and complexity when a lighter fix (better descriptions, few-shot examples, partitioning) suffices (Q7, Q46, Q47, Q49, Q53, Q57, Q65, Q76).
5. **The bigger-context misconception.** "Switch to a larger model / bigger context window / raise the threshold / widen the window" distractors, explicitly debunked: larger context does not fix attention quality, and widening a window "simply delays the same problem" (Q13-family, Q27, Q54, Q66).
6. **Silent failure / hidden information.** Options that skip errors silently, mark failures as successes, hide assumptions, or suppress findings by consensus voting ("report only issues found in at least two runs") — rejected for destroying transparency and suppressing real signal (Q5, Q6, Q9, Q12, Q27, Q74).
7. **Burden-shifting.** Options that push the problem onto humans or upstream actors instead of fixing the system ("require developers to split large PRs", forced escalation, structured intake forms) — Q27, Q74.

Explanation register (for generating answer keys in the same style): 2–4 sentences beginning "**Why X:**", first justifying the correct mechanism, then — especially in later scenarios — dismissing each distractor by letter with a one-clause reason.

### Duplication quirk worth knowing

The set itself contains internal near-duplicates (Q23 vs Q29 share options and answer; Q12/Q27 mirror a pre-test example question; Q6 vs Q3/Q9 revisit the same corrupted-PDF failure at different design depths). The mock-exam generator must not reproduce these stems either — being a duplicate inside the source does not exempt a stem from the ledger.
