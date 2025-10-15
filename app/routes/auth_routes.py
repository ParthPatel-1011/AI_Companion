"""
Authentication Routes
Handles user registration and login
"""
from fastapi import APIRouter, HTTPException, status
from app.models.user_model import UserCreate, UserLogin
from app.services.user_service import user_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreate):
    """
    Register a new user
    
    Args:
        user_data: User registration information
        
    Returns:
        User ID and success message
    """
    try:
        result = user_service.create_user(user_data)
        return result
    except ValueError as e:
        logger.warning(f"Signup failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Signup error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during signup"
        )

@router.post("/login")
async def login(login_data: UserLogin):
    """
    Login user with email
    
    Args:
        login_data: User login credentials (email)
        
    Returns:
        User information and session data
    """
    try:
        result = user_service.login_user(login_data)
        return result
    except ValueError as e:
        logger.warning(f"Login failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during login"
        )

@router.get("/user/{user_id}")
async def get_user(user_id: str):
    """
    Get user information by ID
    
    Args:
        user_id: User's MongoDB ObjectId
        
    Returns:
        User information
    """
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return user

@router.get("/users")
async def get_all_users():
    """
    Get all users (admin endpoint)
    
    Returns:
        List of all users
    """
    try:
        users = user_service.get_all_users()
        return {"users": users, "count": len(users)}
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch users"
        )
