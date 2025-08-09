import subprocess
import sys
import os
from pathlib import Path

def run_hidden():
    """Run the wallpaper changer completely hidden"""
    script_dir = Path(__file__).parent
    wallpaper_script = script_dir / "instant_wallpaper.py"
    
    if wallpaper_script.exists():
        # Run Python script completely hidden
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        
        subprocess.run([
            sys.executable, 
            str(wallpaper_script), 
            "startup"
        ], 
        startupinfo=startupinfo,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW
        )

if __name__ == "__main__":
    run_hidden()
