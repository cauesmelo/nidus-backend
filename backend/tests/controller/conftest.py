from fastapi.testclient import TestClient
from pytest import fixture

from backend.app import app


@fixture
def client() -> TestClient:
    return TestClient(app)
