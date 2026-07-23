<!--
SPEC 4 of 7 · COLLECTION TECHNIQUES
Audience: engineer + the collection job (src/collect.py).
Defines WHERE source documents come from and HOW they are downloaded into kdb/.
This is the "input side" — distillation is a separate spec. Fill every {{placeholder}}.
-->

# Collection Techniques — {{ORACLE_NAME}}

## What lands in kdb/
Raw source documents drawn from the Oracle's canon (see oracle.md): PDFs and
`.md` files listing URLs, plus any pages fetched from those URLs.

## Source inventory
List the concrete sources to collect. Keep in sync with oracle.md's canon.
| Source | Type | Location / URL | Refresh | Notes |
| --- | --- | --- | --- | --- |
| {{name}} | {{pdf / url / feed}} | {{path or link}} | {{once / daily / weekly}} | {{}} |
| {{name}} | {{}} | {{}} | {{}} | {{}} |

## How to download
- **PDFs:** {{copy from a folder / download from URL}} → save under `kdb/pdfs/`.
- **URL lists:** parse `.md` files under `kdb/links/`, fetch each URL, extract readable
  article text (strip nav/ads/boilerplate), save as `kdb/fetched/<slug>.md`.
- **JS-heavy pages:** {{use a headless browser / skip and log}} — plain fetch won't render them.
- **Feeds/APIs (optional):** {{endpoint, auth via .env, polling cadence}}.

## Filtering at collection time
- **Accept only:** sources consistent with the Oracle's canon.
- **Reject/skip:** {{the "explicitly rejected" list from oracle.md}} — don't even store them.
- **Robots/ToS:** respect robots.txt and site terms; {{rate limit N req/min}}.

## Dedup & change detection
- Hash each collected document; store the hash in `.state/manifest.json`.
- Skip re-downloading unchanged sources; re-fetch URLs on their refresh cadence.
- Record every collected item with its source URL/path for provenance.

## Freshness policy
- **Evergreen sources:** {{fetch once}}.
- **Time-sensitive sources:** {{re-fetch daily/weekly; stamp collected_on}}.

## Failure handling
- On fetch failure: {{retry N times, then log to progress.md run log and continue}}.
- Never let one bad source abort the whole collection run.

## Output layout in kdb/
```
kdb/
├── pdfs/            raw PDFs
├── links/           .md files listing URLs to fetch
└── fetched/         cleaned text pulled from those URLs
```
