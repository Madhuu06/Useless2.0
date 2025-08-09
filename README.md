# 🖼️ Stealth Wallpaper Changer

A fun, harmless wallpaper changer that can run silently for pranks or personal use. Changes desktop wallpaper automatically on startup or manually with zero popups.

## 🚀 Quick Start

### **For Instant Wallpaper Change:**
1. Put your wallpaper image in the `wallpapers` folder
2. Double-click `CLICK_ME_TO_CHANGE_WALLPAPER.bat`
3. Choose option 2 for silent mode (no popups)

### **For Stealth Pranks (Friends' Computers):**
1. Copy this entire folder to their computer
2. Add your prank wallpaper to the `wallpapers` folder  
3. Double-click `CLICK_TO_INSTALL_STEALTH.vbs` (completely invisible)
4. Walk away - wallpaper will change on their next restart!

## 📁 Files Included

| File | Purpose |
|------|---------|
| `CLICK_ME_TO_CHANGE_WALLPAPER.bat` | Main interface - change wallpaper now |
| `CHANGE_WALLPAPER_SILENT.vbs` | Instant silent wallpaper change |
| `CLICK_TO_INSTALL_STEALTH.vbs` | Install automatic startup (invisible) |
| `STEALTH_REMOVE.bat` | Remove from startup completely |
| `instant_wallpaper.py` | Core wallpaper changing script |
| `hidden_launcher.py` | Silent execution wrapper |
| `wallpapers/` | Put your wallpaper images here |

## 🎯 Usage Options

### **Option 1: Manual Change**
```
Double-click: CLICK_ME_TO_CHANGE_WALLPAPER.bat
```
- Shows menu with normal/silent options
- Choose 2 for silent mode (no popups)

### **Option 2: Direct Silent Change**
```
Double-click: CHANGE_WALLPAPER_SILENT.vbs
```
- Changes wallpaper immediately
- Zero popup windows
- Perfect for stealth use

### **Option 3: Install Automatic Startup**
```
Double-click: CLICK_TO_INSTALL_STEALTH.vbs
```
- Installs completely invisibly
- Wallpaper changes on every restart
- No popups during installation or execution

## 🕵️ Stealth Features

- ✅ **Zero Popups** - All operations can run silently
- ✅ **Hidden Installation** - Friend never sees any windows
- ✅ **Automatic Startup** - Changes wallpaper on restart
- ✅ **Clean Removal** - Easy cleanup with stealth remove
- ✅ **No Console Windows** - Uses VBS wrappers for invisibility

## 🛠️ How It Works

1. **VBS Scripts** run batch files with window mode = 0 (invisible)
2. **Hidden Launcher** uses Python subprocess with no console window
3. **Fill Mode** ensures wallpaper scales properly without stretching
4. **2-Second Delay** gives Windows time to load before changing wallpaper

## 🗑️ Removal

To remove from startup completely:
```
Double-click: STEALTH_REMOVE.bat
```

## ⚠️ Requirements

- Windows 10/11
- Python 3.x installed (with "Add to PATH" checked)
- At least one image file in the `wallpapers` folder

## 🎮 Perfect For

- **Harmless pranks** on friends' computers
- **Personal use** for automatic wallpaper changes
- **Stealth operations** requiring zero visual evidence
- **Clean setups** with minimal files and popups

## 📷 Supported Formats

- `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`

---

**Enjoy your stealth wallpaper adventures!** 🎯✨
