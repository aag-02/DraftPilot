# 0001 — Technology stack

- **Status:** Accepted
- **Date:** 2026-06-26

## Context

DraftPilot is a live fantasy football draft assistant: a polished, interactive
web product backed by data, algorithms (a draft simulator), and later ML and
LLM features. It is also a solo learning/portfolio project, so the stack should
be widely used, transferable, and demonstrate real engineering practices.

We needed to choose the core technologies for the frontend, backend, database,
cache, and local/dev environment before building the walking skeleton.

## Decision

- **Frontend: Next.js (App Router, TypeScript).** A real, fast, interactive UI is
  core to the product (it is used live during drafts, often on mobile). Next.js
  gives routing, server-side rendering, and tooling out of the box, and is the
  most common React framework — good for transferable skills and portfolio
  visibility.

- **Backend: FastAPI (Python 3.12).** The interesting logic (scoring function,
  Monte Carlo simulator, ML projections, LLM calls) lives in Python, so the
  backend is Python to keep that code in one language with no cross-service
  serialization. FastAPI adds typed request/response models (Pydantic), automatic
  OpenAPI docs, and async support.

- **Database: PostgreSQL + Alembic.** The data is relational (players, leagues,
  drafts, picks, rosters, projections). Postgres is the standard relational choice
  and later provides `pgvector` for RAG without a second datastore. Alembic gives
  versioned, reviewable schema migrations.

- **Cache: Redis.** Wired now, used later for hot draft state, simulator result
  caching, rate-limit counters, and pub/sub for real-time updates.

- **Local/dev: Docker Compose.** One command brings up the full stack (db, redis,
  api, web) reproducibly. Native venv + local Postgres remain the fast inner-dev
  loop; Docker is for reproducibility and as the basis for deployment.

- **CI: GitHub Actions.** Runs tests on every push/PR in a clean Linux
  environment.

## Alternatives considered

- **Frontend:** plain React + Vite (less batteries-included), or Angular (heavier,
  more enterprise). Next.js chosen for SSR/mobile performance and ubiquity.
- **Backend:** Node/Express (would split ML/LLM code into another language) or
  Django (heavier, more opinionated than needed). FastAPI chosen for Python +
  typing + async.
- **Database:** keep data in a non-relational store — rejected; the domain is
  inherently relational and needs joins.
- **Dev env:** develop entirely in Docker — rejected for the inner loop (slower,
  harder to debug on macOS); used for packaging/reproducibility instead.

## Consequences

- One product language split: Python (backend/ML/LLM) and TypeScript (frontend),
  bridged by generated TypeScript types from the API's OpenAPI spec.
- The same code runs in dev, Docker, and (later) production by changing config
  (environment variables) only — no code changes between environments.
- Excludes (for now): Kubernetes, microservices, Kafka, a separate vector DB —
  none justified at this product's scale.
