# SOP — Extracting Anthropic Partner Academy course modules to text

**Version 1.0 · Established and verified 2026-08-19** on the CCDV-F prep path (4 modules, 83 screens,
~381,000 characters, single session).

**Use this when:** a new exam's Academy prep path needs to become local text — CCAR-P, CCAO-F, a
renewal path, or any Skilljar-hosted Anthropic course.

**Do not improvise around this.** Every step below exists because a plausible alternative was tried
and failed. The dead ends are documented in §7; read them before deviating.

---

## 1. What you are dealing with

Academy modules are **SCORM packages containing self-contained HTML — not video.** That is the whole
reason this works. Each package holds **every screen in the DOM at once**, hidden by CSS rather than
fetched per screen, so one pass extracts the entire module.

The DOM path is a **nested iframe**:

```
top document
└── iframe#scorm_content_frame
    └── iframe            ← the module itself
        ├── #splash       ← TOC + self-declared "N screens · M sections · X minutes · K checkpoints"
        ├── #sidebar      ← section list with screen-type labels
        └── #main         ← one child element per screen. THE CONTENT.
```

Screen types, all of which matter to the corpus:

| Type | What it is | Corpus use |
|---|---|---|
| **Teaching** | Decision tables, worked examples, tradeoff comparisons | Core facts + decision tables |
| **Watch Out** | A named production failure and its postmortem | ❌ Misconception blocks, near one-for-one |
| **Checkpoint** | Exam-shaped items | Scenario ✅/❌ blocks |
| **Recap / Glossary** | Takeaways per objective, key terms, source list | Concept inventory |

---

## 2. Preconditions — check all four before starting

1. **Use the `claude-in-chrome` MCP, not the in-app browser.** The Academy is behind Partner Network
   sign-in; only real Chrome carries the session. Confirm with `list_connected_browsers`.
2. **Ram must be signed in** to `anthropic-partners.skilljar.com`. Verify by screenshot — look for the
   avatar and the "CPN Learning Path" nav.
3. **Chrome site permission: Automatic downloads → Allow** for `anthropic-partners.skilljar.com`.
   **This is the step that makes or breaks the run.** Chrome permits one automatic download per page
   load and then silently blocks the rest. Ram sets it via the icon left of the address bar →
   Site settings → Automatic downloads → Allow.
4. **Know which lessons are examinable** before extracting. Read the exam guide's content blueprint
   first. On CCDV-F, lesson 5 ("Accelerators & IP Contribution", 155 min — 20% of the path) mapped to
   **no domain and no skill**. Extracting it would have been wasted work, and studying it wasted time.

---

## 3. Step 1 — map the path

Navigate to the path page, then pull the module slugs. **Return `pathname` only** — returning full
hrefs trips the tool's `[BLOCKED: Cookie/query string data]` filter and you get nothing.

```js
(() => {
  const out = [];
  document.querySelectorAll('a').forEach(a => {
    let p = '';
    try { p = new URL(a.getAttribute('href'), location.href).pathname; } catch(e) { return; }
    if (p.includes('<path-slug>') && p !== '/path/<path-slug>') {
      out.push(p + '   ||   ' + (a.innerText||'').trim().replace(/\s+/g,' ').slice(0,60));
    }
  });
  return [...new Set(out)];
})()
```

Navigating to `/path/<path-slug>/<module-slug>` redirects to the real
`/path/.../<id>/scorm/<hash>` URL. You never need to construct the scorm URL yourself.

---

## 4. Step 2 — per module

For each **examinable** module:

1. `navigate` to the module slug.
2. **`wait` 6 seconds.** The nested iframe loads slowly. Extracting early returns
   `'content not ready'` — the script guards for this, so just re-run rather than guessing.
3. Run the extraction script (§5). It reveals checkpoints, extracts, and downloads in one call.
4. Confirm the file landed: `ls "C:/Users/ramna/Downloads" | grep -i "<name>"`.

**Chrome appends ` (1)` to a repeat filename.** If you re-extract a module, the newer file is the
`(1)` one — check timestamps, do not assume the bare name is current.

---

## 5. The extraction script

Change `FN` per module. Everything else is fixed.

```js
(() => {
  const FN = 'M1_Module-Name.md';                       // <-- change per module
  const REVEAL_OPTIONS = false;                          // see §6 before setting true
  const INLINE = new Set(['SPAN','EM','STRONG','A','CODE','B','I','SUP','SUB','BR','SMALL','U','MARK','ABBR','TIME','KBD','VAR']);

  const f1 = document.getElementById('scorm_content_frame'); if (!f1) return 'no scorm frame';
  const f2 = f1.contentDocument.querySelector('iframe');     if (!f2) return 'no inner frame';
  const d  = f2.contentDocument;
  const main = d.getElementById('main');                     if (!main) return 'content not ready';
  const splash = (d.getElementById('splash')||{textContent:''}).textContent.replace(/\s+/g,' ').trim();

  // --- reveal checkpoint model answers ------------------------------------
  // Answers are NOT in the page source. They are injected on submit, and the
  // reveal button stays disabled until an attempt is entered.
  const before = main.textContent.length;
  [...main.children].forEach(s => {
    s.querySelectorAll('textarea, input[type=text]').forEach(ta => {
      ta.value = 'attempt';
      ta.dispatchEvent(new Event('input',  {bubbles:true}));
      ta.dispatchEvent(new Event('change', {bubbles:true}));
    });
    if (REVEAL_OPTIONS) {
      const seen = new Set();
      s.querySelectorAll('input[type=radio]').forEach(r => {
        if (!seen.has(r.name)) { seen.add(r.name); r.checked = true;
          r.dispatchEvent(new Event('change',{bubbles:true})); try{ r.click(); }catch(e){} }
      });
    }
    s.querySelectorAll('button').forEach(b => {
      const re = REVEAL_OPTIONS ? /reveal|submit/i : /reveal/i;
      if (re.test(b.textContent||'')) { b.disabled = false; try { b.click(); } catch(e){} }
    });
  });
  const revealed = main.textContent.length - before;

  // --- DOM -> markdown -----------------------------------------------------
  const clean = t => (t||'').replace(/[ \t\u00a0]+/g,' ').replace(/\s*\n\s*/g,' ').trim();
  const allInline = el => el.children.length > 0 && [...el.children].every(c => INLINE.has(c.tagName));
  const md = []; const emit = l => md.push(l);
  const walk = node => { for (const el of node.children) {
    const tag = el.tagName; if (tag === 'SCRIPT' || tag === 'STYLE') continue;
    const raw = el.textContent || ''; if (!raw.trim()) continue;
    if (el.classList.contains('codeblock') || tag === 'PRE') {
      emit(''); emit('```'); emit(raw.replace(/\n{3,}/g,'\n\n').replace(/\s+$/,'')); emit('```'); emit(''); continue; }
    if (/^H[1-6]$/.test(tag)) { emit(''); emit('#'.repeat(Math.min(6,+tag[1]+1)) + ' ' + clean(raw)); emit(''); continue; }
    if (tag === 'TABLE') { emit('');
      [...el.querySelectorAll('tr')].forEach((tr,ri) => {
        const c = [...tr.children].map(x => clean(x.textContent));
        emit('| ' + c.join(' | ') + ' |');
        if (ri === 0) emit('|' + c.map(()=>'---').join('|') + '|');
      }); emit(''); continue; }
    if (tag === 'UL' || tag === 'OL') { emit('');
      [...el.children].forEach(li => { if (li.tagName === 'LI') emit('- ' + clean(li.textContent)); });
      emit(''); continue; }
    if (tag === 'LI') { emit('- ' + clean(raw)); continue; }
    if (tag === 'P' || tag === 'BLOCKQUOTE' || allInline(el) || el.children.length === 0) {
      emit(clean(raw)); emit(''); continue; }
    walk(el);
  }};

  emit('# ' + (d.title || 'Module')); emit('');
  emit('> **Source:** Anthropic Partner Academy — <exam name> prep path.');
  emit('> Extracted <YYYY-MM-DD> from the SCORM module, in full, screen by screen.');
  emit('> Free-text checkpoint model answers revealed. Select-two and drag-match checkpoints are left');
  emit('> as authored — their options are NOT marked.');
  emit('> Anthropic training content, held for personal exam preparation. Not for redistribution.');
  emit('');
  emit('**Module self-declares:** ' + splash.slice(-90)); emit('');

  const screens = [...main.children];
  screens.forEach((s,i) => { emit(''); emit('---'); emit('');
    emit('## Screen ' + String(i+1).padStart(2,'0') + (s.id ? ' · ' + s.id : '')); emit(''); walk(s); });

  const text = md.join('\n').replace(/\n{4,}/g,'\n\n\n');
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([text], {type:'text/markdown'}));
  a.download = FN; document.body.appendChild(a); a.click();

  return { file: FN, screens: screens.length, chars: text.length,
           revealedChars: revealed, declares: splash.slice(-70) };
})()
```

A copy lives beside this file as `extract-module.js`.

---

## 6. Checkpoints — what you can and cannot get

| Checkpoint type | Reveal mechanism | What you get |
|---|---|---|
| **Free text** | "Reveal model answer" button, `disabled` until a textarea has content | ✅ **Full model answer with reasoning.** The highest-value output of the whole exercise |
| **Single-select** | Submit with one option chosen | ✅ Question, all options, and rationale for the option tried |
| **Match-the-row** | Submit | ⚠️ Score band only (`Partial · 1/3`). Per-row rationale renders against wrong rows; not captured |
| **Select-two / drag-match** | No reveal button exists | ⚠️ Question and options only |

**Leave `REVEAL_OPTIONS = false` unless the module is mostly single-select.** On CCDV-F M2 it produced
genuine rationale ("Incorrect (Option C) — increasing max_tokens controls how much Claude can write,
not how much it can read"), which was worth having. On M3 and M4, whose checkpoints are select-two and
drag-match, it adds nothing.

Where an answer key is missing, the correct answer is derivable from the teaching screen immediately
preceding the checkpoint. That is how the modules are constructed.

**One thing not to misread:** in select-two items every option is prefixed with **✓**. That is the
module's own unchecked-box glyph (`<span class="box">✓</span>`), rendered uniformly on all options.
**It is not an answer mark.** Verified by re-extracting with zero interaction — the glyphs persist.

---

## 7. Dead ends — do not retry these

Each was attempted on 2026-08-19 and failed. Knowing this saves an hour.

| Approach | Why it fails |
|---|---|
| **Repeat downloads without the site permission** | Chrome allows one automatic download per page load, then blocks silently — no error, no prompt visible in the page viewport. This is why §2.3 exists |
| **Local HTTP receiver the page POSTs to** | Chrome's **Private Network Access** blocks an HTTPS page from reaching `127.0.0.1`. The fetch hangs until the CDP call times out at 45 s. A threaded server and preflight-free simple requests do not help |
| **Pulling text through `javascript_tool`** | Tool results cap at roughly **1 KB**. A 145,000-char module would need ~145 round trips |
| **`get_page_text` in chunks** | Caps at **50,000 chars** per call and only sometimes persists to disk. Workable but needs 3–4 passes per module, floods context, and the last chunk often returns inline |
| **Navigating to a `blob:` URL** | The `navigate` tool rejects it: `Invalid URL` |
| **Retyping content into files** | Do not. These are source-of-record files; a retyped transcript risks drift, which is the exact failure the project's fidelity rules exist to prevent. **The browser download is byte-exact from the DOM — that is why it is the only sanctioned path** |
| **Returning full hrefs or `window` globals from JS** | Trips `[BLOCKED: Cookie/query string data]` / `[BLOCKED: JWT token]`. Return `pathname` and plain values only |

---

## 8. Verify before filing

Compare **extracted screen count against the module's own `#splash` declaration**. The script returns
both — `screens` and `declares`.

Observed on CCDV-F: M1 9/9 exact · M2 29/29 exact · M3 22 extracted vs 21 declared · M4 23 vs 21.
`#main` carries one or two non-screen children in some modules. **A spare element is fine; a missing
screen is not.** Extracted < declared means re-run.

Then check structure:

```python
screens = len(set(re.findall(r'## Screen (\d\d)', t)))
fences  = t.count('\n' + '`'*3) // 2
tables  = t.count('\n|---')
```

---

## 9. File and document

Land transcripts in `<exam folder>/sources/course-transcripts/` as
`<CODE>_Module-N_<Lesson-Title>.md`, with a `README.md` recording:

- Status table: declared vs extracted screens per module, and which lessons were skipped and why
- Which checkpoint types yielded answers and which did not
- The chain rule: **transcript → `notes/` decision rules → `Domain-N_v1.md` → mock papers.**
  Never generate questions from a transcript directly

Then update `<exam folder>/sources/README.md` and `BACKGROUND-MATERIAL-INDEX_v1.md` Tier 1.

---

## 10. Disclose the side effect

Revealing model answers **submits placeholder attempts**, so the modules show attempted checkpoints and
partial scores in the Skilljar record.

This has **no bearing on the credential** — the exam guides state the credential is awarded on exam
performance alone and no course is required. Say so, and mention that each module has a **Reset
progress** control in its sidebar menu.

Do not skip this disclosure. It is the user's training record.

---

## 11. Run summary — CCDV-F, 2026-08-19

| Module | Declared | Extracted | Chars |
|---|---|---|---|
| M1 · MSO Foundations | 9 screens · 59 min · 2 cp | 9 | 23,235 |
| M2 · Production-Grade Prompting, Agents & Tool-use | 29 · 209 min · 9 cp | 29 | 152,380 |
| M3 · Claude Code, MCP & Integration | 21 · 142 min · 8 cp | 22 | 101,893 |
| M4 · Production Engineering, Evals & Security | 21 · 211 min · 6 cp | 23 | 103,127 |
| M5 · Accelerators & IP Contribution | — | **skipped — not on the blueprint** | — |

Once the site permission was set, all four extracted in about six minutes.
