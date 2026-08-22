# course-transcripts/

Full text of the Anthropic Partner Academy prep-path modules, extracted 2026-08-19 so the corpus can be
built and audited against a fixed local source instead of re-scraping.

**Anthropic training content, held for personal exam preparation. Not for redistribution.**

---

## Status — all four examinable modules captured ✅

| Module | Min | Module self-declares | Extracted | Content |
|---|---|---|---|---|
| M1 · MSO Foundations | 57 | 9 screens · 6 sections · 2 checkpoints | **9 screens** ✅ | 23,235 chars |
| M2 · Production-Grade Prompting, Agents & Tool-use | 209 | 29 screens · 10 sections · 9 checkpoints | **29 screens** ✅ | 152,380 chars · 21 code blocks · 19 tables |
| M3 · Claude Code, MCP & Integration | 142 | 21 screens · 8 sections · 8 checkpoints | **22 elements** ✅ | 101,893 chars · 15 code blocks |
| M4 · Production Engineering, Evals & Security | 211 | 21 screens · 5 topic groups · 6 checkpoints | **23 elements** ✅ | 103,127 chars · 29 code blocks |
| M5 · Accelerators & IP Contribution | 155 | — | **not captured, deliberately** | ❌ not on the blueprint |

Total captured: **~381,000 characters** across 83 screens.

M3 and M4 yield one or two more elements than their declared screen count — `#main` carries a couple
of non-screen children. Nothing is missing; a spare element is captured rather than a screen lost.

**M5 is skipped on purpose.** It maps to no domain and no skill in the official exam guide — 155
minutes of partner enablement, not exam preparation. See `../../EXAM-FACTS_v1.md` §3.

---

## What is in a module transcript

The modules are self-contained HTML, not video, so these are the real teaching text rather than a
speech-to-text approximation. Each carries screen types that map directly onto the corpus template:

- **Teaching** — the substance. Decision tables, worked examples, tradeoff comparisons.
- **Watch Out** — a named production failure and its postmortem. *"The description that sent Claude to
  the wrong tool"*, *"The agent that filled the window on session four"*, *"The batch job that was not
  actually a batch"*. These convert almost one-for-one into ❌ Misconception blocks.
- **Checkpoint** — exam-shaped items from the authoritative source.
- **Recap / Glossary** — M2 closes with "Eight takeaways, one per enabling objective", a key-terms
  glossary, and a Sources list naming which Academy courses and docs each section drew on.

---

## Checkpoint answers — what was and was not captured

Model answers are **not** in the page source; they are injected only after a checkpoint is submitted,
and the reveal button stays `disabled` until an attempt is entered. Capturing them meant filling each
input, enabling the button and clicking it.

| Checkpoint type | Captured |
|---|---|
| **Free text** ("Reveal model answer") | ✅ **Full model answer with reasoning.** M2 has five: the broken-prompt fix, the stream-handler repair, the agent-wiring gaps, and both stages of the cumulative debug task |
| **Single-select** | ✅ Question, all options, and the rationale for the option that was tried (e.g. *"Increasing max_tokens controls how much Claude can write, not how much it can read"*) |
| **Match-the-row** | ⚠️ Question and full option sets only. Submitting returns a score band (`Partial · 1/3`); per-row rationale renders against wrong rows and was not captured |
| **Select-two / drag-match** (M3, M4) | ⚠️ Question and full option sets only. These have no reveal button, so no answer key was captured |

Where an answer key is missing, the correct answer is derivable from the teaching screen immediately
preceding the checkpoint — that is how the modules are built.

### One thing not to misread

In M3, every option in a select-two item is prefixed with **✓**. That is the module's own
unchecked-checkbox glyph (`<span class="box">✓</span>`), rendered uniformly on all options. **It is not
an answer mark.** Verified by re-extracting with no interaction at all — the glyphs are still there.

---

## How these were extracted

The modules are SCORM packages: one self-contained HTML file per module, loaded in a nested iframe,
with every screen present in the DOM at once rather than fetched per screen. Extraction walks
`#main > *` (one element per screen), converts to markdown, and preserves `div.codeblock` as fenced
code. The result is downloaded straight from the page, so the file is byte-exact from the DOM rather
than retyped.

M3 was re-extracted with **no option-clicking at all**, to be certain nothing in its answer sets was
altered by the capture.

---

## ⚠️ This wrote placeholder attempts into the Academy record

Revealing the model answers required submitting checkpoints. M1–M4 now show placeholder attempts and
partial scores in the Skilljar record.

**This has no bearing on the credential.** The official exam guide is explicit: *"There are no
mandatory prerequisites or courses required to sit this exam... The credential is awarded based on exam
performance alone."* Course progress is not a gate.

If you want the record clean, each module has a **Reset progress** control in its sidebar menu.

---

## Rules for using these files

**Do not edit them.** They are the source of record.

Derived decision rules go in `../../notes/` with a pointer back to the screen they came from. The
corpus is generated from `../../prep with quiz/CCDV-F_Domain-N_v1.md` — **never from a transcript
directly**, and never from a transcript quoted into a prompt. The chain is:

```
transcript  →  notes/ (decision rules, with provenance)  →  CCDV-F_Domain-N_v1.md  →  mock papers
```

## Naming

`CCDV-F_Module-N_<Lesson-Title>.md`. Re-extraction overwrites in place; if a module is re-captured
after Anthropic updates it, keep both and diff them, the way the exam-guide versions are handled.
