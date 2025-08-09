REM Simple Startup Installer for Wallpaper Changer
@echo off
title Install Wallpaper Changer to Startup

echo.
echo Installing Wallpaper Changer to Windows Startup...
echo.

REM Get the current directory where this script is located
set "SCRIPT_DIR=%~dp0"

REM Create startup batch file that runs wallpaper changer
set "STARTUP_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.bat"

REM Write the startup batch file with better error handling
(
echo @echo off
echo REM Auto-generated startup file for Wallpaper Changer
echo REM Wait a few seconds for Windows to fully load
echo timeout /t 10 /nobreak ^>nul
echo.
echo REM Change to the wallpaper script directory
echo cd /d "%SCRIPT_DIR%"
echo.
echo REM Check if Python and script exist, then run
echo if exist "instant_wallpaper.py" ^(
echo     echo Running wallpaper changer...
echo     python instant_wallpaper.py startup
echo ^) else ^(
echo     echo ERROR: Wallpaper script not found in: %SCRIPT_DIR%
echo     echo Current directory contents:
echo     dir
echo     pause
echo ^)
) > "%STARTUP_FILE%"

echo ✓ Successfully installed to startup!
echo ✓ Wallpaper will change automatically on every restart
echo.
echo The wallpaper changer will now run every time Windows starts.
echo.
pause
