# CCA-F Exam Mechanics

**Source:** guide_en.MD — "Exam Format" and "Out-of-Scope Topics" sections  
**Version:** 1.0 | 2026-06-27

---

## Format

| Attribute | Value |
|---|---|
| Question type | Multiple choice (4 options, single correct answer) |
| Scoring scale | 100–1000 |
| Passing score | 720 |
| No guessing penalty | Unanswered = 0 pts; wrong answer = same as 0 — always guess |
| Scenario structure | 8 scenarios exist; 4 randomly selected per sitting |
| Questions per scenario | ~15 questions each (based on practice test = 60 Q / 4 scenarios) |
| Total questions (real exam) | Not published; practice test is 60 Q |

---

## Scenario Bank (5 documented + 3 implied)

Questions are scenario-anchored. Each question gives a **Situation** (log output, code pattern, user report, architectural decision) and asks what to do / what's the root cause / which approach is best.

### Documented Scenarios

1. **Multi-agent Research System**
   - Coordinator delegates to: web-search agent, document-analysis agent, synthesis agent
   - Key themes: task decomposition, error propagation, coverage annotations, coordinator-hub pattern, context passing, source attribution

2. **Claude Code for Continuous Integration**
   - Key themes: `-p`/`--print` flag for non-interactive mode, Message Batches API (batch vs real-time), `--output-format json`, per-file vs full-PR review passes, few-shot for consistent output, independent review instances

3. **Code Generation with Claude Code**
   - Key themes: CLAUDE.md hierarchy, `.claude/rules/` glob patterns, skills with `context: fork` and `allowed-tools`, planning mode vs direct execution, personal vs project skill precedence, MCP config with env vars

4. **Customer Support Agent**
   - Key themes: tool description clarity, `stop_reason` loop control, PostToolUse hooks, escalation criteria, multi-issue decomposition, context accumulation, `get_customer` before `lookup_order` preconditions

5. **Conversational AI Architecture Patterns**
   - Key themes: stateless API (all history in `messages[]`), behavioral drift across turns, prefilling to suppress filler phrases, context injection via user-message prefix, progressive summarization trade-offs

---

## Answer Pattern Heuristics (from practice test analysis)

These patterns appear repeatedly as the correct-answer logic:

| Heuristic | When it applies |
|---|---|
| Fix the root cause, not the symptom | Misrouting → fix tool descriptions, not add a classifier |
| Least privilege | Give synthesis agent only `verify_fact`, not full web-search access |
| Deterministic over probabilistic | Programmatic precondition > prompt instruction for critical sequencing |
| Structured error context > generic failure | Always return what failed, what was attempted, partial results |
| Parallel with shared context > sequential | Multi-issue requests: decompose and parallelize |
| Coordinator as hub | Subagents never talk to each other directly; always via coordinator |
| Fix root cause before adding infrastructure | Wrong tool descriptions → fix them; don't add a routing layer |
| Independence for review passes | Second Claude instance with no access to first's reasoning = true independent review |

---

## Out-of-Scope Topics (will NOT appear on exam)

Source: guide_en.MD "Out-of-Scope Topics" section

- Fine-tuning or training custom Claude models
- Claude API authentication, billing, or account management
- Language/framework-specific implementation details (beyond tool/schema config)
- Deploying or hosting MCP servers (infrastructure, networking, containers)
- Claude's internal architecture, training process, or model weights
- Constitutional AI, RLHF, or safety training methodologies
- Embedding models or vector database implementation details
- Computer use (browser automation, desktop interaction)
- Image analysis / Vision capabilities
- Streaming API or server-sent events
- Rate limiting, quotas, or detailed API cost calculations
- OAuth, API key rotation, or authentication protocol details
- Cloud-provider-specific configurations (AWS, GCP, Azure)
- Performance benchmarks or model comparison metrics
- Prompt caching implementation details (beyond knowing it exists)
- Token counting algorithms or tokenization specifics

---

## Scoring Context

- Scale: 100–1000 (not percentage-based)
- Pass: 720
- No partial credit per question
- No penalty for wrong answers → always select an answer
- Domain-weighted: D1 questions worth more collectively than D5 questions
