#!/bin/bash
# Build script for creating standalone executable using PyInstaller

set -e

echo "Building Y-Translator CLI standalone executable..."
echo ""

# Check if PyInstaller is installed
if ! python -m pip show pyinstaller > /dev/null 2>&1; then
    echo "PyInstaller not found. Installing..."
    python -m pip install --upgrade pyinstaller
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build/ dist/*.spec

# Build the executable
echo "Building executable..."
pyinstaller trans.spec --clean

echo ""
echo "Build complete!"
echo "Executable: dist/trans"
echo ""
echo "To test:"
echo "  ./dist/trans --help"
echo ""
echo "To install system-wide:"
echo "  sudo cp dist/trans /usr/local/bin/"
