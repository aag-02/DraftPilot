"""FastAPI application — the web layer.

Defines the HTTP endpoints. For Phase 1 there's just `/health`, which reads
a row from the database to prove the full browser -> API -> Postgres round trip.
"""

from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .db import get_session
from .models import Health

app = FastAPI(title="DraftPilot API")


class HealthResponse(BaseModel):
    """The shape of the /health response. FastAPI publishes this in the
    OpenAPI spec and validates that the endpoint actually returns it."""

    status: str
    db_value: str | None


@app.get("/health", response_model=HealthResponse)
def health(session: Session = Depends(get_session)):
    row = session.query(Health).first()
    return {"status": "ok", "db_value": row.value if row else None}
