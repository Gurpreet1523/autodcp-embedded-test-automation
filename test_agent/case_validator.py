from collections.abc import Iterable
from test_agent.schemas.test_case import GeneratedTestCase

def validate_cases(cases: Iterable[GeneratedTestCase], known_requirement_ids: set[str]) -> list[str]:
    errors = []
    seen_ids = set()
    for case in cases:
        if case.requirement_id not in known_requirement_ids:
            errors.append(f"{case.case_id}: unknown requirement {case.requirement_id}")
        if case.case_id in seen_ids:
            errors.append(f"{case.case_id}: duplicate case ID")
        seen_ids.add(case.case_id)
    return errors
