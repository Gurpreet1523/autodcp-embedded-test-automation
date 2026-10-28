from vehicle_simulator.telemetry import make_telemetry

class VirtualECU:
    def __init__(self, ecu_id: str) -> None:
        self.ecu_id = ecu_id
        self.sequence = 0

    def emit(self, signal="vehicle_speed", value=60.0):
        self.sequence += 1
        return make_telemetry(self.ecu_id, self.sequence, signal, value)
