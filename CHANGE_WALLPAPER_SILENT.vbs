Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get current directory
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
batFile = scriptDir & "\CLICK_ME_TO_CHANGE_WALLPAPER.bat"

' Run the batch file in silent mode (no popup windows)
WshShell.Run chr(34) & batFile & chr(34) & " silent", 0, true
