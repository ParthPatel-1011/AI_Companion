#!/bin/bash

echo "========================================"
echo "Starting AI Companion Backend Server"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -f "venv/bin/activate" ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please run ./setup.sh first"
    exit 1
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Starting FastAPI server..."
echo ""
echo "Server will be available at:"
echo "  - API: http://127.0.0.1:8000"
echo "  - Docs: http://127.0.0.1:8000/docs"
echo "  - Test UI: Open index.html in your browser"
echo ""
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo ""

uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
