"""Shared pytest fixtures.

Sets up an isolated TEST database, points the app at it, and gives tests a
clean slate for every run.
"""

import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.db import Base, get_session
from src.main import app

# A separate database for tests — never the dev/prod one.
# CI will provide TEST_DATABASE_URL; locally we fall back to draftpilot_test.
TEST_DATABASE_URL = os.environ.get(
    "TEST_DATABASE_URL",
    "postgresql+psycopg://arya@localhost:5432/draftpilot_test",
)

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


@pytest.fixture(autouse=True)
def fresh_schema():
    """Before each test: create all tables. After: drop them. Clean slate every time."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session():
    """A database session tests can use to insert setup data."""
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client():
    """A test client that calls the app, but with get_session pointed at the test DB."""

    def override_get_session():
        session = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_session] = override_get_session
    yield TestClient(app)
    app.dependency_overrides.clear()
