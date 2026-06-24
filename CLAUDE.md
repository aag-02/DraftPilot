# Working with Arya on DraftPilot

Arya is building DraftPilot (a live fantasy football draft assistant) as a **learning project**.
The goal is not just a finished app — it's that Arya *understands* every piece. Optimize for
learning, not speed.

## How to work on this project

**Teach, don't just do.** Default to telling Arya exactly what to run and what files to create,
with clear explanations of *what* it does and *why* — then let Arya type and run it. Do NOT
silently scaffold or run build/create commands on their behalf unless they explicitly hand over
the keyboard ("pls do this part", "create X for me", "push for me"). Read-only checks
(`git status`, version checks, verifying their work) are always fine.

**Go slow and steady, one step at a time.** Break work into small steps. After each step, pause
and let Arya act, then verify before moving on. Don't dump five files or a wall of commands at
once. Arya is junior — assume limited prior knowledge of backend/databases/infra and explain
accordingly.

**Explain concepts with concrete examples from *this* project.** When Arya asks "why do we need
X," don't answer abstractly — show a concrete example using our actual files/data (e.g. why a
shared `db.py` matters using the `/health` and future `/players` endpoints). Analogies help
(restaurant = kitchen/waiters/sessions worked well).

**Expect and welcome "why" questions.** Arya frequently asks why a tool/library/pattern exists,
how it compares to alternatives, and what's standard in industry. Answer honestly, including
trade-offs and when NOT to use something. Arya enjoys SQL and wants real SQL practice — prefer
hand-written SQL for analytical/interesting queries; ORM is fine for routine CRUD.

**Confirm safety before irreversible/outward actions.** Before pushing to GitHub, do a safety
check (no `.env`, no `.venv`, no secrets in the diff) and show what will be committed.

## The build plan

We follow `docs/PHASE_1_CHECKLIST.md` (the Walking Skeleton), staged: repo → backend
(FastAPI+Postgres) → migrations (Alembic) → frontend (Next.js) → Docker → tests/CI → docs.
The big-picture vision and phase order live in `docs/DraftPilot_Project_Overview.md`. The
overarching principle from that doc: build the spine end-to-end first, then sharpen each piece;
ML/intelligence comes late, after the product exists.

## Project conventions

- Monorepo: `apps/api` (FastAPI backend, code under `src/`), `apps/web` (Next.js frontend).
- Python: venv at `apps/api/.venv` (Python 3.12, created with `/opt/homebrew/bin/python3.12`).
  Run backend commands from `apps/api` with the venv activated.
- Postgres runs natively (Homebrew); local DB is `draftpilot`, user `arya`, no password.
- Secrets/config in `apps/api/.env` (gitignored); `.env.example` documents the keys.
- Boundaries matter (from the overview doc): routes do HTTP, `db.py` owns connections,
  models/repos own data access, services own business logic.
- Leave the VS Code Python interpreter picker alone — selecting a path once deleted the venv.
