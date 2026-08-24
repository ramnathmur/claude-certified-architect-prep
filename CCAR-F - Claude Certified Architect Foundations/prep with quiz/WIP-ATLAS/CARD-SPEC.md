# CCA-F Concept Atlas — CARD-SPEC (contract for authoring and audit)

Every concept card in `items_d1.py … items_d5.py` is one Python dict. The renderer (`build_atlas.py`) joins it to
`inventory.py` by `id` for the citation, task statement and Key-Distinction chips. Agents write cards; they do not
add, drop or renumber ids. If a card cannot be written faithfully, keep the id and set `"flag": "..."` explaining why.

## 1. Data shape

```python
ITEMS = [
{
 "id": "D1-01",                       # exactly as in inventory.py
 "title": "The agentic loop runs on stop_reason",   # may be polished, meaning unchanged, <= 9 words
 "concept": "...",                    # ONE flat sentence, <= 32 words. The fact, stated plainly.
 "tested": "...",                     # 1-3 sentences: the question shape the exam uses + the distractor it is paired against.
 "remember": "...",                   # the rule, <= 30 words, may be two short sentences. Inline code in backticks.
 "analogy": "...",                    # 2-3 sentences, set in the domain's building (Section 3), recurring cast.
 "svg": """...""",                    # inner SVG markup only, for viewBox 0 0 160 120 (Section 4). No <svg> wrapper.
 "alt": "...",                        # <= 12 words, what the picture shows
},
]
```

Prose fields are plain text. Two inline conventions only, converted by the renderer after HTML-escaping:
`backticks` → `<code>`, `**double asterisks**` → `<b>`. Do not write HTML tags in prose. Straight quotes are fine.

## 2. Prose rules (hard)

- A plain, checkable fact gets one flat sentence. No setup, no invented false belief to negate, no narrative wrapper.
  - Not: "Most people assume the loop ends when the text says done. It doesn't. It ends on stop_reason."
  - Write: "The loop ends when `stop_reason` is `end_turn`; the text content is not the signal."
- No diagnose-negate-reveal tricolons ("That is not X. That is Y, and it is Z.") unless X is a real misconception the
  exam actually pairs against the fact — and then it belongs in **tested**, named as the distractor.
- Say a new idea once. If a sentence re-performs the previous one with more feeling, cut it.
- No dramatic one-liners as punctuation. No exclamation marks. No "simply", "just", "the key insight".
- **tested** names the exam mechanics: the situation type ("production logs show the agent calling X instead of Y"),
  the decision asked ("most effective first step"), and the distractor family (symptom-level fix, over-engineering,
  non-existent feature, wrong problem). Ground it in the official samples and the Key Distinctions.
- **remember** is what the reader carries into the room: the rule plus the tell that identifies the right option.
- Names, flags, paths, config keys, field names go in backticks: `stop_reason`, `.mcp.json`, `tool_choice: "any"`, `-p`.
- Official framing wins over current product docs where they differ (e.g. personal skill variants use *different names*).
- Nothing about any learner, score, mock exam, "your weakness", or study history. The reader is a stranger.
- British or American spelling — either, but consistent inside a card. Product names as Anthropic writes them.

## 3. The town and its five buildings (metaphor system)

The whole document is one town. Each domain is a building; every analogy and picture for that domain happens inside
it, with a small recurring cast, so pictures reinforce each other. Stay in your building; do not borrow another's cast.

| Domain | Building | Cast & fixtures (use these; add sparingly) |
|---|---|---|
| **D1** | **The control tower** | the controller (coordinator); pilots/aircraft (subagents — they never speak to each other, only to the tower); the flight strip (a session; a strip can be photocopied to run two what-ifs = fork); clearance vs advisory (code gate vs prompt guidance); the runway-lights interlock (programmatic prerequisite); the ground-crew hand-over sheet (structured handoff); the tower log; holding pattern (loop); "cleared to land" vs "go around" (end_turn vs tool_use); a plane on the ground knows nothing of the last flight (empty subagent context). |
| **D2** | **The library** | the reference librarian (the model choosing among tools); databases and reading rooms (tools) with a blurb on the door (description); the card catalogue (MCP resources — read, not acted on); the request slip returned with a reason code (structured errors: closed today / wrong form / not for lending / staff only); institutional subscription vs your personal card (`.mcp.json` vs `~/.claude.json`); the PIN on your own card (env-var expansion); interlibrary loan (community server) vs building your own archive (custom); full-text search vs finding a book by its title (Grep vs Glob); pencilling a correction on one page vs re-typing the sheet (Edit vs Read+Write). |
| **D3** | **The office** | the company handbook (project CLAUDE.md); your own sticky notes (user-level — nobody else sees them); floor notices (directory CLAUDE.md); binder tabs pointing to other binders (@import); the rules that apply only when you're on the shop floor (path-scoped rules); playbooks on the shelf, pulled when needed (skills); the side room for messy work (context: fork); the tool cupboard key (allowed-tools); the request form that asks what you need (argument-hint); the architect's drawing before knocking a wall down (plan mode) vs the handyman fixing one hinge (direct execution); the overnight audit robot (CI with `-p`); a fresh auditor for the second look (independent review). |
| **D4** | **The courthouse** | the judge and the clerk; the elements of an offence written in statute (explicit criteria) vs "be reasonable" (vague); the precedent binder (few-shot); the clerk's standard form (schema) — a form can be filled correctly and still be wrong (semantic errors); the appeals bench sending a case back with specific grounds (retry with feedback) that cannot rule on evidence not in the record (retry limits); the night docket (batch — cheaper, no promise of when); the case number stamp (custom_id); a second judge who did not sit at trial (independent review); the sentencing grid with example cases (severity examples). |
| **D5** | **The hospital ward** | the chart at the foot of the bed (case-facts block — survives every shift summary); the shift handover (structured, not "she's fine"); a negative test vs a lost specimen (empty result vs access failure); the consultant is called on written criteria, not on how the patient sounds (escalation); the wristband double-check when two patients share a name (ask for another identifier); a timestamp on every lab value (temporal data); the ward round starts with the summary board (position effects); the trimmed lab panel (trim tool output); the notes file (scratchpad); the whiteboard that lets the next doctor resume after a crash (manifest); audits by department, not the hospital average (stratified sampling, segment accuracy). |

Meta pages (Start / The exam / Trap index / Coverage) sit on the town map, outside the buildings.

## 4. SVG vocabulary (one hand, one weight)

- Canvas: `viewBox="0 0 160 120"`. Keep 8 px clear at every edge. One idea per picture; the exam-relevant element gets
  the accent; an anti-pattern is drawn and crossed out with `class="no"`.
- Provide **inner markup only** — the renderer wraps it in `<svg viewBox="0 0 160 120" role="img"><title>alt</title>…</svg>`.
- Default style (from the document CSS, do not restate it): every shape is `fill: none; stroke: var(--ink); stroke-width: 3; stroke-linecap: round; stroke-linejoin: round`.
- Allowed classes — the only styling mechanism:
  - `class="tint"` — fill with the building's pale tint (stroke stays ink) — use for the main object's body
  - `class="acc"` — accent-coloured stroke — the one thing the card is about
  - `class="accfill"` — solid accent fill + accent stroke — small emphasis marks (a dot, a badge, an arrowhead)
  - `class="paper"` — white fill (to occlude what is behind)
  - `class="thin"` — stroke-width 2 (secondary detail)
  - `class="dash"` — dashed stroke (something absent, implied, or a boundary)
  - `class="no"` — ink stroke, width 4.5, use for the ✕ over an anti-pattern (two short lines)
  - `class="lbl"` — for `<text>` only: 11 px monospace, ink fill, no stroke. Max ~5 characters per label
    (`A`, `-p`, `720`, `any`, `id`). No other text. No text smaller than 11 px.
- Allowed elements: `path rect circle ellipse line polyline polygon g text`. Allowed attributes: geometry (`d x y width
  height r rx ry cx cy x1 y1 x2 y2 points`), `class`, `transform`, `opacity` (0.35–1 only), `text-anchor`, `font-size`
  (11 or 12 only, on `text`). **Not allowed:** `style=`, `fill=`, `stroke=`, any hex/rgb colour, `<image>`, `url(`,
  `<script>`, `<use>`, `<defs>`, ids. The lint (`lint_items.py`) rejects any of these.
- Draw with the cast: e.g. a tower is a tapered trunk + a wider cab on top; a plane is a fuselage line + swept wings; a
  book is a rect with a spine line; a binder is a rect with two rings; a form is a rect with 3 short lines and a check
  box; a bed is a low rect with a headboard and a chart clipboard; a chart is a rect with a zigzag line. Keep shapes
  simple enough to read at 160×120 on a phone.

Reference primitives (copy, adapt, keep the weight):

```
tower:   <path class="tint" d="M70 112 L74 60 H86 L90 112 Z"/><rect class="tint" x="58" y="42" width="44" height="18" rx="4"/><path d="M62 42 L66 30 H94 L98 42"/>
plane:   <path class="tint" d="M20 60 h60 l14 -6 v12 l-14 -6"/><path d="M40 60 l-10 -18 h10 l14 18 M40 60 l-10 18 h10 l14 -18"/>
radar:   <circle cx="80" cy="60" r="34"/><circle class="thin" cx="80" cy="60" r="20"/><path class="acc" d="M80 60 L80 26 A34 34 0 0 1 106 40 Z"/>
book:    <rect class="tint" x="40" y="24" width="30" height="72" rx="3"/><line x1="46" y1="24" x2="46" y2="96"/>
shelf:   <line x1="16" y1="100" x2="144" y2="100"/> + several book rects of differing heights on it
drawer:  <rect class="tint" x="40" y="40" width="80" height="40" rx="3"/><line x1="70" y1="60" x2="90" y2="60"/>   (catalogue drawer with a handle)
slip:    <path class="paper" d="M52 20 h56 v80 h-56 z"/><line class="thin" x1="60" y1="36" x2="100" y2="36"/><line class="thin" x1="60" y1="48" x2="100" y2="48"/>
building:<rect class="tint" x="40" y="24" width="80" height="80"/><line x1="40" y1="52" x2="120" y2="52"/><line x1="40" y1="78" x2="120" y2="78"/>  (floors)
sticky:  <rect class="tint" x="96" y="20" width="36" height="36" rx="2" transform="rotate(6 114 38)"/>
binder:  <rect class="tint" x="50" y="26" width="60" height="70" rx="4"/><circle class="thin" cx="60" cy="46" r="4"/><circle class="thin" cx="60" cy="76" r="4"/>
blueprint:<rect class="tint" x="24" y="24" width="112" height="72" rx="3"/><path class="dash" d="M40 40 h40 v24 h-40 z M92 40 h28 v40 h-28"/>
gavel:   <rect class="tint" x="60" y="34" width="40" height="18" rx="4" transform="rotate(-30 80 43)"/><line x1="72" y1="56" x2="40" y2="94"/><rect x="24" y="96" width="60" height="6" rx="3"/>
form:    <rect class="paper" x="46" y="18" width="68" height="84" rx="3"/><line class="thin" x1="56" y1="36" x2="104" y2="36"/><line class="thin" x1="56" y1="50" x2="104" y2="50"/><rect class="thin" x="56" y="62" width="10" height="10"/>
scales:  <line x1="80" y1="24" x2="80" y2="96"/><line x1="40" y1="40" x2="120" y2="40"/><path d="M40 40 l-12 24 h24 z"/><path d="M120 40 l-12 24 h24 z"/>
stamp:   <circle class="acc" cx="80" cy="60" r="22"/><circle class="acc thin" cx="80" cy="60" r="16"/>
bed:     <rect class="tint" x="24" y="64" width="112" height="24" rx="4"/><rect x="24" y="44" width="10" height="44"/><rect class="paper" x="112" y="30" width="26" height="30" rx="2"/>  (chart at the foot)
chart:   <rect class="paper" x="40" y="20" width="80" height="80" rx="3"/><polyline class="acc" points="50,80 64,60 78,70 92,44 108,52"/>
vial:    <path class="tint" d="M70 24 h20 v40 a10 10 0 0 1 -20 0 z"/><line x1="66" y1="24" x2="94" y2="24"/>
clock:   <circle class="paper" cx="80" cy="60" r="28"/><path d="M80 60 V40 M80 60 L94 68"/>
cross:   <line class="no" x1="20" y1="20" x2="40" y2="40"/><line class="no" x1="40" y1="20" x2="20" y2="40"/>
```

## 5. Sample card (D1-05, control tower)

```python
{
 "id": "D1-05",
 "title": "Hub-and-spoke: every message goes through the coordinator",
 "concept": "In a coordinator–subagent system all communication, error handling and information routing pass through the coordinator; subagents do not talk to each other.",
 "tested": "A design question offers a shortcut — letting the synthesis agent query the search agent directly, or agents sharing a channel — against routing through the coordinator. The shortcut option loses observability and uniform error handling; the coordinator route is the answer even when it costs a round trip.",
 "remember": "Coordinator = hub. Subagent-to-subagent links are the distractor. Round trips are the price of observability and controlled information flow.",
 "analogy": "Pilots on approach never coordinate with each other; each talks only to the tower, and the tower sequences everyone. If two pilots agreed a plan on a private channel, the controller would lose the picture and could not recover the sequence when something went wrong.",
 "svg": """<circle class="accfill" cx="80" cy="60" r="12"/>
<circle class="tint" cx="30" cy="28" r="10"/><circle class="tint" cx="130" cy="28" r="10"/><circle class="tint" cx="30" cy="94" r="10"/><circle class="tint" cx="130" cy="94" r="10"/>
<line x1="38" y1="34" x2="70" y2="53"/><line x1="122" y1="34" x2="90" y2="53"/><line x1="38" y1="88" x2="70" y2="67"/><line x1="122" y1="88" x2="90" y2="67"/>
<line class="dash thin" x1="42" y1="28" x2="118" y2="28"/><line class="no" x1="72" y1="20" x2="88" y2="36"/><line class="no" x1="88" y1="20" x2="72" y2="36"/>""",
 "alt": "Four aircraft linked to a central tower; a direct plane-to-plane line is crossed out",
},
```

## 6. Self-check before returning (each agent)

1. Every id from your domain's inventory slice is present exactly once; none added.
2. Every card has all eight fields; `concept` is one sentence; no field mentions a learner, score or exam attempt.
3. Every fact traces to the official-guide bullet text you were given or to the corpus section cited; nothing invented
   (no flags, parameters, thresholds or behaviours that are not in the source).
4. `svg` uses only the allowed elements/classes; no colours; labels ≤ 5 characters, size 11–12 only.
5. Prose rules in Section 2 hold on a re-read of every card.
