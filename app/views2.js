/* Views part 2: Roleplay (cases, timers, planner, rubric, AI judge), drills, judge questions, talking points,
   playbook, team, settings, actions, boot. */
'use strict';

/* ================= TIMER ================= */
const PRESENT_PHASES = [
  {at:0,   cue:'Greet the judge, introduce both partners, give the agenda'},
  {at:60,  cue:'Walk through the PIs: explain, apply to this client, prove with a real example'},
  {at:540, cue:'Your solution: unique, practical, effective. Timeline and who does what'},
  {at:660, cue:'Recap the 3 biggest takeaways, then invite questions'},
  {at:720, cue:'Judge questions: both partners answer at least one'},
];
const TIMER = {
  kind:null, caseId:null, total:0, endsAt:0, iv:null, lastPhase:-1, remote:false,
  startLocal(kind, caseId, seconds, fromRemote=false){ this.stopLocal(true); Object.assign(this,{kind,caseId,total:seconds,endsAt:Date.now()+seconds*1000,lastPhase:-1,remote:fromRemote});
    this.iv=setInterval(()=>this.tick(),250); keepAwake(true); this.tick(); if(!fromRemote) beep(660,.12); },
  stopLocal(silent){ clearInterval(this.iv); this.iv=null; this.endsAt=0; keepAwake(false); if(!silent) this.paint(); },
  left(){ return this.endsAt? Math.max(0,(this.endsAt-Date.now())/1000) : 0; },
  phaseIdx(){ if(this.kind!=='present') return -1; const el=(this.total-this.left())*(900/this.total); let i=0; PRESENT_PHASES.forEach((p,k)=>{ if(el>=p.at) i=k; }); return i; },
  tick(){ const l=this.left(); const pi=this.phaseIdx(); if(pi!==this.lastPhase){ if(this.lastPhase>=0) beep(880,.15,2); this.lastPhase=pi; }
    if(this.kind==='prep' && Math.abs(l-300)<0.13) beep(740,.15,1);
    this.paint(); if(l<=0){ clearInterval(this.iv); this.iv=null; keepAwake(false); beep(520,.35,3); this.onEnd(); } },
  paint(){ const el=$('#bigtimer'); if(!el) return; const l=this.left(); el.textContent=fmtTime(this.endsAt?l:(this.total||0)); el.classList.toggle('low',this.endsAt&&l<60);
    const n=$('#needle'); if(n&&this.total) n.style.left=(100*(1-l/this.total))+'%'; const c=$('#cue'); if(c){ const i=this.phaseIdx(); c.textContent= this.kind==='present'? PRESENT_PHASES[Math.max(0,i)].cue : (this.kind==='prep'? (l>this.total*.8?'Read the case together. Underline the 5 PIs and what the client asked for.':l>this.total*.35?'Split the PIs. Each partner drafts explain + apply + example.':l>this.total*.1?'Write the solution and the opening line. Rehearse handoffs.':'Final run-through. Pick who answers which judge question.') : ''); }
    const sb=$('#timer-btn'); if(sb) sb.innerHTML= this.endsAt? icon('stop')+'Stop' : icon('play')+'Start'; },
  onEnd(){ const k=this.kind; this.endsAt=0; this.paint(); if(k==='prep'){ toast('Prep time is up. Start the presentation.'); } else if(k==='present'){ toast('Time. Score it with the official rubric.'); const cid=this.caseId; UI.caseStep[cid]='score'; if(route().name==='case') rerender(); }
    else if(k==='drillPrep'){ UI.drill.stage='speak'; this.startLocal('drillSpeak',null,60); rerender(); } else if(k==='drillSpeak'){ UI.drill.stage='review'; rerender(); } else if(k==='judgeQ'){ UI.jq.stage='review'; rerender(); } else if(k==='sketch'){ toast('Time. Check your sketch against the list.'); } },
};

/* ================= ROLEPLAY HUB ================= */
V.roleplay=()=>{
  const f=UI.caseFilter||'all'; const cases=allCases().filter(c=>f==='all'||(f==='client'?c.style==='client':f==='ai'?c.style==='ai':c.style!=='client'&&c.style!=='ai'));
  const last={}; (S.caseRuns||[]).forEach(r=>{ if(r.total!=null) last[r.caseId]=r; });
  return `<div class="wrap">${head('Roleplay','Practice the way FTDM is judged: 30 minutes to prep with your partner, 15 minutes with the judge, scored out of 100 on five PIs, a unique/practical/effective solution, three career competencies and overall impression.')}
  <div class="grid3">
    <a class="card stack-s" href="#drills" style="text-decoration:none;color:inherit"><span class="label">Quick reps</span><strong>60-second drills</strong><span class="small muted">${D.cases.drills.length} prompts · prep 1 min, speak 1 min</span></a>
    <a class="card stack-s" href="#judge" style="text-decoration:none;color:inherit"><span class="label">Pressure test</span><strong>Judge questions</strong><span class="small muted">Hear a question, answer in 45 seconds</span></a>
    <a class="card stack-s" href="#playbook" style="text-decoration:none;color:inherit"><span class="label">How to win</span><strong>Roleplay playbook</strong><span class="small muted">Structure, phrases, partner handoffs</span></a>
    <a class="card stack-s" href="#charts" style="text-decoration:none;color:inherit"><span class="label">Stand out</span><strong>Charts that win judges</strong><span class="small muted">Which chart for which PI, and how to sketch it in prep</span></a>
  </div>
  ${CL.sample?`<div class="card row between"><div class="min0"><strong>Need a fresh case?</strong><p class="small muted">Claude writes a new FTDM-style case with 5 PIs, two judge questions and a model answer.${CL.db&&!CL.writeBlocked?' It is shared with your partner.':''}</p></div><button class="btn" data-a="genCase">${icon('spark')}Generate a case</button></div>`:''}
  <div class="chips">${[['all','All cases'],['client','Client advising (like recent district cases)'],['business','Business consulting'],...(allCases().some(c=>c.style==='ai')?[['ai','AI-generated']]:[])].map(([k,l])=>`<button class="chip ${f===k?'on':''}" data-a="caseFilter" data-v="${k}">${l}</button>`).join('')}</div>
  <div class="stack">${cases.map(c=>`<a class="list-link" href="#case-${c.id}"><span class="min0"><strong>${esc(caseTitle(c))}</strong><br><span class="small muted">You: ${esc(c.role)} · Judge: ${esc(c.judge)}</span><br><span class="chips" style="margin-top:4px">${c.pis.map(chipPI).join('')}</span></span>${last[c.id]?`<span class="chip ${last[c.id].total>=80?'good':last[c.id].total>=65?'warn':'bad'}">${last[c.id].total}</span>`:c.style==='client'?'<span class="chip acc">Client</span>':c.style==='ai'?'<span class="chip info">AI</span>':''}</a>`).join('')}</div></div>`;
};
function caseTitle(c){ if(c.title) return c.title; const m=c.judge.match(/^(?:owner|CEO|president|founder and CEO|founder|chief financial officer|CFO|director)[^,]*?of ([A-Z][A-Z0-9 '&.-]+)/); if(m) return m[1].trim()+' · '+c.area; const j=c.judge.replace(/^(an?|the)\s+/i,''); return j.charAt(0).toUpperCase()+j.slice(1); }

/* ================= CASE ================= */
const PREP_KEYS = c => ['opening',...c.pis.map((_,i)=>'pi'+i),'solution','impl','close','q0','q1'];
function prepGet(cid,key){ return S.notes['prep-'+cid]?.f?.[key]??''; }
function prepSet(cid,key,val,remote){ const n=S.notes['prep-'+cid]=S.notes['prep-'+cid]||{f:{}}; n.f=n.f||{}; n.f[key]=val; n.last=Date.now(); save(); if(!remote) PREPSYNC.push(cid,key,val); }
const PREPSYNC = { unsub:null, cid:null, timers:{},
  watch(cid){ if(this.cid===cid) return; this.stop(); if(!CL.db) return; this.cid=cid;
    try{ this.unsub=CL.db.collection('prep/'+cid+'/fields').onSnapshot(qs=>{ qs.docs.forEach(d=>{ if(!d.exists||d.metadata.hasPendingWrites) return; const v=d.data(); const k=d.id; if(v.by===CL.uid && v.v===prepGet(cid,k)) return; if(v.v!==prepGet(cid,k)){ prepSet(cid,k,v.v,true); const el=document.getElementById('prep-'+k); if(el && document.activeElement!==el){ el.value=v.v; } if(k.endsWith('o')){ const g=document.querySelector(`[data-owner="${k}"]`); if(g) rerender(); } const tag=document.getElementById('by-'+k); if(tag) tag.textContent= v.by===CL.uid?'':'edited by '+nameOf(v.by); } }); }, ()=>{}); }catch(e){} },
  stop(){ try{ this.unsub&&this.unsub(); }catch(e){} this.unsub=null; this.cid=null; },
  push(cid,key,val){ if(!CL.db||CL.writeBlocked) return; clearTimeout(this.timers[key]); this.timers[key]=setTimeout(()=>{ CL.db.doc('prep/'+cid+'/fields/'+key).set({v:val,by:CL.uid||'',t:Date.now()}).catch(e=>{ if(e?.code==='invalid_argument') CL.writeBlocked=true; }); },900); },
};
V.case=(cid)=>{
  const c=caseById(cid); if(!c) return V.roleplay();
  UI.caseStep=UI.caseStep||{}; const step=UI.caseStep[cid]||'read'; const half=!!UI.half;
  PREPSYNC.watch(cid);
  const tabs=[['read','1 · Read'],['prep','2 · Prep'],['present','3 · Present'],['score','4 · Score']];
  return `<div class="wrap">${back('#roleplay','All cases')}
  ${head(esc(caseTitle(c)),`<span class="chip">${esc(c.area)}</span> ${c.style==='client'?'<span class="chip acc">Client advising</span>':''}`)}
  <div class="chips scrollx">${tabs.map(([k,l])=>`<button class="chip ${step===k?'on':''}" data-a="caseStep" data-id="${cid}" data-v="${k}">${l}</button>`).join('')}<button class="chip ${half?'on':''}" data-a="toggleHalf">Half case (10 + 7 min)</button></div>
  ${step==='read'?caseRead(c):step==='prep'?casePrep(c,half):step==='present'?casePresent(c,half):caseScore(c)}
  </div>`;
};
function caseRead(c){
  return `<div class="card stack"><div class="row between"><span class="label">Participant instructions</span>${CL.tts?`<button class="btn sm" data-a="speakCase" data-id="${c.id}">${icon('vol')}Read it to me</button>`:''}</div>
    <p>You are to assume the roles of <strong>${esc(c.role)}</strong>. The judge is the <strong>${esc(c.judge)}</strong>.</p>
    <p>${esc(c.situation)}</p>
    <div><span class="label">Your team will discuss</span><ul class="model" style="margin-top:6px">${c.tasks.map(t=>`<li>${esc(t)}</li>`).join('')}</ul></div>
    <div><span class="label">Performance indicators (10 points each)</span><div class="stack-s" style="margin-top:6px">${c.pis.map(p=>`<div class="row nowrap small">${chipPI(p)}<span class="min0">${esc(PI[p]?.pi||p)}</span></div>`).join('')}</div></div>
    <div class="blue-note small"><strong>Also scored:</strong> a unique, practical and effective solution (8 points each), critical thinking, communication and decision making (6 each), and overall impression (8). You have 30 minutes to prep and 15 minutes with the judge, including questions. Both partners must speak.</div>
    <div class="row"><button class="btn primary" data-a="caseStep" data-id="${c.id}" data-v="prep">Start prep</button><a class="btn" href="#judgemode-${c.id}">Judge mode (for a parent or friend)</a></div></div>`;
}
function relatedTalk(c){ const set=new Set(c.pis); return D.talk.filter(t=>t.pis.some(p=>set.has(p))).slice(0,8); }
function ownerToggle(cid,key){ const v=prepGet(cid,key)||''; return `<span class="owner" data-owner="${key}">${['A','B','Both'].map(o=>`<button class="${v===o?'on':''}" data-a="setOwner" data-id="${cid}" data-k="${key}" data-v="${o}">${o==='A'?'Partner A':o==='B'?'Partner B':'Both'}</button>`).join('')}</span>`; }
function prepField(cid,key,label,ph,rows=3){ return `<label class="field">${label}<textarea class="input" id="prep-${key}" data-in="prep" data-id="${cid}" data-k="${key}" rows="${rows}" placeholder="${esc(ph)}">${esc(prepGet(cid,key))}</textarea><span class="tiny faint" id="by-${key}"></span></label>`; }
function casePrep(c,half){
  const secs=half?600:1800; const running=TIMER.endsAt&&TIMER.kind==='prep'&&TIMER.caseId===c.id;
  const shared=CL.db&&!CL.writeBlocked;
  return `<div class="card stack"><div class="row between"><span class="label">Prep timer · ${half?10:30} minutes</span>${CL.room?`<span class="tiny faint">${onlinePeers().length?'Starts on your partner\'s screen too':'Partner timer syncs when they have the app open'}</span>`:''}</div>
    <div class="bigtimer" id="bigtimer">${fmtTime(running?TIMER.left():secs)}</div><div class="cue small muted" id="cue" style="font-size:1rem">Press start when you open the case.</div>
    <div class="row" style="justify-content:center"><button class="btn primary lg" id="timer-btn" data-a="timer" data-k="prep" data-id="${c.id}" data-s="${secs}">${running?icon('stop')+'Stop':icon('play')+'Start'}</button></div></div>
  <div class="card stack"><div class="row between"><h2>Team planner</h2><span class="chip ${shared?'good':''}">${shared?'Shared live with your partner':'Saved on this device'}</span></div>
    <p class="small muted">For each PI: <strong>explain</strong> it in one sentence, <strong>apply</strong> it to this client, and <strong>prove</strong> it with a real-world fact or number. Assign each PI to a partner so both of you speak.</p>
    <div class="planner">
      ${prepField(c.id,'opening','Opening line + agenda','"Thank you for meeting with us. Today we will cover… and leave you with a plan to…"',2)}
      ${c.pis.map((p,i)=>`<div class="pi-block"><div class="hd"><span class="row nowrap">${chipPI(p)}<strong class="small min0">${esc(PI[p]?.pi||p)}</strong></span>${ownerToggle(c.id,'pi'+i+'o')}</div>
        <textarea class="input" id="prep-pi${i}" data-in="prep" data-id="${c.id}" data-k="pi${i}" rows="3" placeholder="Explain: …  Apply: …  Proof: …">${esc(prepGet(c.id,'pi'+i))}</textarea><span class="tiny faint" id="by-pi${i}"></span></div>`).join('')}
      ${prepField(c.id,'solution','Solution: what makes it unique, practical and effective?','One clear recommendation, with a twist the judge hasn\'t heard 20 times today')}
      ${prepField(c.id,'impl','Implementation: timeline, cost, who does what, how you measure success','Month 1: … · Month 3: … · KPI: …')}
      ${prepField(c.id,'close','Closing','Recap three takeaways, thank the judge, invite questions',2)}
    </div></div>
  <div class="card stack"><div class="row between"><h2>Visual to sketch</h2><a class="btn sm" href="#charts">All chart types</a></div><p class="small muted">Spend 3-5 minutes of prep on one hand-drawn chart. You can hand it to the judge. These fit this case's PIs:</p>
    <div class="grid2">${chartsFor(c).slice(0,2).map(id=>`<a class="card flat stack-s" href="#charts-${id}" style="text-decoration:none;color:inherit"><strong class="small">${esc(CHART[id].name)}</strong><div class="chart-wrap">${CHART[id].svg()}</div></a>`).join('')}</div></div>
  <details class="card"><summary>Real-world support for these PIs (${relatedTalk(c).length})</summary><div class="stack">${relatedTalk(c).map(t=>`<div class="tp"><strong class="small">${esc(t.title)}</strong><div class="say">${esc(t.say)}</div><span class="src">${esc(t.source)}${t.asof?' · as of '+esc(t.asof):''}</span></div>`).join('')||'<p class="small muted">Browse all talking points on the Talking points page.</p>'}</div></details>
  <button class="btn primary lg" data-a="caseStep" data-id="${c.id}" data-v="present">I'm ready: start the presentation</button>`;
}
function casePresent(c,half){
  const secs=half?420:900; const running=TIMER.endsAt&&TIMER.kind==='present'&&TIMER.caseId===c.id; const qs=UI.showQs?.[c.id];
  const segs=PRESENT_PHASES.map((p,i)=>({w:((PRESENT_PHASES[i+1]?.at??900)-p.at)/9}));
  const cols=['var(--info)','var(--accent)','var(--warn)','var(--good)','var(--bad)'];
  return `<div class="card stack"><span class="label">Presentation · ${half?7:15} minutes including judge questions</span>
    <div class="bigtimer" id="bigtimer">${fmtTime(running?TIMER.left():secs)}</div>
    <div class="phasebar">${segs.map((s,i)=>`<span style="width:${s.w}%;background:${cols[i]};opacity:.55"></span>`).join('')}<i class="needle" id="needle" style="left:0"></i></div>
    <div class="cue" id="cue">${PRESENT_PHASES[0].cue}</div>
    <div class="row" style="justify-content:center"><button class="btn primary lg" id="timer-btn" data-a="timer" data-k="present" data-id="${c.id}" data-s="${secs}">${running?icon('stop')+'Stop':icon('play')+'Start'}</button></div>
    <p class="tiny faint" style="text-align:center">Beeps mark each phase. Prop up the phone where both of you can see it.</p></div>
  <div class="card stack"><div class="row between"><h2>Judge questions</h2><div class="row">${CL.tts&&qs?`<button class="btn sm" data-a="speakQs" data-id="${c.id}">${icon('vol')}Ask aloud</button>`:''}<button class="btn sm" data-a="showQs" data-id="${c.id}">${qs?'Hide':'Reveal'}</button></div></div>
    ${qs?`<ol class="model">${c.questions.map(q=>`<li><strong>${esc(q)}</strong></li>`).join('')}</ol><p class="small muted">Answer framework: <strong>Answer</strong> in one sentence → <strong>Reason</strong> → <strong>Example</strong> with a real fact → <strong>Tie back</strong> to the client's goal. Partner A takes question 1, Partner B takes question 2.</p>`:'<p class="small muted">Reveal them at the 12-minute mark, the way a real judge would ask after your presentation.</p>'}</div>
  <div class="card stack"><div class="row between"><h2>Record what you said</h2>${CL.dict?`<button class="btn sm mic" id="mic-transcript" data-a="mic" data-target="transcript-${c.id}">${icon('mic')}Dictate</button>`:''}</div>
    <textarea class="input" id="transcript-${c.id}" data-in="note" data-k="transcript-${c.id}" rows="5" placeholder="Paste or dictate your presentation, or type the main points you made. The AI judge uses this.">${esc(S.notes['transcript-'+c.id]?.text||'')}</textarea><span class="tiny faint" id="partial-transcript-${c.id}"></span></div>
  <button class="btn primary lg" data-a="caseStep" data-id="${c.id}" data-v="score">Score this run</button>`;
}
function caseScore(c){
  UI.rub=UI.rub||{}; const r=UI.rub[c.id]=UI.rub[c.id]||{}; const total=RUBRIC.reduce((s,x)=>s+(r[x.k]??0),0);
  const grp={}; RUBRIC.forEach((x,i)=>{(grp[x.grp]=grp[x.grp]||[]).push({...x,label:x.k.startsWith('pi')?`${c.pis[+x.k[2]-1]}: ${PI[c.pis[+x.k[2]-1]]?.pi||''}`:x.label});});
  const band=v=>v>=.95?'Exemplary':v>=.7?'Proficient':v>=.4?'Developing':'Novice';
  return `<div class="card stack"><div class="row between"><h2>Judge's evaluation</h2><span class="score-big" id="rub-total">${total}<small class="faint" style="font-size:1rem">/100</small></span></div>
    <p class="small muted">Same lines and point values as the 2026 FTDM district evaluation form. Be a tough judge: "Exemplary" means you applied the PI to solve this client's problem with real-world reasoning, not just defined it.</p>
    ${Object.entries(grp).map(([g,items])=>`<div class="stack-s"><span class="label">${g}</span><div class="rub">${items.map(x=>`<span class="small">${esc(x.label)}<br><span class="tiny faint" id="band-${x.k}">${r[x.k]!=null?band((r[x.k])/x.max)+' · ':''}${r[x.k]??0}/${x.max}</span></span><input type="range" min="0" max="${x.max}" step="1" value="${r[x.k]??0}" data-in="rub" data-id="${c.id}" data-k="${x.k}" data-max="${x.max}" aria-label="${esc(x.label)}">`).join('')}</div></div>`).join('')}
    <div class="row"><button class="btn primary" data-a="saveRun" data-id="${c.id}">Save score</button>${CL.sample?`<button class="btn" data-a="aiJudge" data-id="${c.id}">${icon('spark')}Have Claude judge my transcript</button>`:''}</div><div id="ai-judge"></div></div>
  <details class="card" open><summary>Model answer</summary><ul class="model">${c.model.map(m=>`<li>${esc(m)}</li>`).join('')}</ul></details>`;
}
V.judgemode=(cid)=>{
  const c=caseById(cid); if(!c) return V.roleplay();
  return `<div class="wrap">${back('#case-'+cid,'Back to case')}${head('Judge mode','Hand this screen to a parent, teacher or friend. They play the client, ask the two questions, and score the team.')}
  <div class="card stack"><span class="label">You are the ${esc(c.judge)}</span><p>${esc(c.situation)}</p><div class="blue-note small">Start by greeting the team and asking to hear their ideas. Let them present without interrupting. After they finish (or at about 12 minutes), ask each question below. End by thanking them.</div>
  <ol class="model">${c.questions.map(q=>`<li><strong>${esc(q)}</strong></li>`).join('')}</ol>
  <details><summary class="small">What a strong team should cover (don't show the team)</summary><ul class="model small">${c.model.map(m=>`<li>${esc(m)}</li>`).join('')}</ul></details></div>
  <div class="row"><button class="btn primary" data-a="caseStep" data-id="${cid}" data-v="score">Go to the score sheet</button></div></div>`;
};

/* ================= DRILLS ================= */
V.drills=()=>{
  const d=UI.drill; if(!d) return drillPicker();
  const dr=DRILL[d.id]; const st=d.stage;
  return `<div class="wrap"><div class="row between"><button class="btn ghost sm" data-a="endDrill">${icon('back')}Drills</button><span class="chips">${dr.pis.map(chipPI).join('')}</span></div>
  <div class="card stack"><div class="row between"><span class="label">${st==='prep'?'Think · 60 seconds':st==='speak'?'Speak · 60 seconds':st==='review'?'Compare':'Ready'}</span>${CL.tts?`<button class="btn sm ghost" data-a="speakText" data-t="${esc(dr.scenario)}">${icon('vol')}Hear it</button>`:''}</div>
    <p style="font-size:1.08rem;font-weight:600">${esc(dr.scenario)}</p>
    ${st!=='review'?`<div class="bigtimer" id="bigtimer">${fmtTime(TIMER.endsAt&&(TIMER.kind==='drillPrep'||TIMER.kind==='drillSpeak')?TIMER.left():60)}</div>`:''}
    ${st==='ready'?`<button class="btn primary lg" data-a="drillGo">Start 60-second prep</button>`:''}
    ${st==='prep'?`<button class="btn lg" data-a="drillSkip">Skip to speaking</button>`:''}
    ${st==='speak'?`<p class="cue">Answer out loud now, as if the judge is in front of you.</p><button class="btn lg" data-a="drillDone">I'm done</button>`:''}
    <div class="stack-s"><div class="row between"><span class="label">Your answer (optional)</span>${CL.dict?`<button class="btn sm mic" id="mic-drill-ans" data-a="mic" data-target="drill-ans">${icon('mic')}Dictate</button>`:''}</div><textarea class="input" id="drill-ans" rows="4" data-in="drillAns" placeholder="Dictate or jot what you said so you can compare and get feedback.">${esc(d.ans||'')}</textarea><span class="tiny faint" id="partial-drill-ans"></span></div>
    ${st==='review'?`<div class="tp"><span class="label">Model answer</span><div class="say">${esc(dr.model)}</div></div>
      <div class="stack-s"><span class="label">How did you do?</span><div class="rate">${[['Missed it',1],['Shaky',2],['Solid',3],['Nailed it',4]].map(([l,v])=>`<button class="btn ${d.rating===v?'primary':''}" data-a="rateDrill" data-v="${v}">${l}</button>`).join('')}</div></div>
      <div class="row">${CL.sample?`<button class="btn" data-a="aiDrill">${icon('spark')}Feedback from Claude</button>`:''}<button class="btn primary" data-a="nextDrill">Next drill</button></div><div id="ai-drill"></div>`:''}
  </div></div>`;
};
function drillPicker(){ const runs={}; (S.drillRuns||[]).forEach(r=>runs[r.id]=r);
  return `<div class="wrap">${back('#roleplay','Roleplay')}${head('60-second drills','Short, frequent speaking reps build the habit of answering with a clear point, a reason and a real example. Prep 1 minute, speak 1 minute, then compare with a model answer.')}
  <button class="btn primary lg" data-a="randomDrill">${icon('shuffle')}Random drill</button>
  <div class="stack">${D.cases.drills.map(d=>`<button class="list-link" data-a="openDrill" data-id="${d.id}"><span class="min0"><span class="small">${esc(d.scenario)}</span><br><span class="chips" style="margin-top:4px">${d.pis.map(chipPI).join('')}</span></span>${runs[d.id]?`<span class="chip ${runs[d.id].rating>=3?'good':'warn'}">${['','Missed','Shaky','Solid','Nailed'][runs[d.id].rating]||'Done'}</span>`:''}</button>`).join('')}</div></div>`; }

/* ================= JUDGE QUESTIONS ================= */
function allJudgeQs(){ const out=[]; allCases().forEach(c=>c.questions.forEach((q,i)=>{ const m=c.model.find(x=>x.startsWith('Judge Q'+(i+1))); out.push({cid:c.id,q,model:m?m.replace(/^Judge Q\d:\s*/,''):'',ctx:c.judge}); })); return out; }
V.judge=()=>{
  const all=allJudgeQs(); if(!UI.jq) UI.jq={i:Math.floor(Math.random()*all.length),stage:'ready'};
  const J=UI.jq; const it=all[J.i%all.length];
  return `<div class="wrap">${back('#roleplay','Roleplay')}${head('Judge questions','Every FTDM judge asks the same two questions to every team, and each partner should answer at least one. Practice answering with Answer → Reason → Example → Tie back.')}
  <div class="card stack"><span class="label">The judge is the ${esc(it.ctx)}</span><p style="font-size:1.2rem;font-weight:650">"${esc(it.q)}"</p>
    ${J.stage!=='review'?`<div class="bigtimer" id="bigtimer">${fmtTime(TIMER.endsAt&&TIMER.kind==='judgeQ'?TIMER.left():45)}</div>`:''}
    <div class="row" style="justify-content:center">${J.stage==='ready'?`<button class="btn primary lg" data-a="jqGo">${CL.tts?icon('vol')+'Ask me and start 45s':icon('play')+'Start 45 seconds'}</button>`:J.stage==='speak'?`<button class="btn lg" data-a="jqDone">Done answering</button>`:''}</div>
    ${J.stage==='review'?`<div class="tp"><span class="label">A strong answer</span><div class="say">${esc(it.model||'Use the case model answer.')}</div><a class="small" href="#case-${it.cid}">Open the full case</a></div><button class="btn primary" data-a="jqNext">Next question</button>`:''}
  </div></div>`;
};

/* ================= TALKING POINTS ================= */
V.talk=(tid)=>{
  if(tid&&TALK[tid]){ const t=TALK[tid]; if(!today().fact && todaysFact().id===tid){ today().fact=1; save(); }
    return `<div class="wrap">${back('#talk','All talking points')}<div class="card tp"><span class="label">${esc(t.topic)}</span><h2>${esc(t.title)}</h2><p>${esc(t.fact)}</p><span class="label">Say it in the roleplay</span><div class="say">${esc(t.say)}</div><div class="chips">${t.pis.map(chipPI).join('')}</div><span class="src">Source: ${esc(t.source)}${t.asof?' · Time-sensitive, as of '+esc(t.asof)+'. Re-check before competing.':''}</span>
    <div class="row"><button class="btn sm" data-a="copy" data-t="${esc(t.say)}">${icon('copy')}Copy line</button><button class="btn sm ${S.talkStar[t.id]?'primary':''}" data-a="star" data-id="${t.id}">${icon('star')}${S.talkStar[t.id]?'Starred':'Star'}</button>${CL.tts?`<button class="btn sm" data-a="speakText" data-t="${esc(t.say)}">${icon('vol')}Hear it</button>`:''}</div></div></div>`; }
  const topics=[...new Set(D.talk.map(t=>t.topic))]; const f=UI.talkTopic||'all'; const q=(UI.talkq||'').toLowerCase(); const pi=UI.talkPI;
  const list=D.talk.filter(t=>(f==='all'||(f==='star'?S.talkStar[t.id]:t.topic===f))&&(!pi||t.pis.includes(pi))&&(!q||(t.title+' '+t.fact+' '+t.say).toLowerCase().includes(q)));
  return `<div class="wrap">${head('Talking points','Real companies, laws, numbers and events to make your roleplay answers concrete, like recommending automatic monthly investing into an S&P 500 index fund at a brokerage such as Fidelity. Every fact lists its source; time-sensitive numbers show a date.')}
  <div class="row"><input class="input" style="max-width:320px" placeholder="Search (e.g. FDIC, Roth, inflation)" value="${esc(UI.talkq||'')}" data-in="talkq">${pi?`<button class="chip on" data-a="talkFilterPI" data-pi="">${esc(pi)} ×</button>`:''}<a class="btn sm" href="#cards-facts">${icon('cards')}Study as flashcards</a></div>
  <div class="chips scrollx">${[['all','All'],['star','Starred'],...topics.map(t=>[t,t])].map(([k,l])=>`<button class="chip ${f===k?'on':''}" data-a="talkTopic" data-v="${esc(k)}">${esc(l)}</button>`).join('')}</div>
  <div class="stack">${list.map(t=>`<div class="card tp"><div class="row between nowrap"><a href="#talk-${t.id}" style="color:inherit;text-decoration:none"><strong>${esc(t.title)}</strong></a><button class="iconbtn" style="${S.talkStar[t.id]?'color:var(--warn)':''}" data-a="star" data-id="${t.id}" aria-label="Star">${icon('star')}</button></div><p class="small">${esc(t.fact)}</p><div class="say">${esc(t.say)}</div><div class="row between"><span class="chips">${t.pis.map(chipPI).join('')}</span><span class="src">${esc(t.source)}${t.asof?' · as of '+esc(t.asof):''}</span></div></div>`).join('')||'<div class="empty">No talking points match.</div>'}</div></div>`;
};

/* ================= PLAYBOOK ================= */
V.playbook=(sec)=>{
  const S2=(id,title,body,open)=>`<details class="card" id="pb-${id}" ${open||sec===id?'open':''}><summary>${title}</summary>${body}</details>`;
  if(sec==='exam' && !today().checklist){ today().checklist=1; save(); }
  return `<div class="wrap">${head('Playbook','The rules, the scoring, and the habits of teams that place. Rules come from the DECA Guide 2026-27 (Team Decision Making, pp. 53-54) and the 2026 FTDM district event.')}
  ${S2('format','Event format',`<div class="scrollx"><table class="tbl"><tbody>${[['Team','2 members of the same chapter. Both must take part in the presentation.'],['Exam','100-question Finance cluster exam each. The two scores are averaged into one team score.'],['Case','One case study in the first round; finalists get a second case.'],['Prep','30 minutes. Partners may consult only each other. Notes made during prep can be used while presenting.'],['Judge','Up to 15 minutes with a business executive judge, including questions.'],['PIs','5 performance indicators per case, listed in the participant instructions.'],['Weighting','The presentation counts twice the averaged exam score (presentation = 2/3 of the total). The exam score carries into finals.'],['Allowed','Four-function calculator during the exam and prep. Materials made during prep may be handed to the judge.'],['Not allowed','Printed reference materials, audio or visual aids, phones, tablets, scientific or graphing calculators.']].map(([k,v])=>`<tr><td><strong>${k}</strong></td><td>${v}</td></tr>`).join('')}</tbody></table></div>`, true)}
  ${S2('rubric','How you are scored (100 points)',`<div class="stack-s small"><p><strong>Performance indicators</strong>: 5 × 10 = 50. Bands: Novice 0-3, Developing 4-6, Proficient 7-9, Exemplary 10.</p><p><strong>Solution</strong>: unique, practical, effective, 8 each = 24.</p><p><strong>Career competencies</strong>: critical thinking, communication, decision making, 6 each = 18.</p><p><strong>Overall impression</strong>: professionalism, poise, confidence = 8.</p>
    <div class="warn-note">The difference between Proficient and Exemplary: Proficient <em>explains</em> the PI and connects it to the case. Exemplary <em>strategically applies</em> it to comprehensively solve the client's problem with practical, real-world reasoning. So never just define a term: apply it to this client and prove it with a real example.</div></div>`)}
  ${S2('structure','The 15-minute structure',`<ol class="model small"><li><strong>0:00-1:00 Open.</strong> Handshake, names, thank the judge. One-sentence recommendation up front. Agenda: "Partner A will cover…, I'll cover…"</li><li><strong>1:00-9:00 The five PIs.</strong> About 90 seconds each: Explain → Apply → Prove. Alternate speakers every PI or two.</li><li><strong>9:00-11:00 Solution.</strong> What, why it's unique, how it works in practice (timeline, cost, who), and how you'll measure success.</li><li><strong>11:00-12:00 Close.</strong> Three takeaways, the benefit to the client, "What questions do you have for us?"</li><li><strong>12:00-15:00 Judge questions.</strong> Each partner answers at least one. Answer → Reason → Example → Tie back.</li></ol>`)}
  ${S2('prep','How to use 30 minutes of prep',`<ol class="model small"><li><strong>0-5 min, together:</strong> read the case twice. Circle the 5 PIs and every request in the "your team will discuss" list. Write the client's real goal in one line.</li><li><strong>5-8 min:</strong> agree on ONE recommendation. Split the PIs (A takes 1, 3, 5; B takes 2, 4). Decide who opens and who closes.</li><li><strong>8-20 min, separately:</strong> for each of your PIs write Explain / Apply / Prove on one note card, using a real fact or number.</li><li><strong>20-25 min:</strong> write the solution: unique twist, practical steps, timeline, metrics. Make one visual for the judge if it helps (a simple timeline or budget).</li><li><strong>25-30 min:</strong> rehearse the opening, the handoffs and the close out loud. Guess the two judge questions and assign them.</li></ol>`)}
  ${S2('phrases','Phrase bank',`<div class="stack-s small"><p><mark>Open</mark> "Thank you for meeting with us. We know you're worried about X, so today we'll show you a plan to Y."</p><p><mark>Explain a PI</mark> "Simply put, [term] means… For your family, that matters because…"</p><p><mark>Prove it</mark> "For example, …" / "According to the FDIC, …" / "A real case of this was …"</p><p><mark>Hand off</mark> "That protects what you have. Now [partner] will show you how to grow it."</p><p><mark>Unique</mark> "What most advisors won't tell you is…" / "Our twist is…"</p><p><mark>Practical</mark> "Here's exactly what happens in the first 30, 60 and 90 days."</p><p><mark>Effective</mark> "You'll know it's working when [metric] reaches [target] by [date]."</p><p><mark>Judge question you can't fully answer</mark> "Great question. What we do know is… and we'd confirm the details by…" Never invent a number.</p><p><mark>Close</mark> "To recap: protect, grow, review. What questions can we answer for you?"</p></div>`)}
  ${S2('partner','Partner choreography',`<ul class="model small"><li>Stand or sit so you can both see the judge and each other. Look at the judge, not your partner, while speaking.</li><li>Speak in turns of 60-120 seconds. Long monologues hurt the communication score.</li><li>The silent partner nods, hands over materials, and is ready to add one sentence if the speaker blanks.</li><li>Agree on a signal ("To add to that…") for jumping in politely.</li><li>Both of you must answer at least one judge question.</li></ul>`)}
  ${S2('past','What recent FTDM district cases asked',`<div class="stack-s small"><p><strong>2026:</strong> financial advisors meet new parents nervous about the future. PIs: responsibilities of finance professionals in client service, need to save and invest, types of investments, types of financial markets, insurance needs. Judge asked how often to examine accounts and how to use credit cards responsibly.</p><p><strong>2025:</strong> small business advisors help a talented tailor start a business with a friend. PIs: entrepreneurship, types of business ownership, role of finance in business, need for financial information, insurance needs, budgets, overhead costs.</p><p><strong>2024:</strong> bank marketing and customer service managers design a flyer on money markets and CDs. PIs: need to save and invest, financial markets, role of financial institutions, time value of money, interpreting policies, informational writing.</p><div class="blue-note">Pattern: advising a person or small business in plain language, heavy on personal finance. That's why the client-advising cases and the talking points matter so much.</div></div>`)}
  ${S2('charts','Charts and visuals',`<p class="small">You can't bring visual aids, but you can hand the judge anything you create during prep. A quick hand-drawn timeline, budget pie or risk matrix makes your solution look planned and practical.</p><a class="btn sm" href="#charts">Open Charts that win judges</a>`)}
  ${S2('exam','Exam strategy and exam-day plan',`<ul class="model small"><li><strong>Pace:</strong> 100 questions. Do a first pass answering everything you know, flag the rest, come back. Never leave a blank: there's no penalty for guessing.</li><li><strong>Read all four options.</strong> Many questions ask for the "best" or "most likely" answer; two options can be partly true.</li><li><strong>Eliminate</strong> extremes ("always", "never", "guaranteed") and options that are true but don't answer the question.</li><li><strong>Watch the stem's keywords:</strong> NOT, EXCEPT, first, primary, main.</li><li><strong>Calculations:</strong> write the formula, plug in, sanity-check the size of the answer. Four-function calculator only.</li><li><strong>Change an answer</strong> only when you find a clear reason, not a hunch.</li><li><strong>Night before:</strong> light flashcard review only, sleep 8+ hours. <strong>Morning:</strong> real breakfast, 10 warm-up cards, arrive early, charged device if testing online.</li></ul>`)}
  </div>`;
};

/* ================= TEAM ================= */
V.team=()=>{
  const me=CL.uid; const ids=Object.keys(CL.team); const ordered=[me,...ids.filter(i=>i!==me)].filter(i=>i&&CL.team[i]);
  const mine=CLOUD.teamSummary();
  const card=(id,s,isMe)=>`<div class="card stack-s"><div class="row">${avatarOf(id)?`<img class="avatar" style="width:36px;height:36px" src="${esc(avatarOf(id))}" alt="">`:''}<div class="min0"><strong>${esc(isMe?'You':nameOf(id))}</strong><br><span class="tiny faint">${isMe?'Updated live':'Active '+ago(s.updated)}${onlinePeers().some(p=>p.by===id)?' · <span class="dot on"></span> online now':''}</span></div></div>
    <div class="grid3" style="grid-template-columns:repeat(3,1fr)"><div class="cd"><span class="label">Today</span><span class="num" style="font-size:1.3rem">${s.planDone??0}/${s.planTotal??0}</span></div><div class="cd"><span class="label">Streak</span><span class="num" style="font-size:1.3rem">${s.streak||0}</span></div><div class="cd"><span class="label">Projected</span><span class="num" style="font-size:1.3rem">${s.projected??'·'}</span></div></div>
    <div class="small muted">${s.answered||0} questions · ${s.cardsMastered||0} cards mastered · ${s.lessonsDone||0}/15 lessons · ${s.casesDone||0} cases${s.caseAvg!=null?` (avg ${s.caseAvg})`:''}</div>
    ${s.mocks?.length?`<div class="small">Mocks: ${s.mocks.map(m=>`<span class="mono">${m.s}</span>`).join(' → ')}</div>`:''}
    ${s.weak?.length?`<div class="small">Needs work: ${s.weak.map(a=>`<span class="chip warn">${esc(areaShort(a))}</span>`).join(' ')}</div>`:''}</div>`;
  if(!CL.db) return `<div class="wrap">${head('Team','Study as a team of two. FTDM averages both partners\' exam scores, so your partner\'s weak areas are your weak areas.')}
    ${card('me',mine,true)}
    <div class="card stack"><h2>Connect with your partner</h2><ol class="model small"><li>Open this app's share menu on claude.ai and invite your partner by email as an <strong>Editor</strong> (on a Team or Enterprise plan, Contributor works too). Don't turn on a public link: on personal plans, invited editors can only save while the link is off.</li><li>Your partner opens the same link while signed in to Claude. You'll each see the other's progress here, a shared prep planner on every case, a team board, and timers that start on both screens.</li></ol>
    <p class="small muted">Live sync isn't available in this view, so here is a manual fallback: copy your progress code and send it to your partner, and paste theirs below.</p>
    <div class="row"><button class="btn" data-a="copyCode">${icon('copy')}Copy my progress code</button></div>
    <textarea class="input" id="partner-code" rows="3" placeholder="Paste your partner's code here">${esc(S.notes.partnerCode?.text||'')}</textarea><button class="btn" data-a="loadCode">Show partner progress</button>
    ${(()=>{ try{ const p=S.notes.partnerCode?.text?JSON.parse(decodeURIComponent(escape(atob(S.notes.partnerCode.text.trim())))):null; return p?card('p',p,false).replace('Partner',esc(p.name||'Partner')):''; }catch(e){ return '<p class="small" style="color:var(--bad)">That code didn\'t work. Ask your partner to copy it again.</p>'; } })()}</div></div>`;
  const ro=CL.writeBlocked;
  return `<div class="wrap">${head('Team','Your progress and your partner\'s, live. FTDM averages both exam scores, so cover each other\'s weak areas.')}
  ${ro?`<div class="warn-note small">You can view the team, but this account can't save shared data. Ask the person who shared the app to invite you as an Editor (and keep public link sharing off).</div>`:''}
  <div class="grid2">${ordered.length?ordered.map(id=>card(id,id===me?mine:CL.team[id],id===me)).join(''):card(me,mine,true)}</div>
  ${ordered.length<2?`<div class="blue-note small">Waiting for your partner. Invite them from the share menu as an Editor; they'll appear here after they open the app.</div>`:''}
  <div class="card stack"><h2>Team board</h2>
    <div class="row nowrap"><input class="input" id="board-text" placeholder="Leave a note: 'I'll take PIs 2 and 4 tonight'" maxlength="400"><button class="btn primary" data-a="postBoard" ${ro?'disabled':''}>Post</button></div>
    <div class="row"><button class="btn sm" data-a="challenge" ${ro?'disabled':''}>Send a 10-question challenge</button>${onlinePeers().length?`<button class="btn sm" data-a="nudge">Nudge partner</button>`:''}</div>
    <div class="stack">${CL.board.map(b=>`<div class="board-msg">${avatarOf(b.by)?`<img class="avatar" src="${esc(avatarOf(b.by))}" alt="">`:'<span class="avatar"></span>'}<div class="min0"><span class="small"><strong>${esc(nameOf(b.by))}</strong> <span class="faint tiny">${ago(b.t)}</span></span><br>${b.kind==='challenge'?`<span>Sent a challenge: ${(b.ids||[]).length} questions. </span>${b.by!==me?`<a href="#quiz-ids.${(b.ids||[]).join(',')}" data-a="takeChallenge" data-id="${b.id}">Take it</a>`:''}`:b.kind==='result'?`<span>Scored <strong>${esc(b.score)}</strong> on a challenge</span>`:`<span>${esc(b.text)}</span>`}${b.by===me&&!ro?` <button class="btn ghost sm" data-a="delBoard" data-id="${b.id}">Delete</button>`:''}</div></div>`).join('')||'<p class="small muted">No posts yet.</p>'}</div></div>
  <div class="card stack-s"><h2>Practice together</h2><p class="small muted">Open any case together: the planner is shared, and starting the prep or presentation timer starts it on your partner's screen. For a full mock roleplay, have someone use Judge mode on a third device.</p><a class="btn" href="#roleplay">Pick a case</a></div></div>`;
};

/* ================= SETTINGS ================= */
V.prefs=()=>`<div class="wrap">${head('Settings')}
  <div class="card stack"><div class="grid2"><label class="field">Cluster exam date<input class="input" type="date" value="${S.settings.examDate}" data-in="set" data-k="examDate"></label><label class="field">Regionals date<input class="input" type="date" value="${S.settings.regionalsDate}" data-in="set" data-k="regionalsDate"></label>
  <label class="field">Theme<select class="input" data-in="set" data-k="theme">${['system','light','dark'].map(t=>`<option ${S.settings.theme===t?'selected':''}>${t}</option>`).join('')}</select></label>
  <label class="field">Blueprint for projections and mocks<select class="input" data-in="set" data-k="blueprint"><option value="district" ${S.settings.blueprint==='district'?'selected':''}>District</option><option value="association" ${S.settings.blueprint==='association'?'selected':''}>Association / state</option></select></label>
  <label class="field">New flashcards per day (0 = automatic)<input class="input" type="number" min="0" max="60" value="${S.settings.newPerDay||0}" data-in="set" data-k="newPerDay"></label>
  ${CL.tts?`<label class="field">Judge voice<select class="input" data-in="set" data-k="voice">${['buttery','airy','glassy','rounded'].map(v=>`<option ${S.settings.voice===v?'selected':''}>${v}</option>`).join('')}</select></label>`:''}</div>
  <p class="tiny faint">Regionals defaults to January 6, 2027. Change it to your exact date.</p></div>
  <div class="card stack"><h2>Backup</h2><p class="small muted">${CL.db&&CL.uid&&!CL.writeBlocked?'Your progress syncs to your Claude account automatically, so it follows you to any device where you open this app.':'Progress is saved in this browser. Copy a backup now and then.'}</p>
  <div class="row"><button class="btn" data-a="copyBackup">${icon('copy')}Copy backup</button></div><textarea class="input" id="restore" rows="3" placeholder="Paste a backup here to restore or merge it"></textarea><button class="btn" data-a="restore">Merge backup</button></div>
  <div class="card stack"><h2>About the content</h2><p class="small muted">${D.questions.length} original exam questions, ${D.cards.length} flashcards, ${D.lessons.length} lessons, ${D.cases.cases.length} cases, ${D.cases.drills.length} drills and ${D.talk.length} sourced talking points. Blueprint from the DECA Guide 2026-27, p. 39. Questions are written for this app; none are copied from DECA or MBA Research. Not affiliated with DECA Inc.</p>
  <button class="btn ghost danger" data-a="reset">Reset all my progress</button></div></div>`;

/* ================= AI prompts ================= */
function aiBox(id,title,text){ const el=document.getElementById(id); if(el) el.innerHTML=`<div class="ai"><h4>${esc(title)}</h4>${esc(text)}</div>`; }
async function runAI(boxId,title,prompt,tier){ aiBox(boxId,title,'Thinking…'); try{ await askClaude(prompt,t=>aiBox(boxId,title,t),{tier}); }catch(e){ aiBox(boxId,title,e?.code==='not_granted'?'Claude isn\'t turned on for this page. Allow it from the page\'s permissions to use AI feedback.':e?.code==='rate_limited'?'Too many requests right now. Try again in a minute.':'Claude couldn\'t answer just now. Try again later.'); } }
const AI_ROLE='You are a DECA Financial Services Team Decision Making (FTDM) coach for a high school team. Be specific, encouraging and honest. Use plain language and short paragraphs. Do not invent statistics; if you mention a number, it must be well established, and say where it comes from.';

/* ================= RENDER ================= */
let lastRoute='';
function render(){
  const r=route(); const key=r.name+'-'+(r.arg||''); const fn=V[r.name]||V.today;
  if(r.name!=='case') PREPSYNC.stop();
  if(r.name==='quiz' && UI.quiz && UI.quiz.spec!==r.arg) UI.quiz=null;
  if(r.name==='cards' && UI.cardSession && UI.cardSession.deck!==(r.arg||UI.cardSession.deck)) UI.cardSession=null;
  $('#main').innerHTML=fn(r.arg);
  if(key!==lastRoute){ window.scrollTo(0,0); lastRoute=key; setPresence(); }
  renderChrome(); TIMER.paint();
}
function rerender(){ const a=document.activeElement; if(a&&$('#main').contains(a)&&(a.tagName==='TEXTAREA'||(a.tagName==='INPUT'&&a.type!=='range'&&a.type!=='checkbox'))){ UI.pending=true; return; } render(); }
document.addEventListener('focusout',()=>{ if(UI.pending){ UI.pending=false; setTimeout(()=>{ const a=document.activeElement; if(!(a&&(a.tagName==='TEXTAREA'||a.tagName==='INPUT'))) render(); else UI.pending=true; },50); } });
function applyTheme(){ const t=S.settings.theme; if(t==='light'||t==='dark') document.documentElement.setAttribute('data-theme',t); else document.documentElement.removeAttribute('data-theme'); }

/* ================= ACTIONS ================= */
const A = {
  flip(){ const cs=UI.cardSession; if(!cs) return; cs.flipped=!cs.flipped; const f=$('.flash'); if(f) f.classList.toggle('flipped',cs.flipped); const ctl=$('#card-ctrl'); const c=CARD[cs.queue[0]]; if(ctl&&c) ctl.innerHTML=cardCtrl(c); },
  rate(el){ const cs=UI.cardSession; const id=cs.queue.shift(); const g=+el.dataset.g; rateCard(id,g); if(CARD[id].lesson==='facts') bump('factCards'); cs.done++; if(g===0){ cs.again++; cs.queue.splice(Math.min(cs.queue.length,4),0,id); } cs.flipped=false; save(); render(); },
  startCards(el){ const deck=el.dataset.deck, mode=el.dataset.mode; const list=deckCards(deck); let q;
    if(mode==='cram') q=pick(list,20).map(c=>c.id); else { const due=dueCards(list).map(c=>c.id); const nw=newCardsIn(list); const quota=deck==='all'?Math.max(0,newPerDay()-(today().newCards||0)):20; q=[...due,...(deck==='facts'?nw:nw).slice(0,quota).map(c=>c.id)].slice(0,80); if(!q.length) q=pick(list,15).map(c=>c.id); }
    UI.cardSession={deck,queue:q,done:0,again:0,flipped:false}; location.hash='#cards'+(deck&&deck!=='all'?'-'+deck:''); render(); },
  endCards(){ UI.cardSession=null; render(); },
  answer(el){ const Z=UI.quiz; const q=QBY[Z.items[Z.i]]; if(Z.ans[q.id]) return; const o=+el.dataset.o; const ok=o===0; Z.ans[q.id]={pick:o,ok,prevW:!!S.qs[q.id]?.w}; recordAnswer(q.id,ok); bump('qs'); if(Z.mode==='smart') bump('smart'); save(); render(); },
  guessed(){ const Z=UI.quiz; const id=Z.items[Z.i]; recordAnswer(id,true,{guess:true}); S.qs[id].n--; S.qs[id].c--; save(); toast('It will come back tomorrow'); },
  nextQ(){ UI.quiz.i++; render(); if(UI.quiz.i>=UI.quiz.items.length && UI.challengeId && CL.db && !CL.writeBlocked){ const Z=UI.quiz; const c=Z.items.filter(id=>Z.ans[id]?.ok).length; CL.db.collection('board').add({kind:'result',by:CL.uid,t:Date.now(),ref:UI.challengeId,score:`${c}/${Z.items.length}`}).catch(()=>{}); UI.challengeId=null; } },
  quitQuiz(){ UI.quiz.closed=true; history.back(); },
  againQuiz(){ const s=UI.quiz.spec; UI.quiz=null; startQuiz(s); render(); },
  lessonDone(el){ today().lesson=el.dataset.id; save(); },
  markLesson(el){ S.lessons[el.dataset.id]=Date.now(); today().lesson=el.dataset.id; save(); toast('Lesson marked as read'); render(); },
  saveTeach(el){ const id=el.dataset.id; S.notes['teach-'+id]={text:$('#teach-'+id).value,last:Date.now()}; save(); toast('Saved'); },
  aiTeach(el){ const id=el.dataset.id; const L=LESSON[id]; const txt=$('#teach-'+id).value.trim(); if(!txt){ toast('Write your explanation first'); return; } S.notes['teach-'+id]={text:txt,last:Date.now()}; save();
    runAI('teach-out','Coach feedback',`${AI_ROLE}\n\nA student wrote this plain-language explanation of an idea from the lesson "${L.title}" as if speaking to an FTDM judge playing a client.\n\nLesson key ideas for reference:\n${L.cards.map(c=>'- '+CARD[c].t+': '+CARD[c].d).join('\n')}\n\nStudent explanation:\n"""${txt}"""\n\nGive: 1) whether it's accurate (fix anything wrong), 2) one way to make it clearer for a client, 3) one real-world example or fact they could add, 4) a polished 2-3 sentence version in their voice. Under 200 words.`,'quick'); },
  aiExplain(el){ const q=QBY[el.dataset.q]; runAI('ai-explain','Another way to see it',`${AI_ROLE}\n\nExplain this exam question to a high school student in a different way than the given explanation, with a memorable everyday example and a quick trick to recognize similar questions. Under 130 words.\n\nQuestion: ${q.q}\nCorrect answer: ${q.o[0]}\nOther options: ${q.o.slice(1).join(' | ')}\nGiven explanation: ${q.e}`,'quick'); },
  startMock(){ const items=mockSet(S.settings.blueprint).map(q=>q.id); const mins=S.settings.mockMinutes; UI.mock={t:Date.now(),items,i:0,answers:{},flags:{},seed:Date.now()%100000,bp:S.settings.blueprint,endsAt:mins?Date.now()+mins*60000:0}; saveMock(); render(); },
  mockPick(el){ const M=UI.mock; M.answers[M.items[M.i]]=+el.dataset.o; saveMock(); render(); },
  mockNav(el){ const M=UI.mock; const d=+el.dataset.d; if(M.i===99&&d>0){ UI.mockGrid=true; render(); return; } M.i=clamp(M.i+d,0,99); saveMock(); render(); },
  mockJump(el){ UI.mock.i=+el.dataset.i; saveMock(); render(); },
  mockFlag(){ const M=UI.mock; const id=M.items[M.i]; M.flags[id]=!M.flags[id]; saveMock(); render(); },
  submitMock(el){ const M=UI.mock; const un=100-Object.keys(M.answers).length; if(un>0 && !el.dataset.sure){ el.dataset.sure='1'; el.textContent=`${un} unanswered. Tap again to submit`; return; } const rec=gradeMock(); location.hash='#review-'+rec.t; },
  abandonMock(el){ if(!el.dataset.sure){ el.dataset.sure='1'; el.textContent='Tap again to quit (nothing saved)'; return; } UI.mock=null; try{localStorage.removeItem('ftdm-ace-mock')}catch(e){} location.hash='#exam'; },
  revFilter(el){ UI.revFilter=el.dataset.v; render(); },
  setQuizTitle(el){ UI.quizTitle=el.dataset.v; },
  piTier(el){ UI.pitier=el.dataset.v; render(); },
  caseFilter(el){ UI.caseFilter=el.dataset.v; render(); },
  caseStep(el){ UI.caseStep=UI.caseStep||{}; UI.caseStep[el.dataset.id]=el.dataset.v; if(route().name!=='case'||route().arg!==el.dataset.id) location.hash='#case-'+el.dataset.id; else render(); },
  toggleHalf(){ UI.half=!UI.half; render(); },
  timer(el){ const k=el.dataset.k, cid=el.dataset.id, s=+el.dataset.s; if(TIMER.endsAt&&TIMER.kind===k){ TIMER.stopLocal(); LIVE.stop(); return; } TIMER.startLocal(k,cid,s); LIVE.start(k,cid,s); if(k==='present'){ today().caseSim=1; save(); } },
  setOwner(el){ const cur=prepGet(el.dataset.id,el.dataset.k); prepSet(el.dataset.id,el.dataset.k,cur===el.dataset.v?'':el.dataset.v); render(); },
  showQs(el){ UI.showQs=UI.showQs||{}; UI.showQs[el.dataset.id]=!UI.showQs[el.dataset.id]; render(); },
  speakQs(el){ const c=caseById(el.dataset.id); speak(c.questions.map((q,i)=>`Question ${i+1}. ${q}`).join(' ')); },
  speakCase(el){ const c=caseById(el.dataset.id); speak(`You are ${c.role}. ${c.situation}`); },
  speakText(el){ speak(el.dataset.t); },
  saveRun(el){ const cid=el.dataset.id; const r=UI.rub?.[cid]||{}; const total=RUBRIC.reduce((s,x)=>s+(r[x.k]??0),0); S.caseRuns.push({t:Date.now(),caseId:cid,scores:{...r},total,half:!!UI.half}); today().caseSim=1; save(); CLOUD.pushTeam(); toast(`Saved: ${total}/100`); },
  aiJudge(el){ const c=caseById(el.dataset.id); const tr=(S.notes['transcript-'+c.id]?.text||'').trim(); const notes=PREP_KEYS(c).map(k=>prepGet(c.id,k)?`${k}: ${prepGet(c.id,k)}`:'').filter(Boolean).join('\n');
    if(!tr&&!notes){ toast('Add a transcript or planner notes first'); return; }
    const box='ai-judge'; aiBox(box,'AI judge','Scoring…');
    CL.sample.json(`${AI_ROLE}\n\nAct as a strict but fair FTDM judge. Score this team's presentation using the official 2026 FTDM evaluation form.\n\nCASE: The team plays ${c.role}. The judge is the ${c.judge}.\n${c.situation}\nTasks: ${c.tasks.join('; ')}\nPerformance indicators: ${c.pis.map((p,i)=>`PI${i+1} ${p} ${PI[p]?.pi}`).join('; ')}\n\nTEAM'S PLANNER NOTES:\n${notes||'(none)'}\n\nTRANSCRIPT OR SUMMARY OF WHAT THEY SAID:\n${tr||'(none, judge from the notes)'}\n\nRubric: pi1-pi5 0-10 each (Novice 0-3, Developing 4-6, Proficient 7-9, Exemplary 10: exemplary means strategically applied to solve the client's problem with real-world reasoning). unique, practical, effective 0-8 each. critical, communication, decision 0-6 each. overall 0-8.\n\nReply with only JSON like {"scores":{"pi1":7,"pi2":6,"pi3":8,"pi4":5,"pi5":7,"unique":5,"practical":6,"effective":6,"critical":4,"communication":4,"decision":4,"overall":5},"strengths":["..."],"improve":["specific fix 1","specific fix 2","specific fix 3"],"realWorld":"one real-world fact or example they should add, with its source"}`,{modelTier:'default',cache:false})
      .then(j=>{ const sc=j&&j.scores||{}; UI.rub=UI.rub||{}; const r=UI.rub[c.id]={}; RUBRIC.forEach(x=>{ const v=Number(sc[x.k]); if(!isNaN(v)) r[x.k]=clamp(Math.round(v),0,x.max); }); render();
        const total=RUBRIC.reduce((s,x)=>s+(r[x.k]??0),0); aiBox(box,`AI judge: ${total}/100 (sliders updated)`,`Strengths:\n• ${(j.strengths||[]).join('\n• ')}\n\nTo score higher:\n• ${(j.improve||[]).join('\n• ')}\n\nAdd this: ${j.realWorld||''}`); })
      .catch(e=>aiBox(box,'AI judge',e?.code==='not_granted'?'Claude isn\'t turned on for this page.':'The AI judge couldn\'t score this run. Try again.')); },
  genCase(el){ el.disabled=true; el.textContent='Writing a case…';
    const piList=D.pis.filter(p=>p.tier===2||['FI:270','FI:077','FI:571','FI:569','FI:831','FI:065','FI:066','FI:071','FI:568','FI:062','FI:579','FI:106','FI:091','FI:093','FI:094','FI:354','BL:003','EN:039','OP:024','EI:128','FI:073','FI:572','SM:075'].includes(p.code)).map(p=>p.code+' '+p.pi).join('\n');
    const seen=allCases().map(c=>c.judge).join('; ');
    CL.sample.json(`${AI_ROLE}\n\nWrite ONE new, original practice case in the style of recent DECA FTDM district events: the team plays advisors (financial advisors, small business advisors, bank or credit union managers, etc.) meeting ONE client or executive (the judge). Make the client situation realistic for ${new Date().getFullYear()} with specific numbers. Avoid these already-used judges: ${seen}.\n\nChoose exactly 5 PIs from this list (use the codes exactly):\n${piList}\n\nReply with only JSON: {"title":"short title","area":"Financial Analysis","role":"financial advisors","judge":"description of the client (judge)","situation":"4-6 sentences","tasks":["what the team will discuss", "..."],"pis":["FI:270","..."],"questions":["judge question 1","judge question 2"],"model":["8-10 bullet points of a strong answer, each tying a PI to this client with a real-world fact; last two start with 'Judge Q1:' and 'Judge Q2:'"]}`,{modelTier:'default',cache:false})
      .then(j=>{ if(!j||!j.situation||!Array.isArray(j.pis)) throw {code:'bad'}; const pis=j.pis.filter(p=>PI[p]).slice(0,5); const c={id:'ai-'+uid(),title:String(j.title||'AI case').slice(0,80),area:j.area||'Financial Analysis',role:String(j.role||'financial advisors'),judge:String(j.judge||'client'),situation:String(j.situation),tasks:(j.tasks||[]).map(String).slice(0,6),pis,questions:(j.questions||[]).map(String).slice(0,2),model:(j.model||[]).map(String).slice(0,12),style:'ai',t:Date.now(),by:CL.uid||''};
        S.gen=[c,...(S.gen||[])].slice(0,30); save(); if(CL.db&&!CL.writeBlocked) CL.db.doc('gen/'+c.id).set(c).catch(()=>{}); location.hash='#case-'+c.id; })
      .catch(()=>{ toast('Couldn\'t generate a case. Try again.'); el.disabled=false; el.innerHTML=icon('spark')+'Generate a case'; }); },
  openDrill(el){ UI.drill={id:el.dataset.id,stage:'ready',ans:''}; render(); },
  randomDrill(){ const ds=D.cases.drills; const runs={}; (S.drillRuns||[]).forEach(r=>runs[r.id]=r); const fresh=ds.filter(d=>!runs[d.id]); const d=pick(fresh.length?fresh:ds,1)[0]; UI.drill={id:d.id,stage:'ready',ans:''}; render(); },
  drillGo(){ UI.drill.stage='prep'; TIMER.startLocal('drillPrep',null,60); render(); },
  drillSkip(){ UI.drill.stage='speak'; TIMER.startLocal('drillSpeak',null,60); render(); },
  drillDone(){ TIMER.stopLocal(true); UI.drill.stage='review'; render(); },
  rateDrill(el){ const d=UI.drill; d.rating=+el.dataset.v; if(!d.logged){ d.logged=true; bump('drills'); d.runT=Date.now(); S.drillRuns.push({t:d.runT,id:d.id,rating:d.rating}); } else { const r=S.drillRuns.find(x=>x.t===d.runT); if(r) r.rating=d.rating; } save(); render(); },
  aiDrill(){ const d=UI.drill; const dr=DRILL[d.id]; const ans=($('#drill-ans')?.value||'').trim(); if(!ans){ toast('Type or dictate your answer first'); return; }
    runAI('ai-drill','Coach feedback',`${AI_ROLE}\n\nRoleplay prompt: ${dr.scenario}\nPIs: ${dr.pis.map(p=>p+' '+PI[p]?.pi).join('; ')}\nModel answer: ${dr.model}\n\nStudent's answer:\n"""${ans}"""\n\nGive: a score out of 10, what was strong, the single most important fix, one real-world fact or example they could add (with source), and a tighter 3-sentence version in their voice. Under 170 words.`,'quick'); },
  nextDrill(){ if(UI.drill&&!UI.drill.logged){ bump('drills'); save(); } A.randomDrill(); },
  endDrill(){ TIMER.stopLocal(true); UI.drill=null; render(); },
  jqGo(){ const all=allJudgeQs(); const it=all[UI.jq.i%all.length]; UI.jq.stage='speak'; if(CL.tts) speak(it.q).then(()=>{ if(UI.jq.stage==='speak'){ TIMER.startLocal('judgeQ',null,45); } }); else TIMER.startLocal('judgeQ',null,45); render(); },
  jqDone(){ TIMER.stopLocal(true); UI.jq.stage='review'; bump('judgeQs'); save(); render(); },
  jqNext(){ const all=allJudgeQs(); UI.jq={i:Math.floor(Math.random()*all.length),stage:'ready'}; render(); },
  talkTopic(el){ UI.talkTopic=el.dataset.v; render(); },
  talkFilterPI(el){ UI.talkPI=el.dataset.pi||null; UI.talkTopic='all'; if(route().name!=='talk') location.hash='#talk'; else render(); },
  star(el){ const id=el.dataset.id; if(S.talkStar[id]) delete S.talkStar[id]; else S.talkStar[id]=Date.now(); save(); render(); },
  copy(el){ const t=el.dataset.t; navigator.clipboard?.writeText(t).then(()=>toast('Copied'),()=>toast('Select the text to copy it')); },
  postBoard(){ const i=$('#board-text'); const v=i.value.trim(); if(!v) return; CL.db.collection('board').add({kind:'note',by:CL.uid,t:Date.now(),text:v.slice(0,400)}).then(()=>{ i.value=''; render(); }).catch(e=>{ if(e?.code==='invalid_argument'){ CL.writeBlocked=true; render(); } toast('Couldn\'t post. Check sharing permissions.'); }); },
  delBoard(el){ CL.db.doc('board/'+el.dataset.id).delete().catch(()=>{}); },
  challenge(){ const missed=D.questions.filter(q=>S.qs[q.id]?.w).map(q=>q.id); const ids=[...shuffle(missed).slice(0,5),...smartSet(10).map(q=>q.id)].filter((v,i,a)=>a.indexOf(v)===i).slice(0,10);
    CL.db.collection('board').add({kind:'challenge',by:CL.uid,t:Date.now(),ids}).then(()=>toast('Challenge sent')).catch(()=>toast('Couldn\'t send the challenge')); },
  takeChallenge(el){ UI.challengeId=el.dataset.id; UI.quizTitle='Partner challenge'; },
  nudge(){ CL.room?.emit('ping',{text:'Time to study! Today\'s plan is waiting.'}).then(()=>toast('Nudge sent')).catch(()=>{}); },
  copyCode(){ const s={...CLOUD.teamSummary(),name:CL.me?.name||''}; const code=btoa(unescape(encodeURIComponent(JSON.stringify(s)))); navigator.clipboard?.writeText(code).then(()=>toast('Code copied. Send it to your partner.'),()=>{ $('#partner-code').value=code; toast('Copy the code from the box'); }); },
  loadCode(){ S.notes.partnerCode={text:$('#partner-code').value.trim(),last:Date.now()}; save(); render(); },
  copyBackup(){ const s=btoa(unescape(encodeURIComponent(JSON.stringify(S)))); navigator.clipboard?.writeText(s).then(()=>toast('Backup copied'),()=>{ $('#restore').value=s; toast('Copy the backup from the box'); }); },
  restore(){ try{ const b=JSON.parse(decodeURIComponent(escape(atob($('#restore').value.trim())))); S=mergeState(S,b); save(); toast('Backup merged'); render(); }catch(e){ toast('That backup is not valid'); } },
  reset(el){ if(!el.dataset.sure){ el.dataset.sure='1'; el.textContent='Tap again to erase everything'; return; } const keep=S.settings; S=blankState(); S.settings=keep; save(); toast('Progress reset'); location.hash='#today'; render(); },
  mic(el){ if(!CL.dict) return; const target=el.dataset.target; if(DICT.target===target&&CL.dict.active()){ CL.dict.stop().catch(()=>{}); return; } DICT.target=target; CL.dict.start().catch(e=>{ if(e?.code==='not_granted') toast('Microphone permission was declined'); }); },
};
const DICT={target:null,init(){ if(!CL.dict) return; CL.dict.onFinal(({text})=>{ const el=document.getElementById(DICT.target); if(el){ el.value=(el.value?el.value.trim()+' ':'')+text; el.dispatchEvent(new Event('input',{bubbles:true})); } const p=document.getElementById('partial-'+DICT.target); if(p) p.textContent=''; });
  CL.dict.onPartial(({text})=>{ const p=document.getElementById('partial-'+DICT.target); if(p) p.textContent=text; });
  CL.dict.onState(({state})=>{ $$('.mic').forEach(b=>b.classList.toggle('on',state==='listening'&&b.dataset.target===DICT.target)); }); }};

/* inputs */
const IN = {
  piq(el){ UI.piq=el.value; clearTimeout(UI.piqT); UI.piqT=setTimeout(()=>{ render(); const i=$('[data-in="piq"]'); if(i){ i.focus(); i.setSelectionRange(i.value.length,i.value.length);} },250); },
  talkq(el){ UI.talkq=el.value; clearTimeout(UI.tqT); UI.tqT=setTimeout(()=>{ render(); const i=$('[data-in="talkq"]'); if(i){ i.focus(); i.setSelectionRange(i.value.length,i.value.length);} },250); },
  deck(el){ location.hash='#cards'+(el.value==='all'?'':'-'+el.value); },
  reverse(el){ UI.reverse=el.checked; },
  bp(el){ S.settings.blueprint=el.value; S.settings.t=Date.now(); save(); render(); },
  mockMin(el){ S.settings.mockMinutes=+el.value; S.settings.t=Date.now(); save(); },
  prep(el){ prepSet(el.dataset.id,el.dataset.k,el.value); },
  note(el){ S.notes[el.dataset.k]={text:el.value,last:Date.now()}; clearTimeout(UI.noteT); UI.noteT=setTimeout(()=>save(),600); },
  drillAns(el){ if(UI.drill) UI.drill.ans=el.value; },
  rub(el){ UI.rub=UI.rub||{}; const r=UI.rub[el.dataset.id]=UI.rub[el.dataset.id]||{}; r[el.dataset.k]=+el.value; const tot=RUBRIC.reduce((s,x)=>s+(r[x.k]??0),0); const t=$('#rub-total'); if(t) t.innerHTML=`${tot}<small class="faint" style="font-size:1rem">/100</small>`; const b=$('#band-'+el.dataset.k); if(b){ const v=+el.value/+el.dataset.max; b.textContent=(v>=.95?'Exemplary':v>=.7?'Proficient':v>=.4?'Developing':'Novice')+' · '+el.value+'/'+el.dataset.max; } },
  set(el){ const k=el.dataset.k; S.settings[k]= el.type==='number'?+el.value:el.value; S.settings.t=Date.now(); const t=today(); delete t.cardsNeed; save(); if(k==='theme') applyTheme(); },
};

/* ================= BOOT ================= */
document.addEventListener('click',e=>{ const el=e.target.closest('[data-a]'); if(!el) return; const fn=A[el.dataset.a]; if(!fn) return; if(el.tagName==='A'&&!el.getAttribute('href')?.startsWith('#')) return; if(el.tagName!=='A') e.preventDefault(); fn(el,e); });
document.addEventListener('input',e=>{ const el=e.target.closest('[data-in]'); if(el&&IN[el.dataset.in]) IN[el.dataset.in](el,e); });
document.addEventListener('keydown',e=>{
  const tag=(e.target.tagName||''); if(tag==='INPUT'||tag==='TEXTAREA'||tag==='SELECT') return; const r=route();
  if(r.name==='cards'&&UI.cardSession&&!UI.cardSession.finished){ if(e.key===' '||e.key==='Enter'){ e.preventDefault(); A.flip(); } else if(UI.cardSession.flipped&&'1234'.includes(e.key)){ A.rate({dataset:{g:String(+e.key-1)}}); } }
  else if(r.name==='quiz'&&UI.quiz){ const Z=UI.quiz; if(Z.i>=Z.items.length) return; const q=QBY[Z.items[Z.i]]; const k=e.key.toLowerCase(); const idx='1234'.indexOf(k)>=0?'1234'.indexOf(k):'abcd'.indexOf(k);
    if(!Z.ans[q.id]&&idx>=0){ A.answer({dataset:{o:String(optOrder(q.id,Z.seed)[idx])}}); } else if(Z.ans[q.id]&&(e.key==='Enter'||e.key==='ArrowRight')){ A.nextQ(); } }
  else if(r.name==='mock'&&UI.mock&&!UI.mock.submitted){ const M=UI.mock; const q=QBY[M.items[M.i]]; const k=e.key.toLowerCase(); const idx='1234'.indexOf(k)>=0?'1234'.indexOf(k):'abcd'.indexOf(k);
    if(idx>=0){ A.mockPick({dataset:{o:String(optOrder(q.id,M.seed)[idx])}}); } else if(e.key==='ArrowRight'){ A.mockNav({dataset:{d:'1'}}); } else if(e.key==='ArrowLeft'){ A.mockNav({dataset:{d:'-1'}}); } }
});
window.addEventListener('hashchange',render);
setInterval(()=>{ const t=$('#mock-timer'); if(t&&UI.mock&&UI.mock.endsAt){ const l=(UI.mock.endsAt-Date.now())/1000; t.textContent=fmtTime(l); t.classList.toggle('low',l<300); if(l<=0&&!UI.mock.submitted){ toast('Time is up. Your exam was submitted.'); const rec=gradeMock(); location.hash='#review-'+rec.t; } } },500);
document.addEventListener('visibilitychange',()=>{ if(!document.hidden && TIMER.endsAt) keepAwake(true); });

