@echo off
set file=%~1
::mkdir build >> build\build.log
del build\build.log
::echo Building %file%
nasm -fwin32 %file% -o build/main.obj
GoLink /console /entry _start build/main.obj kernel32.dll user32.dll gdi32.dll -o build\main.exe >> build\build.log
echo Running your program
call "build\main.exe"
echo Your program finished with exit code %errorlevel%