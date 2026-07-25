# OpenOwls SIT-KB-AWP — Getting Started Guide

### Self-Improving Target-oriented Knowledge-Based Agent Workflow Process
#### *the full-scale extension of SD-KDP (Spec-Driven Knowledge Distillation Process)*

SIT-KB-AWP is a method for building an AI knowledge workflow that **improves
itself against a declared target**. You write a small set of Markdown specs; a
team of simple agents executes them — collecting sources, distilling them
through a declared lens, serving answers, and critiquing its own performance —
and every round, measured feedback flows back into the specs.

The name says the whole design. **Self-Improving:** the gap between measured
performance and the target is an error signal a critic converts into proposed
spec changes. **Target-oriented:** the workflow is organized around KPMs, not
around a corpus — collection and distillation exist to close a measured gap.
**Knowledge-Based:** what improves is never the model's weights; it is the
knowledge base and the specs — inspectable, versioned, reversible artifacts.
**Agent Workflow Process:** the deliverable is a repeatable pipeline of
cooperating agents, of which the chatbot (if any) is just the serving stage.

## Method lineage: from SDD, through SD-KDP

Spec-Driven Development (SDD) builds *software*: specs first, in version
control, used to brief the AI. **SD-KDP** adapted that discipline to building
*distilled knowledge*: declare an **Oracle** — a perspective plus its trusted
canon — and let a nightly pipeline collect, distill, and serve it in the
Oracle's voice. SIT-KB-AWP keeps everything that works in SD-KDP and adds
what a larger project needs: the target, the feedback loop, the agent roster,
and an explicit model of time.

## Which version do I need?

The SD-KDP family has three versions:

**SD-KDP Lite** (four merged specs: overview, oracle, pipeline, loop) is the
right start for a static corpus, a single maintainer, and a simple human
feedback loop — a course quiz bank, a personal knowledge oracle. It runs from
four Markdown files and a cron job.

**SD-KDP** (the original — eight specs, one per concern, including
`progress_measure.md` for the target, per-run checks, and feedback verdicts)
is the reference version: same single-maintainer scope as Lite, but with
collection, distillation, the output contract, batch, and measures each as
its own file. Graduate here from Lite when the merged files get crowded.

**SIT-KB-AWP** (this guide — ten specs plus the agent roster) is for projects
that hit any of: sources arriving on the world's schedule needing dated,
append-only outputs; judgments scored by delayed ground truth (verdict
windows); two human roles needing approval routing; or a critic agent
proposing spec changes.

The graduation rule for coming here: **a spec gains a second owner or a
second clock.** Until then, stay with Lite or the original.

---

## The three layers

SIT-KB-AWP is easiest to hold in mind as three distinct layers. Confusing them is the
most common design error.

**Human roles** own and approve specs. There are two: the **domain expert**
(the business-owner role in SDD terms — owns the goal: what the workflow is
for, whose lens it uses, what the domain's facts are, what "good" measures)
and the **agent developer** (the architect/engineer role — owns the means:
how sources are collected, how distillation works, how the batch runs).

**Spec files** are the contracts. Ten small Markdown files, tracked in git,
that fully determine the system's behavior. Code merely executes them.

**Runtime agents** execute the specs. The collector, distiller, answerer, and
critic are processes; each reads its briefing from the specs. Note what is
*not* on this list: the **Oracle is not an agent**. It is a declared artifact
— the character sheet the distiller and answerer adopt, not a player.

In SDD, humans execute the documents. Here, agents do — which is why the
ownership table (below) has a third column SDD's version doesn't need.

## The Target

`target.md` is the organizing principle: a one-sentence target statement plus
KPMs. **Regression KPMs** run automatically after every build against a fixed
eval set (seeded from the Oracle's key questions) — they are the workflow's
unit tests, so every spec change shows up as a KPM move. **Live KPMs** score
real usage via the feedback log — they reveal what the eval set is missing,
and feed new questions into it. The KPM trend over rounds, logged in
`progress.md`, *is* the self-improvement curve. If it isn't rising, the loop
is broken — and that itself is a finding.

## The Oracle

An Oracle is the declared perspective and canon the workflow aligns to: a
person (Warren Buffett), an institution (the Fed), a curated site — or simply
a *scope*, like one professor's course, where the bias is the boundary of the
canon itself. A generic LLM averages every viewpoint into bland consensus;
SD-KDP deliberately commits to one lens, and declares that bias in version
control where it is transparent rather than hidden.

In SIT-KB-AWP the Oracle is explicitly the **means**, not the end: the target defines
success; the Oracle defines *whose framework* is used to reach it. This
matters most when the workflow outputs judgments — "over-reaction,"
"too difficult" — which are meaningless except relative to a declared lens.

## Two tiers, two verbs

Knowledge has a half-life, and a single corpus folder hides two opposite
lifecycles. The **durable tier** (`kdb/canon/`) is a *library*: the Oracle's
methodology and reference material — fetch once, refresh slowly, value grows
with curation. The **episodic tier** (`kdb/inbox/`) is a *mailroom*: dated
material arriving on the world's schedule — this quarter's filings, this
week's lecture — analyzed once, value decaying after.

Each tier gets its own distillation verb. Canon is **summarized** into
`wiki/` — undated reference articles, updated in place. Inbox material is
**applied**: analyzed *through* the distilled wiki (the lens is an input, not
a sibling) into `assessments/` — dated, append-only snapshots that double as
the system's track record. Every pipeline stage — refresh policy, processing
verb, output location, reprocess trigger, indexing, retention — makes the
opposite choice for each tier. If the specs stay silent, the scripts choose
one policy for both, and the failure is quiet: the worst case is an episode
summarized into the wiki, where it becomes undated "knowledge" confidently
retrieved, stale, years later. A static-corpus project is just the degenerate
case of an empty inbox — the model still holds.

## The three clocks

The temporal profile in `domain_knowledge.md` declares the domain's facts
about time, one row per information type, three clocks per row:

1. **Arrival** — how often new information appears (lectures: weekly in
   semester; earnings: quarterly per company, pre-announced). Drives
   collection scheduling.
2. **Validity** — how long it stays true (methodology: years; a filing:
   a dated snapshot forever). Drives tier routing, date-stamping, retrieval
   filtering, retention.
3. **Verdict** — when ground truth arrives to score a judgment (a market
   reaction resolves in 2 days–1 week; a quiz bank when the instructor
   reviews it). Drives the feedback loop's scoring schedule — and is really a
   parameter of the *target*: a 2-day verdict window and a 3-month one define
   different systems.

Downstream specs *derive* their timing behavior from this table rather than
hard-coding it. The general principle: **information expires on its own
clock; the Oracle's lens is the slow-moving part** — it has seen enough
episodes that one more rarely changes it. (Slow-moving, not immortal: the
lens has a drift policy too.)

## The agent roster

| Agent | Briefed by | Does |
| --- | --- | --- |
| **Monitor** | collection_techniques.md | watches for upcoming episodic events; generates the inbox work list |
| **Collector** | collection_techniques.md | fetches canon (slow clock) and inbox (event clock) sources, with provenance |
| **Distiller** | distillation + output_format + oracle | SUMMARIZE canon → wiki; APPLY wiki lens to inbox → assessments |
| **Answerer** | serving.md + oracle | serves users in the Oracle's voice, grounded only in wiki/assessments; **logs a structured exchange record** |
| **Scorer** | target.md | runs the eval set; scores judgments when verdict windows elapse; appends the track record |
| **Critic** | feedback_loop.md | reads feedback + KPM trend; produces *proposals* — spec diffs, new sources, re-run orders, eval-set additions |
| **Orchestrator** | batch_process.md | sequences the runs: nightly, event-driven, verdict, critic |

The answerer's exchange log deserves emphasis: without a structured record of
question → retrieved → answer → sources, feedback has nothing to attach to,
and the loop cannot close. If an external app is the front-end (a quiz game
ingesting JSON), the serving contract collapses to "produce valid artifacts,"
and the app's review session is the exchange record.

## The self-improvement loop, and who approves what

The loop: serve → collect feedback (human verdicts + delayed outcome data) →
critic finds patterns → critic proposes → **approval routed by ownership** →
specs change → next round → KPMs move → repeat.

Two design rules keep it honest. First, feedback carries a **controlled
verdict vocabulary**, because each failure type routes to a different spec:
`missing-knowledge` → collection; `wrong-vs-source` → distillation
faithfulness; `not-retrieved` → indexing/serving; `off-voice` → oracle
adherence; `mis-calibrated` → the calibration rubric. Routing failures to
specs is the critic's entire job — pattern-level, not case-level.

Second, **the ownership table is also the approval-routing table**:

| Spec | Owner | Runtime consumer | Critic proposals need |
| --- | --- | --- | --- |
| overview.md | domain expert | all (context) | expert approval |
| target.md | domain expert | scorer, critic | expert approval |
| domain_knowledge.md | domain expert | distiller, critic | expert approval |
| oracle.md | domain expert | distiller, answerer | expert approval |
| collection_techniques.md | agent developer | monitor, collector | developer (low ceremony) |
| distillation_techniques.md | agent developer | distiller | developer (low ceremony) |
| output_format.md | shared (§A expert / §B developer) | distiller, indexer | per section |
| serving.md | shared | answerer | per section |
| feedback_loop.md | shared | critic | per section |
| batch_process.md | agent developer | orchestrator | developer (low ceremony) |

Agents may *propose* against any spec; approval authority follows ownership.
That distinction is what keeps "self-improving" from drifting into
"self-redefining" — the critic can improve the *means* freely but must not
quietly rewrite the *goal*, for the same reason QA in SDD can file bugs
against requirements but can't rewrite them.

---

## File structure

```
sit-kb-awp/
├── CLAUDE.md / progress.md        entry point + session memory
├── ai_specs/                      ten specs — the source of truth, in git
├── kdb/canon/    kdb/inbox/       library / mailroom   (contents gitignored)
├── wiki/                          distilled lens — undated, updated in place
├── assessments/                   applied analyses — dated, append-only
└── src/                           the agents (contents in git)
```

`kdb/`, `wiki/`, and `assessments/` contents change every run — they are data,
not code — so they are gitignored (folders kept via `.gitkeep`) and backed up
by `src/backup.py`. The specs and code in git are everything needed to
regenerate them from scratch. The one exception in spirit: `assessments/` and
the track record are *history* — backed up with long retention, never
regenerated-over, because overwriting old judgments destroys the very thing
the calibration KPMs score.

## How to start a project

1. **Declare the target** (`target.md`): the one-sentence target statement,
   the KPMs, the verdict windows. Target before lens.
2. **Declare the Oracle** (`oracle.md`): lens, canon, voice, key questions —
   which seed the eval set. Lens before pipeline.
3. **Write the temporal profile** (`domain_knowledge.md`): one row per
   information type, three clocks per row, plus terminology and rules.
4. **Fill the means-side specs** (collection, distillation, output_format,
   serving, feedback_loop, batch_process) and implement `src/`.
5. **Run once by hand**; score against the eval set; fix specs, not outputs,
   until the regression KPMs pass.
6. **Schedule it** (nightly + event-driven) and open the feedback log.
7. **Run the critic** after feedback accumulates; approve proposals per the
   ownership table; watch the KPM trend in `progress.md` across rounds.

## Golden rules

1. **Fix specifications, not outputs** — a hand-edited artifact is regenerated
   away on the next run.
2. **Target first, Oracle as lens** — success is the KPMs; the Oracle is how
   you get there.
3. **Preserve the Oracle's voice** — distill-of-distill drifts toward
   consensus; reject drift explicitly.
4. **Respect the tiers** — never summarize the inbox into the wiki; never
   overwrite an assessment.
5. **Derive timing from the temporal profile** — no hard-coded clocks in code.
6. **Trace every claim to a source; date every episodic claim** ("as of…").
7. **Log the exchange, or the loop can't close** — feedback needs an anchor.
8. **Approval follows ownership** — improve the means freely; change the goal
   only with the domain expert's sign-off.
9. **Keep data folders out of git; back them up; keep the track record forever.**
10. **Update progress.md every session and every run** — the KPM trend is the
    proof of self-improvement.

---

## Worked examples in one paragraph each

**Course review (static corpus, human verdicts).** Target: a question bank per
lecture, ≥80% accepted unedited, all traceable to lecture material. Oracle:
the course as taught — the bias is scope; the system must quiz on what the
professor covered and *only* that, which is exactly what grounding in the
canon buys over a generic LLM's subject knowledge. Output: JSON matching a
Jeopardy app's bulk-upload schema (plus study cards), every item carrying id,
source ref, difficulty. Feedback: instructor verdicts — `not-grounded`,
`mis-calibrated (too easy)` — and the critic learns this professor's standard
of "hard" over rounds. The inbox is nearly empty: the degenerate case.

**Earnings assessment (rolling feed, outcome-scored).** Target: for companies
reporting soon, a disciplined earnings-quality assessment and a judgment on
whether the market's reaction is justified — scored against price drift at
T+2 days to T+1 week (the verdict clock). Oracle: a declared valuation lens,
because "over-reaction" is meaningless without one. Canon: the lens's
methodology texts → wiki. Inbox: each quarter's filings, transcripts, and
reaction data → dated assessments, append-only, forming a track record the
scorer grades automatically when verdict windows elapse. The critic reviews
missed calls ("guidance mattered more than the EPS beat") and routes fixes to
domain_knowledge or distillation. Framed honestly: not "beat the market," but
disciplined, Oracle-consistent, traceable analysis that keeps score of its
own judgment. Educational output, not investment advice.

---

## Related work

SIT-KB-AWP is built from parts with strong precedent; knowing the lineage both
justifies the design and marks where it differs.

**Retrieval-Augmented Generation (RAG)** is the base pattern: ground an LLM's
answers in retrieved documents rather than parametric memory. SD-KDP's serving
stage is RAG — but over a *curated, distilled, single-lens* corpus rather than
whatever was indexed.

**GraphRAG (Microsoft Research)** pre-processes a corpus offline into entity
graphs and community summaries so retrieval can answer global,
corpus-spanning questions. SD-KDP shares the central bet — spend compute
offline (nightly) so query time hits distilled knowledge, not raw chunks.

**RAPTOR (Sarthi et al., Stanford)** builds a tree of recursive summaries
over a corpus and retrieves at multiple abstraction levels. SD-KDP's
"leader → body → depth" artifact structure is a hand-designed, spec-governed
cousin of RAPTOR's summary hierarchy.

**Progressive summarization / Building a Second Brain (Tiago Forte)** is the
personal-knowledge-management ancestor: layered compression of sources into
increasingly distilled, opinionated notes. SD-KDP is, in one line, *BASB
where agents do the summarizing nightly, governed by specs*.

**Memory-augmented agents (MemGPT/Letta; ChatGPT memory)** pursue the same
goal of an assistant that accumulates knowledge of a user's world and
preferences across sessions. SD-KDP externalizes that memory into versioned
files with declared owners, instead of an opaque memory store.

**Generative agents (Park et al., Stanford)** introduced a *reflection* step:
periodically distilling a raw memory stream into higher-level insights that
guide future behavior. SD-KDP's nightly distillation plus critic round is
reflection made explicit, scheduled, and human-gated.

**Voyager (Wang et al.)** showed an agent improving by accumulating a curated
*skill library* rather than by weight updates. SD-KDP generalizes the move:
the growing, curated artifact — wiki, assessments, specs — is the learning.

**Spec-Driven Development** contributes the governance model: specs as source
of truth, in version control, briefing the builder; roles owning documents.

**What SIT-KB-AWP adds is the packaged synthesis.** Each system above supplies
one organ: offline distillation (GraphRAG, RAPTOR), layered compression
(BASB), externalized memory (MemGPT), reflection (generative agents),
artifact-based learning (Voyager), spec governance (SDD). None of them, as
published, combines: (1) a **declared-bias Oracle** — committing to one lens
and one canon, with the bias stated in version control rather than hidden in
a prompt; (2) a **target-first control loop** — KPMs, verdict windows, and a
track record as the explicit error signal for self-improvement; (3) a
**two-tier temporal model** — durable canon vs. episodic inbox, with three
clocks declared as domain facts and all timing behavior derived from them;
and (4) an **ownership-gated critic** — agents propose against any spec, but
approval authority follows a human ownership table, separating improving the
means from redefining the goal. The claim is not a new algorithm; it is a
new *method*: a small, teachable, spec-driven package in which those proven
parts govern each other — and which a single practitioner can run from ten
Markdown files and a cron job.

---

*SIT-KB-AWP · OpenOwls at Temple · educational framework — outputs of any
instance are that instance's declared-Oracle view, not universal truth, and
never professional advice.*
