import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "reports/junit.xml")
    if not path.exists():
        print(f"Report not found: {path}")
        return 2
    root = ET.parse(path).getroot()
    suites = [root] if root.tag == "testsuite" else list(root.iter("testsuite"))
    tests = sum(int(s.get("tests", 0)) for s in suites)
    failures = sum(int(s.get("failures", 0)) + int(s.get("errors", 0)) for s in suites)
    skipped = sum(int(s.get("skipped", 0)) for s in suites)
    print(f"Tests: {tests}; failures/errors: {failures}; skipped: {skipped}")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
