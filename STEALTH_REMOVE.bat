@echo off
REM Stealth Uninstaller - Removes wallpaper changer without trace

REM Remove all stealth files
del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\SystemUpdate.vbs" 2>nul
del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.vbs" 2>nul
del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WallpaperChanger.bat" 2>nul
del "%~dp0WallpaperChanger_Stealth.bat" 2>nul
del "%~dp0WallpaperChanger_Hidden.bat" 2>nul
del "%~dp0startup_debug.log" 2>nul
del "%~dp0startup_wallpaper.log" 2>nul

REM Exit silently
exit /b 0
