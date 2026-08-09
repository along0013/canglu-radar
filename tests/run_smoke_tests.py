#!/usr/bin/env python3
"""Unified P0/P1 smoke test entrypoint.

Run with:

    $BOX_AGENT_PYTHON tests/run_smoke_tests.py
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEST_SCRIPTS = [
    PROJECT_ROOT / "tests" / "test_cli_paths.py",
    PROJECT_ROOT / "tests" / "test_validate_paths.py",
    PROJECT_ROOT / "tests" / "test_output_smoke.py",
    PROJECT_ROOT / "tests" / "test_compute_reproducibility.py",
    PROJECT_ROOT / "tests" / "test_compute_output_diff.py",
    PROJECT_ROOT / "tests" / "test_dashboard_contract.py",
]


def main():
    for script in TEST_SCRIPTS:
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=PROJECT_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        if result.returncode != 0:
            print(f"FAILED: {script.relative_to(PROJECT_ROOT)}", file=sys.stderr)
            return result.returncode
    print("all P0/P1 smoke tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
