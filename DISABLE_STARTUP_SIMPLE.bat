REM Simple Startup Remover for Wallpaper Changer
@echo off
title Remove Wallpaper Changer from Startup

echo.
echo Removing Wallpaper Changer from Windows Startup...
echo.

REM Remove startup batch file
set "STARTUP_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.bat"
if exist "%STARTUP_FILE%" (
    del "%STARTUP_FILE%"
    echo ✓ Successfully removed from startup!
) else (
    echo ! Wallpaper changer was not found in startup
)

echo.
echo The wallpaper changer will no longer run on Windows startup.
echo.
pause
