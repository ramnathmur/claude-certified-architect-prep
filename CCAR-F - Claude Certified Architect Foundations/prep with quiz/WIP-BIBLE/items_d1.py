# Domain 1 — Agentic Architecture & Orchestration (27%)
# World: kitchen (the restaurant pass) unless the concept is really an API/protocol fact.
S = 'stroke="#15130F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"'

ITEMS = [
{
 "title": "stop_reason drives the loop",
 "world": "post", "flag": "live", "cite": "D1 §1.1 · KD#5",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="34" width="76" height="54" rx="7" fill="#fff"/>
   <path d="M14 40l38 26 38-26"/>
   <circle cx="92" cy="34" r="22" fill="#2F5FBF"/>
   <path d="M83 34l6 6 12-13" stroke="#fff"/></g></svg>''',
 "story": "Every response comes back with a <b>stamp on the envelope</b>. <code>tool_use</code> means "
          "run the tool and post it round again. <code>end_turn</code> means deliver it to the customer. "
          "You read the stamp — you never read the letter to guess whether it is finished.",
 "tell": "Never infer completion from the text, an iteration counter, or the shape of <code>content[0]</code>. "
         "Read <code>stop_reason</code>.",
},
{
 "title": "Hub and spoke — everything through the pass",
 "world": "kitchen", "cite": "D1 §1.2 · KD#6",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="60" cy="60" r="17" fill="#E8552F"/>
   <circle cx="24" cy="24" r="12" fill="#fff"/><circle cx="96" cy="24" r="12" fill="#fff"/>
   <circle cx="60" cy="102" r="12" fill="#fff"/>
   <path d="M33 33l14 14M87 33L73 47M60 85V77"/>
   <path d="M36 24h48" stroke="#FF4757" stroke-dasharray="6 7"/>
   <path d="M52 16l16 16M68 16L52 32" stroke="#FF4757" stroke-width="6"/></g></svg>''',
 "story": "Stations never shout to each other across the kitchen. Every plate, every question, every "
          "failure goes over <b>the pass</b>, where the head chef sees all of it.",
 "tell": "Subagents never talk directly. The coordinator gets visibility, uniform error handling, and "
         "control of who sees what.",
},
{
 "title": "Context isolation — only what is on the ticket",
 "world": "kitchen", "cite": "D1 §1.2 · §1.18",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="20" y="16" width="54" height="70" rx="6" fill="#fff"/>
   <path d="M32 36h30M32 50h30M32 64h18"/>
   <circle cx="88" cy="76" r="20" fill="#FFE8E1"/>
   <path d="M78 72h20M78 82h12"/>
   <path d="M74 44h18" stroke-dasharray="5 6"/></g></svg>''',
 "story": "The grill cook does not know what the sauce station just made. They know what is <b>written on "
          "the ticket handed to them</b> — nothing else. The coordinator's own memory is invisible to them.",
 "tell": "\"The synthesis agent has nothing to work with\" is never the subagent's bug. The coordinator "
         "failed to put the findings in its prompt.",
},
{
 "title": "No Task tool, no delegation",
 "world": "kitchen", "cite": "D1 §1.3",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="34" cy="60" r="16" fill="#fff"/>
   <path d="M50 60h18M50 48h12M50 72h12"/>
   <rect x="70" y="30" width="34" height="22" rx="5" fill="#E8552F"/>
   <rect x="70" y="62" width="34" height="22" rx="5" fill="#fff" stroke-dasharray="6 6"/>
   <path d="M80 68l14 12M94 68l-14 12" stroke="#FF4757"/></g></svg>''',
 "story": "A coordinator that answers everything itself is not being lazy or badly instructed. "
          "It <b>physically cannot delegate</b> — the key is missing from its keyring.",
 "tell": "Coordinator never delegates? Check <code>\"Task\"</code> is in <code>allowedTools</code>. "
         "A prompt cannot grant a tool the config withholds.",
},
{
 "title": "Goals, not a numbered script",
 "world": "kitchen", "cite": "D1 §1.4",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M24 92l24-52 22 34 12-18 14 36z" fill="#FFE8E1"/>
   <path d="M78 40V16" /><path d="M78 18h20l-6 8 6 8H78z" fill="#E8552F"/>
   <path d="M22 28h20M22 40h14" stroke="#FF4757"/>
   <path d="M16 22l32 24M48 22L16 46" stroke="#FF4757" stroke-width="4"/></g></svg>''',
 "story": "Give the coordinator <b>the summit and the standard</b> — not turn-by-turn directions. "
          "A script covers the road someone imagined; the mountain has weather.",
 "tell": "Shallow, checklist-shaped output? Rewrite the coordinator prompt as goals plus quality criteria. "
         "More steps and more agents both make it worse.",
},
{
 "title": "Content and metadata travel in separate boxes",
 "world": "news", "cite": "D1 §1.5",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="26" width="60" height="48" rx="6" fill="#fff"/>
   <path d="M24 62l14-16 12 12 10-8 8 12"/>
   <circle cx="36" cy="40" r="5" fill="#C0326B"/>
   <path d="M76 50l16 8"/>
   <rect x="84" y="52" width="26" height="34" rx="5" fill="#FCE3ED" transform="rotate(12 97 69)"/>
   <path d="M88 64h16M88 74h10" transform="rotate(12 97 69)"/></g></svg>''',
 "story": "A photo with the <b>luggage tag still tied on</b>: source, page, date. Merge the tag into the "
          "caption and the next person cannot tell where it came from.",
 "tell": "Citations wrong or missing downstream? The fix is a structured format separating content from "
         "metadata — not asking the last agent to remember.",
},
{
 "title": "Every subagent succeeded and the answer is still wrong",
 "world": "kitchen", "cite": "D1 §1.6 · KD#7",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="60" cy="60" r="38" fill="#fff"/>
   <path d="M60 22v38l27 27"/>
   <path d="M60 60L98 60A38 38 0 0 0 60 22z" fill="#E8552F"/>
   <circle cx="80" cy="40" r="13" fill="none" stroke-width="6"/>
   <path d="M89 49l12 12" stroke-width="6"/></g></svg>''',
 "story": "Four cooks, four perfect dishes, and the table ordered something else entirely. Nobody "
          "cooked badly — <b>the order was cut wrong at the pass</b>.",
 "tell": "All subagents clean + coverage gap = the coordinator's decomposition. Never the subagents' "
         "prompts or their query quality.",
},
{
 "title": "Fixed pipeline vs adaptive decomposition",
 "world": "kitchen", "cite": "D1 §1.7",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M18 30h84" /><path d="M30 22v16M54 22v16M78 22v16"/>
   <path d="M18 82c14 0 14-18 28-18s14 18 28 18 14-16 28-16" stroke="#E8552F"/>
   <circle cx="46" cy="64" r="5" fill="#E8552F"/><circle cx="74" cy="82" r="5" fill="#E8552F"/>
   <circle cx="102" cy="66" r="5" fill="#E8552F"/></g></svg>''',
 "story": "Rails when you already know every station. A <b>river</b> when you are exploring — it bends "
          "around whatever it finds, and what it finds at step three changes step four.",
 "tell": "Known, repeatable template → fixed pipeline. Open-ended (\"add tests to a legacy codebase\") → "
         "map first, prioritise, adapt as dependencies surface.",
},
{
 "title": "The refinement loop needs a finish line",
 "world": "kitchen", "flag": "watch", "cite": "D1 §1.8",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M92 60a32 32 0 1 1-9-22"/>
   <path d="M84 16v22h-22"/>
   <rect x="44" y="46" width="30" height="30" rx="4" fill="#fff"/>
   <path d="M44 61h30M59 46v30"/>
   <rect x="44" y="46" width="15" height="15" fill="#15130F"/>
   <rect x="59" y="61" width="15" height="15" fill="#15130F"/></g></svg>''',
 "story": "Synthesis comes back thin. The chef does not re-plate the same thin dish — he <b>sends the "
          "runners back out for the missing ingredient</b>, then re-plates. And he knows what \"done\" looks like.",
 "tell": "Gaps in synthesis → coordinator re-delegates targeted queries, then re-invokes synthesis. "
         "Needs a defined sufficiency criterion, not an endless loop.",
},
{
 "title": "A failure report is a form, not the word FAILED",
 "world": "kitchen", "cite": "D1 §1.9 · KD#8",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="18" y="18" width="46" height="60" rx="6" fill="#FF4757"/>
   <path d="M32 44h18M32 56h18" stroke="#fff"/>
   <rect x="58" y="40" width="44" height="62" rx="6" fill="#fff"/>
   <path d="M68 56h24M68 68h24M68 80h16M68 92h20"/></g></svg>''',
 "story": "\"It broke\" tells the chef nothing. <b>What was attempted, what came back, what was already "
          "done, what else could be tried</b> — that is a report he can act on.",
 "tell": "Structured error context: failure type + attempted params + partial results + alternatives. "
         "And never terminate the whole run for one subagent's failure.",
},
{
 "title": "Coverage annotation — shade the map, do not refuse to draw it",
 "world": "news", "cite": "D1 §1.10",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M20 26l28-8 24 8 28-8v72l-28 8-24-8-28 8z" fill="#fff"/>
   <path d="M48 18v72M72 26v72"/>
   <path d="M72 26l28-8v40l-28 8z" fill="#FCE3ED"/>
   <path d="M76 34l20-6M76 46l20-6M76 58l20-6" stroke="#C0326B" stroke-width="3"/></g></svg>''',
 "story": "Three of five sources came back. You still write the briefing — you just <b>hatch the part of "
          "the map nobody surveyed</b> so the reader knows which claims are thin.",
 "tell": "Incomplete inputs → synthesise on what arrived and annotate the gaps. Do not return an error; "
         "do not ship silently as if it were complete.",
},
{
 "title": "Take the firehose away, do not mop afterwards",
 "world": "workshop", "flag": "live", "cite": "D1 §1.11 · D2 §2.5",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M16 44h30l-6 16H16z" fill="#B8791C"/>
   <path d="M46 44l34-16v48L46 60z" fill="#FDF0D8"/>
   <path d="M86 40h18M86 60h18M86 80h10" stroke="#FF4757" stroke-dasharray="4 6"/>
   <circle cx="80" cy="52" r="8" fill="#fff"/></g></svg>''',
 "story": "An agent with <code>fetch_url</code> will eventually fetch something it should not. Swapping it "
          "for <code>load_document</code> means the bad reach <b>never happens</b> — instead of happening and "
          "then being discarded.",
 "tell": "Prefer the tool that cannot do the wrong thing over the hook that cleans up after it. "
         "This is the same rule whether the question mentions hooks or not.",
},
{
 "title": "The four things that warrant a human",
 "world": "kitchen", "cite": "D1 §1.12",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="60" cy="34" r="16" fill="#fff"/>
   <path d="M32 96c0-16 12-28 28-28s28 12 28 28"/>
   <path d="M18 20h14M18 34h10M18 48h12" stroke="#E8552F" stroke-width="4"/>
   <path d="M102 20H88M102 34h-10M102 48H90" stroke="#E8552F" stroke-width="4"/></g></svg>''',
 "story": "Escalation is not a mood or a difficulty score. It is <b>four specific situations</b>: policy is "
          "silent, the customer asked for a person, repeated attempts have failed, or a wrong call does real harm.",
 "tell": "Competitor price-matching when policy only covers your own price drops → escalate; the policy "
         "does not say, and the agent must not invent it. Do not apply the nearest rule, and do not refuse "
         "on a rule that was never written.",
},
{
 "title": "The handoff note is everything the human sees",
 "world": "kitchen", "cite": "D1 §1.13",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M22 74l38-38" stroke-width="11"/>
   <circle cx="24" cy="76" r="9" fill="#E8552F"/>
   <rect x="58" y="20" width="44" height="40" rx="5" fill="#fff" transform="rotate(10 80 40)"/>
   <path d="M68 32h24M68 42h24M68 52h14" transform="rotate(10 80 40)"/></g></svg>''',
 "story": "You pass the baton with the <b>card tied to it</b>. The human picking it up has no transcript, "
          "no history, no idea what you already offered.",
 "tell": "Structured summary: customer ID · root cause · amount · actions already taken · recommended "
         "action. Not a transcript, not a flag, not \"escalate earlier\".",
},
{
 "title": "Preconditions in code, not pleading in the prompt",
 "world": "workshop", "cite": "D1 §1.14 · KD#11",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="18" y="30" width="14" height="62" rx="4" fill="#B8791C"/>
   <rect x="88" y="30" width="14" height="62" rx="4" fill="#B8791C"/>
   <path d="M32 48h56M32 68h56" stroke-width="7"/>
   <circle cx="60" cy="24" r="11" fill="#fff"/>
   <path d="M53 24l5 5 9-10"/></g></svg>''',
 "story": "A sign asking people to check in first gets ignored some of the time. A <b>turnstile that will "
          "not turn</b> gets ignored none of the time.",
 "tell": "Safety-critical sequencing → programmatic precondition or hook. Prompt instructions and "
         "few-shot examples are probabilistic by construction.",
},
{
 "title": "Parallel means one response, not one after another",
 "world": "kitchen", "cite": "D1 §1.15",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="34" cy="60" r="15" fill="#E8552F"/>
   <path d="M49 60h14"/>
   <rect x="64" y="20" width="40" height="22" rx="4" fill="#fff"/>
   <rect x="64" y="50" width="40" height="22" rx="4" fill="#fff"/>
   <rect x="64" y="80" width="40" height="22" rx="4" fill="#fff"/>
   <path d="M49 60L64 31M49 60l15 30"/></g></svg>''',
 "story": "Three tickets pinned to the rail <b>in one motion</b>. Hand them over one at a time and you have "
          "invented a queue with extra steps.",
 "tell": "Multiple <code>Task</code> calls in a <b>single</b> coordinator response run in parallel. Across "
         "separate turns they run sequentially.",
},
{
 "title": "Resume, fork, or start fresh",
 "world": "house", "cite": "D1 §1.16 · D3 §3.12",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M30 100V50a14 14 0 0 1 14-14h16"/>
   <path d="M60 36h16a14 14 0 0 1 14 14v50" stroke="#2E7D5B"/>
   <circle cx="60" cy="36" r="11" fill="#DFF2E7"/>
   <circle cx="30" cy="104" r="8" fill="#fff"/><circle cx="90" cy="104" r="8" fill="#fff"/></g></svg>''',
 "story": "Resume when yesterday still holds — and <b>say which files changed</b> so it re-checks only those. "
          "Fork to run two ideas off one expensive analysis. Start fresh with a summary when the evidence has gone stale.",
 "tell": "Three files refactored overnight → resume and name them. Comparing two approaches → "
         "<code>fork_session</code>. Everything stale → new session with a structured summary.",
},
{
 "title": "A second opinion has to be a second brain",
 "world": "kitchen", "cite": "D1 §1.17 · D4 §4.13",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="38" cy="42" r="16" fill="#fff"/>
   <path d="M22 92c0-12 7-20 16-20s16 8 16 20"/>
   <circle cx="84" cy="42" r="16" fill="#FFE8E1"/>
   <path d="M68 92c0-12 7-20 16-20s16 8 16 20"/>
   <rect x="68" y="36" width="32" height="10" rx="4" fill="#15130F"/></g></svg>''',
 "story": "The cook who plated it cannot taste it honestly — they can still taste their own reasoning. "
          "You need someone who <b>never heard the argument</b>.",
 "tell": "\"Review your work carefully\" and a second pass in the same conversation are both the same "
         "instance agreeing with itself. Independence needs a fresh instance with only the artefact.",
},
{
 "title": "Evaluator-optimizer is NOT context isolation",
 "world": "kitchen", "cite": "D1 §1.18",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="12" y="26" width="40" height="30" rx="5" fill="#fff"/>
   <path d="M52 41h14"/><rect x="66" y="26" width="40" height="30" rx="5" fill="#E8552F"/>
   <path d="M76 41l6 6 12-13" stroke="#fff"/>
   <rect x="12" y="72" width="40" height="30" rx="5" fill="#FFE8E1"/>
   <rect x="20" y="80" width="24" height="8" rx="3" fill="#15130F"/>
   <path d="M52 87h14" stroke-dasharray="5 6"/><rect x="66" y="72" width="40" height="30" rx="5" fill="#fff"/></g></svg>''',
 "story": "Both words contain \"independence\", and they mean different things. <b>Evaluator-optimizer</b> is "
          "a two-stage shape: maker, then critic. <b>Context isolation</b> is about how much an agent is handed.",
 "tell": "Generator → independent critic = evaluator-optimizer. Subagent gets only what the coordinator "
         "passes = context isolation. Naming questions want the mechanism, not the vibe.",
},
]
