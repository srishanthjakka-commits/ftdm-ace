/* Views part 1: shell, Today, Learn, Flashcards, Practice, Mock exam, Progress. */
'use strict';
const V = {}; const UI = {reverse:false, caseStep:{}};
const IC = {
  today:'<path d="M3 10.5 12 3l9 7.5V21h-6v-6H9v6H3z"/>',
  learn:'<path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4zM20 4h-6a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h7z"/>',
  cards:'<rect x="3" y="6" width="14" height="14" rx="2"/><path d="M7 3h12a2 2 0 0 1 2 2v12"/>',
  exam:'<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>',
  roleplay:'<path d="M12 2a3 3 0 0 1 3 3v6a3 3 0 0 1-6 0V5a3 3 0 0 1 3-3z"/><path d="M19 10v1a7 7 0 0 1-14 0v-1M12 18v4M8 22h8"/>',
  team:'<circle cx="9" cy="8" r="3.5"/><path d="M2 21v-1a6 6 0 0 1 6-6h2a6 6 0 0 1 6 6v1"/><circle cx="17.5" cy="7" r="2.5"/><path d="M18 13.2a5 5 0 0 1 4 4.8v1"/>',
  progress:'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
  talk:'<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/>',
  hub:'<path d="M3 21h18M5 21v-9M9.5 21v-9M14.5 21v-9M19 21v-9M2 9.5 12 4l10 5.5z"/>',
  playbook:'<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 7h6M9 11h6M9 15h4"/>',
  prefs:'<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
  check:'<path d="M5 12l5 5L20 7"/>', flag:'<path d="M4 22V4M4 4h13l-2 4 2 4H4"/>', play:'<path d="M7 4v16l13-8z"/>', stop:'<rect x="6" y="6" width="12" height="12" rx="1"/>',
  star:'<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/>', vol:'<path d="M11 5 6 9H3v6h3l5 4zM15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/>',
  mic:'<path d="M12 2a3 3 0 0 1 3 3v6a3 3 0 0 1-6 0V5a3 3 0 0 1 3-3z"/><path d="M19 10v1a7 7 0 0 1-14 0v-1M12 18v4"/>', spark:'<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
  copy:'<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/>', back:'<path d="M15 18l-6-6 6-6"/>', shuffle:'<path d="M16 3h5v5M4 20 21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/>',
};
const icon=(n,cls='')=>`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="${cls}" aria-hidden="true">${IC[n]||''}</svg>`;
const NAV=[['today','Today'],['learn','Learn'],['cards','Cards'],['exam','Exam'],['roleplay','Roleplay'],['team','Team']];
const NAV2=[['hub','Finance Hub'],['talk','Talking points'],['playbook','Playbook'],['progress','Progress'],['prefs','Settings']];
const NAV_OF={lesson:'learn',pis:'learn',quiz:'exam',mock:'exam',review:'exam',case:'roleplay',drills:'roleplay',judge:'roleplay',judgemode:'roleplay',gen:'roleplay'};

function renderChrome(){
  const r=route(); const cur=NAV_OF[r.name]||r.name;
  const rail=$('#rail'); if(rail) rail.innerHTML = `<a class="brand" href="#today"><span class="mark">FT</span>FTDM Ace</a>`+
    NAV.map(([k,l])=>`<a href="#${k}" class="${cur===k?'on':''}">${icon(k)}${l}</a>`).join('')+`<div class="grp label">More</div>`+
    NAV2.map(([k,l])=>`<a href="#${k}" class="${cur===k?'on':''}">${icon(k)}${l}</a>`).join('');
  const tabs=$('#tabs'); if(tabs) tabs.innerHTML = NAV.map(([k,l])=>`<a href="#${k}" class="tab ${cur===k?'on':''}" aria-label="${l}">${icon(k)}<span>${l}</span></a>`).join('');
  const tb=$('#topright'); if(tb){
    const on=onlinePeers(); const st={local:'Saved on this device',syncing:'Syncing…',synced:'Synced',offline:'Can\'t reach sync',readonly:'View-only: saved on this device'}[CL.status]||'';
    const av=on.slice(0,3).map(p=>avatarOf(p.by)?`<img class="avatar" alt="" src="${esc(avatarOf(p.by))}">`:'').join('');
    tb.innerHTML = `${on.length?`<a href="#team" class="chip good" title="Partner online"><span class="dot on"></span>${esc(on.length===1?(CL.names[on[0].by]?.name||'Partner'):on.length+' online')} studying</a>`:''}
      <span class="avatars">${av}</span><span class="tiny faint" title="Sync status">${esc(st)}</span>
      <a class="iconbtn" href="#hub" aria-label="Finance Hub">${icon('hub')}</a><a class="iconbtn" href="#talk" aria-label="Talking points">${icon('talk')}</a><a class="iconbtn" href="#progress" aria-label="Progress">${icon('progress')}</a><a class="iconbtn" href="#prefs" aria-label="Settings">${icon('prefs')}</a>`;
  }
}
function head(title,sub='',right=''){ return `<div class="pagehead"><div class="row nowrap between"><h1>${title}</h1>${right}</div>${sub?`<p class="muted">${sub}</p>`:''}</div>`; }
function chipPI(code){ const p=PI[code]; const has=typeof DEEP!=='undefined'&&DEEP[code]; const h=piHits(code); return `<span class="chip pi${has?' link':''}" title="${esc(p?p.pi:'')}${h?` · on ${h} of ${NEXAMS} past exams`:''}${has?' · open deep dive':''}"${has?` data-a="goPI" data-pi="${esc(code)}" role="link" tabindex="0"`:''}>${esc(code)}</span>`; }
function bar(v,cls=''){ return `<div class="bar ${cls}"><i style="width:${clamp(Math.round(v),0,100)}%"></i></div>`; }
function ring(p,label){ return `<div class="ring" style="--p:${clamp(p,0,100)}"><span>${label}</span></div>`; }
function back(href,label){ return `<a href="${href}" class="btn ghost sm" style="align-self:flex-start">${icon('back')}${esc(label)}</a>`; }
function spark(vals,max=100){ if(vals.length<2) return ''; const w=300,h=56,p=6; const xs=i=>p+i*(w-2*p)/(vals.length-1), ys=v=>h-p-(v/max)*(h-2*p);
  const d=vals.map((v,i)=>(i?'L':'M')+xs(i).toFixed(1)+' '+ys(v).toFixed(1)).join(' ');
  return `<svg class="spark" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" role="img" aria-label="Mock exam scores trend"><line x1="${p}" x2="${w-p}" y1="${ys(70)}" y2="${ys(70)}" stroke="var(--line)" stroke-dasharray="4 4"/><path d="${d} L${xs(vals.length-1)} ${h-p} L${p} ${h-p}Z" fill="var(--accent-soft)"/><path d="${d}" fill="none" stroke="var(--accent)" stroke-width="2.5"/><circle cx="${xs(vals.length-1)}" cy="${ys(vals[vals.length-1])}" r="4.5" fill="var(--accent)"/></svg>`; }

/* ================= TODAY ================= */
V.today=()=>{
  const {P,steps,done}=buildPlan(); const ex=daysUntil(S.settings.examDate), rg=daysUntil(S.settings.regionalsDate);
  const ans=answeredCount(); const proj=ans>=25?projected():null; const st=streak(); const f=todaysFact();
  const partner=partnerIds().map(id=>({id,...CL.team[id]}))[0];
  const hour=new Date().getHours(); const greet=hour<12?'Good morning':hour<18?'Good afternoon':'Good evening';
  return `<div class="wrap">
  <div class="pagehead"><span class="phase">${icon('flag')}${esc(P.name)} · ${esc(P.sub)}</span><h1>${greet}. Here's today's plan.</h1></div>
  <div class="hero">
    <div class="card stack">
      <div class="row between"><div class="countdown">
        <div class="cd"><span class="label">Cluster exam</span><span class="num">${ex>=0?ex:'Done'}${ex>=0?'<small>days</small>':''}</span><span class="tiny faint">${fmtDate(S.settings.examDate,{weekday:'short',month:'short',day:'numeric'})}</span></div>
        <div class="cd"><span class="label">Regionals</span><span class="num">${rg>=0?rg:'Done'}${rg>=0?'<small>days</small>':''}</span><span class="tiny faint">${fmtDate(S.settings.regionalsDate,{weekday:'short',month:'short',day:'numeric'})}</span></div>
      </div>${ring(pct(done,steps.length),done+'/'+steps.length)}</div>
      <div class="steps">${steps.map(s=>`<a class="step ${s.done?'done':''}" href="${s.route}"><span class="tick">${icon('check')}</span><span class="min0"><span class="t">${esc(s.title)}</span><br><span class="s">${esc(s.sub)}</span></span><span class="prog">${s.need!=null?`${s.have}/${s.need}`:(s.done?'Done':'')}</span></a>`).join('')}</div>
    </div>
    <div class="stack">
      <div class="card stack-s"><span class="label">Projected exam score</span>
        ${proj!=null?`<div class="row"><span class="num" style="font-size:2rem;font-weight:600">${proj}</span><span class="muted">/ 100 on the ${S.settings.blueprint} blueprint</span></div><p class="small muted">Based on ${ans} questions answered. Weakest: ${weakAreas(2).map(a=>esc(areaShort(a))).join(', ')}.</p>`
          :`<p class="small muted">Answer ${25-ans} more questions to unlock your projection by blueprint area.</p>`}
        <div class="row small"><span class="chip acc">${st} day streak</span><span class="chip">${cardCounts().ms} cards mastered</span>${(S.mocks||[]).length?`<span class="chip">Last mock ${S.mocks[S.mocks.length-1].score}</span>`:''}</div>
      </div>
      ${partner?`<a class="card stack-s" href="#team" style="text-decoration:none;color:inherit"><span class="label">Your partner</span><div class="row">${avatarOf(partner.id)?`<img class="avatar" src="${esc(avatarOf(partner.id))}" alt="">`:''}<strong>${esc(nameOf(partner.id))}</strong><span class="tiny faint">${ago(partner.updated)}</span></div>
        <p class="small muted">Today ${partner.planDone??0}/${partner.planTotal??0} · ${partner.streak||0} day streak${partner.projected!=null?` · projected ${partner.projected}`:''}</p></a>`
        :`<a class="card stack-s" href="#team" style="text-decoration:none;color:inherit"><span class="label">Study with your partner</span><p class="small muted">Share this app with your FTDM partner to see each other's progress, plan cases together and run shared timers.</p></a>`}
      <a class="card tp" href="#talk-${f.id}" style="text-decoration:none;color:inherit"><span class="label">Real-world fact of the day</span><strong>${esc(f.title)}</strong><p class="small">${esc(f.fact)}</p></a>
    </div>
  </div>
  ${P.id==='exam'?`<div class="card tint stack-s"><span class="label">How this plan works</span><p class="small muted">Until ${fmtDate(S.settings.examDate)} the plan is about 80% exam and 20% speaking: spaced-repetition cards, one lesson a day in blueprint order, interleaved smart practice that brings back what you miss, full timed mocks on ${[16,9,5,2].map(d=>fmtDate(dayKey(parseDay(S.settings.examDate)-d*DAY))).join(', ')}, and a daily drill. After the exam it flips to roleplay season.</p></div>`:''}
  </div>`;
};

/* ================= LEARN ================= */
V.learn=()=>{
  const ls=LESSON_ORDER.map(id=>LESSON[id]);
  return `<div class="wrap">${head('Learn','15 lessons covering every instructional area on the Finance exam. Read the ideas, then prove it with a 5-question check.')}
  <a class="card stack-s" href="#hub" style="text-decoration:none;color:inherit;border-color:var(--accent)"><span class="label">New · Finance Hub</span><strong>Every FTDM topic in depth, plus the judge questions each one prepares you for</strong><span class="small muted">${HUB.length} topics · ${HUB_ORDER.length} sub-topics · ${JQCARDS.length} judge questions with strong answers · ${hubReadCount(HUB_ORDER)} read</span></a>
  <div class="grid3">
    <a class="card stack-s" href="#deep" style="text-decoration:none;color:inherit"><span class="label">Go deeper</span><strong>PI deep dives</strong><span class="small muted">${D.deep.length} PIs explained: what to say, real-world proof, exam traps</span></a>
    <a class="card stack-s" href="#charts" style="text-decoration:none;color:inherit"><span class="label">Stand out</span><strong>Charts that win judges</strong><span class="small muted">12 chart types and when to sketch each</span></a>
    <a class="card stack-s" href="#library" style="text-decoration:none;color:inherit"><span class="label">Research</span><strong>Where to learn more</strong><span class="small muted">Official sources for every FTDM topic</span></a>
  </div>
  <div class="row"><a class="btn" href="#pis">${icon('learn')}All 408 performance indicators</a><a class="btn" href="#talk">${icon('talk')}Real-world talking points</a><a class="btn" href="#playbook">${icon('playbook')}Roleplay & exam playbook</a></div>
  <div class="stack">${ls.map((L,i)=>{ const qs=QS_BY_LESSON[L.id]||[]; let n=0,c=0; qs.forEach(q=>{const r=S.qs[q.id]; if(r){n+=r.n;c+=r.c}}); const cc=cardCounts(D.cards.filter(x=>x.lesson===L.id));
    const [lab,cls]=status(n?c/n:0,n);
    return `<a class="list-link" href="#lesson-${L.id}"><span class="mono faint" style="width:22px">${String(i+1).padStart(2,'0')}</span><span class="min0"><strong>${esc(L.title)}</strong><br><span class="small muted">${esc(L.area)} · ${L.cards.length} ideas · ${qs.length} questions</span></span>
      <span class="stack-s" style="align-items:flex-end">${S.lessons[L.id]?'<span class="chip good">Read</span>':''}${n?`<span class="chip ${cls}">${pct(c,n)}% · ${lab}</span>`:''}<span class="tiny faint">${cc.ms}/${cc.total} cards mastered</span></span></a>`; }).join('')}</div></div>`;
};
V.lesson=(id)=>{
  const L=LESSON[id]; if(!L) return V.learn();
  const cards=L.cards.map(cid=>CARD[cid]); const qs=QS_BY_LESSON[id]||[];
  return `<div class="wrap">${back('#learn','All lessons')}
  ${head(esc(L.title),`<span class="chip">${esc(L.area)}</span> ${L.pis.map(chipPI).join(' ')}`)}
  <div class="blue-note"><strong>Why it matters:</strong> ${esc(L.why)}</div>
  <div class="stack">${cards.map((c,i)=>`<div class="card flat stack-s"><div class="row between nowrap"><h3>${esc(c.t)}</h3><span class="mono tiny faint">${i+1}/${cards.length}</span></div><p>${esc(c.d)}</p>${c.x?`<p class="small"><mark>Exam tip</mark> ${esc(c.x)}</p>`:''}</div>`).join('')}</div>
  <div class="card stack"><h2>Check yourself</h2><p class="muted small">Retrieval practice beats rereading. Five questions from this lesson, with explanations.</p>
    <div class="row"><a class="btn primary" href="#quiz-lesson.${id}" data-a="lessonDone" data-id="${id}">Start the 5-question check</a><a class="btn" href="#cards-${id}">Study these as flashcards</a></div></div>
  <div class="card stack"><h2>Teach it back</h2><p class="muted small">The Feynman technique: explain one idea from this lesson the way you'd say it to a judge playing a client. Two or three sentences.</p>
    <textarea class="input" id="teach-${id}" placeholder="In plain words, ${esc(cards[0].t.toLowerCase())} means…">${esc(S.notes['teach-'+id]?.text||'')}</textarea>
    <div class="row"><button class="btn" data-a="saveTeach" data-id="${id}">Save</button>${CL.sample?`<button class="btn" data-a="aiTeach" data-id="${id}">${icon('spark')}Get feedback from Claude</button>`:''}</div><div id="teach-out"></div></div>
  <div class="row"><button class="btn primary" data-a="markLesson" data-id="${id}">${S.lessons[id]?'Marked as read':'Mark lesson as read'}</button>${(()=>{const i=LESSON_ORDER.indexOf(id);const n=LESSON_ORDER[i+1];return n?`<a class="btn ghost" href="#lesson-${n}">Next: ${esc(LESSON[n].title)}</a>`:''})()}</div>
  </div>`;
};
V.pis=()=>{
  const q=(UI.piq||'').toLowerCase(); const tier=UI.pitier||'2';
  const list=D.pis.filter(p=>(tier==='all'||String(p.tier)===tier)&&(!q||p.pi.toLowerCase().includes(q)||p.code.toLowerCase().includes(q)));
  return `<div class="wrap">${back('#learn','Learn')}${head('Performance indicator guide','Tier 2 PIs are the Finance-cluster ones that show up most on the exam and in FTDM cases. Each roleplay case lists five PIs: explain each one, apply it to the client, and back it with a real example.')}
  <div class="row"><input class="input" style="max-width:340px" placeholder="Search PIs (e.g. insurance, FI:270)" value="${esc(UI.piq||'')}" data-in="piq"><div class="chips">${[['2','Tier 2 (cluster)'],['1','Tier 1 (core)'],['all','All']].map(([k,l])=>`<button class="chip ${tier===k?'on':''}" data-a="piTier" data-v="${k}">${l}</button>`).join('')}</div></div>
  <div class="card flat scrollx"><table class="tbl"><thead><tr><th>PI</th><th>Performance indicator</th><th>Area</th><th class="n">Your accuracy</th></tr></thead><tbody>
  ${list.slice(0,250).map(p=>{const s=piStats(p.code); const tp=D.talk.filter(t=>t.pis.includes(p.code)).length; return `<tr><td>${chipPI(p.code)}</td><td class="min0">${DEEP[p.code]?`<a href="#pi-${p.code}" style="color:inherit">${esc(p.pi)}</a> <span class="chip acc">Deep dive</span>`:esc(p.pi)}${tp?` <a class="tiny" href="#talk" data-a="talkFilterPI" data-pi="${p.code}">${tp} talking point${tp>1?'s':''}</a>`:''}</td><td class="small muted">${esc(areaShort(PI[p.code].area))}</td><td class="n">${s.n?pct(s.c,s.n)+'%':'·'}</td></tr>`}).join('')}
  </tbody></table></div>${list.length>250?`<p class="small muted">Showing 250 of ${list.length}. Search to narrow.</p>`:''}</div>`;
};

/* ================= FLASHCARDS ================= */
V.cards=(deck)=>{
  if(UI.cardSession && UI.cardSession.deck===(deck||UI.cardSession.deck) && !UI.cardSession.finished) return cardSessionView();
  const decks=[['all','Everything',D.cards],['facts','Real-world facts (roleplay)',FACTCARDS],['jq','Judge questions (roleplay Q&A)',JQCARDS],...LESSON_ORDER.map(id=>[id,LESSON[id].title,D.cards.filter(c=>c.lesson===id)])];
  const sel=deck||'all'; const list=deckCards(sel); const due=dueCards(list).length, nw=newCardsIn(list).length; const cc=cardCounts(list);
  return `<div class="wrap">${head('Flashcards','Spaced repetition: rate how well you knew each card and the app schedules it right before you would forget. Again comes back in 10 minutes; easy cards wait weeks.')}
  <div class="card stack"><div class="row between"><div class="stack-s"><span class="label">Deck</span><select class="input" data-in="deck" style="max-width:340px">${decks.map(([k,l,a])=>`<option value="${k}" ${k===sel?'selected':''}>${esc(l)} (${a.length})</option>`).join('')}</select></div>
    <div class="row"><div class="cd"><span class="label">Due</span><span class="num" style="font-size:1.6rem">${due}</span></div><div class="cd"><span class="label">New</span><span class="num" style="font-size:1.6rem">${nw}</span></div><div class="cd"><span class="label">Mastered</span><span class="num" style="font-size:1.6rem">${cc.ms}</span></div></div></div>
    ${bar(pct(cc.ms,cc.total),'good')}
    <div class="row"><button class="btn primary lg" data-a="startCards" data-deck="${sel}" data-mode="due">Study ${Math.min(due+Math.min(nw,sel==='all'?newPerDay():20),80)||'0'} cards</button>
      <button class="btn" data-a="startCards" data-deck="${sel}" data-mode="cram">Cram 20 (ignore schedule)</button>
      <label class="row small muted"><input type="checkbox" data-in="reverse" ${UI.reverse?'checked':''}> Reverse: see the meaning, recall the term</label></div>
    <p class="tiny faint">New cards per day: ${newPerDay()} (set to finish every card before ${fmtDate(S.settings.examDate)}). Keyboard: <span class="kbd">Space</span> flip, <span class="kbd">1</span>-<span class="kbd">4</span> rate.</p>
  </div></div>`;
};
function cardSessionView(){
  const cs=UI.cardSession; const c=CARD[cs.queue[0]];
  if(!c){ cs.finished=true; return `<div class="wrap">${head('Session complete')}<div class="card stack"><p>You reviewed <strong>${cs.done}</strong> cards. ${cs.again} needed another look.</p><div class="row"><a class="btn primary" href="#today">Back to today</a><button class="btn" data-a="startCards" data-deck="${cs.deck}" data-mode="due">Keep going</button></div></div></div>`; }
  const rev=UI.reverse && c.lesson!=='facts' && c.lesson!=='jq'; const front=rev?c.d:c.t; const backMain=rev?c.t:c.d;
  return `<div class="wrap"><div class="row between"><button class="btn ghost sm" data-a="endCards">${icon('back')}End session</button><span class="mono small faint">${cs.done} done · ${cs.queue.length} left</span></div>
  <div class="flash ${cs.flipped?'flipped':''}" data-a="flip" role="button" tabindex="0" aria-label="Flip card">
    <div class="flash-inner"><div class="face front"><span class="label">${c.lesson==='facts'?'Real-world fact':c.lesson==='jq'?'Judge question · answer out loud':esc(LESSON[c.lesson]?.title||'')}${S.cards[c.id]?'':' · new'}</span><div class="center"><div class="term" style="${rev?'font-size:1.15rem;font-weight:600;font-family:var(--f-body)':''}">${esc(front)}</div></div><span class="tiny faint">Tap or press Space to reveal</span></div>
    <div class="face back"><span class="label">${rev?'Term':c.lesson==='jq'?'A strong answer':'Meaning'}</span><div class="center"><div style="font-size:1.08rem;${rev?'font-family:var(--f-display);font-size:1.4rem;font-weight:700':''}">${esc(backMain)}</div>${c.x?`<div class="tip">${c.lesson==='facts'?'<strong>Say it:</strong> ':'<strong>Tip:</strong> '}${esc(c.x)}</div>`:''}${c.src?`<span class="tiny faint">${c.lesson==='jq'?'Finance Hub: ':'Source: '}${esc(c.src)}</span>`:''}</div></div></div></div>
  <div id="card-ctrl">${cardCtrl(c)}</div>
  </div>`;
}
function cardCtrl(c){ return UI.cardSession.flipped?`<div class="rate">${[['Again',0],['Hard',1],['Good',2],['Easy',3]].map(([l,g])=>`<button class="btn ${g===2?'primary':''}" data-a="rate" data-g="${g}">${l}<small>${cardPreview(c.id,g)}</small></button>`).join('')}</div>`
    :`<button class="btn primary lg block" data-a="flip">Show answer</button>`; }

/* ================= EXAM HUB + PRACTICE ================= */
V.exam=()=>{
  const missed=D.questions.filter(q=>S.qs[q.id]?.w).length; const unseen=D.questions.filter(q=>!S.qs[q.id]).length; const mocks=S.mocks||[];
  return `<div class="wrap">${head('Exam','100 questions, Finance cluster, weighted to the 2026-27 district blueprint. Practice short sets daily; take full mocks under time pressure.')}
  <div class="grid2">
    <div class="card stack"><h2>Practice</h2><p class="small muted">Instant feedback and an explanation after every answer.</p>
      <a class="list-link" href="#quiz-smart"><span><strong>Smart practice · 20</strong><br><span class="small muted">Missed questions come back, weak areas get more</span></span>${icon('play')}</a>
      <a class="list-link" href="#quiz-hot"><span><strong>High-yield · 20</strong><br><span class="small muted">PIs tested on 8 or more of the ${NEXAMS} past DECA exams</span></span>${icon('play')}</a>
      <a class="list-link" href="#quiz-missed"><span><strong>Missed questions · ${missed}</strong><br><span class="small muted">Everything you got wrong last time</span></span>${icon('play')}</a>
      <a class="list-link" href="#quiz-unseen"><span><strong>New questions · ${unseen}</strong><br><span class="small muted">Ones you've never seen</span></span>${icon('play')}</a>
    </div>
    <div class="card stack"><h2>Full mock exam</h2><p class="small muted">${S.settings.mockMinutes} minutes, 100 questions in DECA's proportions: Financial Analysis ${BLUEPRINT[S.settings.blueprint]['Financial Analysis']}, Professional Development ${BLUEPRINT[S.settings.blueprint]['Professional Development']}, Emotional Intelligence ${BLUEPRINT[S.settings.blueprint]['Emotional Intelligence']}, Financial-Information Management ${BLUEPRINT[S.settings.blueprint]['Financial-Information Management']}…</p>
      ${UI.mock&&!UI.mock.submitted?`<a class="btn primary lg" href="#mock">Resume mock (${Object.keys(UI.mock.answers).length}/100)</a>`:`<a class="btn primary lg" href="#mock">Start a mock exam</a>`}
      ${mocks.length?`${spark(mocks.map(m=>m.score))}<div class="stack-s">${mocks.slice(-4).reverse().map(m=>`<a class="row between small" href="#review-${m.t}" style="color:inherit"><span>${new Date(m.t).toLocaleDateString(undefined,{month:'short',day:'numeric'})} · ${fmtTime(m.dur)}</span><span class="mono"><strong>${m.score}</strong>/100</span></a>`).join('')}</div>`:'<p class="tiny faint">Your scores will chart here. Dashed line = 70.</p>'}
    </div>
  </div>
  ${hotCard()}
  <div class="card stack"><h2>Practice by instructional area</h2><div class="stack-s">${AREAS.map(a=>{const st=areaStats(a); const [lab,cls]=status(st.acc,st.n); return `<a class="list-link" href="#quiz-area.${encodeURIComponent(a)}"><span class="min0"><strong>${esc(a)}</strong><br><span class="small muted">${BLUEPRINT.district[a]} on the exam · ${st.seen}/${st.pool} seen</span></span><span class="chip ${cls}">${st.n?pct(st.c,st.n)+'%':lab}</span></a>`}).join('')}</div></div>
  </div>`;
};
// The PIs DECA tested most often across the past exams, with your accuracy on each.
function hotCard(){ if(!NEXAMS) return ''; const top=Object.keys(HITS).filter(c=>PI[c]).sort((a,b)=>HITS[b][0]-HITS[a][0]||HITS[b][1]-HITS[a][1]).slice(0,15);
  return `<details class="card"><summary>Most-tested PIs on ${NEXAMS} past DECA exams</summary><p class="small muted">From the PI code behind every question on the 2018-2024 sample exams, the 2025 and 2026 district exams and two other 2026 exams. Finance-cluster (Tier 2) PIs were 50% of the 2026 district exam, and nearly every one appears on every exam.</p>
  <div class="stack-s">${top.map(c=>{ const s=piStats(c); return `<a class="list-link" href="#pi-${c}"><span class="min0"><span class="mono small">${c}</span> <span class="small">${esc(PI[c].pi)}</span></span><span class="row nowrap"><span class="chip acc">${HITS[c][0]}/${NEXAMS} exams</span>${s.n?`<span class="chip ${s.c/s.n>=.8?'good':s.c/s.n>=.65?'warn':'bad'}">${pct(s.c,s.n)}%</span>`:''}</span></a>`; }).join('')}</div>
  <a class="btn primary" href="#quiz-hot">Practice the high-yield PIs</a></details>`; }
function startQuiz(spec){
  let items=[], title='Practice', mode=spec;
  if(spec==='smart'){ items=smartSet(20); title='Smart practice'; }
  else if(spec==='smart10'){ items=smartSet(10); title='Mixed practice'; mode='smart'; }
  else if(spec==='missed'){ items=shuffle(D.questions.filter(q=>S.qs[q.id]?.w)).slice(0,25); title='Missed questions'; }
  else if(spec==='unseen'){ items=pick(D.questions.filter(q=>!S.qs[q.id]),20); title='New questions'; }
  else if(spec==='hot'){ items=smartSet(20,{pool:D.questions.filter(q=>piHits(q.pi)>=8)}); title='High-yield: most-tested PIs'; mode='smart'; }
  else if(spec.startsWith('lesson.')){ const id=spec.slice(7); items=smartSet(5,{pool:QS_BY_LESSON[id]||[]}); title='Check: '+(LESSON[id]?.title||''); }
  else if(spec.startsWith('area.')){ const a=decodeURIComponent(spec.slice(5)); items=smartSet(15,{pool:QS_BY_AREA[a]||[]}); title=a; }
  else if(spec.startsWith('pis.')){ const set=spec.slice(4).split(','); items=shuffle(D.questions.filter(q=>set.includes(q.pi))).slice(0,15); title=set.length===1?set[0]+' practice':'PI practice'; }
  else if(spec.startsWith('ids.')){ items=spec.slice(4).split(',').map(id=>QBY[id]).filter(Boolean); title=UI.quizTitle||'Challenge'; }
  UI.quiz={spec,mode,title,items:items.map(q=>q.id),i:0,ans:{},seed:Date.now()%100000,t:Date.now()};
}
function optOrder(qid,seed){ return shuffle([0,1,2,3],hashStr(qid)+seed); }
V.quiz=(spec)=>{
  if(!UI.quiz||UI.quiz.spec!==spec||UI.quiz.closed) startQuiz(spec||'smart');
  const Z=UI.quiz; if(!Z.items.length) return `<div class="wrap">${back('#exam','Exam')}<div class="empty">Nothing here yet. ${spec==='missed'?'You have no missed questions right now.':'Try smart practice.'}</div></div>`;
  if(Z.i>=Z.items.length) return quizSummary();
  const q=QBY[Z.items[Z.i]]; const a=Z.ans[q.id]; const ord=optOrder(q.id,Z.seed);
  return `<div class="wrap"><div class="row between"><button class="btn ghost sm" data-a="quitQuiz">${icon('back')}${esc(Z.title)}</button><span class="mono small faint">${Z.i+1} / ${Z.items.length}</span></div>
  ${bar(pct(Z.i,Z.items.length))}
  <div class="card qcard"><div class="row"><span class="chip">${esc(areaShort(q.area))}</span>${chipPI(q.pi)}${(a?a.prevW:S.qs[q.id]?.w)?'<span class="chip bad">Missed before</span>':''}</div>
    <div class="qstem">${esc(q.q)}</div>
    <div class="opts">${ord.map((oi,k)=>{ let cls=''; if(a){ if(oi===0) cls='right'; else if(a.pick===oi) cls='wrong'; } return `<button class="opt ${cls}" ${a?'disabled':''} data-a="answer" data-o="${oi}"><span class="k">${'ABCD'[k]}</span><span>${esc(q.o[oi])}</span></button>`;}).join('')}</div>
    ${a?`<div class="explain ${a.ok?'good':'bad'}"><strong>${a.ok?'Correct.':'Not quite.'}</strong> ${esc(q.e)}</div>
      <div class="row between"><div class="row">${a.ok?`<button class="btn sm ghost" data-a="guessed">I guessed. Bring it back tomorrow</button>`:''}${CL.sample?`<button class="btn sm ghost" data-a="aiExplain" data-q="${q.id}">${icon('spark')}Explain it another way</button>`:''}</div><button class="btn primary" data-a="nextQ">${Z.i+1<Z.items.length?'Next':'See results'}</button></div><div id="ai-explain"></div>`
      :`<p class="tiny faint">Keys <span class="kbd">1</span>-<span class="kbd">4</span> or <span class="kbd">A</span>-<span class="kbd">D</span>. Read every option before choosing: the exam rewards the "best" answer.</p>`}
  </div></div>`;
};
function quizSummary(){
  const Z=UI.quiz; const res=Z.items.map(id=>({q:QBY[id],a:Z.ans[id]})); const c=res.filter(r=>r.a?.ok).length;
  if(!Z.logged){ Z.logged=true; S.quizzes.push({t:Z.t,spec:Z.spec,n:res.length,c}); save(); }
  const byArea={}; res.forEach(r=>{const x=byArea[r.q.area]=byArea[r.q.area]||[0,0]; x[1]++; if(r.a?.ok) x[0]++;});
  return `<div class="wrap">${head(`${c} / ${res.length} correct`,esc(Z.title))}
  <div class="card stack"><div class="row">${Object.entries(byArea).map(([a,[cc,n]])=>`<span class="chip ${cc/n>=.8?'good':cc/n>=.6?'warn':'bad'}">${esc(areaShort(a))} ${cc}/${n}</span>`).join('')}</div>
  <div class="row"><a class="btn primary" href="#today">Back to today</a><button class="btn" data-a="againQuiz">Another set</button><a class="btn ghost" href="#exam">Exam hub</a></div></div>
  <div class="stack">${res.filter(r=>!r.a?.ok).map(r=>`<div class="card flat stack-s"><div class="row">${chipPI(r.q.pi)}<span class="chip bad">Missed</span></div><strong>${esc(r.q.q)}</strong><p class="small"><mark>Answer</mark> ${esc(r.q.o[0])}</p><p class="small muted">${esc(r.q.e)}</p></div>`).join('')}</div></div>`;
}

/* ================= MOCK EXAM ================= */
function loadMock(){ try{ const m=JSON.parse(localStorage.getItem('ftdm-ace-mock')||'null'); if(m&&!m.submitted) UI.mock=m; }catch(e){} }
function saveMock(){ try{ localStorage.setItem('ftdm-ace-mock',JSON.stringify(UI.mock)); }catch(e){} }
V.mock=()=>{
  const M=UI.mock;
  if(!M||M.submitted) return `<div class="wrap">${back('#exam','Exam')}${head('Mock exam','Just like the real thing: 100 questions, one timer, no explanations until you submit.')}
   <div class="card stack"><div class="grid3">${AREAS.filter(a=>BLUEPRINT[S.settings.blueprint][a]).map(a=>`<div class="row between small"><span>${esc(areaShort(a))}</span><span class="mono">${BLUEPRINT[S.settings.blueprint][a]}</span></div>`).join('')}</div>
   <div class="row"><label class="field" style="flex:1;min-width:160px">Blueprint<select class="input" data-in="bp"><option value="district" ${S.settings.blueprint==='district'?'selected':''}>District (Dec 7 cluster exam)</option><option value="association" ${S.settings.blueprint==='association'?'selected':''}>Association / state</option></select></label>
   <label class="field" style="flex:1;min-width:160px">Time limit<select class="input" data-in="mockMin">${[45,60,75,90,0].map(m=>`<option value="${m}" ${S.settings.mockMinutes===m?'selected':''}>${m?m+' minutes':'Untimed'}</option>`).join('')}</select></label></div>
   <p class="tiny faint">Ask your chapter advisor for your district's exact time limit. Pace yourself at about 36 seconds per question for 60 minutes.</p>
   <button class="btn primary lg" data-a="startMock">Start the timer</button></div></div>`;
  const q=QBY[M.items[M.i]]; const pickd=M.answers[q.id]; const ord=optOrder(q.id,M.seed); const left=M.endsAt?Math.max(0,(M.endsAt-Date.now())/1000):null;
  return `<div class="wrap"><div class="row between"><span class="label">Mock exam · question ${M.i+1} of 100</span>${left!=null?`<span class="timerpill ${left<300?'low':''}" id="mock-timer">${fmtTime(left)}</span>`:'<span class="timerpill">Untimed</span>'}</div>
  <div class="card qcard"><div class="qstem">${esc(q.q)}</div>
    <div class="opts">${ord.map((oi,k)=>`<button class="opt ${pickd===oi?'sel':''}" data-a="mockPick" data-o="${oi}"><span class="k">${'ABCD'[k]}</span><span>${esc(q.o[oi])}</span></button>`).join('')}</div>
    <div class="row between"><button class="btn" data-a="mockNav" data-d="-1" ${M.i?'':'disabled'}>Back</button><button class="btn ${M.flags[q.id]?'primary':''}" data-a="mockFlag">${icon('flag')}${M.flags[q.id]?'Flagged':'Flag'}</button><button class="btn primary" data-a="mockNav" data-d="1">${M.i<99?'Next':'Review'}</button></div></div>
  <details class="card" ${UI.mockGrid?'open':''}><summary>Question map · ${Object.keys(M.answers).length}/100 answered · ${Object.keys(M.flags).filter(k=>M.flags[k]).length} flagged</summary>
    <div class="qnav">${M.items.map((id,i)=>`<button class="${M.answers[id]!=null?'ans':''} ${M.flags[id]?'flag':''} ${i===M.i?'cur':''}" data-a="mockJump" data-i="${i}">${i+1}</button>`).join('')}</div>
    <div class="row" style="margin-top:12px"><button class="btn primary" data-a="submitMock">Submit exam</button><button class="btn ghost danger" data-a="abandonMock">Quit without saving</button></div></details>
  </div>`;
};
function gradeMock(){
  const M=UI.mock; let c=0; const byArea={}; const items=M.items.map(id=>{const q=QBY[id]; const a=M.answers[id]; const ok=a===0; if(ok)c++; const x=byArea[q.area]=byArea[q.area]||[0,0]; x[1]++; if(ok)x[0]++; recordAnswer(id,ok); return {q:id,a:a??-1};});
  const rec={t:M.t,score:c,dur:Math.round((Date.now()-M.t)/1000),bp:M.bp,byArea,items}; S.mocks.push(rec); today().mock=1; bump('qs',100); M.submitted=true; saveMock(); save();
  return rec;
}
V.review=(t)=>{
  const m=(S.mocks||[]).find(x=>String(x.t)===String(t)); if(!m) return V.exam();
  const filter=UI.revFilter||'wrong'; const items=m.items.filter(x=>filter==='all'||(filter==='wrong'?x.a!==0:x.a===0));
  return `<div class="wrap">${back('#exam','Exam')}${head(`Mock exam: ${m.score}/100`,`${new Date(m.t).toLocaleString(undefined,{month:'short',day:'numeric',hour:'numeric',minute:'2-digit'})} · ${fmtTime(m.dur)} · ${m.bp} blueprint`)}
  <div class="card flat scrollx"><table class="tbl"><thead><tr><th>Area</th><th class="n">On exam</th><th class="n">You</th><th style="width:30%"></th></tr></thead><tbody>
  ${AREAS.filter(a=>m.byArea[a]).map(a=>{const [c,n]=m.byArea[a]; const p=pct(c,n); return `<tr><td>${esc(a)}</td><td class="n">${n}</td><td class="n">${c}/${n}</td><td>${bar(p,p>=80?'good':p>=65?'warn':'bad')}</td></tr>`}).join('')}</tbody></table></div>
  <div class="row"><div class="chips">${[['wrong','Missed'],['right','Correct'],['all','All']].map(([k,l])=>`<button class="chip ${filter===k?'on':''}" data-a="revFilter" data-v="${k}">${l}</button>`).join('')}</div><a class="btn sm" href="#quiz-ids.${m.items.filter(x=>x.a!==0).map(x=>x.q).join(',')}" data-a="setQuizTitle" data-v="Retry missed mock questions">Retry missed questions</a></div>
  <div class="stack">${items.map(x=>{const q=QBY[x.q]; return `<div class="card flat stack-s"><div class="row">${chipPI(q.pi)}<span class="chip">${esc(areaShort(q.area))}</span><span class="chip ${x.a===0?'good':'bad'}">${x.a===0?'Correct':x.a<0?'Skipped':'Missed'}</span></div><strong>${esc(q.q)}</strong>${x.a>0?`<p class="small">You picked: ${esc(q.o[x.a])}</p>`:''}<p class="small"><mark>Answer</mark> ${esc(q.o[0])}</p><p class="small muted">${esc(q.e)}</p></div>`}).join('')}</div></div>`;
};

/* ================= PROGRESS ================= */
V.progress=()=>{
  const ans=answeredCount(); const mocks=S.mocks||[]; const cc=cardCounts(); const runs=(S.caseRuns||[]).filter(r=>r.total!=null);
  const days=[]; for(let i=44;i>=0;i--){ days.push(dayKey(startOfDay()-i*DAY)); }
  const rubAvg={}; RUBRIC.forEach(r=>{ const v=runs.map(x=>x.scores?.[r.k]).filter(v=>v!=null); if(v.length) rubAvg[r.k]=v.reduce((s,x)=>s+x,0)/v.length/r.max; });
  const weakR=Object.entries(rubAvg).sort((a,b)=>a[1]-b[1]).slice(0,2);
  const wp=weakPIs(8);
  return `<div class="wrap">${head('Progress','Where you stand by instructional area, weighted the way DECA weights the exam.')}
  <div class="grid3">
    <div class="card stack-s"><span class="label">Projected score</span><span class="num" style="font-size:2rem;font-weight:600">${ans>=25?projected():'·'}</span><span class="tiny faint">${ans} of ${D.questions.length} questions seen</span></div>
    <div class="card stack-s"><span class="label">Mock exams</span><span class="num" style="font-size:2rem;font-weight:600">${mocks.length?mocks[mocks.length-1].score:'·'}</span>${mocks.length>1?spark(mocks.map(m=>m.score)):`<span class="tiny faint">${mocks.length?'1 mock taken. Take another to see a trend.':'No mocks yet'}</span>`}</div>
    <div class="card stack-s"><span class="label">Flashcards</span><span class="num" style="font-size:2rem;font-weight:600">${cc.ms}<small class="faint" style="font-size:.9rem">/${cc.total}</small></span>${bar(pct(cc.ms,cc.total),'good')}<span class="tiny faint">${cc.lr} learning · ${cc.nw} new</span></div>
    <div class="card stack-s"><span class="label">Roleplay average</span><span class="num" style="font-size:2rem;font-weight:600">${runs.length?Math.round(runs.reduce((s,r)=>s+r.total,0)/runs.length):'·'}</span><span class="tiny faint">${runs.length} scored case${runs.length===1?'':'s'}${weakR.length?` · work on ${weakR.map(([k])=>RUBRIC.find(r=>r.k===k).label.split(':')[0].toLowerCase()).join(', ')}`:''}</span></div>
  </div>
  <div class="card stack"><h2>By instructional area</h2><div class="scrollx"><table class="tbl"><thead><tr><th>Area</th><th class="n">District items</th><th class="n">Seen</th><th class="n">Accuracy</th><th>Status</th><th style="width:22%"></th></tr></thead><tbody>
  ${AREAS.map(a=>{const st=areaStats(a); const [lab,cls]=status(st.acc,st.n); return `<tr><td><a href="#quiz-area.${encodeURIComponent(a)}" style="color:inherit">${esc(a)}</a></td><td class="n">${BLUEPRINT.district[a]}</td><td class="n">${st.seen}/${st.pool}</td><td class="n">${st.n?pct(st.c,st.n)+'%':'·'}</td><td><span class="chip ${cls}">${lab}</span></td><td>${bar(st.n?100*st.acc:0,cls)}</td></tr>`}).join('')}
  </tbody></table></div><p class="tiny faint">Projection = each area's estimated accuracy × its number of items on the ${S.settings.blueprint} blueprint (DECA Guide 2026-27, p. 39). Unseen areas count as about 60%.</p></div>
  ${wp.length?`<div class="card stack"><div class="row between"><h2>Weakest performance indicators</h2><a class="btn sm primary" href="#quiz-pis.${wp.map(w=>w.pi).join(',')}">Practice these</a></div><div class="stack-s">${wp.map(w=>`<div class="row between small"><span class="min0">${chipPI(w.pi)} ${esc(PI[w.pi]?.pi||'')}</span><span class="mono">${pct(w.acc*w.n,w.n)}%</span></div>`).join('')}</div></div>`:''}
  <div class="card stack"><div class="row between"><h2>Last 45 days</h2><span class="chip acc">${streak()} day streak</span></div><div class="heat">${days.map(k=>`<i class="l${activityLevel(k)}" title="${k}"></i>`).join('')}</div></div>
  </div>`;
};
