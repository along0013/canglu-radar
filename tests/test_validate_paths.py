#!/usr/bin/env python3
"""Regression tests for validate.py path resolution.

These tests intentionally avoid external test dependencies so they can run with:

    $BOX_AGENT_PYTHON tests/test_validate_paths.py
"""

import importlib.util
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
VALIDATE_PATH = PROJECT_ROOT / "engine" / "validate.py"

spec = importlib.util.spec_from_file_location("validate_module", VALIDATE_PATH)
validate = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validate)


def test_relative_output_resolves_from_cwd_first():
    previous = Path.cwd()
    try:
        os.chdir(PROJECT_ROOT)
        assert Path(validate.resolve_data_dir("output")) == PROJECT_ROOT / "output"
    finally:
        os.chdir(previous)


def test_absolute_output_is_preserved():
    output = PROJECT_ROOT / "output"
    assert Path(validate.resolve_data_dir(str(output))) == output


def test_missing_relative_path_falls_back_to_script_dir():
    missing = "definitely-missing-data-dir"
    resolved = Path(validate.resolve_data_dir(missing))
    assert resolved == PROJECT_ROOT / "engine" / missing


def run_all():
    test_relative_output_resolves_from_cwd_first()
    test_absolute_output_is_preserved()
    test_missing_relative_path_falls_back_to_script_dir()
    print("validate path regression tests passed")


if __name__ == "__main__":
    run_all()
