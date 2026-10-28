from dataclasses import dataclass

@dataclass(frozen=True)
class NetworkScenario:
    name: str
    timeout_seconds: float = 1.0
    expected_available: bool = True

SCENARIOS = [
    NetworkScenario("normal-connectivity", 1.0, True),
    NetworkScenario("short-timeout", 0.001, False),
    NetworkScenario("service-unavailable", 0.5, False),
]
