# Security Notes

Running log of security decisions and hardening items. Things that are fine for **local
development** but must change before a real deployment are tracked here so they aren't forgotten.

## Done
- **No secrets in committed files.** Credentials live in gitignored `.env` files; committed
  `.env.example` files document the required keys. Verified no `.env` is tracked or in git history.
- **Config via environment.** `docker-compose.yml` uses `${VAR}` substitution from the root
  `.env`; the app reads config from the environment (`os.environ` / `process.env`).
- **Pinned dependencies (direct).** `apps/api/requirements.txt` pins exact versions for
  reproducible builds.

## To harden before deployment

### 1. Don't publish database / cache ports
`docker-compose.yml` currently publishes `db:5432` and `redis:6379` to the host for local
convenience. In production, these must NOT be exposed — only `web` (and possibly `api`) should be
reachable. Services reach `db`/`redis` over the internal Compose/network only.

### 2. Redis authentication
Redis currently has no password. Production needs `requirepass` (or managed Redis with auth) and
must not be internet-reachable.

### 3. Least-privilege database role
Local uses the Postgres superuser (`POSTGRES_USER=draftpilot`). Production should use a dedicated
app role that can read/write its own tables but cannot drop databases or manage roles, to limit
blast radius if the app is compromised.

### 4. Strong, managed credentials
Local credentials are weak/shared (`draftpilot`). Production credentials must be strong, unique,
and injected from a secrets manager (e.g. AWS Secrets Manager) at deploy time — the env-var seam
for this already exists.

### 5. Transitive dependency locking
`requirements.txt` pins *direct* deps only. A full lockfile (pip-tools / uv / Poetry) should pin
the entire transitive tree for stronger reproducibility and supply-chain safety. Docker base
images should be pinned by digest in production.

## On the horizon (tracked in the build plan)
- API authn/authz and rate limiting (especially for cost-sensitive LLM endpoints).
- Restrictive CORS policy (specific origins, never `*`) once the browser calls the API directly.
- Cleanup: `apps/api/alembic.ini` still has the dummy `sqlalchemy.url` placeholder; the real URL
  is injected via `migrations/env.py`, so the placeholder can be blanked to avoid confusion.
