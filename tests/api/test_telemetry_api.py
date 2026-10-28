def payload(message_id="ECU-001-1", sequence=1):
    return {
        "ecu_id": "ECU-001", "message_id": message_id, "sequence": sequence,
        "timestamp": "2026-01-01T12:00:00Z",
        "signal": "vehicle_speed", "value": 60.0,
    }

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_ingest_and_retrieve_message(client):
    message = payload()
    response = client.post("/telemetry", json=message)
    assert response.status_code == 200
    assert response.json()["accepted"] is True
    retrieved = client.get("/telemetry/ECU-001-1")
    assert retrieved.status_code == 200
    assert retrieved.json()["message_id"] == "ECU-001-1"

def test_duplicate_message_is_not_stored_twice(client):
    message = payload()
    first = client.post("/telemetry", json=message)
    second = client.post("/telemetry", json=message)
    assert first.json()["accepted"] is True
    assert second.json()["duplicate"] is True
    assert client.get("/metrics").json()["stored_messages"] == 1

def test_invalid_message_is_rejected(client):
    message = payload()
    message["sequence"] = -1
    assert client.post("/telemetry", json=message).status_code == 422

def test_missing_message_returns_404(client):
    assert client.get("/telemetry/does-not-exist").status_code == 404
