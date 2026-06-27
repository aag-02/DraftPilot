"""Tests for the /health endpoint."""

from src.models import Health


def test_health_empty_database(client):
    """With no rows, /health returns ok and a null db_value."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "db_value": None}


def test_health_reads_db_value(client, db_session):
    """With a row present, /health returns that row's value."""
    db_session.add(Health(value="hello-test"))
    db_session.commit()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "db_value": "hello-test"}
