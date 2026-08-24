# Domain 4 — Prompt Engineering & Structured Output (20%)
S = 'stroke="#15130F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"'

ITEMS = [
{
 "title": "Aim examples at the edge, not the middle",
 "world": "form", "cite": "D4 §4.1 · KD#18",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="60" cy="60" r="40" fill="#fff"/><circle cx="60" cy="60" r="26" fill="#F0E4F9"/>
   <circle cx="60" cy="60" r="12" fill="#fff"/>
   <path d="M96 30l-30 24" stroke="#7A3FA8" stroke-width="4"/>
   <circle cx="34" cy="42" r="5" fill="#7A3FA8"/><circle cx="40" cy="80" r="5" fill="#7A3FA8"/>
   <circle cx="82" cy="76" r="5" fill="#7A3FA8"/></g></svg>''',
 "story": "Twelve examples of the cases that already work teach nothing. The misroutes happen at the "
          "<b>blurry rim</b> — so that is where the examples go, each saying why this tool and not the other.",
 "tell": "4–6 examples targeting the specific ambiguous phrasings, with rationale. "
         "Not 10–15 clear ones, not one example of one sentence, not a classifier in front.",
},
{
 "title": "Reasoning cues are for multi-step work",
 "world": "form", "cite": "D4 §4.2",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="22" width="26" height="18" rx="4" fill="#F0E4F9"/>
   <path d="M40 31h12" stroke="#7A3FA8" stroke-width="4"/>
   <rect x="52" y="22" width="26" height="18" rx="4" fill="#F0E4F9"/>
   <path d="M78 31h12" stroke="#7A3FA8" stroke-width="4"/>
   <rect x="90" y="22" width="18" height="18" rx="4" fill="#7A3FA8"/>
   <rect x="14" y="70" width="34" height="22" rx="4" fill="#fff"/>
   <path d="M48 81h16" stroke="#7A3FA8" stroke-width="4"/>
   <rect x="64" y="70" width="34" height="22" rx="4" fill="#fff"/></g></svg>''',
 "story": "Compare five series across three metrics and rank them — that is a <b>chain</b>, and the chain "
          "benefits from being made explicit. Translate a phrase — that is one hop.",
 "tell": "Add \"think step by step\" for multi-step maths, multi-stage analysis, comparison across N items. "
         "Do not add it to single-step tasks. Temperature is not the dial for reasoning.",
},
{
 "title": "Persistent behaviour lives in the system prompt",
 "world": "form", "cite": "D4 §4.3",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="18" width="88" height="24" rx="5" fill="#7A3FA8"/>
   <path d="M26 30h50" stroke="#fff" stroke-width="3.5"/>
   <rect x="16" y="52" width="60" height="18" rx="4" fill="#fff"/>
   <rect x="34" y="78" width="60" height="18" rx="4" fill="#F0E4F9"/>
   <path d="M8 18v78" stroke="#7A3FA8" stroke-width="4"/></g></svg>''',
 "story": "Tone, persona, format rules and \"always ask before X\" are <b>standing orders</b>. They belong "
          "where they apply for the whole conversation, and where they outrank the chat.",
 "tell": "Not the first user message (loses authority mid-conversation), not the first assistant message "
         "(the model can deviate from its own words), not environment variables (no effect at all).",
},
{
 "title": "Prefilling kills the \"Certainly!\"",
 "world": "form", "cite": "D4 §4.4",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="30" width="88" height="26" rx="6" fill="#fff"/>
   <path d="M26 43h20" stroke="#FF4757" stroke-width="4"/>
   <path d="M56 43h38" stroke-width="3.5"/>
   <path d="M22 37l14 12M36 37L22 49" stroke="#FF4757" stroke-width="3.5"/>
   <rect x="16" y="70" width="88" height="26" rx="6" fill="#F0E4F9"/>
   <rect x="24" y="78" width="24" height="10" rx="3" fill="#7A3FA8"/>
   <path d="M56 83h38" stroke-width="3.5"/></g></svg>''',
 "story": "You do not ask it to stop saying \"Certainly!\". You <b>start the sentence for it</b>, and it "
          "continues from where you left off. There is no gap for the filler to appear in.",
 "tell": "Prefill a partial assistant message. Also the way to inject a live event: prefix it onto the "
         "next user message. Lower temperature does not remove specific phrases.",
},
{
 "title": "Required fields manufacture lies",
 "world": "form", "cite": "D4 §4.5",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="20" y="16" width="80" height="88" rx="6" fill="#fff"/>
   <path d="M32 36h34M32 54h34M32 72h34M32 88h20" stroke-width="3"/>
   <rect x="74" y="30" width="16" height="12" rx="3" fill="#F0E4F9"/>
   <rect x="74" y="48" width="16" height="12" rx="3" fill="#F0E4F9"/>
   <rect x="74" y="66" width="16" height="12" rx="3" fill="#FF4757"/>
   <path d="M78 70l8 8M86 70l-8 8" stroke="#fff" stroke-width="3"/></g></svg>''',
 "story": "A form that will not submit with a blank box does not create the missing information. It creates "
          "a person <b>writing something in the box</b>.",
 "tell": "Mark a field required only if it is <b>always</b> present in the source. Otherwise nullable, so "
         "the model returns <code>null</code> instead of inventing. \"Everything required for completeness\" is the trap.",
},
{
 "title": "tool_use is how you guarantee shape",
 "world": "form", "cite": "D4 §4.6",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="24" width="88" height="72" rx="6" fill="#F0E4F9"/>
   <rect x="28" y="38" width="30" height="18" rx="4" fill="#fff"/>
   <rect x="62" y="38" width="30" height="18" rx="4" fill="#fff"/>
   <rect x="28" y="64" width="64" height="18" rx="4" fill="#fff"/>
   <path d="M60 12v12" stroke="#7A3FA8" stroke-width="4"/>
   <circle cx="60" cy="10" r="6" fill="#7A3FA8"/></g></svg>''',
 "story": "Define a tool whose <b>input schema is your output shape</b>, then read the tool call. The tool "
          "need not do anything — it exists to make malformed JSON impossible.",
 "tell": "This kills the entire syntax-error class. It does nothing about wrong values. "
         "Asking nicely for JSON in the prompt still returns prose preambles and markdown fences.",
},
{
 "title": "Schema-valid and wrong are not opposites",
 "world": "form", "flag": "live", "cite": "D4 §4.7",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="18" y="26" width="84" height="68" rx="6" fill="#fff"/>
   <path d="M30 44h26M30 60h26M30 76h26" stroke-width="3"/>
   <path d="M68 42l6 6 12-14" stroke="#2E7D5B" stroke-width="4.5"/>
   <path d="M68 58l6 6 12-14" stroke="#2E7D5B" stroke-width="4.5"/>
   <circle cx="78" cy="78" r="11" fill="#FF4757"/>
   <path d="M78 72v7" stroke="#fff" stroke-width="3.5"/><circle cx="78" cy="84" r="2" fill="#fff"/></g></svg>''',
 "story": "Every box filled, every type correct, and the total still does not match the line items. The form "
          "is <b>perfectly filled in and factually false</b>.",
 "tell": "Syntax = shape, caught by the schema, 100% of the time. Semantic = meaning, caught only by "
         "business-rule checks. On multiple-response items, do not file a structural violation under semantic.",
},
{
 "title": "One definition, two consumers",
 "world": "form", "cite": "D4 §4.8",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="42" y="14" width="36" height="26" rx="5" fill="#7A3FA8"/>
   <path d="M52 27h16" stroke="#fff" stroke-width="3.5"/>
   <path d="M50 40L28 64M70 40l22 24" stroke="#7A3FA8" stroke-width="4"/>
   <rect x="10" y="64" width="38" height="30" rx="5" fill="#fff"/>
   <rect x="72" y="64" width="38" height="30" rx="5" fill="#fff"/>
   <path d="M18 78h22M80 78h22" stroke-width="3"/></g></svg>''',
 "story": "A hand-maintained schema and a hand-maintained validator will drift, because two humans have to "
          "remember the same thing twice. <b>Generate one from the other</b> and they cannot.",
 "tell": "Pydantic model generates the tool's JSON Schema. A code-review checklist is a process patch for "
         "an architecture problem. And code-side validation is not redundant — schemas cannot express business rules.",
},
{
 "title": "Retry cannot conjure what is not there",
 "world": "form", "cite": "D4 §4.9",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M92 60a32 32 0 1 1-9-22"/><path d="M84 16v22H62"/>
   <rect x="40" y="46" width="40" height="30" rx="5" fill="#fff"/>
   <path d="M50 60h20" stroke="#FF4757" stroke-width="4" stroke-dasharray="5 5"/>
   <circle cx="60" cy="88" r="4" fill="#FF4757"/></g></svg>''',
 "story": "The purchase-order number is not on the document. Ten retries, better feedback, a firmer tone — "
          "none of it puts a number on a page that never had one. It just <b>pressures the model to invent</b>.",
 "tell": "Retry fixes format, structure and arithmetic. For genuinely absent data: make the field nullable, "
         "accept the null, stop. Raising max retries from 3 to 10 is the trap.",
},
{
 "title": "Make it show its working, in the schema",
 "world": "form", "cite": "D4 §4.10",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="24" width="88" height="72" rx="6" fill="#fff"/>
   <rect x="28" y="38" width="30" height="16" rx="4" fill="#F0E4F9"/>
   <rect x="62" y="38" width="30" height="16" rx="4" fill="#F0E4F9"/>
   <path d="M46 62h28" stroke-width="3"/>
   <circle cx="60" cy="80" r="11" fill="#F5C518"/>
   <path d="M60 74v7" stroke-width="3.5"/><circle cx="60" cy="86" r="2" fill="#15130F"/></g></svg>''',
 "story": "Extract the total <b>as written</b>, and separately the total <b>you derived</b>, and a boolean "
          "for whether they disagree. Now the contradiction is data instead of a surprise in reconciliation.",
 "tell": "<code>stated_total</code> + <code>calculated_total</code> + <code>conflict_detected</code>. "
         "Self-correction is structural, not asking \"are you sure?\" afterwards.",
},
{
 "title": "Batch is overnight freight",
 "world": "bay", "cite": "D4 §4.11 · KD#14",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="12" y="46" width="56" height="34" rx="5" fill="#DBF1F4"/>
   <path d="M68 56h18l14 14v10H68z" fill="#fff"/>
   <circle cx="34" cy="88" r="9" fill="#fff"/><circle cx="86" cy="88" r="9" fill="#fff"/>
   <circle cx="34" cy="60" r="13" fill="#fff" stroke="#0E7C8C"/>
   <path d="M34 53v7l5 4" stroke="#0E7C8C" stroke-width="3.5"/></g></svg>''',
 "story": "Half price, arrives <b>some time inside 24 hours</b>, and there is no promise it will not be hour "
          "23. You plan against the worst case or you do not plan at all.",
 "tell": "Submission deadline = your deadline <b>− 24h</b>. Blocking work (pre-merge, interactive) stays "
         "synchronous. <code>custom_id</code> is the join key — result order is not guaranteed. Re-submit only the failures, fixed.",
},
{
 "title": "Attention dilutes; a bigger window does not help",
 "world": "bay", "cite": "D4 §4.12 · KD#17",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="18" width="92" height="24" rx="5" fill="#fff"/>
   <path d="M24 30h72" stroke="#FF4757" stroke-width="3" stroke-dasharray="4 6"/>
   <rect x="14" y="52" width="28" height="22" rx="4" fill="#DBF1F4"/>
   <rect x="46" y="52" width="28" height="22" rx="4" fill="#DBF1F4"/>
   <rect x="78" y="52" width="28" height="22" rx="4" fill="#DBF1F4"/>
   <rect x="14" y="84" width="92" height="22" rx="4" fill="#0E7C8C"/>
   <path d="M26 95h68" stroke="#fff" stroke-width="3"/></g></svg>''',
 "story": "Fourteen files in one pass gives you deep comments on three and nothing on the rest, plus the same "
          "pattern flagged here and waved through there. <b>Per-file passes, then one integration pass.</b>",
 "tell": "\"Use a model with a bigger context window\" is the named trap. More room to put tokens is not "
         "more attention per token.",
},
{
 "title": "Prompt chaining — one job per link",
 "world": "form", "cite": "D4 §4.14",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="10" y="46" width="28" height="28" rx="6" fill="#F0E4F9"/>
   <rect x="46" y="46" width="28" height="28" rx="6" fill="#F0E4F9"/>
   <rect x="82" y="46" width="28" height="28" rx="6" fill="#7A3FA8"/>
   <path d="M38 60h8M74 60h8" stroke="#7A3FA8" stroke-width="4"/>
   <path d="M18 60h12M54 60h12" stroke-width="3.5"/>
   <path d="M90 60h12" stroke="#fff" stroke-width="3.5"/></g></svg>''',
 "story": "\"Find the issues\" then \"write fixes for these issues\" beats one prompt doing both. Each link "
          "gets the previous link's output and <b>one job to do with it</b>.",
 "tell": "Predictable multi-stage work with known steps → chain it. Same family as the fixed pipeline in D1 "
         "§1.7; the opposite is dynamic adaptive decomposition, for when the scope is unknown.",
},
{
 "title": "Draw the escalation line with examples",
 "world": "form", "cite": "D4 §4.15",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M60 12v96" stroke-width="4" stroke-dasharray="8 7"/>
   <rect x="12" y="26" width="36" height="22" rx="5" fill="#F0E4F9"/>
   <path d="M20 37h20" stroke-width="3"/>
   <rect x="12" y="62" width="36" height="22" rx="5" fill="#F0E4F9"/>
   <rect x="72" y="26" width="36" height="22" rx="5" fill="#fff"/>
   <rect x="72" y="62" width="36" height="22" rx="5" fill="#fff"/>
   <path d="M80 73h20" stroke-width="3"/></g></svg>''',
 "story": "\"Escalate complex cases\" is a line nobody can see, so the agent draws it somewhere private — "
          "usually backwards. Put <b>worked cases on both sides</b> of it.",
 "tell": "Explicit criteria plus few-shot examples of resolve-this / escalate-that. Not a self-rated "
         "confidence threshold, not a separate classifier — both add machinery around a boundary that was never drawn.",
},
{
 "title": "Testable criteria beat adjectives",
 "world": "form", "cite": "D4 §4.16",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="24" width="88" height="26" rx="5" fill="#fff"/>
   <path d="M26 37h30" stroke-width="3" stroke-dasharray="4 5"/>
   <path d="M74 30l10 14M84 30l-10 14" stroke="#FF4757" stroke-width="3.5"/>
   <rect x="16" y="66" width="88" height="26" rx="5" fill="#F0E4F9"/>
   <path d="M26 79h44" stroke-width="3.5"/>
   <path d="M78 74l6 6 10-12" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "\"Check that comments are accurate\" is resolved differently on every run. \"Flag a comment only "
          "when the behaviour it claims <b>contradicts the code</b>\" either holds or it does not.",
 "tell": "Move from abstract intent to an explicit condition. Adding \"complete\" and \"helpful\" alongside "
         "\"accurate\" makes it worse, not better.",
},
{
 "title": "Switch off the noisy categories",
 "world": "form", "cite": "D4 §4.17",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="20" width="88" height="18" rx="5" fill="#FF4757"/>
   <rect x="16" y="44" width="88" height="18" rx="5" fill="#FF4757"/>
   <rect x="16" y="68" width="88" height="18" rx="5" fill="#F0E4F9"/>
   <rect x="16" y="92" width="88" height="18" rx="5" fill="#F0E4F9"/>
   <path d="M92 29l-14-4M92 53l-14-4" stroke="#fff" stroke-width="4"/>
   <path d="M28 77l6 6 12-14" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "Two categories at ~50% false positives train the team to dismiss <b>everything</b> — including the "
          "6% category that catches real safety defects. Stop the bleed first, fix the prompts after.",
 "tell": "Temporarily disable the high-false-positive categories. Confidence scores still show every "
         "finding; uniform strictness reduction damages the accurate ones; few-shot across all of them is too slow.",
},
{
 "title": "It can only avoid duplicates it can see",
 "world": "form", "cite": "D4 §4.18",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="26" width="40" height="68" rx="5" fill="#fff"/>
   <path d="M22 42h24M22 54h24M22 66h24M22 78h16" stroke-width="3"/>
   <path d="M58 60h12" stroke-dasharray="4 5"/>
   <rect x="70" y="26" width="36" height="68" rx="5" fill="#F0E4F9"/>
   <path d="M78 42h20M78 54h20" stroke-width="3"/>
   <path d="M78 66l5 5 10-11" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "Six of ten suggested tests already exist. The generator is not careless — it has <b>never been "
          "shown the suite</b>.",
 "tell": "Put the existing test files in context. Cutting the request from 10 to 4 assumes an ordering it "
         "never promised; keyword matching misses semantic duplicates.",
},
{
 "title": "State your assumptions and go",
 "world": "form", "cite": "D4 §4.19 · KD#19",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="22" width="88" height="20" rx="5" fill="#fff"/>
   <path d="M26 32h20M56 32h8M74 32h8M92 32h6" stroke="#FF4757" stroke-width="3.5"/>
   <rect x="16" y="56" width="88" height="44" rx="5" fill="#F0E4F9"/>
   <path d="M26 70h56M26 82h44" stroke-width="3.5"/>
   <path d="M88 88l6 6 10-12" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "Four clarifying questions and a third of people just leave. Name what you assumed, do the work, "
          "and <b>invite the correction</b>.",
 "tell": "Applies inside multi-agent systems too — a synthesis agent should not block waiting on the "
         "coordinator for every gap. Hidden defaults are the other failure: the user never learns what you chose.",
},
{
 "title": "Drift is your own voice drowning the brief",
 "world": "form", "cite": "D4 §4.20 · KD#23",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="16" width="88" height="16" rx="4" fill="#7A3FA8"/>
   <rect x="26" y="40" width="70" height="12" rx="4" fill="#fff"/>
   <rect x="26" y="58" width="70" height="12" rx="4" fill="#F0E4F9"/>
   <rect x="26" y="76" width="70" height="12" rx="4" fill="#F0E4F9"/>
   <rect x="26" y="94" width="70" height="12" rx="4" fill="#F0E4F9"/></g></svg>''',
 "story": "By turn nine the model is pattern-matching <b>its own last eight replies</b> rather than the "
          "standing orders at the top. Nothing overflowed — the orders are simply outnumbered.",
 "tell": "Degrading at 2,500–3,000 tokens is never window exhaustion, and the system prompt <b>is</b> resent "
         "every request. Fix: reminders at breakpoints, or replace verbose rules with few-shot examples.",
},
]
