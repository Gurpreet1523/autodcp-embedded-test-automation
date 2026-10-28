from fastapi import FastAPI, HTTPException
from dcp_service.health import health_payload
from dcp_service.persistence import store
from dcp_service.schemas import TelemetryMessage, TelemetryResult

app = FastAPI(title="AutoDCP Telemetry Service", version="0.1.0")

@app.get("/health")
def health() -> dict[str, str]:
    return health_payload()

@app.post("/telemetry", response_model=TelemetryResult)
def ingest(message: TelemetryMessage) -> TelemetryResult:
    accepted = store.process(message)
    return TelemetryResult(
        accepted=accepted,
        duplicate=not accepted,
        message_id=message.message_id,
        detail="accepted" if accepted else "duplicate ignored",
    )

@app.get("/telemetry/{message_id}", response_model=TelemetryMessage)
def get_telemetry(message_id: str) -> TelemetryMessage:
    message = store.get(message_id)
    if message is None:
        raise HTTPException(status_code=404, detail="message not found")
    return message

@app.get("/metrics")
def metrics() -> dict[str, int]:
    return {"stored_messages": store.count()}
