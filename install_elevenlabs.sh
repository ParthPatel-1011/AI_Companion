#!/bin/bash

echo "========================================"
echo "Installing ElevenLabs for AI Companion"
echo "========================================"
echo

# Activate virtual environment
if [ -f venv/bin/activate ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "Virtual environment not found!"
    echo "Please run setup.sh first."
    exit 1
fi

echo
echo "Installing ElevenLabs package..."
python -m pip install elevenlabs>=1.0.0

echo
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo
echo "Next Steps:"
echo "1. Add your ElevenLabs API key to .env file"
echo "2. Restart the server"
echo "3. Test with: python -c 'import elevenlabs; print(\"ElevenLabs installed!\")'"
echo
echo "See ELEVENLABS_SETUP.md for detailed instructions"
echo
