"""Bake data/ + app/ into one self-contained page: ftdm-ace.html

Run after build_data.py:   python3 build_app.py
The output is written for the claude.ai Artifact publisher (no <html>/<head>/<body> tags; the
publisher adds them). It also opens directly in a browser for local testing.
"""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
def rd(*p):
    with open(os.path.join(ROOT, *p), encoding='utf-8') as f: return f.read()
def js(name):
    with open(os.path.join(ROOT, 'data', name), encoding='utf-8') as f: return json.load(f)

lessons = js('lessons.json'); cases = js('cases.json')
data = {
    'pis': js('pis.json'), 'lessons': lessons['lessons'], 'cards': lessons['cards'],
    'questions': js('questions.json'), 'cases': cases, 'talk': js('talking.json'), 'deep': js('deepdives.json'), 'hub': js('hub.json'),
}
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
script = '\n'.join(rd('app', f) for f in ['core.js', 'views1.js', 'views2.js', 'views3.js', 'views4.js', 'boot.js']).replace('</script', '<\\/script')

page = f'''<title>FTDM Ace</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="DECA Financial Services Team Decision Making study app: daily plan, spaced-repetition flashcards, blueprint-weighted mock exams, roleplay drills and partner sync.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=IBM+Plex+Mono:wght@500;600&family=Inter:wght@400;500;600;700&display=swap">
<style>
{rd('app', 'style.css')}
</style>
<div class="app">
  <nav class="rail" id="rail" aria-label="Sections"></nav>
  <div style="flex:1;min-width:0">
    <header class="topbar"><a class="brand" href="#today"><span class="mark">FT</span>FTDM Ace</a><span class="sp"></span><div class="row nowrap" id="topright"></div></header>
    <main class="main" id="main" tabindex="-1"><div class="wrap"><p class="muted">Loading your study plan…</p></div></main>
  </div>
</div>
<nav class="tabs" id="tabs" aria-label="Sections"></nav>
<script id="ftdm-data" type="application/json">{blob}</script>
<script>
{script}
</script>
'''
out = os.path.join(ROOT, 'ftdm-ace.html')
with open(out, 'w', encoding='utf-8') as f: f.write(page)
# A local preview copy with a full document wrapper, for opening straight from disk.
with open(os.path.join(ROOT, 'preview.html'), 'w', encoding='utf-8') as f:
    f.write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body style="margin:0">' + page + '</body></html>')
print('wrote', out, round(os.path.getsize(out) / 1024), 'KB')
