@echo off
REM Hidden wallpaper changer - no popup window
timeout /t 5 /nobreak >nul
cd /d "C:\Users\madhu\OneDrive\Desktop\Karthik\Project\Wallpaper Script\"
if exist "instant_wallpaper.py" (
    python instant_wallpaper.py startup >nul 2>&1
)
