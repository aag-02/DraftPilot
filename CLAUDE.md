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

`docs/PHASE_1_CHECKLIST.md` (the Walking Skeleton) and `docs/DraftPilot_Project_Overview.md`
are a **rough guide, not gospel.** The plan is flexible and we deviate whenever it makes sense
for Arya. Use the docs as a loose map and for big-picture direction — do NOT treat them as fixed
requirements or keep citing "your doc says X" to justify decisions. Reason from what's actually
best for the project and Arya's learning right now; if that means departing from the doc, do it
and just say so. Suggest deviations proactively when a better path exists.

The loose shape so far: repo → backend (FastAPI+Postgres) → migrations (Alembic) → frontend
(Next.js) → Docker → tests/CI → docs. One genuinely useful principle worth keeping: build the
spine end-to-end first, then sharpen each piece; ML/intelligence comes late, after the product
exists. Everything else is negotiable.

## Build it like production at a company

Arya wants to learn real software-engineering principles by treating this as if it were a
**production system at a company**, not a toy/learning shortcut. This is a core goal — favor the
professional pattern even when a quicker hack would work for a local project, and explain *why*
it's the production-grade choice.

Apply this throughout:
- **No secrets/credentials in committed files** — ever. Use env vars + gitignored `.env`
  (with a committed `.env.example` documenting the keys). Treat every credential as if it
  protected real infrastructure.
- **Config comes from the environment**, not hardcoded — so the same code runs in dev/staging/prod
  by changing config only.
- **Boundaries, tests, migrations, reproducibility, observability** are the default, not optional.
- When there's a "works for local" way and a "how a company would actually do it" way, pick the
  latter and call out the difference. Point out where a real prod setup would go further (secrets
  managers, least-privilege, zero-downtime migrations, etc.) even if we don't build it now.

## Project conventions

- Monorepo: `apps/api` (FastAPI backend, code under `src/`), `apps/web` (Next.js frontend).
- Python: venv at `apps/api/.venv` (Python 3.12, created with `/opt/homebrew/bin/python3.12`).
  Run backend commands from `apps/api` with the venv activated.
- Postgres runs natively (Homebrew); local DB is `draftpilot`, user `arya`, no password.
- Secrets/config in `apps/api/.env` (gitignored); `.env.example` documents the keys.
- Boundaries matter (from the overview doc): routes do HTTP, `db.py` owns connections,
  models/repos own data access, services own business logic.
- Leave the VS Code Python interpreter picker alone — selecting a path once deleted the venv.
- Frontend is **Next.js 16** (App Router) — newer than training defaults and has breaking changes.
  Before writing frontend code, check the bundled docs at `apps/web/node_modules/next/dist/docs/`
  rather than relying on memory. Server Components fetch data via `async/await`; `fetch` is not
  cached by default.

## Maintaining this file

Keep this file updated yourself when genuinely useful, durable info emerges (a hard-won gotcha, a
settled convention, a workflow preference) — without asking each time. Bias toward NOT bloating it:
only add things that will save real time later. Prefer editing/condensing existing lines over
appending new ones; remove anything that becomes stale.
