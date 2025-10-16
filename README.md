# AI Companion Backend

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-green)
![SQLite](https://img.shields.io/badge/SQLite-Latest-brightgreen)
![LLM](https://img.shields.io/badge/LLM-Groq-purple)
![TTS](https://img.shields.io/badge/TTS-ElevenLabs-orange)

A complete backend system for an AI Companion application using **FastAPI**, **SQLite**, and **Groq LLM**. This system enables human-like conversations between users and AI companions (Emma & Alex) with memory retention, personality-driven responses, and voice capabilities powered by ElevenLabs.

## 🌐 Live Demo

- **Frontend**: [https://parthpatel-1011.github.io/AI_Companion/](https://parthpatel-1011.github.io/AI_Companion/)
- **Repository**: [https://github.com/ParthPatel-1011/AI_Companion](https://github.com/ParthPatel-1011/AI_Companion)

## 🌟 Features

- **Groq LLM Integration**: Fast, free AI responses using Llama 3.1 models
- **Voice Features**: Natural text-to-speech with ElevenLabs (gender-appropriate voices)
- **User Management**: Simple name-based authentication system
- **AI Companions**: Emma (girl) and Alex (boy) with unique personalities
- **Conversational Memory**: Context-aware responses with conversation history
- **Chat History**: Persistent storage of all conversations
- **RESTful API**: Clean, documented API endpoints with FastAPI
- **SQLite Database**: Simple, file-based data storage
- **Modular Architecture**: Easy to extend with new features
- **Live Demo**: Deployed and accessible via GitHub Pages

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

## 🚀 Quick Start

### For Complete Setup Instructions

📖 **NEW USERS**: See our comprehensive [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed step-by-step installation instructions including:
- Virtual environment setup
- API key configuration (Groq, ElevenLabs)
- Database initialization
- LLM server setup
- Troubleshooting common issues

### Prerequisites

- Python 3.8+
- Groq API Key (free at [https://console.groq.com](https://console.groq.com))
- ElevenLabs API Key (optional, for voice features - [https://elevenlabs.io](https://elevenlabs.io))

### Quick Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ParthPatel-1011/AI_Companion.git
   cd ai_companion_backend
   ```

2. **Run setup script**
   
   **Windows:**
   ```bash
   setup.bat
   ```
   
   **Linux/Mac:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Configure environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ```

4. **Initialize database**
   
   **Windows:**
   ```bash
   setup_database.bat
   ```
   
   **Linux/Mac:**
   ```bash
   chmod +x setup_database.sh
   ./setup_database.sh
   ```

## 🏃 Running the Application

### Start the Backend Server

**Using run scripts (Recommended):**

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

**Or manually:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start at: `http://localhost:8000`

### API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/

### Test the Frontend

Open `index.html` in your web browser or serve it using:

```bash
python -m http.server 3000
# Then open http://localhost:3000
```

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

## 🔧 Configuration

### Environment Variables

The application uses environment variables for configuration. Create a `.env` file:

```env
# Required
GROQ_API_KEY=your_groq_api_key_here

# Optional (for voice features)
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# Database (SQLite by default)
DATABASE_URL=sqlite:///./ai_companion.db

# Server Configuration
HOST=0.0.0.0
PORT=8000
```

### LLM Configuration

The system uses **Groq** as the LLM provider with the following models:
- `llama-3.1-70b-versatile` (default for conversations)
- `llama-3.1-8b-instant` (for quick responses)
- `mixtral-8x7b-32768` (for long context)

Configuration is in [`app/config.py`](app/config.py).

### Voice Configuration

Voice features use ElevenLabs TTS. See [VOICE_SETUP_GUIDE.md](VOICE_SETUP_GUIDE.md) for details.

## 📊 Database Collections

### Users Collection
Stores user information and authentication data.

### Companions Collection
Stores AI companion personalities and backstories (Emma and Alex).

### Chats Collection
Stores all conversation history between users and companions.

### Messages Collection
Stores individual messages with sentiment analysis and context.

The system uses **SQLite** by default for easy setup. Data is stored in `ai_companion.db`.

## 🔮 Future Extensions

This modular architecture supports easy integration of:

- **Advanced Voice Features** - Real-time voice conversations
- **Multi-language Support** - Conversations in multiple languages
- **Custom Companions** - User-created AI personalities

## 🐛 Troubleshooting

For detailed troubleshooting, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

### Quick Fixes

**API Key Errors:**
```bash
# Check your .env file for correct API keys
# Ensure no extra spaces or quotes
```

**Import Errors:**
```bash
# Activate virtual environment and reinstall
pip install --upgrade -r requirements.txt
```

**Port Already in Use:**
```bash
# Change port in run script or use:
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

**Database Errors:**
```bash
# Delete and recreate database
rm ai_companion.db
python setup_database.py
```

For voice-related issues, see [VOICE_SETUP_GUIDE.md](VOICE_SETUP_GUIDE.md).

## 📝 License

This project is open-source and available for educational and commercial use.

## 👥 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 🙏 Acknowledgments

Built with FastAPI, MongoDB, and Python.

---

**Happy Coding! 🚀**
