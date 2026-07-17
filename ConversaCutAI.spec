# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all


datas = []

datas += collect_all("customtkinter")[0]
datas += collect_all("silero_vad")[0]
datas += collect_all("torch")[0]
datas += collect_all("torchaudio")[0]

datas += [
    (
        "assets/logo.png",
        "assets"
    ),
    (
        "config.json",
        "."
    )
]


a = Analysis(
    ["app.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        "torch",
        "torchaudio",
        "silero_vad",
        "pydub",
        "soundfile",
        "numpy",
        "PIL"
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False
)


pyz = PYZ(a.pure)


exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="ConversaCutAI",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon="assets/logo.ico",
    version="version_info.txt"
)