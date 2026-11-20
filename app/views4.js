/* Views part 4: the Finance Hub (topics -> sub-topics, in depth, with judge questions and model answers). */
'use strict';
Object.assign(NAV_OF,{hub:'hub'});

function hubReadCount(list){ return list.filter(id=>(S.hubRead||{})[id]).length; }
function hubSearch(q){ q=q.toLowerCase(); const out=[];
  HUB.forEach(tp=>tp.subs.forEach(s=>{ const hay=[s.title,tp.title,...s.what,...s.how,...s.nums,...s.real,...s.qs.map(x=>x.q),s.pis.join(' ')].join(' ').toLowerCase();
    if(hay.includes(q)) out.push(s); })); return out; }
function hubSubLink(s,showTopic){ const read=(S.hubRead||{})[s.id]; return `<a class="list-link" href="#hub-${s.id}"><span class="min0"><strong class="small">${esc(s.title)}</strong>${showTopic?`<br><span class="tiny faint">${esc(HUBT[s.topic].title)}</span>`:''}<br><span class="tiny muted">${s.pis.map(esc).join(' · ')} · ${s.qs.length} judge questions</span></span>${read?'<span class="chip good">Read</span>':'<span class="chip">New</span>'}</a>`; }

V.hub=(arg)=>{
  if(arg && HUBSUB[arg]) return hubSubView(HUBSUB[arg]);
  if(arg && HUBT[arg]) return hubTopicView(HUBT[arg]);
  const nq=HUB.reduce((n,tp)=>n+tp.subs.reduce((m,s)=>m+s.qs.length,0),0); const read=hubReadCount(HUB_ORDER);
  const q=(UI.hubq||'').trim(); const nx=nextHubSub();
  return `<div class="wrap">${head('Finance Hub',`Every topic on the 2026-27 Finance PI list, in depth: how it works, key numbers with their sources, real-world examples, traps, and the judge questions each topic prepares you for, with strong answers. ${HUB.length} topics, ${HUB_ORDER.length} sub-topics, ${nq} judge questions.`)}
  <div class="card stack-s"><div class="row between"><span class="label">Your progress</span><span class="mono small">${read}/${HUB_ORDER.length} read</span></div>${bar(pct(read,HUB_ORDER.length),'good')}
    <div class="row">${nx?`<a class="btn primary" href="#hub-${nx.id}">Next up: ${esc(nx.title)}</a>`:''}<button class="btn" data-a="jqPractice" data-pool="hub">${icon('mic')}Practice judge questions</button><a class="btn" href="#cards-jq">${icon('cards')}Judge Q flashcards</a></div>
    <p class="tiny faint">In FTDM the judge asks questions at the end, and you answer on the spot. Each sub-topic lists the questions it prepares you for, with an Answer → Reason → Example → Tie back model.</p></div>
  <input class="input" placeholder="Search the hub (e.g. Roth, FDIC, break-even, inflation)" value="${esc(UI.hubq||'')}" data-in="hubq">
  ${q?`<div class="stack">${hubSearch(q).map(s=>hubSubLink(s,true)).join('')||'<div class="empty">Nothing matches. Try a shorter word.</div>'}</div>`
  :`<div class="grid2">${HUB.map(tp=>{ const ids=tp.subs.map(s=>s.id); const r=hubReadCount(ids);
    return `<div class="card stack-s"><div class="row between nowrap"><a href="#hub-${tp.id}" style="color:inherit;text-decoration:none"><h2>${esc(tp.title)}</h2></a><span class="chip ${r===ids.length?'good':''}">${r}/${ids.length}</span></div>
      <p class="small muted">${esc(tp.blurb)}</p>
      <div class="stack-s">${tp.subs.map(s=>`<a class="small" href="#hub-${s.id}">${(S.hubRead||{})[s.id]?'✓ ':''}${esc(s.title)}</a>`).join('')}</div>
      <span class="tiny faint">${tp.areas.map(esc).join(' · ')}</span></div>`; }).join('')}</div>`}
  </div>`;
};

function hubTopicView(tp){
  const ids=tp.subs.map(s=>s.id); const nq=tp.subs.reduce((m,s)=>m+s.qs.length,0);
  return `<div class="wrap">${back('#hub','Finance Hub')}${head(esc(tp.title),esc(tp.blurb))}
  <div class="row"><span class="chip">${hubReadCount(ids)}/${ids.length} read</span><button class="btn sm" data-a="jqPractice" data-pool="topic:${tp.id}">${icon('mic')}Practice this topic's ${nq} judge questions</button></div>
  <div class="stack">${tp.subs.map(s=>`<a class="card stack-s" href="#hub-${s.id}" style="text-decoration:none;color:inherit"><div class="row between nowrap"><strong>${esc(s.title)}</strong>${(S.hubRead||{})[s.id]?'<span class="chip good">Read</span>':''}</div>
    <p class="small muted">${esc(s.what[0].slice(0,190))}${s.what[0].length>190?'…':''}</p>
    <div class="chips">${s.pis.map(chipPI).join('')}</div>
    <span class="tiny faint">Prepares you for: ${s.qs.map(x=>'"'+esc(x.q)+'"').join('  ')}</span></a>`).join('')}</div></div>`;
}

function hubSubView(s){
  const tp=HUBT[s.topic];
  if(!(S.hubRead||{})[s.id]){ S.hubRead=S.hubRead||{}; S.hubRead[s.id]=Date.now(); today().hub=1; save(); }
  else if(today().hubSub===s.id && !today().hub){ today().hub=1; save(); }
  const i=HUB_ORDER.indexOf(s.id); const prev=HUBSUB[HUB_ORDER[i-1]], next=HUBSUB[HUB_ORDER[i+1]];
  const tps=TALK_BY_SUB[s.id]||[]; const deep=s.pis.filter(p=>DEEP[p]); const nQs=D.questions.filter(q=>s.pis.includes(q.pi)).length;
  const L=(a)=>`<ul class="model small">${a.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>`;
  return `<div class="wrap">${back('#hub-'+tp.id,tp.title)}
  <div class="pagehead"><span class="label">${esc(tp.title)}</span><h1>${esc(s.title)}</h1><div class="chips">${s.pis.map(chipPI).join('')}</div></div>
  <div class="card stack"><span class="label">In depth</span>${s.what.map(p=>`<p>${esc(p)}</p>`).join('')}${CL.tts?`<button class="btn sm" style="align-self:flex-start" data-a="speakText" data-t="${esc(s.what.join(' ').slice(0,1900))}">${icon('vol')}Hear it</button>`:''}</div>
  <div class="grid2"><div class="card stack-s"><span class="label">How it works</span>${L(s.how)}</div>
    <div class="card stack-s"><span class="label">Key numbers</span>${L(s.nums)}<span class="src">Sources are named in brackets. Numbers marked with a 2026 date are time-sensitive: re-check before competing.</span></div></div>
  <div class="card stack-s"><span class="label">Real-world examples</span>${L(s.real)}</div>
  <div class="card tp"><span class="label">Say it to a judge</span><div class="say">${esc(s.say)}</div><div class="row"><button class="btn sm" data-a="copy" data-t="${esc(s.say)}">${icon('copy')}Copy line</button>${CL.tts?`<button class="btn sm" data-a="speakText" data-t="${esc(s.say)}">${icon('vol')}Hear it</button>`:''}</div></div>
  <div class="warn-note small"><strong>Traps:</strong> ${s.traps.map(esc).join(' ')}</div>
  <div class="card stack"><div class="row between"><h2>Judge questions this prepares you for</h2><button class="btn sm" data-a="jqPractice" data-pool="sub:${s.id}">${icon('mic')}Practice all ${s.qs.length}</button></div>
    <p class="tiny faint">Try answering out loud first, then open the strong answer. Structure: Answer → Reason → Example → Tie back to the client.</p>
    ${s.qs.map((x,k)=>`<details class="jqd"><summary><strong>"${esc(x.q)}"</strong></summary><div class="stack-s" style="margin-top:8px"><div class="say">${esc(x.a)}</div><div class="row"><button class="btn sm" data-a="jqPractice" data-pool="sub:${s.id}" data-i="${k}">${icon('play')}Answer it out loud (45s)</button>${CL.tts?`<button class="btn sm" data-a="speakText" data-t="${esc(x.a)}">${icon('vol')}Hear the answer</button>`:''}</div></div></details>`).join('')}
  </div>
  ${tps.length?`<div class="card stack"><h2>Real-world talking points (${tps.length})</h2><div class="stack">${tps.map(t=>`<div class="tp"><a href="#talk-${t.id}" style="color:inherit"><strong class="small">${esc(t.title)}</strong></a><p class="small">${esc(t.fact)}</p><div class="say">${esc(t.say)}</div>${t.answers&&t.answers.length?`<span class="tiny muted">Helps answer: ${t.answers.map(a=>'"'+esc(a)+'"').join('  ')}</span>`:''}<span class="src">${esc(t.source)}${t.asof?' · as of '+esc(t.asof):''}</span></div>`).join('')}</div></div>`:''}
  <div class="card stack-s"><span class="label">Go deeper</span>
    <div class="row">${nQs?`<a class="btn primary sm" href="#quiz-pis.${s.pis.join(',')}">Practice ${Math.min(nQs,15)} exam questions</a>`:''}${deep.map(p=>`<a class="btn sm" href="#pi-${p}">Deep dive ${esc(p)}</a>`).join('')}</div>
    ${s.learn.length?`<div class="stack-s">${s.learn.map(([l,u])=>`<a class="small" href="${esc(u)}" target="_blank" rel="noopener">${esc(l)} ↗</a>`).join('')}</div>`:''}</div>
  <div class="row between">${prev?`<a class="btn ghost sm" href="#hub-${prev.id}">${icon('back')}${esc(prev.title)}</a>`:'<span></span>'}${next?`<a class="btn sm" href="#hub-${next.id}">Next: ${esc(next.title)} →</a>`:''}</div>
  </div>`;
}

Object.assign(A,{
  jqPractice(el){ UI.jqPool=el.dataset.pool||'all'; const pool=judgePool(); const i=el.dataset.i!=null?pool.findIndex(x=>x.hub===UI.jqPool.slice(4)&&x.hi===+el.dataset.i):-1;
    UI.jq={i:i>=0?i:Math.floor(Math.random()*pool.length),stage:'ready'}; if(route().name!=='judge') location.hash='#judge'; else render(); },
});
Object.assign(IN,{
  hubq(el){ UI.hubq=el.value; clearTimeout(UI.hqT); UI.hqT=setTimeout(()=>{ render(); const i=$('[data-in="hubq"]'); if(i){ i.focus(); i.setSelectionRange(i.value.length,i.value.length);} },250); },
  jqPool(el){ UI.jqPool=el.value; if(TIMER.endsAt&&TIMER.kind==='judgeQ') TIMER.stopLocal(true); const pool=judgePool(); UI.jq={i:Math.floor(Math.random()*pool.length),stage:'ready'}; render(); },
});
