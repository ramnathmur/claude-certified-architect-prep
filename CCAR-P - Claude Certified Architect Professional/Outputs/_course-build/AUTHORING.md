# Authoring contract: one objective chapter

The standard is `fragments/o1.2.html` and `fragments/o3.5.html`. Read both before writing. They passed the gates and two cold-review rounds. Match their shape, voice and care.

## Inputs and outputs

- Input: the pack `_authoring/packs/<ID>.md` (made by `node tools/make-pack.js <ID>`). It holds the guide's objective, every corpus section verbatim, each facet ID with its decision row, the lesson text, and the list of pages and anchors that already exist.
- Output: ONE file per chapter, `fragments/<id>.html` (lower case, for example `o2.1.html`). Domain openers are `fragments/d<n>.html`.
- Never edit anything else: not `src/`, `build.js`, `gates.js`, `data/`, other fragments, the corpus, or `Outputs/CCAR-P_Syllabus-Course_v1.html`. Parallel authors share the folder.
- Write the fragment to disk as soon as a first full draft exists, then improve it in place. Do not hold a finished chapter in memory.

## Self-check (run before reporting)

```
COURSE_OUT="<Outputs>/_course-build/_priv/<id>.html" GATE_PAGES=<id> node build.js
```
It builds to a private file and checks only your page. Fix every FAIL. Treat every WARN as a defect unless you can say why it is right. Run it from `_course-build`. Never run `build.js` without `COURSE_OUT`.

## Anatomy, in this order

1. `<div class="chapter"><div class="main">`
2. Opening, 1 to 3 short paragraphs: a concrete case with real numbers before any abstraction. Vary the opening move from chapter to chapter. No title, no eyebrow.
3. One `<section class="concept" id="c<sec>" data-src="<sec>" data-terms="...">` per corpus section (all sections of the objective, in the order that teaches best; the order need not follow the numbers). Inside: `<h3>Plain-language title<span class="sec">§x.y</span></h3>`, 1 to 3 paragraphs of at most 75 words each, an optional `figure.fig`, then `<ul class="rules">` with the header row and one `<li data-facet="F-x.y-nn">` per facet (`span.when`, `span.then` plus `span.why`). Every facet ID in the pack must appear. Sections with no facets still get a concept block.
4. Optional `<details class="deeper"><summary>Go deeper: ...</summary><div>...</div></details>` for mechanics, arithmetic or a live-docs fact. Label worked examples "a worked example, not a corpus rule".
5. `<section class="bites" id="b-<id>">`: `h2` "Where the exam bites"; one paragraph starting `<span class="lbl">Known</span>` (what the guide shows: only Domains 3, 2 and 4 have an official sample, one each; say so honestly for other domains) and `<span class="lbl">Inference</span>` for anything else; then one or two corpus scenarios as `p.stem` + `ul.opts` (`li.ok` with `span.mark` Correct, `li.no` with Wrong and `<a class="fam" href="#/traps/f-...">FAMILY</a>`). Families are linked, never defined here. Use the tags the corpus gives. Say in plain words why each wrong option fails.
6. `<details class="say">` with `<summary><b>Say it back</b><span>question</span></summary><div class="ans"><p>answer</p></div>`.
7. `<nav class="xlinks">` "Connections": 3 to 6 bullets. Each names a real section and what carries over, in a clause. Say which earlier objective this leans on.
8. `<p class="src"><b>Sources.</b> ...</p>`: guide section and objective, corpus sections, and any live document checked with its date.
9. `</div>` then `<aside class="remember">` with `h2` and `ol` of 3 to 6 rules that can be recalled in two minutes. Close `</div>`.

## Voice (hard rules; the lint checks most of them)

- A professor teaching a smart consultant. Concrete before abstract, why before how, numbers over adjectives, medium declarative sentences (about 15 to 20 words), direct address where natural.
- Define every term inline where it first appears, in the same sentence or the next. Also wrap the term once in `<dfn data-def="...">` for the glossary. No jargon before it is defined. Spell out abbreviations once.
- A plain checkable fact gets one flat sentence. No invented belief to knock down. No "not X but Y", no "it's not about X", no diagnose-negate-reveal. No announcing the point before making it. Say each idea once; do not restate it in a quotable closer.
- At most 2 em dashes per chapter (use none). At most one bold run per paragraph, and bold is rare. No exclamation marks, no emoji, no flattery.
- Banned vocabulary (the gate fails on it): actionable, additionally, furthermore, moreover, alignment, best practice(s), bolster, foster, underscore, comprehensive, cutting-edge, game-changing, revolutionary, transformative, delve, deep dive, ecosystem, elevate, embark, journey, roadmap, ensure, ensuring, essentially, fundamentally, ultimately, harness, holistic, multifaceted, nuanced, intricate, in conclusion, to summarize, ever-evolving, important to note, worth noting, landscape, realm, tapestry, leverage, meticulous, myriad, plethora, treasure trove, wealth of, navigate, robust, seamless, testament to, under the hood, unlock, costume, in disguise, dressed up as, backbone, bolted on, scaffold, plumbing, load-bearing, great question.
- No file names, paths or build talk in the body. Section tags like §3.9 are fine.
- British spelling, as in the exemplars. Straight quotes inside text.

## Claims and sources

- Decision rules come only from the corpus rows in the pack. Do not change a rule's meaning, direction or tag. Soften nothing the corpus states firmly, and do not harden anything it states softly.
- Anything beyond the corpus and the guide (a number, a product behaviour, an Anthropic doc claim) must be fetched from Anthropic's own documentation with WebFetch, cited in `p.src` with the date, and labelled. If you cannot verify it, leave it out. Never state a product fact from memory.
- Lesson text may inspire worked examples. Re-derive every number yourself and tag it: `<span class="num" data-calc="12000*4%" data-expect="480">480</span>`. The gate recomputes it.
- Cross-references: link to a page with `#/o3.6`. Link to a concept anchor (`#/o3.5/c3.10`) only if the pack lists that anchor as already written. Never invent an anchor.
- Do not claim what the real exam will ask beyond the guide. Label inference as inference.

## Figures

- At least one hand-drawn inline SVG per chapter, two to three for chapters with three or more sections. Each must teach something the paragraph cannot: a flow, a comparison, a timeline, a map. No decoration.
- Pattern: `<figure class="fig"><div class="scroll"><svg class="sv" viewBox="0 0 616 H" role="img" aria-labelledby="fXYa-t fXYa-d"><title id="fXYa-t">...</title><desc id="fXYa-d">...</desc>...</svg></div><figcaption>...</figcaption></figure>`. Ids are unique across the document: use the prefix in the pack.
- Classes only, no hard-coded colours. Boxes `bx` (plain), `bb` (blue, the right or key thing), `br` (red, the trap), `by` (yellow note), `fl` (muted); lines `ln`, `lb`, `lr`, `ls`, `dash`; text `h` (15 px bold), `b` (bold), `m` (12 px), `s` (12 px muted), `tc` centred, `te` right-aligned, `tr` red, `tb2` blue; fills `fi fb fr fy`; `pl` is a background plate. Arrow markers: `url(#ah)`, `url(#ah-b)`, `url(#ah-r)`, `url(#ah-g)`.
- Keep every label inside its box with at least 6 units spare. Measured widths: about 5.6 units per character at 12 px regular, about 6.3 bold, about 8.3 for a 15 px heading. Keep text off lines. Use a `pl` plate if a label must cross a line. Captions say what to look at in a plain sentence, not a slogan.
- Numbers in a figure must agree with the prose and pass `data-calc` where computed.

## Length

About 180 to 260 words of teaching prose per corpus section plus the rules rows; the whole chapter lands near 700 words of fixed apparatus (exam block, Remember, Say it back, Connections, opening) plus the sections. The two exemplars run 1,550 and 1,820 words. Do not pad and do not compress below the exemplars' care.

## Cost discipline

- Do not take screenshots or run browser checks. The orchestrator runs the browser sweep on every chapter.
- Run the private build at most four times: after the first full draft, after fixes, and once before you report.
- Do not re-read a file you just wrote. Write the first full draft in one Write call, then fix it with Edit.
- Keep reasoning short between tool calls.

## Report

When done, reply with: the file written, words, the gate result, the facts you verified live (URL and date), anything in the corpus that looked wrong or missing (do not fix it), and any judgement call a reviewer should check.
