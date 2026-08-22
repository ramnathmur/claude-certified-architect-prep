# Gate 1 — FIDELITY review: `claude-code-configuration.html`

**VERDICT: PASS** — 0 blockers · 0 majors · 4 minors

PASS bar (0 blockers, 0 majors) is met. Every number, field name, path, hook-event name, permission-mode name, CLI flag, code snippet, and verbatim quote in the lesson traces to the citations file. All 7 inline MCQs/predict-reveals and all 10 final-quiz questions have correct `data-correct` answers and accurate explanations. The exam-trap facts (settings override vs permission-rule merge; deny→ask→allow with deny absolute; only exit code 2 blocks; bare tool name removes from context vs scoped pattern blocks calls; memory is concatenated context, not enforced config) are all stated correctly. All [VERIFY]-flagged volatile facts carry a visible badge/note. The four findings below are minor (one cosmetic count error, three citation-precision nits); none would mislead a learner on an exam-relevant fact.

---

## Detailed verification (the load-bearing checks)

### Quiz / MCQ answer key — all correct
| Item | `data-correct` (0-idx) | Marked answer | Correct per citations? |
|---|---|---|---|
| Sec B MCQ | 2 | "All discovered files are concatenated… broadest first… most specific read last" | ✓ (Memory) |
| Sec C MCQ | 3 | "Model = opus (project overrides user), but BOTH permission rules apply — merge, then deny→ask→allow" | ✓ (Settings) |
| Sec D MCQ | 1 | "Deny wins — evaluated first and absolute" | ✓ (Permissions) |
| Sec E MCQ | 2 | "PreToolUse with exit 2 (or `permissionDecision: deny`)" | ✓ (Hooks) |
| Sec F MCQ | 0 | "Skill takes precedence; commands merged into skills; `.claude/commands/` still works" | ✓ (Skills) |
| Sec G MCQ | 3 | "Today's `local` scope — was called `project` in older versions, `~/.claude.json`, you-only" | ✓ (MCP) |
| Sec H MCQ | 1 | "Letting Claude jump straight to coding can produce code that solves the wrong problem" | ✓ (Best practices) |
| Final Q1 | 2 | Managed > CLI > Local > Project > User; managed can't be overridden | ✓ |
| Final Q2 | 3 | Permission rules merge across scopes | ✓ |
| Final Q3 | 0 | deny → ask → allow; deny absolute | ✓ |
| Final Q4 | 1 | Exit 2 blocks; exit 1 non-blocking | ✓ |
| Final Q5 | 2 | Concatenated; context not enforced config; use PreToolUse hook | ✓ |
| Final Q6 | 3 | `//Users/alice/file` is the true absolute path | ✓ |
| Final Q7 | 1 | `local` "was called `project` in older versions" | ✓ |
| Final Q8 | 0 | Commands merged into skills; skill takes precedence | ✓ |
| Final Q9 | 2 | `hooks`, `mcpServers`, `permissionMode` ignored in plugin subagents | ✓ |
| Final Q10 | 1 | `--bare` (requires `ANTHROPIC_API_KEY` or `apiKeyHelper`) | ✓ |

### Exam-trap accuracy — all correct
- **Settings override but permission rules merge** — stated verbatim and repeatedly (lines 256, 499, 569, Q2). ✓
- **deny → ask → allow, deny absolute** — verbatim "denied at any level, allowed at none" (lines 597, 674, Q3). ✓
- **Only exit code 2 blocks; exit 1 non-blocking** — verbatim (lines 776, Q4, predict-reveal 835). ✓
- **Bare tool name removes from context vs scoped pattern blocks calls** — verbatim (line 623). ✓
- **Memory is concatenated context, not enforced config** — verbatim (lines 370, 396, Q5). ✓

### [VERIFY] coverage — all volatile facts flagged
docs-host migration (currency note + sources [VERIFY] block) ✓ · hook-event roster (line 741–742 badge + note) ✓ · `auto`/`dontAsk` modes (lines 646–647, 651 badges) ✓ · MCP scope renames local-was-project/user-was-global (line 1029 badge) ✓ · model IDs (sources block item 6) ✓ · June-15-2026 SDK-credit note (line 1107 badge) ✓ · managed-settings paths (line 547 badge + 553 note) ✓ · import 4-hop depth (taught at lines 399, 441 — citations mark this STABLE, so no badge required; acceptable) ✓.

### "Lesson framing" labeling — clean
Every non-verbatim assertion is tagged `lesson framing` / "not a verbatim Anthropic quote" exactly where the citations file marks it (two-axis model line 281; `--add-dir` 322; client-enforced permissions 661; Task→Agent rename 425/922; when-to-use decision table 962). No Anthropic "quote" was found that isn't faithfully present in the citations.

---

## Findings (all minor)

| # | Severity | Location | What's wrong | Correct value per citations | Suggested fix |
|---|---|---|---|---|---|
| 1 | Minor | Hero pills, line 223: `🎨 8 diagrams` | Only **7** `<figure>` diagrams exist (captions a, b, c, d, e, g, h — there is no diagram "f"). The count is off by one and the letter sequence skips "f". | n/a (not a citations fact — internal consistency) | Change pill to `7 diagrams`, or add a Section-F diagram and relabel; at minimum keep caption letters contiguous. |
| 2 | Minor | Sec C managed-settings callout, line 551 | Windows `HKCU\SOFTWARE\Policies\ClaudeCode` is shown without the qualifier the citations give. | Citations (line 176): "`HKCU\SOFTWARE\Policies\ClaudeCode` (user, **lowest**)". | Append "(user, lowest)" to match, so the precedence ordering of the two registry hives is preserved. |
| 3 | Minor | Sec C reload paragraph, line 545 & key-takeaway line 570 | Lists live-reload keys as "`permissions`, `hooks`, `apiKeyHelper`" and restart keys as "`model`, `outputStyle`" — correct, but presented as if exhaustive ("Live-reload keys include…" is fine; the key-takeaway drops the "include" hedge). | Citations (line 171) say "edits to **most** keys apply… without a restart" and give these only as examples. | In the key-takeaway, keep the "include"/"e.g." hedge so it doesn't read as the complete set. |
| 4 | Minor | Sec H, line 1102 | "(formerly 'Claude Code SDK')" is presented inline with a `⚠ VERIFY` badge but no `lesson framing` tag, whereas the parallel rename note for Task→Agent (line 425/922) is tagged `lesson framing`. | Citations (VERIFY item 9) support the rename as fact; this is a labeling-consistency nit, not a wrong claim. | Optional: tag consistently (either both `lesson framing` or rely on the VERIFY badge for both). No factual change needed. |

---

## Spot-checks that PASSED (no finding)
- Four-scope table (lines 300–303) and feature→location map (312–316) match citations tables byte-for-byte, including the MCP "odd one out" (`~/.claude.json` for local+user, `.mcp.json` for project).
- Memory load-order table + managed-policy OS paths (line 361) match exactly (macOS `/Library/Application Support/ClaudeCode/CLAUDE.md`, Linux/WSL `/etc/claude-code/CLAUDE.md`, Windows `C:\Program Files\ClaudeCode\CLAUDE.md`).
- `@`-import example block (401–404), managed `claudeMd` JSON (414–416), `settings.json` example (523–542), hook stdin (757–763), exit-code table (769–771), universal JSON output (782–787), PreToolUse decision JSON incl. `defer` value (789–795), hook config with `if` (803–819), subagent file format (911–919), `plugin.json` (927–932), `marketplace.json` (935–945), `.mcp.json` (1046–1054), fan-out loop (1113–1116) — all verbatim-faithful.
- Six permission modes table (643–648) matches; `auto`/`dontAsk` correctly flagged volatile; `--enable-auto-mode` removed v2.1.111 correct (line 651).
- 30-event hook roster (line 742) matches the citations list; classic stable 9-subset correct; no-matcher events correct.
- MCP transports incl. `streamable-http` alias and `ws` JSON-only; three install-scope table; 5-level scope precedence with "no field merge"; auto-memory "first 200 lines or 25KB" + `autoMemoryEnabled` + v2.1.59+ — all correct.
- Auth precedence 6-tier ladder (line 1108) matches citations exactly; `--bare`, output formats, `total_cost_usd`, `structured_output` all correct.
- Subagent priority table (903–907) and the 8-consecutive-block Stop-hook override (line 1144) match.
- No hallucinated facts found: every CLI flag, env var, and field name in the lesson appears in the citations.
