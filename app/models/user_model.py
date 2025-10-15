"""
User Model - Data structure for user information
"""
from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    """Model for user registration"""
    name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    voice_preference: Optional[str] = "default"
    gender_preference: Optional[str] = "girl"  # Preferred companion gender
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "voice_preference": "female_1",
                "gender_preference": "girl"
            }
        }

class UserLogin(BaseModel):
    """Model for user login"""
    email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "john@example.com"
            }
        }

class UserResponse(BaseModel):
    """Model for user data response"""
    user_id: str
    name: str
    email: str
    voice_preference: str
    gender_preference: str
    created_at: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "507f1f77bcf86cd799439011",
                "name": "John Doe",
                "email": "john@example.com",
                "voice_preference": "female_1",
                "gender_preference": "girl",
                "created_at": "2025-10-15T12:00:00"
            }
        }

class UserInDB(BaseModel):
    """Complete user model stored in database"""
    name: str
    email: str
    voice_preference: str = "default"
    gender_preference: str = "girl"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = None
