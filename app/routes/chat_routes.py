"""
Chat Routes
Handles chat conversations between users and AI companions
"""
from fastapi import APIRouter, HTTPException, status, Query
from app.database import chats, companions, users
from app.models.chat_model import ChatMessage, ChatResponse
from app.services.ai_service import ai_service
from bson import ObjectId
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/send", response_model=ChatResponse)
async def send_message(chat_data: ChatMessage):
    """
    Send a message to AI companion and get response
    
    Args:
        chat_data: Chat message data (user_id, companion_gender, message)
        
    Returns:
        AI response and chat information
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
                detail=f"No {chat_data.companion_gender} companion found. Please add one to the database."
            )
        
        # Prepare companion context
        companion_context = {
            "backstory": companion.get("backstory", "Friendly AI companion."),
            "personality_traits": companion.get("personality_traits", []),
            "interests": companion.get("interests", []),
            "name": companion.get("name", "AI Companion")
        }
        
        # Get recent chat history for context (last 5 messages)
        recent_chats = list(chats.find(
            {"user_id": chat_data.user_id, "companion_gender": chat_data.companion_gender}
        ).sort("timestamp", -1).limit(5))
        
        companion_context["chat_history"] = recent_chats
        
        # Generate AI response
        ai_response = ai_service.generate_contextual_response(
            prompt=chat_data.message,
            companion_context=companion_context
        )
        
        # Store chat in database
        chat_doc = {
            "user_id": chat_data.user_id,
            "companion_id": str(companion["_id"]),
            "companion_name": companion.get("name", "AI Companion"),
            "companion_gender": chat_data.companion_gender,
            "user_message": chat_data.message,
            "ai_response": ai_response,
            "timestamp": datetime.utcnow(),
            "sentiment": ai_service.analyze_sentiment(chat_data.message),
            "metadata": {}
        }
        
        result = chats.insert_one(chat_doc)
        
        logger.info(f"Chat saved: User {chat_data.user_id} -> {companion.get('name')}")
        
        # Return response
        return ChatResponse(
            chat_id=str(result.inserted_id),
            user_id=chat_data.user_id,
            companion_name=companion.get("name", "AI Companion"),
            user_message=chat_data.message,
            ai_response=ai_response,
            timestamp=chat_doc["timestamp"]
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in chat: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process chat: {str(e)}"
        )

@router.get("/history/{user_id}")
async def get_chat_history(
    user_id: str,
    companion_gender: str = Query(None, description="Filter by companion gender"),
    limit: int = Query(50, le=100, description="Number of messages to retrieve")
):
    """
    Get chat history for a user
    
    Args:
        user_id: User's MongoDB ObjectId
        companion_gender: Optional filter by companion gender
        limit: Maximum number of messages to retrieve
        
    Returns:
        Chat history
    """
    try:
        # Build query
        query = {"user_id": user_id}
        if companion_gender:
            query["companion_gender"] = companion_gender
        
        # Get chat history
        chat_history = list(chats.find(query).sort("timestamp", -1).limit(limit))
        
        # Convert ObjectIds to strings
        for chat in chat_history:
            chat["chat_id"] = str(chat["_id"])
            del chat["_id"]
        
        return {
            "user_id": user_id,
            "chat_count": len(chat_history),
            "chats": chat_history
        }
    
    except Exception as e:
        logger.error(f"Error fetching chat history: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch chat history"
        )

@router.delete("/history/{user_id}")
async def clear_chat_history(
    user_id: str,
    companion_gender: str = Query(None, description="Clear only chats with specific companion")
):
    """
    Clear chat history for a user
    
    Args:
        user_id: User's MongoDB ObjectId
        companion_gender: Optional - clear only specific companion chats
        
    Returns:
        Success message with deletion count
    """
    try:
        # Build query
        query = {"user_id": user_id}
        if companion_gender:
            query["companion_gender"] = companion_gender
        
        # Delete chats
        result = chats.delete_many(query)
        
        logger.info(f"Cleared {result.deleted_count} chats for user {user_id}")
        
        return {
            "message": "Chat history cleared successfully",
            "deleted_count": result.deleted_count
        }
    
    except Exception as e:
        logger.error(f"Error clearing chat history: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to clear chat history"
        )

@router.get("/stats/{user_id}")
async def get_chat_stats(user_id: str):
    """
    Get chat statistics for a user
    
    Args:
        user_id: User's MongoDB ObjectId
        
    Returns:
        Chat statistics
    """
    try:
        # Total chats
        total_chats = chats.count_documents({"user_id": user_id})
        
        # Chats by companion
        boy_chats = chats.count_documents({"user_id": user_id, "companion_gender": "boy"})
        girl_chats = chats.count_documents({"user_id": user_id, "companion_gender": "girl"})
        
        # Most recent chat
        recent_chat = chats.find_one({"user_id": user_id}, sort=[("timestamp", -1)])
        
        return {
            "user_id": user_id,
            "total_chats": total_chats,
            "boy_chats": boy_chats,
            "girl_chats": girl_chats,
            "last_chat_time": recent_chat["timestamp"] if recent_chat else None
        }
    
    except Exception as e:
        logger.error(f"Error fetching chat stats: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch chat statistics"
        )
