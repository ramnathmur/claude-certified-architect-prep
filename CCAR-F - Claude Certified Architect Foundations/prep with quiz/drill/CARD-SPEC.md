# CARD-SPEC — the flashcard contract

**Version:** 1.0 | 2026-08-10
**Applies to:** every agent that writes or audits cards for the CCA-F drill deck.

This is the single contract. If a rule below conflicts with anything you infer from another file, this file wins.

---

## 1. What a card is

One card drills **one retrievable fact or one decision rule**. The learner (Ram) sits the CCA-F exam on 2026-08-18. He has read the corpus; he cannot retrieve it under a two-minute-per-question clock. A card exists to convert recognition into recall.

A card is not a mock exam question. It has no options, no distractors, no A/B/C/D. The front asks; the back answers.

**The test for a good card:** could Ram answer the front out loud in under ten seconds, and would that answer be either right or wrong with no argument? If the front invites an essay, split it into two cards. If the back is a paragraph, you have written a lesson, not a card.

---

## 2. Schema

Every card is one JSON object. Generators emit a JSON array of them.

```json
{
  "id": null,
  "domain": "D1",
  "type": "trap",
  "front": "An agent loop decides whether to keep going by scanning `response.content` for a completion phrase. What should it check instead?",
  "back": "The `stop_reason` field: `tool_use` means execute the tool and call the API again, `end_turn` means Claude has finished.",
  "trap": "Exam trap: text-matching for completion language is the documented anti-pattern, however reasonable it reads.",
  "cites": ["Domain-1_v2 §1.1", "Key-Distinctions_v1 #5"],
  "tags": ["known-gap", "d1.1", "agentic-loop"],
  "core": true,
  "rev": false
}
```

| Field | Type | Rule |
|---|---|---|
| `id` | `null` | Always emit `null`. The merge step assigns the real id. Never invent one. |
| `domain` | string | Exactly one of `D1 D2 D3 D4 D5 EX`. Use the official numbering in §3 — not any other ordering you may find elsewhere in the repo. |
| `type` | string | `concept` \| `trap` \| `fact` \| `scenario`. See §4. |
| `front` | string | The question. ≤260 characters (≤420 for `scenario`). Ends with `?` unless it is a fill-in prompt. |
| `back` | string | The answer. ≤320 characters. One sentence; two only when the second adds a distinct fact. |
| `trap` | string or omitted | ≤200 characters. Optional. The only place contrast framing is allowed. See §5. |
| `cites` | array | 1–2 strings, primary first, grammar per §6. Every cite must resolve **and** support the back. |
| `tags` | array | Lowercase strings. Reserved: `known-gap` (+ the sub-domain tag, e.g. `d1.1`). See §7. |
| `core` | boolean | High-yield subset flag. See §8. |
| `rev` | boolean | `true` only on `type: "fact"` cards that read correctly backwards. See §9. |

---

## 3. Domain numbering (official — do not deviate)

| Code | Domain | Weight |
|---|---|---|
| D1 | Agentic Architecture & Orchestration | 27% |
| D2 | Tool Design & MCP Integration | 18% |
| D3 | Claude Code Configuration & Workflows | 20% |
| D4 | Prompt Engineering & Structured Output | 20% |
| D5 | Context Management & Reliability | 15% |
| EX | Exam mechanics (format, scoring, scope) | — |

Other files in this repository use a different D2/D3/D4 ordering. Those are wrong for our purposes. This table is the exam's.

---

## 4. Card types

**`concept`** — a mechanism, rule, or "when do you reach for this" decision.
> Front: "What does a coordinator do when every subagent returns clean output but the report still misses a whole topic area?"
> Back: "Fix the coordinator's task decomposition — complete-looking subagent output with missing coverage traces upstream, not to subagent capability."

**`trap`** — an exam trap: two options that look alike with a decisive difference, or a plausible-but-wrong belief. Every Key Distinction entry becomes at least one of these. The `trap` field is usually filled.

**`fact`** — a number, a flag, a filename, an exact value. Short front, short back.
> Front: "What is the CCA-F passing scaled score, and on what scale?"
> Back: "720, on a scale of 100–1,000."

**`scenario`** — a two-or-three-sentence micro-situation ending in one decision question. Use sparingly and only where the decision genuinely depends on situational detail. This is the only type allowed a longer front.

---

## 5. Prose contract (hard rules)

These come from the deck owner's writing rules. A card that breaks them gets sent back.

**One flat sentence for a plain fact.** No setup, no wind-up, no invented false belief to negate.

- Write: "60 questions, 120 minutes, four blocks of about 15."
- Not: "The questions do not arrive loose. They arrive in blocks."

**No diagnose-negate-reveal.** The shape "That is not X. That is Y, and it is Z." is banned outright in `back`. It is permitted in `trap` only when X is a misconception a candidate actually holds — never one manufactured for rhetorical symmetry.

**Say a new idea once.** If the back's second sentence re-paraphrases the first with more feeling, delete it.

**No drama.** No isolated one-liners for punctuation. No "here's the thing." No rhetorical questions inside the back.

**Banned vocabulary** (the build script greps for these and fails the build):

`leverage · robust · seamless · seamlessly · comprehensive · delve · deep dive · ecosystem · holistic · streamline · streamlined · empower · unlock · supercharge · elevate · crucial · pivotal · game-changing · cutting-edge · journey · landscape · realm · harness · foster · navigate (as metaphor) · "it's important to note" · "not just" · "isn't just" · "more than just"`

Plain technical words are always fine. If a banned word is the literal name of a thing (a tool called `harness`), quote it in backticks and it passes.

**Code formatting.** Wrap every identifier, flag, filename, field name, and literal value in backticks: `stop_reason`, `--print`, `.mcp.json`, `tool_choice`, `"any"`. The app renders backticks as `<code>`. Backticks must be balanced.

**Characters.** ASCII plus `§` and `—` only. No smart quotes, no emoji, no arrows. Write `->` as the word "to" or use a colon.

---

## 6. Cite grammar

Cites are the join key between cards and mock-exam questions, so the format is exact. Copy these shapes character for character:

| Shape | Example | Valid range |
|---|---|---|
| `Domain-N_v2 §X.Y` | `Domain-1_v2 §1.1` | Any `## X.Y` heading that actually exists in that domain file |
| `Key-Distinctions_v1 #N` | `Key-Distinctions_v1 #5` | **#1 to #25 only.** The file ends at #25. Do not cite #26–#29; they do not exist. |
| `Exam-Mechanics_v2 <heading>` | `Exam-Mechanics_v2 Format` | Any `##` heading in that file |
| `Official-Guide p.N` | `Official-Guide p.2` | Page numbers present in the extracted text |

Rules:
- **The primary cite comes first**, and it must be the section the back's claim is actually drawn from.
- Two cites maximum. A second cite is for a trap that a Key Distinction also covers.
- **Never cite a mock exam.** Mocks are a mining source, not an authority. If you found a fact in a mock's rationale, trace it to the corpus section that rationale cites and use that.
- A cite that resolves but doesn't support the claim is a defect the audit wave will catch. Do not guess a section number — open the file.

---

## 7. Tags

Free-form lowercase, 1–4 per card. Use them for topic grouping (`agentic-loop`, `mcp-config`, `batch-api`).

**`known-gap` is reserved.** Apply it, plus the sub-domain tag, only to cards covering these eight documented weak points. These come from real recorded misses, and the app weights them:

| Sub-domain tag | Gap | Minimum cards |
|---|---|---|
| `d1.1` | Agentic-loop anti-patterns. **Ram once selected "check the reply text for a completion phrase" as the correct answer.** This is a belief-level error: he does not think he is guessing. Attack it from several angles. | ≥10 |
| `d2.1` | Tool description design | ≥4 |
| `d2.2` | MCP primitives — resources as catalogs, tools as actions | ≥4 |
| `d3.6` | Headless / CI mode, `-p` / `--print` | ≥7 |
| `d3.1` | CLAUDE.md hierarchy and precedence | ≥5 |
| `d4.5` | `stop_reason` / `tool_use` API mechanics | ≥8 |
| `d5.1` | Lost-in-the-middle mechanism | ≥6 |
| `d5.2` | Prompt caching — **as a scope boundary and a distractor**, see the note below | ≥2 |

Sub-domain tags are labels, not cite paths — the card still cites whichever corpus section actually covers it.

**On `d5.2`.** Prompt caching is a recorded weak spot for this learner, but the exam's own position on it is narrow: "prompt caching implementation details (beyond knowing it exists)" sits on the official out-of-scope list, and in the official sample questions caching appears only as a *wrong* option — the over-engineered cost fix that ignores the real requirement. There is no corpus section teaching it. So write two cards at most, and write them about that: caching is out of scope past knowing it exists, and "use prompt caching to cut cost" is a distractor shape. Do not write cards teaching caching mechanics; they would drill material the exam excludes.

---

## 8. `core` — the high-yield flag

Set `core: true` when the card meets any of:
- it encodes a Key Distinction entry,
- it carries `known-gap`,
- it is a number, limit, flag, or filename a candidate must have cold,
- it appears in the EXAM-DIGEST must-know or anti-pattern lists.

Roughly 60% of cards should be core. Set it honestly — a deck where everything is core has no high-yield subset.

---

## 9. `rev` — reversible facts

Set `rev: true` only on `type: "fact"` cards where showing the back and asking for the front is a sensible question.

- Reversible: front "What is the pass mark?" / back "720" — asking "what does 720 mean?" works.
- Not reversible: any card whose back is a rule or an explanation.

Target under 10% of facts. Reversed twins appear only in the Numbers rapid-fire drill and hold no scheduler state.

---

## 10. What you must not do

- **Do not copy or lightly reword any mock-exam stem or option.** Ram sits Mocks 2, 3, and 4 this week; leaked wording destroys them as measurement. Fronts are questions in your own words.
- **Do not write about out-of-scope topics.** The exclusion list is in `CCA-Prep_Exam-Mechanics_v2.md` and includes fine-tuning, streaming/SSE, vision, computer use, vector-DB internals, OAuth, cloud-provider config, rate limits, token-counting internals, and prompt-caching implementation details. Knowing prompt caching *exists* and when it pays is in scope; how it is implemented is not.
- **Do not invent flags, parameters, or behaviors.** If the corpus does not say it, it does not go on a card. `CLAUDE_HEADLESS=true` and `--batch` are examples of things that do not exist.
- **Do not resolve a conflict yourself.** Where `CURRENT-DOCS-DELTA_v1.md` marks an item `[CONFLICT-RISK]`, the official Exam Guide's framing wins, and the card must not make the divergence itself the thing being tested.
- **Do not put the answer in the front.** "Why is `stop_reason` the right signal to check?" hands over the answer. Ask "what should it check instead?"
- **Do not write two cards that ask the same thing in different words.** The build script flags near-duplicates and they cost quota.

---

## 11. Output format

Write your cards to the file path named in your task prompt, as a **UTF-8 JSON array**, no wrapper object, no markdown fence, no commentary:

```json
[
  { "id": null, "domain": "D1", "type": "concept", "front": "...", "back": "...", "cites": ["Domain-1_v2 §1.1"], "tags": ["agentic-loop"], "core": true, "rev": false },
  { "id": null, "domain": "D1", "type": "trap", "front": "...", "back": "...", "trap": "...", "cites": ["Key-Distinctions_v1 #5"], "tags": ["known-gap", "d1.1"], "core": true, "rev": false }
]
```

Use the Write tool (not a shell heredoc) so encoding stays clean. Then report back: how many cards, the type mix, the known-gap counts, and which corpus sections you covered.

---

## 12. Examples

### Three good cards

```json
{ "id": null, "domain": "D3", "type": "trap",
  "front": "Which flag makes Claude Code non-interactive for a CI pipeline?",
  "back": "`-p` (or `--print`) — it runs the prompt and prints the result to stdout.",
  "trap": "Exam trap: `CLAUDE_HEADLESS=true` and `--batch` appear as options and neither exists.",
  "cites": ["Key-Distinctions_v1 #15", "Domain-3_v2 §3.8"],
  "tags": ["known-gap", "d3.6", "ci"], "core": true, "rev": false }
```
Why it works: one retrievable answer, the invented-flag trap is where the contrast belongs, both cites resolve.

```json
{ "id": null, "domain": "D5", "type": "concept",
  "front": "A long conversation keeps losing exact refund amounts even though summarization is working. What structural fix preserves them?",
  "back": "Extract the transactional facts into a case-facts block held outside the summarized history, so compression cannot touch them.",
  "cites": ["Domain-5_v2 §5.4"],
  "tags": ["context-window", "facts-persistence"], "core": true, "rev": false }
```
Why it works: the front carries just enough situation to make the question decidable, and the back names the mechanism.

```json
{ "id": null, "domain": "EX", "type": "fact",
  "front": "How many scenarios does a CCA-F sitting present, and out of how many?",
  "back": "Four, drawn at random from a bank of six.",
  "cites": ["Exam-Mechanics_v2 Format"],
  "tags": ["exam-format"], "core": true, "rev": true }
```
Why it works: flat fact, one sentence, and it reverses cleanly.

### Three bad cards

```json
{ "front": "Tell me about the agentic loop.", "back": "..." }
```
Broken: not a question with one answer. Split into cards on the stop signal, the tool-result append, and the termination condition.

```json
{ "front": "What signals loop completion?",
  "back": "It is not the text of the reply. It is the structured `stop_reason` field, and it is the only reliable signal." }
```
Broken: diagnose-negate-reveal in the back. Write "The `stop_reason` field: `end_turn` means finished." and move the contrast to `trap`.

```json
{ "front": "Why is a comprehensive coordinator-level fix the robust way to handle coverage gaps?",
  "back": "Because it leverages the coordinator's holistic view...",
  "cites": ["Key-Distinctions_v1 #27"] }
```
Broken three ways: banned vocabulary (`comprehensive`, `robust`, `leverages`, `holistic`), the front leaks the answer, and `#27` does not exist — the file stops at #25.
