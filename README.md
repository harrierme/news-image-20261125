# The World in One Day — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/harrierme/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/harrierme/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper front page summing up the world's news of
Wednesday 25 November 2026. Entry for the make.fun competition
`news-image-20261125` (top 50 share $100).

## Run it

```sh
python3 main.py
```

## What it is

- **48 stories**: 4 illustrated leads, 12 illustrated medium cards and
  32 numbered briefs — every one happened, or was first reported, on
  25 November 2026. Sources and trust labels (CONFIRMED / REPORTED /
  CLAIM / OFFICIAL / FORECAST) are printed on the page.
- **World map** with numbered pins (1–16) matching the story numbers.
- **The day in UTC** timeline, **the day in numbers** strip and a
  **DATE CHECK** box listing big stories deliberately left out because
  they are from another day (e.g. the Huawei verdict, the Spotify
  outage, the Libya ship sinking, Pope Leo's October diagnosis).
- Every illustration is drawn with Pillow primitives. No photographs.

## Files

- `main.py` — the entry program (stdlib only): copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`).
- `render.py` — draws the page from `stories.py` with Pillow.
- `stories.py` — the 48 researched stories, numbers, timeline and
  date-check lists.
- `stories.md` — the research notes behind `stories.py`.
- `entry.png` — the rendered front page (1024×1024, under 1 MiB).
- `assets/fonts/` — DM Serif Display, Montserrat (variable) and Bebas
  Neue, all SIL Open Font License, bundled so the render is
  reproducible.

## Rebuild

```
python3 render.py        # writes entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # copies it to out/entry.png
```

## Research

Researched 25 Nov 2026 from Reuters, CNBC, ESA, CMSA, BusinessLine,
The Germany Eye and others. See `stories.md` for the per-item sources
and the DATE CHECK list.

---

<sub>Entered on [make.fun](https://make.fun/?ref=efmrhagc&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
