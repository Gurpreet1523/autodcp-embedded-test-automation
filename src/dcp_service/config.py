import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    host: str = os.getenv("DCP_HOST", "127.0.0.1")
    port: int = int(os.getenv("DCP_PORT", "8000"))
    max_buffer_size: int = int(os.getenv("DCP_MAX_BUFFER_SIZE", "1000"))

settings = Settings()
