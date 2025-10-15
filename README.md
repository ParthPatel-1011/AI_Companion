# AI Companion Backend

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Latest-brightgreen)
![LLM](https://img.shields.io/badge/LLM-Groq%20%7C%20OpenAI%20%7C%20Anthropic-purple)

A complete backend system for an AI Companion application using **FastAPI** and **MongoDB**. This system enables human-like conversations between users and AI companions (boy/girl) with memory retention and personality-driven responses.

## 🌐 Live Demo

- **Frontend**: [https://parthpatel-1011.github.io/AI_Companion/](https://parthpatel-1011.github.io/AI_Companion/)
- **Repository**: [https://github.com/ParthPatel-1011/AI_Companion](https://github.com/ParthPatel-1011/AI_Companion)

## 🌟 Features

- **Multi-LLM Support**: Switch between Groq (free & fast!), OpenAI, and Anthropic
- **User Management**: Registration and login system
- **AI Companions**: Multiple AI personalities (boy/girl) with unique backstories
- **Conversational AI**: Context-aware, human-like responses powered by LLMs
- **Chat Memory**: Persistent conversation history
- **RESTful API**: Clean, documented API endpoints
- **MongoDB Integration**: Flexible, unstructured data storage
- **Modular Architecture**: Easy to extend with new features
- **Live Demo**: Deployed on GitHub Pages

## 📁 Project Structure

```
ai_companion_backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── database.py             # MongoDB connection and collections
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user_model.py       # User data models
│   │   ├── companion_model.py  # Companion data models
│   │   └── chat_model.py       # Chat data models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py      # Authentication endpoints
│   │   ├── companion_routes.py # Companion management endpoints
│   │   └── chat_routes.py      # Chat endpoints
│   └── services/
│       ├── __init__.py
│       ├── ai_service.py       # AI response generation
│       └── user_service.py     # User business logic
├── requirements.txt
├── README.md
└── index.html                  # Test frontend UI
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MongoDB (installed and running on `localhost:27017`)
- MongoDB Compass (optional, for database visualization)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd ai_companion_backend
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure MongoDB is running**
   - Start MongoDB service
   - Verify connection at `mongodb://localhost:27017/`

5. **Initialize the database with companion data**
   
   Open MongoDB Compass and connect to `mongodb://localhost:27017/`
   
   Create database: `AICompanionDB`
   
   Create collection: `companions`
   
   Insert sample companions:

   **Girl Companion:**
   ```json
   {
     "name": "Emma",
     "gender": "girl",
     "age": 22,
     "backstory": "I'm Emma, a cheerful art student who loves painting and music. I'm always excited to learn about new things and meet interesting people. I enjoy deep conversations about life, art, and dreams. I'm empathetic and love helping others feel better.",
     "personality_traits": ["cheerful", "creative", "empathetic", "curious"],
     "interests": ["art", "music", "movies", "coffee", "photography"],
     "speaking_style": "friendly",
     "created_at": {"$date": "2025-10-15T00:00:00Z"}
   }
   ```

   **Boy Companion:**
   ```json
   {
     "name": "Alex",
     "gender": "boy",
     "age": 24,
     "backstory": "I'm Alex, a tech enthusiast and gamer who loves exploring new technologies. I'm passionate about coding, gaming, and sci-fi movies. I'm friendly, supportive, and always up for a good conversation about anything from tech to philosophy.",
     "personality_traits": ["intelligent", "friendly", "supportive", "curious"],
     "interests": ["technology", "gaming", "coding", "sci-fi", "music"],
     "speaking_style": "casual",
     "created_at": {"$date": "2025-10-15T00:00:00Z"}
   }
   ```

## 🏃 Running the Application

### Start the Backend Server

```bash
# Make sure you're in the ai_companion_backend directory
uvicorn app.main:app --reload
```

The server will start at: `http://127.0.0.1:8000`

### API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### Test the Frontend

Open `index.html` in your web browser to test the chat functionality.

## 📚 API Endpoints

### Authentication
- `POST /auth/signup` - Register a new user
- `POST /auth/login` - Login with email
- `GET /auth/user/{user_id}` - Get user information
- `GET /auth/users` - Get all users

### Companion Management
- `GET /companion/get_story/{gender}` - Get companion by gender (boy/girl)
- `GET /companion/all` - Get all companions
- `GET /companion/{companion_id}` - Get companion by ID
- `POST /companion/create` - Create new companion
- `DELETE /companion/{companion_id}` - Delete companion

### Chat
- `POST /chat/send` - Send message and get AI response
- `GET /chat/history/{user_id}` - Get chat history
- `GET /chat/stats/{user_id}` - Get chat statistics
- `DELETE /chat/history/{user_id}` - Clear chat history

## 💡 Usage Examples

### 1. Register a User

```bash
curl -X POST "http://127.0.0.1:8000/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "voice_preference": "female_1",
    "gender_preference": "girl"
  }'
```

### 2. Send a Chat Message

```bash
curl -X POST "http://127.0.0.1:8000/chat/send" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "YOUR_USER_ID",
    "companion_gender": "girl",
    "message": "Hey! How are you today?"
  }'
```

### 3. Get Chat History

```bash
curl "http://127.0.0.1:8000/chat/history/YOUR_USER_ID?limit=20"
```

## 🔧 Configuration

### Database Configuration

Edit `app/database.py` to change MongoDB connection settings:

```python
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "AICompanionDB"
```

### AI Service Configuration

The AI service in `app/services/ai_service.py` currently uses mock responses. To integrate with a real LLM (e.g., OpenAI):

```python
# In ai_service.py, replace the generate_contextual_response method:

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

## 📊 Database Collections

### Users Collection
Stores user information and preferences.

### Companions Collection
Stores AI companion personalities and backstories.

### Chats Collection
Stores all conversation history between users and companions.

## 🔮 Future Extensions

This modular architecture supports easy integration of:

- **Text-to-Speech (TTS)** - Voice output
- **Speech-to-Text (STT)** - Voice input
- **Face Recognition** - Visual identification
- **Emotion Detection** - Sentiment analysis
- **Real LLM Integration** - OpenAI, Anthropic, etc.
- **Advanced Memory** - Long-term conversation memory
- **Multi-modal Input** - Images, voice, video

## 🐛 Troubleshooting

### MongoDB Connection Error
- Ensure MongoDB is running: `mongod --version`
- Check if MongoDB service is active
- Verify connection string in `database.py`

### Import Errors
- Activate virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

### Port Already in Use
- Change port in startup command: `uvicorn app.main:app --reload --port 8001`

## 📝 License

This project is open-source and available for educational and commercial use.

## 👥 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 🙏 Acknowledgments

Built with FastAPI, MongoDB, and Python.

---

**Happy Coding! 🚀**
