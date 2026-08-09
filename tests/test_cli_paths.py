#!/usr/bin/env python3
"""Regression tests for engine CLI path resolution helpers.

Run with:

    $BOX_AGENT_PYTHON tests/test_cli_paths.py
"""

import importlib.util
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


validate = load_module("validate_module", PROJECT_ROOT / "engine" / "validate.py")
compute = load_module("compute_module", PROJECT_ROOT / "engine" / "compute.py")


def test_validate_relative_output_resolves_from_cwd_first():
    previous = Path.cwd()
    try:
        os.chdir(PROJECT_ROOT)
        assert Path(validate.resolve_data_dir("output")) == PROJECT_ROOT / "output"
    finally:
        os.chdir(previous)


def test_validate_absolute_output_is_preserved():
    output = PROJECT_ROOT / "output"
    assert Path(validate.resolve_data_dir(str(output))) == output


def test_validate_missing_relative_path_falls_back_to_script_dir():
    missing = "definitely-missing-data-dir"
    resolved = Path(validate.resolve_data_dir(missing))
    assert resolved == PROJECT_ROOT / "engine" / missing


def test_compute_output_resolves_from_cwd_first():
    previous = Path.cwd()
    try:
        os.chdir(PROJECT_ROOT)
        assert Path(compute.resolve_cli_path("output", fallback_base=PROJECT_ROOT)) == PROJECT_ROOT / "output"
    finally:
        os.chdir(previous)


def test_compute_missing_relative_path_uses_cwd_without_fallback_when_no_base():
    previous = Path.cwd()
    try:
        os.chdir(PROJECT_ROOT)
        missing = "definitely-missing-output-dir"
        assert Path(compute.resolve_cli_path(missing)) == PROJECT_ROOT / missing
    finally:
        os.chdir(previous)


def test_compute_missing_relative_path_falls_back_when_base_given():
    missing = "definitely-missing-shared-dir"
    resolved = Path(compute.resolve_cli_path(missing, fallback_base=PROJECT_ROOT / "engine"))
    assert resolved == PROJECT_ROOT / "engine" / missing


def run_all():
    test_validate_relative_output_resolves_from_cwd_first()
    test_validate_absolute_output_is_preserved()
    test_validate_missing_relative_path_falls_back_to_script_dir()
    test_compute_output_resolves_from_cwd_first()
    test_compute_missing_relative_path_uses_cwd_without_fallback_when_no_base()
    test_compute_missing_relative_path_falls_back_when_base_given()
    print("engine CLI path regression tests passed")


if __name__ == "__main__":
    run_all()
