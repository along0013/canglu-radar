#!/usr/bin/env python3
"""P1 smoke test for numeric-tolerance diff between recomputed output and formal output.

This test recomputes the five-file output package from the project-local shared
fixture by default into a temporary directory. It then recursively compares the
result with the formal output/ package. Numeric fields are compared with
tolerance; stable non-numeric fields must match exactly. Volatile generation
timestamps are intentionally ignored. Set CANGLU_SHARED_DIR to use a full real
shared/ input directory locally.

Run directly with:

    $BOX_AGENT_PYTHON tests/test_compute_output_diff.py
"""

import json
import math
import os
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_SHARED_DIR = PROJECT_ROOT / "tests" / "fixtures" / "shared"
SHARED_DIR = Path(os.environ.get("CANGLU_SHARED_DIR", FIXTURE_SHARED_DIR)).resolve()
FORMAL_OUTPUT_DIR = PROJECT_ROOT / "output"
COMPUTE_SCRIPT = PROJECT_ROOT / "engine" / "compute.py"

OUTPUT_FILES = [
    "metrics.json",
    "history.json",
    "scenarios.json",
    "decisions.json",
    "indices.json",
]

REQUIRED_SHARED_FILES = {
    "scfi-26w.csv",
    "surcharge-scenarios.csv",
    "index-comparison.csv",
    "usd-cny-26w.csv",
}

# The formal output package may have been generated at a different time from the
# temporary recomputation. All other metadata and business fields are expected to
# remain stable.
IGNORED_PATH_SUFFIXES = {
    "_meta.generated_at",
}

ABS_TOL = 1e-6
REL_TOL = 1e-9


class DiffStats:
    def __init__(self):
        self.numeric_fields = 0
        self.exact_fields = 0


def assert_shared_inputs_available():
    assert SHARED_DIR.exists(), f"shared input dir missing: {SHARED_DIR}"
    missing = sorted(name for name in REQUIRED_SHARED_FILES if not (SHARED_DIR / name).exists())
    assert not missing, f"shared input files missing: {missing}"


def load_json(path):
    assert path.exists(), f"missing JSON file: {path}"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def format_path(parts):
    return ".".join(str(part) for part in parts)


def compare_json(expected, actual, path_parts, stats):
    path = format_path(path_parts)
    if any(path.endswith(suffix) for suffix in IGNORED_PATH_SUFFIXES):
        return

    if is_number(expected) and is_number(actual):
        assert math.isclose(
            float(actual),
            float(expected),
            rel_tol=REL_TOL,
            abs_tol=ABS_TOL,
        ), f"numeric mismatch at {path}: expected {expected!r}, got {actual!r}"
        stats.numeric_fields += 1
        return

    if isinstance(expected, dict):
        assert isinstance(actual, dict), f"type mismatch at {path}: expected dict, got {type(actual).__name__}"
        expected_keys = set(expected.keys())
        actual_keys = set(actual.keys())
        assert actual_keys == expected_keys, (
            f"key mismatch at {path}: "
            f"missing={sorted(expected_keys - actual_keys)}, extra={sorted(actual_keys - expected_keys)}"
        )
        for key in sorted(expected_keys):
            compare_json(expected[key], actual[key], path_parts + [key], stats)
        return

    if isinstance(expected, list):
        assert isinstance(actual, list), f"type mismatch at {path}: expected list, got {type(actual).__name__}"
        assert len(actual) == len(expected), f"list length mismatch at {path}: expected {len(expected)}, got {len(actual)}"
        for idx, (expected_item, actual_item) in enumerate(zip(expected, actual)):
            compare_json(expected_item, actual_item, path_parts + [idx], stats)
        return

    assert actual == expected, f"value mismatch at {path}: expected {expected!r}, got {actual!r}"
    stats.exact_fields += 1


def recompute_output(tmp_output):
    result = subprocess.run(
        [
            sys.executable,
            str(COMPUTE_SCRIPT),
            "--shared-dir",
            str(SHARED_DIR),
            "--output-dir",
            str(tmp_output),
        ],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_recomputed_output_matches_formal_output_with_numeric_tolerance():
    assert_shared_inputs_available()
    assert FORMAL_OUTPUT_DIR.exists(), f"formal output dir missing: {FORMAL_OUTPUT_DIR}"

    with tempfile.TemporaryDirectory(prefix="canglu-radar-output-diff-") as tmp:
        tmp_output = Path(tmp)
        recompute_output(tmp_output)

        stats = DiffStats()
        for file_name in OUTPUT_FILES:
            expected = load_json(FORMAL_OUTPUT_DIR / file_name)
            actual = load_json(tmp_output / file_name)
            compare_json(expected, actual, [file_name], stats)

        assert stats.numeric_fields > 0, "no numeric fields were compared"
        assert stats.exact_fields > 0, "no exact fields were compared"


def run_all():
    test_recomputed_output_matches_formal_output_with_numeric_tolerance()
    print("compute output numeric diff smoke test passed")


if __name__ == "__main__":
    run_all()
