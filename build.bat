@echo off
del build.log
pyinstaller --onefile main.py --log-level="FATAL" --name="nebula" --add-data="..\lib;lib" --icon="NONE" --distpath="." --workpath="nebula-build" --specpath="nebula-build"