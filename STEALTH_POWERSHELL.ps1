# PowerShell Stealth Installer - Run this with: powershell -ExecutionPolicy Bypass .\STEALTH_POWERSHELL.ps1

# Get current directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Create VBS file for startup
$vbsFile = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.vbs"
$hiddenBat = "$scriptDir\WallpaperChanger_Hidden.bat"

# Create VBS script content
$vbsContent = @"
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "$hiddenBat" & chr(34), 0, false
"@

# Create hidden batch file content
$batContent = @"
@echo off
timeout /t 2 /nobreak >nul
cd /d "$scriptDir"
if exist "hidden_launcher.py" (
    python hidden_launcher.py
) else if exist "instant_wallpaper.py" (
    python instant_wallpaper.py startup >nul 2>&1
)
"@

# Write files silently
$vbsContent | Out-File -FilePath $vbsFile -Encoding ASCII -Force
$batContent | Out-File -FilePath $hiddenBat -Encoding ASCII -Force

# Exit silently
exit 0
