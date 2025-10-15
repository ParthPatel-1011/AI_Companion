#!/bin/bash

echo "========================================"
echo "AI Companion - Database Setup"
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

echo "Running database setup script..."
echo ""
python setup_database.py

echo ""
