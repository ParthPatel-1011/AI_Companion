# 🎤 Microphone Setup & Troubleshooting Guide

## ✅ Quick Fix for "Error. Try again."

When you click the microphone button and see "Error. Try again.", it's usually a **microphone permission** issue.

---

## 🔧 Step-by-Step Fix

### **For Chrome Users:** (Recommended)

1. **Open** [voice_chat.html](file://d:\Backup\My_Projects\MP\newMP\AIMP\ai_companion_backend\voice_chat.html)

2. **Look for the 🔒 icon** in the address bar (left side)

3. **Click on the 🔒 icon**

4. **Find "Microphone"** in the dropdown

5. **Change to "Allow"**

6. **Refresh the page** (F5)

7. **Click the microphone button again**

---

### **For Edge Users:**

1. Open voice_chat.html

2. Click the **🔒 lock icon** in address bar

3. Click **"Permissions for this site"**

4. Find **"Microphone"**

5. Select **"Allow"**

6. Refresh and try again

---

### **For Safari Users:**

1. Open voice_chat.html

2. Go to **Safari > Settings for This Website**

3. Find **"Microphone"**

4. Select **"Allow"**

5. Refresh and try again

---

## 🎯 Common Error Messages & Solutions

### **Error: "Microphone blocked"**

**Cause:** Browser doesn't have microphone permission

**Solution:**
1. Click 🔒 icon in address bar
2. Set Microphone to "Allow"
3. Refresh page
4. Try again

---

### **Error: "No speech detected"**

**Cause:** You didn't speak, or spoke too quietly

**Solution:**
1. Speak louder and clearer
2. Make sure microphone is working
3. Check system microphone settings
4. Try again

---

### **Error: "No microphone found"**

**Cause:** No microphone connected

**Solution:**
1. Connect a microphone or headset
2. Check if microphone is plugged in
3. Test microphone in system settings
4. Refresh page

---

### **Error: "Network error"**

**Cause:** Internet connection issue

**Solution:**
1. Check your internet connection
2. Make sure backend server is running
3. Try again

---

### **Error: "Speech recognition not supported"**

**Cause:** Browser doesn't support Web Speech API

**Solution:**
- ❌ **Don't use Firefox** (not supported)
- ✅ **Use Chrome** (best support)
- ✅ **Use Edge** (good support)
- ✅ **Use Safari** (Mac/iOS)

---

## ✅ How to Test Your Microphone

### **Test 1: System Check**

**Windows:**
1. Right-click speaker icon in taskbar
2. Click "Sound settings"
3. Scroll to "Input"
4. Speak and watch the bar move

**Mac:**
1. System Preferences > Sound
2. Click "Input" tab
3. Select microphone
4. Speak and watch level meter

---

### **Test 2: Browser Check**

1. Open: **chrome://settings/content/microphone** (Chrome)
2. Or: **edge://settings/content/microphone** (Edge)
3. Check if microphone is listed
4. Make sure it's not blocked

---

### **Test 3: Live Test**

1. Go to: **https://www.onlinemictest.com/**
2. Click "Allow microphone"
3. Speak and see if it detects
4. If working, your mic is fine!

---

## 🎤 Microphone Best Practices

### **For Best Results:**

1. ✅ **Use a headset** - Avoids echo and feedback
2. ✅ **Speak clearly** - Normal pace, clear pronunciation
3. ✅ **Quiet environment** - Reduce background noise
4. ✅ **Test first** - Make sure mic works before chatting
5. ✅ **Check levels** - Not too loud, not too quiet

---

### **Common Mistakes to Avoid:**

1. ❌ Don't use built-in laptop mic if possible (poor quality)
2. ❌ Don't speak too fast
3. ❌ Don't have TV/music loud in background
4. ❌ Don't use Firefox (no support)
5. ❌ Don't forget to allow permissions

---

## 🔍 Detailed Troubleshooting

### **Issue: Microphone button stays disabled**

**Check:**
1. Are you using Chrome/Edge/Safari?
2. Is voice_chat.html open in browser?
3. Check browser console (F12) for errors

**Solution:**
- Use Chrome browser
- Refresh the page
- Check console for specific error

---

### **Issue: "Already listening" message**

**Cause:** Speech recognition already started

**Solution:**
- Wait a few seconds
- Refresh the page
- Try clicking mic button again

---

### **Issue: Audio doesn't play**

**Cause:** Browser audio blocked or TTS issue

**Solution:**
1. Check browser isn't muted (tab icon)
2. Check system volume
3. Make sure OpenAI API key is set
4. Check server logs for errors

---

### **Issue: Keeps saying "No speech detected"**

**Possible causes:**
1. Microphone is muted in system
2. Wrong microphone selected
3. Speaking too quietly
4. Microphone not working

**Solution:**
1. Check system mic settings
2. Select correct microphone
3. Speak louder
4. Test mic at onlinemictest.com

---

## 🎯 Complete Setup Checklist

Before using voice chat, make sure:

- [ ] Using **Chrome, Edge, or Safari** (not Firefox)
- [ ] **Backend server running** on port 8001
- [ ] **Microphone connected** and working
- [ ] **Browser has microphone permission** (🔒 icon shows "Allow")
- [ ] **System microphone not muted**
- [ ] **Correct microphone selected** in system settings
- [ ] **Internet connection** working
- [ ] **Account created** and logged in
- [ ] **OpenAI API key** set in .env

---

## 💡 Pro Tips

### **Tip 1: First Time Setup**
When you first open voice_chat.html:
1. Browser will ask "Allow microphone?"
2. Click **"Allow"**
3. Give it a few seconds
4. Then click mic button

### **Tip 2: Hands-Free Mode**
For the best experience:
1. Get voice working first (manual mode)
2. Then enable "🔄 Hands-free mode"
3. AI will auto-listen after speaking
4. No need to click buttons!

### **Tip 3: Testing**
Before a long conversation:
1. Test with a simple "Hello"
2. Make sure you hear AI response
3. Check microphone quality
4. Adjust volume if needed

---

## 🆘 Still Not Working?

### **Quick Diagnostic:**

Run these checks in order:

1. **Browser Check:**
   ```
   Open Chrome → See if mic icon appears
   ```

2. **Permission Check:**
   ```
   Click 🔒 in address bar → Check Microphone = Allow
   ```

3. **Server Check:**
   ```
   curl http://127.0.0.1:8001/voice/check-tts
   ```

4. **Console Check:**
   ```
   Press F12 → Look for errors in Console tab
   ```

5. **Microphone Check:**
   ```
   Go to onlinemictest.com → Test mic
   ```

---

### **If Still Failing:**

**Check the browser console (F12)** and look for:

- `"not-allowed"` → Permission denied, allow microphone
- `"no-speech"` → Didn't hear you, speak louder
- `"audio-capture"` → No mic found, connect one
- `"network"` → Internet issue, check connection

---

## ✅ Success Signs

You'll know it's working when you see:

1. ✅ Mic button lights up when clicked
2. ✅ Status shows "🎤 Listening..."
3. ✅ Voice visualizer animates
4. ✅ Your speech appears in chat
5. ✅ AI responds with text
6. ✅ You hear AI voice response

---

## 📞 Common Questions

**Q: Do I need to install anything?**
A: No! Just use Chrome browser.

**Q: Does it work offline?**
A: No, requires internet for AI and TTS.

**Q: Which browser is best?**
A: Chrome has the best speech recognition.

**Q: Can I use on mobile?**
A: Yes! Chrome on Android, Safari on iOS.

**Q: Why does it stop listening?**
A: Normal behavior. Enable "Hands-free mode" for auto-listen.

**Q: Is my voice data stored?**
A: Only the text transcript is stored, not audio.

---

## 🎉 You're Ready!

Once you:
1. ✅ Allow microphone in browser
2. ✅ See the mic button light up
3. ✅ Hear the AI respond

You're all set for voice conversations! 🎤🤖

**Happy talking!** 🎉

---

**Need more help?**
- Check TROUBLESHOOTING.md for general issues
- Check server logs in terminal
- Press F12 and check Console tab

**Last Updated:** 2025-10-15
