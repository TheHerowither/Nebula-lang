@echo off

set p=%~1

echo Seting path
echo.%PATH%|findstr "%p%" >nul 2>&1
if not errorlevel 1 (
   echo Found %p% in path, so no need to set to path
) else (
    set PATH="%CD%%p%;%PATH%"
)