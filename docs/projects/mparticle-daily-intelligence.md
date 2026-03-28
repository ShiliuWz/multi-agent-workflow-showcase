# mparticle Daily Intelligence Pipeline

## What this project is
This project packages a **scheduled content intelligence workflow** that turns recurring article monitoring into a daily digest delivery system.

## Visual proof

![mparticle daily digest proof](../../assets/mparticle-daily-digest-proof.jpg)

The screenshot shows a daily digest card delivered in chat form, making the system output more concrete: structured highlights, daily summary, key threads, action items, and important articles.

Public-safe framing:
- scheduled sync and scan workflow
- content extraction and normalization
- daily digest generation
- timed delivery through chat/webhook integration
- configuration templates and deployment examples

## Why I built it
The goal was to reduce manual reading and make daily follow-up easier for a set of recurring content sources.

Instead of checking sources one by one, the workflow was structured as:

**scheduled fetch -> article scan -> content extraction -> digest analysis -> daily delivery**

## What I personally owned
- defined the workflow shape and daily operating goal
- organized the pipeline into separate scripts rather than a single ad hoc script
- designed the data flow between scan, content extraction, analysis, and delivery
- packaged the work into a public-safe showcase format with config templates and deployment examples
- documented the sanitization boundary for GitHub/public review

## Representative modules in the public package
Inside [`examples/mparticle-daily/`](../../examples/mparticle-daily/) the repository now includes:

- `scripts/daily_pipeline_v2.py` — public-safe pipeline entry example
- `scripts/send_report.py` — digest card preview builder
- `scripts/analyzer.py` — deterministic local summary example
- `scripts/sync_runner.py` — authenticated sync stage boundary description
- `scripts/content_reader.py` — normalized article extraction shape
- `scripts/kb_scanner.py` — snapshot / diff workflow example
- `scripts/db_init.py` — public schema outline
- `config/settings.example.py` — template-only settings
- `config/auth.example.json` — schema-only auth example
- `deploy/launchd/*.example.plist` — scheduled execution templates
- `data/sample_articles.json` — synthetic sample output

## Scheduling and operations signals
The original system was designed around two recurring timed stages:
- **09:30** pipeline run / sync and collection
- **09:40** digest send

The public repo preserves this operational signal through example `launchd` templates while removing real machine paths and local usernames.

## What this proves
This project is a strong example of moving from “content scripts” to a **maintainable automation pipeline**:
- recurring execution rather than one-time collection
- staged processing rather than one large script
- delivery-oriented output rather than raw scraped data
- documentation and deployment awareness rather than code only

## Sanitization notes
This public version intentionally excludes:
- real host/IP information
- real auth cookies / tokens / session state
- real webhook destinations
- local database files
- real monitored account lists and raw production article data
- absolute local machine paths

See also:
- [`docs/cases/mparticle-daily-case.md`](../cases/mparticle-daily-case.md)
- [`docs/github-sanitization-notes.md`](../github-sanitization-notes.md)
