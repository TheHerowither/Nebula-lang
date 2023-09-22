@echo off

set p=%~1

echo Seting path
echo.%PATH%|findstr "%p%" >nul 2>&1
rem echo %errorlevel%
if errorlevel 1 (
   echo Found %p% in path, so no need to set to path
) else (
    setx PATH "%CD%%p%;%PATH%"
)