# Y-Translator CLI

An AI-powered command-line translator that converts between English and Chinese.

## Installation

### Option 1: Standalone Executable (Recommended)

Download the pre-built executable - no Python or dependencies required!

**macOS / Linux**:
```bash
# Download
curl -O https://github.com/yourusername/y-translator/releases/latest/download/trans

# Add execute permission
chmod +x trans

# (Optional) Install to system path
sudo mv trans /usr/local/bin/
```

**Windows**:
```powershell
# Download trans.exe from releases
# Add to PATH or run directly
```

### Option 2: Install via pip

```bash
pip install y-translator-cli
```

## Usage

Start the translator:
```bash
trans
```

Options:
- `-h, --help`: Show help message
- `-v, --version`: Show version information
- `--verbose`: Enable debug mode
- `--model MODEL`: Specify AI model to use (default: gpt-4)
- `--api-key KEY`: Set OpenAI API key
- `--api-base URL`: Set custom API base URL
- `-n, --no-stream`: Disable streaming mode

## Environment Variables

You can set the following environment variables:
- `AI_API_KEY`: Your OpenAI API key
- `AI_MODEL`: AI model to use (default: gpt-4)
- `AI_API_BASE`: Custom API base URL

## Examples

1. Start the translator:
```bash
trans
```

2. Enable debug mode:
```bash
trans --verbose
```

3. Use a specific model:
```bash
trans --model gpt-3.5-turbo
```

4. Disable streaming output:
```bash
trans -n
```

## Development

### Installation for Development

```bash
# Clone the repository
git clone https://github.com/yourusername/y-translator.git
cd y-translator

# Install in development mode
pip install -e .
```

### Building the Python Package

```bash
# Use the build script
./build.sh

# Or use build directly
python -m build
```

### Building the Standalone Executable

Build a single executable that includes all dependencies:

**macOS / Linux**:
```bash
# Install PyInstaller
pip install pyinstaller

# Build the executable
./build_exe.sh

# The output will be in dist/trans
```

**Windows**:
```batch
REM Install PyInstaller
pip install pyinstaller

REM Build the executable
build_exe.bat

REM The output will be in dist\trans.exe
```

The standalone executable includes all dependencies and can be distributed as a single file (~100MB).

### Clean Build Artifacts

```bash
# Clean Python package build files
rm -rf dist/ build/ *.egg-info/ __pycache__/ .pytest_cache/
find . -name "*.pyc" -delete

# Clean PyInstaller build files
rm -rf build/ dist/*.spec
```

## License

MIT License 