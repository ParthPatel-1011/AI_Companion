#!/bin/bash

echo "========================================"
echo "AI Companion Backend - Setup Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ first"
    exit 1
fi

echo "[1/4] Creating virtual environment..."
python3 -m venv venv

echo "[2/4] Activating virtual environment..."
source venv/bin/activate

echo "[3/4] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[4/4] Setup complete!"
echo ""
echo "========================================"
echo "Next Steps:"
echo "========================================"
echo "1. Make sure MongoDB is running on localhost:27017"
echo "2. Run: ./setup_database.sh (to initialize sample companions)"
echo "3. Run: ./run.sh (to start the server)"
echo ""
echo "Or manually:"
echo "  - Activate venv: source venv/bin/activate"
echo "  - Start server: uvicorn app.main:app --reload"
echo "========================================"
