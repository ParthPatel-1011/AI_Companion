#!/bin/bash

echo "================================================"
echo "  AI Voice Companion - Quick Start"
echo "================================================"
echo ""

# Check .env file
if [ ! -f ".env" ]; then
    echo "[ERROR] .env file not found!"
    echo ""
    echo "Please create .env file and add your API key:"
    echo "  OPENAI_API_KEY=sk-your-key-here"
    echo ""
    echo "See .env.example for reference"
    exit 1
fi

# Check if venv exists
if [ ! -f "venv/bin/activate" ]; then
    echo "[ERROR] Virtual environment not found!"
    echo "Please run ./setup.sh first"
    exit 1
fi

echo "[1/3] Activating virtual environment..."
source venv/bin/activate

echo ""
echo "[2/3] Starting AI Voice Companion Server..."
echo ""
echo "================================================"
echo "  Server will start on http://127.0.0.1:8001"
echo "================================================"
echo ""
echo "  API Docs: http://127.0.0.1:8001/docs"
echo "  Voice Chat UI: Open voice_chat.html in Chrome"
echo ""
echo "  Press Ctrl+C to stop the server"
echo "================================================"
echo ""

echo "[3/3] Launching server..."
python -m uvicorn app.main:app --host 127.0.0.1 --port 8001

echo ""
echo "Server stopped."
