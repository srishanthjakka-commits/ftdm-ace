# FTDM Ace

Study app for DECA Financial Services Team Decision Making (FTDM), 2026-27.
Runs as a claude.ai Artifact (cloud sync, partner features, AI judge). You can also open
`preview.html` straight from disk to study offline; progress then stays in that browser only.

Not affiliated with or endorsed by DECA Inc. Performance indicator codes in `data/pis.json`
come from DECA's published 2026-27 Finance PI list.

## Rebuild after editing content

```
python build_data.py     # src/*.py -> data/*.json (checks PIs, duplicates, 5 PIs per case)
python build_app.py      # data/ + app/ -> ftdm-ace.html (and preview.html for local testing)
```

Then ask Claude to republish `ftdm-ace.html` to the same artifact URL.

## Where things live

| What | File |
|---|---|
| Lessons and flashcards | `src/lessons_a.py`, `src/lessons_b.py` |
| Exam questions (correct answer first; the app shuffles) | `src/questions_a.py` … `src/questions_e.py` |
| Business cases + drills (original set) | `src/cases.py` |
| Client-advising cases (modeled on 2024-26 district format) | `src/cases_b.py` |
| Client-style 60-second drills | `src/drills_b.py` |
| Real-world talking points with sources | `src/talking.py` (re-check items with an `asof` date before each competition) |
| Exam blueprint, scheduling, plan, sync | `app/core.js` |
| PI deep dives with official sources | `src/deepdives.py` |
| Screens (charts, deep dives, library in views3) | `app/views1.js`, `app/views2.js`, `app/views3.js`, `app/style.css` |

Blueprint: DECA Guide 2026-27, p. 39 (Finance: district / association / ICDC).
Rubric and format: DECA Guide 2026-27 pp. 53-54 and the 2026 FTDM district event.
All questions and cases are original; nothing is copied from DECA or MBA Research.

## Partner sync

Invite your partner from the artifact's Share menu by email as an **Editor** and keep public-link
sharing off (on personal plans, invited editors can save only while the link is off). Each of you
then sees the other's progress on the Team page, shares a live prep planner on every case, and can
start timers on both screens.
