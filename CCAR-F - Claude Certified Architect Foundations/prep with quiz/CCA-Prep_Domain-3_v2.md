# Domain 3: Claude Code Configuration & Workflows (20%)

**Source:** guide_en.MD — Chapters 5–6 (Ch 5.1–5.10, Ch 6.4), Scenario: Code Generation with Claude Code, Claude Code for CI; Official Exam Guide Task Statements 3.1–3.6  
**Version:** 2.0 | 2026-07-06  
**Changelog v2:** Added §3.7 Iterative Refinement (official task 3.5 — previously missing). Corrected §3.1 hierarchy semantics (concatenated load order, not override precedence — verified against code.claude.com/docs 2026-07-06). Corrected §3.3 `allowed-tools` semantics (permission grant, not restriction — verified against current docs 2026-07-06). Expanded §3.1 with `@import` syntax (merged former §3.10), `/memory` diagnosis, and hierarchy-diagnosis workflow. Expanded §3.8 (CI/CD) with re-run consistency, session context isolation, and test-generation context. All v1 content retained; sections renumbered.

---

## 3.1 CLAUDE.md Hierarchy, `@import`, and Memory Diagnosis

### Levels (concatenated load order, root → working directory)
1. **User-level** — `~/.claude/CLAUDE.md` — applies to all projects for this user
2. **Project-level** — `<project-root>/CLAUDE.md` or `<project-root>/.claude/CLAUDE.md` — applies to entire project
3. **Directory-level** — `CLAUDE.md` in any subdirectory — applies when working with files in that directory
4. **Rules files** — `.claude/rules/*.md` with YAML frontmatter — path-scoped conditional loading

### Critical Semantics: Concatenation, NOT Override Precedence
Current official docs (code.claude.com/docs, verified 2026-07-06) describe the hierarchy as a **concatenated load order**: all discovered CLAUDE.md files are concatenated into context, from the root down to the working directory. Every discovered file contributes its instructions — a "lower" file does not silently replace a "higher" one.

- ✅ All levels load together; instructions accumulate. If two files conflict, Claude sees both — resolve conflicts by editing the files, not by relying on one level "winning."
- ❌ **Misconception:** "Lower levels override higher levels — a directory-level CLAUDE.md replaces the project-level one for that directory." Wrong. The files are concatenated, not overridden. There is no documented override-precedence mechanism between CLAUDE.md levels.

### Critical Rule: Shared vs Personal
- **Project-level config** is checked into version control → available to ALL team members
- **User-level config** lives in `~/.claude/CLAUDE.md` → only for that developer; **NOT shared via version control**

**Exam scenario:** Three developers follow "always include comprehensive error handling." Fourth (new) doesn't. All use same repo.
- Root cause: ✅ Guidance is in the original developers' `~/.claude/CLAUDE.md`, not in the project `.claude/CLAUDE.md`
- Fix: Move instruction to project-level config
- Diagnosis workflow: run `/memory` on the new teammate's machine to list which memory files are actually loaded — the project instruction will be visibly absent

### `@import` Syntax — Modular CLAUDE.md
CLAUDE.md can reference external files with `@path`, keeping configuration modular:

```markdown
# CLAUDE.md
Coding standards: @./standards/coding-style.md
Test requirements: @./standards/testing-requirements.md
Project overview: @README.md
```

Rules for `@path`:
- `@` immediately before the path (no space); relative and absolute paths supported
- Relative paths resolve relative to the file containing the import
- Maximum import nesting depth is **5**

Use `@import` to selectively include only the standards files relevant to each package — e.g., each package's CLAUDE.md imports the standards files its maintainers know apply to that package, instead of every package loading one giant global file.

### `/memory` — Verifying What Is Loaded
`/memory` shows and manages the memory files loaded in the current session.
- Use it to **verify which memory files are loaded** and to **diagnose inconsistent behavior across sessions** (e.g., an instruction that works on one machine but not another)
- First diagnostic step whenever "Claude follows rule X sometimes but not always": check whether the file holding rule X is actually in the loaded set

**Exam scenario:** Claude applies a convention in some sessions but not others.
- ✅ Run `/memory` to check which memory files are loaded in each session — the convention likely lives in a file that isn't consistently discovered (wrong level, wrong directory)
- ❌ Repeat the instruction louder in the prompt each session (treats symptom, not root cause)

---

## 3.2 `.claude/rules/` — Path-Scoped Conditional Rules

### Structure
```
.claude/rules/
  testing.md          # glob: **/*.test.*
  api-conventions.md  # glob: src/api/**/*.ts
  react.md            # glob: src/components/**/*.tsx
```

### YAML Frontmatter
```yaml
---
paths:
  - "**/*.test.tsx"
  - "**/*.test.ts"
---
# Testing Conventions
...
```

Rules load automatically **only** when Claude works on files matching the glob patterns — irrelevant rules stay out of context, saving tokens.

### When to Use `.claude/rules/` vs CLAUDE.md

| Use Case | Best Location |
|---|---|
| Conventions that apply always | Root `CLAUDE.md` |
| Conventions scoped to file type/directory | `.claude/rules/` with glob patterns |
| Workflow-specific guidance (PR review, deploy) | Skills in `.claude/skills/` |

**Exam scenario:** React components use hooks, API handlers use async/await, DB models use repository pattern. Tests co-located next to code.
- ✅ `.claude/rules/` with glob patterns — ensures correct conventions regardless of which directory you're in
- ❌ Root CLAUDE.md under headings (relies on model inference, not deterministic file-path matching)
- ❌ Separate CLAUDE.md in every subdirectory (doesn't work well when files are spread across many dirs)

---

## 3.3 Skills — `.claude/skills/`

### Skill Structure
```
.claude/skills/
  commit/
    SKILL.md
  migration/
    SKILL.md
```

### SKILL.md Frontmatter Options
```yaml
---
description: Generate a database migration file
argument-hint: "<migration-name>"
context: fork
allowed-tools: [Write, Read]
---
```

| Frontmatter Key | Purpose |
|---|---|
| `description` | Shown in slash command menu |
| `argument-hint` | Displayed when invoking command, prompts for required args |
| `context: fork` | Runs skill in isolated subagent context (protects main session) |
| `allowed-tools` | Scopes tool access during skill execution — see the dual framing below |

### `allowed-tools` Semantics — Two Framings (answer the exam with the official one)
**Official Exam Guide framing (v0.2, task 3.2 — this is what the exam tests):** `allowed-tools` **restricts tool access during skill execution** — e.g., "limiting to file write operations to prevent destructive actions." Exam questions about scoping a skill's capabilities expect `allowed-tools` as the answer.

**Current product docs framing (code.claude.com/docs/en/skills, verified 2026-07-06):** `allowed-tools` lists tools Claude can use **without asking the user for permission** while the skill is active — a permission pre-grant; unlisted tools follow the normal permission flow rather than being hard-blocked. See `CURRENT-DOCS-DELTA_v1.md` §D1.

Both framings agree on the exam-relevant judgment: `allowed-tools` is the SKILL.md frontmatter key you reach for to scope what a skill may do.

- ✅ Exam answer: to limit a skill to safe file operations, set `allowed-tools` in its SKILL.md frontmatter (e.g., `[Write, Read]`)
- ✅ Real-world nuance: the mechanism is permission pre-granting, so scope it minimally — anything unlisted still surfaces a permission prompt
- ❌ **Misconception:** "tool scoping for a skill is configured in `.mcp.json`, `CLAUDE.md`, or a `config.json` commands array." Wrong — it lives in SKILL.md frontmatter.

### `context: fork` — Critical Use Case
When a skill generates large output or exploration context, `context: fork` runs it in an **isolated subagent context** so the output does not pollute the main conversation window.

**Exam scenario:** `/analyze-codebase` skill causes Claude to lose context of original task.
- ✅ Add `context: fork` in skill frontmatter
- ❌ Switch to faster model (doesn't fix context pollution)
- ❌ Compress results to short summary (loses analysis capability)

**Exam scenario:** `/explore-alternatives` skill — rejected approaches bleed into subsequent implementation.
- ✅ Add `context: fork` — exploration runs in isolation; results summarized back
- ❌ Split into two skills (doesn't prevent context leakage)

---

## 3.4 Custom Slash Commands — `.claude/commands/`

### Location
- **Project-wide** (available to all team members): `.claude/commands/` in the repo — version-controlled
- **Personal** (just for you): `~/.claude/commands/` — not shared via VCS

**Exam scenario:** Team wants `/review` command available to everyone who clones the repo.
- ✅ Create in `.claude/commands/` — version-controlled, auto-available

### `$ARGUMENTS` Variable
The text typed after the command name is available as `$ARGUMENTS` inside the command file.

Note: in current Claude Code, `.claude/commands/` (legacy, still supported) and `.claude/skills/` (current) are unified — both create `/name` commands.

---

## 3.5 Personal vs Project Skill Precedence

Personal skills override project skills with the **same name**.

**Exam scenario:** Developer wants to customize `/commit` without affecting teammates.
- ✅ Create personal skill at `~/.claude/skills/commit/SKILL.md` — same command name, personal override
- ❌ Create `~/.claude/skills/my-commit/SKILL.md` — creates new `/my-commit` command, loses familiar name

---

## 3.6 Planning Mode vs Direct Execution

### Planning Mode
- Use when: large scope, architectural decisions, multiple approaches possible, complex changes across many files
- Claude explores, understands, designs — presents a plan before executing (Read/Grep/Glob only, no side effects)
- Avoids expensive rework from premature execution

### Direct Execution Mode
- Use when: scope is clear, approach is defined, changes are routine
- Claude implements immediately

### Combined Approach
1. Planning mode for investigation and design → 2. User approves plan → 3. Direct execution to implement

**Exam scenarios:**
| Situation | Correct Mode |
|---|---|
| Restructure monolith into microservices (dozens of files) | Planning mode |
| Add Slack support (multiple valid integration approaches) | Planning mode |
| Library migration affecting 45+ files | Planning mode |
| Implement function with well-defined input/output spec | Direct execution |
| Single-file bug fix with a clear stack trace | Direct execution |

**Exam trap:** "Start in direct execution and switch to planning when it gets hard" → Wrong. Reactive switching is expensive. Plan upfront when the task demands it.

---

## 3.7 Iterative Refinement — Progressive Improvement (Official Task 3.5)

Four named techniques for converging on correct output faster than blind re-prompting.

### 3.7.1 The Interview Pattern
Instead of letting Claude generate from an underspecified brief and then iterating on wrong output, have Claude **interview YOU first** — ask clarifying questions to surface considerations you may not have anticipated before it implements anything.

```
Claude: "Before implementing caching for the API, a few questions:
1. Which cache invalidation strategy — TTL or event-based?
2. Is stale data acceptable when the cache is unavailable?
3. Should caching be per-user or global?
4. What is the expected data volume to cache?"
```

**When it pays off:**
- Unfamiliar domains (fintech, healthcare, legal) where you don't know what you don't know
- Tasks with non-obvious implications (cache invalidation strategies, failure modes)
- Multiple viable approaches where the best choice depends on context only you have

**Exam scenario:** Developer asks for a caching layer in an unfamiliar domain; first three generated versions each miss a different requirement (invalidation, stale reads, multi-tenancy).
- ✅ Restart with the interview pattern — "ask me what you need to know before implementing" — requirements are gathered up front instead of discovered through failed iterations
- ❌ Keep iterating on the generated code one missed requirement at a time (slow, and each fix can disturb the last)
- ❌ **Misconception:** "Asking Claude to interview you wastes a turn — it's faster to generate first and correct after." Wrong. For underspecified tasks, one interview turn replaces several correction cycles; requirements surfaced up front prevent rework.

### 3.7.2 Test-Driven Iteration
Write the test suite **first** — covering expected behavior, edge cases, and performance requirements — then iterate by sharing test failures until everything is green.

- Tests are an objective, machine-checkable definition of "done"; prose acceptance criteria are not
- Each iteration feeds Claude the concrete failures, so refinement is targeted, not guesswork
- Providing a specific failing test case with example input and expected output is the fastest way to fix an edge case (e.g., null values in a migration script)

**Exam scenario:** Migration script mishandles null values; the developer keeps describing the bug in prose and gets partial fixes.
- ✅ Provide a concrete test case: sample input row containing nulls + exact expected output; iterate until the test passes
- ❌ Re-describe the bug more emphatically ("really handle ALL nulls") — prose descriptions of edge cases are interpreted inconsistently
- ❌ **Misconception:** "Write tests after generation to verify the result." That's verification, not test-driven iteration — writing tests first anchors generation to the spec and gives every iteration a concrete failure signal.

### 3.7.3 Concrete Input/Output Examples (2–3)
When natural-language descriptions of a transformation are interpreted inconsistently, provide **2–3 concrete input/output example pairs**. Examples are the most effective way to communicate expected transformations — they unambiguously show format and decision logic, and the model generalizes the pattern to new cases rather than just repeating the examples.

**Exam scenario:** A data-transformation prompt described in prose produces a differently-shaped output on each run.
- ✅ Add 2–3 concrete input→output example pairs to the prompt to anchor the transformation
- ❌ Lengthen the prose description with more adjectives (still ambiguous)
- ❌ **Misconception:** "Examples make the model copy the samples instead of generalizing." Wrong. Well-chosen examples demonstrate the pattern; the model applies it to novel inputs.

### 3.7.4 Batching Feedback: One Message vs Sequential
- **Interacting/interdependent issues → one detailed message.** When fixes affect each other, fixing them separately can conflict — fix A can invalidate or collide with fix B. Presenting all interacting issues together lets Claude design one coherent change.
- **Independent issues → sequential iteration.** When fixes don't interact, one-at-a-time keeps each iteration focused and easy to verify.

**Exam scenario:** Review found three issues in one function: a locking bug, a retry bug that depends on the locking behavior, and an unrelated typo in a log string.
- ✅ Send the locking + retry issues together in one detailed message (they interact — fixing retry without knowing the new locking design produces a conflicting patch); the typo can go separately or ride along
- ❌ Feed all three strictly one at a time — the sequential locking fix and retry fix can contradict each other, forcing another round
- ❌ **Misconception:** "Always report one issue per message so Claude can focus." Wrong for interdependent issues — separate fixes to interacting problems can conflict; interdependent fixes belong in a single message.

---

## 3.8 CI/CD Integration — `-p` / `--print` and Pipeline Practices

### Non-Interactive Mode
To run Claude Code in a CI/CD pipeline (no user interaction):
```bash
claude -p "Analyze this pull request for security issues"
```

- `-p` (or `--print`) processes the prompt, prints to stdout, and exits
- Without `-p`, Claude Code waits for interactive input → pipeline hangs

**Exam trap options to reject:**
- `--batch` — does not exist
- `CLAUDE_HEADLESS=true` — does not exist
- `stdin < /dev/null` — Unix workaround, not the documented approach

### Re-Runs: Include Prior Review Results
When a review re-runs after new commits, **include the prior review's findings in the prompt** and instruct Claude to report only new or still-unaddressed issues.
- Keeps the reviewer consistent across runs instead of re-litigating previously settled findings
- Prevents duplicate inline PR comments on unchanged code

**Exam scenario:** CI review posts near-duplicate comments (with slightly different wording) every time the author pushes a follow-up commit.
- ✅ Feed the previous run's findings into the re-run prompt; instruct: report only new or unresolved issues
- ❌ **Misconception:** "Each re-run should start from a blank slate so the review stays objective." Wrong. A blank-slate re-run re-litigates old findings and floods the PR with duplicates; prior findings in context keep the reviewer consistent.

### Session Context Isolation for Review
The same Claude session that generated code is **less effective at reviewing its own changes** — it retains its reasoning context and is less likely to challenge its own decisions. Use an independent instance for review.

### Context for CI-Invoked Claude
- **CLAUDE.md** is the mechanism for giving CI-invoked Claude project context: testing standards, fixture conventions, review criteria — improves test-generation quality and reduces low-value output
- **Existing test files in context** when generating tests → avoids suggesting duplicate scenarios already covered by the suite

---

## 3.9 Structured Output from Claude Code CLI

```bash
claude -p "Review this PR for security" --output-format json --json-schema schema.json
```

- `--output-format json` — forces JSON output
- `--json-schema` — enforces schema (guarantees well-formed output parseable by downstream tools)

**Exam scenario:** Team wants to auto-post each finding as an inline GitHub PR comment (needs file path, line number, severity, suggested fix).
- ✅ `--output-format json` with `--json-schema` — reliable structured output for GitHub API parsing
- ❌ Add "Output Format" section to CLAUDE.md (not guaranteed consistent)
- ❌ Format instruction in prompt (variable compliance)

---

## 3.10 Message Batches API

### When to Use Batch vs Real-Time

| Use Case | API | Reason |
|---|---|---|
| Blocking pre-merge checks | Synchronous | Developers waiting; must complete quickly |
| Overnight tech-debt reports | Batch API | Flexible deadline; 50% cost savings |
| Nightly test generation | Batch API | Scheduled task; 24h window acceptable |
| Weekly security audits | Batch API | Not blocking; scheduled |

### Batch API Properties
- **Cost:** 50% savings vs synchronous
- **Latency:** Up to 24 hours (no SLA)
- **Identifier:** `custom_id` per request for matching outputs to inputs
- **Limitation:** No multi-turn tool calling — batch is fire-and-forget; cannot execute a tool mid-request and return results

**Exam trap:** Iterative code review that fetches related files via tool calls mid-analysis → **cannot use batch API** because batch cannot execute tools during a request and return results to Claude.

---

## 3.11 CLAUDE.md Content Organization Best Practices

**Exam scenario:** CLAUDE.md grew to 400+ lines mixing coding standards, PR checklists, deploy instructions, migration procedures.

- ✅ Keep universal standards in CLAUDE.md; create Skills for workflow-specific guidance (PR review, deploy, migrations) with trigger keywords
- Why: CLAUDE.md content loads in every session; Skills are invoked on demand
- Not preferred: Move everything to Skills (universal standards would need explicit invocation each time)
- Not preferred: Split CLAUDE.md into `.claude/rules/` (rules are path-scoped, not workflow-scoped)

**Exam scenario:** CLAUDE.md 500+ lines, hard to navigate.
- ✅ Create separate Markdown files in `.claude/rules/`, each covering one topic (testing.md, api-conventions.md, deployment.md)
- This is the supported modularization approach for instruction organization
- `@import` (see §3.1) is the complementary approach when content should remain part of the concatenated CLAUDE.md context but live in separate files

---

## 3.12 Session Management

| Feature | Purpose |
|---|---|
| `--resume` | Resume a previous (named) Claude Code session with saved context |
| `fork_session` | Create a branch of the current session — both forks inherit context up to the branch point, then diverge (useful for comparing approaches) |
| `/compact` | Compress context while preserving essential information — risk: exact numeric values, dates, and specific details can be lost in summarization |
| `/memory` | Verify which memory files are loaded; manage persistent memory (see §3.1) |

**When to start a NEW session instead of resuming:** tool results are stale (files changed since), or context has degraded — better to restart with a short summary of prior findings than resume with old tool data.

**Exam scenario:** Discovery phase fills context window before implementation phase.
- ✅ Use Explore subagent for discovery (isolates verbose output), returns summary to main session
- ❌ Use `/compact` mid-task (loses precision; implementation needs the full context)
