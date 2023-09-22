@echo off
del build.log
pyinstaller --onefile main.py --log-level="FATAL" --name="nebula" --add-data="..\lib;lib" --icon="NONE" --distpath="." --workpath="nebula-build" --specpath="nebula-build"
pyinstaller --onefile installer.py --log-level="FATAL" --name="nebula_installer" --add-data="..\lib\info.py;lib.info" --icon="NONE" --distpath="." --workpath="nebula-build" --specpath="nebula-build"