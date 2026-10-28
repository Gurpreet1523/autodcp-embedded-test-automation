import pytest
from vehicle_simulator.fault_injection import FaultScenario

def test_fault_scenario_accepts_valid_values():
    scenario = FaultScenario("packet-loss", delay_ms=20, packet_loss_percent=5)
    assert scenario.delay_ms == 20

@pytest.mark.parametrize("loss", [-1, 101])
def test_fault_scenario_rejects_invalid_packet_loss(loss):
    with pytest.raises(ValueError):
        FaultScenario("invalid", packet_loss_percent=loss)
