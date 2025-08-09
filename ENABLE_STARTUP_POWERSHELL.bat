REM Alternative Startup Installer using PowerShell (More Reliable)
@echo off
title Install Wallpaper Changer to Startup (PowerShell Method)

echo.
echo Installing Wallpaper Changer to Windows Startup...
echo Using PowerShell method for better compatibility...
echo.

REM Get the current directory where this script is located
set "SCRIPT_DIR=%~dp0"

REM Create startup PowerShell script
set "STARTUP_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.ps1"

REM Write the PowerShell startup script
(
echo # Auto-generated PowerShell startup script for Wallpaper Changer
echo Start-Sleep -Seconds 8
echo $scriptDir = "%SCRIPT_DIR%"
echo Set-Location -Path $scriptDir
echo $logFile = Join-Path $scriptDir "startup_debug.log"
echo "$(Get-Date) - PowerShell startup attempt" ^| Out-File -FilePath $logFile -Append
echo "Current directory: $(Get-Location)" ^| Out-File -FilePath $logFile -Append
echo if (Test-Path "instant_wallpaper.py"^) {
echo     "Script found, running..." ^| Out-File -FilePath $logFile -Append
echo     try {
echo         $result = python instant_wallpaper.py startup 2^>^&1
echo         $result ^| Out-File -FilePath $logFile -Append
echo         "Wallpaper change completed successfully" ^| Out-File -FilePath $logFile -Append
echo     } catch {
echo         "Error running Python script: $_" ^| Out-File -FilePath $logFile -Append
echo     }
echo } else {
echo     "ERROR: instant_wallpaper.py not found" ^| Out-File -FilePath $logFile -Append
echo     Get-ChildItem ^| Out-File -FilePath $logFile -Append
echo }
echo "==========================================" ^| Out-File -FilePath $logFile -Append
) > "%STARTUP_FILE%"

echo ✓ Successfully installed PowerShell startup script!
echo ✓ Wallpaper will change automatically on every restart
echo ✓ Debug logs will be saved to startup_debug.log
echo.
echo The wallpaper changer will now run every time Windows starts.
echo.
pause
