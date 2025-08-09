#!/usr/bin/env python3
"""
Setup script for Random Wallpaper Changer
Helps users configure the script to run at startup
"""

import os
import sys
import winreg
from pathlib import Path
import subprocess

class StartupManager:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.main_script = self.script_dir / "wallpaper_changer.py"
        self.python_exe = sys.executable
        
        # Registry key for startup programs
        self.registry_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        self.app_name = "RandomWallpaperChanger"
        
    def is_startup_enabled(self):
        """Check if the script is set to run at startup"""
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_key) as key:
                try:
                    winreg.QueryValueEx(key, self.app_name)
                    return True
                except FileNotFoundError:
                    return False
        except Exception:
            return False
    
    def enable_startup(self):
        """Add the script to Windows startup"""
        try:
            # Command to run the script
            command = f'"{self.python_exe}" "{self.main_script}"'
            
            # Add to registry
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_key, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, self.app_name, 0, winreg.REG_SZ, command)
            
            print("Successfully enabled startup wallpaper changer!")
            print(f"   Command: {command}")
            print("   The script will now run every time you start your computer.")
            return True
            
        except Exception as e:
            print(f"❌ Error enabling startup: {e}")
            print("   Try running this script as administrator.")
            return False
    
    def disable_startup(self):
        """Remove the script from Windows startup"""
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_key, 0, winreg.KEY_SET_VALUE) as key:
                try:
                    winreg.DeleteValue(key, self.app_name)
                    print("✅ Successfully disabled startup wallpaper changer!")
                    print("   The script will no longer run at startup.")
                    return True
                except FileNotFoundError:
                    print("ℹ️  Wallpaper changer was not set to run at startup.")
                    return True
                    
        except Exception as e:
            print(f"❌ Error disabling startup: {e}")
            print("   Try running this script as administrator.")
            return False
    
    def create_batch_file(self):
        """Create a batch file for easier execution"""
        batch_content = f'''@echo off
cd /d "{self.script_dir}"
"{self.python_exe}" "{self.main_script}" %*
pause
'''
        
        batch_file = self.script_dir / "run_wallpaper_changer.bat"
        try:
            with open(batch_file, 'w') as f:
                f.write(batch_content)
            print(f"Created batch file: {batch_file}")
            return True
        except Exception as e:
            print(f"Error creating batch file: {e}")
            return False
    
    def setup_wallpapers_folder(self):
        """Create wallpapers folder and add sample info"""
        wallpapers_folder = self.script_dir / "wallpapers"
        wallpapers_folder.mkdir(exist_ok=True)
        
        # Create sample images info file
        sample_info = """
🎨 Sample Wallpapers to Get You Started!

You can download some sample wallpapers from these sources:

Free High-Quality Images:
• Unsplash.com - Beautiful photography
• Pexels.com - Free stock photos
• Pixabay.com - Various images and graphics

Meme Collections:
• Reddit: r/wallpapers, r/memes
• Know Your Meme - Popular meme templates
• Giphy.com - Animated GIFs (if you want moving wallpapers)

Nature & Landscapes:
• National Geographic wallpapers
• NASA's image gallery
• Desktop Nexus

Gaming & Pop Culture:
• Steam wallpapers
• Movie/TV show promotional images
• Fan art communities

Tips:
• Aim for 1920x1080 (Full HD) or higher resolution
• JPEG files are smaller, PNG files have better quality
• Keep your collection under 100 images for faster loading
• Organize by theme if you like!

Just download images you like and place them in this 'wallpapers' folder!
"""
        
        info_file = wallpapers_folder / "Where_to_find_wallpapers.txt"
        with open(info_file, 'w', encoding='utf-8') as f:
            f.write(sample_info)
    
    def show_status(self):
        """Show current setup status"""
        startup_enabled = self.is_startup_enabled()
        wallpapers_folder = self.script_dir / "wallpapers"
        wallpaper_count = 0
        
        if wallpapers_folder.exists():
            wallpaper_count = len([f for f in wallpapers_folder.iterdir() 
                                 if f.is_file() and f.suffix.lower() in ('.jpg', '.jpeg', '.png', '.bmp', '.gif')])
        
        print("\nRandom Wallpaper Changer Setup Status:")
        print(f"   Startup enabled: {'Yes' if startup_enabled else 'No'}")
        print(f"   Wallpapers folder: {'Exists' if wallpapers_folder.exists() else 'Missing'}")
        print(f"   Wallpapers available: {wallpaper_count}")
        print(f"   Script location: {self.main_script}")
        
        if wallpaper_count == 0:
            print("\nTo get started:")
            print("   1. Add some images to the 'wallpapers' folder")
            print("   2. Run 'python setup.py enable' to enable startup")
            print("   3. Restart your computer to see it in action!")

def main():
    """Main setup function"""
    manager = StartupManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "enable":
            manager.setup_wallpapers_folder()
            manager.create_batch_file()
            manager.enable_startup()
            
        elif command == "disable":
            manager.disable_startup()
            
        elif command == "status":
            manager.show_status()
            
        elif command == "install":
            print("Installing Random Wallpaper Changer...")
            manager.setup_wallpapers_folder()
            manager.create_batch_file()
            print("Installation complete!")
            print("\nNext steps:")
            print("1. Add some images to the 'wallpapers' folder")
            print("2. Run 'python setup.py enable' to enable startup")
            print("3. Test with 'python wallpaper_changer.py test'")
            
        elif command == "help":
            print("""
Random Wallpaper Changer Setup - Usage:

python setup.py install   - Install and set up the wallpaper changer
python setup.py enable    - Enable running at startup
python setup.py disable   - Disable running at startup  
python setup.py status    - Show current setup status
python setup.py help      - Show this help

Quick Start:
1. python setup.py install
2. Add your favorite images to the 'wallpapers' folder
3. python setup.py enable
4. Restart your computer and enjoy!

Note: You may need to run as administrator for startup functionality.
            """)
        else:
            print(f"Unknown command: {command}")
            print("Use 'python setup.py help' for usage information")
    else:
        # Default: show status and basic instructions
        manager.show_status()
        print("\nUse 'python setup.py help' for setup options")

if __name__ == "__main__":
    main()
