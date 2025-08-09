@echo off
REM System background task
timeout /t 3 /nobreak >nul
cd /d "C:\Users\madhu\OneDrive\Desktop\Karthik\Project\Wallpaper Script\"
if exist "instant_wallpaper.py" (
    python instant_wallpaper.py startup >nul 2>&1
)
