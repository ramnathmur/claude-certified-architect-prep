# Authoring brief — D2 Tool Design & MCP Integration (18%) · building: The library

Corpus depth file: `prep with quiz/CCA-Prep_Domain-2_v2.md`. Official guide text: `prep with quiz/source/CCA-F-Official-Exam-Guide_text.txt` (task statements 2.1–2.x and the sample questions).

19 cards, in this order (ids fixed):

## D2-01 — The description is the interface
Home task statement: TS 2.1 — Design effective tool interfaces with clear descriptions and boundaries
Gist (the concept, to be written as one flat sentence): Tool selection runs on descriptions; include input formats, example queries, edge cases and when-to-use boundaries.
Official-guide bullets this card must cover:
- [2.1-K1] Tool descriptions as the primary mechanism LLMs use for tool selection; minimal descriptions lead to unreliable selection among similar tools
- [2.1-K2] The importance of including input formats, example queries, edge cases, and boundary explanations in tool descriptions
- [2.1-S1] Writing tool descriptions that clearly differentiate each tool's purpose, expected inputs, outputs, and when to use it versus similar alternatives
Appendix items it also serves: [APP-I4] Tool interface design: Writing effective tool descriptions, splitting vs consolidating too…; [APP-I5] MCP tool and resource design: Resources for content catalogs, tools for actions, descripti…; [APP-T2] Model Context Protocol (MCP) — MCP servers, MCP tools, MCP resources, isError flag, tool d…

Key Distinction to weave into `tested` / `remember`:
```
KD #10 — Fix tool descriptions vs Add routing layer
When tool misrouting occurs:
- ✅ Fix tool descriptions first (root cause: descriptions don't distinguish similar tools)
- ❌ Add pre-routing classifier (adds infrastructure without fixing the underlying ambiguity)

**Rule:** Fix the signal (description) before adding a new layer that compensates for the bad signal.

---
```

## D2-02 — Overlapping descriptions misroute — rename and differentiate
Home task statement: TS 2.1 — Design effective tool interfaces with clear descriptions and boundaries
Gist (the concept, to be written as one flat sentence): Near-identical descriptions (analyze_content vs analyze_document) cause misrouting; fix by renaming and rewriting for a distinct purpose.
Official-guide bullets this card must cover:
- [2.1-K3] How ambiguous or overlapping tool descriptions cause misrouting (e.g., analyze_content vs analyze_document with near-identical descriptions)
- [2.1-S2] Renaming tools and updating descriptions to eliminate functional overlap (e.g., renaming analyze_content to extract_web_results with a web-specific description)
Appendix items it also serves: [APP-I4] Tool interface design: Writing effective tool descriptions, splitting vs consolidating too…

Key Distinction to weave into `tested` / `remember`:
```
KD #10 — Fix tool descriptions vs Add routing layer
When tool misrouting occurs:
- ✅ Fix tool descriptions first (root cause: descriptions don't distinguish similar tools)
- ❌ Add pre-routing classifier (adds infrastructure without fixing the underlying ambiguity)

**Rule:** Fix the signal (description) before adding a new layer that compensates for the bad signal.

---
```

## D2-03 — Split generic tools into purpose-specific ones
Home task statement: TS 2.1 — Design effective tool interfaces with clear descriptions and boundaries
Gist (the concept, to be written as one flat sentence): One vague analyze_document becomes extract_data_points, summarize_content, verify_claim_against_source, each with a defined contract.
Official-guide bullets this card must cover:
- [2.1-S3] Splitting generic tools into purpose-specific tools with defined input/output contracts (e.g., splitting a generic analyze_document into extract_data_points, summarize_content, and verify_claim_against_source)
Appendix items it also serves: [APP-I4] Tool interface design: Writing effective tool descriptions, splitting vs consolidating too…

## D2-04 — Keyword-sensitive system-prompt wording overrides good descriptions
Home task statement: TS 2.1 — Design effective tool interfaces with clear descriptions and boundaries
Gist (the concept, to be written as one flat sentence): A phrase in the system prompt can bind a tool to a keyword; review the prompt when selection goes wrong despite good descriptions.
Official-guide bullets this card must cover:
- [2.1-K4] The impact of system prompt wording on tool selection: keyword-sensitive instructions can create unintended tool associations
- [2.1-S4] Reviewing system prompts for keyword-sensitive instructions that might override well-written tool descriptions

## D2-05 — isError plus structured error metadata
Home task statement: TS 2.2 — Implement structured error responses for MCP tools
Gist (the concept, to be written as one flat sentence): Return isError with errorCategory, isRetryable and a readable message; a generic "Operation failed" gives the agent nothing to decide on.
Official-guide bullets this card must cover:
- [2.2-K1] The MCP isError flag pattern for communicating tool failures back to the agent
- [2.2-K3] Why uniform error responses (generic "Operation failed") prevent the agent from making appropriate recovery decisions
- [2.2-K4] The difference between retryable and non-retryable errors, and how returning structured metadata prevents wasted retry attempts
- [2.2-S1] Returning structured error metadata including errorCategory (transient/validation/permission), isRetryable boolean, and human-readable descriptions
Appendix items it also serves: [APP-I7] Error handling and propagation: Structured error responses, transient vs business vs permi…; [APP-T2] Model Context Protocol (MCP) — MCP servers, MCP tools, MCP resources, isError flag, tool d…

Key Distinction to weave into `tested` / `remember`:
```
KD #8 — Structured error context vs Generic failure status
| | Structured error context | Generic "search unavailable" |
|---|---|---|
| Includes | Failure type + attempted query + partial results + alternatives | Only: "failed" |
| Enables | Intelligent coordinator recovery (retry with modified query? continue partial?) | Only: retry or abort |
| Correct choice | ✅ Always | ❌ Never return generic status |

---
```

Key Distinction to weave into `tested` / `remember`:
```
KD #9 — Transient vs Permanent errors (MCP tool design)
| | Transient (timeout, network) | Permanent (syntax error, not found) |
|---|---|---|
| Retry? | ✅ Yes, with backoff | ❌ No — will always fail |
| Handle where? | Inside the tool before surfacing | Immediately return error with details |
| "0 results" | Valid result (NOT an error) | — |
| Timeout | Access failure (needs coordinator decision) | — |

**Exam trap:** "0 results" and "timeout" look similar but require completely different responses. Distinguish them explicitly.

---
```

## D2-06 — Four error kinds: transient, validation, business, permission
Home task statement: TS 2.2 — Implement structured error responses for MCP tools
Gist (the concept, to be written as one flat sentence): Each kind gets a different move — retry, fix the input, explain the policy (retriable: false), or ask for access.
Official-guide bullets this card must cover:
- [2.2-K2] The distinction between transient errors (timeouts, service unavailability), validation errors (invalid input), business errors (policy violations), and permission errors
- [2.2-S2] Including retriable: false flags and customer-friendly explanations for business rule violations so the agent can communicate appropriately
Appendix items it also serves: [APP-I7] Error handling and propagation: Structured error responses, transient vs business vs permi…

Key Distinction to weave into `tested` / `remember`:
```
KD #9 — Transient vs Permanent errors (MCP tool design)
| | Transient (timeout, network) | Permanent (syntax error, not found) |
|---|---|---|
| Retry? | ✅ Yes, with backoff | ❌ No — will always fail |
| Handle where? | Inside the tool before surfacing | Immediately return error with details |
| "0 results" | Valid result (NOT an error) | — |
| Timeout | Access failure (needs coordinator decision) | — |

**Exam trap:** "0 results" and "timeout" look similar but require completely different responses. Distinguish them explicitly.

---
```

## D2-07 — Fewer tools per agent
Home task statement: TS 2.3 — Distribute tools appropriately across agents and configure tool choice
Gist (the concept, to be written as one flat sentence): Eighteen tools instead of four or five degrades selection; decision complexity is the cost.
Official-guide bullets this card must cover:
- [2.3-K1] The principle that giving an agent access to too many tools (e.g., 18 instead of 4-5) degrades tool selection reliability by increasing decision complexity

## D2-08 — Scoped tool sets per role, one cross-role tool for the common case
Home task statement: TS 2.3 — Distribute tools appropriately across agents and configure tool choice
Gist (the concept, to be written as one flat sentence): Give each subagent only its role's tools; when one agent frequently needs another's capability, give it a scoped tool (verify_fact) and route the rare complex cases through the coordinator.
Official-guide bullets this card must cover:
- [2.3-K2] Why agents with tools outside their specialization tend to misuse them (e.g., a synthesis agent attempting web searches)
- [2.3-K3] Scoped tool access: giving agents only the tools needed for their role, with limited cross-role tools for specific high-frequency needs
- [2.3-S1] Restricting each subagent's tool set to those relevant to its role, preventing cross-specialization misuse
- [2.3-S3] Providing scoped cross-role tools for high-frequency needs (e.g., a verify_fact tool for the synthesis agent) while routing complex cases through the coordinator
Appendix items it also serves: [APP-T2] Model Context Protocol (MCP) — MCP servers, MCP tools, MCP resources, isError flag, tool d…

## D2-09 — Constrained alternatives to generic tools
Home task statement: TS 2.3 — Distribute tools appropriately across agents and configure tool choice
Gist (the concept, to be written as one flat sentence): Replace fetch_url with load_document that validates document URLs.
Official-guide bullets this card must cover:
- [2.3-S2] Replacing generic tools with constrained alternatives (e.g., replacing fetch_url with load_document that validates document URLs)

## D2-10 — .mcp.json (project, shared) vs ~/.claude.json (user, personal)
Home task statement: TS 2.4 — Integrate MCP servers into Claude Code and agent workflows
Gist (the concept, to be written as one flat sentence): Team servers live in the repo's .mcp.json; personal or experimental servers in ~/.claude.json.
Official-guide bullets this card must cover:
- [2.4-K1] MCP server scoping: project-level (.mcp.json) for shared team tooling vs user-level (~/.claude.json) for personal/experimental servers
- [2.4-S1] Configuring shared MCP servers in project-scoped .mcp.json with environment variable expansion for authentication tokens
- [2.4-S2] Configuring personal/experimental MCP servers in user-scoped ~/.claude.json
Appendix items it also serves: [APP-I6] MCP server configuration: Project vs user scope, environment variable expansion, multi-ser…; [APP-T2] Model Context Protocol (MCP) — MCP servers, MCP tools, MCP resources, isError flag, tool d…

Key Distinction to weave into `tested` / `remember`:
```
KD #2 — `.mcp.json` vs `~/.claude.json`
| | `.mcp.json` | `~/.claude.json` |
|---|---|---|
| Location | Project root | User home directory |
| Scope | Project | User across all projects |
| Version-controlled | ✅ Yes | ❌ No |
| Use for | Shared MCP server config | Personal auth, personal overrides |

**Exam pattern:** Team shares MCP server, each developer has their own token → `.mcp.json` with `${GITHUB_TOKEN}` env var substitution.

---
```

## D2-11 — ${ENV_VAR} expansion keeps secrets out of the repo
Home task statement: TS 2.4 — Integrate MCP servers into Claude Code and agent workflows
Gist (the concept, to be written as one flat sentence): .mcp.json references ${GITHUB_TOKEN}; each developer supplies their own value.
Official-guide bullets this card must cover:
- [2.4-K2] Environment variable expansion in .mcp.json (e.g., ${GITHUB_TOKEN}) for credential management without committing secrets
- [2.4-S1] Configuring shared MCP servers in project-scoped .mcp.json with environment variable expansion for authentication tokens
Appendix items it also serves: [APP-I6] MCP server configuration: Project vs user scope, environment variable expansion, multi-ser…; [APP-T2] Model Context Protocol (MCP) — MCP servers, MCP tools, MCP resources, isError flag, tool d…

Key Distinction to weave into `tested` / `remember`:
```
KD #2 — `.mcp.json` vs `~/.claude.json`
| | `.mcp.json` | `~/.claude.json` |
|---|---|---|
| Location | Project root | User home directory |
| Scope | Project | User across all projects |
| Version-controlled | ✅ Yes | ❌ No |
| Use for | Shared MCP server config | Personal auth, personal overrides |

**Exam pattern:** Team shares MCP server, each developer has their own token → `.mcp.json` with `${GITHUB_TOKEN}` env var substitution.

---
```

## D2-12 — All configured servers' tools are discovered at connection and available together
Home task statement: TS 2.4 — Integrate MCP servers into Claude Code and agent workflows
Gist (the concept, to be written as one flat sentence): Multiple MCP servers do not take turns; their tools are all on the table at once.
Official-guide bullets this card must cover:
- [2.4-K3] That tools from all configured MCP servers are discovered at connection time and available simultaneously to the agent
Appendix items it also serves: [APP-I6] MCP server configuration: Project vs user scope, environment variable expansion, multi-ser…

## D2-13 — MCP resources expose content catalogs
Home task statement: TS 2.4 — Integrate MCP servers into Claude Code and agent workflows
Gist (the concept, to be written as one flat sentence): Resources give the agent visibility into issue lists, doc hierarchies or schemas without exploratory tool calls; tools act, resources are read.
Official-guide bullets this card must cover:
- [2.4-K4] MCP resources as a mechanism for exposing content catalogs (e.g., issue summaries, documentation hierarchies, database schemas) to reduce exploratory tool calls
- [2.4-S5] Exposing content catalogs as MCP resources to give agents visibility into available data without requiring exploratory tool calls
Appendix items it also serves: [APP-I5] MCP tool and resource design: Resources for content catalogs, tools for actions, descripti…; [APP-T2] Model Context Protocol (MCP) — MCP servers, MCP tools, MCP resources, isError flag, tool d…

## D2-14 — It keeps choosing Grep over your MCP tool — fix the description
Home task statement: TS 2.4 — Integrate MCP servers into Claude Code and agent workflows
Gist (the concept, to be written as one flat sentence): The agent prefers a familiar built-in unless the MCP tool's description spells out what it can do that Grep cannot.
Official-guide bullets this card must cover:
- [2.4-S3] Enhancing MCP tool descriptions to explain capabilities and outputs in detail, preventing the agent from preferring built-in tools (like Grep) over more capable MCP tools
Appendix items it also serves: [APP-I5] MCP tool and resource design: Resources for content catalogs, tools for actions, descripti…

Key Distinction to weave into `tested` / `remember`:
```
KD #29 — MCP tool vs built-in tool preference — fix the description, don't remove the built-in
Agents may **default to a familiar built-in (Grep, Read) over a more capable MCP tool** because selection runs on descriptions. If the MCP tool's description doesn't make its superior capability explicit, the agent falls back to the built-in.

**Exam trap:** A semantic, index-backed code-search MCP server exists, but the agent keeps using built-in Grep →
- ✅ Enhance the MCP tool's description — spell out its unique capability, outputs, and what built-in tools *cannot* provide
- ❌ Remove or disable Grep so the agent has no alternative (breaks legitimate content-search cases; root cause is an under-specified description, not the built-in's existence)
- ❌ Add a "always prefer MCP tools" system-prompt rule (blunt and keyword-sensitive; misroutes cases where the built-in genuinely is right)

**Rule (mirrors #10):** Fix the signal (description) before adding a layer — or removing a tool — to compensate for the bad signal.
```

## D2-15 — Community server for standard integrations, custom for your own workflows
Home task statement: TS 2.4 — Integrate MCP servers into Claude Code and agent workflows
Gist (the concept, to be written as one flat sentence): Use an existing Jira server; write your own only for team-specific behaviour.
Official-guide bullets this card must cover:
- [2.4-S4] Choosing existing community MCP servers over custom implementations for standard integrations (e.g., Jira), reserving custom servers for team-specific workflows

## D2-16 — Grep searches inside files; Glob matches paths
Home task statement: TS 2.5 — Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively
Gist (the concept, to be written as one flat sentence): Callers, error strings and imports are Grep; **/*.test.tsx is Glob.
Official-guide bullets this card must cover:
- [2.5-K1] Grep for content search (searching file contents for patterns like function names, error messages, or import statements)
- [2.5-K2] Glob for file path pattern matching (finding files by name or extension patterns)
- [2.5-S1] Selecting Grep for searching code content across a codebase (e.g., finding all callers of a function, locating error messages)
- [2.5-S2] Selecting Glob for finding files matching naming patterns (e.g., **/*.test.tsx)
Appendix items it also serves: [APP-T9] Built-in tools — Read, Write, Edit, Bash, Grep, Glob — their purposes and selection criter…

Key Distinction to weave into `tested` / `remember`:
```
KD #26 — Grep (content search) vs Glob (path pattern match)
| | Grep | Glob |
|---|---|---|
| Searches | *Inside* files — content | File *names / paths* — patterns |
| Finds | Function names, error strings, import statements, call sites | Files by name or extension (`**/*.test.tsx`) |
| "Find all callers of `processPayment`" | ✅ Grep the symbol across the codebase | ❌ Wrong tool |
| "Enumerate all TypeScript test files" | ❌ Wrong tool | ✅ Glob `**/*.test.tsx` |

**Exam trap:** Locate every file that references a deprecated `formatDate` function → Grep for `formatDate` (target is file *content*). ❌ Glob `**/formatDate*` only matches files *named* formatDate, not files that use it. Conversely, Grepping for the word "test" to find test files matches unrelated files and misses test files that don't contain the literal word — that's a Glob job.

---
```

## D2-17 — Edit needs a unique anchor; otherwise Read + Write
Home task statement: TS 2.5 — Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively
Gist (the concept, to be written as one flat sentence): Read/Write handle whole files; Edit replaces by unique text match and fails on duplicates, so fall back to Read then Write.
Official-guide bullets this card must cover:
- [2.5-K3] Read/Write for full file operations; Edit for targeted modifications using unique text matching
- [2.5-K4] When Edit fails due to non-unique text matches, using Read + Write as a fallback for reliable file modifications
- [2.5-S3] Using Read to load full file contents followed by Write when Edit cannot find unique anchor text
Appendix items it also serves: [APP-T9] Built-in tools — Read, Write, Edit, Bash, Grep, Glob — their purposes and selection criter…

Key Distinction to weave into `tested` / `remember`:
```
KD #27 — Edit (unique-text match) vs Read + Write fallback when the anchor is non-unique
| | Edit | Read + Write fallback |
|---|---|---|
| Mechanism | Replace via a **unique** text anchor | Load full file → modify → write full file |
| Fails when | Anchor appears more than once (can't decide which) | — |
| Correct for | Targeted single-occurrence modification | Modification where no unique anchor exists |

**Exam trap:** Edit fails because the anchor isn't unique →
- ✅ Fall back to Read + Write for a reliable full-file modification
- ❌ Retry Edit with a *shorter* anchor — shorter strings are *more* likely to be non-unique, not less
- ❌ Force it with Bash `sed` — bypasses the tool designed for the job; the sanctioned fallback is Read + Write

---
```

## D2-18 — Grep first, then Read to trace — never read everything up front
Home task statement: TS 2.5 — Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively
Gist (the concept, to be written as one flat sentence): Find entry points by content search, then follow imports with targeted reads.
Official-guide bullets this card must cover:
- [2.5-S4] Building codebase understanding incrementally: starting with Grep to find entry points, then using Read to follow imports and trace flows, rather than reading all files upfront
Appendix items it also serves: [APP-T9] Built-in tools — Read, Write, Edit, Bash, Grep, Glob — their purposes and selection criter…

Key Distinction to weave into `tested` / `remember`:
```
KD #28 — Incremental investigation (Grep → Read) vs reading all files upfront
| | Incremental (Grep → Read) | Bulk read upfront |
|---|---|---|
| Discovery driver | Content search locates entry points, then targeted reads follow imports/flows | Read every file "for full context" first |
| Context window | Spent only on relevant files | Burned on irrelevant files |
| Exam verdict | ✅ Correct pattern | ❌ Anti-pattern |

**Exam trap:** To understand a codebase, "Read every file first to get full context" → Wrong. Start with Grep to find entry points, then Read to trace. ❌ Globbing the whole tree and Reading each match before searching is the *same* anti-pattern — discovery should be driven by content search, then targeted reads, not exhaustive upfront reading.

---
```

## D2-19 — Tracing through wrappers: list the exports, then search each name
Home task statement: TS 2.5 — Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively
Gist (the concept, to be written as one flat sentence): Identify every exported name first, then Grep for each across the codebase.
Official-guide bullets this card must cover:
- [2.5-S5] Tracing function usage across wrapper modules by first identifying all exported names, then searching for each name across the codebase
