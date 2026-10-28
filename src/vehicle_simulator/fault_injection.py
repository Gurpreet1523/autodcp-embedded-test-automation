from dataclasses import dataclass

@dataclass(frozen=True)
class FaultScenario:
    name: str
    delay_ms: int = 0
    packet_loss_percent: float = 0.0
    disconnect: bool = False

    def __post_init__(self):
        if self.delay_ms < 0:
            raise ValueError("delay_ms cannot be negative")
        if not 0 <= self.packet_loss_percent <= 100:
            raise ValueError("packet_loss_percent must be between 0 and 100")
