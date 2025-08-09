#!/usr/bin/env python3
"""
INSTANT Wallpaper Changer - No setup required!
Just add your wallpaper image to wallpapers folder and run this script!
"""

import os
import sys
import ctypes
import winreg
from pathlib import Path
import json
import logging
from datetime import datetime

# Setup
script_dir = Path(__file__).parent
wallpapers_folder = script_dir / "wallpapers"
supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

def create_wallpapers_folder():
    """Create wallpapers folder if it doesn't exist"""
    if not wallpapers_folder.exists():
        wallpapers_folder.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created wallpapers folder: {wallpapers_folder}")
        
        # Create quick guide
        guide_content = """ADD YOUR IMAGES HERE!

Supported formats: .jpg, .jpeg, .png, .bmp, .gif

Where to find great wallpapers:
- Unsplash.com (nature photos)
- Reddit r/wallpapers (variety)
- Your phone's camera roll
- Meme websites for fun images

Just drag and drop images into this folder!
"""
        guide_file = wallpapers_folder / "PUT_IMAGES_HERE.txt"
        with open(guide_file, 'w', encoding='utf-8') as f:
            f.write(guide_content)
        return True
    return False

def get_wallpaper_files():
    """Get list of valid wallpaper files"""
    if not wallpapers_folder.exists():
        return []
    
    wallpaper_files = []
    for file_path in wallpapers_folder.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in supported_formats:
            wallpaper_files.append(file_path)
    
    return wallpaper_files

def set_wallpaper(image_path):
    """Set desktop wallpaper using Windows API with Fill mode - PERSISTENT ACROSS REBOOTS"""
    try:
        abs_path = str(Path(image_path).resolve())
        
        # FIRST: Update registry to ensure persistence across reboots
        try:
            import winreg
            key_path = r"Control Panel\Desktop"
            
            # Open registry key
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                # Set the wallpaper path in registry - THIS IS CRUCIAL FOR PERSISTENCE
                winreg.SetValueEx(key, "Wallpaper", 0, winreg.REG_SZ, abs_path)
                # Set WallpaperStyle to "10" (Fill mode)
                winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "10")
                # Set TileWallpaper to "0" (don't tile)
                winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
            
        except Exception as registry_error:
            print(f"⚠ Registry update failed: {registry_error}")
            return False
        
        # SECOND: Use Windows API to set wallpaper immediately
        SPI_SETDESKWALLPAPER = 20
        result = ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 
            0, 
            abs_path, 
            3  # SPIF_UPDATEINIFILE | SPIF_SENDCHANGE - Forces registry update
        )
        
        if result:
            # THIRD: Double-check with another API call to ensure it sticks
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 
                0, 
                abs_path, 
                3
            )
            
            print(f"✓ Successfully changed wallpaper to: {image_path.name}")
            return True
        else:
            print(f"✗ Failed to set wallpaper: {image_path}")
            return False
            
    except Exception as e:
        print(f"✗ Error setting wallpaper: {e}")
        return False

def main():
    """Main function - instant wallpaper changer"""
    # Check if running from startup (no user interaction)
    startup_mode = len(sys.argv) > 1 and sys.argv[1] == "startup"
    
    if not startup_mode:
        print("=" * 50)
        print("  INSTANT WALLPAPER CHANGER")
        print("=" * 50)
        print()
    
    # Create wallpapers folder if needed
    folder_created = create_wallpapers_folder()
    
    # Get available wallpapers
    wallpaper_files = get_wallpaper_files()
    
    if not wallpaper_files:
        if startup_mode:
            # Silent fail for startup mode
            return
            
        print(" No wallpaper images found!")
        print()
        print("QUICK SETUP:")
        print("1. Add your wallpaper image to the 'wallpapers' folder")
        print("2. Run this script again")
        print()
        print("Supported formats: .jpg, .jpeg, .png, .bmp, .gif")
        print()
        
        if folder_created:
            print("📁 Opening wallpapers folder for you...")
            try:
                if os.name == 'nt':  # Windows
                    os.startfile(wallpapers_folder)
                elif os.name == 'posix':  # Mac/Linux
                    os.system(f'open "{wallpapers_folder}"')
            except:
                print(f"📁 Wallpapers folder location: {wallpapers_folder}")
        
        input("\nPress Enter to close...")
        return
    
    # Use the first wallpaper found (no randomization needed for single wallpaper)
    chosen_wallpaper = wallpaper_files[0]
    
    if not startup_mode:
        print(f"📷 Using wallpaper: {chosen_wallpaper.name}")
    
    # Set the wallpaper
    success = set_wallpaper(chosen_wallpaper)
    
    if not startup_mode:
        if success:
            print()
            print("🎉 Wallpaper changed successfully!")
            print()
            print("💡 Want automatic changes on startup?")
            print("   Run: python setup.py enable")
        else:
            print()
            print("❌ Failed to change wallpaper")
            print("   Try with a different image format")
        
        print()
        input("Press Enter to close...")
    else:
        # Startup mode - log to file instead
        log_file = script_dir / "startup_wallpaper.log"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "SUCCESS" if success else "FAILED"
        
        try:
            with open(log_file, "a", encoding='utf-8') as f:
                f.write(f"{timestamp} - {status}: {chosen_wallpaper.name if success else 'Wallpaper change failed'}\n")
        except:
            pass  # Silent fail for logging

if __name__ == "__main__":
    main()
