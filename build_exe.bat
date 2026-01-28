@echo off
REM Build script for creating standalone executable using PyInstaller (Windows)

echo Building Y-Translator CLI standalone executable...
echo.

REM Check if PyInstaller is installed
python -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    python -m pip install --upgrade pyinstaller
)

REM Clean previous builds
echo Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist\*.spec del /q dist\*.spec

REM Build the executable
echo Building executable...
pyinstaller trans.spec --clean

echo.
echo Build complete!
echo Executable: dist\trans.exe
echo.
echo To test:
echo   dist\trans.exe --help
echo.
