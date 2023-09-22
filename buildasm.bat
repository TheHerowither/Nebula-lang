@echo off
set file=%~1
set name=%~2
::mkdir build >> build\build.log
del build\build.log
::echo Building %file%
mkdir build\%name% >> build\build.log
nasm -fwin32 %file% -o build/%name%/%name%.obj
GoLink /console /entry _start build/%name%/%name%.obj kernel32.dll user32.dll gdi32.dll -o build\main.exe >> build\build.log
echo Running your program
call "build\%name%\%name%.exe"
echo Your program finished with exit code %errorlevel%