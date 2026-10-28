from typing import Literal
from pydantic import BaseModel, Field

class GeneratedTestCase(BaseModel):
    case_id: str
    requirement_id: str
    title: str
    category: Literal["positive", "negative", "boundary", "concurrency", "resilience", "security"]
    preconditions: list[str]
    steps: list[str] = Field(min_length=1)
    expected_results: list[str] = Field(min_length=1)
    automation_candidate: bool
    review_status: Literal["pending", "approved", "rejected"] = "pending"
