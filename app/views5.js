/* Views part 5: Econ Lab. The regional FTDM roleplay focuses on Economics, so this section teaches every
   Economics PI and keeps its lessons, flashcards, talking points, roleplays, judge questions and quizzes together. */
'use strict';
Object.assign(NAV_OF,{econ:'econ'});
const ECON = D.econ || {units:[],pis:[]};
const ECONPI = Object.fromEntries(ECON.pis.map(x=>[x.code,x]));
const ECONU = Object.fromEntries(ECON.units.map(u=>[u.id,u]));
const ECON_ORDER = ECON.units.flatMap(u=>u.pis);
// Flashcards: three per PI ("econ" deck, or "econ:<unit>"), plus every PI's judge questions ("econjq" deck).
const ECONCARDS=[]; const ECONJQ=[];
ECON.pis.forEach(x=>{ x.cards.forEach(([t,d,tip],i)=>ECONCARDS.push({id:`e-${x.code}-${i}`,lesson:'econ',t,d,x:tip,src:'',pi:x.code,unit:x.unit}));
  x.qs.forEach((q,i)=>ECONJQ.push({id:`ej-${x.code}-${i}`,lesson:'econjq',t:q.q,d:q.a,x:'',src:x.title,pi:x.code,unit:x.unit})); });
[...ECONCARDS,...ECONJQ].forEach(c=>CARD[c.id]=c);
function econDeck(deck){ if(deck==='econjq') return ECONJQ; if(deck.startsWith('econ:')){ const u=deck.slice(5); return ECONCARDS.filter(c=>c.unit===u); } return ECONCARDS; }
const isEcon=c=>c.pis.filter(p=>p.startsWith('EC:')).length>=2;
function econCases(){ return D.cases.cases.filter(c=>c.econ).concat(D.cases.cases.filter(c=>!c.econ&&isEcon(c))); }
function econDrills(){ return D.cases.drills.filter(d=>d.econ||isEcon(d)); }
function econTalk(){ return D.talk.filter(t=>t.pis.some(p=>p.startsWith('EC:'))); }
function econRead(code){ return !!(S.econRead||{})[code]; }
function econReadCount(list=ECON_ORDER){ return list.filter(econRead).length; }
function nextEconPI(){ const t=today(); if(t.econPI&&ECONPI[t.econPI]&&(!econRead(t.econPI)||t.econ)) return ECONPI[t.econPI];
  const c=ECON_ORDER.find(x=>!econRead(x)); if(!c) return null; t.econPI=c; return ECONPI[c]; }
function econAcc(list){ let n=0,c=0; list.forEach(p=>{ const st=piStats(p); n+=st.n; c+=st.c; }); return {n,c}; }

const ECON_TABS=[['learn','Learn'],['cards','Flashcards'],['talk','Talking points'],['cases','Roleplays'],['judge','Judge questions'],['quiz','Quiz']];
function econHead(tab){
  const r=econReadCount();
  return `${head('Econ Lab',`The regional FTDM roleplay focuses on Economics. All ${ECON_ORDER.length} Economics performance indicators, taught in plain language and tied to financial services, with real-world talking points, flashcards, practice roleplays and the judge questions each PI prepares you for.`)}
  <div class="card stack-s"><div class="row between"><span class="label">Your progress</span><span class="mono small">${r}/${ECON_ORDER.length} PIs read</span></div>${bar(pct(r,ECON_ORDER.length),'good')}</div>
  <div class="chips scrollx" role="tablist">${ECON_TABS.map(([k,l])=>`<a class="chip ${tab===k?'on':''}" role="tab" aria-selected="${tab===k}" href="#econ${k==='learn'?'':'-'+k}">${l}</a>`).join('')}</div>`;
}

V.econ=(arg)=>{
  if(arg && ECONPI[arg]) return econPIView(ECONPI[arg]);
  const tab=ECON_TABS.some(([k])=>k===arg)?arg:'learn';
  const body={learn:econLearn,cards:econCardsTab,talk:econTalkTab,cases:econCasesTab,judge:econJudgeTab,quiz:econQuizTab}[tab]();
  return `<div class="wrap">${econHead(tab)}${body}</div>`;
};

function econLearn(){
  const nx=ECONPI[ECON_ORDER.find(c=>!econRead(c))];
  return `<div class="row">${nx?`<a class="btn primary" href="#econ-${nx.code}">Next up: ${esc(nx.code)} ${esc(nx.title)}</a>`:'<span class="chip good">All PIs read. Keep reviewing with flashcards and judge questions.</span>'}<button class="btn" data-a="econJq" data-pool="econ">${icon('mic')}Practice judge questions</button></div>
  <p class="tiny faint">Each PI page has: the idea in plain English, key points, how it shows up in financial services, real examples with sources, a trap to avoid, a line to say to the judge, and two judge questions with strong answers.</p>
  <div class="grid2">${ECON.units.map(u=>{ const r=econReadCount(u.pis); const a=econAcc(u.pis);
    return `<div class="card stack-s"><div class="row between nowrap"><h2>${esc(u.title)}</h2><span class="chip ${r===u.pis.length?'good':''}">${r}/${u.pis.length}</span></div>
      <p class="small muted">${esc(u.blurb)}</p>
      <div class="stack-s">${u.pis.map(c=>`<a class="small" href="#econ-${c}">${econRead(c)?'✓ ':''}<span class="mono">${esc(c)}</span> ${esc(ECONPI[c].title)}</a>`).join('')}</div>
      <div class="row"><a class="btn sm" href="#quiz-econu.${u.id}">Quiz this unit</a><button class="btn sm" data-a="econJq" data-pool="eunit:${u.id}">${icon('mic')}Judge questions</button>${a.n?`<span class="tiny faint">${pct(a.c,a.n)}% correct</span>`:''}</div></div>`; }).join('')}</div>`;
}

function econPIView(x){
  if(!econRead(x.code)){ S.econRead=S.econRead||{}; S.econRead[x.code]=Date.now(); today().econ=1; save(); }
  else if(today().econPI===x.code && !today().econ){ today().econ=1; save(); }
  const u=ECONU[x.unit]; const i=ECON_ORDER.indexOf(x.code); const prev=ECONPI[ECON_ORDER[i-1]], next=ECONPI[ECON_ORDER[i+1]];
  const L=a=>`<ul class="model small">${a.map(s=>`<li>${esc(s)}</li>`).join('')}</ul>`;
  const tps=D.talk.filter(t=>t.pis.includes(x.code)); const nQ=D.questions.filter(q=>q.pi===x.code).length;
  const cs=D.cases.cases.filter(c=>c.pis.includes(x.code)); const ds=D.cases.drills.filter(d=>d.pis.includes(x.code));
  const h=piHits(x.code);
  return `<div class="wrap">${back('#econ','Econ Lab')}
  <div class="pagehead"><span class="label">${esc(u.title)} · ${esc(x.code)}</span><h1>${esc(x.title)}</h1><p class="small muted">PI: ${esc(PI[x.code]?.pi||'')}${h?` · on ${h} of ${NEXAMS} past exams`:''}</p></div>
  <div class="card stack"><span class="label">In plain English</span>${x.plain.map(s=>`<p>${esc(s)}</p>`).join('')}${CL.tts?`<button class="btn sm" style="align-self:flex-start" data-a="speakText" data-t="${esc(x.plain.join(' ').slice(0,1900))}">${icon('vol')}Hear it</button>`:''}</div>
  <div class="grid2"><div class="card stack-s"><span class="label">Key points</span>${L(x.key)}</div>
    <div class="card stack-s"><span class="label">In financial services</span>${L(x.fin)}</div></div>
  <div class="card stack-s"><span class="label">Real-world examples</span>${L(x.ex)}<span class="src">Sources are named in brackets. Numbers with a 2026 date change often: re-check them before regionals.</span></div>
  <div class="card tp"><span class="label">Say it to a judge</span><div class="say">${esc(x.say)}</div><div class="row"><button class="btn sm" data-a="copy" data-t="${esc(x.say)}">${icon('copy')}Copy line</button>${CL.tts?`<button class="btn sm" data-a="speakText" data-t="${esc(x.say)}">${icon('vol')}Hear it</button>`:''}</div></div>
  <div class="warn-note small"><strong>Trap:</strong> ${esc(x.trap)}</div>
  <div class="card stack"><div class="row between"><h2>Judge questions this PI prepares you for</h2><button class="btn sm" data-a="econJq" data-pool="epi:${x.code}">${icon('mic')}Practice both</button></div>
    <p class="tiny faint">Answer out loud first, then open the strong answer. Structure: Answer → Reason → Example → Tie back to the client.</p>
    ${x.qs.map((q,k)=>`<details class="jqd"><summary><strong>"${esc(q.q)}"</strong></summary><div class="stack-s" style="margin-top:8px"><div class="say">${esc(q.a)}</div><div class="row"><button class="btn sm" data-a="econJq" data-pool="epi:${x.code}" data-code="${x.code}" data-i="${k}">${icon('play')}Answer it out loud (45s)</button>${CL.tts?`<button class="btn sm" data-a="speakText" data-t="${esc(q.a)}">${icon('vol')}Hear the answer</button>`:''}</div></div></details>`).join('')}
  </div>
  <div class="card stack-s"><div class="row between"><h2>Flashcards</h2><a class="btn sm" href="#econ-cards">${icon('cards')}Study the econ decks</a></div>
    ${x.cards.map(([t,d,tip])=>`<details class="jqd"><summary><strong>${esc(t)}</strong></summary><p class="small" style="margin-top:6px">${esc(d)}</p>${tip?`<p class="tiny muted">${esc(tip)}</p>`:''}</details>`).join('')}</div>
  ${tps.length?`<div class="card stack"><h2>Real-world talking points (${tps.length})</h2><div class="stack">${tps.map(t=>`<div class="tp"><a href="#talk-${t.id}" style="color:inherit"><strong class="small">${esc(t.title)}</strong></a><p class="small">${esc(t.fact)}</p><div class="say">${esc(t.say)}</div><span class="src">${esc(t.source)}${t.asof?' · as of '+esc(t.asof):''}</span></div>`).join('')}</div></div>`:''}
  <div class="card stack-s"><span class="label">Practice it</span>
    <div class="row">${nQ?`<a class="btn primary sm" href="#quiz-pis.${x.code}">${nQ} exam questions</a>`:''}${DEEP[x.code]?`<a class="btn sm" href="#pi-${x.code}">Deep dive</a>`:''}</div>
    ${cs.length?`<span class="tiny faint">Roleplays that use this PI</span><div class="stack-s">${cs.map(c=>`<a class="small" href="#case-${c.id}">${esc(caseTitle(c))}</a>`).join('')}</div>`:''}
    ${ds.length?`<span class="tiny faint">60-second drills</span><div class="stack-s">${ds.map(d=>`<button class="list-link" data-a="econDrill" data-id="${d.id}"><span class="small">${esc(d.scenario)}</span></button>`).join('')}</div>`:''}</div>
  <div class="row between">${prev?`<a class="btn ghost sm" href="#econ-${prev.code}">${icon('back')}${esc(prev.title)}</a>`:'<span></span>'}${next?`<a class="btn sm" href="#econ-${next.code}">Next: ${esc(next.title)} →</a>`:''}</div>
  </div>`;
}

function econDeckRow(k,l,list){ const due=dueCards(list).length, cc=cardCounts(list);
  return `<div class="list-link"><span class="min0"><strong class="small">${esc(l)}</strong><br><span class="tiny muted">${list.length} cards · ${due} due · ${cc.nw} new · ${cc.ms} mastered</span></span><span class="row nowrap"><button class="btn sm primary" data-a="startCards" data-deck="${k}" data-mode="due">Study</button><button class="btn sm" data-a="startCards" data-deck="${k}" data-mode="cram">Cram 20</button></span></div>`; }
function econCardsTab(){
  return `<p class="small muted">Spaced repetition, same as the main flashcards: rate each card and it comes back right before you'd forget it. Study a few units a day so all ${ECONCARDS.length} terms are solid before regionals.</p>
  <div class="stack">${econDeckRow('econ','All Economics flashcards',ECONCARDS)}${econDeckRow('econjq','Judge questions: answer out loud, then flip',ECONJQ)}</div>
  <h2>By unit</h2><div class="stack">${ECON.units.map(u=>econDeckRow('econ:'+u.id,u.title,econDeck('econ:'+u.id))).join('')}</div>`;
}

function econTalkTab(){
  const q=(UI.econTq||'').toLowerCase(); const all=econTalk();
  const list=all.filter(t=>!q||(t.title+' '+t.fact+' '+t.say+' '+t.pis.join(' ')).toLowerCase().includes(q));
  return `<div class="row"><input class="input" style="max-width:320px" placeholder="Search (e.g. tariff, GDP, FCPA)" value="${esc(UI.econTq||'')}" data-in="econTq"><span class="tiny faint">${list.length} of ${all.length} talking points</span><a class="btn sm" href="#cards-facts">${icon('cards')}Study all facts as flashcards</a></div>
  <p class="tiny faint">Real numbers, laws and companies to drop into your answers. Time-sensitive facts show a date; re-check them before regionals.</p>
  <div class="stack">${list.map(t=>`<div class="card tp"><div class="row between nowrap"><a href="#talk-${t.id}" style="color:inherit;text-decoration:none"><strong>${esc(t.title)}</strong></a><button class="iconbtn" style="${S.talkStar[t.id]?'color:var(--warn)':''}" data-a="star" data-id="${t.id}" aria-label="Star">${icon('star')}</button></div><p class="small">${esc(t.fact)}</p><div class="say">${esc(t.say)}</div>${(t.answers||[]).length?`<span class="tiny muted">Helps answer: ${t.answers.map(a=>'"'+esc(a)+'"').join('  ')}</span>`:''}<div class="row between"><span class="chips">${t.pis.map(chipPI).join('')}</span><span class="src">${esc(t.source)}${t.asof?' · as of '+esc(t.asof):''}</span></div></div>`).join('')||'<div class="empty">No talking points match.</div>'}</div>`;
}

function econCasesTab(){
  const cs=econCases(); const ds=econDrills(); const last={}; (S.caseRuns||[]).forEach(r=>{ if(r.total!=null) last[r.caseId]=r; });
  return `<div class="card stack-s"><span class="label">How to practice for regionals</span><p class="small">Each case follows the district format: you're the advisors, the judge is the client, 5 PIs (mostly Economics), and two judge questions at the end. Do 30 minutes of prep with your partner, a 15-minute presentation, then score it with the rubric. To earn Exemplary on an econ PI, don't just define it: apply it to this client with a real number or example.</p>
    <div class="row"><button class="btn primary" data-a="econCase">${icon('shuffle')}Random econ case</button><button class="btn" data-a="econDrill">${icon('play')}Random 60-second econ drill</button></div></div>
  <h2>Economics cases (${cs.length})</h2>
  <div class="stack">${cs.map(c=>`<a class="list-link" href="#case-${c.id}"><span class="min0"><strong>${esc(caseTitle(c))}</strong><br><span class="small muted">You: ${esc(c.role)} · Judge: ${esc(c.judge)}</span><br><span class="chips" style="margin-top:4px">${c.pis.map(chipPI).join('')}</span></span>${last[c.id]?`<span class="chip ${last[c.id].total>=80?'good':last[c.id].total>=65?'warn':'bad'}">${last[c.id].total}</span>`:'<span class="chip acc">Econ</span>'}</a>`).join('')}</div>
  <h2>60-second econ drills (${ds.length})</h2>
  <div class="stack">${ds.map(d=>`<button class="list-link" data-a="econDrill" data-id="${d.id}"><span class="min0"><span class="small">${esc(d.scenario)}</span><br><span class="chips" style="margin-top:4px">${d.pis.map(chipPI).join('')}</span></span></button>`).join('')}</div>`;
}

function econJudgeTab(){
  const pool=allJudgeQs().filter(x=>x.econ||(x.cid&&caseById(x.cid)?.econ));
  return `<div class="card stack-s"><p class="small">The judge asks two questions at the end, and you answer on the spot. Hear a question, answer in 45 seconds, then compare with a strong answer. Each partner should take at least one.</p>
    <div class="row"><button class="btn primary" data-a="econJq" data-pool="econ">${icon('mic')}Practice all ${pool.length} econ judge questions</button><a class="btn" href="#cards-econjq">${icon('cards')}As flashcards</a></div></div>
  ${ECON.units.map(u=>{ const n=u.pis.reduce((m,c)=>m+ECONPI[c].qs.length,0);
    return `<details class="card"><summary><strong>${esc(u.title)}</strong> <span class="tiny faint">${n} questions</span></summary><div class="stack-s" style="margin-top:10px"><button class="btn sm" style="align-self:flex-start" data-a="econJq" data-pool="eunit:${u.id}">${icon('mic')}Practice this unit</button>
      ${u.pis.map(c=>ECONPI[c].qs.map((q,k)=>`<details class="jqd"><summary><span class="mono tiny">${esc(c)}</span> "${esc(q.q)}"</summary><div class="stack-s" style="margin-top:6px"><div class="say">${esc(q.a)}</div><div class="row"><button class="btn sm" data-a="econJq" data-pool="eunit:${u.id}" data-code="${c}" data-i="${k}">${icon('play')}Answer it out loud</button><a class="small" href="#econ-${c}">Read ${esc(c)}</a></div></div></details>`).join('')).join('')}</div></details>`; }).join('')}
  <details class="card"><summary><strong>From the econ roleplay cases</strong> <span class="tiny faint">${econCases().length*2} questions</span></summary><div class="stack-s" style="margin-top:10px">${econCases().map(c=>c.questions.map(q=>`<a class="small" href="#case-${c.id}">"${esc(q)}" · ${esc(caseTitle(c))}</a>`).join('')).join('')}</div></details>`;
}

function econQuizTab(){
  const qs=QS_BY_AREA['Economics']||[]; const a=econAcc(ECON_ORDER); const seen=qs.filter(q=>S.qs[q.id]).length;
  const weak=weakPIs(40).filter(w=>w.pi.startsWith('EC:')).slice(0,6);
  return `<div class="card stack-s"><div class="row between"><span class="label">Economics questions</span><span class="mono small">${seen}/${qs.length} seen${a.n?` · ${pct(a.c,a.n)}% correct`:''}</span></div>${bar(pct(seen,qs.length))}
    <div class="row"><a class="btn primary" href="#quiz-econ">20 econ questions</a><a class="btn" href="#quiz-pis.${ECON_ORDER.join(',')}">15 random econ questions</a></div>
    <p class="tiny faint">Econ sets mix never-seen questions with ones you missed earlier. Economics is about 6% of the cluster exam, and it's the regional roleplay focus.</p></div>
  ${weak.length?`<div class="card stack-s"><span class="label">Your weakest econ PIs</span>${weak.map(w=>`<a class="list-link" href="#econ-${w.pi}"><span class="small"><span class="mono">${esc(w.pi)}</span> ${esc(ECONPI[w.pi]?.title||'')}</span><span class="chip bad">${Math.round(w.acc*100)}%</span></a>`).join('')}</div>`:''}
  <h2>By unit</h2><div class="stack">${ECON.units.map(u=>{ const n=qs.filter(q=>u.pis.includes(q.pi)).length; const s=econAcc(u.pis);
    return `<a class="list-link" href="#quiz-econu.${u.id}"><span class="min0"><strong class="small">${esc(u.title)}</strong><br><span class="tiny muted">${n} questions · ${u.pis.length} PIs</span></span>${s.n?`<span class="chip ${status(s.c/s.n,s.n)[1]}">${pct(s.c,s.n)}%</span>`:'<span class="chip">Start</span>'}</a>`; }).join('')}</div>`;
}

Object.assign(A,{
  econJq(el){ UI.jqPool=el.dataset.pool||'econ'; const pool=judgePool();
    const i=el.dataset.code?pool.findIndex(x=>x.econ===el.dataset.code&&x.ei===+el.dataset.i):-1;
    UI.jq={i:i>=0?i:Math.floor(Math.random()*pool.length),stage:'ready'}; if(route().name!=='judge') location.hash='#judge'; else render(); },
  econCase(){ const cs=econCases(); const runs=new Set((S.caseRuns||[]).map(r=>r.caseId)); const fresh=cs.filter(c=>!runs.has(c.id)); location.hash='#case-'+pick(fresh.length?fresh:cs,1)[0].id; },
  econDrill(el){ const ds=econDrills(); let id=el.dataset.id;
    if(!id){ const runs={}; (S.drillRuns||[]).forEach(r=>runs[r.id]=r); const fresh=ds.filter(d=>!runs[d.id]); id=pick(fresh.length?fresh:ds,1)[0].id; }
    UI.drill={id,stage:'ready',ans:''}; if(route().name!=='drills') location.hash='#drills'; else render(); },
  goEcon(el){ location.hash='#econ-'+el.dataset.pi; },
});
Object.assign(IN,{
  econTq(el){ UI.econTq=el.value; clearTimeout(UI.etqT); UI.etqT=setTimeout(()=>{ render(); const i=$('[data-in="econTq"]'); if(i){ i.focus(); i.setSelectionRange(i.value.length,i.value.length);} },250); },
});
