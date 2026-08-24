// Anthropic Partner Academy — SCORM module extractor.
// Paste into mcp__claude-in-chrome__javascript_tool on a loaded module page.
// Full procedure, preconditions and dead ends: SOP_Academy-Course-Extraction_v1.md
//
// Before running:
//   1. Chrome site permission "Automatic downloads" = Allow for anthropic-partners.skilljar.com
//   2. navigate to the module slug, then wait ~6s for the nested iframe
//   3. set FN below

(() => {
  const FN = 'M1_Module-Name.md';   // <-- change per module
  const REVEAL_OPTIONS = false;     // true only if checkpoints are mostly single-select
  const SOURCE_LINE = 'Anthropic Partner Academy — <exam name> prep path.';
  const DATE = '<YYYY-MM-DD>';

  const INLINE = new Set(['SPAN','EM','STRONG','A','CODE','B','I','SUP','SUB','BR',
                          'SMALL','U','MARK','ABBR','TIME','KBD','VAR']);

  const f1 = document.getElementById('scorm_content_frame'); if (!f1) return 'no scorm frame';
  const f2 = f1.contentDocument.querySelector('iframe');     if (!f2) return 'no inner frame';
  const d  = f2.contentDocument;
  const main = d.getElementById('main');                     if (!main) return 'content not ready';
  const splash = (d.getElementById('splash') || {textContent:''}).textContent
                   .replace(/\s+/g, ' ').trim();

  // --- reveal checkpoint model answers --------------------------------------
  // Answers are not in the page source; they are injected on submit, and the
  // reveal button stays disabled until an attempt is entered.
  const before = main.textContent.length;
  [...main.children].forEach(s => {
    s.querySelectorAll('textarea, input[type=text]').forEach(ta => {
      ta.value = 'attempt';
      ta.dispatchEvent(new Event('input',  {bubbles: true}));
      ta.dispatchEvent(new Event('change', {bubbles: true}));
    });
    if (REVEAL_OPTIONS) {
      const seen = new Set();
      s.querySelectorAll('input[type=radio]').forEach(r => {
        if (seen.has(r.name)) return;
        seen.add(r.name);
        r.checked = true;
        r.dispatchEvent(new Event('change', {bubbles: true}));
        try { r.click(); } catch (e) {}
      });
    }
    s.querySelectorAll('button').forEach(b => {
      const re = REVEAL_OPTIONS ? /reveal|submit/i : /reveal/i;
      if (!re.test(b.textContent || '')) return;
      b.disabled = false;
      try { b.click(); } catch (e) {}
    });
  });
  const revealed = main.textContent.length - before;

  // --- DOM -> markdown -------------------------------------------------------
  const clean = t => (t || '').replace(/[ \t\u00a0]+/g, ' ').replace(/\s*\n\s*/g, ' ').trim();
  const allInline = el => el.children.length > 0 &&
                          [...el.children].every(c => INLINE.has(c.tagName));
  const md = [];
  const emit = l => md.push(l);

  const walk = node => {
    for (const el of node.children) {
      const tag = el.tagName;
      if (tag === 'SCRIPT' || tag === 'STYLE') continue;
      const raw = el.textContent || '';
      if (!raw.trim()) continue;

      if (el.classList.contains('codeblock') || tag === 'PRE') {
        emit(''); emit('```');
        emit(raw.replace(/\n{3,}/g, '\n\n').replace(/\s+$/, ''));
        emit('```'); emit('');
        continue;
      }
      if (/^H[1-6]$/.test(tag)) {
        emit(''); emit('#'.repeat(Math.min(6, +tag[1] + 1)) + ' ' + clean(raw)); emit('');
        continue;
      }
      if (tag === 'TABLE') {
        emit('');
        [...el.querySelectorAll('tr')].forEach((tr, ri) => {
          const c = [...tr.children].map(x => clean(x.textContent));
          emit('| ' + c.join(' | ') + ' |');
          if (ri === 0) emit('|' + c.map(() => '---').join('|') + '|');
        });
        emit('');
        continue;
      }
      if (tag === 'UL' || tag === 'OL') {
        emit('');
        [...el.children].forEach(li => { if (li.tagName === 'LI') emit('- ' + clean(li.textContent)); });
        emit('');
        continue;
      }
      if (tag === 'LI') { emit('- ' + clean(raw)); continue; }
      if (tag === 'P' || tag === 'BLOCKQUOTE' || allInline(el) || el.children.length === 0) {
        emit(clean(raw)); emit('');
        continue;
      }
      walk(el);
    }
  };

  emit('# ' + (d.title || 'Module'));
  emit('');
  emit('> **Source:** ' + SOURCE_LINE);
  emit('> Extracted ' + DATE + ' from the SCORM module, in full, screen by screen.');
  emit('> Free-text checkpoint model answers revealed. Select-two and drag-match checkpoints are left');
  emit('> as authored — their options are NOT marked.');
  emit('> Anthropic training content, held for personal exam preparation. Not for redistribution.');
  emit('');
  emit('**Module self-declares:** ' + splash.slice(-90));
  emit('');

  const screens = [...main.children];
  screens.forEach((s, i) => {
    emit(''); emit('---'); emit('');
    emit('## Screen ' + String(i + 1).padStart(2, '0') + (s.id ? ' · ' + s.id : ''));
    emit('');
    walk(s);
  });

  const text = md.join('\n').replace(/\n{4,}/g, '\n\n\n');

  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([text], {type: 'text/markdown'}));
  a.download = FN;
  document.body.appendChild(a);
  a.click();

  return {
    file: FN,
    screens: screens.length,        // compare against `declares` before filing
    chars: text.length,
    revealedChars: revealed,
    declares: splash.slice(-70)
  };
})()
