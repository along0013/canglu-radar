#!/usr/bin/env python3
"""P0 smoke tests for the generated output JSON package.

Run directly with:

    $BOX_AGENT_PYTHON tests/test_output_smoke.py
"""

import json
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "output"
VALIDATE_SCRIPT = PROJECT_ROOT / "engine" / "validate.py"

REQUIRED_FILES = {
    "metrics.json": "routes",
    "history.json": "datasets",
    "scenarios.json": "scenarios",
    "decisions.json": "decisions",
    "indices.json": "indices",
}

ROUTE_CODES = {"EUR", "MED", "USWC", "USEC", "COMPOSITE"}
SCENARIO_ROUTES = {"USWC", "USEC"}


def load_json(name):
    path = OUTPUT_DIR / name
    assert path.exists(), f"missing output file: {path}"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def assert_meta(payload, name):
    meta = payload.get("_meta")
    assert isinstance(meta, dict), f"{name} missing _meta"
    assert meta.get("version") == "5.0", f"{name} version mismatch"
    assert meta.get("latest_week"), f"{name} missing latest_week"
    assert isinstance(meta.get("fx_rate"), (int, float)), f"{name} missing numeric fx_rate"
    return meta


def test_required_files_parse_and_have_core_sections():
    for file_name, section in REQUIRED_FILES.items():
        payload = load_json(file_name)
        assert_meta(payload, file_name)
        assert section in payload, f"{file_name} missing section {section}"
        assert isinstance(payload[section], list), f"{file_name}.{section} must be a list"
        assert payload[section], f"{file_name}.{section} must not be empty"


def test_meta_consistency_across_output_package():
    metas = {name: assert_meta(load_json(name), name) for name in REQUIRED_FILES}
    latest_weeks = {meta["latest_week"] for meta in metas.values()}
    fx_rates = {meta["fx_rate"] for meta in metas.values()}
    assert len(latest_weeks) == 1, f"latest_week mismatch: {latest_weeks}"
    assert len(fx_rates) == 1, f"fx_rate mismatch: {fx_rates}"


def test_metrics_and_decisions_cover_same_routes():
    metrics = load_json("metrics.json")["routes"]
    decisions = load_json("decisions.json")["decisions"]
    metric_codes = {row.get("code") for row in metrics}
    decision_codes = {row.get("code") for row in decisions}
    assert metric_codes == ROUTE_CODES, f"unexpected metrics routes: {metric_codes}"
    assert decision_codes == ROUTE_CODES, f"unexpected decision routes: {decision_codes}"
    assert metric_codes == decision_codes, "metrics and decisions route sets differ"


def test_history_and_scenarios_have_expected_route_coverage():
    history = load_json("history.json")["datasets"]
    scenarios = load_json("scenarios.json")["scenarios"]
    history_codes = {row.get("code") for row in history}
    scenario_routes = {row.get("route_code") for row in scenarios}
    assert history_codes == ROUTE_CODES, f"unexpected history routes: {history_codes}"
    assert scenario_routes == SCENARIO_ROUTES, f"unexpected scenario routes: {scenario_routes}"


def test_validate_cli_accepts_project_relative_output():
    result = subprocess.run(
        [sys.executable, str(VALIDATE_SCRIPT), "--data-dir", "output"],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    normalized_stdout = result.stdout.replace(" ", "")
    assert "ERROR:0" in normalized_stdout, result.stdout
    assert "WARNING:0" in normalized_stdout, result.stdout


def run_all():
    test_required_files_parse_and_have_core_sections()
    test_meta_consistency_across_output_package()
    test_metrics_and_decisions_cover_same_routes()
    test_history_and_scenarios_have_expected_route_coverage()
    test_validate_cli_accepts_project_relative_output()
    print("output package smoke tests passed")


if __name__ == "__main__":
    run_all()
