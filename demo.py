#!/usr/bin/env python3
"""
Demo script for Random Wallpaper Changer
Tests the installation and provides a quick demonstration
"""

import sys
import subprocess
from pathlib import Path
import time

def run_command(command, description):
    """Run a command and show the result"""
    print(f"\n🔧 {description}")
    print(f"   Command: {command}")
    print("   " + "="*50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"Error: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"Error running command: {e}")
        return False

def main():
    """Run the demo"""
    script_dir = Path(__file__).parent
    
    print("🎨 Random Wallpaper Changer - Demo Script")
    print("="*60)
    print("This demo will test the wallpaper changer functionality")
    
    # Check if Python is working
    print(f"\n✅ Python version: {sys.version}")
    print(f"✅ Script directory: {script_dir}")
    
    # Check if main files exist
    main_script = script_dir / "wallpaper_changer.py"
    setup_script = script_dir / "setup.py"
    wallpapers_folder = script_dir / "wallpapers"
    
    print(f"\n📁 File check:")
    print(f"   wallpaper_changer.py: {'✅ Found' if main_script.exists() else '❌ Missing'}")
    print(f"   setup.py: {'✅ Found' if setup_script.exists() else '❌ Missing'}")
    print(f"   wallpapers folder: {'✅ Found' if wallpapers_folder.exists() else '❌ Missing'}")
    
    if not main_script.exists() or not setup_script.exists():
        print("\n❌ Required files are missing. Please ensure all files are in the same folder.")
        return
    
    # Demo commands
    commands = [
        ("python setup.py status", "Checking setup status"),
        ("python wallpaper_changer.py status", "Checking wallpaper changer status"),
        ("python setup.py install", "Installing wallpaper changer"),
        ("python wallpaper_changer.py help", "Showing wallpaper changer help")
    ]
    
    for command, description in commands:
        success = run_command(command, description)
        if not success:
            print(f"⚠️  Command failed, but continuing demo...")
        time.sleep(1)  # Brief pause between commands
    
    # Check wallpapers
    if wallpapers_folder.exists():
        image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        images = [f for f in wallpapers_folder.iterdir() 
                 if f.is_file() and f.suffix.lower() in image_extensions]
        
        print(f"\n📸 Wallpaper images found: {len(images)}")
        if len(images) == 0:
            print("   💡 Add some images to the 'wallpapers' folder to get started!")
            print("   📖 Check 'wallpapers/README.md' for tips on where to find great images")
        else:
            print("   🎉 Great! You have images ready for wallpaper changing")
            
            # Offer to test wallpaper change
            test_choice = input("\n🧪 Test wallpaper change now? (y/n): ").lower().strip()
            if test_choice in ['y', 'yes']:
                run_command("python wallpaper_changer.py test", "Testing wallpaper change")
    
    print("\n🎯 Demo completed!")
    print("\nNext steps:")
    print("1. Add images to the 'wallpapers' folder (see wallpapers/README.md for tips)")
    print("2. Run 'python setup.py enable' to enable startup")
    print("3. Restart your computer to see it in action!")
    print("4. Use 'python setup.py disable' to stop anytime")
    
    print(f"\n📚 For more information, check README.md")
    print("🎉 Enjoy your personalized desktop experience!")

if __name__ == "__main__":
    main()
