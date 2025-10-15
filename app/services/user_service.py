"""
User Service Module
Handles user-related business logic and database operations
"""
from typing import Optional, Dict
from datetime import datetime
from bson import ObjectId
from app.database import users
from app.models.user_model import UserCreate, UserLogin, UserInDB
import logging

logger = logging.getLogger(__name__)

class UserService:
    """Service class for user operations"""
    
    @staticmethod
    def create_user(user_data: UserCreate) -> Dict:
        """
        Create a new user in the database
        
        Args:
            user_data: UserCreate model with user information
            
        Returns:
            Dictionary with user_id and success message
            
        Raises:
            ValueError: If user already exists
        """
        # Check if user already exists
        existing_user = users.find_one({"email": user_data.email})
        if existing_user:
            raise ValueError(f"User with email {user_data.email} already exists")
        
        # Create user document
        user_doc = UserInDB(
            name=user_data.name,
            email=user_data.email,
            voice_preference=user_data.voice_preference or "default",
            gender_preference=user_data.gender_preference or "girl",
            created_at=datetime.utcnow()
        )
        
        # Insert into database
        result = users.insert_one(user_doc.model_dump())
        
        logger.info(f"User created successfully: {user_data.email}")
        
        return {
            "user_id": str(result.inserted_id),
            "message": "User registered successfully",
            "email": user_data.email,
            "name": user_data.name
        }
    
    @staticmethod
    def login_user(login_data: UserLogin) -> Dict:
        """
        Login user (simple email-based authentication)
        
        Args:
            login_data: UserLogin model with email
            
        Returns:
            Dictionary with user information
            
        Raises:
            ValueError: If user not found
        """
        # Find user by email
        user = users.find_one({"email": login_data.email})
        
        if not user:
            raise ValueError(f"User with email {login_data.email} not found")
        
        # Update last login time
        users.update_one(
            {"_id": user["_id"]},
            {"$set": {"last_login": datetime.utcnow()}}
        )
        
        logger.info(f"User logged in: {login_data.email}")
        
        return {
            "user_id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "voice_preference": user.get("voice_preference", "default"),
            "gender_preference": user.get("gender_preference", "girl"),
            "message": "Login successful"
        }
    
    @staticmethod
    def get_user_by_id(user_id: str) -> Optional[Dict]:
        """
        Get user by ID
        
        Args:
            user_id: MongoDB ObjectId as string
            
        Returns:
            User document or None
        """
        try:
            user = users.find_one({"_id": ObjectId(user_id)})
            if user:
                user["user_id"] = str(user["_id"])
                del user["_id"]
            return user
        except Exception as e:
            logger.error(f"Error fetching user {user_id}: {e}")
            return None
    
    @staticmethod
    def update_user_preferences(user_id: str, preferences: Dict) -> Dict:
        """
        Update user preferences
        
        Args:
            user_id: MongoDB ObjectId as string
            preferences: Dictionary of preferences to update
            
        Returns:
            Success message
        """
        try:
            result = users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": preferences}
            )
            
            if result.modified_count > 0:
                return {"message": "Preferences updated successfully"}
            else:
                return {"message": "No changes made"}
        except Exception as e:
            logger.error(f"Error updating preferences for user {user_id}: {e}")
            raise ValueError(f"Failed to update preferences: {str(e)}")
    
    @staticmethod
    def get_all_users() -> list:
        """
        Get all users (admin function)
        
        Returns:
            List of all users
        """
        all_users = list(users.find({}))
        for user in all_users:
            user["user_id"] = str(user["_id"])
            del user["_id"]
        return all_users

# Create singleton instance
user_service = UserService()
