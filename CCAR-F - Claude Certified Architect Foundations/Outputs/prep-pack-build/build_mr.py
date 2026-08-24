"""Build Test-MR.html - the multiple-response drill - from the workflow's verified items."""
import io, json, os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\Claude-Certified-Architect-Foundations_Exam-Prep_v1\Mock tests\Test-MR.html"

p = json.load(io.open(os.path.join(HERE, 'wf_payload.json'), encoding='utf-8'))
qs = p['questions']

DOM_NAMES = {
    "D1": "Agentic Architecture & Orchestration",
    "D2": "Tool Design & MCP Integration",
    "D3": "Claude Code Configuration & Workflows",
    "D4": "Prompt Engineering & Structured Output",
    "D5": "Context Management & Reliability",
}
ORDER = ["D1", "D2", "D3", "D4", "D5"]

# stable order: domain, then section number
def keyf(q):
    d = ORDER.index(q['domain'])
    sec = q.get('section', '0.0')
    a, _, b = sec.partition('.')
    return (d, int(a or 0), int(b or 0))

qs = sorted(qs, key=keyf)
for i, q in enumerate(qs):
    q['g'] = i + 1

quota = {d: sum(1 for q in qs if q['domain'] == d) for d in ORDER}
DATA = {
    "exam_n": 8,
    "format": "MULTI30",
    "quota": quota,
    "domainNames": DOM_NAMES,
    "questions": [
        {"g": q['g'], "domain": q['domain'], "section": q.get('section', ''),
         "stem": q['stem'], "options": q['options'], "correct": sorted(q['correct']),
         "whyRight": q['whyRight'], "whyWrong": q['whyWrong']}
        for q in qs
    ],
}

PACKBAR = ('<nav class="packbar" aria-label="CCA-F prep pack"><span class="pb-lab">CCA-F prep pack</span>'
           '<a href="../README.html">Start here</a>'
           '<a href="../Learning%20corpus/Exam-Day-Guide.html">Exam Day Guide</a>'
           '<a href="../Learning%20corpus/CCA-F_Concept-Atlas_v2.html">Concept Atlas</a>'
           '<a href="../Learning%20corpus/CCA-F_Trap-Sheet_v1.html">Trap Sheet</a>'
           '<a href="../Learning%20corpus/CCA-F_Corpus_v1.html">Corpus</a>'
           '<a href="Test-1.html" aria-current="page">Practice tests</a>'
           '<a href="Dashboard.html">Dashboard</a></nav>')

CSS = r"""
:root{
 --ink:#1a1814;--ink2:#3d3a34;--ink3:#7a7670;
 --cream:#faf7f2;--cream2:#f2ede4;--cream3:#e8e1d4;
 --amber:#c8832a;--amber-light:#f5e6cc;--amber-dark:#8a5a1a;
 --teal:#2a7a6e;--green:#3a7a4a;--green-light:#e2f0e6;
 --coral:#c85a3a;--coral-light:#fae8e2;
 --border:#ddd8ce;--shadow:0 2px 16px rgba(26,24,20,.08);
 --radius:12px;--radius-sm:8px;
 --serif:'DM Serif Display',Georgia,serif;--sans:'DM Sans',system-ui,sans-serif;
 --mono:'JetBrains Mono',ui-monospace,Consolas,monospace;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:88px}
body{font-family:var(--sans);background:var(--cream);color:var(--ink);font-size:16px;line-height:1.7}
.packbar{font:500 13px/1.4 var(--sans);background:#141821;color:#c9d1e0;padding:.5rem .9rem;
 display:flex;flex-wrap:wrap;align-items:center;gap:.35rem .5rem}
.packbar .pb-lab{color:#8d97ab;font-weight:600;letter-spacing:.02em;text-transform:uppercase;font-size:11px;margin-right:.3rem}
.packbar a{color:#c9d1e0;text-decoration:none;padding:.2rem .5rem;border-radius:999px;border:1px solid transparent;white-space:nowrap}
.packbar a:hover{background:#252c3a;color:#fff}
.packbar a[aria-current="page"]{background:#3b6ef5;color:#fff;border-color:#3b6ef5}
.hero{background:var(--cream2);border-bottom:1px solid var(--border);padding:20px 40px 18px;text-align:center}
.hero-eyebrow{font-family:var(--mono);font-size:11px;font-weight:500;letter-spacing:.18em;
 text-transform:uppercase;color:var(--amber-dark);margin-bottom:8px}
.hero h1{font-family:var(--serif);font-weight:400;font-size:clamp(24px,4vw,32px);line-height:1.15;color:var(--ink)}
.hero-sub{font-size:14px;color:var(--ink3);max-width:62ch;margin:9px auto 0}
.chrome{position:sticky;top:0;z-index:30;background:rgba(250,247,242,.97);backdrop-filter:blur(8px);
 border-bottom:1px solid var(--border)}
.chrome-in{max-width:860px;margin:0 auto;padding:9px 24px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.timer{font-family:var(--mono);font-size:15px;font-weight:500;color:var(--ink);letter-spacing:.02em}
.timer.low{color:var(--coral)}
.prog{flex:1;min-width:120px;height:5px;background:var(--cream3);border-radius:99px;overflow:hidden}
.prog i{display:block;height:100%;background:var(--amber);width:0;transition:width .25s}
.prog-txt{font-family:var(--mono);font-size:11.5px;color:var(--ink3);white-space:nowrap}
.hint-wrap{display:flex;align-items:center;gap:7px;font-size:12px;color:var(--ink3);white-space:nowrap}
.sw{width:38px;height:21px;border-radius:99px;background:var(--cream3);border:1px solid var(--border);
 position:relative;cursor:pointer;transition:background .18s;flex-shrink:0}
.sw::after{content:"";position:absolute;top:2px;left:2px;width:15px;height:15px;border-radius:50%;
 background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.2);transition:left .18s}
.sw.on{background:var(--amber)}.sw.on::after{left:19px}
main{max-width:860px;margin:0 auto;padding:26px 24px 90px}
.note{background:#fff;border:1px solid var(--border);border-left:3px solid var(--amber);
 border-radius:0 var(--radius-sm) var(--radius-sm) 0;padding:16px 20px;margin-bottom:24px;font-size:14.5px;line-height:1.65}
.note h2{font-family:var(--serif);font-weight:400;font-size:19px;margin-bottom:8px;color:var(--ink)}
.note p{margin-bottom:9px}.note p:last-child{margin-bottom:0}
.note b{color:var(--ink)}
.q-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);
 padding:26px 28px;margin-bottom:18px;box-shadow:var(--shadow)}
.q-top{display:flex;align-items:center;gap:9px;flex-wrap:wrap;margin-bottom:12px}
.q-n{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3)}
.q-dom{font-family:var(--mono);font-size:10px;letter-spacing:.06em;padding:2px 8px;border-radius:99px;
 background:var(--cream2);border:1px solid var(--border);color:var(--amber-dark)}
.q-sel{font-family:var(--mono);font-size:10px;letter-spacing:.06em;padding:2px 8px;border-radius:99px;
 background:var(--amber-light);border:1px solid #e8cd9c;color:var(--amber-dark);font-weight:600}
.stem{font-size:15.5px;line-height:1.68;color:var(--ink2);margin-bottom:16px}
.opts{display:flex;flex-direction:column;gap:9px}
.opt{display:flex;align-items:flex-start;gap:12px;padding:13px 16px;border:1.5px solid var(--border);
 border-radius:var(--radius-sm);background:var(--cream2);cursor:pointer;transition:all .15s;
 font-size:14px;line-height:1.5;color:var(--ink2)}
.opt:hover:not(.locked){border-color:var(--amber);background:var(--cream)}
.opt .box{width:19px;height:19px;border:1.5px solid var(--ink3);border-radius:5px;flex-shrink:0;
 margin-top:1px;display:flex;align-items:center;justify-content:center;font-size:12px;color:#fff;background:#fff}
.opt.sel{border-color:var(--amber);background:var(--amber-light)}
.opt.sel .box{background:var(--amber);border-color:var(--amber)}
.opt.sel .box::after{content:"\2713"}
.opt .ltr{font-family:var(--mono);font-size:12px;font-weight:600;color:var(--ink3);flex-shrink:0;margin-top:1px}
.opt.locked{cursor:default}
.opt.key{border-color:var(--green);background:var(--green-light)}
.opt.miss{border-color:var(--coral);background:var(--coral-light)}
.q-act{display:flex;align-items:center;gap:12px;margin-top:15px;flex-wrap:wrap}
.btn{font-family:var(--sans);font-size:13px;font-weight:600;padding:9px 22px;border-radius:99px;
 border:1.5px solid var(--amber);background:var(--amber);color:#fff;cursor:pointer;transition:all .15s}
.btn:hover:not(:disabled){background:var(--amber-dark);border-color:var(--amber-dark)}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn.ghost{background:transparent;color:var(--amber-dark)}
.btn.ghost:hover:not(:disabled){background:var(--amber-light)}
.pick-hint{font-size:12px;color:var(--ink3)}
.fb{display:none;margin-top:15px;padding-top:15px;border-top:1px solid var(--cream3)}
.fb.shown{display:block}
.verdict{font-family:var(--mono);font-size:11px;letter-spacing:.09em;text-transform:uppercase;
 font-weight:600;margin-bottom:11px}
.verdict.ok{color:var(--green)}.verdict.no{color:var(--coral)}
.fb-sub{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;
 color:var(--ink3);margin:13px 0 7px}
.fb-row{padding:11px 14px;border-radius:var(--radius-sm);background:var(--cream2);margin-bottom:8px;
 border-left:3px solid var(--border)}
.fb-row.right{border-left-color:var(--green)}
.fb-row.wrong{border-left-color:var(--coral)}
.fb-row .lbl{font-family:var(--mono);font-size:10.5px;letter-spacing:.05em;color:var(--ink3);
 margin-bottom:5px;font-weight:500}
.fb-row .txt{font-size:13.5px;color:var(--ink2);line-height:1.6}
.fb-row .cite{font-family:var(--mono);font-size:10.5px;color:var(--amber-dark);margin-top:6px;letter-spacing:.03em}
.fb-row .cite a{color:var(--amber-dark);text-decoration:none;border-bottom:1px dotted currentColor}
.fb-row .cite a:hover{color:var(--amber);border-bottom-style:solid}
code{font-family:var(--mono);font-size:.87em;background:var(--cream3);padding:1px 5px;border-radius:4px;color:var(--ink)}
.results{display:none;background:#1f1c17;color:var(--cream);border-radius:var(--radius);
 padding:34px 32px;margin-bottom:22px;text-align:center}
.results.shown{display:block}
.results h2{font-family:var(--serif);font-weight:400;font-size:24px;margin-bottom:16px}
.score-big{font-family:var(--serif);font-size:52px;line-height:1;margin-bottom:6px}
.scaled{font-size:13.5px;color:rgba(250,247,242,.72)}
.passline{display:inline-block;margin-top:12px;font-family:var(--mono);font-size:11px;letter-spacing:.08em;
 text-transform:uppercase;padding:5px 14px;border-radius:99px}
.passline.pass{background:rgba(58,122,74,.28);color:#a8dfb6}
.passline.fail{background:rgba(200,90,58,.28);color:#f0b6a2}
.res-label{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;
 color:rgba(250,247,242,.5);margin:28px 0 12px;text-align:left}
.res-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px;text-align:left}
.res-card{background:rgba(250,247,242,.06);border:1px solid rgba(250,247,242,.14);
 border-radius:var(--radius-sm);padding:13px 15px}
.res-card.weak{border-color:rgba(232,120,90,.55);background:rgba(232,120,90,.09)}
.rc-name{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;
 color:var(--amber-light);margin-bottom:6px;line-height:1.3}
.rc-score{font-family:var(--serif);font-size:23px;line-height:1}
.rc-pct{font-size:12px;color:rgba(250,247,242,.6)}
.rc-study{margin-top:9px;padding-top:8px;border-top:1px solid rgba(250,247,242,.13);
 font-family:var(--mono);font-size:9.5px;letter-spacing:.04em;color:rgba(250,247,242,.45);line-height:1.9}
.rc-study a{color:rgba(250,247,242,.78);text-decoration:none;border-bottom:1px solid rgba(250,247,242,.25)}
.rc-study a:hover{color:#fff;border-bottom-color:#fff}
.caveat{font-size:12.5px;color:rgba(250,247,242,.55);margin-top:22px;text-align:left;line-height:1.65}
.caveat b{color:rgba(250,247,242,.85)}
.export{display:none;background:#fff;border:1px solid var(--border);border-radius:var(--radius);
 padding:20px 24px;margin-bottom:22px}
.export.shown{display:block}
.export h3{font-family:var(--serif);font-weight:400;font-size:18px;margin-bottom:5px}
.export p{font-size:13px;color:var(--ink3);margin-bottom:12px}
.export pre{background:var(--cream2);border:1px solid var(--border);border-radius:var(--radius-sm);
 padding:12px 14px;font-family:var(--mono);font-size:11px;max-height:150px;overflow:auto;
 color:var(--ink2);margin-bottom:12px;white-space:pre-wrap;word-break:break-all}
.foot{text-align:center;margin-top:30px}
.tally{font-family:var(--mono);font-size:12px;color:var(--ink3)}
.tally b{color:var(--green)}.tally i{color:var(--coral);font-style:normal}
@media (max-width:640px){.hero{padding:16px 18px 14px}main{padding:20px 16px 60px}
 .q-card{padding:20px 18px}.chrome-in{padding:8px 16px;gap:9px}}
@media print{.packbar,.chrome,.q-act,.export{display:none}}
"""

JS = r"""
const DATA = __DATA__;
const ORDER = ["D1","D2","D3","D4","D5"];
const KEY = "ccaf-mr-v1";
let state = load();
function load(){
  try{const s=JSON.parse(localStorage.getItem(KEY)||"{}");
    return {answers:s.answers||{},locked:s.locked||{},times:s.times||{},started:s.started||null,
            finished:!!s.finished,hint:!!s.hint};}
  catch(e){return {answers:{},locked:{},times:{},started:null,finished:false,hint:false};}
}
function save(){localStorage.setItem(KEY,JSON.stringify(state));}
const esc=s=>String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const letter=i=>"ABCDEF"[i];
function code(t){return esc(t).replace(/`([^`]+)`/g,'<code>$1</code>');}
function citeHref(cite){const m=/\u00a7\s*(\d+)\.(\d+)/.exec(cite||"");
  return m?`../Learning%20corpus/CCA-F_Corpus_v1.html#s-${m[1]}-${m[2]}`:"";}
function fmt(s){s=Math.max(0,Math.round(s));const m=Math.floor(s/60);
  return `${String(m).padStart(2,"0")}:${String(s%60).padStart(2,"0")}`;}
function studyLinks(d){const k=d.toLowerCase();
  return `<a href="../Learning%20corpus/Exam-Day-Guide.html#${k}">Guide</a> &middot; <a href="../Learning%20corpus/CCA-F_Concept-Atlas_v2.html#${k}">Atlas</a>`
       + ` &middot; <a href="../Learning%20corpus/CCA-F_Trap-Sheet_v1.html#p-${k}">Traps</a> &middot; <a href="../Learning%20corpus/CCA-F_Corpus_v1.html#p-${k}">Corpus</a>`;}
const sameSet=(a,b)=>a.length===b.length&&a.every(x=>b.includes(x));
function isRight(q){const a=state.answers[q.g]||[];return sameSet(a,q.correct);}

function render(){
  const host=document.getElementById("qs");
  host.innerHTML=DATA.questions.map(q=>{
    const sel=state.answers[q.g]||[];
    const lk=!!state.locked[q.g];
    const opts=q.options.map((o,i)=>{
      let cls="opt"+(sel.includes(i)?" sel":"")+(lk?" locked":"");
      if(lk&&state.hint){ if(q.correct.includes(i))cls+=" key"; else if(sel.includes(i))cls+=" miss"; }
      return `<div class="${cls}" data-q="${q.g}" data-i="${i}"><span class="box"></span>`
           + `<span class="ltr">${letter(i)}</span><span>${code(o)}</span></div>`;
    }).join("");
    return `<article class="q-card" id="q-${q.g}">
      <div class="q-top"><span class="q-n">Question ${q.g} of ${DATA.questions.length}</span>
      <span class="q-dom">${q.domain} &middot; ${esc(DATA.domainNames[q.domain])}</span>
      <span class="q-sel">Select ${q.correct.length}</span></div>
      <div class="stem">${code(q.stem)}</div>
      <div class="opts">${opts}</div>
      <div class="q-act">
        <button class="btn" id="lock-${q.g}" ${lk?"disabled":""}>Lock answer</button>
        <span class="pick-hint" id="ph-${q.g}"></span>
      </div>
      <div class="fb" id="fb-${q.g}"></div>
    </article>`;
  }).join("");
  DATA.questions.forEach(q=>{
    document.getElementById(`lock-${q.g}`).onclick=()=>lock(q.g);
    paintHint(q);
    if(state.locked[q.g]&&state.hint) feedback(q);
  });
  host.querySelectorAll(".opt").forEach(el=>{
    el.onclick=()=>{
      const g=+el.dataset.q, i=+el.dataset.i;
      if(state.locked[g]) return;
      const q=DATA.questions.find(x=>x.g===g);
      const cur=state.answers[g]||[];
      const at=cur.indexOf(i);
      if(at>=0) cur.splice(at,1);
      else{ if(cur.length>=q.correct.length) return; cur.push(i); }
      state.answers[g]=cur.sort((a,b)=>a-b);
      if(!state.started){state.started=Date.now();tick();}
      save(); render(); document.getElementById(`q-${g}`).scrollIntoView({block:"nearest"});
    };
  });
  updateChrome();
}
function paintHint(q){
  const el=document.getElementById(`ph-${q.g}`); if(!el) return;
  if(state.locked[q.g]){el.textContent=state.hint?(isRight(q)?"Correct":"Not quite"):"Locked";return;}
  const n=(state.answers[q.g]||[]).length;
  el.textContent = n===q.correct.length
    ? "Ready to lock."
    : `Select ${q.correct.length-n} more. Partly-right answers score nothing.`;
}
function lock(g){
  const q=DATA.questions.find(x=>x.g===g);
  const sel=state.answers[g]||[];
  if(sel.length!==q.correct.length) return;
  state.locked[g]=true;
  state.times[g]=state.started?Math.round((Date.now()-state.started)/1000):null;
  save(); render();
  if(state.hint) feedback(q);
  if(Object.keys(state.locked).length===DATA.questions.length) submit();
}
function feedback(q){
  const fb=document.getElementById(`fb-${q.g}`); if(!fb) return;
  const sel=state.answers[q.g]||[], ok=isRight(q);
  const wrongBy={}; q.whyWrong.forEach(w=>wrongBy[w.option]=w);
  const row=(cls,lbl,txt,cite)=>{
    const h=citeHref(cite);
    const c=cite?`<div class="cite">Source: ${h?`<a href="${h}" target="_blank" rel="noopener">${esc(cite)}</a>`:esc(cite)}</div>`:"";
    return `<div class="fb-row ${cls}"><div class="lbl">${lbl}</div><div class="txt">${code(txt)}</div>${c}</div>`;
  };
  let h=`<div class="verdict ${ok?"ok":"no"}">${ok?"Correct \u2014 full credit":"Not quite \u2014 this item scores zero"}</div>`;
  if(!ok){
    const missed=q.correct.filter(i=>!sel.includes(i));
    const extra=sel.filter(i=>!q.correct.includes(i));
    let d=[];
    if(missed.length) d.push(`you missed ${missed.map(letter).join(", ")}`);
    if(extra.length) d.push(`you ticked ${extra.map(letter).join(", ")} which is not in the key`);
    h+=`<div class="fb-sub">Why it scored zero</div>`
     + `<div class="fb-row wrong"><div class="txt">Multiple-response items are all-or-nothing \u2014 ${d.join("; ")}.</div></div>`;
  }
  h+=`<div class="fb-sub">Why the keyed set is right (${q.correct.map(letter).join(", ")})</div>`
   + row("right","The keyed set",q.whyRight.text,q.whyRight.cite);
  h+=`<div class="fb-sub">Why each remaining option is wrong</div>`;
  q.options.forEach((_,i)=>{ if(q.correct.includes(i))return;
    const w=wrongBy[i]; if(w) h+=row("wrong",`Option ${letter(i)}${sel.includes(i)?" \u2014 you ticked this":""}`,w.text,w.cite); });
  fb.innerHTML=h; fb.classList.add("shown");
}
function setHint(on){
  state.hint=on; save();
  document.getElementById("sw").classList.toggle("on",on);
  render();
  if(!on) document.querySelectorAll(".fb").forEach(f=>{f.classList.remove("shown");f.innerHTML="";});
}
function updateChrome(){
  const done=Object.keys(state.locked).length, n=DATA.questions.length;
  document.getElementById("bar").style.width=(done/n*100)+"%";
  document.getElementById("ptxt").textContent=`${done} / ${n} locked`;
  const t=document.getElementById("timer");
  if(state.hint){
    let r=0,w=0;
    DATA.questions.forEach(q=>{if(state.locked[q.g]){isRight(q)?r++:w++;}});
    t.innerHTML=`<span class="tally"><b>${r} right</b> &middot; <i>${w} wrong</i></span>`;
    t.classList.remove("low");
  }else{
    const el=state.started?Math.round((Date.now()-state.started)/1000):0;
    const left=60*60-el;
    t.textContent=fmt(Math.abs(left))+(left<0?" over":"");
    t.classList.toggle("low",left<300);
  }
  document.getElementById("submit").disabled = done===0;
}
function tick(){ setInterval(()=>{ if(!state.finished) updateChrome(); },1000); }
function submit(){
  state.finished=true; save();
  const perDom={}; ORDER.forEach(d=>perDom[d]={correct:0,of:DATA.quota[d]});
  let tot=0; const qlist=[];
  DATA.questions.forEach(q=>{
    const ok=state.locked[q.g]&&isRight(q);
    if(ok){tot++;perDom[q.domain].correct++;}
    qlist.push({q:q.g,domain:q.domain,block:1,type:"multi",
      selected:(state.answers[q.g]||[]).map(letter).join(""),correct:!!ok,seconds:state.times[q.g]||null});
  });
  const n=DATA.questions.length;
  const scaled=Math.round(tot/n*900+100), pass=scaled>=720;
  const grid=ORDER.map(d=>{
    const c=perDom[d], pct=c.of?Math.round(c.correct/c.of*100):0;
    return `<div class="res-card${pct<70?" weak":""}"><div class="rc-name">${d} &middot; ${esc(DATA.domainNames[d])}</div>`
         + `<div class="rc-score">${c.correct}/${c.of}</div><div class="rc-pct">${pct}%</div>`
         + `<div class="rc-study">Study this: ${studyLinks(d)}</div></div>`;
  }).join("");
  const el=state.started?Math.round((Date.now()-state.started)/1000):0;
  document.getElementById("results").innerHTML=`<h2>Multiple-Response Drill \u2014 Results</h2>
    <div class="score-big">${tot} / ${n}</div>
    <div class="scaled">Estimated scaled score: ${scaled} / 1000</div>
    <div class="passline ${pass?"pass":"fail"}">${pass?"Above":"Below"} pass line (720)</div>
    <div class="scaled" style="margin-top:10px">Total time: ${fmt(el)}</div>
    <div class="res-label">By domain</div><div class="res-grid">${grid}</div>
    <p class="caveat"><b>Read this before you compare it to a Test 1\u20137 score.</b> Every item here is all-or-nothing:
    a three-of-six item with two right ticks scores exactly the same as one with none. That makes this drill score
    harder than a single-choice test on identical knowledge, and it is meant to. A low number here with good
    Test 1\u20137 scores means your knowledge is sound but not yet precise enough to defend each tick separately.</p>
    <p class="caveat">Any domain below 70% is marked. The <b>Study this</b> links open that domain in the Guide, the
    Atlas, the Trap Sheet and the Corpus. Every <b>Source</b> line in the feedback above links to the corpus section it cites.</p>`;
  document.getElementById("results").classList.add("shown");
  const payload={test_n:8,format:"MULTI30",attempted_date:new Date().toISOString().slice(0,10),
    total_correct:tot,total_questions:n,total_seconds:el,estimated_scaled:scaled,
    domains:Object.fromEntries(ORDER.map(d=>[d,{correct:perDom[d].correct,of:perDom[d].of,name:DATA.domainNames[d]}])),
    blocks:[{scenario:"Multiple-response drill",correct:tot,of:n}],questions:qlist};
  document.getElementById("json").textContent=JSON.stringify(payload,null,2);
  document.getElementById("export").classList.add("shown");
  document.getElementById("results").scrollIntoView({behavior:"smooth"});
}
function copyJson(){
  const t=document.getElementById("json").textContent;
  navigator.clipboard.writeText(t).then(()=>{
    const b=document.getElementById("copyBtn"),o=b.textContent;
    b.textContent="Copied \u2713";setTimeout(()=>b.textContent=o,1600);});
}
function resetAll(){
  if(!confirm("Clear every answer on this drill and start over?"))return;
  localStorage.removeItem(KEY);
  state={answers:{},locked:{},times:{},started:null,finished:false,hint:false};
  document.getElementById("results").classList.remove("shown");
  document.getElementById("export").classList.remove("shown");
  document.getElementById("sw").classList.remove("on");
  render(); window.scrollTo(0,0);
}
document.getElementById("sw").onclick=()=>setHint(!state.hint);
document.getElementById("submit").onclick=submit;
document.getElementById("reset").onclick=resetAll;
document.getElementById("copyBtn").onclick=copyJson;
if(state.hint) document.getElementById("sw").classList.add("on");
render();
if(state.started) tick();
if(state.finished) submit();
"""

body = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Multiple-Response Drill &middot; CCA-F Practice</title>
<meta name="description" content="Thirty multiple-response CCA-F items, scored all-or-nothing, weighted to the official domain split."/>
<link rel="icon" href="data:,"/>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>%s</style>
</head>
<body>
%s
<div class="hero">
  <div class="hero-eyebrow">Claude Certified Architect &mdash; Foundations</div>
  <h1>Multiple-Response Drill</h1>
  <p class="hero-sub">The item type Tests 1&ndash;7 do not cover. %d questions, each naming how many options to select, each scored all-or-nothing.</p>
</div>
<div class="chrome"><div class="chrome-in">
  <span class="timer" id="timer">60:00</span>
  <span class="prog"><i id="bar"></i></span>
  <span class="prog-txt" id="ptxt">0 / %d locked</span>
  <span class="hint-wrap"><span class="sw" id="sw" role="switch" aria-label="Hint mode"></span>Hint</span>
  <button class="btn ghost" id="submit" disabled>Show results</button>
  <button class="btn ghost" id="reset">Reset</button>
</div></div>
<main>
  <div class="note">
    <h2>How this drill differs from Tests 1&ndash;7</h2>
    <p>The real exam contains items that ask for more than one answer and state how many. Those items are scored
    <b>all-or-nothing</b>: the full set is right or the item scores nothing. Partial credit does not exist.</p>
    <p>That changes how you answer. On a single-choice item you can pick the best of four. Here <b>every tick has to be
    defensible on its own</b> &mdash; a tick you added because it "feels related" costs you the whole item, including the
    answers you got right.</p>
    <p>Each question below shows a <b>Select N</b> badge and will not let you tick more than N. Choose exactly N, then
    <b>Lock answer</b>. With <b>Hint</b> on you see the full reasoning as soon as you lock; with it off you see nothing
    until you finish. Progress saves in this browser.</p>
    <p>Suggested pace: 60 minutes for %d items. Multi-select items take longer than single-choice ones, which is part of
    what makes them expensive on the real paper.</p>
  </div>
  <div class="results" id="results"></div>
  <div class="export" id="export">
    <h3>Copy results JSON</h3>
    <p>Paste this into <a href="Dashboard.html">Dashboard.html</a> to track this drill alongside your Test 1&ndash;7 attempts.</p>
    <pre id="json"></pre>
    <button class="btn" id="copyBtn">Copy results JSON</button>
  </div>
  <div id="qs"></div>
  <div class="foot"><button class="btn" onclick="submit()">Show results</button></div>
</main>
<script>%s</script>
</body>
</html>
""" % (CSS, PACKBAR, len(DATA['questions']), len(DATA['questions']), len(DATA['questions']),
       JS.replace('__DATA__', json.dumps(DATA, ensure_ascii=False)))

io.open(OUT, 'w', encoding='utf-8').write(body)
print('wrote', OUT, len(body), 'bytes,', len(DATA['questions']), 'questions')
print('quota', quota)
