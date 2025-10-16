# Setup Guide - AI Companion Backend

This guide will walk you through setting up the AI Companion Backend and LLM server after cloning the repository.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Git
- pip (Python package manager)
- A text editor or IDE

## Step-by-Step Setup Process

### Step 1: Clone the Repository

```bash
git clone https://github.com/ParthPatel-1011/AI_Companion.git
cd AI_Companion
```

### Step 2: Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the root directory and add your API keys:

```env
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# ElevenLabs API Configuration (for voice features)
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# Database Configuration (optional - uses SQLite by default)
DATABASE_URL=sqlite:///./ai_companion.db

# Server Configuration
HOST=0.0.0.0
PORT=8000
```

**How to get API keys:**
- **Groq API Key**: Sign up at [https://console.groq.com](https://console.groq.com)
- **ElevenLabs API Key**: Sign up at [https://elevenlabs.io](https://elevenlabs.io)

### Step 5: Setup Database

Initialize the database with the setup script:

**On Windows:**
```bash
python setup_database.py
```

**On Linux/Mac:**
```bash
python3 setup_database.py
```

Or use the provided scripts:

**Windows:**
```bash
setup_database.bat
```

**Linux/Mac:**
```bash
chmod +x setup_database.sh
./setup_database.sh
```

### Step 6: Verify Installation (Optional)

Test the backend connection:

**Windows:**
```bash
test_backend.bat
```

**Linux/Mac:**
```bash
python test_tts.py
```

### Step 7: Start the Backend Server

Now you're ready to start the backend server!

**Option 1: Using the run script (Recommended)**

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

**Option 2: Manual start**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Step 8: Verify Server is Running

Once the server starts, you should see output like:

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Open your browser and navigate to:
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/

### Step 9: Test the Frontend

Open the `index.html` file in your browser to access the AI Companion interface.

**Or** use a simple HTTP server:

```bash
# Python 3
python -m http.server 3000

# Then open http://localhost:3000
```

## LLM Server Configuration

The backend uses **Groq** as the LLM provider, which offers:
- Fast inference speeds
- Multiple model options (Llama 3, Mixtral, etc.)
- Free tier available

### Available Models

The system uses the following Groq models:
- `llama-3.1-70b-versatile` (default for conversations)
- `llama-3.1-8b-instant` (for quick responses)
- `mixtral-8x7b-32768` (for long context)

These are configured in `app/config.py` and don't require a separate LLM server.

## Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**2. Port Already in Use**
```bash
# Change port in run script or use:
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

**3. Database Errors**
```bash
# Delete and recreate database
rm ai_companion.db
python setup_database.py
```

**4. API Key Errors**
- Verify your API keys in the `.env` file
- Ensure there are no extra spaces or quotes
- Check API key validity on provider websites

**5. CORS Errors**
- The backend is configured to allow all origins in development
- Check browser console for specific error messages

### Getting Help

For more detailed troubleshooting, see:
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- [VOICE_SETUP_GUIDE.md](VOICE_SETUP_GUIDE.md) (for voice-specific issues)

## Quick Start Commands

Once setup is complete, you can use these commands:

```bash
# Activate virtual environment
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Start backend server
# Windows: run.bat
# Linux/Mac: ./run.sh

# Or manually:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Next Steps

- Read [GETTING_STARTED.md](GETTING_STARTED.md) for feature overview
- Check [ARCHITECTURE.md](ARCHITECTURE.md) to understand the system design
- Review [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for production deployment

## Project Structure

```
ai_companion_backend/
├── app/
│   ├── models/          # Database models
│   ├── routes/          # API endpoints
│   ├── services/        # Business logic
│   ├── config.py        # Configuration
│   ├── database.py      # Database setup
│   └── main.py          # Application entry point
├── index.html           # Frontend interface
├── requirements.txt     # Python dependencies
├── setup_database.py    # Database initialization
└── .env                 # Environment variables (create this)
```

## Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Review the documentation files
3. Open an issue on GitHub

---

**Happy Coding! 🚀**
