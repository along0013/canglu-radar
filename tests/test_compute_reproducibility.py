#!/usr/bin/env python3
"""P0 smoke test for recomputing the output JSON package from shared inputs.

This test runs compute.py against the project-local shared fixture by default
and writes to a temporary directory, so the committed/formal output/ package is
never modified. Set CANGLU_SHARED_DIR to use a full real shared/ input directory
locally.

Run directly with:

    $BOX_AGENT_PYTHON tests/test_compute_reproducibility.py
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_SHARED_DIR = PROJECT_ROOT / "tests" / "fixtures" / "shared"
SHARED_DIR = Path(os.environ.get("CANGLU_SHARED_DIR", FIXTURE_SHARED_DIR)).resolve()
COMPUTE_SCRIPT = PROJECT_ROOT / "engine" / "compute.py"
VALIDATE_SCRIPT = PROJECT_ROOT / "engine" / "validate.py"

REQUIRED_SHARED_FILES = {
    "scfi-26w.csv",
    "surcharge-scenarios.csv",
    "index-comparison.csv",
    "usd-cny-26w.csv",
}

REQUIRED_OUTPUT_FILES = {
    "metrics.json": "routes",
    "history.json": "datasets",
    "scenarios.json": "scenarios",
    "decisions.json": "decisions",
    "indices.json": "indices",
}

ROUTE_CODES = {"EUR", "MED", "USWC", "USEC", "COMPOSITE"}
SCENARIO_ROUTES = {"USWC", "USEC"}


def assert_shared_inputs_available():
    assert SHARED_DIR.exists(), f"shared input dir missing: {SHARED_DIR}"
    missing = sorted(name for name in REQUIRED_SHARED_FILES if not (SHARED_DIR / name).exists())
    assert not missing, f"shared input files missing: {missing}"


def load_json(output_dir, name):
    path = output_dir / name
    assert path.exists(), f"missing generated output file: {path}"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def assert_meta(payload, name):
    meta = payload.get("_meta")
    assert isinstance(meta, dict), f"{name} missing _meta"
    assert meta.get("version") == "5.0", f"{name} version mismatch"
    assert meta.get("latest_week"), f"{name} missing latest_week"
    assert isinstance(meta.get("fx_rate"), (int, float)), f"{name} missing numeric fx_rate"
    return meta


def assert_output_package_contract(output_dir):
    metas = {}
    for file_name, section in REQUIRED_OUTPUT_FILES.items():
        payload = load_json(output_dir, file_name)
        metas[file_name] = assert_meta(payload, file_name)
        assert section in payload, f"{file_name} missing section {section}"
        assert isinstance(payload[section], list), f"{file_name}.{section} must be a list"
        assert payload[section], f"{file_name}.{section} must not be empty"

    latest_weeks = {meta["latest_week"] for meta in metas.values()}
    fx_rates = {meta["fx_rate"] for meta in metas.values()}
    assert len(latest_weeks) == 1, f"latest_week mismatch: {latest_weeks}"
    assert len(fx_rates) == 1, f"fx_rate mismatch: {fx_rates}"

    metrics = load_json(output_dir, "metrics.json")["routes"]
    decisions = load_json(output_dir, "decisions.json")["decisions"]
    history = load_json(output_dir, "history.json")["datasets"]
    scenarios = load_json(output_dir, "scenarios.json")["scenarios"]

    metric_codes = {row.get("code") for row in metrics}
    decision_codes = {row.get("code") for row in decisions}
    history_codes = {row.get("code") for row in history}
    scenario_routes = {row.get("route_code") for row in scenarios}

    assert metric_codes == ROUTE_CODES, f"unexpected metrics routes: {metric_codes}"
    assert decision_codes == ROUTE_CODES, f"unexpected decision routes: {decision_codes}"
    assert history_codes == ROUTE_CODES, f"unexpected history routes: {history_codes}"
    assert metric_codes == decision_codes == history_codes, "route sets differ across generated outputs"
    assert scenario_routes == SCENARIO_ROUTES, f"unexpected scenario routes: {scenario_routes}"


def test_compute_rebuilds_valid_output_package_from_shared_inputs():
    assert_shared_inputs_available()
    with tempfile.TemporaryDirectory(prefix="canglu-radar-compute-") as tmp:
        tmp_output = Path(tmp)
        compute_result = subprocess.run(
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
        assert compute_result.returncode == 0, compute_result.stdout + compute_result.stderr

        assert_output_package_contract(tmp_output)

        validate_result = subprocess.run(
            [sys.executable, str(VALIDATE_SCRIPT), "--data-dir", str(tmp_output)],
            cwd=PROJECT_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        assert validate_result.returncode == 0, validate_result.stdout + validate_result.stderr
        normalized_stdout = validate_result.stdout.replace(" ", "")
        assert "ERROR:0" in normalized_stdout, validate_result.stdout
        assert "WARNING:0" in normalized_stdout, validate_result.stdout


def run_all():
    test_compute_rebuilds_valid_output_package_from_shared_inputs()
    print("compute reproducibility smoke test passed")


if __name__ == "__main__":
    run_all()
