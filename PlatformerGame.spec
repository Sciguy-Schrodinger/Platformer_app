# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['platformer.py'],
    pathex=[],
    binaries=[],
    datas=[('Character1.png', '.'), ('Character2.png', '.'), ('Enemy1.png', '.'), ('Enemy2.png', '.'), ('Level_1.png', '.'), ('Level_2.png', '.'), ('Level_3.png', '.'), ('Platform.png', '.'), ('coin.png', '.'), ('exit.png', '.'), ('Main_menu.png', '.'), ('coin.mp3', '.'), ('death.mp3', '.'), ('Game_music.mp3', '.'), ('Main_menu_music.mp3', '.'), ('unlock_door.mp3', '.'), ('win.mp3', '.')],
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
    name='PlatformerGame',
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
