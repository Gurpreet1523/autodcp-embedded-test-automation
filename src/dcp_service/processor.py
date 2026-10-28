from dcp_service.schemas import TelemetryMessage

class TelemetryProcessor:
    """In-memory starter processor; durable storage is a future milestone."""
    def __init__(self) -> None:
        self._messages: dict[str, TelemetryMessage] = {}

    def process(self, message: TelemetryMessage) -> bool:
        if message.message_id in self._messages:
            return False
        self._messages[message.message_id] = message
        return True

    def get(self, message_id: str) -> TelemetryMessage | None:
        return self._messages.get(message_id)

    def count(self) -> int:
        return len(self._messages)

    def clear(self) -> None:
        self._messages.clear()
