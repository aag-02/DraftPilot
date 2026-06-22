# Phase 1 — Walking Skeleton: Build Checklist

> The thinnest end-to-end slice of the real system: browser → FastAPI → Postgres → back,
> plus the build/test/deploy machinery. No fantasy logic yet — just proof the plumbing connects.
> Work top to bottom; each box is one concrete action.

---

## Stage 0 — Repo foundation ✅ DONE
- [x] `git init`
- [x] Create `docs/` and `docs/decisions/`, move overview doc in
- [x] Create `.gitignore` (Python, Node, env, OS)
- [x] First commit
- [x] Create GitHub repo + connect remote (`origin`)
- [x] Push `main` to GitHub

## Stage 1 — Backend project setup
- [x] Create `draftpilot` database in Postgres
- [x] Create `apps/api/src/` structure
- [x] Create venv (`apps/api/.venv`, Python 3.12)
- [x] Activate venv in terminal (`source .venv/bin/activate`, prompt shows `(.venv)`)
- [x] Create `requirements.txt` (FastAPI, uvicorn, SQLAlchemy, psycopg, Alembic, pytest, httpx, python-dotenv)
- [x] `pip install -r requirements.txt`
- [x] Create `.env` (DB connection string) **and** `.env.example` (same keys, no secrets)

## Stage 1 (cont.) — Write the backend code
- [x] `src/db.py` — SQLAlchemy engine + session (reads DB URL from `.env`)
- [x] `src/models.py` — one `health` table model
- [x] `src/main.py` — FastAPI app + `GET /health` that reads a row and returns it
- [x] Sanity-run: `uvicorn src.main:app --reload`, app starts with no errors

## Stage 2 — Database migrations (Alembic)
- [x] `alembic init` — scaffold migration config
- [x] Point Alembic at the DB URL + models
- [x] Generate first migration (creates `health` table)
- [x] `alembic upgrade head` — table appears in the database
- [x] Seed one row into `health` so `/health` has data to read
- [x] Verify `GET /health` returns the DB value (browser / curl)

## Stage 3 — Frontend (Next.js)
- [ ] `npx create-next-app@latest web --typescript --app` in `apps/`
- [ ] `app/page.tsx` fetches `GET /health` and renders the value
- [ ] Generate TypeScript types from the API's OpenAPI spec
- [ ] Verify: `npm run dev` → browser page shows the value from Postgres

## Stage 4 — Containerize (Docker Compose)
- [ ] `apps/api/Dockerfile`
- [ ] `apps/web/Dockerfile`
- [ ] Root `docker-compose.yml` with 4 services: `db`, `redis`, `api`, `web`
- [ ] Run migrations on API startup
- [ ] Verify: `docker compose up --build` → whole stack runs, browser page works, **zero** manual steps

## Stage 5 — Tests + CI
- [ ] `apps/api/tests/test_health.py` (hits `/health`, asserts 200 + value)
- [ ] `pytest` passes locally
- [ ] `.github/workflows/ci.yml` (Postgres service, lint + pytest on PR)
- [ ] Open a PR, CI runs green
- [ ] Add CI badge to `README.md`

## Stage 6 — Documentation
- [ ] `docs/decisions/0001-stack.md` — first ADR (why FastAPI + Next.js + Postgres + Redis)
- [ ] Update `README.md` (what it is, how to run it)

---

## ✅ Phase 1 is COMPLETE when
- [ ] `docker compose up` → all 4 services, zero manual steps
- [ ] Browser shows a value round-tripped from Postgres
- [ ] `alembic upgrade head` builds schema from scratch
- [ ] `pytest` passes (incl. the `/health` test)
- [ ] A PR triggers CI, badge is green
- [ ] Frontend's API call is typed from OpenAPI
- [ ] `0001-stack.md` exists
