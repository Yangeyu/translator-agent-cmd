# Y-Translator CLI

An AI-powered command-line translator that converts between English and Chinese.

## Installation

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

### Dependencies

The project depends on the following packages:
- `prompt_toolkit>=3.0.0` - Interactive command-line interface
- `agno>=0.1.0` - AI agent framework
- `python-dotenv>=0.19.0` - Environment variable management
- `openai` - OpenAI API client
- `socksio` - SOCKS proxy support

### Building the Package

```bash
# Use build
python -m build
```

If building manually, you may want to clean old files first:
```bash
# Clean before building
rm -rf dist/ build/ *.egg-info/ __pycache__/ .pytest_cache/
find . -name "*.pyc" -delete
python -m build
```

### Publishing to PyPI

1. **Get PyPI API Token**:
   - Login to https://pypi.org
   - Go to Account settings → API tokens
   - Create a new API token (recommended: project-scoped, e.g., `y-translator-cli`)

2. **Set Environment Variables** (recommended):
   ```bash
   export TWINE_USERNAME="__token__"
   export TWINE_PASSWORD="pypi-xxxx..."  # Your API token
   ```

   Or create `~/.pypirc`:
   ```ini
   [pypi]
   username = __token__
   password = pypi-xxxx...
   ```

3. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

4. **Version Bump** (if version already exists):
   PyPI does not allow overwriting existing versions. If you get a "File already exists" error:
   - Update `__version__` in `translator/__init__.py`
   - Rebuild: `rm -rf dist/ build/ *.egg-info/ && python -m build`
   - Upload again: `twine upload dist/*`

## License

MIT License 