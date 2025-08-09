REM Simple Startup Installer for Wallpaper Changer
@echo off
title Install Wallpaper Changer to Startup

echo.
echo Installing Wallpaper Changer to Windows Startup...
echo.

REM Create startup batch file
set "STARTUP_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.bat"
echo @echo off > "%STARTUP_FILE%"
echo cd /d "%~dp0" >> "%STARTUP_FILE%"
echo python instant_wallpaper.py startup >> "%STARTUP_FILE%"

echo ✓ Successfully installed to startup!
echo ✓ Wallpaper will change automatically on every restart
echo.
echo The wallpaper changer will now run every time Windows starts.
echo.
pause
