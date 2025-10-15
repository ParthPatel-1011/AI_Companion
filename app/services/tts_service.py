"""
Text-to-Speech Service
Converts text to natural human-like speech using OpenAI TTS API
"""
import logging
import io
import base64
from typing import Optional
from fastapi import HTTPException

logger = logging.getLogger(__name__)

try:
    from app.config import settings
    from openai import OpenAI
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    logger.warning("OpenAI not available for TTS")
    settings = None
    OpenAI = None

# Try to import gTTS for fallback
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    gTTS = None
    logger.warning("gTTS not available")

class TTSService:
    """Text-to-Speech Service"""
    
    def __init__(self):
        self.client = None
        # Temporarily prefer gTTS if available
        self.use_gtts = ('GTTS_AVAILABLE' in globals() and GTTS_AVAILABLE)
        if TTS_AVAILABLE and (settings is not None):
            self._initialize()
    
    def _initialize(self):
        """Initialize OpenAI TTS client"""
        try:
            if settings is not None and OpenAI is not None and settings.use_openai_tts and settings.openai_api_key:
                if not settings.openai_api_key.startswith("your"):
                    self.client = OpenAI(api_key=settings.openai_api_key)
                    logger.info("OpenAI TTS initialized successfully")
                else:
                    logger.warning("No valid OpenAI API key for TTS")
        except Exception as e:
            logger.error(f"Failed to initialize TTS: {e}")
    
    async def text_to_speech(
        self,
        text: str,
        voice: Optional[str] = None,
        speed: Optional[float] = None
    ) -> bytes:
        """
        Convert text to speech audio
        
        Args:
            text: Text to convert to speech
            voice: Voice to use (alloy, echo, fable, onyx, nova, shimmer)
            speed: Speaking speed (0.25 to 4.0)
            
        Returns:
            Audio data as bytes (MP3 format)
        """
        # Prefer gTTS when enabled
        if self.use_gtts and 'GTTS_AVAILABLE' in globals() and GTTS_AVAILABLE and (gTTS is not None):
            try:
                buf = io.BytesIO()
                tts = gTTS(text=text, lang='en')
                tts.write_to_fp(buf)
                audio_bytes = buf.getvalue()
                logger.info(f"Generated gTTS audio: {len(text)} chars -> {len(audio_bytes)} bytes")
                return audio_bytes
            except Exception as e:
                logger.error(f"gTTS generation failed: {e}")
                # Fall through to OpenAI if available
        
        # Fallback to OpenAI TTS if configured and available
        if self.client and getattr(settings, 'use_openai_tts', True):
            try:
                voice_name = voice or (settings.openai_tts_voice if settings is not None else "nova")
                speed_value = speed or (settings.default_voice_speed if settings is not None else 1.0)
                response = self.client.audio.speech.create(
                    model=(settings.openai_tts_model if settings is not None else "tts-1"),
                    voice=voice_name,
                    input=text,
                    speed=speed_value
                )
                audio_bytes = response.content
                logger.info(f"Generated OpenAI TTS audio: {len(text)} chars -> {len(audio_bytes)} bytes")
                return audio_bytes
            except Exception as e:
                logger.error(f"OpenAI TTS generation failed: {e}")
                raise HTTPException(
                    status_code=500,
                    detail=f"TTS generation failed: {str(e)}"
                )
        
        # No TTS provider available
        raise HTTPException(
            status_code=503,
            detail="TTS service not available. Configure OpenAI API key or install gTTS."
        )
    
    async def text_to_speech_base64(
        self,
        text: str,
        voice: Optional[str] = None,
        speed: Optional[float] = None
    ) -> str:
        """
        Convert text to speech and return as base64 encoded string
        Useful for direct browser playback
        """
        audio_bytes = await self.text_to_speech(text, voice, speed)
        return base64.b64encode(audio_bytes).decode('utf-8')
    
    def is_available(self) -> bool:
        """Check if TTS service is available"""
        return (self.client is not None) or ('GTTS_AVAILABLE' in globals() and GTTS_AVAILABLE)

# Create singleton instance
tts_service = TTSService()
