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

REM Write the startup batch file with better error handling and debugging
(
echo @echo off
echo title Wallpaper Changer Startup
echo REM Auto-generated startup file for Wallpaper Changer
echo REM Wait for Windows to fully load
echo timeout /t 8 /nobreak ^>nul
echo.
echo REM Log startup attempt
echo echo %date% %time% - Startup attempt >> "%SCRIPT_DIR%startup_debug.log"
echo.
echo REM Change to the wallpaper script directory
echo cd /d "%SCRIPT_DIR%"
echo echo Current directory: %cd% >> "%SCRIPT_DIR%startup_debug.log"
echo.
echo REM Check if Python is available
echo python --version >> "%SCRIPT_DIR%startup_debug.log" 2^>^&1
echo.
echo REM Check if script exists and run
echo if exist "instant_wallpaper.py" ^(
echo     echo Script found, running... >> "%SCRIPT_DIR%startup_debug.log"
echo     python instant_wallpaper.py startup >> "%SCRIPT_DIR%startup_debug.log" 2^>^&1
echo     echo Wallpaper change completed >> "%SCRIPT_DIR%startup_debug.log"
echo ^) else ^(
echo     echo ERROR: Script not found in: %cd% >> "%SCRIPT_DIR%startup_debug.log"
echo     echo Directory contents: >> "%SCRIPT_DIR%startup_debug.log"
echo     dir >> "%SCRIPT_DIR%startup_debug.log"
echo ^)
echo.
echo REM Add separator for next run
echo echo ========================================== >> "%SCRIPT_DIR%startup_debug.log"
) > "%STARTUP_FILE%"

echo ✓ Successfully installed to startup!
echo ✓ Wallpaper will change automatically on every restart
echo.
echo The wallpaper changer will now run every time Windows starts.
echo.
pause
