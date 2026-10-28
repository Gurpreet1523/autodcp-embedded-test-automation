import json
import socket

def send_message(host: str, port: int, message: dict, timeout: float = 2.0) -> bytes:
    payload = json.dumps(message).encode("utf-8") + b"\\n"
    with socket.create_connection((host, port), timeout=timeout) as connection:
        connection.settimeout(timeout)
        connection.sendall(payload)
        response = bytearray()
        while not response.endswith(b"\\n"):
            chunk = connection.recv(4096)
            if not chunk:
                raise ConnectionError("Connection closed before acknowledgment")
            response.extend(chunk)
        return bytes(response)
