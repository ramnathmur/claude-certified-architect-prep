# Non-domain pages: Tuesday protocol, the visual key, live errors, heuristics, out-of-scope.
S = 'stroke="#15130F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"'


def page_start():
    return """<section class="page on" id="start">
  <header class="page-head">
    <div class="eyebrow">Read this bit even if you read nothing else</div>
    <h2>Tuesday protocol</h2>
    <p class="count">Exam: Tue 18 Aug · 60 questions · 120 minutes · pass 720/1000</p>
  </header>

  <div class="note hot">
    <h3>The four rules that are worth marks on their own</h3>
    <ul class="tick">
      <li><b>Pause on file paths and <code>tool_choice</code> values.</b> On your last paper, four of nine
        misses took under 40 seconds — on a paper where you used a third of the clock. If an option names
        <code>.claude/</code> anything, or <code>auto</code>/<code>any</code>/a forced tool, stop and read all
        four options before choosing.</li>
      <li><b>Count your picks on multiple-response.</b> Half right scores exactly the same as blank. Both
        your multiple-response misses last time were partial answers — you had one of the two right.</li>
      <li><b>Match the guarantee to the requirement.</b> Not "is this a guarantee?" but "is this the
        guarantee the question asked for?" A stronger guarantee than needed is still wrong.</li>
      <li><b>Answer everything.</b> No penalty for a wrong answer. A blank and a wrong guess score the same,
        so a blank is strictly worse.</li>
    </ul>
  </div>

  <div class="grid2">
    <div class="stat"><div class="k">Your last paper</div><div class="v">51 / 60</div>
      <div class="s">Exam 17, 14 Aug · 865 scaled. Built specifically to attack your known error shapes,
      so a lower score there means more than a higher score elsewhere.</div></div>
    <div class="stat"><div class="k">Your band across 11 papers</div><div class="v">49 – 57</div>
      <div class="s">Every single one clears 720. Your worst paper ever, Exam 4, scored 775.</div></div>
    <div class="stat"><div class="k">Time you actually use</div><div class="v">~38 min</div>
      <div class="s">Of 120. You are not short of time — you are short of pauses.</div></div>
    <div class="stat"><div class="k">Question weight</div><div class="v">D1 27%</div>
      <div class="s">D3 20% · D4 20% · D2 18% · D5 15%. Getting a D1 question wrong costs most.</div></div>
  </div>

  <div class="note" style="margin-top:14px">
    <h3>How the paper is built</h3>
    <p>Four scenarios drawn at random from a bank of six, roughly fifteen questions each. You will not get
    all six. Items are multiple-choice <b>and</b> multiple-response, and every item states how many
    responses to select — read that line before the options.</p>
    <p>Scoring is scaled 100–1000 with the pass at 720, and the score report gives you percent-correct by
    domain as information only. Pass or fail is decided by the total.</p>
  </div>

  <div class="note cool">
    <h3>Two things you have already fixed — do not re-litigate them in the room</h3>
    <p><b><code>tool_choice</code> auto vs any.</b> You missed this twice in fourteen hours across Exams 12
    and 13. On Exam 17 it was attacked from four directions and you got three right, including the exact
    "which one <i>guarantees</i> a call" shape, which you spent 138 seconds on. It is done. What replaced it
    is one level finer — see Live errors.</p>
    <p><b>Two-tool token binding.</b> Missed on Exams 4, 5 and 6; correct on every appearance since. The log
    calls it durably cleared. If you see a <code>preview</code>/<code>execute</code> pair, trust yourself.</p>
  </div>
</section>"""


def page_worlds(worlds):
    icons = {"kitchen": "🍳", "workshop": "🧰", "house": "🏠", "post": "📮",
             "form": "📋", "bay": "🚚", "news": "📰"}
    rows = ""
    for key, (ink, tint, name) in worlds.items():
        rows += (f'<div class="worldrow"><div class="swatch" style="background:{tint}">{icons[key]}</div>'
                 f'<div><b style="color:{ink}">{name}</b><div style="font-size:13.5px;color:#413A31">'
                 f'{WORLD_BLURB[key]}</div></div></div>')
    return f"""<section class="page" id="worlds">
  <header class="page-head">
    <div class="eyebrow">Your visual key</div>
    <h2>Seven worlds</h2>
    <p class="count">Every card below borrows its picture from one of these. Same world = same family of ideas.</p>
  </header>
  <div class="note">{rows}</div>
  <div class="note">
    <h3>Why worlds and not 80 random icons</h3>
    <p>Eighty unrelated drawings is noise, and noise is what you forget. Each domain borrows from one or two
    worlds, so a picture tells you where you are before you have read a word — and the <b>differences</b>
    between two cards in the same world are what stick.</p>
  </div>
</section>"""


WORLD_BLURB = {
 "kitchen": "Orchestration. Coordinator, subagents, tickets, the pass. Mostly D1.",
 "workshop": "Tools and MCP. Drawers, labels, jigs, the bench. Mostly D2.",
 "house": "Configuration. Fridge notes, room signs, recipe books. Mostly D3.",
 "post": "The protocol. Envelopes, stamps, tracking numbers. API facts.",
 "form": "Structured output. Boxes, blanks, ticks. Mostly D4.",
 "bay": "Context and batches. Freight, pallets, the loading dock. Mostly D5.",
 "news": "Provenance. Sources, datelines, contradictory wires.",
}


LIVE = [
{
 "title": "Guarantee strength — the one that replaced tool_choice",
 "world": "workshop", "flag": "live", "cite": "Exam 17 Q36 · D4 §4.6",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="62" width="26" height="42" rx="4" fill="#FDF0D8"/>
   <rect x="47" y="42" width="26" height="62" rx="4" fill="#B8791C"/>
   <rect x="80" y="20" width="26" height="84" rx="4" fill="#E8552F"/>
   <path d="M60 32l6 6 12-14" stroke="#15130F" stroke-width="4"/>
   <circle cx="93" cy="14" r="7" fill="#fff"/></g></svg>''',
 "story": "You picked <code>any</code> where the pipeline needed <b>one named tool</b>, because that tool's "
          "schema was the contract. <code>any</code> is a real guarantee — it was just the wrong rung.",
 "tell": "Ask what the requirement <b>names</b>. \"Must call something\" → <code>any</code>. "
         "\"Must call <i>this</i>\" → forced. \"May answer in text\" → <code>auto</code>.",
},
{
 "title": "Prevention doesn't transfer out of the hooks frame",
 "world": "workshop", "flag": "live", "cite": "Exam 17 Q2 ✓ vs Q19 ✗ · D2 §2.5",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="12" y="34" width="40" height="52" rx="6" fill="#fff"/>
   <path d="M22 60h20" stroke="#2E7D5B" stroke-width="5"/>
   <rect x="68" y="34" width="40" height="52" rx="6" fill="#FFE8E1"/>
   <path d="M78 52l20 20M98 52l-20 20" stroke="#FF4757" stroke-width="4"/>
   <path d="M60 26v68" stroke-dasharray="6 7" stroke-width="4"/></g></svg>''',
 "story": "Asked as \"PreToolUse or PostToolUse?\" you got it right. Asked as \"how should this tool be "
          "designed?\" — same distinction, no hook mentioned — you picked the one that <b>cleans up after</b>.",
 "tell": "Whenever a fix could either stop the thing or tidy it afterwards, prefer the one that stops it. "
         "The word \"hook\" does not have to appear for this rule to apply.",
},
{
 "title": "Wrong axis, not wrong fact",
 "world": "house", "flag": "live", "cite": "Exam 17 Q50, Q54 · D3 §3.7",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M20 100V24" stroke-width="4"/><path d="M20 100h84" stroke-width="4"/>
   <path d="M14 30l6-8 6 8M96 94l8 6-8 6" stroke-width="4"/>
   <circle cx="52" cy="66" r="9" fill="#DFF2E7"/>
   <circle cx="80" cy="44" r="9" fill="#FF4757"/>
   <path d="M34 88l58-48" stroke="#2E7D5B" stroke-width="3" stroke-dasharray="6 6"/></g></svg>''',
 "story": "Both misses knew the material and sorted it on the <b>wrong dimension</b>. Examples were treated as "
          "an addition to better prose rather than a replacement for it; feedback was split by size rather "
          "than by whether the fixes collide.",
 "tell": "Prose failed → examples <b>supersede</b> it. Feedback splits on <b>interacting vs independent</b>. "
         "When two options both look correct, check which axis the question is actually sorting on.",
},
{
 "title": "The rules/ reflex is now a speed problem",
 "world": "house", "flag": "live", "cite": "Exam 17 Q9 ✓ 99s · Q41 ✗ 32s",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="60" cy="60" r="40" fill="#fff"/>
   <path d="M60 34v26l18 12" stroke-width="5"/>
   <path d="M60 20v6M100 60h-6M60 100v-6M20 60h6" stroke-width="4"/>
   <circle cx="60" cy="60" r="5" fill="#2E7D5B"/></g></svg>''',
 "story": "Same three-way discrimination, twice on one paper. Right when you gave it 99 seconds. Wrong when "
          "you gave it 32. <b>You know this — you just answer it too fast.</b>",
 "tell": "Fourth wrong <code>.claude/rules/</code> pick across three papers. When the options list file "
         "paths, that is the signal to slow down, not to go on instinct.",
},
{
 "title": "Composite vs bundling — five papers running",
 "world": "workshop", "flag": "live", "cite": "Exams 6, 8, 9, 10, 11 · D2 §2.8",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="32" cy="42" r="13" fill="#fff"/><circle cx="32" cy="80" r="13" fill="#fff"/>
   <path d="M45 42h12M45 80h12" stroke-dasharray="4 5"/>
   <rect x="60" y="48" width="44" height="26" rx="6" fill="#FDF0D8"/>
   <path d="M70 61h24" stroke-width="4"/>
   <path d="M82 30v12" stroke="#2E7D5B" stroke-width="4"/>
   <path d="M76 36l6-6 6 6" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "Your longest-running miss. Two tools that always travel together feel like they want merging — "
          "and the corpus says <b>don't merge them, just ask for both in one turn</b>.",
 "tell": "Prompt the agent to bundle related tool requests into a single turn. A composite tool hides the "
         "composition, and it is explicitly the not-preferred answer.",
},
{
 "title": "CLAUDE.md mechanics — six misses, five papers",
 "world": "house", "flag": "live", "cite": "Exams 4, 7, 8, 11, 12 · D3 §3.1",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="22" y="16" width="76" height="18" rx="4" fill="#fff"/>
   <rect x="22" y="42" width="76" height="18" rx="4" fill="#DFF2E7"/>
   <rect x="22" y="68" width="76" height="18" rx="4" fill="#fff"/>
   <path d="M60 34v8M60 60v8" stroke-width="4"/>
   <circle cx="60" cy="102" r="10" fill="#2E7D5B"/>
   <path d="M55 102l4 4 7-8" stroke="#fff" stroke-width="3.5"/></g></svg>''',
 "story": "Three separate mistakes wearing one coat: thinking a lower file <b>overrides</b> a higher one, "
          "reaching for a fix before running <code>/memory</code>, and forgetting the import depth.",
 "tell": "Files <b>concatenate</b>, root down — nothing overrides. Inconsistent behaviour is a discovery "
         "problem: run <code>/memory</code> first. <code>@import</code> nests to a maximum of 5.",
},
]


def page_red(card):
    cards = "\n".join(card(i) for i in LIVE)
    return f"""<section class="page" id="red">
  <header class="page-head">
    <div class="eyebrow">From eleven scored papers · 79 wrong answers traced</div>
    <h2>What is still open</h2>
    <p class="count">Six things. Everything else on your record is either cleared or a one-off.</p>
  </header>
  <div class="note hot">
    <h3>Read these six twice</h3>
    <p>This page is not the syllabus — it is <b>your</b> error record. Two of the six are not knowledge
    problems at all: the <code>.claude/rules/</code> one is a speed problem, and the prevention one is a
    transfer problem. Both are fixed by pausing, not by revising.</p>
  </div>
  <div class="cards">{cards}</div>
</section>"""


HEUR = [
 ("Fix the root cause, not the symptom", "Misrouting → fix tool descriptions, not add a classifier"),
 ("Proportionate first response", "Try the prompt/description fix before adding infrastructure — classifiers, routing layers, bigger models"),
 ("Programmatic enforcement for critical sequences", "Verify-before-refund → hook or precondition, never prompt-only"),
 ("Least privilege", "Scoped <code>verify_fact</code> for the synthesis agent, not full web search"),
 ("Deterministic over probabilistic", "Hooks and gates for guaranteed compliance; prompts for guidance"),
 ("Structured error context &gt; generic failure", "Failure type, attempted query, partial results, alternatives"),
 ("Parallel with shared context &gt; sequential", "Multi-issue requests: decompose and parallelise"),
 ("Coordinator as hub", "Subagents never talk to each other directly"),
 ("Independence for review passes", "Second instance without the generator's reasoning context"),
 ("Match the API to the latency requirement", "Blocking pre-merge → synchronous; overnight reports → batch"),
 ("Coverage gaps trace upstream", "Complete-looking subagent output + missing topics → check the decomposition"),
 ("Attention dilution → split passes", "Inconsistent 14-file review → per-file plus integration pass, not a bigger window"),
]


def page_rules():
    rows = "".join(f"<tr><td><b>{h}</b></td><td>{w}</td></tr>" for h, w in HEUR)
    return f"""<section class="page" id="rules">
  <header class="page-head">
    <div class="eyebrow">When two options both look right</div>
    <h2>The twelve tiebreakers</h2>
    <p class="count">Straight from the exam's own answer-pattern analysis</p>
  </header>
  <div class="note">
    <p class="big">Nearly every question is one of these wearing a costume. If you are stuck between two
    plausible options, find which heuristic applies and it will usually pick for you.</p>
    <table><thead><tr><th>Heuristic</th><th>When it fires</th></tr></thead><tbody>{rows}</tbody></table>
  </div>
  <div class="note hot">
    <h3>The one that has cost you most</h3>
    <p>Numbers 1, 2 and 5 are the same instinct viewed from three sides, and they account for the single
    biggest cluster in your record — reaching for something that <b>copes with</b> the failure instead of
    something that <b>removes</b> it. Post-processing, a fallback, a retry, an extra layer, a firmer
    instruction. If one option adds a stage and another deletes the problem, take the one that deletes it.</p>
  </div>
</section>"""


OUT = [
 "Fine-tuning or training custom Claude models",
 "Claude API authentication, billing, or account management",
 "Language/framework-specific implementation details (beyond tool/schema config)",
 "Deploying or hosting MCP servers (infrastructure, networking, containers)",
 "Claude's internal architecture, training process, or model weights",
 "Constitutional AI, RLHF, or safety training methodologies",
 "Embedding models or vector database implementation details",
 "Computer use (browser automation, desktop interaction)",
 "Image analysis / Vision capabilities",
 "Streaming API or server-sent events",
 "Rate limiting, quotas, or detailed API cost calculations",
 "OAuth, API key rotation, or authentication protocol details",
 "Cloud-provider-specific configurations (AWS, GCP, Azure)",
 "Performance benchmarks or model comparison metrics",
 "Prompt caching implementation details (beyond knowing it exists)",
 "Token counting algorithms or tokenization specifics",
]


def page_scope():
    lis = "".join(f"<li>{o}</li>" for o in OUT)
    return f"""<section class="page" id="scope">
  <header class="page-head">
    <div class="eyebrow">Officially excluded</div>
    <h2>Will not appear</h2>
    <p class="count">16 items · straight from the exam guide's own exclusion list</p>
  </header>
  <div class="note cool">
    <h3>If a question seems to need one of these, you have misread it</h3>
    <p>None of the following is examinable. If an option depends on knowing one, that option is almost
    certainly the distractor — and if a whole question seems to hinge on one, re-read the stem, because it
    is testing something else.</p>
    <ul class="tick cross">{lis}</ul>
  </div>
  <div class="note">
    <h3>Three that trip people specifically</h3>
    <p><b>Vector databases</b> are out of scope as an implementation topic — but "semantic retrieval over
    months of history" is still the right <i>answer</i> to a long-term-recall question. The concept is in;
    the implementation is out.</p>
    <p><b>Prompt caching</b> — you need to know it exists, nothing more.</p>
    <p><b>Cost</b> — the 50% batch discount is examinable because it drives a design decision. Detailed cost
    arithmetic is not.</p>
  </div>
</section>"""
