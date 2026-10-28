import os
from openai import OpenAI
from pydantic import BaseModel, Field

class CandidateCase(BaseModel):
    title: str
    category: str
    preconditions: list[str]
    steps: list[str] = Field(min_length=1)
    expected_results: list[str] = Field(min_length=1)

class CandidateCases(BaseModel):
    requirement_id: str
    cases: list[CandidateCase]

def generate_cases(requirement_id: str, requirement_text: str) -> CandidateCases:
    """Generate candidates only; require human review before regression use."""
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.responses.parse(
        model=os.environ["OPENAI_MODEL"],
        input=[
            {"role": "system", "content": "Act as an embedded QA engineer. Generate test candidates. Cover negative, boundary and recovery cases where relevant. Never invent numeric acceptance criteria. Flag ambiguity for human review."},
            {"role": "user", "content": f"Requirement ID: {requirement_id}\nRequirement: {requirement_text}"},
        ],
        text_format=CandidateCases,
    )
    result = response.output_parsed
    if result is None:
        raise ValueError("No structured test cases returned")
    if result.requirement_id != requirement_id:
        raise ValueError("Generated requirement ID does not match input")
    return result
