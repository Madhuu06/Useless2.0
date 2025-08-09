@echo off
echo.
echo ========================================
echo   RANDOM WALLPAPER CHANGER - INSTANT!
echo ========================================
echo.

REM Get the directory where this batch file is located
set "SCRIPT_DIR=%~dp0"

REM Create wallpapers folder if it doesn't exist
if not exist "%SCRIPT_DIR%wallpapers" (
    echo Creating wallpapers folder...
    mkdir "%SCRIPT_DIR%wallpapers"
    echo.
)

REM Check if there are any images in wallpapers folder
set "IMAGE_COUNT=0"
for %%f in ("%SCRIPT_DIR%wallpapers\*.jpg" "%SCRIPT_DIR%wallpapers\*.jpeg" "%SCRIPT_DIR%wallpapers\*.png" "%SCRIPT_DIR%wallpapers\*.bmp" "%SCRIPT_DIR%wallpapers\*.gif") do (
    if exist "%%f" set /a IMAGE_COUNT+=1
)

if %IMAGE_COUNT%==0 (
    echo No wallpaper images found!
    echo.
    echo QUICK SETUP:
    echo 1. Add some images to the 'wallpapers' folder
    echo 2. Double-click this file again
    echo.
    echo Supported formats: .jpg, .jpeg, .png, .bmp, .gif
    echo.
    echo Opening wallpapers folder for you...
    start "" "%SCRIPT_DIR%wallpapers"
    echo.
    pause
    exit /b
)

echo Found %IMAGE_COUNT% wallpaper images!
echo Changing wallpaper...
echo.

REM Run the Python script
python "%SCRIPT_DIR%wallpaper_changer.py"

echo.
echo ========================================
echo Want automatic wallpaper changes on startup?
echo Run: python setup.py enable
echo ========================================
echo.
pause
