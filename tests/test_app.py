import pytest
from src.app import app as flask_app


@pytest.fixture
def app():
    """Create a new Flask application for testing."""
    app = flask_app
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()


def test_root_path(client):
    response = client.get("/")
    assert response.status_code == 200
