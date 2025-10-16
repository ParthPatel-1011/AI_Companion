"""
Text-to-Speech Service
Converts text to natural human-like speech using ElevenLabs API
Supports gender-specific voices: female voices for female companions, male voices for male companions
"""
import logging
import io
import base64
from typing import Optional
from fastapi import HTTPException

logger = logging.getLogger(__name__)

try:
    from app.config import settings
    from elevenlabs.client import ElevenLabs
    from elevenlabs import VoiceSettings
    ELEVENLABS_AVAILABLE = True
except ImportError:
    ELEVENLABS_AVAILABLE = False
    logger.warning("ElevenLabs not available for TTS")
    settings = None
    ElevenLabs = None
    VoiceSettings = None

# Legacy TTS imports (now commented out - replaced by ElevenLabs)
# try:
#     from openai import OpenAI
#     OPENAI_TTS_AVAILABLE = True
# except ImportError:
#     OPENAI_TTS_AVAILABLE = False
#     logger.warning("OpenAI not available for TTS")
#     OpenAI = None

# gTTS fallback (now commented out - replaced by ElevenLabs)
# try:
#     from gtts import gTTS
#     GTTS_AVAILABLE = True
# except ImportError:
#     GTTS_AVAILABLE = False
#     gTTS = None
#     logger.warning("gTTS not available")

class TTSService:
    """Text-to-Speech Service using ElevenLabs API"""
    
    def __init__(self):
        self.client = None
        if ELEVENLABS_AVAILABLE and (settings is not None):
            self._initialize()
    
    def _initialize(self):
        """Initialize ElevenLabs TTS client"""
        try:
            if settings is not None and ElevenLabs is not None and settings.use_elevenlabs_tts and settings.elevenlabs_api_key:
                if not settings.elevenlabs_api_key.startswith("your"):
                    self.client = ElevenLabs(api_key=settings.elevenlabs_api_key)
                    logger.info("ElevenLabs TTS initialized successfully")
                else:
                    logger.warning("No valid ElevenLabs API key for TTS")
        except Exception as e:
            logger.error(f"Failed to initialize ElevenLabs TTS: {e}")
    
    async def text_to_speech(
        self,
        text: str,
        voice: Optional[str] = None,
        speed: Optional[float] = None,
        gender: Optional[str] = None
    ) -> bytes:
        """
        Convert text to speech audio using ElevenLabs
        
        Args:
            text: Text to convert to speech
            voice: Voice ID to use (optional, will use gender-based default)
            speed: Speaking speed (0.25 to 4.0) - Note: ElevenLabs uses stability/similarity settings
            gender: Companion gender ('boy' or 'girl') to select appropriate voice
            
        Returns:
            Audio data as bytes (MP3 format)
        """
        if not self.client:
            raise HTTPException(
                status_code=503,
                detail="ElevenLabs TTS service not available. Please configure ELEVENLABS_API_KEY in .env"
            )
        
        try:
            # Select voice based on gender
            if voice:
                voice_id = voice
            elif gender:
                # Use female voice for 'girl' companion, male voice for 'boy' companion
                if gender.lower() in ['girl', 'female']:
                    voice_id = settings.elevenlabs_female_voice_id
                    logger.info(f"Using female voice for {gender} companion")
                elif gender.lower() in ['boy', 'male']:
                    voice_id = settings.elevenlabs_male_voice_id
                    logger.info(f"Using male voice for {gender} companion")
                else:
                    voice_id = settings.elevenlabs_female_voice_id  # Default to female
                    logger.warning(f"Unknown gender '{gender}', defaulting to female voice")
            else:
                # Default to female voice if no gender specified
                voice_id = settings.elevenlabs_female_voice_id
                logger.info("No gender specified, using default female voice")
            
            # Generate audio using ElevenLabs
            # VoiceSettings optimized for friendly, warm, human-like speech
            # - stability: Higher for consistent, reliable voice (0.6 = warm and friendly)
            # - similarity_boost: Higher to maintain voice character (0.8 = natural)
            # - style: Slight exaggeration for more expressive, friendly tone (0.3)
            # - use_speaker_boost: Enhances clarity and warmth
            voice_settings = None
            if VoiceSettings is not None:
                voice_settings = VoiceSettings(
                    stability=0.6,           # Warm, consistent tone
                    similarity_boost=0.8,     # Natural voice character
                    style=0.3,               # Friendly, expressive
                    use_speaker_boost=True    # Enhanced clarity
                )
            
            # Generate speech
            audio_stream = self.client.text_to_speech.convert(
                voice_id=voice_id,
                text=text,
                model_id="eleven_multilingual_v2",  # High quality model
                voice_settings=voice_settings
            )
            
            # Collect audio bytes from stream
            audio_bytes = b"".join(audio_stream)
            
            logger.info(f"Generated ElevenLabs TTS audio: {len(text)} chars -> {len(audio_bytes)} bytes (voice: {voice_id})")
            return audio_bytes
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f"ElevenLabs TTS generation failed: {error_msg}")
            
            # Check if it's an API key issue
            if '401' in error_msg or 'unusual_activity' in error_msg or 'unauthorized' in error_msg.lower():
                logger.warning("ElevenLabs API key issue detected. TTS will be disabled for this request.")
                logger.warning("To fix: Get your own free API key from https://elevenlabs.io/")
                # Return empty bytes instead of raising error - allows app to continue without TTS
                return b""
            
            # For other errors, also return empty bytes to prevent app from crashing
            logger.warning(f"TTS unavailable for this request. App will continue without voice output.")
            return b""
    
    # Legacy methods commented out - replaced by ElevenLabs
    # async def text_to_speech_gtts(self, text: str) -> bytes:
    #     """Legacy gTTS method - now replaced by ElevenLabs"""
    #     buf = io.BytesIO()
    #     tts = gTTS(text=text, lang='en')
    #     tts.write_to_fp(buf)
    #     return buf.getvalue()
    # 
    # async def text_to_speech_openai(self, text: str, voice: str) -> bytes:
    #     """Legacy OpenAI TTS method - now replaced by ElevenLabs"""
    #     response = self.client.audio.speech.create(
    #         model="tts-1",
    #         voice=voice,
    #         input=text
    #     )
    #     return response.content
    
    async def text_to_speech_base64(
        self,
        text: str,
        voice: Optional[str] = None,
        speed: Optional[float] = None,
        gender: Optional[str] = None
    ) -> str:
        """
        Convert text to speech and return as base64 encoded string
        Useful for direct browser playback
        
        Args:
            text: Text to convert to speech
            voice: Voice ID to use (optional)
            speed: Speaking speed (optional)
            gender: Companion gender to select appropriate voice
        """
        audio_bytes = await self.text_to_speech(text, voice, speed, gender)
        return base64.b64encode(audio_bytes).decode('utf-8')
    
    def is_available(self) -> bool:
        """Check if ElevenLabs TTS service is available"""
        return self.client is not None

# Create singleton instance
tts_service = TTSService()
