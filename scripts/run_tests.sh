#!/bin/bash

# Restaurant Web App Test Runner
# AI-Generated with DeepSeek assistance

echo "========================================="
echo "Restaurant Web App Test Suite"
echo "========================================="

# Set environment variables
export PYTHONPATH=$(pwd)/src:$PYTHONPATH

# Create reports directory
mkdir -p documentation/reports/screenshots

# Run static analysis
echo "Running static analysis..."
python -m py_compile src/**/*.py

# Run unit tests
echo "Running unit tests..."
pytest src/tests/unit_tests.py -v --html=documentation/reports/unit_test_report.html

# Run integration tests
echo "Running integration tests..."
pytest src/tests/integration_tests.py -v --html=documentation/reports/integration_test_report.html

# Run Selenium tests
echo "Running Selenium tests..."
python src/tests/test_suite.py

echo "========================================="
echo "Test execution complete!"
echo "Reports available in documentation/reports/"
echo "========================================="