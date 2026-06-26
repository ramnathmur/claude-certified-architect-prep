# GAPS.md — Misconceptions & Weak Areas

**Purpose:** Running log of anything answered incorrectly in module quizzes or mock exams. Review this before every practice session and before the real exam.

---

## How to Use

When a quiz question is missed, log it here:
- **What was asked** (paraphrase the question)
- **What I said** (the wrong answer)
- **What is correct** (the right mental model, not just the right words)
- **Pattern to remember** (one sentence that captures the rule)

---

## Active Gaps

### Module 0 — Foundations (run 2026-06-06) · ⚠ SYNTHETIC RUN
> Ram was distracted and authorised a self-driven pass; answers below were **modeled by Claude, not Ram's real recall**. Score (4/5) is illustrative only — re-run Module 0 interactively to capture a genuine baseline before trusting these as resolved.

- **Asked:** Why does a *scaled* score (720/1000) matter more than raw %?
  - **Modeled answer:** "Scaled means it's curved."
  - **Correct:** Not curved. *Scaled* = questions carry unequal weight and scores normalise across exam forms, so hard scenario/anti-pattern items hold most of the points; you can't pass by volume of easy recall.
  - **Pattern to remember:** Scaled score → study for judgment, not coverage.
- **Asked:** Name the exam scenarios from memory.
  - **Modeled answer:** Got 5; blanked on one.
  - **Correct:** The missed one is **Developer Productivity** (official Domain 2 — Tool Design & MCP). Full set is **6** (verified against the official exam guide): Customer Support Resolution Agent · Code Generation with Claude Code · Multi-Agent Research System · Developer Productivity with Claude · Claude Code for Continuous Integration · Structured Data Extraction.
  - **Pattern to remember:** **6** scenarios, 4 appear per sitting. (An earlier community guide wrongly claimed 8 — there is no Conversational-AI or Agentic-AI-Tools scenario.)

---

### Module 1 — Agentic Architecture (run 2026-06-06) · ⚠ SYNTHETIC RUN
> Self-driven (Ram distracted); answers modeled by Claude, not real recall. Score 4.5/5 illustrative. Re-run interactively — this is the 27% domain, the highest-value module to do for real.

- **Asked:** Orchestrator calls 8 tools in one turn — design smell?
  - **Modeled answer:** "Yes, too many tools / doing too much."
  - **Correct:** It *depends*. Parallel calls to **independent** tools is good design (cuts latency, Anthropic encourages it). It's a smell only if the calls are **interdependent/need sequencing**, the orchestrator is doing **worker grunt-work** instead of delegating, or it's **runaway** tool-calling. The count isn't the tell — the dependency structure is.
  - **Pattern to remember:** Parallel-independent = good; interdependent-or-grunt-work = smell. Judge dependency, not count.

### Modules 2–5 (run 2026-06-06) · ⚠ SYNTHETIC BATCH RUN
> Self-driven (Ram distracted); answers modeled by Claude, not real recall. Scores illustrative. Re-run interactively for genuine baselines.

**Module 2 — Claude Code (4/5).** Gap: "run a command after every file save" is a **PostToolUse hook in settings.json** (the harness runs it), NOT a `CLAUDE.md` memory instruction — Claude can't reliably self-enforce "always." *Pattern: automations = hooks; preferences = memory.*

**Module 3 — Prompt Engineering (4.5/5).** Gap: for malformed-JSON at scale, the first lever is **Structured Outputs (constrained decoding)** which makes invalid output *impossible at the source* — retry/dead-letter is the fallback, not the primary fix. *Pattern: prevent at the source > catch after.*

**Module 4 — Tool Design & MCP (4.5/5).** Gap: when a tool returns a 500, **recoverable-vs-escalate is an architectural decision** encoded in the error surface (retry-with-backoff for transient, graceful degradation for partial, human escalation for persistent/auth) — not simply "Claude retries." *Pattern: the architecture decides recovery; the model only adapts within it.* (Also: current transport term is **Streamable HTTP**, not standalone SSE.)

**Module 5 — Context Management (4.5/5).** Gap: **CALM = Compress, Anchor, Layer, Monitor** — the L is **Layer** (system vs history vs injected context), not "Limit." *Pattern: cache_control goes after the stable prefix, before the variable per-turn content.*

---

## Resolved Gaps

> Move entries here once you can answer the question correctly 3 times in a row without prompting.

