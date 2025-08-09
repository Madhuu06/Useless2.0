# 🔧 TROUBLESHOOTING GUIDE - If Startup Doesn't Work

## 🚨 **Common Issues & Solutions:**

### **Issue 1: Python Not Installed**
**Symptoms:** Error messages about "python not found"
**Solution:**
1. Go to [python.org](https://python.org/downloads/)
2. Download latest Python
3. **IMPORTANT:** Check "Add Python to PATH" during installation
4. Restart computer after installation

### **Issue 2: No Wallpaper Images**
**Symptoms:** "No wallpaper images found" message
**Solution:**
1. Open the `wallpapers` folder
2. Add at least one image file (.jpg, .png, .jpeg, .bmp)
3. Run the script again

### **Issue 3: Startup Not Working After Restart**
**Solution Options (try in order):**

#### **Option A: Use Diagnostic Tool**
1. Double-click `DIAGNOSE_ISSUES.bat`
2. Fix any ❌ errors it shows
3. Try restarting again

#### **Option B: Try PowerShell Method**
1. Double-click `ENABLE_STARTUP_POWERSHELL.bat`
2. Restart computer
3. Check if wallpaper changes

#### **Option C: Manual Startup Setup**
1. Copy the entire wallpaper folder to Desktop
2. Run `ENABLE_STARTUP_SIMPLE.bat` from Desktop location
3. Restart computer

### **Issue 4: Still Not Working**
**Check Debug Log:**
1. Look for `startup_debug.log` file
2. Open it with Notepad
3. Check the last few lines for error messages

**Most Common Fixes:**
- Reinstall Python with "Add to PATH" checked
- Move wallpaper folder to a simpler location (like Desktop)
- Run Windows as Administrator when installing startup

### **🆘 Emergency Method - Manual Desktop Shortcut:**
If automatic startup still doesn't work:
1. Right-click on Desktop → New → Shortcut
2. Browse to `instant_wallpaper.py`
3. Name it "Change Wallpaper"
4. Double-click this shortcut after each restart

## 📞 **Need Help?**
Send the contents of `startup_debug.log` file to debug the issue!
