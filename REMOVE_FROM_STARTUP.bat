@echo off
title Remove Wallpaper Changer from Startup

echo.
echo ========================================
echo   REMOVE AUTOMATIC WALLPAPER CHANGER
echo ========================================
echo.

REM Get startup folder path
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "STARTUP_FILE=%STARTUP_FOLDER%\WallpaperChanger.bat"

REM Check if startup file exists
if not exist "%STARTUP_FILE%" (
    echo ✓ Wallpaper changer is not installed in startup
    echo   Nothing to remove!
    goto :end
)

echo Found wallpaper changer in startup folder
echo.
echo This will STOP automatic wallpaper changes on startup.
echo You can still use the manual wallpaper changer anytime.
echo.
choice /c YN /m "Remove from startup? (Y/N)"

if errorlevel 2 goto :cancel
if errorlevel 1 goto :remove

:remove
del "%STARTUP_FILE%" 2>nul
if exist "%STARTUP_FILE%" (
    echo ✗ Failed to remove startup file
    echo   You may need to delete it manually from:
    echo   %STARTUP_FOLDER%
) else (
    echo ✓ Successfully removed from startup!
    echo ✓ Automatic wallpaper changes disabled
    echo.
    echo You can still double-click the main .bat file for manual changes
)
goto :end

:cancel
echo ✓ Removal cancelled - startup wallpaper changer still active
goto :end

:end
echo.
pause
