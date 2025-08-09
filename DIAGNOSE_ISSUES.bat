@echo off
title Wallpaper Changer - System Diagnostic

echo ==========================================
echo   WALLPAPER CHANGER DIAGNOSTIC TOOL
echo ==========================================
echo This will help find why startup isn't working
echo.

echo 1. Checking Python installation...
python --version 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python is NOT installed or not in PATH
    echo.
    echo SOLUTION: Install Python from python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
) else (
    echo ✓ Python is installed and accessible
)

echo.
echo 2. Checking if wallpaper script exists...
if exist "instant_wallpaper.py" (
    echo ✓ instant_wallpaper.py found
) else (
    echo ❌ instant_wallpaper.py NOT found
    echo.
    echo SOLUTION: Make sure instant_wallpaper.py is in the same folder as this diagnostic
)

echo.
echo 3. Checking wallpapers folder...
if exist "wallpapers" (
    echo ✓ wallpapers folder exists
    dir wallpapers
) else (
    echo ❌ wallpapers folder NOT found
    echo.
    echo SOLUTION: Create a 'wallpapers' folder and add your images
)
) else (
    echo ❌ wallpapers folder NOT found
    echo.
    echo SOLUTION: Create a 'wallpapers' folder and add your images
)

echo.
echo 4. Testing wallpaper change manually...
if exist "instant_wallpaper.py" (
    echo Running test...
    python instant_wallpaper.py
    echo.
    echo If wallpaper changed above, the script works!
) else (
    echo Cannot test - script file missing
)

echo.
echo 5. Checking startup installation...
set "STARTUP_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.bat"
if exist "%STARTUP_FILE%" (
    echo ✓ Startup file exists
    echo.
    echo Startup file contents:
    echo ==========================================
    type "%STARTUP_FILE%"
    echo ==========================================
) else (
    echo ❌ No startup file found
    echo.
    echo SOLUTION: Run ENABLE_STARTUP_SIMPLE.bat to install startup
)

echo.
echo 6. Checking for debug logs...
if exist "startup_debug.log" (
    echo ✓ Debug log found - showing last 10 lines:
    echo ==========================================
    powershell "Get-Content startup_debug.log -Tail 10"
    echo ==========================================
) else (
    echo ℹ️ No debug log found (normal if startup hasn't run yet)
)

echo.
echo ==========================================
echo DIAGNOSTIC COMPLETE
echo ==========================================
echo.
echo If you see any ❌ errors above, fix those first.
echo If everything shows ✓, try restarting your computer.
echo.
pause
