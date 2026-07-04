# Batch Runs

> **OpenOwls SDD** — Living operational document. Update this file whenever a batch job is added, changed, or its latest run status changes.
> Captures every scheduled / batch process the system runs and the state of the most recent runs.
> Claude Code reads this to understand what runs unattended (e.g. nightly jobs) and must never assume a batch job's behavior without checking here.

## Batch Overview
<!-- One or two sentences: what batch / scheduled processing does this system rely on? -->

_e.g. The system runs several unattended jobs overnight — data syncs, report generation, and cleanup — outside of any user request._

---

## Batch Job Inventory
<!-- Every batch job the system defines. One row per job. -->

| Job Name | Purpose | Schedule | Trigger | Owner |
|----------|---------|----------|---------|-------|
| _e.g. nightly-report_ | _Generates the daily summary report_ | _e.g. 02:00 UTC daily_ | _e.g. cron_ | _e.g. Student A_ |
| _Add more_ | | | | |

---

## Schedule
<!-- When does each job run? Use a consistent timezone (e.g. UTC). -->

| Time (UTC) | Job | Frequency |
|------------|-----|-----------|
| _e.g. 02:00_ | _nightly-report_ | _Daily_ |
| _Add more_ | | |

---

## Currently Active / Latest Runs
<!-- The most recent run of each job. This is the "current state" — keep it up to date. -->

| Job | Last Run (UTC) | Status | Duration | Records Processed | Notes |
|-----|----------------|--------|----------|-------------------|-------|
| _e.g. nightly-report_ | _YYYY-MM-DD 02:00_ | _Success / Failed / Running_ | _e.g. 3m 12s_ | _e.g. 1,240_ | |
| _Add more_ | | | | | |

---

## Run Log
<!-- Brief history of notable runs. Most recent at the top. -->

| Date (UTC) | Job | Status | Notes |
|------------|-----|--------|-------|
| YYYY-MM-DD | _job-name_ | _Success / Failed_ | _Initial entry_ |

---

## Job Dependencies
<!-- Does any job depend on another finishing first? Document the order. -->

- _e.g. `nightly-report` must run after `data-sync` completes_

---

## Failure Handling & Alerts
<!-- What happens when a batch job fails? Who is notified and how? -->

| Concern | Decision |
|---------|----------|
| Retry policy | _e.g. Retry once after 10 minutes, then alert_ |
| Alerting | _e.g. Email the on-call student on failure_ |
| Manual recovery | _e.g. Re-run via the manual trigger below after fixing the cause_ |

---

## Manual Trigger
<!-- How to run a batch job by hand (outside its schedule) for testing or recovery. -->

```bash
# e.g. python -m app.batch.nightly_report
```
