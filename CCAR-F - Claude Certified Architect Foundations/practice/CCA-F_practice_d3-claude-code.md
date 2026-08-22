# CCA-F Practice — Domain 3: Claude Code Configuration & Workflows (20%)
_10 questions · original, exam-style · grounded in EXAM-DIGEST + D3 citations_

## Questions

**Q1.** A team lead adds a line to the project `CLAUDE.md`: "NEVER run `terraform apply` without explicit human approval." During a session, Claude reads an issue that instructs it to provision infrastructure, and it proceeds to run `terraform apply` anyway. The lead is surprised the instruction "failed." What is the correct architectural explanation and fix?
- A) CLAUDE.md instructions are case-sensitive; rewriting the rule in lowercase will make Claude honor it.
- B) The rule was placed in the project file, which loses to the user file by precedence; move it to `~/.claude/CLAUDE.md` so it overrides.
- C) CLAUDE.md is loaded as context, not enforced configuration; to hard-block the action, use a PreToolUse hook (or a deny permission rule).
- D) The line must be added to `CLAUDE.local.md`, the only memory scope that enforces blocking behavior.

**Q2.** An architect wants four behaviors configured in Claude Code: (1) project naming conventions that should bias every session, (2) a guaranteed code formatter that runs after every file write with no way for Claude to skip it, (3) a multi-step "release" procedure invoked on demand, and (4) lint instructions that apply only when editing files under `infra/`. Which mapping to extension surfaces is correct?
- A) (1) Hook · (2) CLAUDE.md · (3) Skill · (4) Rule
- B) (1) CLAUDE.md · (2) Hook · (3) Skill · (4) Rule (with `paths:` frontmatter)
- C) (1) Rule · (2) Skill · (3) Hook · (4) CLAUDE.md
- D) (1) Skill · (2) Rule · (3) Hook · (4) CLAUDE.md

**Q3.** A developer has these permission entries across scopes: managed settings `deny: ["Bash(rm *)"]`, project settings `allow: ["Bash(rm *)"]`, and a PreToolUse hook that returns `permissionDecision: "allow"` for `rm` commands. Claude attempts `rm -rf build/`. What happens?
- A) The hook's `allow` decision is evaluated last and wins, so the command runs.
- B) The project `allow` rule and the managed `deny` rule cancel out, falling back to an interactive prompt.
- C) The command is blocked — deny is evaluated first and a managed deny cannot be overridden by any other level, and hook decisions do not bypass deny rules.
- D) The command runs because permission rules merge across scopes, and a merged set containing one `allow` permits it.

**Q4.** A reviewer claims: "Settings always override by precedence — Managed > CLI > Local > Project > User — so if my project `settings.json` defines a permission `allow` rule, it completely replaces the user-level `allow` rules." Where is this reasoning wrong?
- A) It isn't wrong; permission rules follow the same override precedence as every other setting.
- B) Most settings override by precedence, but permission rules *merge* across scopes rather than override — the user and project allow rules combine.
- C) The precedence order is actually User > Project > Local > CLI > Managed, so the claim is backwards.
- D) Permission rules also override, but only `deny` rules override; `allow` rules merge.

**Q5.** A developer wants Claude to find every place in the codebase that calls the function `processPayment`, including inside files whose names give no hint. Which built-in tool is the right primary choice, and why is the common alternative wrong?
- A) Glob, because it matches file paths and patterns recursively across the tree.
- B) Bash with `find`, because shell tools are more flexible than Claude's built-in tools.
- C) Grep, because it searches text *inside* files; Glob only matches filenames/paths, so it can't find in-file references.
- D) Read on each file in turn, because only Read can inspect file contents reliably.

**Q6.** A teammate says: "I always turn on plan mode when I want Claude to think harder about a tricky algorithm — it's basically the same as extended thinking." Which correction is accurate?
- A) Correct — `--permission-mode plan` and extended thinking are two names for the same reasoning feature.
- B) Plan mode is a workflow control that gates Claude to read-only exploration and proposing before it edits; extended thinking improves reasoning quality. They are different and can be combined.
- C) Plan mode disables thinking entirely to save tokens, so it is the opposite of extended thinking.
- D) Plan mode is only available in the headless SDK, while extended thinking is interactive-only.

**Q7.** An engineer writes a PreToolUse hook to enforce a security policy: if the proposed Bash command touches `/etc`, the hook prints an error to stderr and exits with code `1`. In testing, the dangerous command still runs. What is the bug?
- A) PreToolUse hooks cannot block Bash commands; only PostToolUse hooks can.
- B) Exit code 1 is treated as a non-blocking error and execution continues; only exit code 2 blocks the action (or return `permissionDecision: "deny"`).
- C) The hook must write to stdout, not stderr, for the block to register.
- D) Hooks only run after the permission prompt, so the command had already been approved before the hook fired.

**Q8.** A developer ran an exploratory session yesterday that built up useful context, then closed the terminal. They want to branch off that exact session to try two different refactors in parallel without the two attempts contaminating each other's *conversation* history, and they also need the working-tree files isolated. Which combination is correct?
- A) Use `--continue` twice in two terminals; sessions are safe to resume concurrently.
- B) Use `--fork-session` (with `--resume` to target the session) to branch the transcript per attempt, and use git branches/worktrees for file isolation.
- C) Use `--session-id` with the same UUID in both terminals; the filesystem is automatically snapshotted per session.
- D) Sessions store filesystem state, so simply resuming the session in each terminal restores isolated files automatically.

**Q9.** A platform team is wiring Claude Code into CI to migrate files in a loop. They need: (a) reproducible runs that ignore whatever skills/MCP/CLAUDE.md happen to be on the runner, (b) machine-parseable results that include the run's dollar cost, and (c) non-interactive auth that doesn't depend on a developer's keychain login. Which set of choices satisfies all three?
- A) `claude -p` with `--output-format text`; rely on the default OAuth keychain login.
- B) Interactive `claude` with plan mode; parse the terminal scrollback; export `ANTHROPIC_API_KEY` from the dev's laptop.
- C) `claude -p` with `--bare` (skips auto-discovery) and `--output-format json` (includes `total_cost_usd`); authenticate via `claude setup-token` → `CLAUDE_CODE_OAUTH_TOKEN`.
- D) `claude -p` with `--fork-session`; `--output-format stream-json` without `--verbose`; log in with `/login` inside the CI job.

**Q10.** A senior engineer just finished a large, security-sensitive change in a long Claude Code session and asks Claude — in that same session — "now review this for vulnerabilities." Why is this a recognized anti-pattern, and what is the recommended practice?
- A) It's fine; the session that wrote the code has the most context and will give the most accurate review.
- B) The author session is biased toward justifying its own work and shares the assumptions that produced any bugs; review in a fresh context — a new session, a dedicated subagent, or CI.
- C) The problem is only token cost; running `/compact` first makes the same-session review reliable.
- D) Reviews must always run in `bypassPermissions` mode, which is unavailable in the original session.

---

## Answer Key

**Q1 — C.** CLAUDE.md (all scopes) is loaded as context that Claude *treats as guidance*, not enforced configuration — "to block an action regardless of what Claude decides, use a PreToolUse hook." B is the classic precedence misconception: memory files *concatenate* (broad→specific), they don't override, and no CLAUDE.md scope enforces blocking. _Sub-topic: CLAUDE.md context-not-enforcement · Difficulty: easy_

**Q2 — B.** The four surfaces map by need: CLAUDE.md = every-session soft guidance (conventions); Hooks = hard, deterministic enforcement (a mandatory formatter Claude can't skip); Skills = on-demand multi-step procedures (release flow); Rules with `paths:` frontmatter = soft, topic/path-scoped guidance. The mnemonic is "automations = hooks, preferences = memory." Every other option swaps the hard-enforcement item (formatter) off of hooks. _Sub-topic: four extension surfaces · Difficulty: med_

**Q3 — C.** Rules evaluate deny → ask → allow, and "if a tool is denied at any level, no other level can allow it"; managed deny cannot be overridden by anything, including CLI. Critically, PreToolUse hook decisions "do not bypass permission rules" — deny is evaluated regardless of the hook. A and D both ignore deny's absolute precedence; D also misapplies the merge rule (merging never resurrects a denied call). _Sub-topic: permissions deny→ask→allow + hooks don't bypass · Difficulty: hard_

**Q4 — B.** This is the headline D3 trap: settings override by precedence, "Permission rules behave differently because they merge across scopes rather than override." So project and user `allow` rules combine rather than the project set replacing the user set. A states the misconception; C inverts the documented precedence; D invents an allow/deny distinction that doesn't exist for the merge behavior. _Sub-topic: settings-override-but-rules-merge · Difficulty: med_

**Q5 — C.** Grep searches text *inside* files (find code references); Glob matches filenames/paths only and therefore cannot locate an in-file call site. The logged anti-pattern is exactly "filename search to find in-file references." B violates the "Bash is a last resort when a structured tool exists" rule; D is inefficient and not the intended tool for searching. _Sub-topic: built-in tools Grep vs Glob · Difficulty: easy_

**Q6 — B.** Plan mode (`--permission-mode plan`) is workflow control: read-only exploration and a proposal step before any edits, suited to multi-file/architecture/breaking changes. Extended thinking is about reasoning quality. They are orthogonal and combine. A is the conflation the question targets; C and D are fabricated behaviors. _Sub-topic: plan mode ≠ extended thinking · Difficulty: med_

**Q7 — B.** For most hook events only exit code 2 blocks; exit code 1 is treated as a non-blocking error and Claude proceeds — even though 1 is the conventional Unix failure code. The fix is `exit 2` or returning `permissionDecision: "deny"`. A is false (PreToolUse can block; PostToolUse can't, since the tool already ran). C and D misstate the contract — PreToolUse runs before permission rules are evaluated. _Sub-topic: hooks exit-code semantics · Difficulty: med_

**Q8 — B.** `--fork-session` branches the transcript so each attempt gets an independent conversation history (use `--resume`/`-r` to target the prior session). Sessions are stored transcripts, not filesystem state, so file isolation needs git branches/worktrees. A is explicitly discouraged ("don't resume one session in two terminals"); C and D rest on the false premise that sessions snapshot the filesystem. _Sub-topic: sessions --fork/--resume; transcripts≠filesystem · Difficulty: hard_

**Q9 — C.** `--bare` skips auto-discovery of hooks/skills/plugins/MCP/auto-memory/CLAUDE.md for reproducible CI; `--output-format json` includes `total_cost_usd`; `claude setup-token` issues a one-year OAuth token consumed via `CLAUDE_CODE_OAUTH_TOKEN` for non-interactive auth. A skips reproducibility and cost; D's `stream-json` requires `--verbose`, `--fork-session` is irrelevant, and `/login` is interactive. _Sub-topic: headless / Agent SDK flags · Difficulty: hard_

**Q10 — B.** Reviewing with the same context that wrote the code is a named anti-pattern: that session carries the author's assumptions and bias, so it tends to ratify its own bugs. The fix is a fresh review context — a new session, a dedicated review subagent, or CI. A endorses the anti-pattern; C reduces it to token cost (compaction doesn't remove the bias); D invents a permission-mode requirement. _Sub-topic: fresh-review-context · Difficulty: easy_
