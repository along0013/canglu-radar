#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PYTHON_BIN="${BOX_AGENT_PYTHON:-python3}"

cd "${PROJECT_ROOT}"
exec "${PYTHON_BIN}" tests/run_smoke_tests.py
