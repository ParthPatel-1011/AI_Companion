"""
Companion Model - Data structure for AI companion personalities
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class CompanionCreate(BaseModel):
    """Model for creating a new companion"""
    name: str = Field(..., min_length=1, max_length=50)
    gender: str = Field(..., pattern="^(boy|girl)$")
    age: int = Field(..., ge=18, le=30)
    backstory: str = Field(..., min_length=50)
    personality_traits: List[str] = Field(default_factory=list)
    interests: List[str] = Field(default_factory=list)
    speaking_style: Optional[str] = "friendly"
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Emma",
                "gender": "girl",
                "age": 22,
                "backstory": "I'm Emma, a cheerful art student who loves painting and music...",
                "personality_traits": ["cheerful", "creative", "empathetic"],
                "interests": ["art", "music", "movies", "coffee"],
                "speaking_style": "friendly"
            }
        }

class CompanionResponse(BaseModel):
    """Model for companion data response"""
    companion_id: str
    name: str
    gender: str
    age: int
    backstory: str
    personality_traits: List[str]
    interests: List[str]
    speaking_style: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "companion_id": "507f1f77bcf86cd799439012",
                "name": "Emma",
                "gender": "girl",
                "age": 22,
                "backstory": "I'm Emma, a cheerful art student...",
                "personality_traits": ["cheerful", "creative"],
                "interests": ["art", "music"],
                "speaking_style": "friendly"
            }
        }

class CompanionInDB(BaseModel):
    """Complete companion model stored in database"""
    name: str
    gender: str
    age: int
    backstory: str
    personality_traits: List[str] = Field(default_factory=list)
    interests: List[str] = Field(default_factory=list)
    speaking_style: str = "friendly"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    metadata: Optional[Dict] = Field(default_factory=dict)
