def test_duplicate_message_regression(client):
    payload = {
        "ecu_id": "ECU-002", "message_id": "ECU-002-99", "sequence": 99,
        "timestamp": "2026-01-01T12:00:00Z",
        "signal": "battery_voltage", "value": 12.4,
    }
    assert client.post("/telemetry", json=payload).json()["accepted"] is True
    duplicate = client.post("/telemetry", json=payload).json()
    assert duplicate["duplicate"] is True
    assert client.get("/metrics").json()["stored_messages"] == 1
