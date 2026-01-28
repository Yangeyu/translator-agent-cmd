# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 在此代码仓库中工作时提供指导。

## 项目概述

Y-Translator CLI 是一个基于 AI 的英汉翻译命令行工具。作为 Python 包通过 PyPI 分发，使用 `trans` 命令启动。

## 开发命令

```bash
# 以开发模式安装（可编辑安装）
pip install -e .

# 构建包
./build.sh          # 自动构建脚本（包含清理）
python -m build     # 直接构建命令

# 运行测试
pytest

# 运行特定测试
pytest tests/test_cli.py

# 手动清理构建产物
rm -rf dist/ build/ *.egg-info/ __pycache__/ .pytest_cache/
```

## 架构设计

代码库采用分层架构，各层职责清晰：

```
用户输入 → CLI → 配置 → 翻译代理 → Agno 框架 → AI 模型 → 输出
```

### 核心组件

- **`translator/cli.py`**：入口点和主要 CLI 逻辑，使用 `prompt_toolkit` 实现交互式会话。处理彩色输出和流式响应。

- **`translator/config.py`**：使用 dataclasses 的配置管理。支持环境变量（`AI_API_KEY`、`AI_MODEL`、`AI_API_BASE`）和 CLI 参数。

- **`translator/agent.py`**：使用 `agno` 库的 AI 翻译代理封装。使用 `OpenAILike` 类兼容 OpenAI API 模型。代理严格配置为仅用于翻译（不处理问答）。

- **`translator/__init__.py`**：包元数据和版本定义（当前为 0.1.3）。

### 关键依赖

- `agno>=0.1.0` - AI 代理框架
- `prompt_toolkit>=3.0.0` - 交互式 CLI 输入处理
- `python-dotenv>=0.19.0` - 环境变量管理

## 配置

应用按优先级顺序接受配置：
1. CLI 参数（`--api-key`、`--model`、`--api-base`、`--verbose`）
2. 环境变量（`AI_API_KEY`、`AI_MODEL`、`AI_API_BASE`）

默认模型为 `gpt-4`。代理使用 OpenAI 兼容的 API，允许通过自定义 base URL 使用其他提供商。
