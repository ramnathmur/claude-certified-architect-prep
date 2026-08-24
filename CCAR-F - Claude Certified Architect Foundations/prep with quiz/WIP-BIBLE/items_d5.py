# Domain 5 — Context Management & Reliability (15%)
S = 'stroke="#15130F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"'

ITEMS = [
{
 "title": "The API remembers nothing",
 "world": "post", "cite": "D5 §5.1 · KD#25",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="30" width="42" height="30" rx="5" fill="#E1EAFB"/>
   <rect x="22" y="48" width="42" height="30" rx="5" fill="#E1EAFB"/>
   <rect x="30" y="66" width="42" height="30" rx="5" fill="#E1EAFB"/>
   <path d="M82 40v52" stroke="#2F5FBF" stroke-width="4"/>
   <path d="M74 48l8-8 8 8" stroke="#2F5FBF" stroke-width="4"/>
   <circle cx="100" cy="66" r="10" fill="#fff"/>
   <path d="M95 66h10" stroke="#FF4757" stroke-width="3.5"/></g></svg>''',
 "story": "Every request is a stranger at the counter. It knows what you handed it and nothing else — so you "
          "<b>hand over the whole file, every time</b>.",
 "tell": "\"It forgot what I said two turns ago\" → the app is not resending <code>messages[]</code>. "
         "There is no <code>session_id</code>, and a vector DB is for months of history, not turn three. "
         "Also why cost and latency climb as a conversation grows.",
},
{
 "title": "Lost in the middle",
 "world": "bay", "cite": "D5 §5.2 · KD#20",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="18" y="16" width="84" height="18" rx="4" fill="#0E7C8C"/>
   <rect x="18" y="40" width="84" height="14" rx="4" fill="#DBF1F4" opacity=".55"/>
   <rect x="18" y="60" width="84" height="14" rx="4" fill="#DBF1F4" opacity=".35"/>
   <rect x="18" y="80" width="84" height="14" rx="4" fill="#DBF1F4" opacity=".55"/>
   <rect x="18" y="100" width="84" height="14" rx="4" fill="#0E7C8C"/>
   <path d="M108 46l6 20-6 20" stroke="#FF4757" stroke-width="3.5"/></g></svg>''',
 "story": "The top and bottom of a long input get read properly. The <b>middle sags</b> — and the decisive "
          "finding sitting at the 40,000-token mark quietly does not exist.",
 "tell": "Key-findings summary at the <b>start</b> plus explicit section headings. Rotating whose output "
         "goes first does not change the attention pattern; compressing to 20K risks losing the thing itself.",
},
{
 "title": "The hybrid window — extract, summarise, keep",
 "world": "bay", "cite": "D5 §5.3 · §5.13",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="18" width="92" height="26" rx="5" fill="#0E7C8C"/>
   <path d="M24 31h34" stroke="#fff" stroke-width="3.5"/>
   <rect x="76" y="24" width="22" height="14" rx="3" fill="#fff"/>
   <rect x="14" y="52" width="92" height="20" rx="5" fill="#DBF1F4"/>
   <path d="M24 62h30" stroke-width="3" stroke-dasharray="4 5"/>
   <rect x="14" y="80" width="92" height="26" rx="5" fill="#fff"/>
   <path d="M24 90h70M24 100h50" stroke-width="3"/></g></svg>''',
 "story": "Three jobs at once. <b>Extract</b> the numbers, dates and IDs verbatim into a block. "
          "<b>Summarise</b> the low-density chat. <b>Keep</b> the last few exchanges intact so the current turn "
          "still makes sense.",
 "tell": "Uniform summarisation loses precision; a pure recency window drops whatever was said early. "
         "Semantic retrieval is for months across sessions, not one long conversation.",
},
{
 "title": "The case-facts block survives compression",
 "world": "bay", "cite": "D5 §5.4 · KD#21",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="20" width="88" height="34" rx="5" fill="#fff"/>
   <path d="M26 32h32M26 44h50" stroke-width="3" stroke-dasharray="4 5"/>
   <rect x="16" y="64" width="88" height="40" rx="5" fill="#0E7C8C"/>
   <path d="M28 78h28M28 92h44" stroke="#fff" stroke-width="3.5"/>
   <rect x="72" y="70" width="24" height="12" rx="3" fill="#fff"/></g></svg>''',
 "story": "\"Four instalments of £310, first due 12 October\" becomes \"a payment plan was discussed\" by turn "
          "forty. Put the facts in a <b>box outside the summariser's reach</b> and they cannot be blurred.",
 "tell": "Persistent case-facts block, updated as facts appear, included in every prompt. Raising the "
         "summarisation threshold only delays it; a better summariser prompt still relies on perfect execution.",
},
{
 "title": "Trim tool output before it lands",
 "world": "bay", "cite": "D5 §5.5",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M22 20h76l-16 34H38z" fill="#fff"/>
   <path d="M46 54h28l-6 42H52z" fill="#DBF1F4"/>
   <path d="M34 34h52" stroke="#0E7C8C" stroke-width="3"/>
   <path d="M56 68h8M56 80h8" stroke-width="3"/></g></svg>''',
 "story": "One lookup returns forty fields when five matter — and all forty sit in context for <b>every "
          "remaining turn</b> of the conversation.",
 "tell": "<code>PostToolUse</code> hook filters to the relevant fields. Choose which fields by what "
         "downstream actually uses — dropping one the reviewer depends on creates a silent blind spot.",
},
{
 "title": "Send the mess to a side room",
 "world": "bay", "cite": "D5 §5.6 · KD#22",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="12" y="30" width="38" height="58" rx="5" fill="#fff"/>
   <path d="M20 46h22M20 58h22" stroke-width="3"/>
   <path d="M50 52h16" stroke-dasharray="5 5"/>
   <rect x="66" y="20" width="42" height="78" rx="5" fill="#DBF1F4" stroke-dasharray="8 6"/>
   <path d="M74 34h26M74 44h26M74 54h26M74 64h26M74 74h18" stroke-width="2.5"/>
   <path d="M66 88H50" stroke="#0E7C8C" stroke-width="4"/>
   <path d="M56 82l-6 6 6 6" stroke="#0E7C8C" stroke-width="4"/></g></svg>''',
 "story": "Discovery across 120 files will eat the window before implementation starts. An <b>Explore "
          "subagent</b> does it elsewhere and hands back a summary.",
 "tell": "Isolation for verbose discovery — not <code>/compact</code> mid-task, which destroys the precision "
         "the implementation phase still needs.",
},
{
 "title": "Months of history need retrieval, not summary",
 "world": "bay", "cite": "D5 §5.7 · KD#24",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="34" cy="34" r="9" fill="#DBF1F4"/><circle cx="66" cy="26" r="9" fill="#DBF1F4"/>
   <circle cx="92" cy="46" r="9" fill="#DBF1F4"/><circle cx="30" cy="72" r="9" fill="#DBF1F4"/>
   <circle cx="62" cy="86" r="9" fill="#0E7C8C"/><circle cx="94" cy="82" r="9" fill="#DBF1F4"/>
   <circle cx="62" cy="56" r="14" fill="none" stroke="#0E7C8C" stroke-width="5"/>
   <path d="M72 66l14 14" stroke="#0E7C8C" stroke-width="5"/></g></svg>''',
 "story": "\"What did we conclude about the theme of isolation?\" is a <b>needle</b> question. Progressive "
          "summarisation has already ground that needle into \"we discussed several themes\".",
 "tell": "Semantic embeddings with retrieval over the full history. Rolling windows discard; summarisation "
         "abstracts away the exact conclusion you need to quote.",
},
{
 "title": "Escalate on structure, never on mood",
 "world": "kitchen", "cite": "D5 §5.8",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="24" width="42" height="72" rx="5" fill="#fff"/>
   <path d="M24 40h22M24 54h22M24 68h22M24 82h14" stroke-width="3"/>
   <circle cx="86" cy="42" r="18" fill="#FF4757"/>
   <path d="M78 36c3 3 5 3 8 0M86 50h.01" stroke="#fff" stroke-width="3.5"/>
   <path d="M74 30l24 24M98 30L74 54" stroke="#fff" stroke-width="3"/>
   <path d="M68 84h36" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "An angry message can be trivially fixable and a calm one can be a genuine mess. Mood is <b>not "
          "a complexity signal</b>, and neither is the model's own confidence score.",
 "tell": "Escalate on: explicit request for a human · policy silent or ambiguous · repeated failures · "
         "above a financial threshold. First expression of frustration is not a request for a manager.",
},
{
 "title": "Two matches? Ask one more question",
 "world": "kitchen", "cite": "D5 §5.8",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="36" cy="38" r="14" fill="#fff"/><circle cx="36" cy="76" r="14" fill="#fff"/>
   <path d="M56 38h14M56 76h14" stroke-dasharray="4 5"/>
   <rect x="74" y="44" width="32" height="26" rx="6" fill="#FFE8E1"/>
   <path d="M84 54h12M84 62h6" stroke-width="3"/>
   <path d="M86 70l-4 8 10-8"/></g></svg>''',
 "story": "Same surname, same initial, two accounts. Picking the more recently active one is a coin flip "
          "with someone's money. <b>One clarifying question</b> settles it.",
 "tell": "Ask for another identifier — email, order number, account number. Do not pick by heuristic, do "
         "not take the first result, and do not escalate: this ambiguity is resolvable by asking.",
},
{
 "title": "97% overall can hide 40% wrong",
 "world": "news", "cite": "D5 §5.9",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="70" width="18" height="34" rx="3" fill="#2E7D5B"/>
   <rect x="38" y="60" width="18" height="44" rx="3" fill="#2E7D5B"/>
   <rect x="62" y="66" width="18" height="38" rx="3" fill="#2E7D5B"/>
   <rect x="86" y="88" width="18" height="16" rx="3" fill="#FF4757"/>
   <path d="M10 46h100" stroke="#C0326B" stroke-width="4" stroke-dasharray="7 6"/>
   <path d="M95 82V60" stroke="#FF4757" stroke-width="4"/>
   <path d="M89 66l6-6 6 6" stroke="#FF4757" stroke-width="4"/></g></svg>''',
 "story": "The average is fine because the rare document type is rare. That type is still <b>wrong four "
          "times in ten</b>, and the aggregate is what is hiding it.",
 "tell": "Before reducing human review: break accuracy down <b>by document type and by field</b>, and "
         "stratify-sample the high-confidence stream too. Raw self-reported confidence needs calibrating against a labelled set first.",
},
{
 "title": "Carry both numbers, and carry the date",
 "world": "news", "cite": "D5 §5.10 · §5.11",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="12" y="26" width="42" height="34" rx="5" fill="#fff"/>
   <path d="M22 42h22" stroke-width="3.5"/>
   <rect x="66" y="26" width="42" height="34" rx="5" fill="#fff"/>
   <path d="M76 42h22" stroke-width="3.5"/>
   <path d="M60 34v18" stroke="#C0326B" stroke-width="4" stroke-dasharray="5 5"/>
   <rect x="26" y="72" width="20" height="14" rx="3" fill="#FCE3ED"/>
   <rect x="76" y="72" width="20" height="14" rx="3" fill="#FCE3ED"/>
   <path d="M20 100h80" stroke="#C0326B" stroke-width="4"/></g></svg>''',
 "story": "Two credible sources, two different numbers. You do not pick a winner and you do not average them "
          "— you <b>keep both with their names on</b> and flag the disagreement upward.",
 "tell": "And attach publication dates: without them, a 2023 figure and a 2024 figure look like a "
         "contradiction instead of a year of growth. A bibliography at the end is not attribution.",
},
{
 "title": "Write the state down before the crash",
 "world": "bay", "cite": "D5 §5.12",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="20" width="30" height="24" rx="4" fill="#fff"/>
   <rect x="14" y="52" width="30" height="24" rx="4" fill="#fff"/>
   <rect x="14" y="84" width="30" height="24" rx="4" fill="#fff"/>
   <path d="M44 32h16v52H44" stroke="#0E7C8C"/><path d="M44 64h16"/>
   <rect x="60" y="46" width="46" height="36" rx="5" fill="#DBF1F4"/>
   <path d="M70 58h26M70 70h16" stroke-width="3"/>
   <path d="M96 64l6 6 8-10" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "Four hours of work dies eight minutes from the end. Each agent should have been <b>exporting its "
          "state to a known place</b>, with a manifest the coordinator reads on the way back up.",
 "tell": "Status + findings + coverage + gaps per agent, plus a manifest. Conversation history does not "
         "survive a crash — the API is stateless. Scratchpad files serve the same role for long single-agent tasks.",
},
{
 "title": "Symptom → cause → fix, all on one screen",
 "world": "bay", "cite": "D5 §5.14",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="18" width="92" height="84" rx="6" fill="#fff"/>
   <path d="M14 38h92M44 38v64M76 38v64"/>
   <path d="M24 28h20" stroke-width="3"/>
   <circle cx="29" cy="52" r="4" fill="#FF4757"/><circle cx="59" cy="52" r="4" fill="#F5C518"/>
   <circle cx="91" cy="52" r="4" fill="#2E7D5B"/>
   <circle cx="29" cy="70" r="4" fill="#FF4757"/><circle cx="59" cy="70" r="4" fill="#F5C518"/>
   <circle cx="91" cy="70" r="4" fill="#2E7D5B"/>
   <circle cx="29" cy="88" r="4" fill="#FF4757"/><circle cx="59" cy="88" r="4" fill="#F5C518"/>
   <circle cx="91" cy="88" r="4" fill="#2E7D5B"/></g></svg>''',
 "story": "The last thing to read before you walk in. Most reliability questions describe a <b>symptom</b> and "
          "ask for the fix — so practise going symptom → cause → fix, in that order, rather than pattern-matching "
          "straight to an answer you like the look of.",
 "tell": "If you can name the <b>cause</b> column, the fix column is forced. Most wrong answers are fixes "
         "for a cause the question never described.",
 "extra": """<div class="scroller"><table>
<thead><tr><th>Symptom</th><th>Root cause</th><th>Fix</th></tr></thead><tbody>
<tr><td>Loop never terminates</td><td>Not checking <code>stop_reason</code></td><td>Exit on <code>end_turn</code></td></tr>
<tr><td>Precision lost late in a long chat</td><td>Facts swept into the summary</td><td>Case-facts block outside it</td></tr>
<tr><td>Context bloats from tool calls</td><td>40+ fields returned per call</td><td><code>PostToolUse</code> trims</td></tr>
<tr><td>Subagent "has nothing to work with"</td><td>Context isolation</td><td>Coordinator passes it explicitly</td></tr>
<tr><td>Middle of a long input ignored</td><td>Lost in the middle</td><td>Key findings first + headings</td></tr>
<tr><td>Window full before implementation</td><td>Discovery output floods the session</td><td>Explore subagent returns a summary</td></tr>
<tr><td>Human queue flooded</td><td>Sentiment or self-confidence used as a proxy</td><td>Escalate on structural signals</td></tr>
<tr><td>Wrong customer actioned</td><td>Heuristic pick among matches</td><td>Ask for another identifier</td></tr>
<tr><td>Errors slip through automation</td><td>Aggregate accuracy hides a segment</td><td>Per-type accuracy + stratified sampling</td></tr>
<tr><td>Report cannot attribute a claim</td><td>Claim→source lost in summarising</td><td>Structured mappings preserved through</td></tr>
<tr><td>Sources look contradictory</td><td>No publication dates</td><td>Require dates in every output</td></tr>
<tr><td>Work lost on a crash</td><td>Nothing persisted</td><td>State exports + manifest on resume</td></tr>
<tr><td>Behaviour drifts after many turns</td><td>Assistant turns dilute the system prompt</td><td>Reminders at breakpoints, or few-shot</td></tr>
<tr><td>Formats inconsistent across tools</td><td>Each source returns its own shape</td><td><code>PostToolUse</code> normalises centrally</td></tr>
</tbody></table></div>""",
},
]
