"""
Voice Routes
Handles voice-based interactions: speech-to-text, text-to-speech, voice chat
"""
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse, Response
from pydantic import BaseModel
from typing import Optional
import logging
import io

from app.database import chats, companions, users
from app.models.chat_model import ChatMessage
from app.services.ai_service_enhanced import enhanced_ai_service
from app.services.tts_service import tts_service
from bson import ObjectId
from datetime import datetime

logger = logging.getLogger(__name__)

router = APIRouter()

class VoiceChatRequest(BaseModel):
    """Request model for voice chat"""
    user_id: str
    companion_gender: str
    message: str  # Transcribed text from speech
    voice: Optional[str] = "nova"  # TTS voice to use
    
class VoiceChatResponse(BaseModel):
    """Response model for voice chat"""
    chat_id: str
    user_id: str
    companion_name: str
    user_message: str
    ai_response: str
    audio_base64: str  # Base64 encoded audio
    timestamp: datetime

@router.post("/chat", response_model=VoiceChatResponse)
async def voice_chat(chat_data: VoiceChatRequest):
    """
    Voice chat endpoint - receives transcribed text, generates AI response with TTS
    
    Flow:
    1. Receive user's transcribed speech as text
    2. Generate AI response
    3. Convert AI response to speech (TTS)
    4. Return both text and audio
    """
    try:
        # Verify user exists
        user = users.find_one({"_id": ObjectId(chat_data.user_id)})
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with ID {chat_data.user_id} not found"
            )
        
        # Get companion information
        companion = companions.find_one({"gender": chat_data.companion_gender})
        if not companion:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No {chat_data.companion_gender} companion found"
            )
        
        # Prepare companion context
        companion_context = {
            "backstory": companion.get("backstory", "Friendly AI companion."),
            "personality_traits": companion.get("personality_traits", []),
            "interests": companion.get("interests", []),
            "name": companion.get("name", "AI Companion")
        }
        
        # Get recent chat history for context
        recent_chats = list(chats.find(
            {"user_id": chat_data.user_id, "companion_gender": chat_data.companion_gender}
        ).sort("timestamp", -1).limit(5))
        
        companion_context["chat_history"] = recent_chats
        
        # Generate AI response using enhanced AI service
        ai_response_text = enhanced_ai_service.generate_contextual_response(
            prompt=chat_data.message,
            companion_context=companion_context
        )
        
        # Convert AI response to speech
        if tts_service.is_available():
            audio_base64 = await tts_service.text_to_speech_base64(
                text=ai_response_text,
                voice=chat_data.voice
            )
        else:
            logger.warning("TTS not available, returning empty audio")
            audio_base64 = ""
        
        # Store chat in database
        chat_doc = {
            "user_id": chat_data.user_id,
            "companion_id": str(companion["_id"]),
            "companion_name": companion.get("name", "AI Companion"),
            "companion_gender": chat_data.companion_gender,
            "user_message": chat_data.message,
            "ai_response": ai_response_text,
            "timestamp": datetime.utcnow(),
            "interaction_type": "voice",
            "metadata": {
                "voice_used": chat_data.voice
            }
        }
        
        result = chats.insert_one(chat_doc)
        
        logger.info(f"Voice chat completed: User {chat_data.user_id} -> {companion.get('name')}")
        
        return VoiceChatResponse(
            chat_id=str(result.inserted_id),
            user_id=chat_data.user_id,
            companion_name=companion.get("name", "AI Companion"),
            user_message=chat_data.message,
            ai_response=ai_response_text,
            audio_base64=audio_base64,
            timestamp=chat_doc["timestamp"]
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Voice chat error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Voice chat failed: {str(e)}"
        )

@router.post("/tts")
async def text_to_speech_endpoint(
    text: str,
    voice: Optional[str] = "nova",
    speed: Optional[float] = 1.0
):
    """
    Convert text to speech audio
    Returns MP3 audio stream
    """
    try:
        if not tts_service.is_available():
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="TTS service not available. Please configure OpenAI API key."
            )
        
        audio_bytes = await tts_service.text_to_speech(text, voice, speed)
        
        return Response(
            content=audio_bytes,
            media_type="audio/mpeg",
            headers={
                "Content-Disposition": "inline; filename=speech.mp3"
            }
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"TTS endpoint error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"TTS failed: {str(e)}"
        )

@router.get("/check-tts")
async def check_tts_availability():
    """Check if TTS service is available"""
    available = tts_service.is_available()
    return {
        "tts_available": available,
        "provider": "OpenAI TTS" if available else "None",
        "message": "TTS ready" if available else "Please configure OpenAI API key"
    }

@router.get("/voices")
async def list_available_voices():
    """List available TTS voices"""
    voices = [
        {"id": "alloy", "name": "Alloy", "description": "Neutral and balanced"},
        {"id": "echo", "name": "Echo", "description": "Male, clear and articulate"},
        {"id": "fable", "name": "Fable", "description": "British accent, expressive"},
        {"id": "onyx", "name": "Onyx", "description": "Deep male voice"},
        {"id": "nova", "name": "Nova", "description": "Female, warm and friendly"},
        {"id": "shimmer", "name": "Shimmer", "description": "Female, soft and gentle"}
    ]
    
    return {
        "voices": voices,
        "default": "nova",
        "tts_available": tts_service.is_available()
    }
