# Case: mparticle Daily Content Intelligence

## Problem
Recurring content monitoring is easy to start manually but hard to sustain consistently. Once the number of sources grows, the process becomes fragmented:
- source checking becomes repetitive
- article reading becomes uneven
- daily follow-up quality becomes inconsistent
- delivery is easy to miss without scheduling

## What I built
I structured the work as a **daily content intelligence pipeline** with clear stages:

1. scheduled sync / source scan
2. new article detection
3. content extraction and normalization
4. digest generation
5. scheduled delivery

This changed the task from “read things when I remember” into a repeatable daily operating workflow.

## Workflow / architecture
Representative flow:

**scheduler -> sync runner -> KB scanner -> content reader -> analyzer -> digest delivery**

Public evidence in this repository:
- [`examples/mparticle-daily/scripts/`](../../examples/mparticle-daily/scripts/)
- [`examples/mparticle-daily/config/`](../../examples/mparticle-daily/config/)
- [`examples/mparticle-daily/deploy/launchd/`](../../examples/mparticle-daily/deploy/launchd/)
- [`examples/mparticle-daily/data/sample_articles.json`](../../examples/mparticle-daily/data/sample_articles.json)

## What was hard
The main challenge was not just extracting content, but packaging the whole workflow so it could run reliably and be shared publicly without leaking sensitive internals.

That required handling three different boundaries:
- **runtime boundary**: scheduled execution and multi-stage script organization
- **data boundary**: article metadata, normalized content, digest-ready structure
- **privacy boundary**: auth state, webhook targets, local paths, and local DB files

## What I owned
- workflow definition and packaging direction
- modular script boundary design
- digest-oriented output framing
- public-safe config/deploy template creation
- GitHub sanitization and portfolio packaging

## What is intentionally sanitized
This public repo does **not** include:
- real credentials or login cookies
- real webhook/chat targets
- local SQLite databases
- raw private monitored account data
- real hostnames/IPs
- absolute machine paths from launchd config

## Why this case matters
This case is useful in interviews because it shows more than simple scraping:
- workflow thinking
- operations thinking
- delivery thinking
- maintainability and packaging discipline
- the ability to turn a private working system into a recruiter-readable public portfolio artifact
