# Domain 1 part B — Agentic Architecture & Orchestration · building: the control tower

ITEMS = [
{
 "id": "D1-14",
 "title": "Parallel subagents: multiple Task calls in one response",
 "concept": "Parallel subagents are spawned by emitting several `Task` tool calls inside a single coordinator response; the same calls issued across separate turns run sequentially.",
 "tested": "A coordinator works independent research subtasks, or the parts of a multi-issue request, one after another, and the question asks how to run them in parallel. The answer emits all the `Task` calls in one coordinator response. Distractors ask for parallelism in the prompt wording, add more subagents, or name a concurrency setting that does not exist.",
 "remember": "Several `Task` calls in one response run in parallel; one call per turn is sequential, whatever the prompt says. Parallelism is a property of the response.",
 "analogy": "The controller clears three aircraft in one transmission and all three start moving together. Reading the same three clearances out one at a time, waiting for each readback before the next, leaves the third aircraft holding while the first is already airborne.",
 "svg": """<rect class="tint" x="12" y="16" width="26" height="64" rx="3"/>
<text class="lbl" x="25" y="52" text-anchor="middle">1</text>
<path class="acc" d="M38 24 h28 M60 20 l6 4 -6 4"/>
<path class="acc" d="M38 48 h28 M60 44 l6 4 -6 4"/>
<path class="acc" d="M38 72 h28 M60 68 l6 4 -6 4"/>
<circle class="tint" cx="78" cy="24" r="8"/>
<circle class="tint" cx="78" cy="48" r="8"/>
<circle class="tint" cx="78" cy="72" r="8"/>
<rect class="dash thin" x="102" y="20" width="26" height="16" rx="2"/>
<path class="thin" d="M115 36 v34 M111 66 l4 4 4 -4"/>
<rect class="dash thin" x="102" y="70" width="26" height="16" rx="2"/>
<line class="no" x1="100" y1="24" x2="130" y2="82"/>
<line class="no" x1="130" y1="24" x2="100" y2="82"/>
<text class="lbl" x="115" y="102" text-anchor="middle">turns</text>""",
 "alt": "One response fanning to three aircraft; a turn-by-turn chain crossed out",
},
{
 "id": "D1-15",
 "title": "Coordinator prompts state goals and quality criteria, not procedures",
 "concept": "A coordinator's subagent prompts state the research goal and the quality criteria for the result rather than a step-by-step procedure, so subagents can adapt as findings emerge.",
 "tested": "A research coordinator returns shallow, checklist-shaped results, or its subagents stall when a step's output does not match the script, and the question asks how to change the coordinator prompt. The answer states the goal and the quality criteria, such as the areas that must be covered and the number of independent sources per claim, and leaves the method to the subagent. Distractors write more detailed steps, which deepens the rigidity, or add more subagents, which runs the same script more times.",
 "remember": "Goal plus quality criteria, not step 1, step 2, step 3. More procedural detail and more subagents are the two distractors; both keep the script.",
 "analogy": "The controller gives a pilot the runway, the level and the sequence, then leaves the flying to the pilot. A controller who called out each control input would have nothing left to give when the wind shifted on final approach.",
 "svg": """<rect class="paper" x="12" y="20" width="60" height="76" rx="3"/>
<circle class="acc" cx="42" cy="42" r="11"/>
<circle class="accfill" cx="42" cy="42" r="4"/>
<line class="thin" x1="22" y1="64" x2="62" y2="64"/>
<line class="thin" x1="22" y1="76" x2="62" y2="76"/>
<line class="thin" x1="22" y1="88" x2="50" y2="88"/>
<rect class="tint" x="88" y="20" width="60" height="76" rx="3"/>
<text class="lbl" x="98" y="42">1</text>
<text class="lbl" x="98" y="60">2</text>
<text class="lbl" x="98" y="78">3</text>
<line class="thin" x1="110" y1="38" x2="140" y2="38"/>
<line class="thin" x1="110" y1="56" x2="140" y2="56"/>
<line class="thin" x1="110" y1="74" x2="140" y2="74"/>
<line class="no" x1="110" y1="32" x2="144" y2="84"/>
<line class="no" x1="144" y1="32" x2="110" y2="84"/>""",
 "alt": "A goal target with criteria beside a crossed-out numbered step list",
},
{
 "id": "D1-16",
 "title": "Programmatic enforcement vs prompt guidance",
 "concept": "A sequence that must always hold is enforced in code with a hook or prerequisite gate that blocks the downstream tool until the prerequisite has returned, because prompt compliance is probabilistic.",
 "tested": "Production data shows the agent skipping `get_customer` and calling `lookup_order` on the customer's stated name, producing misidentified accounts and incorrect refunds, and the question asks the change that most effectively addresses it. The answer is a programmatic prerequisite that blocks `lookup_order` and `process_refund` until `get_customer` has returned a verified customer ID. Distractors strengthen the system prompt or add few-shot examples of the correct order, both of which rely on probabilistic compliance, or add a routing classifier, which changes which tools are available rather than the order they run in.",
 "remember": "A sequence that must always hold goes in code: a hook or prerequisite gate. Stronger prompts and few-shot examples are the probabilistic distractors; tool availability is a different problem.",
 "analogy": "The runway-lights interlock holds red until the previous aircraft has reported clear, so the clearance cannot be issued out of order. A standing instruction to the controller to check first is followed nearly every time; the wiring covers the rest.",
 "svg": """<rect class="tint" x="10" y="50" width="34" height="26" rx="3"/>
<text class="lbl" x="27" y="67" text-anchor="middle">id</text>
<path d="M44 63 h18 M56 59 l6 4 -6 4"/>
<path class="acc" d="M74 34 v72"/>
<circle class="accfill" cx="74" cy="63" r="5"/>
<path d="M82 63 h22 M98 59 l6 4 -6 4"/>
<rect class="tint" x="110" y="50" width="38" height="26" rx="3"/>
<text class="lbl" x="129" y="67" text-anchor="middle">pay</text>
<path class="dash" d="M30 48 q42 -32 84 0"/>
<line class="no" x1="66" y1="18" x2="82" y2="34"/>
<line class="no" x1="82" y1="18" x2="66" y2="34"/>""",
 "alt": "Verified id gate barring the pay tool; a bypass route crossed out",
},
{
 "id": "D1-17",
 "title": "Structured handoff to a human",
 "concept": "A mid-process escalation carries a structured summary — customer ID, root cause, refund amount, recommended action — because the human agent has no access to the conversation transcript.",
 "tested": "Human agents receiving escalations keep asking customers for details the agent already collected, and the question asks the root cause or the fix. The answer compiles a structured handoff summary: customer ID, root cause, amount, actions already taken, recommended action. Distractors hand the human the raw transcript, which they do not have by design, or have them re-run the agent's tools to rebuild the context.",
 "remember": "Handoff payload: customer ID, root cause, amount, recommended action, actions taken. The summary is everything the human sees, so it has to stand alone.",
 "analogy": "The controller coming on shift takes over from a written hand-over sheet: which aircraft, what state, what has been agreed, what to do next. They heard none of the transmissions, so anything left off the sheet is not available to them.",
 "svg": """<rect class="paper" x="14" y="18" width="62" height="84" rx="3"/>
<text class="lbl" x="22" y="38">id</text>
<line class="acc thin" x1="42" y1="34" x2="68" y2="34"/>
<text class="lbl" x="22" y="56">why</text>
<line class="acc thin" x1="48" y1="52" x2="68" y2="52"/>
<text class="lbl" x="22" y="74">amt</text>
<line class="acc thin" x1="48" y1="70" x2="68" y2="70"/>
<text class="lbl" x="22" y="92">next</text>
<line class="acc thin" x1="52" y1="88" x2="68" y2="88"/>
<path class="acc" d="M82 44 h16 M92 40 l6 4 -6 4"/>
<circle cx="122" cy="34" r="9"/>
<path d="M122 43 v18 M108 52 h28"/>
<rect class="dash thin" x="102" y="76" width="38" height="24" rx="2"/>
<line class="no" x1="108" y1="80" x2="134" y2="96"/>
<line class="no" x1="134" y1="80" x2="108" y2="96"/>""",
 "alt": "Handover sheet of four fields passed to a person; transcript crossed out",
},
{
 "id": "D1-18",
 "title": "Multi-concern requests: split, investigate in parallel, synthesise",
 "concept": "A message raising several issues is decomposed into distinct items, each investigated in parallel against shared context, then answered as one unified resolution.",
 "tested": "A customer message carries three problems at once — a double charge, a discount that was not applied, an order to cancel — and the question asks how the agent should work it. The answer splits the message into items, investigates them in parallel on shared customer context, and returns one resolution. Distractors work the issues one after another, repeating the same lookups and raising the tool-call count, or answer each in its own reply and skip the synthesis.",
 "remember": "Several concerns in one message: distinct items, parallel investigation, shared context, one answer. Sequential handling repeats lookups; a reply per issue drops the unified resolution.",
 "analogy": "A pilot calls with three things at once: a level change, a routing question and a fault report. The controller separates them, works all three against the same flight strip, and comes back with one instruction rather than three part-answers.",
 "svg": """<rect class="tint" x="10" y="44" width="26" height="32" rx="3"/>
<text class="lbl" x="23" y="64" text-anchor="middle">3?</text>
<rect class="dash thin" x="54" y="14" width="36" height="92" rx="3"/>
<path class="acc" d="M36 60 h10 v-32 h14"/>
<path class="acc" d="M36 60 h24"/>
<path class="acc" d="M36 60 h10 v32 h14"/>
<rect class="tint" x="60" y="20" width="24" height="16" rx="2"/>
<rect class="tint" x="60" y="52" width="24" height="16" rx="2"/>
<rect class="tint" x="60" y="84" width="24" height="16" rx="2"/>
<path class="acc" d="M84 28 h12 v32"/>
<path class="acc" d="M84 60 h12"/>
<path class="acc" d="M84 92 h12 v-32"/>
<path class="acc" d="M96 60 h14 M104 56 l6 4 -6 4"/>
<rect class="acc" x="114" y="46" width="32" height="28" rx="3"/>""",
 "alt": "One message split into three parallel items, merged into one answer",
},
{
 "id": "D1-19",
 "title": "Two-tool token binding vs a dry_run flag",
 "concept": "A preview is guaranteed only when it is split into two tools: the preview tool returns a single-use confirmation token and the execute tool requires that token.",
 "tested": "A tool with a `dry_run` boolean is being called with `dry_run=false` directly, and the question asks the most reliable way to make every execution follow a preview the user confirmed. The answer replaces it with two tools, a preview tool returning a single-use confirmation token and an execute tool that requires the token. Distractors add instructions and few-shot examples to the tool description, or permit `dry_run=false` only when a matching `dry_run=true` call happened inside a time window. This card is about binding the preview into the tool contract; enforcing a required order between two tools is a prerequisite gate, which is the guide's own answer on that question (D1-16).",
 "remember": "Mandatory preview: two tools bound by a token, so execution without a preview has no token to present. A flag the caller sets is a preview the caller can skip.",
 "analogy": "The tower issues a numbered slip once the approach has been checked, and the runway controller accepts nothing but that slip. A tick-box on the pilot's own paperwork saying the check was done is filled in by whoever would otherwise have skipped it.",
 "svg": """<rect class="tint" x="10" y="16" width="44" height="28" rx="3"/>
<text class="lbl" x="32" y="34" text-anchor="middle">prev</text>
<path class="acc" d="M54 30 h20 M68 26 l6 4 -6 4"/>
<circle class="accfill" cx="86" cy="30" r="7"/>
<path class="acc" d="M86 37 v22 M82 53 l4 6 4 -6"/>
<rect class="tint" x="60" y="62" width="52" height="32" rx="3"/>
<circle class="acc thin" cx="86" cy="70" r="4"/>
<text class="lbl" x="86" y="88" text-anchor="middle">exec</text>
<path class="dash" d="M14 84 h46"/>
<line class="no" x1="25" y1="77" x2="39" y2="91"/>
<line class="no" x1="39" y1="77" x2="25" y2="91"/>""",
 "alt": "Preview issues a token the execute tool needs; bypass crossed out",
},
{
 "id": "D1-20",
 "title": "PostToolUse hooks normalise tool results",
 "concept": "A `PostToolUse` hook intercepts tool results and normalises heterogeneous formats — Unix timestamps, ISO 8601, numeric status codes — from different MCP tools before the model processes them.",
 "tested": "Several MCP tools return the same kind of value in different shapes and the agent compares or reads them wrongly, and the question asks where the conversion belongs. The answer is a `PostToolUse` hook that normalises each result before the model sees it. Distractors put the conversion in the prompt, where it has to be performed correctly on every result, or apply it after the model has already reasoned over the raw values.",
 "remember": "Heterogeneous formats from several tools: a `PostToolUse` hook, applied before the model reads the result. Conversion asked for in the prompt is the probabilistic distractor.",
 "analogy": "Heights arrive in feet from one aircraft and metres from another, times in local and in Zulu, so the tower's feed converts every report to one scale before it reaches the controller. The controller reads one set of units, and no conversion depends on someone remembering to do it.",
 "svg": """<rect class="tint" x="10" y="16" width="30" height="18" rx="2"/>
<text class="lbl" x="25" y="29" text-anchor="middle">1712</text>
<rect class="tint" x="10" y="50" width="30" height="18" rx="2"/>
<text class="lbl" x="25" y="63" text-anchor="middle">ISO</text>
<rect class="tint" x="10" y="84" width="30" height="18" rx="2"/>
<text class="lbl" x="25" y="97" text-anchor="middle">200</text>
<path class="thin" d="M40 25 h16 M50 21 l6 4 -6 4"/>
<path class="thin" d="M40 59 h16 M50 55 l6 4 -6 4"/>
<path class="thin" d="M40 93 h16 M50 89 l6 4 -6 4"/>
<rect class="acc" x="58" y="14" width="30" height="92" rx="4"/>
<text class="lbl" x="73" y="63" text-anchor="middle">hook</text>
<path class="acc" d="M88 59 h14 M96 55 l6 4 -6 4"/>
<rect class="paper" x="106" y="34" width="42" height="52" rx="3"/>
<line class="thin" x1="114" y1="48" x2="140" y2="48"/>
<line class="thin" x1="114" y1="60" x2="140" y2="60"/>
<line class="thin" x1="114" y1="72" x2="140" y2="72"/>""",
 "alt": "Three formats passing through a hook into one uniform record",
},
{
 "id": "D1-21",
 "title": "Intercept outgoing tool calls to block and redirect",
 "concept": "A hook that intercepts outgoing tool calls blocks policy-violating actions, such as a refund above $500, and redirects them to an alternative workflow such as human escalation.",
 "tested": "A business rule has to hold on every call, such as no refund above $500, and the question asks where to enforce it. The answer intercepts the outgoing tool call, blocks the violating one and redirects to human escalation. Distractors state the limit in the system prompt or the tool description, which holds most of the time, or check after the call has run, once the refund has already been issued.",
 "remember": "Rule that must hold every time: intercept the outgoing call, block it, redirect. A limit stated in the prompt is probabilistic; a check after the call is too late.",
 "analogy": "A clearance that would put two aircraft on one runway is refused by the tower's own system before it can be transmitted, and the go-around is offered instead. The refusal happens at the microphone, not after the readback.",
 "svg": """<rect class="tint" x="10" y="64" width="34" height="26" rx="3"/>
<text class="lbl" x="27" y="81" text-anchor="middle">call</text>
<path d="M44 77 h16 M54 73 l6 4 -6 4"/>
<path class="acc" d="M72 52 v46"/>
<text class="lbl" x="72" y="108" text-anchor="middle">$500</text>
<line class="no" x1="64" y1="70" x2="80" y2="84"/>
<line class="no" x1="80" y1="70" x2="64" y2="84"/>
<path class="acc" d="M62 72 q2 -38 30 -38 h16 M102 30 l6 4 -6 4"/>
<circle cx="126" cy="42" r="9"/>
<path d="M126 51 v20 M112 60 h28"/>""",
 "alt": "Tool call stopped at a $500 barrier and redirected to a person",
},
{
 "id": "D1-22",
 "title": "Prompt chaining vs adaptive decomposition",
 "concept": "Prompt chaining runs passes fixed in advance and suits predictable multi-aspect work; dynamic adaptive decomposition generates each subtask from what the previous step discovered and suits open-ended investigation.",
 "tested": "The stem names the workflow — a review that always follows the same template, or an open-ended task such as adding comprehensive tests to a legacy codebase — and asks which decomposition fits. Open-ended work maps the structure first, identifies high-impact areas, then builds a prioritised plan that adapts as dependencies are discovered. Distractors apply a fixed pipeline to a task whose scope is not known up front, apply dynamic decomposition to a predictable one, or put everything in a single pass.",
 "remember": "Scope known up front: prompt chaining, fixed passes. Scope discovered as you go: adaptive, so map, prioritise, adapt. The stem's phrase open-ended investigation is the tell.",
 "analogy": "The day's scheduled arrivals are worked from a sequence written before the shift began. A search flight is directed a leg at a time: the controller sends it where the last leg reported something, and the next instruction does not exist until that report comes in.",
 "svg": """<rect class="tint" x="12" y="18" width="34" height="18" rx="2"/>
<path class="thin" d="M29 36 v10 M25 42 l4 4 4 -4"/>
<rect class="tint" x="12" y="46" width="34" height="18" rx="2"/>
<path class="thin" d="M29 64 v10 M25 70 l4 4 4 -4"/>
<rect class="tint" x="12" y="74" width="34" height="18" rx="2"/>
<line class="dash thin" x1="58" y1="14" x2="58" y2="98"/>
<circle class="acc" cx="72" cy="92" r="6"/>
<path class="acc" d="M77 88 l16 -16"/>
<circle class="acc" cx="98" cy="67" r="6"/>
<path class="acc" d="M102 62 l14 -14"/>
<path class="acc" d="M94 62 l-6 -14"/>
<circle class="acc" cx="121" cy="43" r="6"/>
<circle class="acc" cx="86" cy="42" r="6"/>
<path class="acc dash" d="M125 38 l10 -12"/>
<path class="acc dash" d="M84 36 l-6 -12"/>
<text class="lbl" x="29" y="106" text-anchor="middle">fixed</text>
<text class="lbl" x="104" y="106" text-anchor="middle">adapt</text>""",
 "alt": "A fixed three-step chain beside a plan that branches as it goes",
},
{
 "id": "D1-23",
 "title": "--resume <session-name> continues a named session",
 "concept": "`--resume <session-name>` continues a specific named prior conversation with its saved context, so one investigation can be picked up across several work sessions.",
 "tested": "A named investigation was left unfinished and the question asks how to carry it on in a later work session. The answer resumes that session by name with `--resume`. Distractors open a new conversation and re-describe the problem, or re-run the exploration from the beginning, both discarding context that is still valid.",
 "remember": "`--resume <session-name>` picks up that specific conversation with its context. Naming sessions is what keeps a multi-day investigation addressable; a new session starts empty.",
 "analogy": "Each investigation has its own flight strip in the rack, filed under its number. The controller returning to it pulls that strip and has everything already agreed on it in front of them; a blank strip carries none of that history.",
 "svg": """<rect class="tint" x="10" y="18" width="74" height="88" rx="3"/>
<line class="thin" x1="84" y1="18" x2="84" y2="106"/>
<rect class="paper" x="16" y="24" width="62" height="16" rx="1"/>
<rect class="paper" x="16" y="68" width="62" height="16" rx="1"/>
<rect class="paper" x="16" y="88" width="62" height="14" rx="1"/>
<rect class="acc" x="16" y="46" width="128" height="16" rx="1"/>
<text class="lbl" x="112" y="58" text-anchor="middle">auth</text>""",
 "alt": "A named flight strip pulled out of the rack of strips",
},
{
 "id": "D1-24",
 "title": "fork_session branches from a shared baseline",
 "concept": "`fork_session` creates independent branches from one shared analysis baseline, so two approaches can be explored without repeating the analysis and without either branch seeing the other's reasoning.",
 "tested": "A team wants to compare two refactoring or testing strategies from one completed and expensive codebase analysis, and the question asks how to set that up. The answer is `fork_session` from the analysed session. Distractors run the two strategies one after another in the same session, where the first biases the second, or open two new sessions, each of which redoes the baseline analysis.",
 "remember": "Compare approaches from one analysis: `fork_session`. Both branches inherit context up to the branch point, then diverge. Sequential in one session contaminates; two fresh sessions repeat the work.",
 "analogy": "The strip for a flight already worked up is photocopied so two controllers can each run a what-if, one the northern routing and one the southern, from the same agreed picture. Neither sees the other's markings, and neither reads the flight plan again from the start.",
 "svg": """<rect class="tint" x="10" y="46" width="52" height="26" rx="2"/>
<line class="thin" x1="18" y1="56" x2="54" y2="56"/>
<line class="thin" x1="18" y1="64" x2="44" y2="64"/>
<path class="acc" d="M62 59 l14 -22 h10"/>
<path class="acc" d="M80 33 l6 4 -6 4"/>
<path class="acc" d="M62 59 l14 22 h10"/>
<path class="acc" d="M80 77 l6 4 -6 4"/>
<rect class="acc" x="88" y="20" width="52" height="26" rx="2"/>
<text class="lbl" x="114" y="37" text-anchor="middle">A</text>
<rect class="acc" x="88" y="72" width="52" height="26" rx="2"/>
<text class="lbl" x="114" y="89" text-anchor="middle">B</text>
<line class="dash thin" x1="114" y1="46" x2="114" y2="72"/>
<line class="no" x1="107" y1="52" x2="121" y2="66"/>
<line class="no" x1="121" y1="52" x2="107" y2="66"/>""",
 "alt": "One strip forking into two branches that exchange nothing",
},
{
 "id": "D1-25",
 "title": "Resume and name what changed, or start fresh",
 "concept": "Resume when prior context is mostly valid, start a new session with a structured summary when prior tool results are stale, and on resume name the files that changed.",
 "tested": "A session analysed the codebase and several files have since been refactored, and the question asks how to continue. The answer resumes the named session and states which files changed, so re-analysis is targeted. Distractors resume without mentioning the changes, leaving the agent reasoning over stale tool results, or re-explore the whole codebase when most of the context still holds.",
 "remember": "Mostly valid: resume, and name the changed files. Stale: a new session with a structured summary, which carries the conclusions without the outdated evidence.",
 "analogy": "A controller returning to a strip after a break is told which two aircraft have changed level, and re-checks those two. When the picture has moved on entirely, the strip is written out afresh from the current state rather than annotated.",
 "svg": """<rect class="paper" x="12" y="18" width="64" height="84" rx="3"/>
<line class="thin" x1="22" y1="32" x2="68" y2="32"/>
<line class="acc" x1="22" y1="48" x2="68" y2="48"/>
<circle class="accfill" cx="16" cy="48" r="3"/>
<line class="thin" x1="22" y1="64" x2="68" y2="64"/>
<line class="acc" x1="22" y1="80" x2="68" y2="80"/>
<circle class="accfill" cx="16" cy="80" r="3"/>
<line class="thin" x1="22" y1="96" x2="68" y2="96"/>
<path class="acc" d="M80 64 h16 M90 60 l6 4 -6 4"/>
<path class="tint" d="M116 104 L120 68 H130 L134 104 Z"/>
<rect class="tint" x="108" y="50" width="34" height="16" rx="3"/>
<path class="thin" d="M112 50 L115 40 H135 L138 50"/>""",
 "alt": "File list with two rows marked, feeding the tower for re-analysis",
},
]
