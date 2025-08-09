@echo off
title Test Startup Manually
echo Testing startup functionality...
echo.

REM Run the same command that startup would run
cd /d "%~dp0"
python instant_wallpaper.py startup

echo.
echo If you see "Successfully changed wallpaper" above, startup is working!
echo.
pause
