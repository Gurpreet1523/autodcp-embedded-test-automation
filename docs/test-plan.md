# Test Plan

## Scope
Starter API, schema validation, in-memory duplicate detection, buffer utility and simulator helpers.

## Environment
Python 3.12+, pytest, FastAPI TestClient, local machine or GitHub Ubuntu runner.

## Data
Valid telemetry, negative sequence, empty ECU ID, unknown field, duplicate ID, unavailable TCP port.

## Run
```bash
PYTHONPATH=src python -m pytest -v
```

## Exclusions
No actual QNX/driver hardware tests, PostgreSQL, complete TCP/UDP server, VLAN/TSN, or measured load/soak benchmark in starter release.
