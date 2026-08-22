# Gate 1 — Content Fidelity Review: MCP at a Builder Level

**VERDICT: PASS**

**Blockers: 0 / Majors: 0 / Minors: 3**

**Reviewer:** Independent QA (AI Professor + Senior Research Analyst). Did not author either file.
**Lesson:** `courses/claude-101/extensions/mcp-at-a-builder-level.html`
**Source-of-truth:** `courses/claude-101/extensions/source/mcp-at-a-builder-level_citations.md`
**Date:** 2026-06-05

---

## Check 1 — Coverage

Every major section of the citations file is represented, with proportional depth. Mapping:

| Citations section | Lesson location | Status |
|---|---|---|
| §1 Why MCP exists / M×N | Section 1 (`#l1`) | Full — M×N→M+N, USB-C, Nov 25 2024 origin, scope boundary |
| §2 Architecture host/client/server | Section 2 (`#l2`) | Full — 3 participants verbatim, one-client-per-server, VS Code/Sentry worked example, data/transport layers |
| §3 M-A-U server primitives | Section 3 (`#l3`) | Full — control table verbatim, all three sub-primitives, methods, URIs |
| §4 Client primitives Sampling/Roots/Elicitation | Section 4 (`#l4`) | Full — all three + Logging as fourth utility |
| §5 Transports stdio vs Streamable HTTP + SSE nuance | Section 5 (`#l5`) | Full — both transports, SSE-survives nuance, 3 security warnings, custom transports |
| §6 JSON-RPC + initialize handshake | Section 6 (`#l6`) | Full — 3 message types, 3 handshake purposes, verbatim request/response JSON, ready notification, cancellation |
| §7 Discovery/invocation method catalog | Section 7 (`#l7`) | Full — 15-row catalog matches citations table 1:1, tools/list + tools/call examples |
| §8 MCP with Claude (connector vs Claude Code) | Section 8 (`#l8`) | Full — connector limits, beta header, scopes, `--` separator |
| §9 Security | Section 9 (`#l9`) | Full — human oversight, trust-before-connect, prompt injection, layered boundaries |
| §10 MCP vs raw tool use | Section 10 (`#l10`) | Full — unified registry, indistinguishability, C-E1 tie-in |

No section is missing or thinly covered. Coverage is complete.

---

## Check 2 — Correctness (spot-checks)

All targeted spot-checks pass:

- **M-A-U control split** — Tools=Model, Resources=Application, Prompts=User. Verbatim table (HTML lines 438–440) matches citations table (lines 71–73) exactly. The mnemonic callout (line 444) maps letters correctly: "Tools = Model-controlled · Resources = Application-controlled · Prompts = User-controlled." **No swap.** ✓
- **One-client-per-server** — Quoted verbatim (line 354): "one MCP client for each MCP server… Each MCP client maintains a dedicated connection." The remote two-connection trap (Client3/Client4 to Server C) is preserved (line 381). ✓
- **Initialize request/response JSON** — HTML lines 797–821 reproduce the citations JSON (lines 192–219) character-for-character: `protocolVersion: 2025-06-18`, `capabilities: {elicitation:{}}` (request), `tools:{listChanged:true}` + `resources:{}` (response), matching `clientInfo`/`serverInfo`. ✓
- **`tools/list` / `tools/call`** — Names and shapes exact. `tools/list` "no parameters" (line 899); `tools/call` with `name`+`arguments` and the `weather_current` / San Francisco / imperial example (lines 909–917) matches citations lines 266–276. ✓
- **Connector limitations** — Remote-only ("Local STDIO servers cannot be connected directly") and tool-calls-only ("only tool calls are currently supported") both verbatim (lines 990–991). Platform matrix (not on Bedrock/Vertex) and ZDR ineligibility preserved. ✓
- **`--` separator** — Verbatim "Everything after `--` is passed to the server untouched" (line 1015). ✓
- **SSE-survives nuance** — Correctly stated, not the common error. Line 703: "SSE itself survives as an optional streaming mechanism inside Streamable HTTP. So 'SSE is deprecated' is only half-true." The predict-reveal (line 719) explicitly flags "SSE has been removed" as **False** and a "classic trap." Final-quiz Q5 distractor [1] "SSE has been entirely removed" is correctly keyed wrong; keyed-correct [2] states the nuance. ✓

No numeric, quote, JSON, or method-name discrepancy found.

---

## Check 3 — Traceability / Anti-hallucination

Every substantive claim traces to the citations file. I found **no** invented statistic, method name, fact, or distractor-presented-as-true. Specific adversarial probes:

- The 15-method consolidated catalog (lines 925–939) is identical to the citations catalog (lines 245–259) — no methods added or invented.
- The "5 apps × 8 sources = 40 / 13" reveal (line 298) is arithmetic on the source's own M×N→M+N framing, not a sourced "fact." Legitimate worked example.
- The `weather_current`, `calendar://events/2024`, `travel://activities/{city}/{category}`, `file:///Users/agent/travel-planning` examples all originate in the citations file. ✓
- No keyed-correct MCQ answer relies on a claim outside the source. Distractors (e.g., "roots enforce a hard sandbox," "N²," "WebSocket as a standard transport") are all genuinely false per the source.

---

## Check 4 — [VERIFY] preservation

All **6** source `[VERIFY]` flags are surfaced as visible inline notes and consolidated in the Sources block (lines 1260–1261). None dropped, none presented as settled:

1. **Protocol version string** — `.verifynote` at line 705 (transports section) + consolidated flag #1. ✓
2. **`mcp-client-2025-11-20` beta header** — `.verifynote` at line 997 + key-takeaway VERIFY chip (line 1049) + consolidated #2. ✓
3. **Primitive maturity** — `.verifynote` at line 610 ("Tasks Experimental; Sampling/Elicitation GA unverified") + key-takeaway chip (line 629) + consolidated #3. ✓
4. **Transport status** — VERIFY chip in S5 key takeaways (line 738) + verifynote line 705 ("re-verify the deprecation hasn't progressed to removal") + consolidated #4. ✓
5. **Platform availability** — Noted in verifynote line 997 ("Platform availability is also subject to change") + consolidated #5. ✓
6. **Complete method set** — `.verifynote` at line 943 (tools/call content-type enumeration, resources/unsubscribe) + consolidated #6. ✓

All six are framed as open/version-sensitive, consistent with the source.

---

## Check 5 — MCQ answer-key soundness

I audited **all 22** interactive items (10 inline quick-checks, 4 Quiz-A, 8 final-quiz) against the source. A representative ~8-item sample with full reasoning:

| Item | `data-correct` | Keyed option | Source-grounded? | Distractors all wrong? |
|---|---|---|---|---|
| S1 quick-check | 2 | "standardizes context exchange, not reasoning" | ✓ citations §1 line 35 | ✓ |
| S2 quick-check | 1 | "Two — one dedicated client per server" | ✓ §2 line 43 | ✓ |
| S3 quick-check | 3 | "Application — application-driven, read-only" | ✓ §3 line 72/90 | ✓ |
| Quiz-A Q3 | 0 | "Model, Application, User (M-A-U)" | ✓ §3 line 77 | ✓ |
| S5 quick-check | 1 | "stdio" (local subprocess) | ✓ §5 line 143 | ✓ |
| Final Q5 | 2 | "Streamable HTTP current; standalone HTTP+SSE deprecated but SSE survives" | ✓ §5 line 160 | ✓ ([1] removal-claim correctly false) |
| Final Q9 | 3 | "Remote (HTTPS), tool-calls-only; local STDIO cannot connect" | ✓ §8 line 289 | ✓ |
| Final Q10 | 1 | "standardized packaging/transport over same loop; indistinguishable" | ✓ §10 line 330/332 | ✓ |

Every key index maps to a genuinely correct option in 0-indexed order, and no distractor is true. **Zero mis-keyed questions.** Answer-key soundness is clean.

---

## Itemized findings by severity

### Blockers (0)
None.

### Majors (0)
None.

### Minors (3)

**m1 — Client-primitive table order differs from source (cosmetic).**
- **File/concept:** `#l4` Section 4 table, HTML lines 579–581 vs citations §4 lines 107–109.
- The citations file orders the client features **Elicitation → Roots → Sampling**; the lesson table orders them **Sampling → Roots → Elicitation**. Each feature is still correctly paired with its verbatim description and method (`sampling/createMessage`, `roots/list`, `elicitation/create`), so there is **no feature↔method swap** and no factual error.
- **Fix:** Optional. Reordering would make the table line up with the source for easier diffing, but the current order (leading with Sampling, the D2-overlap concept) is pedagogically defensible. Leave as-is or align — no correctness impact.

**m2 — Minor grammar slip in a transition sentence.**
- **File/concept:** `#l4` Section 4, HTML line 575.
- Reads: *"Sections 3 was server → client…"* — subject/verb number disagreement ("Sections 3 was").
- **Fix:** Change "Sections 3 was" → "Section 3 was". Pure typo; no content-fidelity impact.

**m3 — Forward link to an unbuilt file (already disclosed).**
- **File/concept:** `#nextbox` line 1240 and footer line 1267 link to `prompt-caching-economics.html`.
- The lesson **itself discloses** this: "(that file is not built yet — this forward link may 404 until it lands)." So it is not a hidden defect, but the footer link (line 1267) carries no such disclaimer and will 404 if clicked.
- **Fix:** Optional — add a matching "(coming soon)" note to the footer link, or leave since the nextbox already discloses it. Not a fidelity issue against the source (the source has no "next lesson" claim either way).

---

## One-line readout

Faithful, fully-traceable rendering of the source — all 6 [VERIFY] flags preserved, the SSE-survives nuance and M-A-U split stated correctly, and all 22 MCQ keys sound; only 3 cosmetic minors. **PASS.**
