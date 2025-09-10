#!/bin/bash

# Run code formatter
echo "Running Black code formatter..."
black src tests

# Run linting (flake8)
echo "Running Flake8 linting..."
flake8 src tests

echo "Formatting and linting completed."
