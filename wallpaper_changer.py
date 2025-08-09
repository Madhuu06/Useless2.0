#!/usr/bin/env python3
"""
Random Wallpaper Changer - A fun startup script
Changes desktop wallpaper randomly from a custom folder on system boot.
Safe, reversible, and perfect for adding personality to your computer!
"""

import os
import random
import sys
import ctypes
import winreg
from pathlib import Path
import json
import logging
from datetime import datetime

# Setup logging
log_file = Path(__file__).parent / "wallpaper_log.txt"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

class WallpaperChanger:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.wallpapers_folder = self.script_dir / "wallpapers"
        self.config_file = self.script_dir / "config.json"
        self.supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        
        # Load or create configuration
        self.config = self.load_config()
        
    def load_config(self):
        """Load configuration from config.json or create default config"""
        default_config = {
            "wallpapers_folder": str(self.wallpapers_folder),
            "enabled": True,
            "last_wallpaper": None,
            "change_frequency": "boot",  # Could be extended to "daily", "hourly", etc.
            "log_changes": True
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                # Merge with defaults for any missing keys
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
            except Exception as e:
                logging.warning(f"Could not load config file: {e}. Using defaults.")
                return default_config
        else:
            # Create default config file
            self.save_config(default_config)
            return default_config
    
    def save_config(self, config=None):
        """Save configuration to config.json"""
        if config is None:
            config = self.config
        
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            logging.error(f"Could not save config file: {e}")
    
    def setup_wallpapers_folder(self):
        """Create wallpapers folder if it doesn't exist"""
        if not self.wallpapers_folder.exists():
            self.wallpapers_folder.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created wallpapers folder: {self.wallpapers_folder}")
            
            # Create a sample instruction file
            readme_content = """
# Welcome to your Wallpaper Collection! 🎨

Place your favorite images in this folder to use as wallpapers!

Supported formats: .jpg, .jpeg, .png, .bmp, .gif

Tips:
- Add memes for a fun daily surprise! 😄
- Include scenic photos for beautiful landscapes 🌄
- Create themed folders (but keep images in this main folder)
- Higher resolution images (1920x1080 or higher) work best

The script will randomly pick from all images in this folder every time your computer starts!

Enjoy your personalized desktop experience! ✨
"""
            readme_file = self.wallpapers_folder / "README.txt"
            with open(readme_file, 'w', encoding='utf-8') as f:
                f.write(readme_content)
    
    def get_wallpaper_files(self):
        """Get list of valid wallpaper files from the wallpapers folder"""
        if not self.wallpapers_folder.exists():
            return []
        
        wallpaper_files = []
        for file_path in self.wallpapers_folder.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in self.supported_formats:
                wallpaper_files.append(file_path)
        
        return wallpaper_files
    
    def set_wallpaper(self, image_path):
        """Set desktop wallpaper using Windows API with Fill mode"""
        try:
            # Convert to absolute path string
            abs_path = str(Path(image_path).resolve())
            
            # Use Windows API to set wallpaper
            SPI_SETDESKWALLPAPER = 20
            result = ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 
                0, 
                abs_path, 
                3  # SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
            )
            
            if result:
                # Set wallpaper style to "Fill" for best fit
                # This ensures the image fills the screen properly without stretching
                try:
                    import winreg
                    key_path = r"Control Panel\Desktop"
                    
                    # Open registry key
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                        # Set WallpaperStyle to "10" (Fill mode)
                        # Fill mode scales the image to fill the desktop while maintaining aspect ratio
                        winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "10")
                        # Set TileWallpaper to "0" (don't tile)
                        winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
                    
                    # Refresh desktop to apply the style changes
                    SPI_SETDESKWALLPAPER = 20
                    ctypes.windll.user32.SystemParametersInfoW(
                        SPI_SETDESKWALLPAPER, 
                        0, 
                        abs_path, 
                        3
                    )
                    
                except Exception as style_error:
                    # If registry update fails, wallpaper still gets set, just maybe not optimal fit
                    pass
                
                logging.info(f"Successfully set wallpaper: {image_path.name}")
                return True
            else:
                logging.error(f"Failed to set wallpaper: {image_path}")
                return False
                
        except Exception as e:
            logging.error(f"Error setting wallpaper: {e}")
            return False
    
    def change_wallpaper(self):
        """Main function to change wallpaper randomly"""
        if not self.config.get("enabled", True):
            logging.info("Wallpaper changer is disabled in config")
            return False
        
        # Setup wallpapers folder
        self.setup_wallpapers_folder()
        
        # Get available wallpapers
        wallpaper_files = self.get_wallpaper_files()
        
        if not wallpaper_files:
            logging.warning(f"No wallpaper files found in {self.wallpapers_folder}")
            logging.info("Please add some images (.jpg, .jpeg, .png, .bmp, .gif) to the wallpapers folder!")
            return False
        
        # Choose a random wallpaper (avoid repeating the last one if possible)
        last_wallpaper = self.config.get("last_wallpaper")
        available_choices = wallpaper_files.copy()
        
        # If we have more than one option and want to avoid repeating
        if len(available_choices) > 1 and last_wallpaper:
            available_choices = [w for w in wallpaper_files if str(w) != last_wallpaper]
        
        if not available_choices:
            available_choices = wallpaper_files
        
        chosen_wallpaper = random.choice(available_choices)
        
        # Set the wallpaper
        success = self.set_wallpaper(chosen_wallpaper)
        
        if success:
            # Update config with last wallpaper
            self.config["last_wallpaper"] = str(chosen_wallpaper)
            self.save_config()
            
            if self.config.get("log_changes", True):
                logging.info(f"Today's wallpaper: {chosen_wallpaper.name}")
            
            return True
        
        return False
    
    def disable(self):
        """Disable the wallpaper changer"""
        self.config["enabled"] = False
        self.save_config()
        logging.info("Wallpaper changer disabled")
    
    def enable(self):
        """Enable the wallpaper changer"""
        self.config["enabled"] = True
        self.save_config()
        logging.info("Wallpaper changer enabled")
    
    def status(self):
        """Show current status"""
        wallpaper_count = len(self.get_wallpaper_files())
        status = "enabled" if self.config.get("enabled", True) else "disabled"
        
        print(f"\nRandom Wallpaper Changer Status:")
        print(f"   Status: {status}")
        print(f"   Wallpapers available: {wallpaper_count}")
        print(f"   Wallpapers folder: {self.wallpapers_folder}")
        print(f"   Last wallpaper: {self.config.get('last_wallpaper', 'None')}")
        print(f"   Log file: {log_file}")

def main():
    """Main entry point"""
    changer = WallpaperChanger()
    
    # Handle command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "disable":
            changer.disable()
        elif command == "enable":
            changer.enable()
        elif command == "status":
            changer.status()
        elif command == "test":
            print("Testing wallpaper change...")
            success = changer.change_wallpaper()
            if success:
                print("Test successful!")
            else:
                print("Test failed. Check the log for details.")
        elif command == "help":
            print("""
Random Wallpaper Changer - Usage:

python wallpaper_changer.py          - Change wallpaper (default)
python wallpaper_changer.py test     - Test wallpaper change
python wallpaper_changer.py status   - Show current status
python wallpaper_changer.py enable   - Enable wallpaper changer
python wallpaper_changer.py disable  - Disable wallpaper changer
python wallpaper_changer.py help     - Show this help

Add your favorite images to the 'wallpapers' folder!
Supported formats: .jpg, .jpeg, .png, .bmp, .gif
            """)
        else:
            print(f"Unknown command: {command}")
            print("Use 'python wallpaper_changer.py help' for usage information")
    else:
        # Default action: change wallpaper
        changer.change_wallpaper()

if __name__ == "__main__":
    main()
