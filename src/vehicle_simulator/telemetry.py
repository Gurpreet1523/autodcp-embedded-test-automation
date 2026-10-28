from datetime import datetime, timezone
from dcp_service.schemas import TelemetryMessage

def make_telemetry(ecu_id="ECU-001", sequence=1, signal="vehicle_speed", value=60.0):
    return TelemetryMessage(
        ecu_id=ecu_id, message_id=f"{ecu_id}-{sequence}", sequence=sequence,
        timestamp=datetime.now(timezone.utc), signal=signal, value=value
    )
