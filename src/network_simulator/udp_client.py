import json
import socket

def send_datagram(host: str, port: int, message: dict, timeout: float = 1.0) -> bytes:
    payload = json.dumps(message).encode("utf-8")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(timeout)
        sock.sendto(payload, (host, port))
        response, _ = sock.recvfrom(4096)
        return response
