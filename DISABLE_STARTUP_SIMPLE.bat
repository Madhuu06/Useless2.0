REM Simple Startup Remover for Wallpaper Changer
@echo off
title Remove Wallpaper Changer from Startup

echo.
echo Removing Wallpaper Changer from Windows Startup...
echo.

REM Remove both VBS and BAT startup files
set "STARTUP_VBS=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.vbs"
set "STARTUP_BAT=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.bat"
set "HIDDEN_BAT=%~dp0WallpaperChanger_Hidden.bat"

if exist "%STARTUP_VBS%" (
    del "%STARTUP_VBS%"
    echo ✓ Removed VBS startup file
)

if exist "%STARTUP_BAT%" (
    del "%STARTUP_BAT%"
    echo ✓ Removed BAT startup file
)

if exist "%HIDDEN_BAT%" (
    del "%HIDDEN_BAT%"
    echo ✓ Removed hidden batch file
)

echo ✓ Successfully removed from startup!

echo.
echo The wallpaper changer will no longer run on Windows startup.
echo.
pause
