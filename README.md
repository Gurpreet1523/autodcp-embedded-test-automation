# AutoDCP — Embedded Test Automation Lab

A starter portfolio simulation for an automotive Data Collection Platform (DCP). It includes a FastAPI telemetry receiver, Pydantic validation, duplicate detection, a virtual ECU generator, network client utilities, pytest tests, documentation templates, an optional AI test-case generator, and CI.

> Learning simulation only. It is not production automotive software and does not demonstrate actual QNX, kernel-driver, or vehicle hardware testing.

## Quick start

Requires Python 3.12+.

### Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
$env:PYTHONPATH = "src"
python -m pytest -v
```

### Linux / WSL
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
PYTHONPATH=src python -m pytest -v
```

## Included
- FastAPI telemetry API with health, ingest, retrieval and metrics endpoints
- Schema validation and duplicate message detection
- Bounded FIFO buffer utility
- Virtual ECU and telemetry generator
- TCP/UDP client helpers and fault-scenario model
- Unit, API, integration, protocol, resilience and regression tests
- Requirements, traceability matrix, test plan, defect/RCA templates
- Optional AI-assisted candidate test generator
- GitHub Actions workflow and Docker starter

## Known limitations
The starter uses in-memory storage; PostgreSQL is a future milestone. TCP/UDP helpers are clients, not a complete protocol server. Performance/soak testing, realistic network impairment, authentication, VLAN/QoS/TSN and QNX/driver testing are extension tasks. The AI generator requires an API key and model setting. Review AI-generated cases before use.
