# System Design

```text
Virtual ECU(s)
    | telemetry (starter API uses HTTP; TCP/UDP clients are utilities)
    v
FastAPI DCP Receiver
    v
Schema Validation -> Duplicate Detection -> In-memory Store
    +--> Health / Metrics / Retrieval API

Independent QA Framework
    +--> Unit / API / Protocol / Integration / Regression Tests
    +--> Reports and CI artifacts
    +--> AI candidates -> validation -> human approval
```

Current implementation: FastAPI, Pydantic, in-memory message store, buffer utility, virtual ECU generator, TCP/UDP client helpers, pytest suite.

Planned: PostgreSQL, TCP/UDP receiver, concurrency tests, realistic fault injection, resource monitoring, performance, authentication and target-system testing where available.
