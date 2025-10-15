@echo off
echo ================================================
echo   AI Voice Companion - Quick Start
echo ================================================
echo.

REM Check .env file
if not exist ".env" (
    echo [ERROR] .env file not found!
    echo.
    echo Please create .env file and add your API key:
    echo   OPENAI_API_KEY=sk-your-key-here
    echo.
    echo See .env.example for reference
    pause
    exit /b 1
)

REM Check if venv exists
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

echo [1/3] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [2/3] Starting AI Voice Companion Server...
echo.
echo ================================================
echo   Server will start on http://127.0.0.1:8001
echo ================================================
echo.
echo   API Docs: http://127.0.0.1:8001/docs
echo   Voice Chat UI: Open voice_chat.html in Chrome
echo.
echo   Press Ctrl+C to stop the server
echo ================================================
echo.

echo [3/3] Launching server...
venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001

echo.
echo Server stopped.
pause
