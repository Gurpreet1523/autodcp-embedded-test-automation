from datetime import datetime, timezone
import pytest
from pydantic import ValidationError
from dcp_service.schemas import TelemetryMessage

def valid_data():
    return {
        "ecu_id": "ECU-001", "message_id": "ECU-001-1", "sequence": 1,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "signal": "vehicle_speed", "value": 60.0,
    }

def test_valid_message_is_accepted():
    message = TelemetryMessage.model_validate(valid_data())
    assert message.ecu_id == "ECU-001"
    assert message.sequence == 1

@pytest.mark.parametrize("sequence", [-1, -100])
def test_negative_sequence_is_rejected(sequence):
    data = valid_data()
    data["sequence"] = sequence
    with pytest.raises(ValidationError):
        TelemetryMessage.model_validate(data)

def test_unknown_fields_are_rejected():
    data = valid_data()
    data["unexpected"] = "invalid"
    with pytest.raises(ValidationError):
        TelemetryMessage.model_validate(data)

def test_empty_ecu_id_is_rejected():
    data = valid_data()
    data["ecu_id"] = ""
    with pytest.raises(ValidationError):
        TelemetryMessage.model_validate(data)
