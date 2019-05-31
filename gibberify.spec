# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files

import PyInstaller.config
PyInstaller.config.CONF['distpath'] = './standalone'

block_cipher = None

added_files = []
added_files += collect_data_files('pyphen')
added_files += [('./gibberify/data', 'data')]

extra_imports = ['pyphen']


a = Analysis(['gibberify/__main__.py'],
             pathex=['./gibberify'],
             binaries=[],
             datas=added_files,
             hiddenimports=extra_imports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='gibberify',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
