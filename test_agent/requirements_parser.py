from pathlib import Path

def load_requirements(path: str | Path) -> list[dict[str, str]]:
    requirements = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip().lstrip("-").strip()
        if line.startswith("DCP-") and ":" in line:
            requirement_id, description = line.split(":", 1)
            requirements.append({"requirement_id": requirement_id.strip(), "description": description.strip()})
    return requirements
