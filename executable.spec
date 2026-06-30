# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['executable.py'],
    pathex=[],
    binaries=[],
    datas=[('Character1.png', '.'), ('Character2.png', '.'), ('Enemy1.png', '.'), ('Enemy2.png', '.'), ('Level_1.png', '.'), ('Level_2.png', '.'), ('Level_3.png', '.'), ('Main_menu.png', '.'), ('Platform.png', '.'), ('exit.png', '.'), ('coin.png', '.'), ('coin.mp3', '.'), ('death.mp3', '.'), ('win.mp3', '.'), ('unlock_door.mp3', '.'), ('Game_music.mp3', '.'), ('Main_menu_music.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='executable',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
