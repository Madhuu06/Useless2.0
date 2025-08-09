Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get current directory
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Create startup VBS file
startupVBS = CreateObject("WScript.Shell").SpecialFolders("Startup") & "\WallpaperChanger.vbs"
hiddenBat = scriptDir & "\WallpaperChanger_Hidden.bat"

' VBS content for startup
vbsContent = "Set WshShell = CreateObject(""WScript.Shell"")" & vbCrLf & _
             "WshShell.Run chr(34) & """ & hiddenBat & """ & chr(34), 0, false"

' Hidden batch file content  
batContent = "@echo off" & vbCrLf & _
             "timeout /t 2 /nobreak >nul" & vbCrLf & _
             "cd /d """ & scriptDir & """" & vbCrLf & _
             "if exist ""hidden_launcher.py"" (" & vbCrLf & _
             "    python hidden_launcher.py" & vbCrLf & _
             ") else if exist ""instant_wallpaper.py"" (" & vbCrLf & _
             "    python instant_wallpaper.py startup >nul 2>&1" & vbCrLf & _
             ")"

' Write startup VBS file
Set file1 = fso.CreateTextFile(startupVBS, True)
file1.Write vbsContent
file1.Close

' Write hidden batch file
Set file2 = fso.CreateTextFile(hiddenBat, True)
file2.Write batContent
file2.Close

' Done - exit silently
