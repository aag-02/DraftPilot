# DraftPilot

[![CI](https://github.com/aag-02/DraftPilot/actions/workflows/ci.yml/badge.svg)](https://github.com/aag-02/DraftPilot/actions/workflows/ci.yml)

A live fantasy football draft assistant. (Work in progress — currently the Phase 1
walking skeleton: a full-stack slice running browser → Next.js → FastAPI → Postgres.)

## Stack

- **Frontend:** Next.js (App Router, TypeScript) — `apps/web`
- **Backend:** FastAPI (Python 3.12) — `apps/api`
- **Database:** PostgreSQL, with Alembic migrations
- **Cache:** Redis (wired, used in later phases)
- **Containerized** with Docker Compose; **CI** via GitHub Actions

## Run the whole stack (Docker)

```bash
cp .env.example .env        # fill in values
docker compose up --build
```

- Web: http://localhost:3000
- API: http://localhost:8000 (docs at `/docs`)

Migrations run automatically on API startup.

## Run the backend natively (dev)

```bash
cd apps/api
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # set DATABASE_URL
alembic upgrade head
uvicorn src.main:app --reload
```

## Run the frontend natively (dev)

```bash
cd apps/web
npm install
npm run dev
```

## Tests

```bash
cd apps/api
createdb draftpilot_test    # one-time
pytest -v
```

## Docs

- `docs/DraftPilot_Project_Overview.md` — the product vision and build plan
- `docs/PHASE_1_CHECKLIST.md` — current build progress
- `docs/security-notes.md` — security decisions and deferred hardening
