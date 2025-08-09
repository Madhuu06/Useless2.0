REM Ultimate Stealth Installer - No popups guaranteed
@echo off

REM Create completely invisible installer using PowerShell
powershell -WindowStyle Hidden -ExecutionPolicy Bypass -Command "& {
    $scriptDir = '%~dp0'
    $vbsFile = $env:APPDATA + '\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.vbs'
    $hiddenBat = $scriptDir + 'WallpaperChanger_Hidden.bat'
    
    # Create VBS script
    @'
Set WshShell = CreateObject(""WScript.Shell"")
WshShell.Run chr(34) & ""' + $hiddenBat + '"" & chr(34), 0, false
'@ | Out-File -FilePath $vbsFile -Encoding ASCII
    
    # Create hidden batch file
    @'
@echo off
timeout /t 2 /nobreak >nul
cd /d ""' + $scriptDir + '""
if exist ""hidden_launcher.py"" (
    python hidden_launcher.py
) else if exist ""instant_wallpaper.py"" (
    python instant_wallpaper.py startup >nul 2>&1
)
'@ | Out-File -FilePath $hiddenBat -Encoding ASCII
}" >nul 2>&1

REM Exit completely silently
exit /b 0
