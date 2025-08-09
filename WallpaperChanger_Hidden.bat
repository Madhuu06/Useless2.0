@echo off
timeout /t 2 /nobreak >nul
cd /d "C:\Users\madhu\OneDrive\Desktop\Karthik\Project\Wallpaper Script"
if exist "hidden_launcher.py" (
    python hidden_launcher.py
) else if exist "instant_wallpaper.py" (
    python instant_wallpaper.py startup >nul 2>&1
)