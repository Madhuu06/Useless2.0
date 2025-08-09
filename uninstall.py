#!/usr/bin/env python3
"""
Uninstaller for Random Wallpaper Changer
Safely removes the wallpaper changer from startup and cleans up files
"""

import os
import sys
import winreg
from pathlib import Path
import shutil

class Uninstaller:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.registry_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        self.app_name = "RandomWallpaperChanger"
    
    def remove_from_startup(self):
        """Remove the script from Windows startup (both methods)"""
        removed_count = 0
        
        # Method 1: Remove from Windows Registry
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_key, 0, winreg.KEY_SET_VALUE) as key:
                try:
                    winreg.DeleteValue(key, self.app_name)
                    print("✅ Removed from Windows startup registry")
                    removed_count += 1
                except FileNotFoundError:
                    print("ℹ️  Not found in startup registry")
                    
        except Exception as e:
            print(f"❌ Error removing from startup registry: {e}")
        
        # Method 2: Remove from Startup Folder (new batch file method)
        try:
            import os
            startup_folder = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
            startup_file = os.path.join(startup_folder, "WallpaperChanger.bat")
            
            if os.path.exists(startup_file):
                os.remove(startup_file)
                print("✅ Removed from Windows startup folder")
                removed_count += 1
            else:
                print("ℹ️  Not found in startup folder")
                
        except Exception as e:
            print(f"❌ Error removing from startup folder: {e}")
            print("   You may need to manually delete: %APPDATA%\\...\\Startup\\WallpaperChanger.bat")
        
        if removed_count == 0:
            print("ℹ️  Wallpaper changer was not installed for automatic startup")
        
        return removed_count > 0
    
    def list_files_to_remove(self):
        """List files that will be removed"""
        files_to_remove = [
            "wallpaper_changer.py",
            "setup.py", 
            "uninstall.py",
            "README.md",
            "requirements.txt",
            "wallpaper_log.txt",
            "startup_wallpaper.log",
            "run_wallpaper_changer.bat",
            "instant_wallpaper.py",
            "CLICK_ME_TO_CHANGE_WALLPAPER.bat",
            "INSTANT_WALLPAPER_CHANGER.bat",
            "REMOVE_FROM_STARTUP.bat",
            "SETUP_FOR_FRIENDS.txt",
            "demo.py"
        ]
        
        existing_files = []
        for file_name in files_to_remove:
            file_path = self.script_dir / file_name
            if file_path.exists():
                existing_files.append(file_path)
        
        return existing_files
    
    def backup_wallpapers(self):
        """Ask user if they want to backup their wallpapers folder"""
        wallpapers_folder = self.script_dir / "wallpapers"
        
        if not wallpapers_folder.exists():
            return True
        
        # Count actual image files (not just any files)
        image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        image_files = [f for f in wallpapers_folder.iterdir() 
                      if f.is_file() and f.suffix.lower() in image_extensions]
        
        if not image_files:
            print("ℹ️  No wallpaper images found to backup")
            return True
        
        print(f"\n📁 Found {len(image_files)} wallpaper images in your collection")
        print("   These are your personal images that you added.")
        
        while True:
            choice = input("\n🤔 Do you want to keep your wallpapers folder? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                print("✅ Wallpapers folder will be preserved")
                return False  # Don't remove wallpapers
            elif choice in ['n', 'no']:
                print("🗑️  Wallpapers folder will be removed")
                return True   # Remove wallpapers
            else:
                print("Please enter 'y' for yes or 'n' for no")
    
    def uninstall(self, remove_wallpapers=None):
        """Perform the uninstallation"""
        print("🗑️  Random Wallpaper Changer Uninstaller")
        print("=" * 50)
        
        # Remove from startup
        print("\n1. Removing from Windows startup...")
        self.remove_from_startup()
        
        # Handle wallpapers folder
        wallpapers_folder = self.script_dir / "wallpapers"
        if remove_wallpapers is None:
            remove_wallpapers = self.backup_wallpapers()
        
        # List files to remove
        files_to_remove = self.list_files_to_remove()
        
        print(f"\n2. Files to be removed:")
        for file_path in files_to_remove:
            print(f"   - {file_path.name}")
        
        if wallpapers_folder.exists() and remove_wallpapers:
            print(f"   - wallpapers/ (folder with your images)")
        
        # Confirm removal
        if len(sys.argv) <= 1 or sys.argv[1].lower() != "force":
            while True:
                choice = input(f"\n⚠️  Remove these files? (y/n): ").lower().strip()
                if choice in ['y', 'yes']:
                    break
                elif choice in ['n', 'no']:
                    print("❌ Uninstallation cancelled")
                    return False
                else:
                    print("Please enter 'y' for yes or 'n' for no")
        
        # Remove files
        print("\n3. Removing files...")
        removed_count = 0
        
        for file_path in files_to_remove:
            try:
                if file_path.exists():
                    file_path.unlink()
                    print(f"   ✅ Removed {file_path.name}")
                    removed_count += 1
            except Exception as e:
                print(f"   ❌ Could not remove {file_path.name}: {e}")
        
        # Remove wallpapers folder if requested
        if wallpapers_folder.exists() and remove_wallpapers:
            try:
                shutil.rmtree(wallpapers_folder)
                print(f"   ✅ Removed wallpapers folder")
                removed_count += 1
            except Exception as e:
                print(f"   ❌ Could not remove wallpapers folder: {e}")
        
        print(f"\n✅ Uninstallation complete! Removed {removed_count} items.")
        
        if wallpapers_folder.exists() and not remove_wallpapers:
            print(f"📁 Your wallpapers are preserved in: {wallpapers_folder}")
        
        print("\n🎉 The Random Wallpaper Changer has been removed from your system.")
        print("   Your desktop wallpaper will no longer change automatically.")
        print("   Thanks for using the Random Wallpaper Changer! 👋")
        
        return True

def main():
    """Main uninstaller function"""
    uninstaller = Uninstaller()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "force":
            # Force uninstall without prompts (remove wallpapers)
            uninstaller.uninstall(remove_wallpapers=True)
        elif command == "keep":
            # Uninstall but keep wallpapers
            uninstaller.uninstall(remove_wallpapers=False)
        elif command == "help":
            print("""
🗑️  Random Wallpaper Changer Uninstaller - Usage:

python uninstall.py        - Interactive uninstallation (asks about wallpapers)
python uninstall.py keep   - Uninstall but keep wallpapers folder
python uninstall.py force  - Force uninstall everything (including wallpapers)
python uninstall.py help   - Show this help

What gets removed:
- Windows startup entries (both registry and startup folder)
- All script files (wallpaper_changer.py, setup.py, batch files, etc.)
- Configuration and log files
- Optionally: your wallpapers folder (asks first)

This removes EVERYTHING including:
- Automatic startup wallpaper changes
- Manual wallpaper changer
- All configuration files
- Startup folder entries created by CLICK_ME_TO_CHANGE_WALLPAPER.bat

The uninstaller will ask before removing your personal wallpaper collection.
            """)
        else:
            print(f"Unknown command: {command}")
            print("Use 'python uninstall.py help' for usage information")
    else:
        # Interactive uninstall
        uninstaller.uninstall()

if __name__ == "__main__":
    main()
