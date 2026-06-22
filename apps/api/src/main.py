"""FastAPI application — the web layer.

Defines the HTTP endpoints. For Phase 1 there's just `/health`, which reads
a row from the database to prove the full browser -> API -> Postgres round trip.
"""

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db import get_session
from .models import Health

app = FastAPI(title="DraftPilot API")


@app.get("/health")
def health(session: Session = Depends(get_session)):
    row = session.query(Health).first()
    return {"status": "ok", "db_value": row.value if row else None}
