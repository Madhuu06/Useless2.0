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
set "VBS_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.vbs"

REM Create VBS script to run batch file invisibly
(
echo Set WshShell = CreateObject("WScript.Shell"^)
echo WshShell.Run chr(34^) ^& "%SCRIPT_DIR%WallpaperChanger_Hidden.bat" ^& chr(34^), 0, false
) > "%VBS_FILE%"

REM Create the actual batch file to run hidden
set "HIDDEN_BAT=%SCRIPT_DIR%WallpaperChanger_Hidden.bat"
(
echo @echo off
echo REM Hidden wallpaper changer - no popup window
echo timeout /t 2 /nobreak ^>nul
echo cd /d "%SCRIPT_DIR%"
echo if exist "instant_wallpaper.py" ^(
echo     python instant_wallpaper.py startup ^>nul 2^>^&1
echo ^)
) > "%HIDDEN_BAT%"

echo ✓ Successfully installed to startup!
echo ✓ Wallpaper will change automatically on every restart (NO POPUP!)
echo ✓ Uses invisible VBS script to prevent command prompt window
echo.
echo The wallpaper changer will now run silently every time Windows starts.
echo.
pause
