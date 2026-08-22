# [VERIFY] Fact-Drift Sweep — 2026-06-09

**Method:** 5 parallel Sonnet web-researchers re-checked every `[VERIFY]`/`[UNVERIFIED]` item across all 9 extension citation files against live Anthropic docs (`platform.claude.com`, `code.claude.com`, `modelcontextprotocol.io`, arXiv).
**Aggregate:** ~89 confirmed · ~10 drifted/additive · ~10 unverifiable (most already flagged in-file). The material is current; no pricing/multiplier/precedence/exit-code core fact reversed.

> **✓ Citations-touch pass APPLIED 2026-06-10:** every additive drift below is now recorded in the 9 citation files (each got a "Re-verified 2026-06-09" manifest line + a re-verification addendum; resolved [VERIFY] items marked in-place). Lesson HTML bodies untouched — drifts are additive, not reversals.

---

## ⚠ The one genuine error to fix (exam-relevant)
- **C-E6 hooks — `PostToolBatch` is BLOCKABLE via exit 2** (live Hooks doc: "stops the agentic loop before next model call"). Earlier framing grouped it with the post-hooks that "cannot block." → **Fixed** in `claude-code-configuration.html` + citations (this sweep).

## Resolved (previously [UNVERIFIED] → now confirmed)
- **Subagent `@agent-name` mention syntax exists** — `@agent-<name>` (local), `@agent-plugin:name` (plugin), via `@` typeahead. (C-E6 citations [VERIFY] #11 — resolve.)
- **No per-turn subagent concurrency cap** outside the Workflow runtime (16 concurrent / 1,000 total apply to Workflow only).
- **1M context needs no beta header** for the listed models; **MCP spec `2025-11-25`** still latest.

## Drifts / additions worth noting (additive — not reversals)
| Area | Update | Action |
|---|---|---|
| Prompt-eng (D3) | Structured Outputs support list now includes **Claude Mythos Preview**; **Sonnet 4.6 defaults to `high` effort** (new vs 4.5); Haiku 4.5 pinned snapshot `claude-haiku-4-5-20251001` | note added to citations |
| Models (D3/D5) | **Opus 4.8 does NOT support extended thinking** (adaptive only) — route extended-thinking workloads to Sonnet 4.6 | note added |
| Caching (D5) | `usage` now has a **`cache_creation`** sub-object (`ephemeral_5m_input_tokens` / `ephemeral_1h_input_tokens`); thinking blocks can't be tagged with `cache_control` but ARE cached passively | note added |
| Tool use (D4) | Per-model tool-use token table grew (Opus 4.8 290/410 still correct); **Mythos Preview rejects forced `tool_choice`** (400) | note added |
| Subagents (D1) | **Fork subagents** (v2.1.117+, `/fork` default v2.1.161) inherit full parent context — qualifies "subagents always start fresh"; 2 more built-ins (`statusline-setup`, `claude-code-guide`); **agent teams** as a higher construct | note added |

## Time-sensitive
- **Agent SDK / `claude -p` separate monthly credit starts June 15, 2026** (6 days out) — re-check billing after that date.
- `--bare` still NOT the `-p` default (planned).

## Still unverifiable (leave flagged in-file)
MAST category % split (41.8/36.9/21.3 — not in arXiv abstract); MRCR v2 8-needle scores; `context_management.applied_edits` field shape; `criticalSystemReminder_EXPERIMENTAL` TS field; Claude Code auto-compact %.

---
_Full per-researcher reports are in this session's transcript. Re-run this sweep close to exam day (volatile: model IDs, hook roster, billing, fork/agent-teams features)._
