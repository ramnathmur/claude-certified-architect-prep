# Citations & Research Notes — Claude Code Configuration & Workflows (D2)

## Manifest

- **Date researched:** 2026-06-06 · **Re-verified 2026-06-09** (12/13 [VERIFY] items confirmed; 1 update: `PostToolBatch` is blockable via exit 2; `@agent-name` syntax resolved — see [VERIFY] #11). Full sweep: `QA-VERIFY-SWEEP_2026-06-09.md`.
- **CCA-F domains covered:** **Domain 2 — Claude Code Configuration & Workflows (20%)** is primary. Overlaps flagged where they occur: **Domain 1** (Claude/agent fundamentals — the agentic loop, context window) brushes Sections E/F/H; **Domain 4** (security/governance/enterprise) brushes Sections C/D/E/G (managed settings, permissions, hook security, MCP allowlists); **Domain 5** (extending/integration/automation) brushes Sections F/G/H (skills, plugins, MCP, Agent SDK, CI).
- **Critical version note up front (READ FIRST):**
  1. **The docs moved host.** `docs.claude.com/en/docs/claude-code/*` and `docs.anthropic.com/en/docs/claude-code/*` now **301/308-redirect to `code.claude.com/docs/en/*`**. The famous engineering blog post `anthropic.com/engineering/claude-code-best-practices` now **308-redirects into the docs** at `code.claude.com/docs/en/best-practices`. Old URLs still resolve via redirect but the canonical home is `code.claude.com/docs/en/`. Exam questions citing old URLs may be stale.
  2. **"Custom slash commands have been merged into skills."** A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy`. `.claude/commands/` still works, but **skills are the recommended primary mechanism** now (source: code.claude.com/docs/en/skills). This is a recent, exam-relevant consolidation.
  3. **The hook event list is much larger than the classic 8.** The live reference lists **~30 hook events** (see Section E). The "classic" set (PreToolUse, PostToolUse, UserPromptSubmit, Notification, Stop, SubagentStop, PreCompact, SessionStart, SessionEnd) is a stable subset; many newer events (PostToolUseFailure, PostToolBatch, PermissionRequest, PermissionDenied, ConfigChange, etc.) are volatile and likely to keep growing.
  4. **Permission-mode names** now include `auto` and `dontAsk` alongside the classic `default`/`acceptEdits`/`plan`/`bypassPermissions`. `auto` is a research preview.
  5. **Volatile model IDs / version-gated features** appear throughout the docs (e.g., `claude-opus-4-8`, `claude-sonnet-4-6`, "v2.1.x" minimum-version notes). Treat any specific version number or model ID as drift-prone.

---

### Sources consulted

1. **Claude Code Settings** — https://code.claude.com/docs/en/settings — Anthropic, PRIMARY — establishes settings file locations, settings precedence order, the full `settings.json` field catalog, env vars, and managed-settings deployment paths.
2. **Hooks reference** — https://code.claude.com/docs/en/hooks — Anthropic, PRIMARY — establishes the full hook-event list, matcher rules, input/output JSON contract, exit-code semantics, per-event blocking behavior, and hook security warnings.
3. **How Claude remembers your project (Memory / CLAUDE.md)** — https://code.claude.com/docs/en/memory — Anthropic, PRIMARY — establishes CLAUDE.md scopes and load order, `@`-imports (4-hop depth), `.claude/rules/`, auto memory, managed CLAUDE.md.
4. **Configure permissions** — https://code.claude.com/docs/en/permissions — Anthropic, PRIMARY — establishes allow/ask/deny semantics, deny→ask→allow evaluation, rule syntax (Bash/Read/Edit/WebFetch/MCP/Agent), permission modes, settings precedence for permissions, managed-only settings.
5. **Create custom subagents** — https://code.claude.com/docs/en/sub-agents — Anthropic, PRIMARY — establishes subagent file locations & priority, full frontmatter field list, built-in subagents (Explore/Plan/general-purpose), `--agents` JSON, plugin-subagent restrictions.
6. **Extend Claude with skills** — https://code.claude.com/docs/en/skills — Anthropic, PRIMARY — establishes SKILL.md structure, skill scopes/precedence, frontmatter reference, string substitutions ($ARGUMENTS / $N / $name), dynamic context injection, commands-merged-into-skills.
7. **Create plugins** — https://code.claude.com/docs/en/plugins — Anthropic, PRIMARY — establishes plugin directory layout, `plugin.json` manifest, what a plugin bundles, `--plugin-dir`, standalone-vs-plugin guidance.
8. **Create and distribute a plugin marketplace** — https://code.claude.com/docs/en/plugin-marketplaces — Anthropic, PRIMARY — establishes `.claude-plugin/marketplace.json` schema and `/plugin marketplace add` / `/plugin install` flow.
9. **Connect Claude Code to tools via MCP** — https://code.claude.com/docs/en/mcp — Anthropic, PRIMARY — establishes `claude mcp add` transports (http/sse/stdio/ws), installation scopes (local/project/user), `.mcp.json` structure, scope precedence, auth.
10. **Run Claude Code programmatically (Headless / Agent SDK via CLI)** — https://code.claude.com/docs/en/headless — Anthropic, PRIMARY — establishes `claude -p`, `--bare`, output formats, fan-out/CI patterns, structured output.
11. **CLI reference** — https://code.claude.com/docs/en/cli-reference — Anthropic, PRIMARY — establishes CLI commands and flags (`--permission-mode`, `--allowedTools`, `--settings`, `--setting-sources`, `--mcp-config`, `--agents`, etc.).
12. **Commands** — https://code.claude.com/docs/en/commands — Anthropic, PRIMARY — establishes the built-in slash command + bundled-skill catalog.
13. **Output styles** — https://code.claude.com/docs/en/output-styles — Anthropic, PRIMARY — establishes output-style files, locations, `outputStyle` setting, built-in styles.
14. **Authentication** — https://code.claude.com/docs/en/authentication — Anthropic, PRIMARY — establishes auth methods, credential storage, authentication precedence, `claude setup-token` / `CLAUDE_CODE_OAUTH_TOKEN` for CI.
15. **Best practices for Claude Code** — https://code.claude.com/docs/en/best-practices (redirect target of anthropic.com/engineering/claude-code-best-practices) — Anthropic, PRIMARY-adjacent — establishes explore→plan→code→commit, verification loops, context management (`/clear`, `/compact`), fan-out automation.

---

## Section A — The configuration model & the `.claude/` directory (what lives where; project vs user vs enterprise scope)

**Lesson framing (not a verbatim Anthropic quote):** Claude Code's configuration is organized along two axes — *scope* (managed/enterprise → user → project → local) and *feature* (settings, memory, subagents, skills/commands, hooks, MCP, plugins, output styles). The `.claude/` directory is the per-scope home; managed/enterprise config lives in OS-level policy locations.

The four scopes and where they live (verbatim table, source: https://code.claude.com/docs/en/settings):

| Scope | Location | Who it affects | Shared with team? |
|-------|----------|----------------|-------------------|
| **Managed** | Server-managed settings, plist / registry, or system-level `managed-settings.json` | All users on the machine | Yes (deployed by IT) |
| **User** | `~/.claude/` directory | You, across all projects | No |
| **Project** | `.claude/` in repository | All collaborators on this repository | Yes (committed to git) |
| **Local** | `.claude/settings.local.json` | You, in this repository only | No (gitignored) |

File locations by feature (verbatim, source: https://code.claude.com/docs/en/settings):

| Feature | User location | Project location | Local location |
|---------|---------------|------------------|----------------|
| **Settings** | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| **Subagents** | `~/.claude/agents/` | `.claude/agents/` | None |
| **MCP servers** | `~/.claude.json` | `.mcp.json` | `~/.claude.json` (per-project) |
| **Plugins** | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| **CLAUDE.md** | `~/.claude/CLAUDE.md` | `CLAUDE.md` or `.claude/CLAUDE.md` | `CLAUDE.local.md` |

> "**Windows note:** Paths shown as `~/.claude` resolve to `%USERPROFILE%\.claude`" (source: https://code.claude.com/docs/en/settings)

**Skills** live at `.claude/skills/<skill-name>/SKILL.md` (project) and `~/.claude/skills/<skill-name>/SKILL.md` (personal) (source: https://code.claude.com/docs/en/skills). **Output styles** live at `~/.claude/output-styles` and `.claude/output-styles` (source: https://code.claude.com/docs/en/output-styles).

**Architect note (lesson framing):** `--add-dir` grants *file access* but NOT full config discovery. Per the docs: "Adding a directory extends where Claude can read and edit files. It does not make that directory a full configuration root" — only Skills (with live reload), `enabledPlugins`/`extraKnownMarketplaces`, and (conditionally) CLAUDE.md load from `--add-dir` directories; subagents/commands/output-styles/hooks do not (source: https://code.claude.com/docs/en/permissions).

---

## Section B — Memory: CLAUDE.md types & precedence, imports/@-mentions, how memory is loaded

CLAUDE.md scope/location table, **listed in load order, broadest → most specific** (verbatim, source: https://code.claude.com/docs/en/memory):

| Scope | Location | Shared with |
| --- | --- | --- |
| **Managed policy** | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`; Linux & WSL: `/etc/claude-code/CLAUDE.md`; Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | All users in organization |
| **User instructions** | `~/.claude/CLAUDE.md` | Just you (all projects) |
| **Project instructions** | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team members via source control |
| **Local instructions** | `./CLAUDE.local.md` (add to `.gitignore`) | Just you (current project) |

> "The table below lists them in load order, from broadest scope to most specific, so a project instruction appears in context after a user instruction." (source: https://code.claude.com/docs/en/memory)

**How loading actually works (verbatim):**
> "Claude Code reads CLAUDE.md files by walking up the directory tree from your current working directory... All discovered files are concatenated into context rather than overriding each other. Across the directory tree, content is ordered from the filesystem root down to your working directory... Within each directory, `CLAUDE.local.md` is appended after `CLAUDE.md`, so your personal notes are the last thing Claude reads at that level." (source: https://code.claude.com/docs/en/memory)

> "Claude also discovers `CLAUDE.md` and `CLAUDE.local.md` files in subdirectories under your current working directory. Instead of loading them at launch, they are included when Claude reads files in those subdirectories." (source: https://code.claude.com/docs/en/memory)

**Architect nuance (lesson framing):** memory "precedence" here is **concatenation/ordering**, NOT override. CLAUDE.md is *context*, not enforced config: "Both are loaded at the start of every conversation. Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a [PreToolUse hook] instead." (source: https://code.claude.com/docs/en/memory). Managed policy CLAUDE.md **cannot be excluded** by individual settings.

**Imports / `@`-mentions (verbatim):**
> "CLAUDE.md files can import additional files using `@path/to/import` syntax. Imported files are expanded and loaded into context at launch... Both relative and absolute paths are allowed. Relative paths resolve relative to the file containing the import... Imported files can recursively import other files, with a maximum depth of four hops." (source: https://code.claude.com/docs/en/memory)

Example import line (verbatim):
```text
See @README for project overview and @package.json for available npm commands for this project.

# Additional Instructions
- git workflow @docs/git-instructions.md
```

**Size guidance (verbatim):** "target under 200 lines per CLAUDE.md file." and "Bloated CLAUDE.md files cause Claude to ignore your actual instructions!" (sources: https://code.claude.com/docs/en/memory ; https://code.claude.com/docs/en/best-practices)

**`.claude/rules/` (path-scoped rules):**
> "Rules without [`paths` frontmatter] are loaded at launch with the same priority as `.claude/CLAUDE.md`." Path-scoped rules use YAML frontmatter with a `paths` glob list and "only apply when Claude is working with files matching the specified patterns." User-level rules in `~/.claude/rules/` "are loaded before project rules, giving project rules higher priority." (source: https://code.claude.com/docs/en/memory)

**AGENTS.md:** "Claude Code reads `CLAUDE.md`, not `AGENTS.md`." Bridge with `@AGENTS.md` import or a symlink (source: https://code.claude.com/docs/en/memory).

**Managed CLAUDE.md via settings:** the `claudeMd` key embeds managed CLAUDE.md content directly in `managed-settings.json`; "honored: managed and policy settings only" (source: https://code.claude.com/docs/en/memory):
```json
{
  "claudeMd": "Always run `make lint` before committing.\nNever push directly to main."
}
```

**Auto memory (distinct from CLAUDE.md):** machine-local notes Claude writes itself, stored per-repo at `~/.claude/projects/<project>/memory/` with a `MEMORY.md` index; "The first 200 lines of `MEMORY.md`, or the first 25KB, whichever comes first, are loaded at the start of every conversation." On by default (`autoMemoryEnabled`, default `true`); requires v2.1.59+ (source: https://code.claude.com/docs/en/memory).

---

## Section C — `settings.json`: the settings hierarchy & precedence, key fields, env vars

**Settings precedence order (verbatim, source: https://code.claude.com/docs/en/settings):**
> 1. **Managed** (highest) — can't be overridden by anything
> 2. **Command line arguments** — temporary session overrides
> 3. **Local** — overrides project and user settings
> 4. **Project** — overrides user settings
> 5. **User** (lowest) — applies when nothing else specifies the setting

> "Permission rules behave differently because they merge across scopes rather than override." (source: https://code.claude.com/docs/en/settings) — **this is an exam trap: settings *override* by precedence, but permission rules *merge*.**

**Key `settings.json` fields (verbatim selections, source: https://code.claude.com/docs/en/settings):**
- `model` — "Override the default model to use for Claude Code"
- `env` — "Environment variables applied to every session and to subprocesses Claude Code spawns"
- `permissions` — "Allow/deny/ask rules for tool execution" (`allow`, `deny`, `ask` arrays; also `defaultMode`, `additionalDirectories`, `disableBypassPermissionsMode`)
- `hooks` — "Configure custom commands to run at lifecycle events"
- `apiKeyHelper` — "Custom script to generate an auth value"
- `statusLine` — "Configure a custom status line to display context"
- `outputStyle` — "Configure an output style to adjust the system prompt"
- `autoMemoryEnabled` (default `true`), `autoMemoryDirectory`, `claudeMd` (managed only), `claudeMdExcludes`
- `cleanupPeriodDays` (default 30), `includeCoAuthoredBy` (**Deprecated** — "Use `attribution` instead"), `attribution`
- `enableAllProjectMcpServers`, `enabledMcpjsonServers`, `disabledMcpjsonServers`

**Managed-only / governance fields (verbatim selections, sources: https://code.claude.com/docs/en/settings ; https://code.claude.com/docs/en/permissions):**
- `allowManagedHooksOnly` — "only managed hooks, SDK hooks, and force-enabled plugin hooks are loaded"
- `allowManagedPermissionRulesOnly` — "prevents user and project settings from defining `allow`, `ask`, or `deny` permission rules"
- `allowManagedMcpServersOnly`, `allowedMcpServers`, `deniedMcpServers`
- `strictKnownMarketplaces`, `blockedMarketplaces`, `strictPluginOnlyCustomization` ("`true` locks all four surfaces; an array such as `["skills", "hooks"]` locks only the named ones")
- `forceLoginMethod`, `forceLoginOrgUUID`, `requiredMinimumVersion`, `requiredMaximumVersion`, `forceRemoteSettingsRefresh`

**Example `settings.json` (verbatim, source: https://code.claude.com/docs/en/settings):**
```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  }
}
```

**Reload behavior (verbatim):**
> "Claude Code watches your settings files and reloads them when they change, so edits to most keys apply to the running session without a restart." Live-reload keys include `permissions`, `hooks`, `apiKeyHelper`. **Read once at session start (apply on next restart):** `model` (use `/model` to switch mid-session) and `outputStyle` ("rebuilt on `/clear` or restart"). (source: https://code.claude.com/docs/en/settings)

**Managed settings deployment locations (verbatim, source: https://code.claude.com/docs/en/settings):**
- macOS: `/Library/Application Support/ClaudeCode/managed-settings.json` (+ `managed-settings.d/`), or `com.anthropic.claudecode` plist
- Linux & WSL: `/etc/claude-code/managed-settings.json` (+ `managed-settings.d/`)
- Windows: registry `HKLM\SOFTWARE\Policies\ClaudeCode` (admin) / `HKCU\SOFTWARE\Policies\ClaudeCode` (user, lowest); file `C:\Program Files\ClaudeCode\managed-settings.json` (+ `managed-settings.d\`). "Legacy path (no longer supported as of v2.1.75): `C:\ProgramData\ClaudeCode\managed-settings.json`"

**Selected env vars set via the `env` field (verbatim names, source: https://code.claude.com/docs/en/settings):** `CLAUDE_CODE_ENABLE_TELEMETRY`, `OTEL_METRICS_EXPORTER`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY`, `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`, `ANTHROPIC_MODEL`, `DISABLE_AUTOUPDATER`, `CLAUDE_CODE_USE_POWERSHELL_TOOL`, `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD`. `/status` shows active "Setting sources" for the current session.

---

## Section D — Permissions: allow/ask/deny rules, tool-pattern syntax, permission modes, enterprise managed policy

**Three rule types (verbatim, source: https://code.claude.com/docs/en/permissions):**
> "**Allow** rules let Claude Code use the specified tool without manual approval. **Ask** rules prompt for confirmation... **Deny** rules prevent Claude Code from using the specified tool."

**Evaluation order (verbatim — exam-critical):**
> "Rules are evaluated in order: **deny -> ask -> allow**. The first matching rule wins, so deny rules always take precedence."

> "If a tool is denied at any level, no other level can allow it." (source: https://code.claude.com/docs/en/permissions)

**Bare tool name vs scoped pattern (verbatim):**
> "A bare tool name like `Bash` removes the tool from Claude's context entirely, so Claude never sees it. A scoped rule like `Bash(rm *)` leaves the tool available and blocks matching calls when Claude attempts them."

**Permission modes (verbatim table, source: https://code.claude.com/docs/en/permissions). Set via `defaultMode` in settings or `--permission-mode` flag:**

| Mode | Description |
| --- | --- |
| `default` | "Standard behavior: prompts for permission on first use of each tool" |
| `acceptEdits` | "Automatically accepts file edits and common filesystem commands (`mkdir`, `touch`, `mv`, `cp`, etc.) for paths in the working directory or `additionalDirectories`" |
| `plan` | "Plan Mode: Claude reads files and runs read-only shell commands to explore but does not edit your source files" |
| `auto` | "Auto-approves tool calls with background safety checks... Currently a research preview" |
| `dontAsk` | "Auto-denies tools unless pre-approved via `/permissions` or `permissions.allow` rules" |
| `bypassPermissions` | "Skips all permission prompts. Root and home directory removals such as `rm -rf /` still prompt as a circuit breaker" |

> "Administrators can prevent this mode by setting `permissions.disableBypassPermissionsMode` to `"disable"` in [managed settings]." Also `permissions.disableAutoMode`. (source: https://code.claude.com/docs/en/permissions)

**Rule syntax — `Tool` or `Tool(specifier)` (verbatim examples, source: https://code.claude.com/docs/en/permissions):**
- `Bash` / `Bash(*)` → all Bash commands (as a deny rule, removes the tool entirely)
- `Bash(npm run build)` → exact command; `Bash(npm run test *)` → prefix (space before `*` enforces a word boundary; `Bash(ls *)` matches `ls -la` but not `lsof`; `Bash(ls*)` matches both). `:*` suffix ≡ trailing ` *` (only recognized at end of pattern).
- `Read(./.env)`, `Edit(/src/**/*.ts)` — gitignore-style patterns with four anchors: `//path` (absolute), `~/path` (home), `/path` (relative to project root), `path`/`./path` (relative to cwd). **Trap:** "A pattern like `/Users/alice/file` is NOT an absolute path. It's relative to the project root. Use `//Users/alice/file` for absolute paths."
- `WebFetch(domain:example.com)`
- MCP: `mcp__puppeteer` (whole server), `mcp__puppeteer__*` (wildcard), `mcp__puppeteer__puppeteer_navigate` (single tool)
- `Agent(Explore)`, `Agent(my-custom-agent)` — control which subagents Claude may use

> "Claude Code is aware of shell operators, so a rule like `Bash(safe-cmd *)` won't give it permission to run the command `safe-cmd && other-cmd`. The recognized command separators are `&&`, `||`, `;`, `|`, `|&`, `&`, and newlines." (source: https://code.claude.com/docs/en/permissions)

**Warning (verbatim):** "Bash permission patterns that try to constrain command arguments are fragile." — for reliable URL filtering, deny `curl`/`wget` and use `WebFetch(domain:...)`, or use a PreToolUse hook (source: https://code.claude.com/docs/en/permissions).

**Permission precedence (verbatim, source: https://code.claude.com/docs/en/permissions):**
> 1. **Managed settings** — cannot be overridden by any other level, including command line arguments
> 2. **Command line arguments**
> 3. **Local project settings** (`.claude/settings.local.json`)
> 4. **Shared project settings** (`.claude/settings.json`)
> 5. **User settings** (`~/.claude/settings.json`)

> "a managed settings deny cannot be overridden by `--allowedTools`, and `--disallowedTools` can add restrictions beyond what managed settings define." (source: https://code.claude.com/docs/en/permissions)

**Hooks extend permissions (verbatim):** PreToolUse hooks run *before* the permission prompt. "Hook decisions do not bypass permission rules. Deny and ask rules are evaluated regardless of what a PreToolUse hook returns... A hook that exits with code 2 stops the tool call before permission rules are evaluated." (source: https://code.claude.com/docs/en/permissions)

**Architect note (lesson framing):** Permissions are client-enforced, not model-enforced — "Permission rules are enforced by Claude Code, not by the model." For OS-level enforcement use **sandboxing** (`sandbox.enabled`), which complements permissions (permissions cover all tools; sandbox covers Bash + child processes).

---

## Section E — Hooks: events, matchers, input/output JSON contract, exit-code semantics, security

**What hooks are (verbatim):** "Claude Code hooks are user-defined shell commands that execute at various points in Claude Code's lifecycle and provide deterministic control over Claude Code's behavior." (source: https://code.claude.com/docs/en/hooks). Configured under the `hooks` key in `settings.json` (or `hooks/hooks.json` in a plugin). Browse with `/hooks`.

**Full hook-event list (verbatim, source: https://code.claude.com/docs/en/hooks):**
`SessionStart`, `Setup`, `UserPromptSubmit`, `UserPromptExpansion`, `PreToolUse`, `PermissionRequest`, `PermissionDenied`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Notification`, `MessageDisplay`, `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`, `Stop`, `StopFailure`, `TeammateIdle`, `InstructionsLoaded`, `ConfigChange`, `CwdChanged`, `FileChanged`, `WorktreeCreate`, `WorktreeRemove`, `PreCompact`, `PostCompact`, `Elicitation`, `ElicitationResult`, `SessionEnd`.

**Matchers (verbatim rules, source: https://code.claude.com/docs/en/hooks):**

| Matcher Value | Evaluated As |
| --- | --- |
| `"*"`, `""`, or omitted | Match all |
| Only letters, digits, `_`, `\|` | Exact string or `\|`-separated list (e.g. `Bash`, `Edit\|Write`) |
| Any other character | JavaScript regular expression (e.g. `^Notebook`, `mcp__memory__.*`) |

Tool-name matching applies to `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied`. `SessionStart` matches `startup`/`resume`/`clear`/`compact`. `PreCompact`/`PostCompact` match `manual`/`auto`. `ConfigChange` matches `user_settings`/`project_settings`/`local_settings`/`policy_settings`/`skills`. Events with **no matcher support** (always fire): `UserPromptSubmit`, `PostToolBatch`, `Stop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove`, `MessageDisplay`, `CwdChanged`.

**Common input fields on stdin (verbatim, source: https://code.claude.com/docs/en/hooks):**
```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default|plan|acceptEdits|auto|dontAsk|bypassPermissions",
  "hook_event_name": "EventName"
}
```

**Exit-code semantics (verbatim, source: https://code.claude.com/docs/en/hooks):**

| Exit Code | Behavior | JSON Processing |
| --- | --- | --- |
| **0** | Success | Parses stdout for JSON output |
| **2** | Blocking error | Ignores stdout/JSON; feeds stderr to Claude as error |
| **Other** (1, 3, ...) | Non-blocking error | stderr shown in transcript; execution continues |

**Exam-critical security warning (verbatim):**
> "For most hook events, only exit code 2 blocks the action. Claude Code treats exit code 1 as a non-blocking error and proceeds with the action, even though 1 is the conventional Unix failure code. If your hook is meant to enforce a policy, use `exit 2`." (source: https://code.claude.com/docs/en/hooks)

**Which events can block via exit 2 (verbatim selections, source: https://code.claude.com/docs/en/hooks):** `PreToolUse` (blocks the tool call), `PermissionRequest` (denies), `UserPromptSubmit` (blocks + erases the prompt), `Stop`/`SubagentStop` (prevents stopping), `PreCompact` (blocks compaction), `ConfigChange` (blocks the change except `policy_settings`), `WorktreeCreate` (any non-zero fails), `PostToolBatch` (stops the agentic loop before the next model call) `[VERIFY 2026-06-09: confirmed blockable on live Hooks doc]`. **Cannot block:** `PostToolUse`/`PostToolUseFailure` ("tool already ran"), `StopFailure`, `Notification`, `SessionStart`, `SessionEnd`, etc.

**JSON output schema — universal fields (verbatim, source: https://code.claude.com/docs/en/hooks):**
```json
{
  "continue": true,
  "stopReason": "Message when continue is false",
  "suppressOutput": false,
  "systemMessage": "Warning message shown to user"
}
```

**PreToolUse decision control (verbatim, source: https://code.claude.com/docs/en/hooks):**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask|defer",
    "permissionDecisionReason": "Reason for decision"
  }
}
```

**SessionStart can inject context (verbatim):** `hookSpecificOutput.additionalContext` adds context to Claude's window; "Output strings ... are capped at 10,000 characters."

**Hook config + matcher example (verbatim, source: https://code.claude.com/docs/en/hooks):**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(rm *)",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh",
            "args": []
          }
        ]
      }
    ]
  }
}
```

**Security notes (verbatim, source: https://code.claude.com/docs/en/hooks):**
- "On macOS and Linux, command hooks run in their own session without a controlling terminal as of v2.1.139... To surface a message to the user on any platform, return `systemMessage` in JSON output."
- Bash `if`-matching "fails open (runs hook regardless) when Bash command cannot be parsed. Use the [permission system] rather than a hook to enforce hard allow/deny."
- Prompt-injection guidance for `additionalContext`: "Write the text as factual statements rather than imperative system instructions."
- Managed governance: `allowManagedHooksOnly`, `allowedHttpHookUrls`, `httpHookAllowedEnvVars`, `disableAllHooks` (source: https://code.claude.com/docs/en/settings).

**Hooks in subagents (verbatim example, source: https://code.claude.com/docs/en/sub-agents):**
```yaml
---
name: db-reader
description: Execute read-only database queries
tools: Bash
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
---
```

---

## Section F — Extending Claude Code: slash commands, subagents, skills, plugins & marketplaces

### F.1 Custom slash commands / skills (merged)

**Verbatim (source: https://code.claude.com/docs/en/skills):**
> "**Custom commands have been merged into skills.** A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way. Your existing `.claude/commands/` files keep working."

**Skill scopes/precedence (verbatim table, source: https://code.claude.com/docs/en/skills):**

| Location | Path | Applies to |
| --- | --- | --- |
| Enterprise | See managed settings | All users in your organization |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<skill-name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Where plugin is enabled |

> "When skills share the same name across levels, enterprise overrides personal, and personal overrides project... if a skill and a command share the same name, the skill takes precedence." (source: https://code.claude.com/docs/en/skills)

**Skill command name source (verbatim):** directory name under `.claude/skills/` (e.g. `deploy-staging/SKILL.md` → `/deploy-staging`); file name under `.claude/commands/` (`deploy.md` → `/deploy`); plugin skill namespaced `plugin-name:skill-name`.

**Skill frontmatter reference (verbatim selections, source: https://code.claude.com/docs/en/skills):**
- `name` — display name (defaults to directory name)
- `description` (recommended) — "What the skill does and when to use it... truncated at 1,536 characters in the skill listing"
- `when_to_use`, `argument-hint`, `arguments`
- `disable-model-invocation: true` — "prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`."
- `user-invocable: false` — "hide from the `/` menu. Use for background knowledge"
- `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context: fork`, `hooks`, `paths`, `shell`

**String substitutions (verbatim, source: https://code.claude.com/docs/en/skills):** `$ARGUMENTS` (all args; "If `$ARGUMENTS` is not present in the content, arguments are appended as `ARGUMENTS: <value>`"), `$ARGUMENTS[N]`, `$N` (shorthand, 0-based: `$0` first arg), `$name` (declared in `arguments` frontmatter), `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}`.

**Dynamic context injection (verbatim):** ``!`git diff HEAD` `` runs the command and "replaces the line with its output before Claude sees the skill content." (source: https://code.claude.com/docs/en/skills)

**Example skill with manual invocation (verbatim, source: https://code.claude.com/docs/en/best-practices):**
```markdown
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
...
```

### F.2 Subagents (`.claude/agents/`)

**What they are (verbatim):** "Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions. When Claude encounters a task that matches a subagent's description, it delegates to that subagent..." (source: https://code.claude.com/docs/en/sub-agents)

**Built-in subagents (verbatim):** **Explore** (Haiku, read-only, codebase search; "skips your CLAUDE.md files"), **Plan** (inherits model, read-only, used in plan mode), **general-purpose** (inherits model, all tools). Also helper agents `statusline-setup` (Sonnet) and `claude-code-guide` (Haiku). "subagents cannot spawn other subagents." (source: https://code.claude.com/docs/en/sub-agents)

**Subagent scope/priority (verbatim table, source: https://code.claude.com/docs/en/sub-agents):**

| Location | Scope | Priority |
| --- | --- | --- |
| Managed settings | Organization-wide | 1 (highest) |
| `--agents` CLI flag | Current session | 2 |
| `.claude/agents/` | Current project | 3 |
| `~/.claude/agents/` | All your projects | 4 |
| Plugin's `agents/` directory | Where plugin is enabled | 5 (lowest) |

**Subagent file format (verbatim, source: https://code.claude.com/docs/en/sub-agents):**
```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```

**Frontmatter fields (verbatim, source: https://code.claude.com/docs/en/sub-agents).** Required: `name`, `description`. Optional: `tools` (inherits all if omitted), `disallowedTools`, `model` (`sonnet`/`opus`/`haiku`/full ID/`inherit`; default `inherit`), `permissionMode` (`default`/`acceptEdits`/`auto`/`dontAsk`/`bypassPermissions`/`plan`), `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory` (`user`/`project`/`local`), `background`, `effort`, `isolation` (`worktree`), `color`, `initialPrompt`.

> "**For security reasons, plugin subagents do not support the `hooks`, `mcpServers`, or `permissionMode` frontmatter fields.** These fields are ignored when loading agents from a plugin." (source: https://code.claude.com/docs/en/sub-agents)

> "Subagents are loaded at session start. If you add or edit a subagent file directly on disk, restart your session to load it. Subagents created through the `/agents` interface take effect immediately without a restart." (source: https://code.claude.com/docs/en/sub-agents)

**Note (lesson framing):** the Task tool was renamed to Agent in v2.1.63; `Task(...)` still works as an alias.

### F.3 Plugins

**What a plugin bundles (verbatim directory table, source: https://code.claude.com/docs/en/plugins):**

| Directory | Location | Purpose |
| --- | --- | --- |
| `.claude-plugin/` | Plugin root | Contains `plugin.json` manifest |
| `skills/` | Plugin root | Skills as `<name>/SKILL.md` directories |
| `commands/` | Plugin root | Skills as flat Markdown files (use `skills/` for new plugins) |
| `agents/` | Plugin root | Custom agent definitions |
| `hooks/` | Plugin root | Event handlers in `hooks.json` |
| `.mcp.json` | Plugin root | MCP server configurations |
| `.lsp.json` | Plugin root | LSP server configurations |
| `monitors/` | Plugin root | Background monitor configs in `monitors.json` |
| `bin/` | Plugin root | Executables added to Bash `PATH` while enabled |
| `settings.json` | Plugin root | Default settings applied when enabled (only `agent` and `subagentStatusLine` keys supported) |

> "**Common mistake**: Don't put `commands/`, `agents/`, `skills/`, or `hooks/` inside the `.claude-plugin/` directory. Only `plugin.json` goes inside `.claude-plugin/`." (source: https://code.claude.com/docs/en/plugins)

**`plugin.json` manifest (verbatim, source: https://code.claude.com/docs/en/plugins):**
```json
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```
> "`name` — Unique identifier and skill namespace. Skills are prefixed with this (e.g., `/my-first-plugin:hello`)." `version` optional; "If omitted and your plugin is distributed via git, the commit SHA is used and every commit counts as a new version."

**Testing/dev:** `claude --plugin-dir ./my-plugin` (also accepts a `.zip` as of v2.1.128), `claude --plugin-url <url>`, `/reload-plugins`. `claude plugin init my-tool` scaffolds a skills-dir plugin that loads as `my-tool@skills-dir`. (source: https://code.claude.com/docs/en/plugins)

### F.4 Marketplaces

**`marketplace.json` (verbatim, lives at `.claude-plugin/marketplace.json` in repo root, source: https://code.claude.com/docs/en/plugin-marketplaces):**
```json
{
  "name": "my-plugins",
  "owner": { "name": "Your Name" },
  "plugins": [
    {
      "name": "quality-review-plugin",
      "source": "./plugins/quality-review-plugin",
      "description": "Adds a quality-review skill for quick code reviews"
    }
  ]
}
```
Install flow (verbatim): `/plugin marketplace add ./my-marketplace` then `/plugin install quality-review-plugin@my-plugins`; refresh with `/plugin marketplace update`. Anthropic maintains `claude-plugins-official` (auto-available) and `claude-community` (add with `/plugin marketplace add anthropics/claude-plugins-community`). (sources: https://code.claude.com/docs/en/plugin-marketplaces ; https://code.claude.com/docs/en/plugins)

**When to use which (lesson framing, grounded in docs):** standalone `.claude/` for personal/project/quick experiments (short names like `/deploy`); plugins for sharing/versioning/reuse across projects (namespaced names like `/my-plugin:deploy`). Skill = on-demand procedural/reference knowledge; Subagent = isolated context + tool restriction; Hook = deterministic guaranteed action; MCP = external tool/data integration (source: https://code.claude.com/docs/en/best-practices, "Configure your environment").

### F.5 Output styles

> "Output styles change how Claude responds, not what Claude knows. They modify the system prompt..." Built-in: **Default**, **Proactive**, **Explanatory**, **Learning**. Files live at `~/.claude/output-styles` (user) or `.claude/output-styles` (project); select via `/config` or set the `outputStyle` field. Custom-style frontmatter: `name`, `description`, `keep-coding-instructions`, `force-for-plugin`. "Changes take effect after `/clear` or a new session." (source: https://code.claude.com/docs/en/output-styles)

---

## Section G — MCP in Claude Code: scopes, transports, `.mcp.json`, auth

**Transports (verbatim commands, source: https://code.claude.com/docs/en/mcp):**
- HTTP (recommended for remote): `claude mcp add --transport http <name> <url>` (e.g. `claude mcp add --transport http notion https://mcp.notion.com/mcp`). In JSON, `type` accepts `streamable-http` as an alias for `http`.
- SSE (**deprecated**): `claude mcp add --transport sse <name> <url>`
- stdio (local): `claude mcp add [options] <name> -- <command> [args...]` — "the `--` (double dash) separates Claude's own options... from the command and arguments that run the server."
- WebSocket: `type: "ws"` via `.mcp.json` or `claude mcp add-json` (not supported by `--transport`).

**Installation scopes (verbatim table, source: https://code.claude.com/docs/en/mcp):**

| Scope | Loads in | Shared with team | Stored in |
| --- | --- | --- | --- |
| Local | Current project only | No | `~/.claude.json` |
| Project | Current project only | Yes, via version control | `.mcp.json` in project root |
| User | All your projects | No | `~/.claude.json` |

> "`local` (default): Available only to you in the current project (was called `project` in older versions)" and "`user`: Available to you across all projects (was called `global` in older versions)" — **naming changed; an exam trap.** (source: https://code.claude.com/docs/en/mcp)

**Project `.mcp.json` (verbatim, designed to be checked into version control, source: https://code.claude.com/docs/en/mcp):**
```json
{
  "mcpServers": {
    "shared-server": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```
> "For security reasons, Claude Code prompts for approval before using project-scoped servers from `.mcp.json` files." Reset with `claude mcp reset-project-choices`.

**Scope precedence (verbatim, source: https://code.claude.com/docs/en/mcp):**
> 1. Local scope  2. Project scope  3. User scope  4. Plugin-provided servers  5. claude.ai connectors
> "The entire server entry from that source is used; fields are not merged across scopes."

**Management commands (verbatim):** `claude mcp list`, `claude mcp get <name>`, `claude mcp remove <name>`, and in-session `/mcp` (also handles OAuth 2.0 auth for remote servers).

**Governance (lesson framing, grounded in docs):** managed-only keys `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`, plus `enableAllProjectMcpServers`/`enabledMcpjsonServers`/`disabledMcpjsonServers`. CLI: `--mcp-config <file>` and `--strict-mcp-config` ("Only use MCP servers from `--mcp-config`"). (sources: https://code.claude.com/docs/en/settings ; https://code.claude.com/docs/en/cli-reference)

---

## Section H — Workflows & automation: headless mode, the Agent SDK, CI, best-practice workflows

**Headless / non-interactive (verbatim, source: https://code.claude.com/docs/en/headless):**
> "To run Claude Code in non-interactive mode, pass `-p` with your prompt..."
```bash
claude -p "Find and fix the bug in auth.py" --allowedTools "Read,Edit,Bash"
```

**The Agent SDK relationship (verbatim):** "The [Agent SDK] gives you the same tools, agent loop, and context management that power Claude Code. It's available as a CLI for scripts and CI/CD, or as Python and TypeScript packages..." `claude -p` IS the SDK-via-CLI surface. (source: https://code.claude.com/docs/en/headless)

**Bare mode (verbatim):** `--bare` "skip[s] auto-discovery of hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md" for reproducible CI; "will become the default for `-p` in a future release." Bare mode requires `ANTHROPIC_API_KEY` or `apiKeyHelper` (skips OAuth/keychain). (source: https://code.claude.com/docs/en/headless)

**Output formats (verbatim):** `--output-format text|json|stream-json`; `--json-schema` for structured output (result lands in `structured_output`); `stream-json` needs `--verbose` (and `--include-partial-messages` for token streaming). `--output-format json` includes `total_cost_usd`. (source: https://code.claude.com/docs/en/headless)

**CI authentication (verbatim, source: https://code.claude.com/docs/en/authentication):** `claude setup-token` generates a one-year OAuth token → set `CLAUDE_CODE_OAUTH_TOKEN`. Authentication precedence: (1) cloud-provider creds (`CLAUDE_CODE_USE_BEDROCK/VERTEX/FOUNDRY`), (2) `ANTHROPIC_AUTH_TOKEN`, (3) `ANTHROPIC_API_KEY`, (4) `apiKeyHelper`, (5) `CLAUDE_CODE_OAUTH_TOKEN`, (6) subscription OAuth from `/login`. **Volatile note:** "Starting June 15, 2026, Agent SDK and `claude -p` usage on subscription plans will draw from a new monthly Agent SDK credit."

**Key CLI flags for automation (verbatim, source: https://code.claude.com/docs/en/cli-reference):** `--print`/`-p`, `--permission-mode` (`default`/`acceptEdits`/`plan`/`auto`/`dontAsk`/`bypassPermissions`), `--allowedTools`, `--disallowedTools`, `--max-turns` (print mode only), `--max-budget-usd` (print mode only), `--settings <file-or-json>`, `--setting-sources` (`user,project,local`), `--mcp-config`, `--strict-mcp-config`, `--agents <json>`, `--append-system-prompt(-file)`, `--system-prompt(-file)` (full replace), `--continue`/`-c`, `--resume`/`-r`, `--fallback-model`, `--dangerously-skip-permissions` (≡ `--permission-mode bypassPermissions`).

**Fan-out pattern (verbatim, source: https://code.claude.com/docs/en/best-practices):**
```bash
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

**The canonical interactive workflow — explore → plan → code → commit (verbatim 4 phases, source: https://code.claude.com/docs/en/best-practices):**
1. **Explore** — "Enter plan mode. Claude reads files and answers questions without making changes."
2. **Plan** — "Ask Claude to create a detailed implementation plan." (`Ctrl+G` to edit the plan)
3. **Implement** — "Switch out of plan mode and let Claude code, verifying against its plan."
4. **Commit** — "Ask Claude to commit with a descriptive message and create a PR."
> "Letting Claude jump straight to coding can produce code that solves the wrong problem."

**Verification / TDD-flavored loop (verbatim guidance):** "Give Claude a check it can run: tests, a build, a screenshot to compare." Gate options: in-prompt, `/goal` condition, **Stop hook** ("blocks the turn from ending until it passes. Claude Code overrides the hook and ends the turn after 8 consecutive blocks"), or an adversarial review subagent / `/code-review`. (source: https://code.claude.com/docs/en/best-practices)

**Context management (verbatim):** "Use `/clear` frequently between tasks"; "`/compact <instructions>`"; "After two failed corrections, `/clear` and write a better initial prompt." (source: https://code.claude.com/docs/en/best-practices)

**Built-in commands an architect should know (verbatim selections, source: https://code.claude.com/docs/en/commands):** `/init`, `/memory`, `/permissions` (alias `/allowed-tools`), `/mcp`, `/agents`, `/hooks`, `/skills`, `/plugin`, `/config` (alias `/settings`), `/status`, `/model`, `/context`, `/compact`, `/clear`, `/plan`, `/doctor`, `/code-review`, `/security-review`. Bundled **skills** (prompt-based, not fixed logic) are marked **Skill** in the catalog (e.g. `/code-review`, `/batch`, `/debug`, `/loop`, `/claude-api`). MCP-exposed prompts appear as `/mcp__<server>__<prompt>`.

---

## [VERIFY] list — version-sensitive / volatile / uncertain facts

1. **Docs host migration (HIGH drift):** canonical docs are now `code.claude.com/docs/en/*`; `docs.claude.com` / `docs.anthropic.com` Claude Code paths and `anthropic.com/engineering/claude-code-best-practices` redirect there. *Stable: the content. Volatile: the URLs — verify before citing in the lesson.*
2. **Hook-event roster (HIGH drift):** the full list is ~30 events. The classic subset (PreToolUse, PostToolUse, UserPromptSubmit, Notification, Stop, SubagentStop, PreCompact, SessionStart, SessionEnd) is **stable**; newer events (PostToolUseFailure, PostToolBatch, PermissionRequest, PermissionDenied, ConfigChange, Setup, UserPromptExpansion, InstructionsLoaded, CwdChanged, FileChanged, WorktreeCreate/Remove, Elicitation/ElicitationResult, TaskCreated/Completed, TeammateIdle, MessageDisplay, StopFailure, SubagentStart, PostCompact) are likely to keep growing. Re-verify against the live Hooks reference.
3. **Permission-mode names (MEDIUM drift):** `default`, `acceptEdits`, `plan`, `bypassPermissions` are **stable**; `auto` (research preview) and `dontAsk` are **newer and could be renamed/removed**. `--enable-auto-mode` was already removed in v2.1.111.
4. **"Commands merged into skills" (MEDIUM):** `.claude/commands/` still works but skills are now primary. The exam may still phrase questions in the old "custom slash commands" framing — both should be treated as correct.
5. **MCP scope name changes (MEDIUM trap):** `local` was previously `project`; `user` was previously `global`. Older study material will use the old names.
6. **Settings precedence vs. permission-rule merge (STABLE concept, exam trap):** settings *override* by precedence (Managed > CLI > Local > Project > User); permission *rules merge across scopes* and evaluate deny→ask→allow. Confirm wording stays the same.
7. **Exit-code 2 = block (STABLE but counter-intuitive):** only exit 2 blocks for most events; exit 1 is non-blocking. High-value exam fact; unlikely to change but worth re-confirming.
8. **Specific model IDs (HIGH drift):** `claude-opus-4-8`, `claude-sonnet-4-6` appear in docs as examples; treat any concrete model ID as drift-prone (model selection is owned by another lesson anyway).
9. **Agent SDK naming / billing (MEDIUM):** "Agent SDK" is the current name (formerly "Claude Code SDK"); the June 15, 2026 separate-credit billing change is date-sensitive — re-verify after that date.
10. **`--bare` becoming the `-p` default (LOW-MEDIUM):** docs say this is planned for "a future release"; verify whether it has shipped before teaching `-p` defaults.
11. **Subagent explicit-invocation syntax [RESOLVED 2026-06-09]:** the `@`-mention form IS documented — `@agent-<name>` for local subagents (e.g. `@agent-code-reviewer`), `@agent-plugin:name` for plugin agents, surfaced via an `@` typeahead. Plus delegation by `description` and `--agent`/`Use the X agent` phrasing. (Confirmed live on code.claude.com/docs/en/sub-agents.)
12. **Managed-settings file paths (MEDIUM):** Windows legacy `C:\ProgramData\ClaudeCode\managed-settings.json` is "no longer supported as of v2.1.75"; OS policy locations are version-noted — re-verify for the current release.
13. **CLAUDE.md import depth = 4 hops (STABLE):** likely stable but a precise number worth re-confirming.

---

**Sources:**
- [Settings](https://code.claude.com/docs/en/settings)
- [Hooks reference](https://code.claude.com/docs/en/hooks)
- [Memory / CLAUDE.md](https://code.claude.com/docs/en/memory)
- [Permissions](https://code.claude.com/docs/en/permissions)
- [Subagents](https://code.claude.com/docs/en/sub-agents)
- [Skills](https://code.claude.com/docs/en/skills)
- [Plugins](https://code.claude.com/docs/en/plugins)
- [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [MCP](https://code.claude.com/docs/en/mcp)
- [Headless / Agent SDK via CLI](https://code.claude.com/docs/en/headless)
- [CLI reference](https://code.claude.com/docs/en/cli-reference)
- [Commands](https://code.claude.com/docs/en/commands)
- [Output styles](https://code.claude.com/docs/en/output-styles)
- [Authentication](https://code.claude.com/docs/en/authentication)
- [Best practices](https://code.claude.com/docs/en/best-practices)
