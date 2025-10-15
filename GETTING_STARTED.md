# 🎉 AI Companion Backend - Getting Started

## ✅ Project Setup Complete!

Your AI Companion Backend is now fully set up and running!

---

## 🌐 Server Information

**Backend API:** `http://127.0.0.1:8001`  
**API Documentation (Swagger UI):** `http://127.0.0.1:8001/docs`  
**Alternative Docs (ReDoc):** `http://127.0.0.1:8001/redoc`  
**Test Frontend UI:** Open `index.html` in your browser

---

## 📋 Quick Test Steps

### 1. Create a User Account

Open your browser and navigate to: `http://127.0.0.1:8001/docs`

Find the **POST /auth/signup** endpoint and click "Try it out"

Use this sample data:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "voice_preference": "default",
  "gender_preference": "girl"
}
```

Click "Execute" and **copy the `user_id`** from the response!

### 2. Test the Chat UI

1. Double-click `index.html` to open the test frontend
2. Paste your `user_id` in the User ID field
3. Select a companion (Emma or Alex)
4. Type a message like "Hey! How are you today?"
5. Click "Send" and watch the AI respond!

---

## 📊 Database Information

**Database Name:** `AICompanionDB`  
**MongoDB URI:** `mongodb://localhost:27017/`

### Collections Created:

1. **users** - User accounts and preferences
2. **companions** - AI personalities (Emma & Alex pre-loaded)
3. **chats** - Conversation history

You can view these in MongoDB Compass!

---

## 🤖 Pre-loaded AI Companions

### Emma (Girl)
- **Age:** 22
- **Personality:** Cheerful, creative, empathetic
- **Interests:** Art, music, movies, coffee, photography
- **Backstory:** An art student who loves deep conversations

### Alex (Boy)
- **Age:** 24
- **Personality:** Intelligent, friendly, supportive
- **Interests:** Technology, gaming, coding, sci-fi
- **Backstory:** A tech enthusiast passionate about AI

---

## 🔧 API Endpoints Reference

### Authentication
- `POST /auth/signup` - Register new user
- `POST /auth/login` - Login with email
- `GET /auth/user/{user_id}` - Get user info
- `GET /auth/users` - List all users

### Companion Management
- `GET /companion/get_story/{gender}` - Get companion by gender
- `GET /companion/all` - List all companions
- `GET /companion/{companion_id}` - Get specific companion
- `POST /companion/create` - Create new companion
- `DELETE /companion/{companion_id}` - Delete companion

### Chat
- `POST /chat/send` - Send message and get AI response
- `GET /chat/history/{user_id}` - Get chat history
- `GET /chat/stats/{user_id}` - Get chat statistics
- `DELETE /chat/history/{user_id}` - Clear chat history

---

## 💻 Command Reference

### Start the Server
```bash
# Windows - from ai_companion_backend directory
venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001

# Linux/Mac
source venv/bin/activate
uvicorn app.main:app --host 127.0.0.1 --port 8001
```

### Stop the Server
Press `Ctrl+C` in the terminal where the server is running

### Reinitialize Database
```bash
# Windows
venv\Scripts\activate
python setup_database.py

# Linux/Mac
source venv/bin/activate
python setup_database.py
```

---

## 🧪 Sample API Requests

### Using PowerShell (Windows)

**Create User:**
```powershell
$body = @{
    name = "Test User"
    email = "test@example.com"
    voice_preference = "default"
    gender_preference = "girl"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8001/auth/signup" -Method Post -Body $body -ContentType "application/json"
```

**Send Chat:**
```powershell
$body = @{
    user_id = "YOUR_USER_ID_HERE"
    companion_gender = "girl"
    message = "Hey! How are you?"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8001/chat/send" -Method Post -Body $body -ContentType "application/json"
```

### Using curl (Linux/Mac/Git Bash)

**Create User:**
```bash
curl -X POST "http://127.0.0.1:8001/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","voice_preference":"default","gender_preference":"girl"}'
```

**Send Chat:**
```bash
curl -X POST "http://127.0.0.1:8001/chat/send" \
  -H "Content-Type: application/json" \
  -d '{"user_id":"YOUR_USER_ID","companion_gender":"girl","message":"Hey! How are you?"}'
```

---

## 📁 Project Structure

```
ai_companion_backend/
├── app/
│   ├── main.py              # FastAPI application
│   ├── database.py          # MongoDB connection
│   ├── models/              # Data models
│   │   ├── user_model.py
│   │   ├── companion_model.py
│   │   └── chat_model.py
│   ├── routes/              # API endpoints
│   │   ├── auth_routes.py
│   │   ├── companion_routes.py
│   │   └── chat_routes.py
│   └── services/            # Business logic
│       ├── ai_service.py    # AI response generation
│       └── user_service.py  # User operations
├── venv/                    # Virtual environment
├── index.html               # Test frontend UI
├── requirements.txt         # Python dependencies
├── setup_database.py        # Database initialization
├── setup.bat / setup.sh     # Setup scripts
├── run.bat / run.sh         # Run scripts
├── README.md                # Full documentation
├── QUICKSTART.md            # Quick start guide
└── GETTING_STARTED.md       # This file!
```

---

## 🚀 Next Steps

### 1. Test All Features
- ✅ Create users via API
- ✅ Chat with Emma and Alex
- ✅ View chat history
- ✅ Test different message types

### 2. Customize Companions
Edit companions in MongoDB or use the API to create new ones with different personalities!

### 3. Integrate Real LLM
Replace the mock AI service with OpenAI, Anthropic, or other LLM APIs:

Edit `app/services/ai_service.py`:
```python
import openai

def generate_contextual_response(self, prompt: str, companion_context: Dict) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": companion_context["backstory"]},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
```

### 4. Future Enhancements
- Add voice chat (TTS/STT)
- Implement authentication tokens
- Add face recognition
- Deploy to cloud (AWS, Google Cloud, Azure)
- Add more personality traits
- Implement emotion detection

---

## 🐛 Troubleshooting

### Server Not Starting
- Make sure MongoDB is running
- Check if port 8001 is available
- Verify virtual environment is activated

### Database Connection Error
- Start MongoDB: `mongod` or check MongoDB service
- Verify connection string in `app/database.py`

### Import Errors
- Activate venv: `venv\Scripts\activate` (Windows)
- Reinstall: `pip install -r requirements.txt`

---

## 📞 Support

For issues or questions:
1. Check `README.md` for detailed documentation
2. Review `QUICKSTART.md` for setup instructions
3. Check MongoDB Compass for database issues
4. Review FastAPI docs at `/docs` endpoint

---

## 🎊 Congratulations!

You've successfully set up a complete AI Companion Backend with:
- ✅ FastAPI REST API
- ✅ MongoDB database with sample data
- ✅ Two AI companions (Emma & Alex)
- ✅ Chat system with memory
- ✅ Test frontend UI
- ✅ Full API documentation

**Enjoy building your AI companion application! 🚀**

---

*Last Updated: 2025-10-15*
