#!/usr/bin/env bash

set -eo pipefail

BLACK_ACTION="--check"
ISORT_ACTION="--check-only"

function usage
{
    echo "usage: run_tests.sh [--format-code]"
    echo ""
    echo " --format-code : Format the code instead of checking formatting."
    exit 1
}

while [[ $# -gt 0 ]]; do
    arg="$1"
    case $arg in
        --format-code)
        BLACK_ACTION="--quiet"
        ISORT_ACTION=""
        ;;
        -h|--help)
        usage
        ;;
        "")
        # ignore
        ;;
        *)
        echo "Unexpected argument: ${arg}"
        usage
        ;;
    esac
    shift
done

# only generate html locally
pytest --cov plugin_scripts/ tests --cov-report html

echo "Running MyPy..."
mypy plugin_scripts tests

echo "Running isort..."
isort ${ISORT_ACTION} plugin_scripts tests

echo "Running black..."
black ${BLACK_ACTION} plugin_scripts tests

echo "Running flake8..."
flake8 plugin_scripts tests

echo "Running bandit..."
bandit --ini .bandit --quiet -r plugin_scripts tests
