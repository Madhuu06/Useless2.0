@echo off
title Random Wallpaper Changer - Instant!

REM Change to script directory
cd /d "%~dp0"

REM Check if we should install to startup
if "%1"=="startup" goto :run_wallpaper_change

REM First time setup - offer to install to startup
echo.
echo ==========================================
echo   RANDOM WALLPAPER CHANGER - FIRST RUN
echo ==========================================
echo.
echo This will:
echo 1. Change your wallpaper now
echo 2. Ask if you want automatic daily changes
echo.

REM Run the instant wallpaper changer first
python instant_wallpaper.py

REM Ask about startup installation
echo.
echo ==========================================
echo   AUTOMATIC DAILY WALLPAPER CHANGES?
echo ==========================================
echo.
echo Would you like wallpaper to change automatically
echo every time you start your computer?
echo.
choice /c YN /m "Enable automatic startup wallpaper changes? (Y/N)"

if errorlevel 2 goto :skip_startup
if errorlevel 1 goto :install_startup

:install_startup
echo.
echo Installing to Windows startup...

REM Get startup folder path
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

REM Create a startup batch file that calls this script
echo @echo off > "%STARTUP_FOLDER%\WallpaperChanger.bat"
echo cd /d "%~dp0" >> "%STARTUP_FOLDER%\WallpaperChanger.bat"
echo "%~f0" startup >> "%STARTUP_FOLDER%\WallpaperChanger.bat"

echo ✓ Successfully installed to startup!
echo ✓ Wallpaper will change automatically on every restart
echo.
echo You can still double-click this file anytime for instant changes!
goto :end

:skip_startup
echo.
echo ✓ Startup installation skipped
echo ✓ You can double-click this file anytime for instant changes!
goto :end

:run_wallpaper_change
REM This runs on startup - just change wallpaper silently
python instant_wallpaper.py
goto :end

:end
echo.
pause
