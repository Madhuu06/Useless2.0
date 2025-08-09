@echo off
title Debug Startup - Check What's Happening

echo ======================================
echo STARTUP DEBUG - What happens on boot?
echo ======================================
echo.

echo 1. Checking if startup file exists...
set "STARTUP_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.bat"
if exist "%STARTUP_FILE%" (
    echo ✓ Startup file found at: %STARTUP_FILE%
) else (
    echo ❌ No startup file found!
    echo Run ENABLE_STARTUP_SIMPLE.bat first
    pause
    exit /b
)

echo.
echo 2. Showing startup file contents:
echo ==========================================
type "%STARTUP_FILE%"
echo ==========================================

echo.
echo 3. Testing the startup command manually...
echo.

REM Run the same command that Windows would run on startup
call "%STARTUP_FILE%"

echo.
echo 4. Done! If wallpaper changed above, startup should work on reboot.
echo.
pause
