# Domain 3: Claude Code Configuration & Workflows (20%)

**Source:** guide_en.MD — Chapters 6–8, Scenario: Code Generation with Claude Code, Claude Code for CI  
**Version:** 1.0 | 2026-06-27

---

## 3.1 CLAUDE.md Hierarchy

### Four Levels (highest → lowest precedence)
1. **User-level** — `~/.claude/CLAUDE.md` — applies to all projects for this user
2. **Project-level** — `<project-root>/CLAUDE.md` or `<project-root>/.claude/CLAUDE.md` — applies to entire project
3. **Directory-level** — `CLAUDE.md` in any subdirectory — applies when working in that directory
4. **Rules files** — `.claude/rules/*.md` with YAML frontmatter — path-scoped conditional loading

### Critical Rule: Shared vs Personal
- **Project-level config** is checked into version control → available to ALL team members
- **User-level config** lives in `~/.claude/CLAUDE.md` → only for that developer

**Exam scenario:** Three developers follow "always include comprehensive error handling." Fourth (new) doesn't. All use same repo.
- Root cause: ✅ Guidance is in the original developers' `~/.claude/CLAUDE.md`, not in the project `.claude/CLAUDE.md`
- Fix: Move instruction to project-level config

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

Rules load automatically when Claude works on files matching the glob patterns.

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
| `allowed-tools` | Restricts which tools the skill can use (least privilege) |

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
- **Project-wide** (available to all team members): `.claude/commands/` in the repo
- **Personal** (just for you): `~/.claude/commands/`

**Exam scenario:** Team wants `/review` command available to everyone who clones the repo.
- ✅ Create in `.claude/commands/` — version-controlled, auto-available

### `$ARGUMENTS` Variable
The text typed after the command name is available as `$ARGUMENTS` inside the command file.

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
- Claude explores, understands, designs — presents a plan before executing
- Avoids expensive rework from premature execution

### Direct Execution Mode
- Use when: scope is clear, approach is defined, changes are routine
- Claude implements immediately

**Exam scenarios:**
| Situation | Correct Mode |
|---|---|
| Restructure monolith into microservices (dozens of files) | Planning mode |
| Add Slack support (multiple valid integration approaches) | Planning mode |
| Implement function with well-defined input/output spec | Direct execution |

**Exam trap:** "Start in direct execution and switch to planning when it gets hard" → Wrong. Reactive switching is expensive. Plan upfront when the task demands it.

---

## 3.7 CI/CD Integration — `-p` / `--print` Flag

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

---

## 3.8 Structured Output from Claude Code CLI

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

## 3.9 Message Batches API

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

## 3.10 `@`-Imports in CLAUDE.md

```markdown
# CLAUDE.md
@./docs/api-conventions.md
@./docs/testing-guide.md
```

Imports referenced files' content into the effective CLAUDE.md. Use to modularize large instruction sets without placing everything in one file.

---

## 3.11 CLAUDE.md Content Organization Best Practices

**Exam scenario:** CLAUDE.md grew to 400+ lines mixing coding standards, PR checklists, deploy instructions, migration procedures.

- ✅ Keep universal standards in CLAUDE.md; create Skills for workflow-specific guidance (PR review, deploy, migrations) with trigger keywords
- Why: CLAUDE.md content loads in every session; Skills are invoked on demand
- Not preferred: Move everything to Skills (universal standards would need explicit invocation each time)
- Not preferred: Split CLAUDE.md into `.claude/rules/` (rules are path-scoped, not workflow-scoped)

**Exam scenario:** CLAUDE.md 500+ lines, hard to navigate.
- ✅ Create separate Markdown files in `.claude/rules/`, each covering one topic
- This is the supported modularization approach for instruction organization

---

## 3.12 Session Management

| Feature | Purpose |
|---|---|
| `--resume` | Resume a previous Claude Code session |
| `fork_session` | Create a branch of the current session |
| `/compact` | Compress context while preserving essential information |
| `/memory` | Access and manage persistent memory |

**Exam scenario:** Discovery phase fills context window before implementation phase.
- ✅ Use Explore subagent for discovery (isolates verbose output), returns summary to main session
- ❌ Use `/compact` mid-task (loses precision; implementation needs the full context)
