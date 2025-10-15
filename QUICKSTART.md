# 🚀 Quick Start Guide - AI Companion Backend

## Prerequisites
✅ Python 3.8 or higher installed  
✅ MongoDB running on `localhost:27017`  
✅ MongoDB Compass (optional, for viewing data)

---

## Option 1: Automated Setup (Recommended) ⚡

### Windows Users:

```bash
# 1. Run setup script
setup.bat

# 2. Initialize database with sample companions
setup_database.bat

# 3. Start the server
run.bat
```

### Linux/Mac Users:

```bash
# 1. Make scripts executable
chmod +x setup.sh run.sh setup_database.sh

# 2. Run setup script
./setup.sh

# 3. Initialize database
./setup_database.sh

# 4. Start the server
./run.sh
```

---

## Option 2: Manual Setup 🔧

### Step 1: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Initialize Database

```bash
python setup_database.py
```

This will create:
- Database: `AICompanionDB`
- Sample companions: Emma (girl) and Alex (boy)

### Step 4: Start the Server

```bash
uvicorn app.main:app --reload
```

---

## 🎯 Testing the Application

### 1. Access the API Documentation
Open in browser: http://127.0.0.1:8000/docs

### 2. Open the Test UI
Double-click `index.html` to open the chat interface

### 3. Create a User (Using API Docs or cURL)

**Option A - Using Swagger UI:**
1. Go to http://127.0.0.1:8000/docs
2. Expand `POST /auth/signup`
3. Click "Try it out"
4. Enter user data:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "voice_preference": "default",
  "gender_preference": "girl"
}
```
5. Click "Execute"
6. Copy the `user_id` from the response

**Option B - Using cURL:**
```bash
curl -X POST "http://127.0.0.1:8000/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "voice_preference": "default",
    "gender_preference": "girl"
  }'
```

### 4. Start Chatting!

1. Open `index.html` in your browser
2. Paste your `user_id` in the User ID field
3. Select a companion (Emma or Alex)
4. Type a message and click "Send"

---

## 📊 View Database in MongoDB Compass

1. Open MongoDB Compass
2. Connect to: `mongodb://localhost:27017/`
3. Navigate to `AICompanionDB` database
4. You'll see three collections:
   - `users` - User accounts
   - `companions` - AI personalities
   - `chats` - Conversation history

---

## 🎨 Sample API Requests

### Login
```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "john@example.com"}'
```

### Get Companion Story
```bash
curl "http://127.0.0.1:8000/companion/get_story/girl"
```

### Send Chat Message
```bash
curl -X POST "http://127.0.0.1:8000/chat/send" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "YOUR_USER_ID_HERE",
    "companion_gender": "girl",
    "message": "Hey! How are you?"
  }'
```

### Get Chat History
```bash
curl "http://127.0.0.1:8000/chat/history/YOUR_USER_ID_HERE?limit=20"
```

---

## 🔧 Troubleshooting

### MongoDB Connection Error
**Problem:** `ConnectionFailure: [Errno 61] Connection refused`

**Solution:**
- Ensure MongoDB is running
- Windows: Start MongoDB service from Services
- Mac: `brew services start mongodb-community`
- Linux: `sudo systemctl start mongod`

### Module Not Found Error
**Problem:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
# Make sure virtual environment is activated
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Port Already in Use
**Problem:** `Error: [Errno 48] Address already in use`

**Solution:**
```bash
# Use a different port
uvicorn app.main:app --reload --port 8001
```

Then update the frontend URL in `index.html`:
```javascript
fetch("http://127.0.0.1:8001/chat/send", ...)
```

---

## 📝 Next Steps

1. ✅ **Integrate Real LLM**: Replace mock responses with OpenAI/Anthropic API
2. ✅ **Add Authentication**: Implement JWT tokens for secure sessions
3. ✅ **Add TTS/STT**: Integrate voice input/output
4. ✅ **Add More Companions**: Create diverse AI personalities
5. ✅ **Deploy**: Host on cloud platforms (AWS, Google Cloud, etc.)

---

## 🎉 You're All Set!

Your AI Companion Backend is ready! Start chatting with Emma or Alex and enjoy the conversation! 🚀

For detailed documentation, see `README.md`
