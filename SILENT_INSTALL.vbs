Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
batFile = scriptDir & "\ENABLE_STARTUP_SIMPLE.bat"
WshShell.Run chr(34) & batFile & chr(34), 0, true
