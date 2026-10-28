from vehicle_simulator.ecu import VirtualECU

def test_virtual_ecu_generates_incrementing_sequences():
    ecu = VirtualECU("ECU-003")
    first = ecu.emit()
    second = ecu.emit()
    assert first.sequence == 1
    assert second.sequence == 2
    assert first.ecu_id == second.ecu_id == "ECU-003"
