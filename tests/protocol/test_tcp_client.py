import socket
import pytest
from network_simulator.tcp_client import send_message

def test_connection_to_unavailable_port_fails():
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
    with pytest.raises(OSError):
        send_message("127.0.0.1", port, {"message_id": "ECU-001-1"}, timeout=0.5)
