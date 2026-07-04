# Batch Runs — Suite-Wide

> **OpenOwls SDD — Suite Edition.** Shared, system-wide, operational. Living document — update whenever a batch job is added, changed, or its latest run status changes.
> Captures every scheduled / batch process across the **whole suite** and the state of the most recent runs, noting which package owns each job.
> Claude Code reads this to understand what runs unattended (e.g. nightly jobs) and which package is responsible for each. There is **one** batchrun file for the suite — it lives here at the root, never inside a package.

## Batch Overview
<!-- One or two sentences: what batch / scheduled processing does the suite rely on, and where does it run? -->

_e.g. Nightly jobs are triggered from the top `app` package and orchestrate work down through `middleware` and `core`._

---

## Batch Job Inventory
<!-- Every batch job in the suite. One row per job. Name the owning package. -->

| Job Name | Owning Package | Purpose | Schedule | Trigger |
|----------|----------------|---------|----------|---------|
| _e.g. nightly-report_ | _e.g. app_ | _Generates the daily summary_ | _e.g. 02:00 UTC daily_ | _e.g. cron_ |
| _Add more_ | | | | |

---

## Schedule
<!-- When does each job run? Use a consistent timezone (e.g. UTC). -->

| Time (UTC) | Job | Owning Package | Frequency |
|------------|-----|----------------|-----------|
| _e.g. 02:00_ | _nightly-report_ | _app_ | _Daily_ |
| _Add more_ | | | |

---

## Currently Active / Latest Runs
<!-- The most recent run of each job. This is the "current state" — keep it up to date. -->

| Job | Owning Package | Last Run (UTC) | Status | Duration | Notes |
|-----|----------------|----------------|--------|----------|-------|
| _e.g. nightly-report_ | _app_ | _YYYY-MM-DD 02:00_ | _Success / Failed / Running_ | _e.g. 3m 12s_ | |
| _Add more_ | | | | | |

---

## Run Log
<!-- Brief history of notable runs. Most recent at the top. -->

| Date (UTC) | Job | Package | Status | Notes |
|------------|-----|---------|--------|-------|
| YYYY-MM-DD | _job-name_ | — | _Success / Failed_ | _Initial entry_ |

---

## Cross-Package Job Dependencies
<!-- Does a job depend on another (possibly in a different package) finishing first? -->

- _e.g. `nightly-report` (app) must run after `data-sync` (middleware) completes_

---

## Failure Handling & Alerts
<!-- What happens when a batch job fails? Who is notified and how? -->

| Concern | Decision |
|---------|----------|
| Retry policy | _e.g. Retry once after 10 minutes, then alert_ |
| Alerting | _e.g. Email the on-call student on failure_ |
| Manual recovery | _e.g. Re-run from the owning package's venv after fixing the cause_ |

---

## Manual Trigger
<!-- How to run a batch job by hand. Remember: activate the OWNING package's venv first. -->

```bash
# cd <owning-package> && source .venv/bin/activate
# e.g. python -m app.batch.nightly_report
```
