from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class TelemetryMessage(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ecu_id: str = Field(min_length=1, max_length=32)
    message_id: str = Field(min_length=1, max_length=64)
    sequence: int = Field(ge=0)
    timestamp: datetime
    signal: str = Field(min_length=1, max_length=64)
    value: float = Field(ge=-1000, le=1000)

class TelemetryResult(BaseModel):
    accepted: bool
    duplicate: bool = False
    message_id: str
    detail: str
