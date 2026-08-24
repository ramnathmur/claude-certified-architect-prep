# Domain 1 part A — Agentic Architecture & Orchestration · building: the control tower

ITEMS = [
{
 "id": "D1-01",
 "title": "The agentic loop runs on stop_reason",
 "concept": "After each API call the orchestrator reads `stop_reason`: `tool_use` means execute the requested tools, append the results and call Claude again; `end_turn` means the loop stops.",
 "tested": "Implementation questions give you a loop and ask what the continue-or-stop decision keys on. The correct option branches on `stop_reason`; the distractor reads Claude's text for a completion phrase, which is probabilistic control where a deterministic field already exists.",
 "remember": "`tool_use` → run the tool, append the result, go round again. `end_turn` → stop and return. The field is the signal; the text is not.",
 "analogy": "Every call from an aircraft ends with one entry on the flight strip: another circuit, or cleared to land. The controller acts on that entry, and a pilot who sounds finished but has not been cleared flies the pattern again.",
 "svg": """<path class="tint" d="M22 104 L26 66 H38 L42 104 Z"/>
<rect class="tint" x="16" y="48" width="32" height="18" rx="4"/>
<path d="M20 48 L24 38 H40 L44 48"/>
<rect class="paper" x="66" y="40" width="52" height="38" rx="3"/>
<line class="thin" x1="74" y1="52" x2="110" y2="52"/>
<line class="thin" x1="74" y1="62" x2="98" y2="62"/>
<path class="acc" d="M118 50 h20 M132 45 l6 5 -6 5"/>
<text class="lbl" x="130" y="34" text-anchor="middle">end</text>
<path class="acc" d="M92 78 v18 H58 V56 h8 M60 51 l6 5 -6 5"/>
<text class="lbl" x="78" y="106" text-anchor="middle">tool</text>""",
 "alt": "Flight strip with one arrow looping back and one leaving",
},
{
 "id": "D1-02",
 "title": "Tool results are appended to the conversation",
 "concept": "Each tool result is appended to the message history as a `tool_result` block, so the next request carries it and the model reasons over the new information.",
 "tested": "Loop-construction questions ask what has to happen between two iterations. The correct option appends the tool result to the conversation history before the next request; distractors hold the result only in the application's own state, leaving the next iteration to reason without it.",
 "remember": "Run the tool, append the result to the messages, then call again. Anything the next iteration must reason over has to be in the conversation history.",
 "analogy": "Every readback the controller takes goes onto the flight strip before the next instruction is issued, so the strip alone carries the picture. A detail kept in the controller's head is not on the strip, and the next decision is made without it.",
 "svg": """<rect class="tint" x="26" y="18" width="56" height="14" rx="2"/>
<rect class="tint" x="26" y="38" width="56" height="14" rx="2"/>
<rect class="tint" x="26" y="58" width="56" height="14" rx="2"/>
<rect class="acc" x="26" y="78" width="56" height="14" rx="2"/>
<path class="acc" d="M116 85 h-22 M100 80 l-6 5 6 5"/>
<rect class="tint" x="116" y="70" width="28" height="30" rx="3"/>
<path class="thin" d="M124 80 h12 M124 88 h12"/>
<text class="lbl" x="54" y="106" text-anchor="middle">msgs</text>""",
 "alt": "Message stack with the newest block accented, fed by a tool box",
},
{
 "id": "D1-03",
 "title": "Model-driven decisions, not a hard-coded decision tree",
 "concept": "In an agentic system Claude reasons from context about which tool to call next, which is what separates it from a pre-configured decision tree or fixed tool sequence.",
 "tested": "Reliability scenarios offer a deterministic front end: a routing layer that parses each request and pre-selects the tool, or a classifier that enables only a subset of tools. The official rationale calls the routing layer over-engineered because it bypasses the model's own language understanding, and the classifier a fix to tool availability rather than to the stated problem.",
 "remember": "Claude picks the next tool from context. A keyword router or pre-set sequence is the over-engineering distractor: it bypasses the model's language understanding.",
 "analogy": "The controller sequences aircraft from the picture in front of them — weather, fuel states, what is already on the runway — rather than working down an order printed that morning. A tower running the printed order would keep issuing it while the runway is blocked.",
 "svg": """<rect class="tint" x="16" y="20" width="26" height="18" rx="3"/>
<path class="thin" d="M42 29 h12 M50 25 l4 4 -4 4"/>
<rect class="tint" x="54" y="20" width="26" height="18" rx="3"/>
<path class="thin" d="M80 29 h12 M88 25 l4 4 -4 4"/>
<rect class="tint" x="92" y="20" width="26" height="18" rx="3"/>
<line class="no" x1="48" y1="16" x2="86" y2="42"/>
<line class="no" x1="86" y1="16" x2="48" y2="42"/>
<circle class="accfill" cx="66" cy="72" r="9"/>
<circle class="tint" cx="24" cy="100" r="8"/>
<circle class="tint" cx="66" cy="102" r="8"/>
<circle class="tint" cx="108" cy="100" r="8"/>
<line class="dash thin" x1="59" y1="79" x2="31" y2="93"/>
<line class="acc" x1="66" y1="81" x2="66" y2="94"/>
<line class="dash thin" x1="73" y1="79" x2="101" y2="93"/>""",
 "alt": "Fixed tool chain crossed out; a hub choosing one of three tools",
},
{
 "id": "D1-04",
 "title": "Loop-termination anti-patterns",
 "concept": "Loop termination keys on `stop_reason`; parsing natural-language signals, an arbitrary iteration cap as the primary stopping mechanism, and checking for assistant text are the named anti-patterns.",
 "tested": "A loop that runs on past the work, or stops before it, is shown and the question asks which change fixes it. The distractor family is probabilistic control where a deterministic field already exists: matching a completion phrase in the response text, or capping iterations and calling that the stopping condition. Read the cap option closely — a cap is an anti-pattern as the primary stopping mechanism.",
 "remember": "Only `stop_reason` ends the loop. Text matching, assistant-text presence and an iteration cap as the primary mechanism are the three named anti-patterns.",
 "analogy": "The strip is closed by the clearance, not by a pilot who sounds finished, and not by counting how many circuits they have flown. An aircraft on its fifth lap can still be waiting for the runway.",
 "svg": """<rect class="tint" x="14" y="16" width="40" height="16" rx="3"/>
<text class="lbl" x="34" y="28" text-anchor="middle">done</text>
<rect class="tint" x="14" y="40" width="40" height="16" rx="3"/>
<text class="lbl" x="34" y="52" text-anchor="middle">cap</text>
<rect class="tint" x="14" y="64" width="40" height="16" rx="3"/>
<text class="lbl" x="34" y="76" text-anchor="middle">text</text>
<path class="thin" d="M54 24 H66 V72 H54"/>
<path class="thin" d="M66 48 h20"/>
<line class="no" x1="82" y1="40" x2="96" y2="56"/>
<line class="no" x1="96" y1="40" x2="82" y2="56"/>
<rect class="dash" x="116" y="34" width="30" height="70" rx="3"/>
<path class="acc" d="M40 96 H112 M104 90 l8 6 -8 6"/>
<text class="lbl" x="70" y="90" text-anchor="middle">stop</text>""",
 "alt": "Three crossed-out signals; only the stop arrow reaches the exit",
},
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
{
 "id": "D1-06",
 "title": "Subagents start with an empty context",
 "concept": "A subagent does not inherit the coordinator's conversation history or share memory between invocations, so every finding it needs must be written into its prompt.",
 "tested": "The synthesis subagent produces work that ignores what search and analysis already found, and the question asks for the fix. The answer puts the complete prior findings inside the synthesis subagent's prompt. Distractors assume an inheritance that does not exist: telling the subagent to refer back to earlier results, or relying on memory shared between invocations.",
 "remember": "Nothing is inherited. Whatever the subagent must reason over goes into its prompt in full, prior agents' findings included.",
 "analogy": "A crew boarding for the next leg knows only what is on the sheet handed to them; nothing carries over from the aircraft's last flight. If the controller wants them acting on what an earlier crew reported, it goes on the sheet.",
 "svg": """<path class="tint" d="M22 100 L26 62 H38 L42 100 Z"/>
<rect class="tint" x="16" y="44" width="32" height="18" rx="4"/>
<path d="M20 44 L24 34 H40 L44 44"/>
<rect class="acc" x="58" y="40" width="24" height="30" rx="2"/>
<path class="acc thin" d="M64 50 h12 M64 60 h12"/>
<path class="acc" d="M84 55 h16 M96 50 l5 5 -5 5"/>
<path class="tint" d="M106 56 h30 l12 -6 v12 l-12 -6"/>
<path d="M118 56 l-8 -14 h8 l12 14 M118 56 l-8 14 h8 l12 -14"/>
<rect class="dash" x="104" y="84" width="46" height="20" rx="2"/>
<line class="dash thin" x1="48" y1="86" x2="100" y2="94"/>
<line class="no" x1="68" y1="84" x2="80" y2="96"/>
<line class="no" x1="80" y1="84" x2="68" y2="96"/>""",
 "alt": "Tower hands a written sheet to a plane; inherited history crossed out",
},
{
 "id": "D1-07",
 "title": "The coordinator decomposes, delegates, aggregates — and chooses",
 "concept": "The coordinator decomposes the task, decides which subagents this query needs, delegates to them and aggregates their results rather than routing every query through the full pipeline.",
 "tested": "A design question asks what the coordinator is responsible for, or how to stop a system running every subagent on every query. The answer has the coordinator analyse the request and select the subagents it needs; distractors move that choice elsewhere, putting a routing model in front, or leave the full pipeline in place and optimise the subagents instead.",
 "remember": "Four coordinator jobs: decompose, delegate, aggregate, and choose which subagents this query needs. Always running the full pipeline is the distractor.",
 "analogy": "The controller reads what the request needs and calls only the positions involved — one aircraft for a routine arrival, several for an unfolding situation. Working every position on every movement would fill the frequency without improving the outcome.",
 "svg": """<circle class="accfill" cx="28" cy="58" r="10"/>
<circle class="tint" cx="82" cy="22" r="9"/>
<circle class="tint" cx="82" cy="58" r="9"/>
<circle class="dash" cx="82" cy="94" r="9"/>
<line class="acc" x1="37" y1="53" x2="73" y2="28"/>
<line class="acc" x1="38" y1="58" x2="73" y2="58"/>
<line class="dash thin" x1="37" y1="64" x2="73" y2="89"/>
<path d="M91 26 L114 50"/>
<path d="M91 58 h23"/>
<rect class="tint" x="116" y="44" width="30" height="28" rx="3"/>
<path class="thin" d="M124 54 h14 M124 62 h14"/>""",
 "alt": "Coordinator calls two of three subagents and merges their results",
},
{
 "id": "D1-08",
 "title": "Narrow decomposition leaves coverage gaps",
 "concept": "When every subagent succeeds and the output still misses whole parts of the topic, the cause is the coordinator's task decomposition rather than subagent performance.",
 "tested": "The stem states that each subagent completed successfully, quotes the coordinator's log showing three subtasks drawn from one corner of the topic, and asks for the most likely root cause. The correct option names the coordinator's decomposition; the three distractors blame downstream agents that worked correctly inside the scope they were given.",
 "remember": "All subagents succeed, coverage is still partial → look at the coordinator's decomposition. Blaming search quality, synthesis gap-detection or analysis filters blames agents that did their job.",
 "analogy": "Three aircraft are sent to search, and all three fly their assigned boxes exactly, but every box was drawn in the same corner of the sea. The gap is in the plan on the controller's table, not in the flying.",
 "svg": """<circle class="dash" cx="80" cy="60" r="42"/>
<circle class="thin" cx="80" cy="60" r="24"/>
<line class="thin" x1="80" y1="18" x2="80" y2="102"/>
<line class="thin" x1="38" y1="60" x2="122" y2="60"/>
<path class="acc" d="M80 60 L80 18 A42 42 0 0 1 122 60 Z"/>
<circle class="accfill" cx="92" cy="34" r="3"/>
<circle class="accfill" cx="104" cy="46" r="3"/>
<circle class="accfill" cx="97" cy="55" r="3"/>""",
 "alt": "Radar circle with all three markers inside one quadrant",
},
{
 "id": "D1-09",
 "title": "Partition scope so subagents do not duplicate work",
 "concept": "The coordinator partitions the research space before delegating, assigning each subagent a distinct subtopic or source type.",
 "tested": "Two subagents come back with overlapping findings and the question asks for the fix. The answer partitions the scope up front, one distinct subtopic or source type per agent. The distractor deduplicates the results after the fact, which leaves the same ground covered twice.",
 "remember": "One distinct subtopic or source type per subagent, assigned before delegation. Deduplicating afterwards is the distractor: the tokens are already spent.",
 "analogy": "The controller divides the search area into sectors and gives each crew one, so two aircraft never sweep the same water. Sorting out the overlap after everyone has landed does not buy back the fuel.",
 "svg": """<rect class="tint" x="14" y="30" width="56" height="60" rx="3"/>
<line class="thin" x1="14" y1="50" x2="70" y2="50"/>
<line class="thin" x1="14" y1="70" x2="70" y2="70"/>
<circle class="accfill" cx="42" cy="40" r="4"/>
<circle class="accfill" cx="42" cy="60" r="4"/>
<circle class="accfill" cx="42" cy="80" r="4"/>
<circle class="dash" cx="106" cy="52" r="20"/>
<circle class="dash" cx="126" cy="66" r="20"/>
<line class="no" x1="108" y1="52" x2="124" y2="66"/>
<line class="no" x1="124" y1="52" x2="108" y2="66"/>""",
 "alt": "Three separated sectors each with one marker; overlapping circles crossed out",
},
{
 "id": "D1-10",
 "title": "Iterative refinement: evaluate, re-delegate, re-synthesise",
 "concept": "The coordinator evaluates the synthesis output for gaps, re-delegates targeted queries to the search and analysis subagents, and re-invokes synthesis until coverage is sufficient.",
 "tested": "A synthesis comes back with coverage gaps and the question asks what the architecture should do. The answer keeps gap evaluation with the coordinator, which sends targeted follow-up queries and re-runs synthesis. Distractors hand the synthesis agent its own search tools, breaking least privilege, or ship the report with a note that further research is needed.",
 "remember": "Gap evaluation belongs to the coordinator: re-delegate, re-invoke synthesis, stop on a coverage criterion. Handing synthesis the full search toolset is the distractor; one scoped lookup tool is not (D2-08).",
 "analogy": "The controller reads the picture that comes back, sees the stretch nobody covered, and sends one aircraft to that stretch rather than re-flying the whole task. The picture is rebuilt with the new returns, and the cycle ends when the controller's own criteria are met.",
 "svg": """<rect class="paper" x="40" y="16" width="60" height="32" rx="3"/>
<path class="thin" d="M48 28 h44 M48 38 h24"/>
<rect class="acc dash" x="76" y="33" width="18" height="10" rx="2"/>
<path d="M70 48 v22 M65 64 l5 6 5 -6"/>
<circle class="accfill" cx="70" cy="82" r="10"/>
<path class="acc" d="M80 82 h34 M108 77 l6 5 -6 5"/>
<circle class="tint" cx="126" cy="82" r="10"/>
<path class="acc" d="M126 72 V32 h-26 M106 27 l-6 5 6 5"/>""",
 "alt": "Synthesis with a gap sent back through the coordinator for a targeted query",
},
{
 "id": "D1-11",
 "title": "Task tool + allowedTools includes \"Task\"",
 "concept": "Subagents are spawned with the `Task` tool, and a coordinator can invoke them only if `\"Task\"` is present in its `allowedTools`.",
 "tested": "A coordinator attempts everything itself instead of delegating, and the question asks the cause or the change to make. The answer checks the coordinator's `allowedTools` for `\"Task\"`. Distractors rewrite the system prompt to instruct it to delegate, or add subagent descriptions to that prompt, neither of which grants a tool the configuration withholds.",
 "remember": "No `\"Task\"` in `allowedTools`, no delegation. A prompt cannot grant a tool the configuration withholds, and descriptions spawn nothing on their own.",
 "analogy": "A controller who has not been given the frequency cannot call the aircraft, however firmly the operations manual says to delegate. The instruction is in the book; the capability is in the equipment.",
 "svg": """<rect class="tint" x="14" y="26" width="56" height="66" rx="3"/>
<path class="thin" d="M22 42 h40 M22 76 h40"/>
<rect class="acc" x="20" y="52" width="44" height="14" rx="2"/>
<text class="lbl" x="42" y="63" text-anchor="middle">Task</text>
<path class="acc" d="M70 59 h20"/>
<path class="thin" d="M90 59 L103 36 M90 59 h13 M90 59 L103 82"/>
<circle class="tint" cx="112" cy="34" r="9"/>
<circle class="tint" cx="112" cy="60" r="9"/>
<circle class="tint" cx="112" cy="84" r="9"/>""",
 "alt": "Tool list with Task highlighted, fanning out to three subagents",
},
{
 "id": "D1-12",
 "title": "AgentDefinition: description, system prompt, tool restrictions",
 "concept": "An `AgentDefinition` configures each subagent type with a description, its own system prompt and the set of tools it is allowed to use.",
 "tested": "A question asks where a subagent type's behaviour and tool scope are configured, or offers a wider tool set for flexibility. The three levers sit in the `AgentDefinition`: description, system prompt, tool restrictions. Handing every subagent type the full set is the over-provisioning distractor, since restriction per type is how separation of responsibilities and least privilege are enforced.",
 "remember": "One definition per subagent type, three levers: description, system prompt, tool restrictions. Restricting tools per type is the least-privilege mechanism, not a limit to work around.",
 "analogy": "Every position in the tower is defined the same way: what it handles, how it is to be worked, and which frequencies and switches it may touch. Handing every position every switch removes the reason for having separate positions.",
 "svg": """<rect class="paper" x="30" y="16" width="76" height="88" rx="3"/>
<line class="thin" x1="38" y1="30" x2="98" y2="30"/>
<text class="lbl" x="38" y="46">desc</text>
<line class="thin" x1="38" y1="52" x2="98" y2="52"/>
<text class="lbl" x="38" y="68">sys</text>
<line class="thin" x1="38" y1="74" x2="98" y2="74"/>
<rect class="acc" x="38" y="80" width="60" height="16" rx="2"/>
<text class="lbl" x="68" y="92" text-anchor="middle">tools</text>
<circle class="acc" cx="122" cy="88" r="7"/>
<path class="acc" d="M129 88 h16 M141 88 v6"/>""",
 "alt": "Definition card with description, system prompt and an accented tools field",
},
{
 "id": "D1-13",
 "title": "Content and metadata travel in separate fields",
 "concept": "Findings passed between agents use a structured format that keeps content in one field and metadata — source URL, document name, page number — in another, so attribution survives aggregation.",
 "tested": "The final report carries claims whose citations are missing or attached to the wrong source, and the question asks the root cause or the fix. Content and metadata were passed as merged free text, so the fix is a structured format that separates them. Distractors tell the synthesis agent to remember to cite, which it cannot do from metadata it never received, or send an agent back to the web to find sources for finished claims.",
 "remember": "Claim in one field; source URL, document name and page number in another. A prompt to cite properly cannot recover metadata that was never passed.",
 "analogy": "Each contact goes onto the strip in its own boxes — callsign, level, squawk — so the next controller can read any one of them on its own. A single scribbled line holds the same words and loses which is which.",
 "svg": """<rect class="paper" x="14" y="24" width="60" height="72" rx="3"/>
<rect class="tint" x="22" y="34" width="44" height="22" rx="2"/>
<rect class="acc" x="22" y="62" width="44" height="10" rx="2"/>
<rect class="acc" x="22" y="78" width="44" height="10" rx="2"/>
<text class="lbl" x="44" y="106" text-anchor="middle">meta</text>
<rect class="dash" x="94" y="34" width="52" height="52" rx="3"/>
<path class="thin" d="M102 46 h36 M102 56 h36 M102 66 h36 M102 76 h20"/>
<line class="no" x1="110" y1="50" x2="130" y2="70"/>
<line class="no" x1="130" y1="50" x2="110" y2="70"/>""",
 "alt": "Record with content above two accented metadata fields; merged blob crossed out",
},
]
