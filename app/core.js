/* FTDM Ace core: data, state, spaced repetition, analytics, plan, routing, cloud sync. */
'use strict';
const D = JSON.parse(document.getElementById('ftdm-data').textContent);

/* ---------- constants ---------- */
// DECA Guide 2026-27, p. 39: Finance cluster exam blueprint (items per 100).
const BLUEPRINT = {
  district:    {'Business Law':7,'Communications':5,'Customer Relations':5,'Economics':6,'Emotional Intelligence':9,'Entrepreneurship':1,'Financial Analysis':24,'Financial-Information Management':9,'Human Resources Management':1,'Information Management':6,'Marketing':1,'Operations':6,'Professional Development':13,'Risk Management':6,'Strategic Management':1},
  association: {'Business Law':8,'Communications':4,'Customer Relations':5,'Economics':5,'Emotional Intelligence':8,'Entrepreneurship':0,'Financial Analysis':28,'Financial-Information Management':10,'Human Resources Management':0,'Information Management':5,'Marketing':1,'Operations':5,'Professional Development':14,'Risk Management':7,'Strategic Management':0},
};
const AREAS = Object.keys(BLUEPRINT.district).sort((a,b)=>BLUEPRINT.district[b]-BLUEPRINT.district[a]);
const AREA_SHORT = {'Financial Analysis':'Fin. Analysis','Financial-Information Management':'Fin.-Info Mgmt','Professional Development':'Prof. Dev.','Emotional Intelligence':'Emotional Intel.','Human Resources Management':'HR Mgmt','Information Management':'Info. Mgmt','Customer Relations':'Customer Rel.','Strategic Management':'Strategic Mgmt'};
const LESSON_ORDER = ['statements','money-tvm','institutions','economy-securities','careers-clients','governance','ei','law','fim-core','fim-analysis','risk','managerial','data','econ-ops','comm-pd'];
const RUBRIC = [
  {k:'pi1',label:'PI 1',max:10,grp:'Performance indicators'},{k:'pi2',label:'PI 2',max:10,grp:'Performance indicators'},{k:'pi3',label:'PI 3',max:10,grp:'Performance indicators'},{k:'pi4',label:'PI 4',max:10,grp:'Performance indicators'},{k:'pi5',label:'PI 5',max:10,grp:'Performance indicators'},
  {k:'unique',label:'Unique: original thinking, fresh perspective',max:8,grp:'Solution'},{k:'practical',label:'Practical: actionable in the real world',max:8,grp:'Solution'},{k:'effective',label:'Effective: achieves relevant outcomes',max:8,grp:'Solution'},
  {k:'critical',label:'Critical thinking',max:6,grp:'Career competencies'},{k:'communication',label:'Communication',max:6,grp:'Career competencies'},{k:'decision',label:'Decision making',max:6,grp:'Career competencies'},
  {k:'overall',label:'Overall impression: professionalism, poise, confidence',max:8,grp:'Overall'},
];
const DAY = 86400000;

/* ---------- indexes ---------- */
const PI = Object.fromEntries(D.pis.map(p=>[p.code,{...p,area:p.area==='Communication Skills'?'Communications':p.area}]));
const QBY = Object.fromEntries(D.questions.map(q=>[q.id,q]));
const CARD = Object.fromEntries(D.cards.map(c=>[c.id,c]));
const LESSON = Object.fromEntries(D.lessons.map(l=>[l.id,l]));
const TALK = Object.fromEntries(D.talk.map(t=>[t.id,t]));
const QS_BY_AREA = {}; D.questions.forEach(q=>{(QS_BY_AREA[q.area]=QS_BY_AREA[q.area]||[]).push(q)});
const QS_BY_LESSON = {}; D.questions.forEach(q=>{(QS_BY_LESSON[q.lesson]=QS_BY_LESSON[q.lesson]||[]).push(q)});
// Talking points also study as flashcards ("facts" deck).
const FACTCARDS = D.talk.map(t=>({id:'f-'+t.id,lesson:'facts',t:t.title,d:t.fact,x:t.say,src:t.source,tid:t.id}));
FACTCARDS.forEach(c=>CARD[c.id]=c);
// Finance Hub: topics -> sub-topics. Each sub-topic's judge questions also study as flashcards ("jq" deck).
const HUB = D.hub||[]; const HUBT={}, HUBSUB={}; const HUB_ORDER=[];
HUB.forEach(tp=>{ HUBT[tp.id]=tp; tp.subs.forEach(s=>{ s.topic=tp.id; HUBSUB[s.id]=s; HUB_ORDER.push(s.id); }); });
const TALK_BY_SUB={}; D.talk.forEach(t=>(t.subs||[]).forEach(id=>(TALK_BY_SUB[id]=TALK_BY_SUB[id]||[]).push(t)));
const JQCARDS=[]; HUB.forEach(tp=>tp.subs.forEach(s=>s.qs.forEach((q,i)=>JQCARDS.push({id:`j-${s.id}-${i}`,lesson:'jq',t:q.q,d:q.a,x:'',src:s.title,sub:s.id}))));
JQCARDS.forEach(c=>CARD[c.id]=c);
function allCases(){ return [...(S.gen||[]), ...(CL.gen||[]).filter(g=>!(S.gen||[]).some(x=>x.id===g.id)), ...D.cases.cases]; }
function caseById(id){ return allCases().find(c=>c.id===id); }
const DRILL = Object.fromEntries(D.cases.drills.map(d=>[d.id,d]));
// How many of the past DECA Finance exams (2018-2026) tested each PI. Used to weight practice and mocks.
const HITS=(D.hits&&D.hits.pis)||{}; const NEXAMS=(D.hits&&D.hits.meta&&D.hits.meta.exams)||0;
function piHits(c){ return (HITS[c]||[0])[0]; }
function hitW(q){ return 1+piHits(q.pi)/6; }
// Random order that favors questions on frequently tested PIs (weighted shuffle).
function weightedOrder(arr){ return arr.map(x=>[Math.pow(Math.random(),1/hitW(x)),x]).sort((a,b)=>b[0]-a[0]).map(p=>p[1]); }

/* ---------- utils ---------- */
const $ = (s,el=document)=>el.querySelector(s);
const $$ = (s,el=document)=>[...el.querySelectorAll(s)];
const esc = s => String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
const pct=(a,b)=>b?Math.round(100*a/b):0;
function dayKey(d=new Date()){ const x=new Date(d); return x.getFullYear()+'-'+String(x.getMonth()+1).padStart(2,'0')+'-'+String(x.getDate()).padStart(2,'0'); }
function startOfDay(ms=Date.now()){ const d=new Date(ms); d.setHours(0,0,0,0); return d.getTime(); }
function parseDay(s){ const [y,m,d]=s.split('-').map(Number); return new Date(y,m-1,d).getTime(); }
function daysUntil(s){ return Math.round((parseDay(s)-startOfDay())/DAY); }
function fmtDate(s,opt={month:'short',day:'numeric'}){ return new Date(parseDay(s)).toLocaleDateString(undefined,opt); }
function fmtTime(sec){ sec=Math.max(0,Math.round(sec)); const m=Math.floor(sec/60), s=sec%60; return m+':'+String(s).padStart(2,'0'); }
function ago(ms){ if(!ms) return 'never'; const s=(Date.now()-ms)/1000; if(s<60) return 'just now'; if(s<3600) return Math.floor(s/60)+'m ago'; if(s<86400) return Math.floor(s/3600)+'h ago'; return Math.floor(s/86400)+'d ago'; }
function shuffle(a,seed){ a=[...a]; let r=seed??Math.random()*1e9; const rnd=()=>{r=(r*9301+49297)%233280;return r/233280}; for(let i=a.length-1;i>0;i--){const j=Math.floor((seed==null?Math.random():rnd())*(i+1));[a[i],a[j]]=[a[j],a[i]]} return a; }
function pick(a,n){ return shuffle(a).slice(0,n); }
function hashStr(s){ let h=0; for(const c of s) h=(h*31+c.charCodeAt(0))|0; return Math.abs(h); }
function uid(){ return Date.now().toString(36)+Math.random().toString(36).slice(2,8); }
function toast(msg){ const t=document.createElement('div'); t.className='toast'; t.setAttribute('role','status'); t.textContent=msg; document.body.appendChild(t); setTimeout(()=>t.remove(),2600); }
function areaShort(a){ return AREA_SHORT[a]||a; }

/* ---------- state ---------- */
const KEY='ftdm-ace-v1';
function blankState(){ return {v:1,created:Date.now(),cards:{},qs:{},lessons:{},daily:{},quizzes:[],mocks:[],caseRuns:[],drillRuns:[],notes:{},talkStar:{},gen:[],hubRead:{},
  settings:{t:0,examDate:'2026-12-07',regionalsDate:'2027-01-06',theme:'system',mockMinutes:60,blueprint:'district',newPerDay:0,voice:'buttery'}}; }
let S = (()=>{ try{ const raw=localStorage.getItem(KEY); if(raw){ const s=JSON.parse(raw); const b=blankState(); return {...b,...s,settings:{...b.settings,...(s.settings||{})}}; } }catch(e){} return blankState(); })();
let saveT=null;
function save(opts={}){ S.updated=Date.now(); try{ localStorage.setItem(KEY,JSON.stringify(S)); }catch(e){} if(!opts.local) CLOUD.queue(); }
function today(){ const k=dayKey(); return (S.daily[k]=S.daily[k]||{}); }
function bump(kind,n=1){ const t=today(); t[kind]=(t[kind]||0)+n; t.at=Date.now(); }

/* ---------- flashcards: SM-2 style scheduling ---------- */
function cardState(id){ return S.cards[id]; }
function rateCard(id, g){ // g: 0 again, 1 hard, 2 good, 3 easy
  const now=Date.now(); const p=S.cards[id]||{e:2.5,i:0,n:0,l:0};
  let {e,i,n,l}=p; const isNew=!S.cards[id];
  if(g===0){ l++; n=0; i=0; e=Math.max(1.3,e-0.2); }
  else { if(g===1){ i=isNew||i<1?1:Math.max(1,Math.round(i*1.2)); e=Math.max(1.3,e-0.15); }
    else if(g===2){ i=isNew||i<1?1:(i<3?3:Math.round(i*e)); }
    else { i=isNew||i<1?3:Math.round(Math.max(i,1)*e*1.3); e+=0.15; }
    n++; }
  i=Math.min(i,60);
  const due = g===0 ? now+10*60000 : startOfDay(now)+i*DAY+3600000*4;
  S.cards[id]={e:+e.toFixed(2),i,n,l,due,last:now};
  bump('cards'); if(isNew) bump('newCards');
}
function cardPreview(id,g){ const p=S.cards[id]; const isNew=!p; let i=p?.i||0, e=p?.e||2.5;
  if(g===0) return '10m'; if(g===1) i=isNew||i<1?1:Math.max(1,Math.round(i*1.2)); else if(g===2) i=isNew||i<1?1:(i<3?3:Math.round(i*e)); else i=isNew||i<1?3:Math.round(Math.max(i,1)*e*1.3);
  i=Math.min(i,60); return i+'d'; }
function deckCards(deck){ if(deck==='facts') return FACTCARDS; if(deck==='jq') return JQCARDS; if(deck==='all'||!deck) return D.cards; return D.cards.filter(c=>c.lesson===deck); }
function dueCards(list){ const now=Date.now(); return list.filter(c=>S.cards[c.id]&&S.cards[c.id].due<=now).sort((a,b)=>S.cards[a.id].due-S.cards[b.id].due); }
function newCardsIn(list){ return list.filter(c=>!S.cards[c.id]); }
function newPerDay(){ if(S.settings.newPerDay) return S.settings.newPerDay; const left=newCardsIn(D.cards).length; const d=daysUntil(S.settings.examDate); return d>2? clamp(Math.ceil(left/Math.max(1,d-2)),8,30) : 10; }
function cardCounts(list=D.cards){ let nw=0,lr=0,ms=0; list.forEach(c=>{const s=S.cards[c.id]; if(!s) nw++; else if(s.i>=7) ms++; else lr++;}); return {nw,lr,ms,total:list.length}; }

/* ---------- questions: results + review scheduling ---------- */
function recordAnswer(qid, correct, opts={}){
  const now=Date.now(); const p=S.qs[qid]||{n:0,c:0,s:0};
  p.n++; if(correct){p.c++; p.s=(p.s||0)+1;} else p.s=0;
  p.w = correct?0:1; p.last=now;
  const ladder=[1,3,7,14,30];
  p.due = correct ? startOfDay(now)+ladder[Math.min(p.s-1,4)]*DAY : now; // missed questions come straight back in review
  if(opts.guess){ p.due=startOfDay(now)+DAY; p.g=1; } else if(correct) p.g=0;
  S.qs[qid]=p;
}
function qAcc(q){ const r=S.qs[q.id]; return r? r.c/r.n : null; }
function areaStats(area){ const qs=QS_BY_AREA[area]||[]; let n=0,c=0,seen=0; qs.forEach(q=>{const r=S.qs[q.id]; if(r){n+=r.n;c+=r.c;seen++;}});
  const est=(c+1.2)/(n+2); return {n,c,seen,pool:qs.length,acc:n?c/n:null,est}; }
function piStats(code){ let n=0,c=0; D.questions.forEach(q=>{ if(q.pi===code){const r=S.qs[q.id]; if(r){n+=r.n;c+=r.c;}} }); return {n,c,acc:n?c/n:null}; }
function answeredCount(){ return Object.keys(S.qs).length; }
function projected(bp=S.settings.blueprint){ const w=BLUEPRINT[bp]; let tot=0; for(const a in w){ tot+=w[a]*areaStats(a).est; } return Math.round(tot); }
function status(acc,n){ if(!n) return ['Not started','']; if(acc>=.8) return ['Strong','good']; if(acc>=.65) return ['Getting there','warn']; return ['Weak','bad']; }
function weakAreas(k=3){ return AREAS.filter(a=>BLUEPRINT.district[a]>=3).map(a=>({a,st:areaStats(a)})).sort((x,y)=>(x.st.est-y.st.est)*1 - 0.004*(BLUEPRINT.district[x.a]-BLUEPRINT.district[y.a])).slice(0,k).map(x=>x.a); }
function weakPIs(k=8){ const m={}; D.questions.forEach(q=>{const r=S.qs[q.id]; if(!r) return; const x=m[q.pi]=m[q.pi]||{n:0,c:0}; x.n+=r.n; x.c+=r.c;});
  return Object.entries(m).filter(([,x])=>x.n>=2).map(([pi,x])=>({pi,acc:x.c/x.n,n:x.n})).sort((a,b)=>a.acc-b.acc).slice(0,k); }

// Smart practice: missed and due first, then weak areas weighted by blueprint, then unseen questions.
function smartSet(n, opts={}){
  const now=Date.now(); const pool=opts.pool||D.questions; const chosen=new Set(); const out=[];
  const add=q=>{ if(out.length<n && !chosen.has(q.id)){chosen.add(q.id); out.push(q);} };
  shuffle(pool.filter(q=>{const r=S.qs[q.id]; return r && r.w && r.due<=now;})).slice(0,Math.ceil(n*.35)).forEach(add);
  shuffle(pool.filter(q=>{const r=S.qs[q.id]; return r && !r.w && r.due<=now;})).slice(0,Math.ceil(n*.2)).forEach(add);
  const bp=BLUEPRINT[S.settings.blueprint]; const weights={};
  AREAS.forEach(a=>{ const st=areaStats(a); weights[a]=(bp[a]||0.5)*(1.25-st.est); });
  let guard=0;
  while(out.length<n && guard++<500){
    const tot=Object.values(weights).reduce((s,x)=>s+x,0); let r=Math.random()*tot, area=AREAS[0];
    for(const a of AREAS){ r-=weights[a]; if(r<=0){area=a;break;} }
    const cands=(QS_BY_AREA[area]||[]).filter(q=>pool.includes(q)&&!chosen.has(q.id));
    if(!cands.length){ weights[area]=0; if(Object.values(weights).every(x=>!x)) break; continue; }
    const unseen=cands.filter(q=>!S.qs[q.id]); add(weightedOrder(unseen.length&&Math.random()<.7?unseen:cands)[0]);
  }
  shuffle(pool).forEach(add);
  return shuffle(out);
}
function mockSet(bp=S.settings.blueprint){
  const w=BLUEPRINT[bp]; const usedInMocks=new Set((S.mocks||[]).slice(-3).flatMap(m=>(m.items||[]).map(x=>x.q)));
  let out=[];
  AREAS.forEach(a=>{ const need=w[a]||0; if(!need) return; const pool=QS_BY_AREA[a]||[];
    const fresh=weightedOrder(pool.filter(q=>!usedInMocks.has(q.id))); const old=weightedOrder(pool.filter(q=>usedInMocks.has(q.id)));
    out.push(...[...fresh,...old].slice(0,need)); });
  if(out.length<100){ const have=new Set(out.map(q=>q.id)); out.push(...shuffle((QS_BY_AREA['Financial Analysis']||[]).filter(q=>!have.has(q.id))).slice(0,100-out.length)); }
  return shuffle(out).slice(0,100);
}

/* ---------- plan for today ---------- */
function mockDay(d){ return [16,9,5,2].includes(d); }
function phase(){ const d=daysUntil(S.settings.examDate), r=daysUntil(S.settings.regionalsDate);
  if(d>0) return {id:'exam',d,r,name:'Exam sprint',sub:`${d} day${d===1?'':'s'} to the cluster exam`};
  if(d===0) return {id:'examday',d,r,name:'Exam day',sub:'Warm up, then go get it'};
  if(r>0) return {id:'roleplay',d,r,name:'Roleplay season',sub:`${r} day${r===1?'':'s'} to regionals`};
  if(r===0) return {id:'compday',d,r,name:'Competition day',sub:'Trust the reps'};
  return {id:'state',d,r,name:'Next round',sub:'Keep the roleplay reps going'}; }
function nextLesson(){ return LESSON_ORDER.find(id=>!S.lessons[id]) || null; }
function weakestLesson(){ let best=null,bv=2; LESSON_ORDER.forEach(id=>{ const qs=QS_BY_LESSON[id]||[]; let n=0,c=0; qs.forEach(q=>{const r=S.qs[q.id]; if(r){n+=r.n;c+=r.c}}); const v=(c+1)/(n+2); if(v<bv){bv=v;best=id;} }); return best; }
function todaysFact(){ const k=dayKey(); return D.talk[hashStr(k)%D.talk.length]; }
// Today's Hub sub-topic: the one picked today (so it stays put after you read it), else the first unread one,
// with sub-topics whose PIs you're weakest on first.
function nextHubSub(){ const t=today(); if(t.hubSub&&HUBSUB[t.hubSub]) return HUBSUB[t.hubSub];
  const unread=HUB_ORDER.filter(id=>!(S.hubRead||{})[id]); if(!unread.length) return null;
  const acc=id=>{ let n=0,c=0; HUBSUB[id].pis.forEach(p=>{ const st=piStats(p); n+=st.n; c+=st.c; }); return n?c/n:0.7; };
  const pick=unread.slice().sort((a,b)=>acc(a)-acc(b)||HUB_ORDER.indexOf(a)-HUB_ORDER.indexOf(b))[0];
  t.hubSub=pick; return HUBSUB[pick]; }
function buildPlan(){
  const P=phase(), t=today(), steps=[];
  const cardsNeed = t.cardsNeed || (t.cardsNeed = clamp(dueCards(D.cards).length + newPerDay(), 10, 60));
  const C=(k)=>t[k]||0;
  if(P.id==='exam'){
    steps.push({id:'cards',title:`Review ${cardsNeed} flashcards`,sub:'Spaced repetition: due cards first, then new ones',route:'#cards',have:Math.min(C('cards'),cardsNeed),need:cardsNeed});
    const nl=nextLesson(), lid=nl||weakestLesson();
    steps.push({id:'lesson',title:nl?`Lesson: ${LESSON[lid].title}`:`Re-study: ${LESSON[lid].title}`,sub:nl?`${LESSON[lid].cards.length} key ideas, then a 5-question check`:'Your weakest lesson by quiz accuracy',route:'#lesson-'+lid,done:!!t.lesson});
    steps.push({id:'smart',title:'Answer 20 smart-practice questions',sub:'Missed questions + weak areas, weighted to the blueprint',route:'#quiz-smart',have:Math.min(C('smart'),20),need:20});
    if(mockDay(P.d)) steps.push({id:'mock',title:'Take a full 100-question mock exam',sub:`Timed ${S.settings.mockMinutes} min, weighted to the ${S.settings.blueprint} blueprint`,route:'#mock',done:!!t.mock});
    else steps.push({id:'drill',title:'One 60-second speaking drill',sub:'Keeps roleplay skills warm while you cram',route:'#drills',have:Math.min(C('drills'),1),need:1});
    { const hs=nextHubSub(); if(hs) steps.push({id:'hub',title:'Finance Hub: '+hs.title,sub:'Read it, then answer one of its judge questions out loud',route:'#hub-'+hs.id,done:!!t.hub}); }
    steps.push({id:'fact',title:'Learn today\'s real-world fact',sub:todaysFact().title,route:'#talk-'+todaysFact().id,done:!!t.fact});
  } else if(P.id==='examday'){
    steps.push({id:'checklist',title:'Read the exam-day game plan',sub:'Pacing, elimination, what to do when stuck',route:'#playbook-exam',done:!!t.checklist});
    steps.push({id:'cards',title:'Warm up with 10 flashcards',sub:'Light review only, no new material',route:'#cards',have:Math.min(C('cards'),10),need:10});
  } else {
    const full = (hashStr(dayKey())%2===0);
    steps.push({id:'case',title: full?'Full case: 30-min prep + 15-min presentation':'Half case: 10-min prep + 7-min pitch',sub:'Do it with your partner if you can, then score it with the official rubric',route:'#roleplay',done:!!t.caseSim});
    steps.push({id:'drill',title:'Two 60-second speaking drills',sub:'Answer out loud, then compare to the model',route:'#drills',have:Math.min(C('drills'),2),need:2});
    steps.push({id:'judge',title:'Answer 3 judge questions out loud',sub:'45 seconds each',route:'#judge',have:Math.min(C('judgeQs'),3),need:3});
    { const hs=nextHubSub(); if(hs) steps.push({id:'hub',title:'Finance Hub: '+hs.title,sub:'Read it, then answer one of its judge questions out loud',route:'#hub-'+hs.id,done:!!t.hub}); }
    steps.push({id:'facts',title:'Study 8 real-world fact cards',sub:'Numbers and examples that make judges remember you',route:'#cards-facts',have:Math.min(C('factCards'),8),need:8});
    steps.push({id:'smart',title:'Answer 10 mixed questions',sub:'Keeps PI knowledge sharp for the roleplay',route:'#quiz-smart10',have:Math.min(C('smart'),10),need:10});
    if(!full) steps.push({id:'sketch',title:'Sketch one chart in 3 minutes',sub:'A visual you could hand the judge',route:'#sketch',done:!!t.sketch});
  }
  steps.forEach(s=>{ if(s.need!=null) s.done = s.have>=s.need; });
  const done=steps.filter(s=>s.done).length;
  if(done===steps.length && !t.planDone){ t.planDone=Date.now(); save(); setTimeout(()=>celebrate(),200); }
  return {P,steps,done};
}
function streak(){ let n=0; let d=startOfDay(); if(!S.daily[dayKey(d)]?.planDone) d-=DAY; while(S.daily[dayKey(d)]?.planDone){ n++; d-=DAY; } return n; }
function activityLevel(k){ const t=S.daily[k]; if(!t) return 0; const v=(t.cards||0)/10+(t.qs||0)/10+(t.drills||0)+(t.mock?3:0)+(t.caseSim?3:0)+(t.lesson?1:0); return v<=0?0:v<2?1:v<5?2:3; }

/* ---------- celebration ---------- */
function celebrate(){ if(matchMedia('(prefers-reduced-motion: reduce)').matches){ toast('Today\'s plan is done. Streak +1'); return; }
  const c=document.createElement('canvas'); c.className='confetti'; c.width=innerWidth; c.height=innerHeight; document.body.appendChild(c); const x=c.getContext('2d');
  const cs=getComputedStyle(document.documentElement); const cols=[cs.getPropertyValue('--accent'),cs.getPropertyValue('--hl'),cs.getPropertyValue('--info'),cs.getPropertyValue('--warn')].map(s=>s.trim()||'#0b7a55');
  const ps=Array.from({length:110},()=>({x:innerWidth/2,y:innerHeight*.35,vx:(Math.random()-.5)*12,vy:-Math.random()*11-3,r:Math.random()*6+3,c:cols[Math.floor(Math.random()*4)],a:Math.random()*6}));
  let f=0; (function tick(){ x.clearRect(0,0,c.width,c.height); ps.forEach(p=>{p.x+=p.vx;p.y+=p.vy;p.vy+=.32;p.a+=.15;x.fillStyle=p.c;x.save();x.translate(p.x,p.y);x.rotate(p.a);x.fillRect(-p.r/2,-p.r/2,p.r,p.r*.6);x.restore();}); if(++f<120) requestAnimationFrame(tick); else c.remove(); })();
  toast('Today\'s plan is done. Streak +1'); }

/* ---------- sound + wake lock for timers ---------- */
let AC=null; function beep(freq=880,dur=.18,times=1){ try{ AC=AC||new (window.AudioContext||window.webkitAudioContext)(); for(let i=0;i<times;i++){ const o=AC.createOscillator(),g=AC.createGain(); o.frequency.value=freq; o.connect(g); g.connect(AC.destination); const t0=AC.currentTime+i*(dur+.08); g.gain.setValueAtTime(.0001,t0); g.gain.exponentialRampToValueAtTime(.25,t0+.01); g.gain.exponentialRampToValueAtTime(.0001,t0+dur); o.start(t0); o.stop(t0+dur+.02);} }catch(e){} }
let wakeLock=null; async function keepAwake(on){ try{ if(on&&!wakeLock&&navigator.wakeLock) wakeLock=await navigator.wakeLock.request('screen'); else if(!on&&wakeLock){ await wakeLock.release(); wakeLock=null; } }catch(e){ wakeLock=null; } }

/* ---------- cloud: private sync across devices, team summary, shared prep, live presence, AI ---------- */
const CL = {ready:false,db:null,user:null,room:null,sample:null,tts:null,dict:null,uid:null,me:null,canWrite:null,writeBlocked:false,team:{},board:[],gen:[],peers:[],names:{},status:'local'};
function mergeState(a,b){ // merge remote b into local a without losing anything
  const out={...a};
  const byLast=(x={},y={})=>{ const o={...x}; for(const k in y){ if(!o[k] || (y[k].last||0)>(o[k].last||0)) o[k]=y[k]; } return o; };
  out.cards=byLast(a.cards,b.cards); out.qs=byLast(a.qs,b.qs);
  out.lessons={...b.lessons,...a.lessons};
  out.daily={...a.daily}; for(const k in (b.daily||{})){ const x=out.daily[k]||{}, y=b.daily[k]; const m={...x}; for(const f in y){ if(typeof y[f]==='number') m[f]=Math.max(x[f]||0,y[f]); else if(y[f]&&!x[f]) m[f]=y[f]; } out.daily[k]=m; }
  const uni=(x=[],y=[],key='t')=>{ const seen=new Set(x.map(i=>i[key])); return [...x,...y.filter(i=>!seen.has(i[key]))].sort((p,q)=>(p.t||0)-(q.t||0)); };
  out.quizzes=uni(a.quizzes,b.quizzes).slice(-150); out.mocks=uni(a.mocks,b.mocks).slice(-30); out.caseRuns=uni(a.caseRuns,b.caseRuns).slice(-120); out.drillRuns=uni(a.drillRuns,b.drillRuns).slice(-300);
  out.gen=uni(a.gen,b.gen,'id');
  out.notes=byLast(a.notes,b.notes);
  out.talkStar={...b.talkStar,...a.talkStar};
  out.hubRead={...(b.hubRead||{}),...(a.hubRead||{})};
  out.settings=((b.settings?.t||0)>(a.settings?.t||0))?{...a.settings,...b.settings}:a.settings;
  return out; }
function withTimeout(p,ms){ return Promise.race([p,new Promise(r=>setTimeout(()=>r(null),ms))]); }
const CLOUD = {
  writing:false, pending:false, timer:null, teamTimer:null, lastTeam:'',
  queue(){ if(!CL.db||!CL.uid||CL.writeBlocked) return; clearTimeout(this.timer); this.timer=setTimeout(()=>this.flush(),3500); clearTimeout(this.teamTimer); this.teamTimer=setTimeout(()=>this.pushTeam(),8000); },
  async flush(){ if(this.writing){ this.pending=true; return; } this.writing=true;
    try{ await CL.db.doc('data/users/'+CL.uid+'/progress').set({state:JSON.stringify(S),updated:Date.now()}); CL.status='synced'; }
    catch(e){ if(e?.code==='invalid_argument'||e?.code==='not_granted'){ CL.writeBlocked=true; CL.status='readonly'; } else if(e?.code==='quota_exceeded'){ toast('Cloud storage is full. Progress is still saved on this device.'); } }
    this.writing=false; renderChrome(); if(this.pending){ this.pending=false; this.flush(); } },
  teamSummary(){ const P=buildPlanSilent(); const m=(S.mocks||[]).slice(-6).map(x=>({t:x.t,s:x.score}));
    const areas={}; AREAS.forEach(a=>{const st=areaStats(a); if(st.n) areas[a]=Math.round(100*st.acc);});
    const cr=(S.caseRuns||[]).filter(r=>r.total!=null); const cc=cardCounts();
    return {updated:Date.now(),streak:streak(),planDone:P.done,planTotal:P.total,projected:answeredCount()>=25?projected():null,answered:answeredCount(),mocks:m,areas,
      cardsMastered:cc.ms,cardsSeen:cc.ms+cc.lr,casesDone:cr.length,caseAvg:cr.length?Math.round(cr.reduce((s,r)=>s+r.total,0)/cr.length):null,
      weak:weakAreas(3),lessonsDone:Object.keys(S.lessons).length,drills:(S.drillRuns||[]).length}; },
  async pushTeam(){ if(!CL.db||!CL.uid||CL.writeBlocked) return; const s=this.teamSummary(); const sig=JSON.stringify({...s,updated:0}); if(sig===this.lastTeam) return; this.lastTeam=sig;
    try{ await CL.db.doc('team/'+CL.uid).set(s); }catch(e){} },
};
function buildPlanSilent(){ try{ const t=today(); const had=!!t.planDone; const p=buildPlan(); return {done:p.done,total:p.steps.length}; }catch(e){ return {done:0,total:0}; } }

async function initCloud(){
  if(!window.claude||typeof window.claude.use!=='function') { CL.status='local'; return; }
  const use=n=>withTimeout(window.claude.use(n).catch(()=>null),10000);
  const [user,db,room,sample,tts,dict]=await Promise.all([use('user'),use('db'),use('room'),use('sample'),use('tts'),use('dictation')]);
  Object.assign(CL,{user,db,room,sample,tts,dict});
  if(user){ try{ CL.uid=await user.id(); CL.me=await user.me(); }catch(e){} try{ const c=await user.can('data.write'); CL.canWrite=c; }catch(e){} }
  if(db && CL.uid){
    CL.status='syncing'; renderChrome();
    const ref=db.doc('data/users/'+CL.uid+'/progress');
    let loadTimer=setTimeout(()=>{ if(CL.status==='syncing'){ CL.status='offline'; renderChrome(); } },10000);
    ref.onSnapshot(snap=>{ clearTimeout(loadTimer); if(snap.metadata.hasPendingWrites) return;
      if(snap.exists){ try{ const remote=JSON.parse(snap.data().state); const before=JSON.stringify(S); S=mergeState(S,remote); const changed=JSON.stringify(S)!==before; save({local:true}); if(changed) rerender(); if(JSON.stringify(S)!==snap.data().state) CLOUD.queue(); }catch(e){} }
      else CLOUD.queue();
      CL.status='synced'; renderChrome(); }, err=>{ clearTimeout(loadTimer); CL.status='offline'; renderChrome(); });
    db.collection('team').onSnapshot(qs=>{ CL.team={}; qs.docs.forEach(d=>{ if(d.exists) CL.team[d.id]=d.data(); }); resolveNames(Object.keys(CL.team)); if(['team','today'].includes(route().name)) rerender(); renderChrome(); }, ()=>{});
    db.collection('board').orderBy('t','desc').limit(60).onSnapshot(qs=>{ CL.board=qs.docs.filter(d=>d.exists).map(d=>({id:d.id,...d.data()})); resolveNames(CL.board.map(b=>b.by)); if(route().name==='team') rerender(); }, ()=>{});
    db.collection('gen').orderBy('t','desc').limit(40).onSnapshot(qs=>{ CL.gen=qs.docs.filter(d=>d.exists).map(d=>({id:d.id,...d.data(),style:d.data().style||'ai'})); if(route().name==='roleplay') rerender(); }, ()=>{});
    setTimeout(()=>CLOUD.pushTeam(),1500);
  }
  if(room){
    try{ room.onPeers(ch=>{ CL.peers=ch.peers; resolveNames(CL.peers.map(p=>p.by).filter(Boolean)); renderChrome(); if(route().name==='team') rerender(); }, ()=>{});
      room.on('timer', msg=>{ if(msg.isMe&&msg.sameTab) return; LIVE.onRemote(msg); }, ()=>{});
      room.on('ping', msg=>{ if(msg.isMe) return; const n=CL.names[msg.by]||'Your partner'; toast(`${n}: ${String(msg.data?.text||'').slice(0,80)}`); }, ()=>{});
      setPresence(); }catch(e){}
  }
  CL.ready=true; renderChrome(); rerender();
}
async function resolveNames(ids){ if(!CL.user||!ids.length) return; try{ const ps=await CL.user.profiles(ids); let changed=false; for(const id in ps){ const p=ps[id]; const v={name:p.name||'',avatar:p.avatarUrl,color:p.color,isMe:p.isMe}; if(JSON.stringify(CL.names[id])!==JSON.stringify(v)){ CL.names[id]=v; changed=true; } } if(changed){ renderChrome(); if(['team'].includes(route().name)) rerender(); } }catch(e){} }
function nameOf(id){ const n=CL.names[id]; if(!n) return id===CL.uid?'You':'Partner'; if(n.isMe||id===CL.uid) return 'You'; return n.name||'Partner'; }
function avatarOf(id){ const n=CL.names[id]; return n&&n.avatar?n.avatar:''; }
function setPresence(){ if(!CL.room) return; try{ CL.room.presence({view:route().name,at:Date.now()}); }catch(e){} }
function partnerIds(){ return Object.keys(CL.team).filter(id=>id!==CL.uid); }
function onlinePeers(){ return (CL.peers||[]).filter(p=>!p.isMe&&p.by&&p.kind==='viewer'); }

/* Live shared timer between partners (room events; nothing persists). */
const LIVE = {
  remote:null,
  start(kind,caseId,seconds){ if(!CL.room) return; CL.room.emit('timer',{kind:'start',timer:kind,caseId,seconds,startedAt:Date.now()}).catch(()=>{}); },
  stop(){ if(!CL.room) return; CL.room.emit('timer',{kind:'stop'}).catch(()=>{}); },
  onRemote(msg){ const d=msg.data||{}; if(d.kind==='start'){ const who=CL.names[msg.by]?.name||'Your partner'; TIMER.startLocal(d.timer,d.caseId,d.seconds,true); toast(`${who} started the ${d.timer==='prep'?'prep':'presentation'} timer`); if(route().name!=='case'||route().arg!==d.caseId) location.hash='#case-'+d.caseId; } else if(d.kind==='stop'){ TIMER.stopLocal(true); } },
};

/* ---------- AI helpers (Claude via the sample capability) ---------- */
async function askClaude(prompt, onText, opts={}){
  if(!CL.sample) throw {code:'unavailable'};
  const r=await CL.sample(prompt,{onText:onText?({text})=>onText(text):undefined,modelTier:opts.tier||'default',cache:false});
  return r.text;
}
async function speak(text){ if(!CL.tts) return false; try{ await CL.tts.speak(String(text).slice(0,1990),{voice:S.settings.voice||'buttery'}); return true; }catch(e){ return false; } }
function stopSpeak(){ try{ CL.tts&&CL.tts.stop(); }catch(e){} }

/* ---------- routing ---------- */
function route(){ const h=(location.hash||'#today').slice(1); const i=h.indexOf('-'); if(i<0) return {name:h||'today',arg:null}; return {name:h.slice(0,i),arg:h.slice(i+1)}; }
