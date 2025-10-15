"""
Chat Model - Data structure for chat conversations
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

class ChatMessage(BaseModel):
    """Model for sending a chat message"""
    user_id: str = Field(..., min_length=1)
    companion_gender: str = Field(..., pattern="^(boy|girl)$")
    message: str = Field(..., min_length=1, max_length=1000)
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "507f1f77bcf86cd799439011",
                "companion_gender": "girl",
                "message": "Hey! How are you doing today?"
            }
        }

class ChatResponse(BaseModel):
    """Model for chat response"""
    chat_id: str
    user_id: str
    companion_name: str
    user_message: str
    ai_response: str
    timestamp: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "chat_id": "507f1f77bcf86cd799439013",
                "user_id": "507f1f77bcf86cd799439011",
                "companion_name": "Emma",
                "user_message": "Hey! How are you doing?",
                "ai_response": "Hi! I'm doing great, thanks for asking!",
                "timestamp": "2025-10-15T12:00:00"
            }
        }

class ChatInDB(BaseModel):
    """Complete chat model stored in database"""
    user_id: str
    companion_id: str
    companion_name: str
    companion_gender: str
    user_message: str
    ai_response: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    sentiment: Optional[str] = None
    metadata: Optional[Dict] = Field(default_factory=dict)

class ChatHistory(BaseModel):
    """Model for retrieving chat history"""
    user_id: str
    companion_gender: Optional[str] = None
    limit: int = Field(default=50, le=100)
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "507f1f77bcf86cd799439011",
                "companion_gender": "girl",
                "limit": 50
            }
        }
