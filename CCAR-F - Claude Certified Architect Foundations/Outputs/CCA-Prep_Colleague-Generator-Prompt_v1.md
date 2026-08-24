# CCA-F Mock Test Generator — shareable kit

**Version:** 2.0 | 2026-08-19
**Purpose:** what Ram forwards to Infosys colleagues who ask for "the prompt" behind the CCA-F prep pack.
**The kit is two files, and nothing else:** this prompt, and `CCA-F_Generator-Corpus_v1.md`.

---

## Read this first (Ram — not for forwarding)

**v2 removes every dependency on the prep pack.** v1 read the corpus, the renderer and the dedup ledger out of the pack you had already sent. This version carries all of it. Someone who has never seen the pack can run this and get a working 60-question test.

**What changed to make that true.** Three couplings had to be cut:

| Was | Now |
|---|---|
| Corpus read from `Learning corpus/CCA-F_Corpus_v1.html` | `CCA-F_Generator-Corpus_v1.md`, shipped alongside |
| Renderer copied out of a `Test-N.html` in the pack | Embedded in this prompt as an appendix the agent extracts |
| Style profile computed from the pack's 450 questions | Measured once, stated as constants in Phase 2 |

The renderer in the appendix is your shell with three pack couplings removed: the top nav bar (six links into pack files), the citation linkifier (pointed at the pack's corpus HTML), and the results-card study links (four more pack links). Everything else — layout, pagination, hint mode, the countdown, scoring, the results card, JSON export, localStorage resume — is byte-for-byte yours.

**One deliberate downgrade.** Citations now render as plain text rather than clickable links. In your pack they linked into `CCA-F_Corpus_v1.html`; a standalone recipient has no such file, and a dead link is worse than no link. The section numbers still match your corpus exactly, so a reader searches `§1.6` in the corpus file instead. If you would rather keep live links for pack-holders, say so and I will make the appendix detect the pack and link when it is present.

**What is deliberately not in the kit:** the official Exam Guide PDF (Anthropic Partner Academy asset — colleagues with Academy access download their own), the `ccg-mirror` crawl, and `PRACTICE-TEST-STEMS_v1.md` with its 76 verbatim community stems. None of anyone else's question text travels. Details in Part C.

**How to send it.** Attach both files. Or paste Part A as text and attach the corpus — Part A carries the renderer inside it either way.

---
---

## Part A — the kit to forward

═══════════════════════════════════════════════════════════════════════

# Generate a CCA-F practice test

You are generating a complete 60-question practice exam for the Anthropic Claude Certified Architect — Foundations certification, and writing it out as a single self-contained HTML file.

## What this is, and what it is not

- This produces **practice** material. These are not real exam questions and no one involved has seen the live exam.
- This is **not affiliated with, endorsed by, or sponsored by Anthropic**.
- **Every factual claim in every question must come from the corpus file.** Never write a question from your own knowledge of Claude, the Agent SDK, or Claude Code. If the corpus does not say it, it does not go in the test. This is the single rule that separates useful practice from confidently wrong practice — a fabricated flag or an invented parameter teaches an error the learner will carry into the exam.
- Expect 20–40 minutes and a substantial number of tokens. You are writing 60 questions and 240 rationales.

## What you need

Two files, both of which came with this prompt:

1. **This prompt.** Its appendix contains the complete HTML renderer.
2. **`CCA-F_Generator-Corpus_v1.md`** — the grounding corpus. 73 numbered sections.

Nothing else. No prep pack, no downloads, no network.

---

## PHASE 0 — Check your inputs

Locate `CCA-F_Generator-Corpus_v1.md`. Ask the user for the path if it is not obvious.

If it is missing, **stop and say so**. Do not offer to proceed from general knowledge.

Also note the path of **this prompt file** if you have it on disk — Phase 6 extracts the renderer from it. If you only have this prompt as pasted text, Phase 6 has a fallback.

Ask the user where the finished test should be written. Default to the folder the corpus is in.

---

## PHASE 1 — Load the corpus

Read `CCA-F_Generator-Corpus_v1.md` in full. About 22,000 words, and it is the entire basis of the exam you are about to write.

| Part | What you use it for |
|---|---|
| 0 — Exam mechanics | Format, scoring, the six official scenarios with their primary domains, the in-scope and out-of-scope lists |
| 1–5 — Domains D1–D5 | The subject matter. 73 numbered sections, §1.1 through §5.14 |
| 6 — Key Distinctions | 29 documented traps. Your richest source of distractors |

**Two constraints live in Part 0 and are binding.** Read them there rather than from memory: the **out-of-scope list** — nothing on it may appear in a stem, an option or a rationale — and the **six-scenario bank** with each scenario's primary domains, which governs Phase 3.

### The quota table

The one planning number not in the corpus. A 60-question paper distributes by the official domain weights:

| Code | Domain | Weight | Questions in a 60 |
|---|---|---|---|
| D1 | Agentic Architecture & Orchestration | 27% | 16 |
| D2 | Tool Design & MCP Integration | 18% | 11 |
| D3 | Claude Code Configuration & Workflows | 20% | 12 |
| D4 | Prompt Engineering & Structured Output | 20% | 12 |
| D5 | Context Management & Reliability | 15% | 9 |

---

## PHASE 2 — Calibration and numbering

### Style constants

These are measured from 450 questions written against this corpus and calibrated to the official sample questions. Treat them as binding targets, not suggestions.

| Property | Target | Hard limit |
|---|---|---|
| Stem length | median 50–55 words | never above 95 |
| Option length | median around 16 words | never above 35 |
| Options carrying an inline code/config token | 20–25% exam-wide | concentrated in D2/D3, never forced |
| Options per question | exactly 4 | — |

**The code-token rate overshoots if you leave it to the blocks.** It is an exam-wide budget, but each block author only sees its own 60 options, and the D2/D3-heavy blocks naturally run high — a measured run came in at 23% and 23% for the two narrative-heavy blocks against 38% and 32% for the tool- and config-heavy ones, for a 30% exam-wide result against a 25% ceiling. Either give the config-heavy blocks a lower per-block allowance when you brief them in Phase 3, or plan to strip decorative tokens at Phase 5. Strip only scene-dressing: where the token *is* the tested distinction — `Grep` versus `Glob`, `context: fork` — removing it destroys the question.

**The four distractor archetypes** the real paper uses, and which yours should draw on: the *symptom-level fix* (treats the visible effect, not the cause), the *over-engineered answer* (correct but disproportionate), the *wrong problem* (solves something adjacent), and the *non-existent feature* (plausible-sounding but not real — only ever use this shape when the corpus documents the misconception; never invent the feature yourself).

### Numbering

Look in the output folder for existing `Test-*.html` files. Take the highest `exam_n` inside them and add 1. If there are none, this is **Test 1**.

One caveat if the user also has the original CCA-F prep pack in that folder: its multiple-response drill carries `exam_n: 8` internally and its dashboard reserves that number, so skip 8.

### Deduplication

Look for **any** `Test-*.html` the user already has — tests you generated before, and the original CCA-F prep pack's `Mock tests/` folder if they happen to have it. Ask; do not assume they have none. Extract each file's `const DATA` object and collect every stem.

This step is optional in the sense that the generator runs without it. It is not optional in value: skipping it is the single most likely way this run produces a test the user has effectively already sat.

No new stem may repeat or closely paraphrase one in that ledger. Testing the same corpus point again is fine — reusing the same situation, the same numbers-with-different-values, and the same tested distinction is not.

### The corpus's worked examples are an attractor — do not lift them

Many corpus sections carry a worked illustration, often labelled "Exam scenario". **Those illustrations are teaching material, not question material.** Any generation that writes straight from them converges on the same handful of situations, which means a "new" test quietly repeats one the user has already seen.

This is measured, not hypothetical. A generation run from this corpus with no ledger produced three questions that were reskins of existing ones at 0.31–0.40 word overlap: a procedural-coordinator prompt where only the registry name and the step count changed, a schema-drift scenario reusing "twice this quarter", and a skill flooding the context window fixed by `context: fork`. Each kept the corpus's own illustration and renamed the surface details.

So: take the **tested distinction** from the section and build a **different situation** around it — one the corpus does not itself use to explain the point. If the corpus illustrates a decomposition failure with a research brief, write yours around a migration plan or an incident review. Keep the misconception; change the world it lives in.

---

## PHASE 3 — Plan the exam before writing anything

**Format:** FULL-60 — four scenario blocks of 15. The renderer is built for exactly 60 questions.

**Pick 4 of the 6 scenarios** from corpus Part 0. If the user has generated tests before, prefer the least-used. State which four you drew.

**Write the block × domain allocation table.** Exam-wide totals must be D1 16, D2 11, D3 12, D4 12, D5 9. Let each block lean toward its scenario's primary domains — and inside any block, a non-primary domain must never outnumber a primary one.

**Assign corpus sections per block, disjointly** wherever the quota allows, so two blocks do not independently mine the same section. Where a domain's quota exceeds its section count, say which sections carry a second question and make sure those two questions test different points.

**Pre-plan the correct-answer letters before any option text exists.** This is what produces balance; checking afterwards is not enough. For each block build the multiset `{A×4, B×4, C×4, D×3}` and rotate which letter carries the short count — block 1 short on D, block 2 short on C, block 3 short on B, block 4 short on A. The exam then lands at 15/15/15/15. Shuffle each block's multiset into a random per-question order — never sorted, never grouped — and treat that as the block's answer key.

**Give each block one evolving narrative.** The same system, tools and metrics recurring across its 15 questions with the situation progressing — not 15 unrelated vignettes. Frame it generically: "your agent", "the pipeline", "production logs show". Never invent a company, product or persona name. A cold audit of all known real-exam question text found zero named fictional companies; inventing one is an immediate tell.

---

## PHASE 4 — Author the four blocks

Dispatch four parallel subagents, one per block. If parallel subagents are unavailable, write the blocks sequentially — the standard is identical.

Each subagent receives: its scenario and narrative, its domain allocation **with the specific corpus sections assigned to each question slot**, its pre-planned letter sequence (a subagent never invents its own), the style constants, and the schema below. A subagent cannot see its siblings, so anything that needs cross-block consistency has to be decided here and handed down.

### Per-question standard

- **Stem** opens with a concrete situation tied to the block narrative — log output, a metric ("12% of cases"), a config snippet, a reported symptom. Median 50–55 words, hard cap 95.
- **Exactly four options**, hard cap 35 words, grammatically parallel, no giveaways. The correct one sits at its pre-assigned letter.
- **Three distractors, each a documented misconception.** The corpus marks them with ❌ — there are over 200, and Part 6 collects the 29 highest-yield. Never fabricate a flag, parameter, tool or behaviour: real distractors trap partial understanding, they do not invent vocabulary.
- **Four rationales.** `whyRight` explains why the key is correct; one `whyWrong` per distractor names the misconception it encodes and why it fails here. This is also a quality gate — a distractor whose `whyWrong` cannot name a real misconception gets replaced.
- **Every rationale cites a section** as `Corpus §N.M`, taken from the corpus's own headings. **Keep the `§`** — it is how a reader finds the section, and the renderer styles it. Cite one section per rationale.

### Question schema

```json
{
  "g": 1,
  "block": 0,
  "domain": "D1",
  "stem": "...",
  "options": ["...", "...", "...", "..."],
  "correct": 2,
  "whyRight": {"text": "...", "cite": "Corpus §1.6"},
  "whyWrong": [
    {"option": 0, "text": "...", "cite": "Corpus §1.6"},
    {"option": 1, "text": "...", "cite": "Corpus §1.2"},
    {"option": 3, "text": "...", "cite": "Corpus §1.9"}
  ],
  "blockLabel": "Multi-Agent Research System"
}
```

`g` runs 1–60 across the whole exam. `block` is 0–3. `correct` is the zero-based index of the right option. `whyWrong` has exactly three entries, for the three indices that are not `correct`.

### Full DATA object

```json
{
  "exam_n": 1,
  "format": "FULL60",
  "quota": {"D1": 16, "D2": 11, "D3": 12, "D4": 12, "D5": 9},
  "domainNames": {
    "D1": "Agentic Architecture & Orchestration",
    "D2": "Tool Design & MCP Integration",
    "D3": "Claude Code Configuration & Workflows",
    "D4": "Prompt Engineering & Structured Output",
    "D5": "Context Management & Reliability"
  },
  "blocks": [{"label": "...", "narrative": "..."}],
  "questions": []
}
```

`blocks` has four entries in block order. Renumber `g` to 1–60 across the assembled exam when you merge the four blocks.

---

## PHASE 5 — Verification gate

Compute all nine checks across the assembled 60 questions. Do not touch any HTML until every one passes. Fix failures and re-run the whole gate — a fix can break a check that passed a moment ago. Report the computed numbers, not a claim that you checked.

1. Domain totals are exactly 16 / 11 / 12 / 12 / 9.
2. Correct-answer letters match the pre-plan; exam-wide distribution is 15 / 15 / 15 / 15.
3. Stem word median is 50–55; no stem over 95 words; no option over 35.
4. 20–25% of options carry an inline code or config token, concentrated in D2 and D3.
5. In every block, no non-primary domain outnumbers a primary domain.
6. No stem duplicates or closely paraphrases another — within this exam, and against any prior generated test in the folder.
7. Every question has a `whyRight` and exactly three `whyWrong`, each citing a `§N.M` that exists in the corpus and genuinely supports the point.
8. No invented company, product or persona name anywhere.
9. Nothing from the corpus's out-of-scope list — in a stem, an option, **or a rationale**. The trap to watch for is an out-of-scope technology used as a wrong answer: "you would need a vector database for this" is still a vector database appearing in the paper. Match on whole words when you check: substring matching flags "revision" for *vision*, "flaws" for *AWS*, and "provisioning" for *vision* again, and chasing those wastes a pass.

---

## PHASE 6 — Build the file

The renderer is in the appendix at the end of this prompt, between the `SHELL-BEGIN` and `SHELL-END` markers. It is complete and self-contained — no network, no dependencies, no pack.

**If you have this prompt as a file on disk**, extract it programmatically rather than retyping it. Copying 37KB by hand invites silent corruption:

```python
import re
PROMPT = r"<path to this prompt file>"
OUT    = r"<output folder>\Test-N.html"

src = open(PROMPT, encoding="utf-8").read()
shell = re.search(r"<!-- SHELL-BEGIN -->\n(.*?)\n<!-- SHELL-END -->", src, re.S).group(1)

data = open("exam_data.json", encoding="utf-8").read()   # your assembled DATA object
i = shell.index("const DATA = ")
start = shell.index("{", i)
depth = 0
for j in range(start, len(shell)):
    if shell[j] == "{": depth += 1
    elif shell[j] == "}":
        depth -= 1
        if depth == 0:
            end = j + 1; break
out = shell[:start] + data + shell[end:]
out = out.replace('const KEY = "cca-test-1";', 'const KEY = "cca-test-N";')
open(OUT, "w", encoding="utf-8").write(out)
```

**If you only have this prompt as pasted text**, write the appendix block out to `Test-N.html` first, then do the same DATA replacement.

Either way, two things change and nothing else:

1. The `const DATA = {...}` placeholder object becomes your assembled exam.
2. `const KEY = "cca-test-1";` becomes `"cca-test-N"` for your number. Skip this and the new test silently shares saved answers with an earlier one.

Everything else derives from `DATA` at runtime — `initChrome()` sets the page title, the test number in the hero and on the landing card, and the quota line. Do not hand-edit them.

---

## PHASE 7 — Report

State: the four scenarios drawn; the domain tally; the answer-letter distribution; stem median, stem max, option max and the code-token rate; the dedup result; each of the nine gate checks with its computed value; and the output path.

Then tell the user:

- Open the file directly in a browser. Nothing needs to be installed or served.
- Hint mode on turns the paper into a teaching session — the answer and all four rationales appear as soon as an option is picked. Hint mode off runs it as a timed 120-minute exam with everything withheld until submission.
- Answers and timings persist in the browser, so a paper can be left and resumed.
- The results card gives a per-domain and per-block breakdown, an estimated scaled score against the 720 pass line, and a "Copy results JSON" button.

## Known limits — say these plainly if asked

- Citations render as plain text, not links. Look the section up in `CCA-F_Generator-Corpus_v1.md` by its `§` number.
- The page loads three fonts from Google Fonts. On a network that blocks it, everything works and the type falls back. Nothing else touches the network.
- The corpus was authored against Exam Guide v0.2 and re-checked against v1.0 (effective July 2026); weights, all six scenarios, all thirty task statements and both scope lists were identical between them. Anything decision-critical should still be confirmed against the guide currently published on the Anthropic Partner Academy.
- Generated questions reflect the corpus, which reflects the published exam guide. They are not the exam.

---

## APPENDIX — the renderer

Everything between the two markers is one complete HTML file. Extract it verbatim.

```html
<!-- SHELL-BEGIN -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>CCA-F Practice Test</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>
:root{
  --ink:#1a1814; --ink2:#3d3a34; --ink3:#7a7670;
  --cream:#faf7f2; --cream2:#f2ede4; --cream3:#e8e1d4;
  --amber:#c8832a; --amber-light:#f5e6cc; --amber-dark:#8a5a1a;
  --teal:#2a7a6e; --teal-light:#d4f0ec;
  --coral:#c85a3a; --coral-light:#fae8e2;
  --green:#3a7a4a; --green-light:#e2f0e6;
  --blue:#2a5a8a; --blue-light:#ddeaf5;
  --violet:#6b4a8a; --violet-light:#ece2f5;
  --border:#ddd8ce; --shadow:0 2px 16px rgba(26,24,20,0.08);
  --radius:12px; --radius-sm:8px;
  --serif:'DM Serif Display',Georgia,serif; --sans:'DM Sans',system-ui,sans-serif;
  --mono:'JetBrains Mono',ui-monospace,Consolas,monospace;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:var(--sans);background:var(--cream);color:var(--ink);font-size:16px;line-height:1.7;}
.hero{background:var(--cream2);border-bottom:1px solid var(--border);color:var(--ink);padding:20px 40px 18px;text-align:center;}
.hero-eyebrow{font-family:var(--mono);font-size:11px;font-weight:500;letter-spacing:0.18em;text-transform:uppercase;color:var(--amber-dark);margin-bottom:8px;}
.hero h1{font-family:var(--serif);font-size:clamp(20px,3vw,28px);font-weight:400;line-height:1.15;margin-bottom:6px;color:var(--ink);}
.hero h1 em{font-style:italic;color:var(--amber-dark);}
.hero-sub{font-size:13px;font-weight:300;color:var(--ink2);max-width:620px;margin:0 auto 12px;line-height:1.5;}
.hero-tags{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;}
.tag{font-size:11px;font-weight:500;letter-spacing:0.06em;padding:4px 11px;border-radius:99px;border:1px solid var(--border);color:var(--ink2);background:#fff;}
.tag.new{border-color:var(--violet);color:var(--violet);background:var(--violet-light);}
.nav-bar{position:sticky;top:0;z-index:100;background:rgba(250,247,242,0.96);backdrop-filter:blur(8px);border-bottom:1px solid var(--border);padding:12px 40px;display:flex;flex-direction:column;}
.nav-bar-row{display:flex;align-items:center;gap:18px;}
.nav-progress{flex:1;min-width:0;}
.progress-track{height:8px;background:var(--cream2);border-radius:99px;overflow:hidden;}
.progress-fill{height:8px;background:linear-gradient(to right,var(--amber),var(--amber-dark));width:0;transition:width .4s;}
.progress-meta{font-family:var(--mono);font-size:11px;color:var(--ink3);margin-top:4px;letter-spacing:0.05em;display:flex;justify-content:space-between;gap:10px;}
.nav-timer{font-family:var(--mono);font-size:12px;font-weight:600;padding:6px 12px;border-radius:99px;background:var(--cream2);border:1px solid var(--border);color:var(--ink2);white-space:nowrap;}
.nav-timer.time-low{color:var(--coral);border-color:var(--coral);background:var(--coral-light);}
.score-pill{font-family:var(--mono);font-size:12px;font-weight:600;padding:6px 12px;border-radius:99px;background:var(--cream2);border:1px solid var(--border);color:var(--ink2);white-space:nowrap;}
.score-pill .ok{color:var(--green);} .score-pill .x{color:var(--coral);}
.pct-pill{font-family:var(--mono);font-size:12px;font-weight:700;padding:6px 12px;border-radius:99px;background:var(--cream2);border:1px solid var(--border);color:var(--ink3);white-space:nowrap;}
.pct-pill.pass{color:var(--green);border-color:var(--green);background:var(--green-light);}
.pct-pill.fail{color:var(--coral);border-color:var(--coral);background:var(--coral-light);}
.hint-toggle{display:flex;align-items:center;gap:7px;cursor:pointer;user-select:none;font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--ink2);white-space:nowrap;}
.hint-toggle input{position:absolute;opacity:0;width:0;height:0;}
.hint-slider{position:relative;width:34px;height:19px;background:var(--cream3);border:1px solid var(--border);border-radius:99px;transition:all .15s;flex-shrink:0;}
.hint-slider::before{content:"";position:absolute;top:1px;left:1px;width:15px;height:15px;background:#fff;border-radius:50%;box-shadow:0 1px 3px rgba(26,24,20,0.25);transition:all .15s;}
.hint-toggle input:checked + .hint-slider{background:var(--violet);border-color:var(--violet);}
.hint-toggle input:checked + .hint-slider::before{transform:translateX(15px);}
.hint-toggle input:focus-visible + .hint-slider{outline:2px solid var(--amber);outline-offset:2px;}
.container{max-width:840px;margin:0 auto;padding:36px 40px 80px;}
.start-card{background:var(--amber-light);border:1px solid #e8d0a0;border-radius:var(--radius);padding:30px 34px;margin:8px 0 34px;}
.start-card .kicker{font-family:var(--mono);font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:var(--amber-dark);margin-bottom:12px;}
.start-card h3{font-family:var(--serif);font-size:26px;font-weight:400;margin-bottom:12px;color:var(--ink);text-align:center;}
.start-card p{font-size:14px;color:var(--ink2);margin:0 auto 12px;line-height:1.7;max-width:620px;}
.start-facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:18px 0 6px;}
.sf{background:rgba(255,255,255,0.6);border:1px solid #e8d0a0;border-radius:var(--radius-sm);padding:12px 14px;}
.sf .k{font-family:var(--mono);font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--amber-dark);margin-bottom:5px;}
.sf .v{font-size:14px;color:var(--ink);font-weight:500;}
.sf.flag{border-color:var(--violet);background:var(--violet-light);}
.sf.flag .k{color:var(--violet);}
.scen-list{list-style:none;margin:10px 0 0;padding:0;display:flex;flex-direction:column;gap:6px;}
.scen-list li{font-size:13px;color:var(--ink2);padding-left:20px;position:relative;}
.scen-list li::before{content:"";position:absolute;left:4px;top:9px;width:7px;height:7px;border-radius:50%;background:var(--amber);}
.block-hdr{background:var(--ink);color:var(--cream);padding:26px 30px;border-radius:var(--radius);margin:38px 0 22px;}
.block-hdr .kicker{font-family:var(--mono);font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:var(--amber);margin-bottom:10px;}
.block-hdr h2{font-family:var(--serif);font-size:26px;font-weight:400;margin-bottom:10px;color:#fff;}
.block-hdr p{font-size:14px;color:rgba(250,247,242,0.82);line-height:1.7;}
.q-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:28px 30px;margin-bottom:18px;box-shadow:var(--shadow);}
.q-meta{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;gap:10px;}
.q-num{font-family:var(--mono);font-size:12px;font-weight:600;color:var(--amber);letter-spacing:0.08em;}
.q-domain{font-family:var(--mono);font-size:10px;font-weight:500;letter-spacing:0.1em;text-transform:uppercase;color:var(--blue);background:var(--blue-light);padding:3px 10px;border-radius:99px;}
.q-stem{font-family:var(--serif);font-size:18px;line-height:1.5;color:var(--ink);margin-bottom:20px;}
.q-stem code{font-family:var(--mono);font-size:14px;background:var(--cream2);padding:1px 6px;border-radius:4px;color:var(--ink2);}
.q-opts{display:flex;flex-direction:column;gap:10px;}
.opt{display:flex;align-items:flex-start;gap:12px;padding:13px 16px;border:1.5px solid var(--border);border-radius:var(--radius-sm);background:var(--cream2);cursor:pointer;transition:all .15s;font-size:14px;line-height:1.5;color:var(--ink2);}
.opt:hover:not(.locked){border-color:var(--amber);background:var(--cream);}
.opt.locked{cursor:default;}
.opt.pending{border-color:var(--violet);background:var(--violet-light);color:var(--ink);font-weight:500;}
.opt.pick-correct{border-color:var(--green);background:var(--green-light);color:var(--ink);font-weight:500;}
.opt.pick-wrong{border-color:var(--coral);background:var(--coral-light);color:var(--ink);}
.opt.reveal-correct{border-color:var(--green);background:var(--green-light);color:var(--ink);font-weight:500;}
.opt.dim{opacity:0.65;}
.opt-letter{font-family:var(--mono);font-size:13px;font-weight:600;flex-shrink:0;min-width:18px;}
.opt-mark{margin-left:auto;font-family:var(--mono);font-size:12px;font-weight:700;flex-shrink:0;text-align:right;}
.opt.pick-correct .opt-mark,.opt.reveal-correct .opt-mark{color:var(--green);}
.opt.pick-wrong .opt-mark{color:var(--coral);}
.feedback{margin-top:18px;border-radius:var(--radius-sm);overflow:hidden;display:none;border:1px solid var(--border);}
.feedback.shown{display:block;animation:fadeUp .35s ease;}
@keyframes fadeUp{from{opacity:0;transform:translateY(6px);}to{opacity:1;transform:translateY(0);}}
.fb-verdict{padding:12px 18px;font-family:var(--mono);font-size:12px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;}
.fb-verdict.ok{background:var(--green-light);color:var(--green);}
.fb-verdict.no{background:var(--coral-light);color:var(--coral);}
.fb-body{padding:6px 18px 16px;background:#fff;}
.fb-row{padding:12px 0;border-bottom:1px solid var(--cream2);}
.fb-row:last-child{border-bottom:none;}
.fb-row .lbl{font-family:var(--mono);font-size:10px;letter-spacing:0.1em;text-transform:uppercase;font-weight:600;margin-bottom:5px;display:flex;align-items:center;gap:8px;}
.fb-row.right .lbl{color:var(--green);}
.fb-row.wrong .lbl{color:var(--coral);}
.fb-row .opt-ref{font-family:var(--mono);font-size:11px;color:var(--ink3);font-weight:500;}
.fb-row .txt{font-size:13.5px;color:var(--ink2);line-height:1.6;}
.fb-row .cite{font-family:var(--mono);font-size:10.5px;color:var(--amber-dark);margin-top:5px;letter-spacing:0.03em;}
.fb-sub{font-family:var(--mono);font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink3);margin:6px 0 2px;}
.results{background:var(--ink);color:var(--cream);padding:40px 36px;border-radius:var(--radius);margin:44px 0 24px;text-align:center;display:none;}
.results.shown{display:block;}
.results h2{font-family:var(--serif);font-size:30px;font-weight:400;margin-bottom:8px;color:#fff;}
.results .score-big{font-family:var(--serif);font-size:52px;color:var(--amber);margin:14px 0 4px;}
.results .scaled{font-family:var(--mono);font-size:14px;color:rgba(250,247,242,0.8);margin-bottom:6px;}
.results .passline{font-family:var(--mono);font-size:12px;font-weight:600;padding:5px 14px;border-radius:99px;display:inline-block;margin-top:6px;}
.results .passline.pass{background:var(--green);color:#fff;}
.results .passline.fail{background:var(--coral);color:#fff;}
.results .caveat{font-size:12px;color:rgba(250,247,242,0.6);max-width:560px;margin:14px auto 0;line-height:1.6;font-style:italic;}
.res-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin-top:26px;text-align:left;}
.res-card{background:rgba(250,247,242,0.06);border:1px solid rgba(250,247,242,0.14);border-radius:var(--radius-sm);padding:13px 15px;}
.res-card .rc-name{font-family:var(--mono);font-size:9.5px;letter-spacing:0.08em;text-transform:uppercase;color:var(--amber);margin-bottom:6px;line-height:1.3;}
.res-card .rc-score{font-family:var(--serif);font-size:22px;color:#fff;}
.res-card .rc-pct{font-size:12px;color:rgba(250,247,242,0.6);}
.res-section-label{font-family:var(--mono);font-size:11px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(250,247,242,0.55);margin:28px 0 2px;text-align:left;}
.export{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:22px 24px;margin:24px 0;display:none;box-shadow:var(--shadow);}
.export.shown{display:block;}
.export h3{font-family:var(--serif);font-size:20px;font-weight:400;margin-bottom:6px;color:var(--ink);}
.export p{font-size:13px;color:var(--ink3);margin-bottom:14px;line-height:1.6;}
.export pre{background:var(--cream2);border:1px solid var(--border);border-radius:var(--radius-sm);padding:14px;font-family:var(--mono);font-size:11px;color:var(--ink2);overflow-x:auto;max-height:240px;white-space:pre;}
.btn{font-family:var(--sans);font-size:13px;font-weight:600;padding:9px 22px;border-radius:99px;border:1.5px solid var(--amber);background:var(--amber);color:#fff;cursor:pointer;transition:all .15s;}
.btn:hover:not(:disabled){background:var(--amber-dark);border-color:var(--amber-dark);}
.btn.ghost{background:transparent;color:var(--ink2);border-color:var(--border);}
.btn.ghost:hover{border-color:var(--ink2);background:var(--cream2);}
.export-actions{display:flex;gap:10px;margin-top:14px;flex-wrap:wrap;}
.submit-wrap{text-align:center;margin:30px 0;}
.submit-note{font-size:13px;color:var(--ink3);margin-bottom:12px;}
@media (max-width:720px){
  .container{padding:24px 16px 60px;}
  .nav-bar{padding:10px 16px;gap:12px;}
  .hero{padding:16px 16px 14px;}
  .block-hdr{padding:20px;}
  .nav-timer,.score-pill,.pct-pill{font-size:11px;padding:5px 9px;}
}
@media print{.nav-bar,.btn,.export{display:none!important;}body{background:#fff;}.q-card{break-inside:avoid;}#printAll{display:block;}}

.jump-toggle{font-family:var(--mono);font-size:11px;font-weight:600;color:var(--ink3);cursor:pointer;white-space:nowrap;user-select:none;}
.jump-toggle:hover{color:var(--amber-dark);}
.nav-jumpmap{display:none;}
.nav-jumpmap.open{display:block;padding-top:14px;margin-top:12px;border-top:1px solid var(--border);}
.jm-block{margin-bottom:10px;}
.jm-block:last-child{margin-bottom:0;}
.jm-block-label{font-family:var(--mono);font-size:10px;letter-spacing:0.08em;text-transform:uppercase;color:var(--ink3);margin-bottom:6px;}
.jm-dots{display:flex;flex-wrap:wrap;gap:6px;}
.dot{width:26px;height:26px;display:flex;align-items:center;justify-content:center;border-radius:6px;border:1.5px solid var(--border);background:var(--cream2);font-family:var(--mono);font-size:11px;font-weight:600;color:var(--ink3);cursor:pointer;transition:all .15s;position:relative;}
.dot:hover{border-color:var(--amber);}
.dot.answered{background:var(--teal-light);border-color:var(--teal);color:var(--teal);}
.dot.current{border-width:2px;border-color:var(--amber);box-shadow:0 0 0 2px var(--amber-light);}
.jm-actions{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:12px;padding-top:12px;border-top:1px solid var(--border);flex-wrap:wrap;}
.jm-legend{font-family:var(--mono);font-size:10px;color:var(--ink3);letter-spacing:0.06em;}
.block-tag{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:var(--amber-dark);background:var(--amber-light);display:inline-block;padding:6px 14px;border-radius:99px;margin-bottom:18px;}
.page-nav{display:flex;align-items:center;justify-content:space-between;margin-top:24px;gap:12px;}
.btn:disabled{background:var(--cream3);border-color:var(--border);color:var(--ink3);cursor:default;}
.btn.ghost:disabled{background:transparent;color:var(--border);border-color:var(--border);}
.start-actions{text-align:center;margin-top:20px;}
#printAll{display:none;}
</style>
<style id="packbar-css">
.packbar{font:500 13px/1.4 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 background:#141821;color:#c9d1e0;padding:.5rem .9rem;display:flex;flex-wrap:wrap;align-items:center;gap:.35rem .5rem}
.packbar .pb-lab{color:#8d97ab;font-weight:600;letter-spacing:.02em;text-transform:uppercase;font-size:11px;margin-right:.3rem}
.packbar a{color:#c9d1e0;text-decoration:none;padding:.2rem .5rem;border-radius:999px;border:1px solid transparent;white-space:nowrap}
.packbar a:hover{background:#252c3a;color:#fff}
.packbar a[aria-current="page"]{background:#3b6ef5;color:#fff;border-color:#3b6ef5}
.fb-row .cite a{color:var(--amber-dark);text-decoration:none;border-bottom:1px dotted currentColor}
.fb-row .cite a:hover{color:var(--amber);border-bottom-style:solid}
.rc-study{margin-top:9px;padding-top:8px;border-top:1px solid rgba(250,247,242,0.13);
 font-family:var(--mono);font-size:9.5px;letter-spacing:.04em;color:rgba(250,247,242,0.45);line-height:1.9}
.rc-study a{color:rgba(250,247,242,0.78);text-decoration:none;border-bottom:1px solid rgba(250,247,242,0.25)}
.rc-study a:hover{color:#fff;border-bottom-color:#fff}
.res-card.weak{border-color:rgba(232,120,90,0.55);background:rgba(232,120,90,0.09)}
.res-card.weak .rc-study{color:rgba(250,247,242,0.6)}
@media print{.packbar{display:none}}
</style>
</head>
<body>
<div class="hero">
  <div class="hero-eyebrow">Claude Certified Architect — Foundations</div>
  <h1>Test <em id="heroTestNum">1</em></h1>
  <p class="hero-sub">60 single-choice questions across 4 scenario blocks, weighted to the official exam. Exam simulation by default — turn on Hint (top right) anytime to see the full reasoning after each question, why the right answer is right and why each wrong one isn't.</p>
  <div class="hero-tags"><span class="tag">FULL-60</span><span class="tag">4 scenario blocks</span><span class="tag">Single-choice</span><span class="tag">Pass line 720</span></div>
</div>
<div class="nav-bar">
  <div class="nav-bar-row">
    <div class="nav-progress">
      <div class="progress-track"><div class="progress-fill" id="progFill"></div></div>
      <div class="progress-meta"><span id="progCount">0 / 60 answered</span></div>
    </div>
    <span class="nav-timer" id="navTimer">120:00</span>
    <span class="score-pill" id="scorePill" style="display:none"><span class="ok">0 right</span> · <span class="x">0 wrong</span></span>
    <span class="pct-pill" id="pctPill" style="display:none">—%</span>
    <label class="hint-toggle"><input type="checkbox" id="hintCheckbox" onchange="setHintMode(this.checked)"/><span class="hint-slider"></span><span>Hint</span></label>
    <span class="jump-toggle" id="jumpToggle" onclick="toggleJumpMap()">▸ Jump to question</span>
  </div>
  <div class="nav-jumpmap" id="navJumpMap"></div>
</div>
<div class="container">
  <div class="start-card" id="startCard">
    <div class="kicker">Before you begin</div>
    <h3>Test <em id="startTestNum">1</em></h3>
    <p>A full-length practice exam for the Claude Certified Architect exam: 60 single-choice questions across 4 scenario blocks, weighted to the official domain breakdown.</p>
    <div class="start-facts">
      <div class="sf"><div class="k">Format</div><div class="v">60 single-choice questions · 4 blocks</div></div>
      <div class="sf"><div class="k">Domain quota</div><div class="v" id="quotaText">—</div></div>
      <div class="sf"><div class="k">Pass line</div><div class="v">720 / 1000 scaled</div></div>
      <div class="sf"><div class="k">Time limit</div><div class="v">120 minutes</div></div>
    </div>
    <div class="sf flag" style="margin-top:12px"><div class="k">Hint toggle</div><div class="v" style="font-weight:400;font-size:13px;line-height:1.6;">Off by default, to simulate real exam conditions — no feedback while you work, just a 120:00 countdown. Turn Hint on anytime, including mid-exam, to see the correct answer and full explanation immediately after each question, plus a live right/wrong score in place of the countdown.</div></div>
    <div class="sf" style="margin-top:12px;background:rgba(255,255,255,0.6)"><div class="k">Scenarios in this test</div>
      <ul class="scen-list" id="scenList" style="list-style:none;margin:10px 0 0;padding:0;display:flex;flex-direction:column;gap:6px;"></ul>
    </div>
    <div class="start-actions"><button class="btn" onclick="goToQuestion(1)">Begin exam →</button></div>
  </div>
  <div id="exam"></div>
  <div class="results" id="results"></div>
  <div class="export" id="export">
    <h3>Results JSON</h3>
    <p>Copy this if you want a structured record of this attempt.</p>
    <pre id="exportJson"></pre>
    <div class="export-actions"><button class="btn" onclick="copyJson()">Copy results JSON</button><button class="btn ghost" onclick="printAll()">Print full exam</button><button class="btn ghost" onclick="resetExam()">Reset this exam</button></div>
  </div>
</div>
<script>
const KEY = "cca-test-1";   // bump per generated test
const DOM_ORDER = ["D1","D2","D3","D4","D5"];
// Pass-equivalent raw-percentage threshold, derived from round((correct/60)*900+100) >= 720:
// correct/60 >= 620/900 = 31/45 ~= 68.8889% -- NOT a round number, computed precisely, not assumed.
const PASS_PCT_THRESHOLD = 620/9; // = 68.888...
let hintMode = false; // off = exam simulation (default); on = immediate per-question reveal + study aids
let state = load();
let currentG = null;          // 1..60 while viewing a question; null on landing/results
let currentView = "landing";  // "landing" | "question" | "results"
let jumpMapOpen = false;

function load(){
  try{
    const s=JSON.parse(localStorage.getItem(KEY));
    if(s&&s.answers){ return s; }
  }catch(e){}
  return {answers:{}, times:{}, started:null, firstShownAt:{}};
}
function save(){localStorage.setItem(KEY,JSON.stringify(state));}

function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function code(s){return esc(s).replace(/`([^`]+)`/g,'<code>$1</code>');}
function letter(i){return String.fromCharCode(65+i);}

function fmtTime(sec){sec=Math.max(0,Math.round(sec));const m=Math.floor(sec/60),s=sec%60;return m+":"+String(s).padStart(2,"0");}

function isRight(q,ans){ return ans!==null && ans!==undefined && ans===q.correct; }
function answerLetters(q,ans){ return (ans===null||ans===undefined) ? null : letter(ans); }

function setView(mode){
  currentView = mode;
  document.getElementById("startCard").style.display = (mode==="landing") ? "" : "none";
  document.getElementById("exam").style.display = (mode==="question") ? "" : "none";
  document.getElementById("jumpToggle").style.display = (mode==="landing") ? "none" : "";
  if(mode==="landing") collapseJumpMap();
  if(mode!=="results"){
    document.getElementById("results").classList.remove("shown");
    document.getElementById("export").classList.remove("shown");
  }
}

function collapseJumpMap(){
  jumpMapOpen = false;
  document.getElementById("navJumpMap").classList.remove("open");
  document.getElementById("jumpToggle").textContent = "▸ Jump to question";
}

function toggleJumpMap(){
  jumpMapOpen = !jumpMapOpen;
  document.getElementById("navJumpMap").classList.toggle("open", jumpMapOpen);
  document.getElementById("jumpToggle").textContent = (jumpMapOpen?"▾":"▸") + " Jump to question";
}

function isFirstOfBlock(q){
  const idx = DATA.questions.indexOf(q);
  return idx===0 || DATA.questions[idx-1].block !== q.block;
}

function renderBlockHdr(blockIdx){
  const b = DATA.blocks[blockIdx];
  return `<div class="block-hdr"><div class="kicker">Scenario Block ${blockIdx+1} of 4</div><h2>${esc(b.label)}</h2><p>${code(b.narrative)}</p></div>`;
}

function renderJumpMap(){
  let rows = "";
  for(let b=0; b<DATA.blocks.length; b++){
    const qs = DATA.questions.filter(q=>q.block===b);
    const chips = qs.map(q=>{
      const answered = q.g in state.answers;
      const cls = "dot"+(answered?" answered":"")+(q.g===currentG?" current":"");
      const t = `Q${q.g}${answered?' · answered':''}`;
      return `<span class="${cls}" onclick="goToQuestion(${q.g})" title="${t}">${q.g}</span>`;
    }).join("");
    rows += `<div class="jm-block"><div class="jm-block-label">Block ${b+1} · ${esc(DATA.blocks[b].label)}</div><div class="jm-dots">${chips}</div></div>`;
  }
  rows += `<div class="jm-actions"><span class="jm-legend">Teal = answered</span><span class="submit-note" id="submitNote"></span><button class="btn ghost" onclick="submitExam()">Show results now</button></div>`;
  document.getElementById("navJumpMap").innerHTML = rows;
}

function renderPage(g, opts={}){
  const scrollTop = opts.scrollTop !== false;
  const q = DATA.questions.find(x=>x.g===g);
  currentG = g;
  setView("question");

  let h = isFirstOfBlock(q) ? renderBlockHdr(q.block)
                             : `<div class="block-tag">Block ${q.block+1} of 4 · ${esc(DATA.blocks[q.block].label)}</div>`;
  h += renderQ(q);

  const answered = g in state.answers;
  const isLast = (g===60);
  h += `<div class="page-nav">
    <button class="btn ghost" id="backBtn" onclick="goBack()" ${g===1?'disabled':''}>← Back</button>
    <button class="btn" id="nextBtn" onclick="${isLast?'submitExam()':'goNext()'}" ${answered?'':'disabled'}>${isLast?'Show my results':'Next →'}</button>
  </div>`;

  document.getElementById("exam").innerHTML = h;

  markShown(q);
  if(answered){ if(hintMode) paintAnswered(q); else paintExamSelected(q); }
  renderJumpMap();
  updateNav();
  if(scrollTop) window.scrollTo(0,0);
}

function goNext(){
  if(!(currentG in state.answers)) return;
  if(currentG < 60) renderPage(currentG+1);
}

function goBack(){
  if(currentG > 1) renderPage(currentG-1);
}

function goToQuestion(g){
  if(g<1 || g>60) return;
  collapseJumpMap();
  renderPage(g);
}

function renderQ(q){
  const opts=q.options.map((o,i)=>
    `<div class="opt" id="opt-${q.g}-${i}" onclick="pick(${q.g},${i})">`+
    `<span class="opt-letter">${letter(i)}</span><span class="opt-text">${code(o)}</span><span class="opt-mark" id="mark-${q.g}-${i}"></span></div>`
  ).join("");
  return `<div class="q-card" id="q-${q.g}" data-domain="${q.domain}" data-block="${q.block}">
    <div class="q-meta"><span class="q-num">Q${q.g} / 60</span><span class="q-domain" title="${esc(DATA.domainNames[q.domain])}">${q.domain} · ${esc(DATA.domainNames[q.domain])}</span></div>
    <div class="q-stem">${code(q.stem)}</div>
    <div class="q-opts">${opts}</div>
    <div class="feedback" id="fb-${q.g}"></div>
  </div>`;
}

function markShown(q){ if(!(q.g in state.firstShownAt)){ state.firstShownAt[q.g]=Date.now(); } }

function commit(q,ans){
  if(state.started===null){state.started=Date.now();}
  const shown = state.firstShownAt[q.g] || state.started || Date.now();
  state.times[q.g]=Math.max(1,Math.round((Date.now()-shown)/1000));
  state.answers[q.g]=ans;
  save();
  renderPage(q.g,{scrollTop:false});
  const btn=document.getElementById("nextBtn");
  if(btn){ btn.scrollIntoView({behavior:"smooth",block:"end"}); btn.focus({preventScroll:true}); }
}

function pick(g,i){
  if(g in state.answers) return; // locked once answered, regardless of Hint
  const q=DATA.questions.find(x=>x.g===g);
  if(state.started===null){state.started=Date.now();}
  commit(q,i);
}

// Hint off: highlight the chosen option, no correctness color, no rationale.
function paintExamSelected(q){
  const ans=state.answers[q.g];
  q.options.forEach((o,i)=>{
    const el=document.getElementById(`opt-${q.g}-${i}`);
    const mk=document.getElementById(`mark-${q.g}-${i}`);
    if(!el) return;
    el.classList.add("locked");
    el.classList.remove("pick-correct","pick-wrong","reveal-correct","dim");
    el.classList.toggle("pending", i===ans);
    if(mk) mk.textContent = (i===ans) ? "selected" : "";
  });
  const fb=document.getElementById(`fb-${q.g}`);
  if(fb){ fb.innerHTML=""; fb.classList.remove("shown"); }
}

function paintAnswered(q){
  const ans=state.answers[q.g];
  q.options.forEach((o,i)=>{
    const el=document.getElementById(`opt-${q.g}-${i}`);
    const mk=document.getElementById(`mark-${q.g}-${i}`);
    if(!el) return;
    el.classList.add("locked");
    el.classList.remove("pending","pick-correct","pick-wrong","reveal-correct","dim");
    mk.textContent="";
    if(i===ans && i===q.correct){el.classList.add("pick-correct");mk.textContent="✓ your answer";}
    else if(i===ans && i!==q.correct){el.classList.add("pick-wrong");mk.textContent="✗ your answer";}
    else if(i===q.correct){el.classList.add("reveal-correct");mk.textContent="✓ correct";}
    else{el.classList.add("dim");}
  });
  renderFeedback(q,ans);
}

function citeHref(cite){
  // Standalone build: citations render as plain text.
  // Look the section up in CCA-F_Generator-Corpus_v1.md by its § number.
  return "";
}
function fbRow(cls,label,ref,txt,cite){
  let citeBlock="";
  if(cite){
    const href=citeHref(cite);
    citeBlock = href
      ? `<div class="cite">Source: <a href="${href}" target="_blank" rel="noopener" title="Open this section of the corpus">${esc(cite)}</a></div>`
      : `<div class="cite">Source: ${esc(cite)}</div>`;
  }
  return `<div class="fb-row ${cls}"><div class="lbl">${label}${ref?`<span class="opt-ref">${ref}</span>`:""}</div><div class="txt">${code(txt)}</div>${citeBlock}</div>`;
}

function renderFeedback(q,ans){
  const fb=document.getElementById(`fb-${q.g}`);
  if(!fb) return;
  const wrongByOpt={}; q.whyWrong.forEach(w=>wrongByOpt[w.option]=w);
  const ok = isRight(q,ans);
  const all = q.options.map((_,i)=>i);
  let rows="";

  if(ok){
    rows+=fbRow("right",`✓ Correct — why ${letter(q.correct)} is right`,"",q.whyRight.text,q.whyRight.cite);
    rows+=`<div class="fb-sub">Why the other options are wrong</div>`;
    all.filter(i=>i!==q.correct).forEach(i=>{
      const w=wrongByOpt[i]; if(w) rows+=fbRow("wrong",`Option ${letter(i)}`,"",w.text,w.cite);
    });
    fb.innerHTML=`<div class="fb-verdict ok">Correct</div><div class="fb-body">${rows}</div>`;
  }else{
    const w=wrongByOpt[ans];
    rows+=`<div class="fb-sub">Your answer</div>`;
    rows+=fbRow("wrong",`✗ Why ${letter(ans)} is wrong`,"",w?w.text:"",w?w.cite:"");
    rows+=`<div class="fb-sub">The correct answer</div>`;
    rows+=fbRow("right",`✓ ${letter(q.correct)} is correct`,"",q.whyRight.text,q.whyRight.cite);
    const rest = all.filter(i=>i!==q.correct && i!==ans);
    if(rest.length){
      rows+=`<div class="fb-sub">The other incorrect options</div>`;
      rest.forEach(i=>{
        const w2=wrongByOpt[i]; if(w2) rows+=fbRow("wrong",`Option ${letter(i)}`,"",w2.text,w2.cite);
      });
    }
    fb.innerHTML=`<div class="fb-verdict no">Not quite</div><div class="fb-body">${rows}</div>`;
  }
  fb.classList.add("shown");
}

function updateNav(){
  const answered=Object.keys(state.answers).length;
  document.getElementById("progFill").style.width=(answered/60*100)+"%";
  document.getElementById("progCount").textContent=answered+" / 60 answered";
  let correct=0;
  for(const g in state.answers){
    const q=DATA.questions.find(x=>x.g==g);
    if(q&&isRight(q,state.answers[g]))correct++;
  }
  document.getElementById("scorePill").innerHTML=`<span class="ok">${correct} right</span> · <span class="x">${answered-correct} wrong</span>`;
  const pctPill=document.getElementById("pctPill");
  if(answered===0){
    pctPill.textContent="—%";
    pctPill.classList.remove("pass","fail");
  }else{
    const rawPct=correct/answered*100;
    pctPill.textContent=Math.round(rawPct)+"%";
    pctPill.classList.toggle("pass", rawPct>=PASS_PCT_THRESHOLD);
    pctPill.classList.toggle("fail", rawPct<PASS_PCT_THRESHOLD);
  }
  const note=document.getElementById("submitNote");
  if(note) note.textContent = answered<60 ? `${60-answered} question(s) still unanswered — you can submit now or finish them first.` : "All 60 answered.";
}

// Always a 120:00 countdown, regardless of Hint — Hint only changes which nav element is displayed.
setInterval(()=>{
  const t=document.getElementById("navTimer");
  if(!t)return;
  if(state.started===null){t.textContent="120:00";return;}
  const elapsed=(Date.now()-state.started)/1000;
  const remain=Math.max(0,7200-elapsed);
  t.textContent=fmtTime(remain);
  t.classList.toggle("time-low", remain<600);
},1000);

function totalSeconds(){
  return Object.values(state.times).reduce((a,b)=>a+b,0);
}

function setHintMode(on){
  hintMode = on;
  document.getElementById("navTimer").style.display = hintMode ? "none" : "";
  document.getElementById("scorePill").style.display = hintMode ? "" : "none";
  document.getElementById("pctPill").style.display = hintMode ? "" : "none";
  updateNav();
  if(currentView==="question" && currentG!==null){
    const q=DATA.questions.find(x=>x.g===currentG);
    if(q && (q.g in state.answers)){ if(hintMode) paintAnswered(q); else paintExamSelected(q); }
  }
}

function submitExam(){
  setView("results");
  const perDom={}, perBlock={};
  DOM_ORDER.forEach(d=>perDom[d]={correct:0,of:DATA.quota[d]});
  DATA.blocks.forEach((b,i)=>perBlock[i]={label:b.label,correct:0,of:0});
  let totalCorrect=0;
  const qlist=[];
  DATA.questions.forEach(q=>{
    const ans = (q.g in state.answers)?state.answers[q.g]:null;
    const ok = isRight(q,ans);
    if(ok){totalCorrect++;perDom[q.domain].correct++;perBlock[q.block].correct++;}
    perBlock[q.block].of++;
    qlist.push({q:q.g,domain:q.domain,block:q.block+1,type:"single",
                selected:answerLetters(q,ans),correct:ok,seconds:state.times[q.g]||null});
  });
  const scaled=Math.round((totalCorrect/60)*900+100);
  const pass=scaled>=720;
  const tSec=totalSeconds();

  let grid=DOM_ORDER.map(d=>{
    const c=perDom[d];const pct=Math.round(c.correct/c.of*100);
    const k=d.toLowerCase();
    const study="";
    return `<div class="res-card${pct<70?' weak':''}"><div class="rc-name">${d} · ${esc(DATA.domainNames[d])}</div><div class="rc-score">${c.correct}/${c.of}</div><div class="rc-pct">${pct}%</div>${study}</div>`;
  }).join("");
  let bgrid=Object.values(perBlock).map(b=>{
    const pct=Math.round(b.correct/b.of*100);
    return `<div class="res-card"><div class="rc-name">${esc(b.label)}</div><div class="rc-score">${b.correct}/${b.of}</div><div class="rc-pct">${pct}%</div></div>`;
  }).join("");
  const r=document.getElementById("results");
  r.innerHTML=`<h2>Test ${DATA.exam_n} · Results</h2>
    <div class="score-big">${totalCorrect} / 60</div>
    <div class="scaled">Estimated scaled score: ${scaled} / 1000</div>
    <div class="passline ${pass?'pass':'fail'}">${pass?'Above':'Below'} pass line (720)</div>
    <div class="scaled" style="margin-top:10px">Total time: ${fmtTime(tSec)}</div>
    <div class="res-section-label">By domain (official weights)</div>
    <div class="res-grid">${grid}</div>
    <div class="res-section-label">By scenario block</div>
    <div class="res-grid">${bgrid}</div>
    <p class="caveat">This scaled figure is a linear approximation. The real exam uses psychometric scaling across equated forms, so treat it as a rough gauge, not a prediction.</p>
    <p class="caveat">Any domain below 70% is marked. Follow its <b>Study this</b> links — they open that domain in the Guide, the Atlas, the Trap Sheet and the Corpus. Every <b>Source</b> line in the question feedback above is also a live link into the corpus section it cites.</p>`;
  r.classList.add("shown");

  const payload={
    test_n:DATA.exam_n, format:DATA.format, attempted_date:new Date().toISOString().slice(0,10),
    total_correct:totalCorrect, total_questions:60, total_seconds:tSec,
    estimated_scaled:scaled,
    domains:Object.fromEntries(DOM_ORDER.map(d=>[d,{correct:perDom[d].correct,of:perDom[d].of}])),
    blocks:Object.values(perBlock).map(b=>({scenario:b.label,correct:b.correct,of:b.of})),
    questions:qlist
  };
  document.getElementById("exportJson").textContent=JSON.stringify(payload,null,2);
  document.getElementById("export").classList.add("shown");
  r.scrollIntoView({behavior:"smooth"});
}

function copyJson(){
  const t=document.getElementById("exportJson").textContent;
  navigator.clipboard.writeText(t).then(()=>{
    const b=event.target;const o=b.textContent;b.textContent="Copied ✓";setTimeout(()=>b.textContent=o,1600);
  }).catch(()=>{
    const rng=document.createRange();rng.selectNode(document.getElementById("exportJson"));
    window.getSelection().removeAllRanges();window.getSelection().addRange(rng);
  });
}

function resetExam(){
  if(!confirm(`Clear all your answers and timing for Test ${DATA.exam_n}?`))return;
  localStorage.removeItem(KEY);state={answers:{},times:{},started:null,firstShownAt:{}};
  currentG=null;
  setView("landing");
  updateNav();
  window.scrollTo(0,0);
}

function printAll(){
  document.getElementById("exam").innerHTML = "";  // clear any stale question left in #exam to avoid duplicate-id collisions below
  const box = document.createElement("div");
  box.id = "printAll";
  let h = "";
  DATA.questions.forEach(q=>{
    if(isFirstOfBlock(q)) h += renderBlockHdr(q.block);
    h += renderQ(q);
  });
  box.innerHTML = h;
  document.body.appendChild(box);
  DATA.questions.forEach(q=>{ if(q.g in state.answers) paintAnswered(q); });
  window.print();
  document.body.removeChild(box);
}

function initChrome(){
  document.title = `Test ${DATA.exam_n} · CCA-F Practice`;
  document.getElementById("heroTestNum").textContent = DATA.exam_n;
  document.getElementById("startTestNum").textContent = DATA.exam_n;
  document.getElementById("quotaText").textContent = DOM_ORDER.map(d=>`${d} ${DATA.quota[d]}`).join(" · ");
  document.getElementById("scenList").innerHTML = DATA.blocks.map(b=>`<li>${esc(b.label)}</li>`).join("");
  document.getElementById("hintCheckbox").checked = false;
  setHintMode(false);
}

function routeOnLoad(){
  initChrome();
  renderJumpMap();
  if(state.started===null){
    setView("landing");
    updateNav();
    return;
  }
  const next=DATA.questions.find(q=>!(q.g in state.answers));
  if(next) renderPage(next.g);
  else submitExam();
}
window.addEventListener("DOMContentLoaded", routeOnLoad);

const DATA = {
  /* REPLACE THIS ENTIRE OBJECT WITH YOUR GENERATED EXAM DATA. */
  "exam_n": 1, "format": "FULL60",
  "quota": {"D1": 16, "D2": 11, "D3": 12, "D4": 12, "D5": 9},
  "domainNames": {"D1": "Agentic Architecture & Orchestration",
    "D2": "Tool Design & MCP Integration",
    "D3": "Claude Code Configuration & Workflows",
    "D4": "Prompt Engineering & Structured Output",
    "D5": "Context Management & Reliability"},
  "blocks": [], "questions": []
};
</script>
</body>
</html>
<!-- SHELL-END -->
```

═══════════════════════════════════════════════════════════════════════

---
---

## Part B — reply for anyone asking about "the corpus prompt"

Paste this as-is.

> There's no prompt that builds the corpus — but here's the corpus itself.
>
> `CCA-F_Generator-Corpus_v1.md` (attached) is the whole thing in one file: exam mechanics, all five domains across 73 numbered sections, and 29 documented exam traps. About 22,000 words.
>
> Use it two ways. Read it directly if you want the source behind any wrong-answer explanation in the practice tests. Or pair it with the generator prompt (also attached), which reads it and writes you a fresh 60-question paper as a self-contained HTML file. Those two files are the whole kit — nothing else needed, no install, no network.
>
> On how it was made: it wasn't prompted into existence. It was written over a couple of months against Anthropic's official Exam Guide and audited section by section against the 30 official task statements. A community study guide (github.com/paullarionov/claude-certified-architect) was used for depth, never as authority. If you want to build your own instead, that's the honest path — download the Exam Guide from the Partner Academy yourself and work the 30 task statements one at a time. I can't share my copy of the guide; it's Anthropic's.
>
> Usual caveat: this is study material, not affiliated with or endorsed by Anthropic, and it contains no real exam questions.

---
---

## Part C — what travels and what doesn't (Ram's reference)

**Shipped as `CCA-F_Generator-Corpus_v1.md`** — assembled verbatim from `CCA-Prep_Exam-Mechanics_v2.md`, `CCA-Prep_Domain-1..5_v2.md` and `CCA-Prep_Key-Distinctions_v1.md`. Stripped: each file's version/changelog/source header, cross-references to files that stay behind, and one dead pointer to an `EXAM-LOG.md` line number. Retained: 73 sections, 139 tables, 64 code blocks, 207 ❌ misconception markers, all 29 traps. Rebuild any time by running `Outputs/build_corpus.py`.

**Shipped inside the prompt** — the renderer, derived from `Test-1.html` by `Outputs/build_shell.py`. Removed: the packbar nav, the citation linkifier, and the results-card study links. Everything else untouched.

| Held back | Reason |
|---|---|
| `source/CCA-F-Official-Exam-Guide_v1.0.pdf` | Anthropic Partner Academy asset. Colleagues with Academy access download their own. Part B says this explicitly. |
| `Outputs/ccg-mirror/` | A crawl of a third-party community site. |
| `PRACTICE-TEST-STEMS_v1.md` | Carries 76 community practice-test stems verbatim. Phase 2 states the derived style constants instead, so the numbers survive and nobody else's text moves. |
| `EXAM-LOG.md`, `GENERATION-INTELLIGENCE.md`, `SESSION-STATE.md` | Your learner state and cross-session learning loop. Dropped by design — no state for a cold user to corrupt. |
| `tools/archetype_gate.py` | Its checks are reproduced inline as Phase 5. |
| `CCA-Orchestration-Prompt_v10.md` | 1,100 lines assuming your folder layout, absolute paths and state files. Part A is the distilled, portable version. |
| The pack's 450 questions | They were v1's dedup ledger and style source. v2 needs neither: a standalone user has never seen them, and the style profile is now stated as constants. |

**Carried forward from v10:** domain quotas, scenario rotation with primary-domain checks, answer-letter pre-planning, the word-count budget, the code-token rate band, generic scenario framing, per-option rationales with section citations, and the out-of-scope hard constraint — the fidelity work that closed findings PB-08 through PB-11.

**Dropped:** the Professor's Note, the three-exam insights cadence, corpus-freshness tracking, the Open Findings Ledger, and DRILL-30 (the renderer hardcodes the question count in fourteen places in its JavaScript alone, so a 30-question variant means editing the shell).
