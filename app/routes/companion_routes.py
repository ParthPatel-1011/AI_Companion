"""
Companion Routes
Handles AI companion information and backstories
"""
from fastapi import APIRouter, HTTPException, status
from app.database import companions
from app.models.companion_model import CompanionCreate, CompanionResponse
from bson import ObjectId
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/get_story/{gender}")
async def get_companion_story(gender: str):
    """
    Get companion backstory by gender
    
    Args:
        gender: 'boy' or 'girl'
        
    Returns:
        Companion information including backstory
    """
    if gender not in ["boy", "girl"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Gender must be 'boy' or 'girl'"
        )
    
    companion = companions.find_one({"gender": gender})
    
    if not companion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No {gender} companion found. Please add one to the database."
        )
    
    # Convert ObjectId to string
    companion["companion_id"] = str(companion["_id"])
    del companion["_id"]
    
    return companion

@router.get("/all")
async def get_all_companions():
    """
    Get all companions
    
    Returns:
        List of all companions
    """
    all_companions = list(companions.find({}))
    
    for companion in all_companions:
        companion["companion_id"] = str(companion["_id"])
        del companion["_id"]
    
    return {"companions": all_companions, "count": len(all_companions)}

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_companion(companion_data: CompanionCreate):
    """
    Create a new companion (admin endpoint)
    
    Args:
        companion_data: Companion information
        
    Returns:
        Created companion ID
    """
    try:
        # Check if companion with this gender already exists
        existing = companions.find_one({"gender": companion_data.gender})
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"A {companion_data.gender} companion already exists. Update or delete it first."
            )
        
        # Insert companion
        result = companions.insert_one(companion_data.model_dump())
        
        logger.info(f"Companion created: {companion_data.name} ({companion_data.gender})")
        
        return {
            "companion_id": str(result.inserted_id),
            "message": "Companion created successfully",
            "name": companion_data.name
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating companion: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create companion"
        )

@router.get("/{companion_id}")
async def get_companion_by_id(companion_id: str):
    """
    Get companion by ID
    
    Args:
        companion_id: Companion's MongoDB ObjectId
        
    Returns:
        Companion information
    """
    try:
        companion = companions.find_one({"_id": ObjectId(companion_id)})
        
        if not companion:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Companion with ID {companion_id} not found"
            )
        
        companion["companion_id"] = str(companion["_id"])
        del companion["_id"]
        
        return companion
    except Exception as e:
        logger.error(f"Error fetching companion: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch companion"
        )

@router.delete("/{companion_id}")
async def delete_companion(companion_id: str):
    """
    Delete a companion (admin endpoint)
    
    Args:
        companion_id: Companion's MongoDB ObjectId
        
    Returns:
        Success message
    """
    try:
        result = companions.delete_one({"_id": ObjectId(companion_id)})
        
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Companion with ID {companion_id} not found"
            )
        
        logger.info(f"Companion deleted: {companion_id}")
        
        return {"message": "Companion deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting companion: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete companion"
        )
