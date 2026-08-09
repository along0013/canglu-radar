#!/usr/bin/env python3
"""P0 field contract tests for dashboard/demo-v3.html and output JSON.

The current dashboard is a static HTML demo with embedded data constants. This
smoke test verifies that the fields actually consumed by the dashboard still
exist in the generated output package and that the embedded dashboard snapshot
keeps the same route/index/scenario coverage as output/.

Run directly with:

    $BOX_AGENT_PYTHON tests/test_dashboard_contract.py
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "output"
DASHBOARD_HTML = PROJECT_ROOT / "dashboard" / "demo-v3.html"

ROUTE_CODES = {"EUR", "MED", "USWC", "USEC", "COMPOSITE"}
SCENARIO_CODES = {"BASE_USEC", "BASE_USWC", "STRESS_USEC", "STRESS_USWC", "USEC_PANAMA_STRESS"}
DASHBOARD_SCENARIO_CODES = {"BASE_USEC", "BASE_USWC", "STRESS_USEC", "STRESS_USWC", "USEC_PANAMA"}
SCENARIO_ROUTES = {"USWC", "USEC"}

DASHBOARD_REQUIRED_TOKENS = {
    "ROUTES": ["code", "name", "unit", "val", "z", "wow", "streak", "level", "tags", "color"],
    "HISTORY": ["labels", "datasets", "code", "name", "color", "data"],
    "SCENARIOS": ["code", "name", "total_usd", "total_cny", "risk", "desc"],
    "DECISIONS": ["code", "name", "level", "advice", "tags", "conf"],
    "INDICES": ["name", "val", "unit", "date", "ql", "status"],
}

OUTPUT_REQUIRED_FIELDS = {
    "metrics.json": {
        "section": "routes",
        "fields": {"code", "name", "unit", "current_value", "z_score", "wow_change_pct", "up_streak_weeks", "warning_level", "warning_tags"},
    },
    "history.json": {
        "section": "datasets",
        "fields": {"code", "name", "unit", "color", "data"},
    },
    "scenarios.json": {
        "section": "scenarios",
        "fields": {"code", "name", "route_code", "total_cost_usd", "total_cost_cny", "risk_level", "description"},
    },
    "decisions.json": {
        "section": "decisions",
        "fields": {"code", "name", "warning_level", "suggestion", "confidence", "source_metrics"},
    },
    "indices.json": {
        "section": "indices",
        "fields": {"name", "value", "unit", "date", "quality_level", "status"},
    },
}

FIELD_ALIASES = {
    "routes": {
        "val": "current_value",
        "z": "z_score",
        "wow": "wow_change_pct",
        "streak": "up_streak_weeks",
        "level": "warning_level",
        "tags": "warning_tags",
    },
    "scenarios": {
        "total_usd": "total_cost_usd",
        "total_cny": "total_cost_cny",
        "risk": "risk_level",
        "desc": "description",
    },
    "decisions": {
        "level": "warning_level",
        "advice": "suggestion",
        "conf": "confidence",
        "tags": "source_metrics.warning_tags",
    },
    "indices": {
        "val": "value",
        "ql": "quality_level",
    },
}


def load_json(name):
    with (OUTPUT_DIR / name).open("r", encoding="utf-8") as f:
        return json.load(f)


def read_dashboard():
    return DASHBOARD_HTML.read_text(encoding="utf-8")


def require_fields(rows, fields, section):
    assert rows, f"{section} must not be empty"
    for idx, row in enumerate(rows):
        missing = fields - set(row)
        assert not missing, f"{section}[{idx}] missing fields: {sorted(missing)}"


def test_dashboard_html_contains_consumed_data_constants_and_tokens():
    html = read_dashboard()
    for constant_name, tokens in DASHBOARD_REQUIRED_TOKENS.items():
        assert f"const {constant_name}" in html, f"dashboard missing const {constant_name}"
        for token in tokens:
            assert re.search(rf"\b{re.escape(token)}\b", html), f"dashboard missing token {constant_name}.{token}"


def test_output_package_exposes_dashboard_source_fields():
    for file_name, spec in OUTPUT_REQUIRED_FIELDS.items():
        payload = load_json(file_name)
        rows = payload[spec["section"]]
        require_fields(rows, spec["fields"], f"{file_name}.{spec['section']}")


def test_dashboard_field_aliases_are_backed_by_output_fields():
    metrics_fields = set(load_json("metrics.json")["routes"][0])
    scenario_fields = set(load_json("scenarios.json")["scenarios"][0])
    decision_fields = set(load_json("decisions.json")["decisions"][0])
    index_fields = set(load_json("indices.json")["indices"][0])

    field_sets = {
        "routes": metrics_fields,
        "scenarios": scenario_fields,
        "decisions": decision_fields,
        "indices": index_fields,
    }

    for section, aliases in FIELD_ALIASES.items():
        for dashboard_field, output_field in aliases.items():
            root_field = output_field.split(".")[0]
            assert root_field in field_sets[section], f"{section}: {dashboard_field} not backed by {output_field}"


def test_dashboard_snapshot_coverage_matches_output_package():
    html = read_dashboard()

    metric_codes = {row["code"] for row in load_json("metrics.json")["routes"]}
    decision_codes = {row["code"] for row in load_json("decisions.json")["decisions"]}
    history_codes = {row["code"] for row in load_json("history.json")["datasets"]}
    scenario_codes = {row["code"] for row in load_json("scenarios.json")["scenarios"]}
    scenario_routes = {row["route_code"] for row in load_json("scenarios.json")["scenarios"]}
    index_names = {row["name"] for row in load_json("indices.json")["indices"]}

    assert metric_codes == ROUTE_CODES
    assert decision_codes == ROUTE_CODES
    assert history_codes == ROUTE_CODES
    assert scenario_codes == SCENARIO_CODES
    assert scenario_routes == SCENARIO_ROUTES

    for code in ROUTE_CODES | DASHBOARD_SCENARIO_CODES:
        assert code in html, f"dashboard embedded snapshot missing code {code}"
    index_aliases = {
        "上海出口集装箱运价指数": "SCFI 上海出口集装箱",
        "中国出口集装箱运价指数": "CCFI 中国出口集装箱",
        "上海出口集装箱结算运价指数(欧洲)": "SCFIS 结算运价(欧洲)",
        "Drewry World Container Index": "Drewry WCI",
        "Freightos Baltic Index": "Freightos FBX",
        "波罗的海干散货运价指数": "BDI 波罗的海干散货",
        "布伦特原油期货": "布伦特原油",
    }
    for name in index_names:
        expected_label = index_aliases.get(name, name)
        assert expected_label in html, f"dashboard embedded snapshot missing index {name} as {expected_label}"


def test_dashboard_snapshot_meta_matches_output_meta():
    html = read_dashboard()
    meta = load_json("metrics.json")["_meta"]
    assert f'"version":"{meta["version"]}"' in html
    assert f'"latest_week":"{meta["latest_week"]}"' in html
    assert f'"fx_rate":{meta["fx_rate"]}' in html


def run_all():
    test_dashboard_html_contains_consumed_data_constants_and_tokens()
    test_output_package_exposes_dashboard_source_fields()
    test_dashboard_field_aliases_are_backed_by_output_fields()
    test_dashboard_snapshot_coverage_matches_output_package()
    test_dashboard_snapshot_meta_matches_output_meta()
    print("dashboard field contract tests passed")


if __name__ == "__main__":
    run_all()
