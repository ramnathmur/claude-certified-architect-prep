# Domain 5 part A — Context Management & Reliability · building: the hospital ward

ITEMS = [
{
 "id": "D5-01",
 "title": "Keep a case-facts block outside the summary",
 "concept": "Amounts, percentages, dates, order numbers and statuses are extracted into a persistent case-facts block included in every prompt, outside the summarised history, so compression cannot blur them.",
 "tested": "After a long support conversation the agent quotes a discount or refund amount that no longer matches what the customer was promised, and the question asks which change preserves precision. Extracting the transactional facts into a case-facts block sent outside the summarised history is the answer; the distractors revise the summarisation prompt to preserve numbers or raise the summarisation threshold, and both still route the amounts through compression.",
 "remember": "Precise numbers live outside summarisation, in a case-facts block sent every turn. A better summarisation prompt still depends on the summariser executing perfectly.",
 "analogy": "The shift summary says the patient is comfortable and improving; the chart at the foot of the bed still carries the dose, the time it was given and the allergy. Every handover rewrites the summary, and the chart is carried across untouched.",
 "svg": """<rect class="dash" x="10" y="26" width="38" height="54" rx="2"/>
<path class="thin" d="M16 42 q5 -5 10 0 t10 0 M16 54 q5 -5 10 0 t10 0 M16 66 h20"/>
<rect class="tint" x="58" y="70" width="84" height="22" rx="4"/>
<rect x="58" y="52" width="9" height="40"/>
<path d="M66 92 v10 M136 92 v10"/>
<rect class="acc" x="100" y="20" width="46" height="34" rx="2"/>
<rect class="thin" x="116" y="14" width="14" height="6" rx="1"/>
<text class="lbl" x="123" y="42" text-anchor="middle">89.99</text>
<line class="thin" x1="123" y1="54" x2="123" y2="70"/>
<line class="dash thin" x1="96" y1="36" x2="52" y2="40"/>
<line class="no" x1="66" y1="30" x2="82" y2="46"/>
<line class="no" x1="82" y1="30" x2="66" y2="46"/>""",
 "alt": "Chart clipboard reading 89.99; its route into the blurred summary crossed out",
},
{
 "id": "D5-02",
 "title": "Lost in the middle: summary first, headers throughout",
 "concept": "Models process the beginning and end of long inputs reliably and may omit findings from middle sections, so key findings go at the start and the detail carries explicit section headers.",
 "tested": "A synthesis agent reads a large aggregated input and its report reflects the opening and closing material while findings from the middle are missing; the question asks the mitigation. A key-findings summary at the start plus explicit section headers is the answer, against rotating which agent's output appears first, which leaves the attention pattern unchanged, and compressing everything under a token target, which can drop critical information.",
 "remember": "Beginning and end are read reliably. Key findings at the top, explicit section headers throughout. Rotation and blanket compression are the distractors.",
 "analogy": "The ward round starts at the summary board, and what is written there is what the team carries to every bed. Findings buried in the middle of a long file get skimmed, so they are moved to the board and each part of the file is given a heading.",
 "svg": """<rect class="acc" x="24" y="10" width="80" height="18" rx="2"/>
<text class="lbl" x="64" y="23" text-anchor="middle">key</text>
<rect class="tint" x="24" y="34" width="80" height="74" rx="2"/>
<rect class="accfill" x="30" y="40" width="6" height="6"/>
<line x1="42" y1="43" x2="96" y2="43"/>
<line class="thin" x1="30" y1="53" x2="88" y2="53"/>
<line class="thin" opacity="0.35" x1="30" y1="63" x2="96" y2="63"/>
<line class="thin" opacity="0.35" x1="30" y1="71" x2="86" y2="71"/>
<line class="thin" opacity="0.35" x1="30" y1="79" x2="92" y2="79"/>
<rect class="accfill" x="30" y="86" width="6" height="6"/>
<line x1="42" y1="89" x2="96" y2="89"/>
<line class="thin" x1="30" y1="99" x2="88" y2="99"/>
<line class="acc" x1="114" y1="43" x2="128" y2="43"/>
<line class="dash thin" x1="114" y1="71" x2="128" y2="71"/>
<line class="acc" x1="114" y1="89" x2="128" y2="89"/>""",
 "alt": "Long file with a faint middle; key-findings board pinned at the top",
},
{
 "id": "D5-03",
 "title": "Trim tool output before it enters context",
 "concept": "Tool results accumulate in context and consume tokens out of proportion to their relevance, so a lookup returning forty-plus fields is cut to the five the task needs before it lands.",
 "tested": "Long multi-issue sessions fill with order lookups returning forty-plus fields when five matter, and the question asks how to conserve context. Trimming tool output to the relevant fields before it accumulates is the answer; distractors instruct the model to ignore the irrelevant fields, which still pays the tokens, or summarise the conversation harder, which treats the symptom while the verbose results keep arriving.",
 "remember": "Trim at the source, before the result enters context. Telling the model to ignore fields still spends the tokens; heavier summarisation leaves the flood in place.",
 "analogy": "A full lab panel prints forty values and today's decision turns on five of them. The chart carries those five, because filing the whole panel at every review buries the lines anyone will read.",
 "svg": """<rect class="tint" x="12" y="18" width="46" height="88" rx="2"/>
<text class="lbl" x="35" y="34" text-anchor="middle">40</text>
<line class="thin" x1="18" y1="44" x2="52" y2="44"/>
<line class="thin" x1="18" y1="52" x2="52" y2="52"/>
<line class="thin" x1="18" y1="60" x2="52" y2="60"/>
<line class="thin" x1="18" y1="68" x2="52" y2="68"/>
<line class="thin" x1="18" y1="76" x2="52" y2="76"/>
<line class="thin" x1="18" y1="84" x2="52" y2="84"/>
<line class="thin" x1="18" y1="92" x2="52" y2="92"/>
<line class="thin" x1="18" y1="100" x2="52" y2="100"/>
<path d="M64 62 h18 M76 56 l6 6 -6 6"/>
<rect class="paper" x="94" y="32" width="48" height="62" rx="2"/>
<text class="lbl" x="118" y="48" text-anchor="middle">5</text>
<line class="acc" x1="100" y1="58" x2="136" y2="58"/>
<line class="acc" x1="100" y1="66" x2="136" y2="66"/>
<line class="acc" x1="100" y1="74" x2="136" y2="74"/>
<line class="acc" x1="100" y1="82" x2="136" y2="82"/>
<line class="acc" x1="100" y1="90" x2="136" y2="90"/>""",
 "alt": "Forty-row lab panel trimmed to five relevant lines",
},
{
 "id": "D5-04",
 "title": "The API is stateless: resend the history",
 "concept": "Claude holds no server-side memory between requests, so conversational coherence comes from the application passing the complete prior conversation in the `messages` array of each new request.",
 "tested": "A user states a preference in turn one and the agent asks for it again two turns later, or the same history is re-sent on every turn and the question asks the root cause. The stateless API is the answer: the application must include prior messages, and every request re-sends them. Distractors invent a `session_id` parameter or reach for a vector database, which serves retrieval over months of history rather than ordinary multi-turn memory.",
 "remember": "No server-side memory. Memory is the `messages` array you send. There is no `session_id`, and ordinary multi-turn conversation needs no vector database.",
 "analogy": "A locum takes the ward round each shift and has never met anyone in the beds. Whatever the folder handed over contains is what is known, and nothing carries over in anyone's head.",
 "svg": """<rect class="tint" x="10" y="14" width="52" height="20" rx="2"/>
<line class="thin" x1="16" y1="24" x2="36" y2="24"/>
<rect class="tint" x="10" y="42" width="52" height="28" rx="2"/>
<line class="thin" x1="16" y1="52" x2="36" y2="52"/>
<line class="thin" x1="16" y1="62" x2="46" y2="62"/>
<rect class="acc" x="10" y="78" width="52" height="34" rx="2"/>
<line class="thin" x1="16" y1="88" x2="36" y2="88"/>
<line class="thin" x1="16" y1="98" x2="46" y2="98"/>
<line class="thin" x1="16" y1="106" x2="52" y2="106"/>
<path d="M70 56 h16 M80 50 l6 6 -6 6"/>
<rect class="tint" x="94" y="34" width="52" height="36" rx="3"/>
<text class="lbl" x="120" y="56" text-anchor="middle">API</text>
<line class="dash thin" x1="120" y1="70" x2="120" y2="84"/>
<rect class="dash" x="100" y="84" width="40" height="20" rx="10"/>
<line class="no" x1="104" y1="86" x2="136" y2="102"/>
<line class="no" x1="136" y1="86" x2="104" y2="102"/>""",
 "alt": "Three requests each resending the whole history; a memory store crossed out",
},
{
 "id": "D5-05",
 "title": "Subagents return structured findings, not prose",
 "concept": "Subagents return key facts, citations, relevance scores and metadata such as dates, source locations and methodological context in structured outputs, rather than verbose content and reasoning chains.",
 "tested": "Combined subagent output far exceeds what the downstream agent's context budget allows, or the synthesis loses the context needed to interpret a finding, and the question asks where to fix it. Changing the upstream agents to emit structured data with metadata is the answer; the distractor inserts an intermediate summarisation agent, which adds a stage and another point of failure without addressing the source.",
 "remember": "Fix the output format upstream: key facts, citations, relevance scores, dates and source locations. An extra summarisation stage treats the volume rather than its cause.",
 "analogy": "A handover that says she is fine leaves the next doctor to reconstruct everything. The ward's handover form has a field for the finding, when it was measured and who recorded it, which is what makes the next shift's decisions safe.",
 "svg": """<rect class="dash" x="10" y="28" width="46" height="60" rx="2"/>
<path class="thin" d="M16 44 q5 -5 10 0 t10 0 M16 56 q5 -5 10 0 t10 0 M16 68 q5 -5 10 0 t10 0"/>
<line class="no" x1="16" y1="34" x2="50" y2="82"/>
<line class="no" x1="50" y1="34" x2="16" y2="82"/>
<path d="M64 58 h18 M76 52 l6 6 -6 6"/>
<rect class="paper" x="92" y="18" width="54" height="82" rx="2"/>
<rect class="accfill" x="98" y="28" width="6" height="6"/>
<line class="acc" x1="110" y1="31" x2="140" y2="31"/>
<rect class="accfill" x="98" y="46" width="6" height="6"/>
<line class="acc" x1="110" y1="49" x2="140" y2="49"/>
<rect class="accfill" x="98" y="64" width="6" height="6"/>
<line class="acc" x1="110" y1="67" x2="134" y2="67"/>
<rect class="accfill" x="98" y="82" width="6" height="6"/>
<line class="acc" x1="110" y1="85" x2="140" y2="85"/>""",
 "alt": "Rambling page crossed out beside a structured handover form with labelled fields",
},
{
 "id": "D5-06",
 "title": "Behavioural drift is dilution, not overflow",
 "concept": "When system-prompt behaviour degrades after a handful of turns at around 2,500 tokens, the cause is accumulated assistant responses diluting the instruction rather than a full context window.",
 "tested": "An agent stops following a system-prompt rule by the seventh turn while the conversation totals about 2,500 tokens, and the question asks the root cause. Accumulated responses diluting the system prompt is the answer; context-window overflow is impossible at that size, and the claim that the system prompt applies only to the first turn is false, since it is included in every request.",
 "remember": "Small token count plus fading rule-following means dilution, not overflow. The system prompt is sent every request, and it competes with everything accumulated after it.",
 "analogy": "The protocol notice is still pinned by the door, unchanged, but after seven pages of the team's own notes it is one line among many that the reader passes. The folder is nowhere near full; the notice has been outnumbered.",
 "svg": """<rect class="dash" x="10" y="14" width="58" height="92" rx="3"/>
<rect class="tint" x="14" y="86" width="50" height="16" rx="2"/>
<text class="lbl" x="39" y="76" text-anchor="middle">2.5K</text>
<line class="no" x1="50" y1="20" x2="66" y2="36"/>
<line class="no" x1="66" y1="20" x2="50" y2="36"/>
<line class="acc" x1="84" y1="20" x2="148" y2="20"/>
<line class="thin" x1="84" y1="32" x2="148" y2="32"/>
<line class="thin" x1="84" y1="44" x2="148" y2="44"/>
<line class="thin" x1="84" y1="56" x2="148" y2="56"/>
<line class="thin" x1="84" y1="68" x2="148" y2="68"/>
<line class="thin" x1="84" y1="80" x2="148" y2="80"/>
<line class="thin" x1="84" y1="92" x2="148" y2="92"/>
<line class="thin" x1="84" y1="104" x2="148" y2="104"/>""",
 "alt": "Barely filled window crossed out; one accent line among many later notes",
},
{
 "id": "D5-07",
 "title": "Months of history need retrieval, not summarisation",
 "concept": "Recalling a specific past exchange from months of conversation, around 85K tokens, calls for semantic embeddings with retrieval, because progressive summarisation compresses those conclusions into abstractions.",
 "tested": "The question asks what was concluded about a particular point weeks earlier, across a history of about 85K tokens, and the design decision is how the system should recall it. Semantic retrieval over the stored exchanges is the answer; progressive summarisation is the distractor, since the specific conclusion is what compression removes.",
 "remember": "Specific recall from months of history → retrieve the actual exchange; summarisation keeps the gist and loses the sentence being asked about. How retrieval is built is out of scope.",
 "analogy": "The archive holds every clinic letter from the past three months, and the question is what the cardiologist concluded in March. The March letter is pulled and read; a discharge summary recording that a cardiac review took place cannot answer it.",
 "svg": """<rect class="tint" x="10" y="58" width="76" height="46" rx="3"/>
<text class="lbl" x="14" y="24">85K</text>
<line class="thin" x1="20" y1="66" x2="20" y2="98"/>
<line class="thin" x1="30" y1="66" x2="30" y2="98"/>
<line class="thin" x1="40" y1="66" x2="40" y2="98"/>
<line class="thin" x1="62" y1="66" x2="62" y2="98"/>
<line class="thin" x1="72" y1="66" x2="72" y2="98"/>
<rect class="acc paper" x="44" y="20" width="16" height="34" rx="1" transform="rotate(-8 52 37)"/>
<line class="acc thin" x1="52" y1="56" x2="52" y2="64"/>
<rect class="dash" x="96" y="36" width="48" height="54" rx="2"/>
<path class="thin" d="M102 50 q5 -5 10 0 t10 0 M102 62 q5 -5 10 0 t10 0 M102 74 h20"/>
<line class="no" x1="102" y1="42" x2="138" y2="84"/>
<line class="no" x1="138" y1="42" x2="102" y2="84"/>""",
 "alt": "One record pulled from an 85K archive; blurred summary page crossed out",
},
{
 "id": "D5-08",
 "title": "Escalate on request, policy gap, or stalled progress",
 "concept": "The escalation triggers are an explicit customer request for a human, a policy exception or gap where policy is silent or ambiguous, and inability to make meaningful progress.",
 "tested": "A customer asks for something policy does not address, such as matching a competitor's price when policy covers only the company's own adjustments, and the question asks what the agent should do. Escalation is the answer, on the ground that policy is silent rather than that the case is hard; distractors improvise a decision from adjacent policy or treat complexity on its own as the trigger.",
 "remember": "Three structural triggers: they asked for a human, policy is silent or ambiguous, progress has stalled. Difficulty on its own is not one of them.",
 "analogy": "The ward calls the consultant on written triggers: the patient asks for one, the protocol does not cover this presentation, or the plan has stopped moving. A demanding case is not on that list, and neither is a junior finding it uncomfortable.",
 "svg": """<rect class="paper" x="10" y="16" width="74" height="60" rx="2"/>
<rect class="thin" x="16" y="24" width="8" height="8"/>
<path class="acc" d="M18 28 l3 3 l5 -6"/>
<line class="thin" x1="30" y1="28" x2="76" y2="28"/>
<rect class="thin" x="16" y="42" width="8" height="8"/>
<path class="acc" d="M18 46 l3 3 l5 -6"/>
<line class="thin" x1="30" y1="46" x2="76" y2="46"/>
<rect class="thin" x="16" y="60" width="8" height="8"/>
<path class="acc" d="M18 64 l3 3 l5 -6"/>
<line class="thin" x1="30" y1="64" x2="76" y2="64"/>
<line class="dash thin" x1="30" y1="90" x2="76" y2="90"/>
<line class="no" x1="40" y1="82" x2="56" y2="98"/>
<line class="no" x1="56" y1="82" x2="40" y2="98"/>
<path class="acc" d="M92 46 h16 M102 40 l6 6 -6 6"/>
<circle cx="128" cy="34" r="9"/>
<path d="M128 43 v20 M116 50 h24 M120 78 l8 -15 M136 78 l-8 -15"/>""",
 "alt": "Three ticked escalation criteria; a vague fourth trigger crossed out",
},
{
 "id": "D5-09",
 "title": "Explicit criteria with examples, not sentiment or self-confidence",
 "concept": "Escalation calibration comes from explicit criteria in the system prompt with few-shot examples of when to escalate and when to resolve, because sentiment and self-reported confidence do not track case complexity.",
 "tested": "An agent escalates straightforward cases while attempting the ones that need policy exceptions, and the question asks the most effective way to improve escalation calibration. Explicit criteria with few-shot examples is the answer; a self-reported confidence score fails because the agent is already confidently wrong on the hard cases, sentiment analysis addresses a different problem, and a separately trained classifier is over-engineering before prompt work has been tried.",
 "remember": "Unclear decision boundaries are fixed with written criteria plus worked examples. Self-rated confidence is uncalibrated, mood does not track complexity, and a trained classifier is premature.",
 "analogy": "The consultant is called on written criteria with worked examples of calls that were right and calls that were not. How distressed the patient sounds, and how sure the junior feels, are not the trigger.",
 "svg": """<rect class="paper" x="10" y="14" width="70" height="92" rx="2"/>
<line class="acc" x1="18" y1="28" x2="72" y2="28"/>
<rect class="thin" x="18" y="40" width="20" height="14" rx="2"/>
<path d="M42 47 h10 M48 43 l4 4 -4 4"/>
<rect class="acc thin" x="56" y="40" width="16" height="14" rx="2"/>
<rect class="thin" x="18" y="66" width="20" height="14" rx="2"/>
<path d="M42 73 h10 M48 69 l4 4 -4 4"/>
<rect class="acc thin" x="56" y="66" width="16" height="14" rx="2"/>
<line class="thin" x1="18" y1="94" x2="64" y2="94"/>
<circle cx="114" cy="34" r="15"/>
<path class="thin" d="M108 29 v3 M120 29 v3 M107 43 q7 -6 14 0"/>
<line class="no" x1="124" y1="40" x2="138" y2="54"/>
<line class="no" x1="138" y1="40" x2="124" y2="54"/>
<circle cx="114" cy="84" r="15"/>
<path class="thin" d="M100 86 a14 14 0 0 1 28 0 M114 86 l9 -7"/>
<line class="no" x1="124" y1="90" x2="138" y2="104"/>
<line class="no" x1="138" y1="90" x2="124" y2="104"/>""",
 "alt": "Criteria card with worked examples; mood face and confidence dial crossed out",
},
{
 "id": "D5-10",
 "title": "Explicit request escalates now; frustration gets an offer",
 "concept": "An explicit request for a human is honoured immediately without first attempting investigation, while frustration over a solvable issue gets acknowledgement and an offer, escalating only if the customer reiterates.",
 "tested": "One message demands a manager and another vents about a problem the agent can fix, and the question asks how each should be handled. The demand is escalated at once with no investigation first; the frustration is acknowledged and answered with a concrete resolution, and escalated when the customer repeats the request. Distractors attempt a fix before honouring the explicit request, or escalate at the first sign of dissatisfaction.",
 "remember": "Asked for a human → escalate now, no investigation first. Frustrated about something solvable → acknowledge, offer the fix, escalate if they ask again.",
 "analogy": "A patient who asks to see the consultant is referred straight away, without the ward first trying to talk them round. A patient upset about a delay the ward can fix is heard out and offered the fix, and referred if they ask again.",
 "svg": """<path class="tint" d="M10 12 h56 v24 h-42 l-8 8 v-8 h-6 z"/>
<text class="lbl" x="36" y="29" text-anchor="middle">human</text>
<path class="acc" d="M72 26 h22 M86 20 l6 6 -6 6"/>
<circle cx="118" cy="14" r="8"/>
<path d="M118 22 v14 M108 28 h20 M112 50 l6 -14 M124 50 l-6 -14"/>
<path class="tint" d="M10 60 h46 v24 h-32 l-8 8 v-8 h-6 z"/>
<path class="thin" d="M18 78 l6 -10 l5 10 l6 -10 l5 10"/>
<path d="M60 74 h16 M68 68 l6 6 -6 6"/>
<rect class="paper" x="80" y="58" width="30" height="32" rx="2"/>
<path class="acc" d="M86 74 l5 5 l10 -12"/>
<line class="dash thin" x1="114" y1="74" x2="126" y2="74"/>
<circle class="dash" cx="138" cy="74" r="9"/>""",
 "alt": "Human request goes straight to the consultant; frustration gets an offer first",
},
{
 "id": "D5-11",
 "title": "Two matches: ask for another identifier",
 "concept": "When a lookup returns multiple matching customers the agent asks for an additional identifier such as an email or order number, rather than selecting a match by heuristic.",
 "tested": "A name search returns several accounts and the question asks what the agent should do next. Requesting another identifier is the answer; distractors take the most recently active account or the first result the tool returned, both of which risk actioning the wrong customer, while escalating to a human is heavier than an ambiguity a question resolves.",
 "remember": "Multiple matches → ask for one more identifier. Most recent and first-in-list are heuristics, and escalation is more than this ambiguity needs.",
 "analogy": "Two patients on the ward share a surname, so nothing is given until the wristband is checked against a second detail. Choosing the one whose notes are nearest to hand is how the wrong person gets treated.",
 "svg": """<rect class="tint" x="10" y="18" width="54" height="20" rx="10"/>
<text class="lbl" x="37" y="32" text-anchor="middle">J Lee</text>
<rect class="tint" x="10" y="60" width="54" height="20" rx="10"/>
<text class="lbl" x="37" y="74" text-anchor="middle">J Lee</text>
<path class="dash thin" d="M88 28 h-16 M78 24 l-6 4 6 4"/>
<line class="no" x1="72" y1="20" x2="88" y2="36"/>
<line class="no" x1="88" y1="20" x2="72" y2="36"/>
<rect class="acc" x="92" y="52" width="52" height="32" rx="3"/>
<text class="lbl" x="118" y="72" text-anchor="middle">DOB?</text>
<line class="acc thin" x1="92" y1="60" x2="66" y2="40"/>
<line class="acc thin" x1="92" y1="76" x2="66" y2="72"/>""",
 "alt": "Two identical wristbands; picking one crossed out, an identifier requested instead",
},
{
 "id": "D5-12",
 "title": "State assumptions and proceed on a vague request",
 "concept": "For a vague request the effective response proceeds on reasonable assumptions that are stated in the reply and open to correction.",
 "tested": "A request arrives underspecified and the question asks how the agent should handle it. Proceeding on stated assumptions with an invitation to correct them is the answer; a wall of clarifying questions drives people to abandon the interaction, and defaults applied silently leave them puzzled when the output does not match what they meant.",
 "remember": "Say what you assumed, do the work, invite correction. This is an underspecified task request; when a tool returns several possible customers, the guide's answer is to ask for one more identifier instead (D5-11).",
 "analogy": "A request for the usual discharge paperwork does not say which template is meant. The ward notes which one it has assumed, prepares it, and flags the assumption for correction, rather than returning a questionnaire and waiting. Where the doubt is which patient is meant, the wristband is checked instead.",
 "svg": """<rect class="dash" x="10" y="24" width="46" height="64" rx="2"/>
<text class="lbl" x="33" y="44" text-anchor="middle">?</text>
<line class="thin" x1="18" y1="56" x2="48" y2="56"/>
<line class="thin" x1="18" y1="66" x2="48" y2="66"/>
<line class="thin" x1="18" y1="76" x2="48" y2="76"/>
<line class="no" x1="16" y1="30" x2="50" y2="82"/>
<line class="no" x1="50" y1="30" x2="16" y2="82"/>
<path d="M62 56 h16 M70 50 l6 6 -6 6"/>
<rect class="paper" x="86" y="24" width="58" height="62" rx="2"/>
<line class="acc" x1="94" y1="38" x2="136" y2="38"/>
<line class="acc" x1="94" y1="50" x2="130" y2="50"/>
<line class="thin" x1="94" y1="62" x2="136" y2="62"/>
<line class="thin" x1="94" y1="74" x2="124" y2="74"/>
<path class="acc" d="M112 94 h20 M126 88 l6 6 -6 6"/>""",
 "alt": "Four-question form crossed out; note of stated assumptions, work continuing",
},
{
 "id": "D5-13",
 "title": "Structured error context enables coordinator recovery",
 "concept": "A failing subagent returns structured error context — the failure type, the query attempted, any partial results and potential alternatives — so the coordinator can choose how to recover.",
 "tested": "The web search subagent times out and the question asks which error propagation approach best enables intelligent recovery. Structured error context is the answer; a generic status such as search unavailable after retries hides what the coordinator needs, returning an empty result set marked successful suppresses the failure, and propagating the exception to a top-level handler terminates the whole workflow while recovery was still available.",
 "remember": "Failure type, attempted query, partial results, alternatives. A bare status leaves only retry or abort; silent success and whole-workflow termination are both anti-patterns.",
 "analogy": "A specimen that could not be processed comes back with the reason, which test was attempted, what was salvageable and what could be run instead. A slip that says unavailable leaves the ward to repeat everything or drop the investigation.",
 "svg": """<rect class="paper" x="10" y="14" width="64" height="90" rx="2"/>
<rect class="accfill" x="18" y="26" width="6" height="6"/>
<line class="acc" x1="30" y1="29" x2="66" y2="29"/>
<rect class="accfill" x="18" y="46" width="6" height="6"/>
<line class="acc" x1="30" y1="49" x2="66" y2="49"/>
<rect class="accfill" x="18" y="66" width="6" height="6"/>
<line class="acc" x1="30" y1="69" x2="60" y2="69"/>
<rect class="accfill" x="18" y="86" width="6" height="6"/>
<line class="acc" x1="30" y1="89" x2="66" y2="89"/>
<path class="acc" d="M80 40 h18 M92 34 l6 6 -6 6"/>
<circle cx="126" cy="22" r="9"/>
<path d="M126 31 v14 M116 37 h20 M120 58 l6 -13 M132 58 l-6 -13"/>
<text class="lbl" x="124" y="72" text-anchor="middle">fail</text>
<rect class="dash" x="102" y="78" width="44" height="24" rx="3"/>
<line class="no" x1="108" y1="82" x2="140" y2="98"/>
<line class="no" x1="140" y1="82" x2="108" y2="98"/>""",
 "alt": "Handover slip with four labelled fields; a bare fail tag crossed out",
},
{
 "id": "D5-14",
 "title": "Access failure is not an empty result",
 "concept": "A timeout is an access failure needing a retry decision while zero matches is a successful query, and error reporting distinguishes the two so the coordinator can decide appropriately.",
 "tested": "A tool returns nothing and the question turns on whether that is a failure or an answer. Reporting them differently is the answer: an empty result is a valid outcome the workflow can proceed on, while a timeout carries a retry decision. Distractors collapse both into one error status, or mark a timeout as an empty success, which hides a failure the coordinator could have recovered from.",
 "remember": "Zero results is an answer, not an error. A timeout is an access failure and needs a retry decision. Report them as different things.",
 "analogy": "A negative test result and a lost specimen arrive on similar slips and mean opposite things. One closes the question; the other means the sample has to be taken again, and a ward that files them together acts on an answer it never had.",
 "svg": """<path class="tint" d="M22 30 h22 v22 a11 11 0 0 1 -22 0 z"/>
<line x1="18" y1="30" x2="48" y2="30"/>
<text class="lbl" x="33" y="48" text-anchor="middle">0</text>
<path class="acc" d="M22 80 l7 8 l14 -17"/>
<line class="dash thin" x1="80" y1="14" x2="80" y2="106"/>
<path class="dash" d="M112 30 h22 v22 a11 11 0 0 1 -22 0 z"/>
<line x1="108" y1="30" x2="138" y2="30"/>
<path class="acc" d="M106 80 q16 -12 32 -2 M131 71 l8 7 -10 3"/>
<circle class="paper" cx="122" cy="96" r="13"/>
<path d="M122 96 v-8 M122 96 l7 5"/>""",
 "alt": "Vial reading zero ticked; a missing specimen with a clock and retry",
},
{
 "id": "D5-15",
 "title": "Recover locally, propagate what you could not fix",
 "concept": "Subagents implement local recovery for transient failures and propagate only the errors they cannot resolve, including what was attempted and any partial results.",
 "tested": "A subagent hits a failure that a retry would clear, and the question asks where recovery belongs. Handling transient failures inside the subagent and escalating only the unresolved ones is the answer, carrying the attempts made and the partial results with them; distractors send every failure up to the coordinator, losing the cheap local fix, or retry internally and then report a bare status, stripping the context the coordinator needs.",
 "remember": "Transient failures are handled where they happen. What reaches the coordinator is what could not be fixed, plus the attempts made and any partial results.",
 "analogy": "The ward repeats a specimen that clotted before it troubles the consultant. What goes up the line is the problem the ward cannot resolve, with the attempts already made and whatever results did come back.",
 "svg": """<rect class="tint" x="10" y="62" width="56" height="44" rx="4"/>
<path class="acc" d="M20 88 q12 -16 26 -4 M40 78 l7 6 -9 3"/>
<text class="lbl" x="38" y="102" text-anchor="middle">retry</text>
<path d="M70 76 h8"/>
<rect class="paper" x="80" y="58" width="30" height="34" rx="2"/>
<line class="thin" x1="86" y1="70" x2="104" y2="70"/>
<line class="thin" x1="86" y1="80" x2="100" y2="80"/>
<path class="acc" d="M110 74 h14 v-26 M118 54 l6 -6 6 6"/>
<rect class="tint" x="100" y="14" width="48" height="30" rx="4"/>
<line class="dash thin" x1="44" y1="60" x2="100" y2="36"/>
<line class="no" x1="64" y1="42" x2="80" y2="58"/>
<line class="no" x1="80" y1="42" x2="64" y2="58"/>""",
 "alt": "Subagent retries locally, then sends attempts and partial results upward",
},
]
