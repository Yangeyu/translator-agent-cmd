# Y-Translator CLI

An AI-powered command-line translator that converts between English and Chinese.

## Installation

### From PyPI (pip)

```bash
pip install y-translator-cli
```

### With uv tool (recommended)

Install from PyPI:
```bash
uv tool install y-translator-cli
```

Or install from source:
```bash
git clone https://github.com/yourusername/y-translator.git
cd y-translator
uv tool install -e .
```

## Usage

Start the translator:
```bash
trans
```

Or translate text directly:
```bash
trans "Hello, world!"
trans "你好，世界！"
```

Options:
- `-h, --help`: Show help message
- `-v, --version`: Show version information
- `--verbose`: Enable debug mode
- `--model MODEL`: Specify AI model to use (default: qwen3.6-flash)
- `--api-key KEY`: Set DashScope API key
- `-n, --no-stream`: Disable streaming mode

## Environment Variables

You can set the following environment variables:
- `DASHSCOPE_API_KEY`: Your DashScope API key
- `AI_MODEL`: AI model to use (default: qwen3.6-flash)

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
trans --model qwen3.6-flash
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

# Install with uv
uv sync --dev
```

### Dependencies

The project depends on the following packages:
- `prompt_toolkit>=3.0.0` - Interactive command-line interface
- `agno>=0.1.0` - AI agent framework (with DashScope provider)
- `python-dotenv>=0.19.0` - Environment variable management
- `socksio` - SOCKS proxy support

### Building the Package

```bash
# Build with uv
uv build
```

### Publishing to PyPI

1. **Get PyPI API Token**:
   - Login to https://pypi.org
   - Go to Account settings → API tokens
   - Create a new API token (recommended: project-scoped, e.g., `y-translator-cli`)

2. **Upload to PyPI with uv**:
   ```bash
   uv publish
   ```

3. **Version Bump** (if version already exists):
   PyPI does not allow overwriting existing versions. If you get a "File already exists" error:
   - Update `__version__` in `translator/__init__.py`
   - Rebuild: `uv build`
   - Upload again: `uv publish`

## License

MIT License 