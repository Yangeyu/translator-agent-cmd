"""Configuration management for Y-Translator CLI"""

import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    """Configuration settings for Y-Translator CLI"""
    api_key: str = os.getenv("DASHSCOPE_API_KEY", "")
    model: str = os.getenv("AI_MODEL", "qwen3.6-flash")
    api_base: str = os.getenv("DASHSCOPE_API_BASE", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    debug: bool = False
    
    @classmethod
    def from_args(cls, args) -> 'Config':
        """Create config from command line arguments"""
        return cls(
            api_key=args.api_key or os.getenv("DASHSCOPE_API_KEY", ""),
            model=args.model or os.getenv("AI_MODEL", "qwen3.6-flash"),
            api_base=args.api_base or os.getenv("DASHSCOPE_API_BASE", "https://dashscope.aliyuncs.com/compatible-mode/v1"),
            debug=args.verbose,
        )
