/* Views part 3: PI deep dives, charts that win judges, sketch drill, learning library. */
'use strict';
const DEEP = Object.fromEntries((D.deep||[]).map(d=>[d.pi,d]));
Object.assign(NAV_OF,{pi:'learn',deep:'learn',library:'learn',charts:'roleplay',sketch:'roleplay'});

/* ---------- chart drawings (inline SVG, theme tokens) ---------- */
const SV=(body,h=170)=>`<svg viewBox="0 0 320 ${h}" class="chart-svg" role="img" aria-hidden="false" style="width:100%;max-width:420px;height:auto;display:block">${body}</svg>`;
const T=(x,y,s,o={})=>`<text x="${x}" y="${y}" font-size="${o.size||11}" font-family="Inter,system-ui,sans-serif" font-weight="${o.w||500}" fill="${o.fill||'var(--ink)'}" text-anchor="${o.a||'start'}">${esc(s)}</text>`;
const CHARTS = [
 {id:'timeline',name:'Implementation timeline',when:'Every case. Judges score "practical," and a 30-60-90 day plan proves your solution can actually happen.',
  example:'Twins on the way: Month 1 insurance and wills, months 2-6 emergency fund, birth: open two 529s, year 3: house down payment.',
  steps:['Draw one long horizontal line.','Mark 3-4 points: Now, 30 days, 90 days, 1 year.','Write one action under each point, with who does it.','Title it with the outcome: "Fully protected in 30 days."'],
  say:'"Here\'s exactly what happens and when. You\'ll be fully protected within 30 days."',
  svg:()=>SV(`${T(10,22,'Your 12-month plan',{w:700,size:13})}<line x1="20" y1="80" x2="300" y2="80" stroke="var(--ink-3)" stroke-width="3"/>${[[48,'Now','Insurance + wills'],[126,'Day 30','Autopay savings'],[204,'Day 90','Open 529s'],[280,'Year 1','6-mo fund done']].map(([x,a,b],i)=>`<circle cx="${x}" cy="80" r="8" fill="${['var(--accent)','var(--info)','var(--warn)','var(--good)'][i]}"/>${T(x,60,a,{a:'middle',w:700})}${T(x,108,b,{a:'middle',size:9,fill:'var(--ink-2)'})}`).join('')}`,140)},
 {id:'pie',name:'Budget pie (50/30/20)',when:'Budgets, overhead, start-up costs, "where does the money go."',
  example:'First paycheck plan: $3,400 a month take-home split into needs $1,700, wants $1,020, savings and debt $680.',
  steps:['Draw a circle, then split it: half, then about a third and a fifth of the rest.','Label each slice with the category AND the dollar amount from the case.','Shade the slice you want the judge to notice (savings).','Title it with the takeaway: "$680 a month goes to your future."'],
  say:'"Half of your take-home covers needs, and $680 a month goes straight to your future."',
  svg:()=>{ const cx=95,cy=95,r=62; const seg=(a0,a1,c)=>{const p=(a)=>[cx+r*Math.cos(a),cy+r*Math.sin(a)]; const [x0,y0]=p(a0),[x1,y1]=p(a1); return `<path d="M${cx} ${cy}L${x0.toFixed(1)} ${y0.toFixed(1)}A${r} ${r} 0 ${a1-a0>Math.PI?1:0} 1 ${x1.toFixed(1)} ${y1.toFixed(1)}Z" fill="${c}" stroke="var(--surface)" stroke-width="2"/>`;};
    const a=-Math.PI/2; return SV(`${seg(a,a+Math.PI,'var(--info)')}${seg(a+Math.PI,a+Math.PI*1.6,'var(--warn)')}${seg(a+Math.PI*1.6,a+Math.PI*2,'var(--accent)')}${T(180,52,'Needs 50%  $1,700',{w:600})}${T(180,82,'Wants 30%  $1,020',{w:600})}${T(180,112,'Save + debt 20%  $680',{w:700,fill:'var(--accent)'})}${T(180,140,'Take-home: $3,400/mo',{size:10,fill:'var(--ink-2)'})}`,190); }},
 {id:'bars',name:'Comparison bar chart',when:'Comparing options with numbers: interest costs, fees, savings rates, loan terms.',
  example:'Credit comeback: total interest paying minimums vs the $900/month plan.',
  steps:['Draw a baseline and 2-4 bars side by side.','Write the exact number on top of each bar.','Make the bar you recommend darker.','Title: "The plan saves about $X."'],
  say:'"Paying minimums costs you more than twice as much. This bar is the plan."',
  svg:()=>SV(`${T(10,20,'Interest paid on $16,500 of card debt',{w:700,size:12})}<line x1="30" y1="150" x2="300" y2="150" stroke="var(--ink-3)"/><rect x="60" y="45" width="70" height="105" rx="4" fill="var(--bad)" opacity=".75"/><rect x="190" y="112" width="70" height="38" rx="4" fill="var(--accent)"/>${T(95,40,'Minimums: many years',{a:'middle',size:10,w:700})}${T(225,106,'Plan: ~23 months',{a:'middle',size:10,w:700})}${T(95,165,'Minimum payments',{a:'middle',size:10})}${T(225,165,'$900 / month',{a:'middle',size:10})}`,175)},
 {id:'growth',name:'Growth curve (start now vs later)',when:'Time value of money, need to save and invest, retirement, college savings.',
  example:'First paycheck plan: $200 a month from 22 vs from 32, ending around $895,000 vs $387,000 at 8%.',
  steps:['Draw an L: years along the bottom, dollars up the side.','Sketch two curves that bend upward; the earlier one starts left and ends much higher.','Write the end value at the tip of each curve.','Title: "Starting 10 years earlier more than doubles it."'],
  say:'"Same $200 a month. The only difference is when you start."',
  svg:()=>SV(`${T(10,18,'$200/month at 8% until age 65',{w:700,size:12})}<line x1="30" y1="150" x2="300" y2="150" stroke="var(--ink-3)"/><line x1="30" y1="150" x2="30" y2="28" stroke="var(--ink-3)"/><path d="M40 148 C150 145, 230 120, 290 36" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M110 149 C200 147, 255 132, 290 104" fill="none" stroke="var(--warn)" stroke-width="3"/>${T(292,34,'$895K',{size:11,w:700,a:'end',fill:'var(--accent)'})}${T(292,98,'$387K',{size:11,w:700,a:'end',fill:'var(--warn)'})}${T(40,165,'Age 22',{size:10})}${T(110,165,'32',{size:10})}${T(285,165,'65',{size:10})}${T(60,60,'Start at 22',{size:10,fill:'var(--accent)',w:600})}${T(60,76,'Start at 32',{size:10,fill:'var(--warn)',w:600})}`,172)},
 {id:'riskmatrix',name:'Risk matrix',when:'Insurance needs, risk management, ERM, fraud, any "what could go wrong."',
  example:'Twins on the way: a parent dying (low likelihood, huge impact → term life), job loss (medium, high → 6-month fund), car repair (high, low → emergency fund).',
  steps:['Draw a 3×3 grid. Bottom = likelihood (low→high). Side = impact (low→high).','Plot 3-5 risks from the case as dots with short labels.','Write the response next to each: transfer (insurance), reduce, accept.','Title: "Insurance covers the top-right risks."'],
  say:'"The risks in the top right could hurt your family most, so those are the ones we transfer with insurance."',
  svg:()=>{ let g=''; for(let i=0;i<3;i++)for(let j=0;j<3;j++){ const c=(i+(2-j))>=3?'var(--bad-soft)':(i+(2-j))>=2?'var(--warn-soft)':'var(--good-soft)'; g+=`<rect x="${60+i*70}" y="${20+j*45}" width="68" height="43" fill="${c}"/>`; }
    return SV(`${g}<circle cx="100" cy="40" r="6" fill="var(--bad)"/>${T(110,44,'Death: term life',{size:9,w:700})}<circle cx="170" cy="62" r="6" fill="var(--bad)"/>${T(150,80,'Job loss: 6-mo fund',{size:9,w:700})}<circle cx="250" cy="130" r="6" fill="var(--good)"/>${T(196,148,'Car repair: accept',{size:9,w:700})}${T(165,170,'Likelihood →',{a:'middle',size:10})}${T(14,90,'Impact',{size:10})}${T(14,102,'↑',{size:12})}`,175); }},
 {id:'tchart',name:'Pros and cons T-chart',when:'Two-way decisions: loan vs partner, LLC vs sole proprietor, term vs whole life, bank vs credit union.',
  example:'Food truck: LLC vs sole proprietorship, with the recommendation circled.',
  steps:['Draw a big T. Option A on the left, option B on the right.','List 2-3 pros (+) and cons (−) under each, using case facts.','Circle the winner and write one line why.','Title: "Why we recommend the LLC."'],
  say:'"Both work, but this side protects your house if a customer sues."',
  svg:()=>SV(`<line x1="160" y1="30" x2="160" y2="160" stroke="var(--ink-3)" stroke-width="2"/><line x1="20" y1="44" x2="300" y2="44" stroke="var(--ink-3)" stroke-width="2"/>${T(90,36,'LLC ✓',{a:'middle',w:800,size:13,fill:'var(--accent)'})}${T(230,36,'Sole proprietor',{a:'middle',w:700,size:13})}${T(28,68,'+ Protects personal assets',{size:10})}${T(28,88,'+ Pass-through taxes',{size:10})}${T(28,108,'− State filing fee',{size:10})}${T(168,68,'+ Simplest to start',{size:10})}${T(168,88,'+ No filing in most states',{size:10})}${T(168,108,'− Unlimited liability',{size:10,fill:'var(--bad)'})}<ellipse cx="90" cy="32" rx="44" ry="15" fill="none" stroke="var(--accent)" stroke-width="2"/>`,170)},
 {id:'decision',name:'Decision matrix',when:'Three or more options: choosing a bank, financing, a product, a strategy. It looks analytical, which feeds the critical-thinking score.',
  example:'Windfall: pay off mortgage vs invest vs keep in savings, scored on return, safety and flexibility.',
  steps:['Rows = options, columns = 3 criteria that matter to THIS client.','Score each 1-5 (optionally weight the most important criterion ×2).','Total each row and circle the highest.','Title: "Investing scores highest for your goals."'],
  say:'"We scored each option on what you told us matters most. Here\'s why this one wins."',
  svg:()=>{ const rows=[['Pay off mortgage','2','5','1','8'],['Invest (index funds)','5','3','4','12'],['Keep in savings','1','5','5','11']]; let g=`${['Option','Return','Safety','Flex','Total'].map((h,i)=>T([20,150,200,245,290][i],30,h,{w:700,size:10,a:i?'middle':'start'})).join('')}`;
    rows.forEach((r,k)=>{ const y=56+k*30; g+=`<line x1="14" y1="${y-18}" x2="310" y2="${y-18}" stroke="var(--line)"/>`+r.map((c,i)=>T([20,150,200,245,290][i],y,c,{size:10,w:i===4?800:500,a:i?'middle':'start',fill:i===4&&k===1?'var(--accent)':'var(--ink)'})).join(''); });
    return SV(g+`<circle cx="290" cy="82" r="13" fill="none" stroke="var(--accent)" stroke-width="2"/>`,150); }},
 {id:'flow',name:'Process flowchart',when:'Client-service process, fraud controls, compliance (prevent-detect-correct), "what happens if."',
  example:'After the phone scam: report → freeze → dispute → protect, with the bank\'s role in each box.',
  steps:['Draw 3-5 boxes left to right (or top to bottom).','One verb per box: Discover, Recommend, Implement, Review.','Arrows between them; loop the last back to the first if it repeats.','Title: "How we work for you."'],
  say:'"This is our process, and you\'re in control at every step."',
  svg:()=>SV(`${['Discover','Recommend','Implement','Review'].map((s,i)=>`<rect x="${12+i*77}" y="55" width="66" height="40" rx="8" fill="var(--accent-soft)" stroke="var(--accent)"/>${T(45+i*77,79,s,{a:'middle',size:10,w:700})}${i<3?`<path d="M${80+i*77} 75 l9 0" stroke="var(--ink-3)" stroke-width="2" marker-end="url(#ah)"/>`:''}`).join('')}<path d="M276 97 C276 135, 45 135, 45 99" fill="none" stroke="var(--ink-3)" stroke-dasharray="4 3"/>${T(160,148,'Review every year or after a life event',{a:'middle',size:10,fill:'var(--ink-2)'})}<defs><marker id="ah" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0L6 3L0 6z" fill="var(--ink-3)"/></marker></defs>`,160)},
 {id:'pyramid',name:'Financial planning pyramid',when:'Order of priorities for any client: protect first, then save, then invest, then legacy. Great for new parents, graduates, windfalls.',
  example:'Growing family: base = emergency fund + insurance; next = 401(k) match; next = 529s and index funds; top = wills and estate plan.',
  steps:['Draw a triangle split into 4 layers.','Bottom: Protect (emergency fund, insurance). Then Save (match, debt payoff). Then Invest (index funds, 529). Top: Legacy (will, estate).','Put a check on layers the client already has.','Title: "We build from the bottom up."'],
  say:'"We start at the base: nothing on top is safe until your family is protected."',
  svg:()=>SV(`${[['Legacy: will, trusts','var(--info)'],['Invest: index funds, 529','var(--accent)'],['Save: 401(k) match, pay debt','var(--warn)'],['Protect: emergency fund, insurance','var(--good)']].map(([s,c],i)=>{ const top=20+i*36,bot=top+34; const w0=96+i*52,w1=96+(i+1)*52; return `<path d="M${160-w0/2} ${top} L${160+w0/2} ${top} L${160+w1/2} ${bot} L${160-w1/2} ${bot}Z" fill="${c}" opacity=".85"/>${T(160,top+21,s,{a:'middle',size:i?10:9,w:700,fill:'var(--surface)'})}`; }).join('')}`,170)},
 {id:'org',name:'Governance org chart',when:'Corporate governance, compliance structure, who approves what.',
  example:'Pinecrest IPO: shareholders → board (audit committee, independent directors) → CEO → CFO and internal audit (dotted line to the audit committee).',
  steps:['Top box: Shareholders. Below: Board of directors.','Hang committees off the board (audit, compensation).','Below the board: CEO, then CFO and other officers.','Draw a dotted line from internal audit to the audit committee: that independence is the point.'],
  say:'"Internal audit reports to the independent audit committee, not just the CEO. That\'s what investors want to see."',
  svg:()=>SV(`${[[110,12,100,'Shareholders'],[110,56,100,'Board of directors'],[230,56,82,'Audit committee'],[110,100,100,'CEO'],[40,142,90,'CFO'],[190,142,100,'Internal audit']].map(([x,y,w,s])=>`<rect x="${x}" y="${y}" width="${w}" height="28" rx="6" fill="var(--surface-2)" stroke="var(--ink-3)"/>${T(x+w/2,y+18,s,{a:'middle',size:10,w:700})}`).join('')}<path d="M160 40v16M160 84v16M210 70h20M160 128v6M85 134h155M85 134v8M240 134v8" stroke="var(--ink-3)" fill="none"/><path d="M290 142 V84" stroke="var(--accent)" stroke-dasharray="4 3" fill="none" stroke-width="2"/>`,175)},
 {id:'cashbars',name:'Monthly cash flow bars',when:'Cash flow problems, seasonal businesses, "profitable but broke."',
  example:'GreenEdge Landscaping: tall summer bars, short winter bars, a shaded gap and the line of credit that fills it.',
  steps:['Draw 12 short bars (Jan to Dec) for cash in; mark monthly costs as a flat line.','Shade the months where bars fall below the line.','Label the gap in dollars.','Title: "A $225,000 cushion covers the winter."'],
  say:'"The shaded months are the problem. This reserve, built in summer, covers them."',
  svg:()=>{ const v=[25,25,40,85,110,120,125,120,100,70,30,25]; return SV(`${T(10,18,'Cash in by month vs monthly costs',{w:700,size:12})}${v.map((h,i)=>`<rect x="${20+i*24}" y="${150-h}" width="16" height="${h}" rx="2" fill="${h<60?'var(--bad)':'var(--accent)'}" opacity="${h<60?.7:.9}"/>`).join('')}<line x1="14" y1="90" x2="306" y2="90" stroke="var(--ink)" stroke-dasharray="5 4" stroke-width="1.5"/>${T(306,84,'Monthly costs',{a:'end',size:9,w:700})}${'JFMAMJJASOND'.split('').map((m,i)=>T(28+i*24,164,m,{a:'middle',size:9})).join('')}`,172); }},
 {id:'kpi',name:'KPI scorecard',when:'Every case\'s "how will we know it worked" and the judge question about measuring success.',
  example:'Hometown Bank: accounts opened under age 30, app rating, 90-day retention, products per customer.',
  steps:['Draw a 4-column table: Measure, Today, Target, By when.','Pick 3-4 measures tied to the client\'s goal.','Use numbers from the case for "Today."','Title: "How you\'ll know it\'s working."'],
  say:'"You\'ll know this is working when these numbers hit their targets. We\'d review them every quarter."',
  svg:()=>{ const r=[['Emergency fund','$9K','$30K','Jun 2028'],['Credit score','610','700+','Nov 2027'],['Savings rate','3%','15%','Mar 2027']]; let g=['Measure','Today','Target','By'].map((h,i)=>T([16,150,205,262][i],30,h,{w:700,size:10})).join('');
    r.forEach((row,k)=>{ const y=58+k*28; g+=`<line x1="12" y1="${y-18}" x2="308" y2="${y-18}" stroke="var(--line)"/>`+row.map((c,i)=>T([16,150,205,262][i],y,c,{size:10,w:i===2?700:500,fill:i===2?'var(--accent)':'var(--ink)'})).join(''); }); return SV(g,140); }},
];
const CHART=Object.fromEntries(CHARTS.map(c=>[c.id,c]));
function chartsFor(c){
  const m=[[/^(FI:062|FI:238|FI:270|FI:569|FI:831)$/,'growth'],[/^(FI:066|FI:106|FM:013|OP:024|FI:065)$/,'pie'],[/^(FI:571|FI:081|SM:075|SM:076|RM:)/,'riskmatrix'],[/^(FI:077|FI:337)$/,'pyramid'],
    [/^(BL:003|FI:336|FI:075|FI:076|FI:354|FI:573)$/,'tchart'],[/^(PD:213|PD:214|PD:302|PD:303|PD:301)$/,'org'],[/^(FI:091|FI:093|FI:094|FM:014)$/,'cashbars'],[/^(CR:012|BL:148|RM:058|FI:073|CR:010|EI:128|FI:830)$/,'flow'],[/^(FI:568|FI:782|FI:071|FI:002|FI:072)$/,'bars']];
  const out=[]; c.pis.forEach(p=>m.forEach(([re,id])=>{ if(re.test(p)&&!out.includes(id)) out.push(id); }));
  out.push('timeline','kpi'); return [...new Set(out)].slice(0,3);
}

/* ---------- CHARTS PAGE ---------- */
V.charts=(id)=>{
  const one=id&&CHART[id];
  const card=c=>`<div class="card stack" id="chart-${c.id}"><div class="row between"><h2>${esc(c.name)}</h2></div><div class="chart-wrap">${c.svg()}</div>
    <p class="small"><strong>Use it for:</strong> ${esc(c.when)}</p><p class="small muted"><strong>FTDM example:</strong> ${esc(c.example)}</p>
    <div><span class="label">Draw it in 2 minutes</span><ol class="model small" style="margin-top:4px">${c.steps.map(s=>`<li>${esc(s)}</li>`).join('')}</ol></div>
    <div class="tp"><span class="label">What to say as you hand it over</span><div class="say">${esc(c.say)}</div></div></div>`;
  if(one) return `<div class="wrap">${back('#charts','All chart types')}${card(one)}<a class="btn primary" href="#sketch">Practice sketching it</a></div>`;
  return `<div class="wrap">${head('Charts that win judges','A simple hand-drawn chart makes your solution look planned and practical, and it gives the judge something to remember you by. Here is what you can use, which chart fits which PI, and how to draw each one fast.')}
  <div class="warn-note small"><strong>The rules (DECA Guide 2026-27, Team Decision Making):</strong> you may not bring printed materials or visual aids into the event. You <em>may</em> hand the judge or leave with them materials you create during the 30-minute prep, using the materials provided there. So every chart must be sketched by hand during prep: keep it simple.</div>
  <div class="card stack"><h2>Seven rules for a chart that scores</h2><ol class="model small">
    <li><strong>One chart, one message.</strong> If you can't say its point in one sentence, it's too complicated.</li>
    <li><strong>Title = the takeaway</strong>, not the topic: "Starting now more than doubles your money," not "Investment growth."</li>
    <li><strong>Use the case's real numbers.</strong> Every number you write is proof you read the case closely.</li>
    <li><strong>Big, dark and clean.</strong> Thick lines, few words, labels written right on the chart instead of a legend.</li>
    <li><strong>Highlight the answer:</strong> circle, darken or star the option you recommend.</li>
    <li><strong>Time it.</strong> Budget 3-5 minutes of prep for one chart. Hand it over when you reach that point, not at the start, so the judge listens instead of reading ahead.</li>
    <li><strong>Talk to the judge, not the paper.</strong> Point, say the takeaway, then look up. Both partners can refer back to it in the judge questions.</li></ol>
    <p class="small muted">Feeds the rubric: <em>practical</em> and <em>effective</em> (a timeline and KPIs show the plan works), <em>critical thinking</em> (a decision matrix shows your reasoning), and <em>communication</em> (one picture beats a paragraph).</p></div>
  <div class="card stack"><h2>Which chart for which PI</h2><div class="scrollx"><table class="tbl"><thead><tr><th>If the case asks about…</th><th>Sketch</th></tr></thead><tbody>
    ${[['Need to save and invest, time value of money, retirement, college','growth'],['Budgets, overhead, start-up costs, goals','pie'],['Insurance needs, risk management, ERM, fraud risk','riskmatrix'],['Types of investments, markets, where to put money','pyramid'],['Ownership types, choosing an institution, debt vs equity','tchart'],['Three or more options to choose between','decision'],['Corporate governance, compliance structure','org'],['Cash flow, financial statements, ratios','cashbars'],['Client service, controls, scams, "what happens if"','flow'],['Debt payoff, cost of credit, comparing costs','bars'],['Any solution: when it happens and how you measure it','timeline']].map(([q,id])=>`<tr><td class="small">${q}</td><td><a href="#charts-${id}">${esc(CHART[id].name)}</a></td></tr>`).join('')}</tbody></table></div></div>
  <a class="btn primary lg" href="#sketch">${icon('play')}Practice: 3-minute sketch drill</a>
  <div class="stack">${CHARTS.map(card).join('')}</div></div>`;
};
V.sketch=()=>{
  const cases=allCases(); if(!UI.sketch){ const c=pick(cases,1)[0]; UI.sketch={cid:c.id,stage:'ready'}; }
  const S0=UI.sketch; const c=caseById(S0.cid)||cases[0]; const sug=chartsFor(c);
  const checks=['Title states the takeaway','Uses at least two numbers from the case','The recommendation is highlighted','A stranger would get it in 5 seconds','You can explain it in one sentence'];
  return `<div class="wrap">${back('#charts','Charts')}${head('Sketch drill','Read the case summary, pick a chart, and sketch it on paper in 3 minutes, the way you would during prep.')}
  <div class="card stack"><span class="label">${esc(caseTitle(c))}</span><p class="small">${esc(c.situation)}</p><div class="chips">${c.pis.map(chipPI).join('')}</div>
    <p class="small"><strong>Suggested charts:</strong> ${sug.map(id=>`<a href="#charts-${id}">${esc(CHART[id].name)}</a>`).join(' · ')}</p>
    <div class="bigtimer" id="bigtimer" data-idle="180">${fmtTime(TIMER.endsAt&&TIMER.kind==='sketch'?TIMER.left():180)}</div>
    <div class="row" style="justify-content:center"><button class="btn primary lg" id="timer-btn" data-a="sketchGo">${TIMER.endsAt&&TIMER.kind==='sketch'?icon('stop')+'Stop':icon('play')+'Start 3 minutes'}</button><button class="btn" data-a="sketchNew">${icon('shuffle')}Different case</button></div></div>
  <div class="card stack"><h2>Check your sketch</h2>${checks.map((t,i)=>`<label class="row small"><input type="checkbox" data-in="sketchChk" data-i="${i}" ${S0['c'+i]?'checked':''}> ${esc(t)}</label>`).join('')}
    <p class="small muted">Then compare with the example drawing on the chart's page. Practice each chart type at least once before regionals.</p></div></div>`;
};

/* ---------- PI DEEP DIVES ---------- */
V.deep=()=>{
  const q=(UI.deepq||'').toLowerCase(); const t=UI.deepTier||'all';
  const list=D.deep.filter(d=>{ const p=PI[d.pi]; return (t==='all'||String(p.tier)===t)&&(!q||(d.pi+' '+p.pi+' '+d.plain).toLowerCase().includes(q)); });
  const past=new Set(['CR:012','FI:270','FI:077','FI:337','FI:571','EN:039','BL:003','FI:354','FI:579','FI:106','OP:024','FI:336','FI:062','CR:007','CO:039','SM:075','EI:128']);
  return `<div class="wrap">${back('#learn','Learn')}${head('PI deep dives',`In-depth study notes for all ${D.deep.filter(d=>PI[d.pi].tier===2).length} Finance-cluster (Tier 2) PIs and the ${D.deep.filter(d=>PI[d.pi].tier===1).length} Tier 1 PIs FTDM cases use most. Each one: what to say, must-know terms, how to apply it to a client, real-world proof with sources, the exam trap, the chart to sketch, and where to learn more.`)}
  <div class="row"><input class="input" style="max-width:320px" placeholder="Search (e.g. insurance, governance)" value="${esc(UI.deepq||'')}" data-in="deepq"><div class="chips">${[['all','All'],['2','Tier 2'],['1','Tier 1']].map(([k,l])=>`<button class="chip ${t===k?'on':''}" data-a="deepTier" data-v="${k}">${l}</button>`).join('')}</div></div>
  <div class="stack">${list.map(d=>{ const s=piStats(d.pi); return `<a class="list-link" href="#pi-${d.pi}"><span class="min0">${chipPI(d.pi)} <strong class="small">${esc(PI[d.pi].pi)}</strong><br><span class="small muted">${esc(d.plain.slice(0,120))}${d.plain.length>120?'…':''}</span></span><span class="stack-s" style="align-items:flex-end">${past.has(d.pi)?'<span class="chip acc">Past district PI</span>':''}${piHits(d.pi)?`<span class="tiny faint">${piHits(d.pi)}/${NEXAMS} exams</span>`:''}${s.n?`<span class="chip ${s.c/s.n>=.8?'good':s.c/s.n>=.65?'warn':'bad'}">${pct(s.c,s.n)}%</span>`:''}</span></a>`; }).join('')}</div></div>`;
};
V.pi=(code)=>{
  const p=PI[code]; if(!p) return V.deep(); const d=DEEP[code];
  const qs=D.questions.filter(q=>q.pi===code); const cards=D.cards.filter(c=>LESSON[c.lesson]?.pis.includes(code)).slice(0,6); const tp=D.talk.filter(t=>t.pis.includes(code));
  const cs=allCases().filter(c=>c.pis.includes(code)); const s=piStats(code);
  return `<div class="wrap">${back('#deep','All deep dives')}
  <div class="pagehead"><div class="row" style="justify-content:flex-start">${chipPI(code)}<span class="chip">Tier ${p.tier} · ${esc(areaShort(p.area))}</span>${piHits(code)?`<span class="chip acc">On ${piHits(code)} of ${NEXAMS} past exams</span>`:''}<span class="chip">${esc({PQ:'Prerequisite',CS:'Career-sustaining',SP:'Specialist'}[p.level]||p.level)}</span>${s.n?`<span class="chip ${s.c/s.n>=.8?'good':'warn'}">Your accuracy ${pct(s.c,s.n)}%</span>`:''}</div><h1>${esc(p.pi)}</h1></div>
  ${d?`<div class="card stack"><span class="label">Say it to a judge</span><p style="font-size:1.05rem">${esc(d.plain)}</p>${CL.tts?`<button class="btn sm" style="align-self:flex-start" data-a="speakText" data-t="${esc(d.plain)}">${icon('vol')}Hear it</button>`:''}</div>
  <div class="grid2"><div class="card stack-s"><span class="label">Must-know</span><ul class="model small">${d.key.map(k=>`<li>${esc(k)}</li>`).join('')}</ul></div>
    <div class="card stack-s"><span class="label">Apply it to the client</span><p class="small">${esc(d.apply)}</p>${d.trap?`<div class="warn-note small"><strong>Exam trap:</strong> ${esc(d.trap)}</div>`:''}</div></div>
  <div class="card stack-s"><span class="label">Real-world proof</span><ul class="model small">${d.proof.map(k=>`<li>${esc(k)}</li>`).join('')}</ul></div>
  ${d.chart?`<div class="card row between"><div class="min0"><span class="label">Chart to sketch</span><p class="small">${esc(d.chart)}</p></div><a class="btn sm" href="#charts">How to draw it</a></div>`:''}
  ${d.learn.length?`<div class="card stack-s"><span class="label">Learn more</span><div class="stack-s">${d.learn.map(([l,u])=>`<a class="small" href="${esc(u)}" target="_blank" rel="noopener">${esc(l)} ↗</a>`).join('')}</div></div>`:''}`
  :`<div class="blue-note small">No deep dive for this Tier ${p.tier} PI yet. Use the related cards and questions below.</div>`}
  ${tp.length?`<details class="card"><summary>Talking points (${tp.length})</summary><div class="stack">${tp.map(t=>`<div class="tp"><strong class="small">${esc(t.title)}</strong><div class="say">${esc(t.say)}</div><span class="src">${esc(t.source)}${t.asof?' · as of '+esc(t.asof):''}</span></div>`).join('')}</div></details>`:''}
  ${cards.length?`<details class="card"><summary>Related flashcards (${cards.length})</summary><div class="stack-s">${cards.map(c=>`<p class="small"><strong>${esc(c.t)}:</strong> ${esc(c.d)}</p>`).join('')}</div></details>`:''}
  <div class="row">${qs.length?`<a class="btn primary" href="#quiz-pis.${code}">Practice ${qs.length} question${qs.length>1?'s':''}</a>`:''}${cs.map(c=>`<a class="btn sm" href="#case-${c.id}">Case: ${esc(caseTitle(c))}</a>`).join('')}</div></div>`;
};

/* ---------- LIBRARY ---------- */
V.library=()=>{
  const groups=[
   ['Official DECA materials',[['DECA FTDM event page (guidelines, sample cases, sample exam)','https://www.deca.org/compete/financial-services-team-decision-making'],['DECA Direct: role-play and competition advice','https://www.decadirect.org'],['MBA Research: the LAPs (Learning Activity Packages) cited in DECA exam answer keys; ask your advisor if your chapter has them','https://www.mbaresearch.org']]],
   ['Personal finance (most FTDM district cases)',[['SEC Investor.gov: investing basics, compound interest calculator, fraud alerts','https://www.investor.gov'],['CFPB: credit, debt, budgeting, consumer rights','https://www.consumerfinance.gov'],['FDIC Money Smart and deposit insurance','https://www.fdic.gov'],['Next Gen Personal Finance: free lessons and case studies','https://www.ngpf.org'],['Federal Student Aid: FAFSA and loans','https://studentaid.gov'],['Social Security Administration: benefits, calculators','https://www.ssa.gov'],['Insurance Information Institute: insurance explained','https://www.iii.org'],['TreasuryDirect: T-bills and savings bonds','https://www.treasurydirect.gov']]],
   ['Markets, economy and companies',[['Federal Reserve: rates and monetary policy','https://www.federalreserve.gov'],['Bureau of Labor Statistics: inflation (CPI) and jobs','https://www.bls.gov'],['SEC EDGAR: 10-K, 10-Q and 8-K filings','https://www.sec.gov/edgar'],['Federal Reserve History: how banking and crises evolved','https://www.federalreservehistory.org']]],
   ['Business, risk and governance',[['U.S. Small Business Administration: start-up costs, loans, ownership types','https://www.sba.gov'],['IRS: business structures, tax rules and limits','https://www.irs.gov'],['COSO: internal control and ERM frameworks','https://www.coso.org'],['FINRA and BrokerCheck: broker rules and records','https://www.finra.org'],['FinCEN: anti-money laundering rules','https://www.fincen.gov']]],
   ['Careers',[['BLS Occupational Outlook Handbook: pay and outlook for finance jobs','https://www.bls.gov/ooh'],['CFP Board: becoming a financial planner','https://www.cfp.net']]],
  ];
  return `<div class="wrap">${back('#learn','Learn')}${head('Where to learn more','Trustworthy sources to go deeper on anything FTDM asks about, and to find fresh real-world facts before competition. Links open in a new tab.')}
  ${groups.map(([g,ls])=>`<div class="card stack-s"><h2>${esc(g)}</h2>${ls.map(([l,u])=>`<a class="small" href="${u}" target="_blank" rel="noopener">${esc(l)} ↗</a>`).join('')}</div>`).join('')}
  <div class="blue-note small"><strong>Before regionals:</strong> re-check the time-sensitive numbers in Talking points (Fed rate, inflation, savings and mortgage rates). The Fed meets Dec. 8-9, 2026, and the next CPI report comes out Dec. 10.</div></div>`;
};

/* ---------- actions & inputs for part 3 ---------- */
Object.assign(A,{
  deepTier(el){ UI.deepTier=el.dataset.v; render(); },
  goPI(el){ location.hash='#pi-'+el.dataset.pi; },
  sketchGo(){ if(TIMER.endsAt&&TIMER.kind==='sketch'){ TIMER.stopLocal(); return; } TIMER.startLocal('sketch',null,180); today().sketch=1; save(); render(); },
  sketchNew(){ TIMER.stopLocal(true); UI.sketch=null; render(); },
});
Object.assign(IN,{
  deepq(el){ UI.deepq=el.value; clearTimeout(UI.dqT); UI.dqT=setTimeout(()=>{ render(); const i=$('[data-in="deepq"]'); if(i){ i.focus(); i.setSelectionRange(i.value.length,i.value.length);} },250); },
  sketchChk(el){ UI.sketch['c'+el.dataset.i]=el.checked; },
});
