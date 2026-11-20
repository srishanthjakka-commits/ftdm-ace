"""Rebuild the JSON in data/ from the Python content files in src/.

Run:  python3 build_data.py      (Windows: py build_data.py)
Then: python3 build_app.py       to bake the new data into ftdm-ace.html
"""
import json, sys, os, collections
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
DATA = os.path.join(ROOT, 'data')

def load(name):
    ns = {}
    # utf-8 explicitly: the content uses curly quotes and symbols, and Windows defaults to cp1252.
    with open(os.path.join(SRC, name), encoding='utf-8') as f:
        exec(f.read(), ns)
    return ns

def dump(obj, name):
    with open(os.path.join(DATA, name), 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, separators=(',', ':'))

with open(os.path.join(DATA, 'pis.json'), encoding='utf-8') as f:
    pis = {p['code']: p for p in json.load(f)}
AREA_FIX = {'Communication Skills': 'Communications'}
def area_of(code): a = pis[code]['area']; return AREA_FIX.get(a, a)

errors = []
lessons = load('lessons_a.py')['L'] + load('lessons_b.py')['L']
cards = []
for L in lessons:
    for c in L['pis']:
        if c not in pis: errors.append(f"lesson {L['id']} bad PI {c}")
    for i, (t, d, x) in enumerate(L['cards']):
        cards.append({'id': f"{L['id']}-{i}", 'lesson': L['id'], 't': t, 'd': d, 'x': x})
    L['cards'] = [f"{L['id']}-{i}" for i in range(len(L['cards']))]
    L['area'] = AREA_FIX.get(L['area'], L['area'])

qs = []
seen = set()
for f in ['questions_a.py', 'questions_b.py', 'questions_c.py', 'questions_d.py', 'questions_e.py']:
    for pi, stem, opts, exp in load(f)['Q']:
        if pi not in pis: errors.append(f"bad PI {pi} in {stem[:40]}")
        if len(opts) != 4 or len(set(opts)) != 4: errors.append(f"options issue: {stem[:50]}")
        if stem in seen: errors.append(f"duplicate: {stem[:50]}")
        seen.add(stem)
        qs.append({'id': f"q{len(qs)+1}", 'pi': pi, 'area': area_of(pi) if pi in pis else '?', 'q': stem, 'o': opts, 'e': exp})

# map each question to a lesson by PI (first lesson listing it), else by area
pi2lesson = {}
for L in lessons:
    for c in L['pis']: pi2lesson.setdefault(c, L['id'])
area2lesson = {}
for L in lessons: area2lesson.setdefault(L['area'], L['id'])
for x in qs:
    x['lesson'] = pi2lesson.get(x['pi']) or area2lesson.get(x['area']) or 'comm-pd'

cs = load('cases.py')
cb = load('cases_b.py')
db = load('drills_b.py')
for c in cs['CASES']: c.setdefault('style', 'business')
for d in cs['DRILLS']: d.setdefault('style', 'business')
all_cases = cb['CASES'] + cs['CASES']
all_drills = db['DRILLS'] + cs['DRILLS']
ids = collections.Counter(c['id'] for c in all_cases + all_drills)
for k, n in ids.items():
    if n > 1: errors.append(f"duplicate case/drill id {k}")
for c in all_cases + all_drills:
    for p in c['pis']:
        if p not in pis: errors.append(f"case {c['id']} bad PI {p}")
for c in all_cases:
    if len(c['pis']) != 5: errors.append(f"case {c['id']} has {len(c['pis'])} PIs (2026-27 TDM cases list 5)")

tns = load('talking.py')
with open(os.path.join(SRC, 'talking_b.py'), encoding='utf-8') as f:
    exec(f.read(), tns)   # more points + hub tags, run in the same namespace so ids continue
talk = tns['T']
deep = load('deepdives.py')['DD']

# Finance Hub: topics -> sub-topics, each tied to PIs, with judge questions and model answers.
hub = load('hub_a.py')['H'] + load('hub_b.py')['H'] + load('hub_c.py')['H']
subids = collections.Counter(s['id'] for tp in hub for s in tp['subs'])
for k, n in subids.items():
    if n > 1: errors.append(f'duplicate hub sub-topic id {k}')
if len({tp['id'] for tp in hub}) != len(hub): errors.append('duplicate hub topic id')
for tp in hub:
    for s in tp['subs']:
        for p in s['pis']:
            if p not in pis: errors.append(f"hub {s['id']} bad PI {p}")
        if len(s['qs']) < 2: errors.append(f"hub {s['id']} needs at least 2 judge questions")
        for fld in ('what', 'how', 'nums', 'real', 'traps', 'say'):
            if not s[fld]: errors.append(f"hub {s['id']} missing {fld}")
for x in talk:
    if not x.get('subs'): errors.append(f"talking point {x['id']} has no hub sub-topic")
    if not x.get('answers'): errors.append(f"talking point {x['id']} has no judge questions")
    for sid in x.get('subs', []):
        if sid not in subids: errors.append(f"talking point {x['id']} unknown hub sub-topic {sid}")
if len({x['title'] for x in talk}) != len(talk): errors.append('duplicate talking point title')
for x in deep:
    if x['pi'] not in pis: errors.append(f"deep dive bad PI {x['pi']}")
if len({x['pi'] for x in deep}) != len(deep): errors.append('duplicate deep dive')
t2missing = [c for c, p in pis.items() if p['tier'] == 2 and not any(x['pi'] == c for x in deep)]
if t2missing: errors.append(f'tier-2 PIs without a deep dive: {t2missing}')
for x in talk:
    for p in x['pis']:
        if p not in pis: errors.append(f"talking point {x['id']} bad PI {p}")

if errors:
    print('\n'.join(errors)); sys.exit(1)
dump({'lessons': lessons, 'cards': cards}, 'lessons.json')
dump(qs, 'questions.json')
dump({'cases': all_cases, 'drills': all_drills}, 'cases.json')
dump(talk, 'talking.json')
dump(deep, 'deepdives.json')
dump(hub, 'hub.json')
print(len(lessons), 'lessons', len(cards), 'cards', len(qs), 'questions', len(all_cases), 'cases', len(all_drills), 'drills', len(talk), 'talking points', len(deep), 'deep dives')
nsub = sum(len(tp['subs']) for tp in hub)
print('finance hub:', len(hub), 'topics', nsub, 'sub-topics', sum(len(s['qs']) for tp in hub for s in tp['subs']), 'judge questions')
hubpis = {p for tp in hub for s in tp['subs'] for p in s['pis']}
print('tier-2 PIs not in the hub:', [c for c, p in pis.items() if p['tier'] == 2 and c not in hubpis])
print('questions by area:', collections.Counter(x['area'] for x in qs).most_common())
t2 = [c for c, p in pis.items() if p['tier'] == 2]
missing = [c for c in t2 if not any(x['pi'] == c for x in qs)]
print('tier-2 PIs with no question:', missing)
for f in sorted(os.listdir(DATA)): print(f, os.path.getsize(os.path.join(DATA, f)))
