REM Startup Installer with 1-Second Popup
@echo off
title Install Wallpaper Changer to Startup (1-Second Popup)

echo.
echo Installing Wallpaper Changer to Windows Startup...
echo This version shows a 1-second popup when wallpaper changes...
echo.

REM Get the current directory where this script is located
set "SCRIPT_DIR=%~dp0"

REM Create startup batch file that runs wallpaper changer
set "STARTUP_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.bat"

REM Write the startup batch file with 1-second popup
(
echo @echo off
echo title Wallpaper Changed!
echo REM Wait for Windows to fully load
echo timeout /t 5 /nobreak ^>nul
echo.
echo REM Change to the wallpaper script directory
echo cd /d "%SCRIPT_DIR%"
echo.
echo REM Check if script exists and run
echo if exist "instant_wallpaper.py" ^(
echo     echo Changing wallpaper...
echo     python instant_wallpaper.py startup
echo     timeout /t 1 /nobreak ^>nul
echo ^)
) > "%STARTUP_FILE%"

echo ✓ Successfully installed to startup!
echo ✓ Wallpaper will change with a 1-second popup notification
echo.
echo The wallpaper changer will show a brief popup every time Windows starts.
echo.
pause
