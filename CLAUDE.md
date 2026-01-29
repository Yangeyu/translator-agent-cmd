# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 提供在此代码库中工作的指导。

## 项目概述

Y-Translator CLI 是一个 AI 驱动的命令行翻译工具，支持中英文互译。项目使用 `agno` 库实现 AI 代理功能，使用 `prompt_toolkit` 提供交互式命令行界面。

## 开发命令

### 安装
```bash
# 以开发/可编辑模式安装
pip install -e .
```

### 构建
```bash
# 构建包
python -m build

# 构建前清理旧的构建产物（推荐）
rm -rf dist/ build/ *.egg-info/ __pycache__/ .pytest_cache/
find . -name "*.pyc" -delete
python -m build
```

### 测试
```bash
# 运行测试
pytest
```

### 运行 CLI
```bash
# 运行翻译器
trans

# 带选项运行
trans --verbose --model gpt-3.5-turbo -n
```

## 架构

### 包结构
- `translator/` - 主包目录
  - `cli.py` - 命令行入口、参数解析、交互式会话循环
  - `config.py` - 配置数据类，支持环境变量
  - `agent.py` - AI 代理封装，使用 agno.Agent 和 OpenAILike 模型
  - `__init__.py` - 包初始化，导出 `__version__`

### 核心组件

**Config** (`translator/config.py`)：从命令行参数或环境变量（`AI_API_KEY`、`AI_MODEL`、`AI_API_BASE`）加载配置的数据类。

**TranslatorAgent** (`translator/agent.py`)：封装 `agno.agent.Agent`，内置预定义的指令集。代理配置为：
- 仅执行翻译（不回答问题）
- 中文输入 → 英文输出
- 英文输入 → 中文输出
- 默认启用流式响应

**CLI** (`translator/cli.py`)：使用 `prompt_toolkit.PromptSession` 和 `InMemoryHistory` 实现 REPL 界面。入口点是 `main()` 函数。

### 入口点
控制台脚本入口点在 `setup.py` 中定义为 `trans=translator.cli:main`。

## 配置

应用可通过以下方式配置：
- 命令行参数：`--api-key`、`--model`、`--api-base`、`--verbose`、`--no-stream`
- 环境变量：`AI_API_KEY`、`AI_MODEL`、`AI_API_BASE`

默认模型为 `gpt-4`，默认 API 基础 URL 为 `https://api.openai.com/v1`。
