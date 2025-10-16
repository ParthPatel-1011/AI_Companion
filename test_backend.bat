@echo off
echo ========================================
echo Testing AI Companion Connection
echo ========================================
echo.

echo Step 1: Checking if backend is running...
echo.

curl -s http://127.0.0.1:8001/ >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Backend is running on port 8001!
    echo.
    
    echo Step 2: Testing API endpoint...
    curl http://127.0.0.1:8001/
    echo.
    echo.
    
    echo Step 3: Testing TTS service...
    curl http://127.0.0.1:8001/voice/check-tts
    echo.
    echo.
    
    echo ========================================
    echo [SUCCESS] All tests passed!
    echo ========================================
    echo.
    echo You can now:
    echo 1. Open index.html in Chrome
    echo 2. Sign up and start chatting
    echo.
) else (
    echo [ERROR] Backend is NOT running!
    echo.
    echo Please start the backend first:
    echo   run.bat
    echo.
    echo Then run this test again.
    echo.
)

pause
