# CCA-F Integration Checkpoint B — Claude Code in CI/CD (D3 × D4)
_Cross-domain · exam Scenario 5 · ~20 min · design cold, then compare_

## Why this checkpoint exists

Domain 3 teaches headless Claude Code as a configuration topic — flags, permission modes, hooks, `--output-format` — and Domain 4 teaches structured output as a prompting topic — schemas, XML contracts, the Structured Outputs feature. The exam tests them separately, but **Scenario 5 (an automated PR-review bot running in CI) only works if you fuse them**: a headless invocation that is also schema-constrained, non-interactive, and reproducible. The transfer failure this catches: you can recite every D3 flag and every D4 output technique, yet still wire a pipeline that hangs on a permission prompt, emits prose instead of parseable JSON, or produces a different result on every run.

## The scenario

Your team wants Claude Code to review every pull request automatically. A **GitHub Actions** job triggers on each PR, runs Claude Code in **headless mode** against the diff, and posts the result back as a structured PR comment (severity, file, line, finding, suggested fix).

Hard constraints:
- **Non-interactive** — no TTY, no human at the keyboard. Any permission prompt would hang the runner until timeout.
- **Machine-parseable output** — a downstream step parses the result and calls the GitHub API to post comments. A `JSON.parse()` failure breaks the pipeline.
- **Deterministic / reproducible** — the same PR should not pull in a developer's local `CLAUDE.md`, personal hooks, or ad-hoc MCP servers. Two runs of the same commit should behave the same way.
- **Least-privilege tool access** — the bot reads code and the diff; it must not be able to edit files, push, or run arbitrary shell.
- **CI authentication** — no interactive `/login`; the runner needs a non-interactive credential.

## Design it cold (do this before scrolling)

1. **Which headless flags are non-negotiable** to make this run unattended? (Think: how do you even enter non-interactive mode, and how do you make the output a machine format rather than chat text?)
2. **How do you GUARANTEE the review JSON is parseable** — at the source, not by hoping the prompt holds? Which D4 mechanism makes malformed JSON *impossible*, and what is the correct fallback if it isn't available?
3. **What stops a permission prompt from hanging the runner?** Name the two levers (pre-allow specific tools vs. change the permission posture) and when each is appropriate.
4. **How do you keep the run reproducible** so a contributor's local `CLAUDE.md` / hooks / MCP servers / auto-memory don't leak into the review? Which single flag turns off auto-discovery?
5. **How does the runner authenticate** without an interactive login?
6. **What is the least-privilege `--allowedTools` set** for "read the diff, read code, produce a review" — and what must it NOT include?
7. **Where does the structured result actually land** in the output, and how does the next CI step read it?

Write your answer before reading on. The traps live in the *interaction* between these, not in any single one.

---

## Model architecture (compare your design)

**The invocation.** Non-interactive mode is entered with `-p` / `--print`, and the output is forced to a machine format with `--output-format json` (which also includes `total_cost_usd` in the envelope) (source: code.claude.com/docs/en/headless). The skeleton:

```bash
claude -p "Review the PR diff. Emit findings per the schema." \
  --output-format json \
  --json-schema review-schema.json \
  --bare \
  --allowedTools "Read,Bash(git diff *),Bash(git log *)" \
  --permission-mode dontAsk
```

**The parseable-output guarantee (the D4 half).** Do NOT rely on the prompt saying "respond in JSON." In an unattended pipeline that is a probabilistic hope. The source-level fix is **Structured Outputs / constrained decoding** — `--json-schema` for headless, backed by the JSON-outputs feature (`output_config.format`) — which makes invalid output impossible: "Always valid: No more `JSON.parse()` errors," "Reliable: No retries needed for schema violations" (source: platform.claude.com/.../structured-outputs). With `--json-schema`, the constrained result lands in the `structured_output` field of the JSON envelope, which the next CI step reads directly (source: code.claude.com/docs/en/headless). **Retry / dead-letter handling is the fallback, not the primary fix.** Schema rules to honor: `additionalProperties: false` is required; NOT supported are recursive schemas, external `$ref`, and numeric/string-length constraints (`minimum`, `maxLength`, etc.) (source: structured-outputs). First call pays a grammar-compile latency cost; compiled grammars cache for ~24h.

**The non-interactive permission posture (the D3 half).** Permission prompts are the classic CI hang. Two correct levers:
- **Pre-allow exactly what's needed** via `--allowedTools "Read,Bash(git diff *)"`. Combined with `--permission-mode dontAsk`, which "auto-denies tools unless pre-approved via `/permissions` or `permissions.allow` rules" (source: code.claude.com/docs/en/permissions) — so nothing prompts, and anything not on the allowlist is denied rather than blocking.
- `bypassPermissions` (≡ `--dangerously-skip-permissions`) "skips all permission prompts" — it removes the hang but is the wrong tool for a least-privilege review bot because it grants everything. Prefer `dontAsk` + a tight allowlist; reach for `bypassPermissions` only when the job genuinely needs broad access and the runner is otherwise sandboxed.

Remember permissions are evaluated **deny → ask → allow**, first match wins, and a bare tool name (`Bash`) removes the tool from context entirely while a scoped rule (`Bash(git diff *)`) leaves it available but constrained (source: permissions).

**The reproducibility lever.** `--bare` "skip[s] auto-discovery of hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md" — exactly the local-environment leakage you must eliminate for a deterministic CI run (source: code.claude.com/docs/en/headless). Note `--bare` requires `ANTHROPIC_API_KEY` or `apiKeyHelper` (it skips OAuth/keychain), so pair your auth choice with it deliberately.

**CI authentication.** For a subscription/OAuth setup, run `claude setup-token` once (generates a ~one-year OAuth token) and set `CLAUDE_CODE_OAUTH_TOKEN` as a CI secret (source: code.claude.com/docs/en/authentication). Auth precedence runs cloud-provider creds → `ANTHROPIC_AUTH_TOKEN` → `ANTHROPIC_API_KEY` → `apiKeyHelper` → `CLAUDE_CODE_OAUTH_TOKEN` → interactive `/login`. **Interaction trap:** because `--bare` skips OAuth/keychain, a `--bare` job must authenticate via `ANTHROPIC_API_KEY` or `apiKeyHelper`, not `CLAUDE_CODE_OAUTH_TOKEN` — so the auth method and the reproducibility flag are coupled, not independent choices.

**Least-privilege `allowedTools`.** Grant `Read` and the read-only git commands the review needs (`Bash(git diff *)`, `Bash(git log *)`). Do **not** include `Edit`/`Write`, unscoped `Bash`, or push/commit commands — the bot's job is to *report*, not mutate the repo. (Contrast the docs' fan-out example, which intentionally grants `Edit,Bash(git commit *)` because that job *does* migrate and commit — source: code.claude.com/docs/en/best-practices. Match the allowlist to the job, never copy it.)

The prompt itself should also be a good D4 prompt: a clear role + instructions, the schema referenced, and ideally a few `<example>` findings to steer format — but the *guarantee* of parseability comes from `--json-schema`, not the prose.

## The cross-domain traps this checkpoint tests

- **Prompt-only JSON in an unattended pipeline.** Telling Claude "reply in JSON" and parsing the text output of `--output-format json` is the #1 failure. Without `--json-schema` (Structured Outputs), one malformed run breaks the GitHub-comment step. The fix is source-level constrained decoding; retry is only the fallback.
- **A permission prompt hanging CI.** Forgetting that headless still evaluates permission rules. With `--permission-mode default`, the first un-allowed tool prompts forever on a TTY-less runner. Must pre-allow (`--allowedTools` + `dontAsk`) or, if broad access is required, `bypassPermissions`.
- **Non-reproducible runs from auto-discovery leakage.** Omitting `--bare` lets a contributor's local `CLAUDE.md`, `.claude/hooks`, project MCP servers, or auto-memory bleed into the review — two runs of the same commit diverge. `--bare` is the determinism lever.
- **`--output-format text` instead of `json`.** Defaulting to text gives you a chat transcript no downstream parser can consume, and you lose the `structured_output` field and `total_cost_usd`.
- **Coupling blind spot: auth vs. `--bare`.** Choosing `CLAUDE_CODE_OAUTH_TOKEN` *and* `--bare` together — `--bare` skips OAuth/keychain, so the OAuth token is ignored and auth fails. The reproducibility flag and the auth method must be chosen together (`--bare` ⇒ `ANTHROPIC_API_KEY`/`apiKeyHelper`).

## Self-score

Target — you should have named, cold:

| # | Lever | Got it? |
|---|---|---|
| 1 | Headless entry + machine output: `-p` + `--output-format json` | ☐ |
| 2 | Parseable-output **guarantee**: `--json-schema` / Structured Outputs (constrained decoding), not prompt-only; retry = fallback; result in `structured_output` | ☐ |
| 3 | No-hang permission posture: pre-allow via `--allowedTools` + `--permission-mode dontAsk` (or `bypassPermissions` when broad access is justified) | ☐ |
| 4 | Reproducibility lever: `--bare` (skips CLAUDE.md / hooks / skills / MCP / auto-memory) | ☐ |
| 5 | CI auth: `claude setup-token` → `CLAUDE_CODE_OAUTH_TOKEN` — and the `--bare` ⇒ API-key coupling | ☐ |
| 6 | Least-privilege `allowedTools`: read + read-only git only; no Edit/Write/push | ☐ |

**Scoring:** 6/6 = exam-ready on Scenario 5. 4–5/6 = solid, re-read the miss. ≤3/6, or if you reached for prompt-only JSON / forgot `--bare` / left permissions at `default` — log it to `../GAPS.md` (e.g. "CP-B: relied on prompt JSON instead of Structured Outputs in unattended pipeline") and re-attempt cold in 2 days.
