"""Database connection layer.

The single place in the app that knows how to talk to Postgres.
Everything else asks this file for a session instead of connecting directly.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Load variables from the .env file into the environment.
load_dotenv()

# Read the database URL that .env defined.
DATABASE_URL = os.environ["DATABASE_URL"]

# The engine = the connection pool to Postgres. Created ONCE for the whole app.
engine = create_engine(DATABASE_URL)

# A factory that hands out new sessions (one short "conversation" with the DB).
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """Parent class for all table models. SQLAlchemy/Alembic use it to
    discover which tables exist."""


def get_session():
    """Yield a database session, then always close it.

    FastAPI calls this per request: the endpoint borrows a session,
    uses it, and it's cleaned up automatically when the request ends.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
