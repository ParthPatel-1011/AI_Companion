# 🔧 Troubleshooting Guide - AI Voice Companion

## Common Issues and Solutions

---

### ❌ **Problem: Port Already in Use Error**

**Error Message:**
```
[Errno 10048] error while attempting to bind on address ('127.0.0.1', 8001): 
only one usage of each socket address is normally permitted
```

**Cause:** Port 8001 is already being used by another process (usually an old server instance).

**Solution 1: Kill the Process (Windows)**
```bash
# Find the process using port 8001
netstat -ano | findstr :8001

# Kill the process (replace XXXX with the PID number)
taskkill /PID XXXX /F
```

**Solution 2: Kill the Process (Linux/Mac)**
```bash
# Find the process using port 8001
lsof -i :8001

# Kill the process (replace XXXX with the PID)
kill -9 XXXX
```

**Solution 3: Use a Different Port**
```bash
# Start server on port 8002 instead
venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8002
```
Then update `voice_chat.html` line 280:
```javascript
const API_BASE = 'http://127.0.0.1:8002';
```

---

### ❌ **Problem: MongoDB Connection Error**

**Error Message:**
```
ConnectionFailure: [Errno 61] Connection refused
```

**Cause:** MongoDB is not running.

**Solution (Windows):**
```bash
# Start MongoDB service
net start MongoDB

# OR manually start mongod
mongod --dbpath="C:\data\db"
```

**Solution (Linux/Mac):**
```bash
# Start MongoDB service
sudo systemctl start mongod

# OR using Homebrew (Mac)
brew services start mongodb-community
```

**Verify MongoDB is Running:**
```bash
# Connect with MongoDB Compass
mongodb://localhost:27017/
```

---

### ❌ **Problem: API Key Not Valid**

**Error Message:**
```
Error code: 401 - Invalid API Key
```

**Cause:** OpenAI API key is missing or incorrect.

**Solution:**

1. **Edit `.env` file:**
   ```env
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

2. **Get a valid API key:**
   - OpenAI: https://platform.openai.com/api-keys
   - Groq (Free): https://console.groq.com/keys

3. **Restart the server** after changing `.env`

---

### ❌ **Problem: ModuleNotFoundError**

**Error Message:**
```
ModuleNotFoundError: No module named 'openai'
```

**Cause:** Dependencies not installed.

**Solution:**
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install all dependencies
pip install -r requirements.txt
```

---

### ❌ **Problem: TTS Not Available**

**Error Message:**
```
TTS service not available
```

**Cause:** OpenAI API key not configured for TTS.

**Solution:**

1. **Check `.env` file:**
   ```env
   USE_OPENAI_TTS=true
   OPENAI_API_KEY=sk-your-key-here
   ```

2. **Test TTS endpoint:**
   ```bash
   curl http://127.0.0.1:8001/voice/check-tts
   ```

3. **Restart server** after changes

---

### ❌ **Problem: Microphone Not Working**

**Cause:** Browser doesn't have microphone permission or speech recognition not supported.

**Solution:**

1. **Use Chrome or Edge** (Firefox doesn't support Web Speech API)

2. **Allow microphone permission** when browser asks

3. **Check browser console** (F12) for errors

4. **Test microphone:**
   - Go to chrome://settings/content/microphone
   - Make sure your site is allowed

5. **For HTTPS requirement:**
   - Speech recognition requires secure context (HTTPS or localhost)
   - localhost works fine for development

---

### ❌ **Problem: No Audio Playback**

**Cause:** Audio blocked by browser or TTS failed.

**Solution:**

1. **Check browser audio settings**
   - Unmute the tab
   - Check system volume

2. **Check browser console** (F12) for errors

3. **Test direct TTS endpoint:**
   ```bash
   curl "http://127.0.0.1:8001/voice/tts?text=Hello&voice=nova" --output test.mp3
   ```

4. **Try different voice:**
   - Edit in `voice_chat.html` or `.env`
   - Options: nova, alloy, echo, fable, onyx, shimmer

---

### ❌ **Problem: CORS Error**

**Error Message:**
```
Access to fetch blocked by CORS policy
```

**Cause:** Frontend and backend on different domains without proper CORS setup.

**Solution:**

Backend already configured in `app/main.py`, but if needed:

```python
# In app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### ❌ **Problem: Virtual Environment Not Found**

**Error Message:**
```
venv\Scripts\activate : The term is not recognized
```

**Cause:** Virtual environment not created.

**Solution:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

---

### ❌ **Problem: Import Error in Services**

**Error Message:**
```
ImportError: cannot import name 'settings' from 'app.config'
```

**Cause:** Missing or incorrect imports.

**Solution:**

1. **Check `.env` file exists** in project root

2. **Verify pydantic-settings installed:**
   ```bash
   pip install pydantic-settings
   ```

3. **Restart server**

---

## 🔍 **Debugging Tips**

### **Check Server Logs**
Watch the terminal where server is running for detailed error messages.

### **Test API Endpoints**
```bash
# Health check
curl http://127.0.0.1:8001/

# Check TTS
curl http://127.0.0.1:8001/voice/check-tts

# Test signup
curl -X POST http://127.0.0.1:8001/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@test.com","voice_preference":"nova","gender_preference":"girl"}'
```

### **Check MongoDB**
```bash
# Test connection
python -c "from app.database import db; print('MongoDB OK')"

# View data in MongoDB Compass
mongodb://localhost:27017/AICompanionDB
```

### **Verify API Key**
```bash
# Check if key is loaded
python -c "from app.config import settings; print(settings.openai_api_key[:10] + '...')"
```

---

## 🆘 **Still Having Issues?**

### **1. Clear Everything and Restart**
```bash
# Windows
taskkill /F /IM python.exe
venv\Scripts\activate
pip install -r requirements.txt
venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001
```

### **2. Check System Requirements**
- Python 3.8+ installed
- MongoDB running
- Modern browser (Chrome/Edge)
- Internet connection for API calls

### **3. Review Documentation**
- VOICE_SETUP_GUIDE.md
- VOICE_SYSTEM_SUMMARY.md
- README.md

### **4. Test Step by Step**
1. MongoDB connection ✓
2. Server starts ✓
3. API responds ✓
4. Frontend loads ✓
5. Microphone works ✓
6. TTS plays ✓

---

## ✅ **Quick Fix Commands**

**Restart Server:**
```bash
# Kill old process
taskkill /F /IM python.exe

# Start fresh
venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001
```

**Reset Database:**
```bash
python setup_database.py
```

**Reinstall Dependencies:**
```bash
venv\Scripts\activate
pip install --upgrade -r requirements.txt
```

---

**Last Updated:** 2025-10-15  
**Version:** 2.0
