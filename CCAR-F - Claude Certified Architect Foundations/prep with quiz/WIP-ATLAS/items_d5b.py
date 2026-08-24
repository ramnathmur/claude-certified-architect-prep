# Domain 5 part B — Context Management & Reliability · building: the hospital ward

ITEMS = [
{
 "id": "D5-16",
 "title": "Coverage annotations in the synthesis",
 "concept": "Synthesis output carries coverage annotations marking which findings are well supported and which topic areas have gaps because a source was unavailable.",
 "tested": "A subagent times out, the coordinator proceeds with partial results, and the question asks what the final output must carry. The answer annotates coverage: which findings are well supported, and which topics are thin because a source could not be reached. Distractors present the partial synthesis as a finished report, or terminate the whole workflow on the one failure.",
 "remember": "Partial results ship with the gap named. A coverage annotation marks each finding as well supported or as thin because a source was unavailable.",
 "analogy": "The discharge summary says which results are back and which bloods the lab could not run, so the doctor taking over knows what is missing. A summary listing only the tests that returned reads as a full workup.",
 "svg": """<rect class="paper" x="30" y="18" width="100" height="90" rx="3"/>
<rect class="tint" x="66" y="10" width="28" height="12" rx="3"/>
<line x1="42" y1="36" x2="102" y2="36"/>
<circle class="accfill" cx="36" cy="52" r="3"/><line class="thin" x1="44" y1="52" x2="104" y2="52"/>
<circle class="accfill" cx="36" cy="66" r="3"/><line class="thin" x1="44" y1="66" x2="104" y2="66"/>
<circle class="accfill" cx="36" cy="80" r="3"/><line class="thin" x1="44" y1="80" x2="104" y2="80"/>
<circle class="acc" cx="36" cy="96" r="3"/><line class="dash acc" x1="44" y1="96" x2="104" y2="96"/>
<text class="lbl" x="110" y="100">gap</text>""",
 "alt": "Report rows: three supported findings and one dashed row marked gap",
},
{
 "id": "D5-17",
 "title": "Context degradation in long sessions",
 "concept": "In an extended session the model starts giving inconsistent answers and referencing typical patterns rather than the specific classes it discovered earlier.",
 "tested": "Two hours into a codebase exploration the answers stop matching earlier ones and generic talk of typical patterns replaces the classes the session had named; the question asks the cause or the first response. The cause is context degradation over the length of the session. The distractor family reaches for a bigger context window or a stronger model instead of persisting the findings outside the session.",
 "remember": "Late-session inconsistency, plus typical patterns where specific names used to appear, is context degradation. The findings have to live outside the session.",
 "analogy": "Late in a long shift the doctor's recall of one patient's actual numbers softens into what a case like this usually looks like. The chart at the foot of the bed still holds the specific values.",
 "svg": """<rect class="paper" x="14" y="20" width="132" height="80" rx="3"/>
<polyline class="acc" points="24,84 38,58 52,74 66,52"/>
<circle class="accfill" cx="24" cy="84" r="3"/>
<line class="dash thin" x1="76" y1="26" x2="76" y2="94"/>
<polyline class="dash" points="84,68 100,68 116,68 134,68"/>
<circle class="thin" cx="126" cy="38" r="10"/>
<path class="thin" d="M126 38 V32 M126 38 l6 3"/>
<text class="lbl" x="34" y="38">spec</text>
<text class="lbl" x="92" y="54">typ</text>""",
 "alt": "Chart trace turns from a specific zigzag into a flat dashed line",
},
{
 "id": "D5-18",
 "title": "Scratchpad files persist findings across context boundaries",
 "concept": "Agents write key findings to a scratchpad file and read it back when answering later questions, so the findings survive context boundaries.",
 "tested": "A long investigation whose later answers no longer match what was found earlier, and the question asks what holds the findings. The answer has the agent maintain a scratchpad file of key findings and reference it for subsequent questions. Distractors reach for a bigger context window or leave the findings in the session's own context.",
 "remember": "Findings that must outlive the window go to a file, read back at each continuation. Compaction compresses what is in the session; the file keeps the finding exact.",
 "analogy": "The notes file the doctor keeps at the desk holds the specific findings: which drug the patient reacted to, which line is in which arm. Every return to that bed starts by reading the file, so the ward does not run on anyone's memory of a twelve-hour shift.",
 "svg": """<rect class="dash" x="12" y="18" width="58" height="86" rx="4"/>
<line class="thin" x1="22" y1="38" x2="60" y2="38"/>
<line class="thin" x1="22" y1="50" x2="60" y2="50"/>
<line class="thin" x1="22" y1="62" x2="60" y2="62"/>
<rect class="tint" x="94" y="26" width="52" height="76" rx="3"/>
<line class="thin" x1="102" y1="46" x2="138" y2="46"/>
<line class="thin" x1="102" y1="58" x2="138" y2="58"/>
<line class="thin" x1="102" y1="70" x2="138" y2="70"/>
<path class="acc" d="M74 44 h14 M84 39 l5 5 -5 5"/>
<path class="acc" d="M90 78 h-14 M80 73 l-5 5 5 5"/>
<text class="lbl" x="120" y="20" text-anchor="middle">file</text>""",
 "alt": "A session box writes findings to a notes file and reads them back",
},
{
 "id": "D5-19",
 "title": "Delegate verbose exploration; the main agent coordinates",
 "concept": "Subagents are spawned to investigate specific questions such as finding all test files or tracing refund flow dependencies, isolating their verbose output while the main agent coordinates.",
 "tested": "A multi-phase task whose discovery output would fill the main window before implementation begins, and the question asks how to preserve the main context. The answer spawns a subagent per question and takes back a concise summary, so the verbose output never reaches the main window. The paired option is `/compact`, which the guide lists for reducing usage once a session has already filled.",
 "remember": "One question per subagent; the summary comes back and the main agent stays at coordination level. Isolation prevents the window filling; `/compact` is the guide's remedy once it has.",
 "analogy": "The registrar is sent to work through one patient's old notes and comes back with the two lines that matter, rather than wheeling the whole file trolley onto the round. The consultant leading the round keeps the picture of every bed.",
 "svg": """<text class="lbl" x="34" y="24" text-anchor="middle">main</text>
<rect class="tint" x="10" y="30" width="48" height="40" rx="3"/>
<line class="thin" x1="18" y1="46" x2="50" y2="46"/>
<line class="thin" x1="18" y1="58" x2="40" y2="58"/>
<circle cx="98" cy="30" r="8"/>
<path d="M98 38 v14 M88 44 h20"/>
<rect class="tint" x="108" y="92" width="38" height="8"/>
<rect class="tint" x="112" y="82" width="32" height="8"/>
<rect class="tint" x="106" y="72" width="36" height="8"/>
<rect class="tint" x="110" y="62" width="30" height="8"/>
<rect class="tint" x="114" y="52" width="28" height="8"/>
<rect class="acc" x="70" y="40" width="16" height="12" rx="2"/>
<path class="acc" d="M68 46 h-8 M64 42 l-4 4 4 4"/>""",
 "alt": "Main whiteboard receives one card from a subagent buried in charts",
},
{
 "id": "D5-20",
 "title": "Summarise a phase before spawning the next",
 "concept": "Key findings from one exploration phase are summarised before the next phase's sub-agents are spawned, and that summary is injected into their initial context.",
 "tested": "A multi-phase exploration where the second phase's agents lack what the first phase established, and the question asks the design. The answer summarises phase one and injects the summary into the next phase's initial context. Distractors rely on automatic context inheritance, or hand the next phase the full verbose output of the first.",
 "remember": "Between phases: summarise, then inject into the next agents' initial context. A fresh subagent inherits nothing, so the summary is what it is given.",
 "analogy": "The handover is written up before the incoming team is called in, and each doctor arriving is handed it. Nobody on the new shift is expected to have overheard the previous round.",
 "svg": """<text class="lbl" x="24" y="22" text-anchor="middle">P1</text>
<rect class="tint" x="10" y="28" width="28" height="30" rx="2"/>
<rect class="tint" x="10" y="70" width="28" height="30" rx="2"/>
<path d="M44 64 h12 M52 59 l5 5 -5 5"/>
<rect class="acc" x="62" y="44" width="32" height="40" rx="2"/>
<line class="acc thin" x1="70" y1="58" x2="86" y2="58"/>
<line class="acc thin" x1="70" y1="70" x2="86" y2="70"/>
<text class="lbl" x="132" y="22" text-anchor="middle">P2</text>
<rect class="dash" x="116" y="28" width="30" height="30" rx="2"/>
<rect class="dash" x="116" y="70" width="30" height="30" rx="2"/>
<line class="acc thin" x1="98" y1="56" x2="112" y2="46"/>
<circle class="accfill" cx="114" cy="45" r="3"/>
<line class="acc thin" x1="98" y1="72" x2="112" y2="82"/>
<circle class="accfill" cx="114" cy="83" r="3"/>""",
 "alt": "Phase one summarised into a sheet injected into phase two agents",
},
{
 "id": "D5-21",
 "title": "Crash recovery: state exports plus a manifest",
 "concept": "Each agent exports its state to a known location, and on resume the coordinator loads a manifest and injects the persisted findings into agent prompts.",
 "tested": "A long multi-agent run dies partway through and the question asks how the completed work survives. The answer has each agent export structured state to a known location, with a manifest the coordinator reads on resume and injects into prompts. Distractors rely on the interrupted run's own context still being available to the new one, or re-run the whole investigation from the start.",
 "remember": "Agents write state to a known path; the coordinator reads the manifest on resume and injects it. Assuming the dead run's own context is still available is the distractor.",
 "analogy": "The board at the nurses' station carries each bed's status, so the doctor arriving after the power cut resumes from what is written. Nothing on the ward depends on someone remembering the last four hours.",
 "svg": """<rect class="tint" x="10" y="14" width="80" height="62" rx="4"/>
<line x1="10" y1="30" x2="90" y2="30"/>
<text class="lbl" x="50" y="26" text-anchor="middle">state</text>
<circle class="accfill" cx="20" cy="42" r="3"/><line class="thin" x1="28" y1="42" x2="80" y2="42"/>
<circle class="accfill" cx="20" cy="56" r="3"/><line class="thin" x1="28" y1="56" x2="80" y2="56"/>
<circle class="acc" cx="20" cy="70" r="3"/><line class="dash thin" x1="28" y1="70" x2="80" y2="70"/>
<path class="acc" d="M96 42 h14 M104 36 l6 6 -6 6"/>
<circle cx="128" cy="32" r="8"/>
<path d="M128 40 v16 M118 46 h20"/>
<rect class="dash" x="14" y="88" width="46" height="20" rx="3"/>
<line class="no" x1="19" y1="92" x2="55" y2="104"/>
<line class="no" x1="55" y1="92" x2="19" y2="104"/>""",
 "alt": "Status board read on resume; the lost in-session memory is crossed out",
},
{
 "id": "D5-22",
 "title": "/compact when discovery output fills the window",
 "concept": "`/compact` reduces context usage during an extended exploration session when the window has filled with verbose discovery output.",
 "tested": "`/compact` sits on both sides of the same distinction. When a session has already filled with verbose discovery output and the work must continue, it is the in-session lever. When the question is how to keep that output out of the main window in the first place, the Explore subagent is the stronger answer, because it prevents the filling rather than compressing after it.",
 "remember": "`/compact` shrinks a session already full of discovery output, which is what the guide lists it for. Where the choice is still open, isolate discovery in a subagent instead.",
 "analogy": "When the notes file has grown too long to work from, the doctor rewrites it shorter and carries on. Detail goes out with the rewrite, so anything that has to stay exact belongs somewhere the trimming does not reach.",
 "svg": """<rect class="tint" x="12" y="12" width="50" height="96" rx="3"/>
<line class="thin" x1="20" y1="30" x2="54" y2="30"/>
<line class="thin" x1="20" y1="44" x2="54" y2="44"/>
<line class="thin" x1="20" y1="58" x2="54" y2="58"/>
<line class="thin" x1="20" y1="72" x2="54" y2="72"/>
<line class="thin" x1="20" y1="86" x2="54" y2="86"/>
<text class="lbl" x="80" y="42" text-anchor="middle">/comp</text>
<path class="acc" d="M70 58 h16 M80 52 l6 6 -6 6"/>
<rect class="acc" x="96" y="30" width="50" height="44" rx="3"/>
<line class="thin" x1="104" y1="46" x2="138" y2="46"/>
<line class="thin" x1="104" y1="60" x2="138" y2="60"/>
<line class="dash thin" x1="104" y1="88" x2="128" y2="88"/>
<line class="dash thin" x1="112" y1="100" x2="136" y2="100"/>""",
 "alt": "A long notes page compacted into a short one; detail falls away",
},
{
 "id": "D5-23",
 "title": "97% overall can hide a bad segment",
 "concept": "An aggregate accuracy figure such as 97% overall can mask poor performance on one document type or field, so accuracy is validated by segment before high-confidence extractions are automated.",
 "tested": "An extraction system reports 97% overall accuracy and the team proposes auto-processing everything above the confidence threshold; the question asks the first step. The answer analyses accuracy by document type and by field, so every segment is shown to meet the bar on its own. The distractor family trusts the aggregate: auto-process on the overall number, or raise the threshold without ever breaking the number down.",
 "remember": "An aggregate can mask a bad segment. Break accuracy down by document type and by field before reducing human review.",
 "analogy": "The ward's overall infection figure looks acceptable while one bay accounts for most of the cases. The audit is run department by department, because the hospital average is the number that hides it.",
 "svg": """<line x1="14" y1="100" x2="148" y2="100"/>
<line class="dash" x1="14" y1="40" x2="148" y2="40"/>
<text class="lbl" x="28" y="32" text-anchor="middle">97%</text>
<rect class="tint" x="22" y="44" width="18" height="56"/>
<rect class="tint" x="48" y="42" width="18" height="58"/>
<rect class="tint" x="74" y="46" width="18" height="54"/>
<rect class="acc" x="100" y="74" width="18" height="26"/>
<rect class="tint" x="126" y="44" width="18" height="56"/>""",
 "alt": "Five accuracy bars under one dashed average; one accent bar falls short",
},
{
 "id": "D5-24",
 "title": "Stratified random sampling of high-confidence output",
 "concept": "Stratified random sampling of high-confidence extractions measures the error rate of the automated path and detects novel error patterns.",
 "tested": "A pipeline auto-processes its high-confidence extractions and the question asks what ongoing measurement to keep. The answer samples that high-confidence stream at random, stratified across document types and field categories. Distractors review only the low-confidence queue, or sample a flat percentage without stratifying, which leaves the automated path unmeasured and the rare segments under-sampled.",
 "remember": "Keep sampling the confident output, stratified across document types and fields. Reviewing only what the model flagged low measures nothing about the automated path.",
 "analogy": "The ward pulls a set number of charts from every bay each week, including the ones nobody flagged, because an error nobody has noticed shows up no other way. Reading only the charts already marked doubtful leaves the routine ones unread.",
 "svg": """<rect class="tint" x="14" y="18" width="14" height="20" rx="2"/>
<rect class="tint" x="32" y="18" width="14" height="20" rx="2"/>
<rect class="acc" x="50" y="18" width="14" height="20" rx="2"/>
<rect class="tint" x="14" y="46" width="14" height="20" rx="2"/>
<rect class="acc" x="32" y="46" width="14" height="20" rx="2"/>
<rect class="tint" x="50" y="46" width="14" height="20" rx="2"/>
<rect class="acc" x="14" y="74" width="14" height="20" rx="2"/>
<rect class="tint" x="32" y="74" width="14" height="20" rx="2"/>
<rect class="tint" x="50" y="74" width="14" height="20" rx="2"/>
<path class="acc" d="M72 56 h14 M80 50 l6 6 -6 6"/>
<rect class="tint" x="94" y="34" width="50" height="46" rx="3"/>
<rect class="acc" x="102" y="42" width="12" height="14" rx="2"/>
<rect class="acc" x="118" y="42" width="12" height="14" rx="2"/>
<rect class="acc" x="110" y="60" width="12" height="14" rx="2"/>""",
 "alt": "One chart sampled from every bay, collected into a review tray",
},
{
 "id": "D5-25",
 "title": "Field-level confidence, calibrated on labeled data, routes review",
 "concept": "Models output a confidence score for each field, review thresholds are calibrated against a labeled validation set, and low-confidence or contradictory-source extractions are routed to human review.",
 "tested": "A high-volume extraction pipeline has more documents than reviewers, and the question asks how to direct the limited review capacity. The answer scores confidence per field, calibrates the threshold on a labeled validation set, and routes low-confidence or ambiguous-source extractions to people. Distractors take raw self-reported confidence at face value, produce one score per document, or send every document to review.",
 "remember": "Per field, not per document. Calibrate the threshold on a labeled validation set; route low confidence and contradictory sources to a human.",
 "analogy": "Each value on the lab panel carries its own flag rather than one verdict for the whole sheet, and the flag levels were set against samples whose answers were already known. The reviewer's time goes to the flagged values and to specimens whose labels disagree.",
 "svg": """<rect class="paper" x="12" y="16" width="76" height="88" rx="3"/>
<line class="thin" x1="20" y1="34" x2="60" y2="34"/><rect class="tint" x="66" y="29" width="14" height="8" rx="2"/>
<line class="thin" x1="20" y1="52" x2="60" y2="52"/><rect class="tint" x="66" y="47" width="14" height="8" rx="2"/>
<line class="thin" x1="20" y1="70" x2="60" y2="70"/><rect class="acc" x="66" y="65" width="14" height="8" rx="2"/>
<line class="thin" x1="20" y1="88" x2="60" y2="88"/><rect class="tint" x="66" y="83" width="14" height="8" rx="2"/>
<path class="acc" d="M94 70 h14 M102 64 l6 6 -6 6"/>
<circle cx="128" cy="46" r="9"/>
<path d="M128 55 v16 M116 62 h24"/>""",
 "alt": "Per-field confidence marks; the low one routes to a human reviewer",
},
{
 "id": "D5-26",
 "title": "Claim-source mappings survive synthesis",
 "concept": "Subagents output structured claim-source mappings, giving the source URL or document name and the relevant excerpt, which the synthesis agent preserves and merges rather than compressing away.",
 "tested": "A final report states figures that cannot be traced back to any source, and the question asks where the attribution went or how to keep it. The answer requires structured claim-source mappings from the subagents, preserved by downstream agents through synthesis. Distractors compress the mapping away and append a general bibliography, or re-derive attributions by searching the sources again at the end.",
 "remember": "Attribution is lost at the summarisation step, so claim, excerpt and source travel together through synthesis. A bibliography at the end leaves individual claims untraceable.",
 "analogy": "Every entry in the notes records who reported it and what they said, and the discharge summary carries that attribution forward. A list of everyone seen that day, appended at the end, does not say which of them reported the fever.",
 "svg": """<rect class="tint" x="10" y="14" width="34" height="16" rx="2"/><circle class="accfill" cx="54" cy="22" r="4"/>
<rect class="tint" x="10" y="50" width="34" height="16" rx="2"/><circle class="accfill" cx="54" cy="58" r="4"/>
<rect class="tint" x="10" y="86" width="34" height="16" rx="2"/><circle class="accfill" cx="54" cy="94" r="4"/>
<path d="M64 58 h12 M72 53 l5 5 -5 5"/>
<rect class="paper" x="86" y="14" width="60" height="88" rx="3"/>
<line class="thin" x1="94" y1="34" x2="126" y2="34"/><circle class="accfill" cx="134" cy="34" r="4"/>
<line class="thin" x1="94" y1="58" x2="126" y2="58"/><circle class="accfill" cx="134" cy="58" r="4"/>
<line class="thin" x1="94" y1="82" x2="126" y2="82"/><circle class="accfill" cx="134" cy="82" r="4"/>""",
 "alt": "Each claim keeps its source dot through synthesis into the report",
},
{
 "id": "D5-27",
 "title": "Conflicting figures: keep both, attribute both",
 "concept": "When credible sources give different statistics, the analysis is completed with both values included and the conflict annotated with source attribution, leaving the coordinator to reconcile.",
 "tested": "A document-analysis agent finds a government report at 40% growth and an industry analysis at 12%, both credible, and the question asks what it should do. The answer finishes the analysis with both values, marks the conflict with its source attribution, and passes reconciliation to the coordinator. Distractors pick one of the two values by heuristic, or stop and ask the coordinator before completing the analysis.",
 "remember": "Do not choose a value. Carry both with their sources and mark the conflict; stopping mid-analysis to ask the coordinator is the other distractor.",
 "analogy": "Two readings of the same measurement both go on the chart, each with the time and the person who took it, and which one to act on goes to the consultant. Rubbing one out because it looks less likely removes the evidence that decision needs.",
 "svg": """<rect class="paper" x="10" y="16" width="78" height="64" rx="3"/>
<circle class="accfill" cx="20" cy="36" r="3"/>
<line class="thin" x1="28" y1="36" x2="52" y2="36"/>
<text class="lbl" x="60" y="40">40%</text>
<circle class="accfill" cx="20" cy="58" r="3"/>
<line class="thin" x1="28" y1="58" x2="52" y2="58"/>
<text class="lbl" x="60" y="62">12%</text>
<path class="acc" d="M92 36 h8 v22 h-8 M100 47 h10"/>
<circle cx="126" cy="36" r="9"/>
<path d="M126 45 v14 M114 51 h24"/>
<rect class="dash" x="14" y="88" width="44" height="20" rx="3"/>
<line class="no" x1="19" y1="92" x2="53" y2="104"/>
<line class="no" x1="53" y1="92" x2="19" y2="104"/>""",
 "alt": "Both conflicting figures kept with source dots; picking one is crossed out",
},
{
 "id": "D5-28",
 "title": "Well-established and contested findings in separate sections",
 "concept": "Reports carry explicit sections separating well-established findings from contested ones, keeping each source's original characterisation and its methodological context.",
 "tested": "A synthesis flattens strong evidence and disputed claims into one confident narrative, and the question asks how to structure the report. The answer gives well-established and contested findings their own sections and keeps the sources' own characterisations and methodological context. Distractors normalise every finding into one confident format, or drop the methodology note as detail.",
 "remember": "Two named sections: well-established and contested. The source's own hedging and its methodology travel with the finding rather than being smoothed out.",
 "analogy": "The notes keep what is confirmed apart from what is still suspected, and each entry keeps the wording of the doctor who wrote it, including how the finding was reached. Merged into one list, the suspicions read as settled.",
 "svg": """<rect class="paper" x="24" y="12" width="112" height="96" rx="3"/>
<line x1="24" y1="60" x2="136" y2="60"/>
<path class="acc" d="M34 32 l4 5 8 -10"/>
<line class="thin" x1="52" y1="32" x2="124" y2="32"/>
<path class="acc" d="M34 48 l4 5 8 -10"/>
<line class="thin" x1="52" y1="48" x2="124" y2="48"/>
<text class="lbl" x="38" y="82" text-anchor="middle">?</text>
<line class="dash thin" x1="52" y1="78" x2="124" y2="78"/>
<text class="lbl" x="38" y="98" text-anchor="middle">?</text>
<line class="dash thin" x1="52" y1="94" x2="124" y2="94"/>""",
 "alt": "One report split into ticked established rows and dashed contested rows",
},
{
 "id": "D5-29",
 "title": "Dates in every structured output",
 "concept": "Structured outputs carry publication or data-collection dates, so that differences between time periods are not read as contradictions.",
 "tested": "Two credible sources give different figures for the same measure and the pipeline reports a contradiction; the question asks what the outputs are missing. The answer requires publication or collection dates in every structured output, so 10% in one year and 15% in the next reads as change over time. Distractors flag every numeric disagreement as a conflict, or pick one of the two values.",
 "remember": "Every finding carries its date. Without one, a year of change between two sources is reported as a disagreement.",
 "analogy": "Every lab value on the chart is stamped with when the sample was taken, so a rising figure reads as a trend rather than two departments contradicting each other. An undated value cannot be set against the one before it.",
 "svg": """<rect class="paper" x="10" y="16" width="126" height="86" rx="3"/>
<line class="thin" x1="20" y1="38" x2="58" y2="38"/>
<text class="lbl" x="66" y="42">10%</text>
<circle class="acc" cx="112" cy="38" r="9"/>
<path class="acc" d="M112 38 v-5 M112 38 l4 3"/>
<line class="thin" x1="20" y1="62" x2="58" y2="62"/>
<text class="lbl" x="66" y="66">15%</text>
<circle class="acc" cx="112" cy="62" r="9"/>
<path class="acc" d="M112 62 v-5 M112 62 l4 3"/>
<line class="dash thin" x1="20" y1="86" x2="58" y2="86"/>
<circle class="dash" cx="112" cy="86" r="9"/>
<line class="no" x1="106" y1="80" x2="118" y2="92"/>
<line class="no" x1="118" y1="80" x2="106" y2="92"/>""",
 "alt": "Two dated lab values; an undated third value is crossed out",
},
{
 "id": "D5-30",
 "title": "Render each content type in its natural form",
 "concept": "Synthesis output renders financial data as tables, news and analysis as prose, and technical findings as structured lists, rather than converting everything to one uniform format.",
 "tested": "A synthesis agent converts every finding to uniform narrative prose for consistency, and the question asks the cost or the alternative. The answer renders each content type in its own form: tables for financial data, prose for news and analysis, structured lists for technical findings. The distractor is the single uniform format, which leaves tabular figures imprecise and harder to verify.",
 "remember": "Tables for figures, prose for news and analysis, lists for technical findings. One uniform format, chosen for consistency, is the distractor.",
 "analogy": "The chart keeps observations in a table, the round note in prose, and the drug list as a list, because each is read differently at the bedside. Written out as a paragraph, an observation that was checked at a glance has to be hunted for.",
 "svg": """<rect class="acc" x="12" y="14" width="46" height="36" rx="2"/>
<line class="acc thin" x1="12" y1="28" x2="58" y2="28"/>
<line class="acc thin" x1="35" y1="14" x2="35" y2="50"/>
<rect class="tint" x="12" y="62" width="46" height="36" rx="2"/>
<line class="thin" x1="18" y1="74" x2="52" y2="74"/>
<line class="thin" x1="18" y1="82" x2="52" y2="82"/>
<line class="thin" x1="18" y1="90" x2="46" y2="90"/>
<rect class="tint" x="94" y="14" width="46" height="36" rx="2"/>
<circle cx="102" cy="26" r="2"/><line class="thin" x1="108" y1="26" x2="134" y2="26"/>
<circle cx="102" cy="38" r="2"/><line class="thin" x1="108" y1="38" x2="134" y2="38"/>
<path class="thin" d="M64 46 L86 62 M86 62 l-8 1 M86 62 l-1 -8"/>
<rect class="dash" x="94" y="62" width="46" height="36" rx="2"/>
<line class="thin" x1="100" y1="72" x2="134" y2="72"/>
<line class="thin" x1="100" y1="80" x2="134" y2="80"/>
<line class="thin" x1="100" y1="88" x2="128" y2="88"/>
<line class="no" x1="100" y1="68" x2="134" y2="92"/>
<line class="no" x1="134" y1="68" x2="100" y2="92"/>""",
 "alt": "Table, prose and list panels; a uniform-format panel is crossed out",
},
]
