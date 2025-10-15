@echo off
echo ========================================
echo AI Companion Backend - Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
python -m venv venv

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo [4/4] Setup complete!
echo.
echo ========================================
echo Next Steps:
echo ========================================
echo 1. Make sure MongoDB is running on localhost:27017
echo 2. Run: setup_database.bat (to initialize sample companions)
echo 3. Run: run.bat (to start the server)
echo.
echo Or manually:
echo   - Activate venv: venv\Scripts\activate
echo   - Start server: uvicorn app.main:app --reload
echo ========================================
pause
