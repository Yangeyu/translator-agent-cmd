#!/bin/bash

# Exit on error
set -e

echo "Building Y-Translator CLI package..."

# Clean up old build files
echo "Cleaning up old build files..."
rm -rf dist/ build/ y_translator_cli.egg-info/ translator_cli.egg-info/ translator.egg-info/
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete

# Ensure build package is installed
if ! python -m pip show build > /dev/null 2>&1; then
    echo "Installing build dependencies..."
    python -m pip install --upgrade build
fi

# Build the package
echo "Building distribution packages..."
python -m build

# Output success
echo "Build complete!"
echo "Distribution files created in dist/ directory"
echo ""
echo "To install locally (development):"
echo "  pip install -e ."
echo ""
echo "To upload to PyPI:"
echo "  python -m pip install --upgrade twine"
echo "  python -m twine upload dist/*"

# Make the script executable
chmod +x "$(realpath "$0")" 