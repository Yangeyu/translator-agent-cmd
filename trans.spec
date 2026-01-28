# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Y-Translator CLI
Builds a standalone executable with all dependencies bundled.
"""

import sys

block_cipher = None

a = Analysis(
    ['trans_main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'agno',
        'agno.agent',
        'agno.models',
        'agno.models.openai',
        'agno.models.openai.like',
        'prompt_toolkit',
        'prompt_toolkit.history',
        'prompt_toolkit.shortcuts',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='trans',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
