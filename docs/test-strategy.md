# Test Strategy

## Levels
1. Unit: schema, buffer, duplicate logic.
2. API: health, ingestion, retrieval, validation errors.
3. Integration: virtual ECU and DCP components.
4. Protocol: socket failures and framing.
5. Resilience: fault configuration and recovery (expand with receiver).
6. Performance: load, stress, soak (planned).
7. Security: input validation, dependency audit, authentication (planned).
8. Regression: repeat tests for previously fixed defects.

## Entry criteria
Requirements and expected behavior documented; isolated environment; dependencies installed; synthetic data only.

## Exit criteria
Required tests pass or failures are triaged; no unresolved critical defects in release scope; results retained; limitations documented.

## Defect lifecycle
New -> Triaged -> In Progress -> Fixed -> Retest -> Closed (or Reopened).
