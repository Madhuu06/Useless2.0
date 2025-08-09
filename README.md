# 🎨 Random Wallpaper Changer

A fun and harmless Python-based startup script that changes your desktop wallpaper every time you boot your system! The wallpapers are chosen randomly from a custom folder filled with memes, scenic photos, or any themed images you love.

## ✨ Features

- 🎲 **Random Selection**: Different wallpaper every startup
- 🔒 **Safe & Reversible**: Easy to enable/disable anytime
- 📁 **Custom Collection**: Use your own images
- 📊 **Smart Logging**: Track wallpaper changes
- ⚙️ **Easy Setup**: Simple installation and configuration
- 🖼️ **Multiple Formats**: Supports JPG, PNG, BMP, GIF
- 🚫 **No Repeats**: Avoids showing the same wallpaper consecutively
- 🎯 **Perfect Fit**: Uses "Fill" mode for optimal image display without stretching

## 🚀 Quick Start

### Step 1: Install
```bash
python setup.py install
```

### Step 2: Add Your Images
1. Navigate to the newly created `wallpapers` folder
2. Add your favorite images (memes, photos, artwork, etc.)
3. Supported formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`

### Step 3: Enable Startup
```bash
python setup.py enable
```

### Step 4: Test It!
```bash
python wallpaper_changer.py test
```

### Step 5: Enjoy!
Restart your computer and enjoy a fresh wallpaper every boot! 🎉

## 📖 Usage Guide

### Setup Commands
```bash
python setup.py install    # Set up the wallpaper changer
python setup.py enable     # Enable running at startup
python setup.py disable    # Disable running at startup
python setup.py status     # Show current setup status
python setup.py help       # Show help for setup
```

### Wallpaper Commands
```bash
python wallpaper_changer.py          # Change wallpaper now
python wallpaper_changer.py test     # Test wallpaper change
python wallpaper_changer.py status   # Show wallpaper status
python wallpaper_changer.py enable   # Enable wallpaper changer
python wallpaper_changer.py disable  # Disable wallpaper changer
python wallpaper_changer.py help     # Show wallpaper help
```

### Batch File (Alternative)
After installation, you can also use:
```bash
run_wallpaper_changer.bat
```

## 📁 File Structure

```
Wallpaper Script/
├── wallpaper_changer.py       # Main script
├── setup.py                   # Setup and startup manager
├── run_wallpaper_changer.bat   # Windows batch file (auto-created)
├── config.json                # Configuration file (auto-created)
├── wallpaper_log.txt          # Log file (auto-created)
├── wallpapers/                 # Your image collection
│   ├── README.txt             # Instructions for adding images
│   └── [your images here]
└── README.md                  # This file
```

## ⚙️ Configuration

The script creates a `config.json` file with these options:

```json
{
    "wallpapers_folder": "path/to/wallpapers",
    "enabled": true,
    "last_wallpaper": "last_used_image.jpg",
    "change_frequency": "boot",
    "log_changes": true
}
```

You can manually edit this file to customize behavior.

## 🎯 Tips for Best Experience

### Image Recommendations
- **Resolution**: Use 1920x1080 (Full HD) or higher for best quality
- **Format**: JPEG files are smaller, PNG files have better quality
- **Quantity**: Keep your collection under 100 images for faster loading
- **Organization**: You can organize by theme, but keep all images in the main `wallpapers` folder

### Where to Find Great Wallpapers
- **Photography**: Unsplash.com, Pexels.com, Pixabay.com
- **Memes**: Reddit (r/wallpapers, r/memes), Know Your Meme
- **Nature**: National Geographic, NASA Image Gallery
- **Gaming**: Steam wallpapers, game promotional art
- **Art**: DeviantArt, ArtStation

### Performance Tips
- Keep image file sizes reasonable (under 10MB each)
- Use JPEG for photos, PNG for graphics with transparency
- Regularly clean out images you no longer want

## 🔧 Troubleshooting

### Common Issues

**"No wallpaper files found"**
- Make sure you have images in the `wallpapers` folder
- Check that images have supported extensions (.jpg, .png, etc.)

**"Failed to set wallpaper"**
- Ensure the image file isn't corrupted
- Try with a different image format
- Check that the file path doesn't contain special characters

**Startup not working**
- Run `python setup.py enable` as administrator
- Check Windows startup programs in Task Manager
- Verify Python is in your system PATH

**Script not running**
- Make sure Python is installed and accessible
- Check that all files are in the same folder
- Look at `wallpaper_log.txt` for error messages

### Getting Help
1. Check the log file: `wallpaper_log.txt`
2. Run `python wallpaper_changer.py status` to see current state
3. Test manually with `python wallpaper_changer.py test`

## 🛡️ Safety & Privacy

- **Safe**: Only changes desktop wallpaper, no system modifications
- **Reversible**: Easy to disable or completely remove
- **Local**: No internet access required, all data stays on your computer
- **Open Source**: Full source code available for review

## 🗑️ Uninstalling

To completely remove the wallpaper changer:

1. Disable startup: `python setup.py disable`
2. Delete the entire `Wallpaper Script` folder
3. (Optional) Manually remove from Windows startup in Task Manager

## 🎉 Enjoy Your Daily Surprise!

Every time you start your computer, you'll be greeted with a fresh, randomly selected wallpaper from your personal collection. Whether it's a funny meme to start your day with a smile, a beautiful landscape to inspire you, or artwork that matches your mood - you'll never know what you'll get!

Perfect for:
- 😄 Adding humor to your daily routine
- 🌟 Keeping your desktop fresh and interesting  
- 🎨 Showcasing your favorite images
- ✨ Adding personality to your computer experience

---

*Made with ❤️ for desktop personalization enthusiasts!*
