"""Database table definitions (SQLAlchemy models).

Each class here = one table in Postgres. For Phase 1 there's just `health`,
which exists only to prove the app can read from the database.
"""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


class Health(Base):
    __tablename__ = "health"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[str] = mapped_column(String, nullable=False)
