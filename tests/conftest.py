import pytest
from fastapi.testclient import TestClient
from dcp_service.main import app
from dcp_service.persistence import store

@pytest.fixture
def client():
    store.clear()
    with TestClient(app) as test_client:
        yield test_client
    store.clear()
