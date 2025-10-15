"""
MongoDB Database Connection Module
Handles all database connections and collection references
"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "AICompanionDB"

# Initialize MongoDB Client
try:
    client = MongoClient(MONGO_URI)
    # Test connection
    client.admin.command('ping')
    logger.info("Successfully connected to MongoDB!")
except ConnectionFailure as e:
    logger.error(f"Failed to connect to MongoDB: {e}")
    raise

# Get database instance
db = client[DATABASE_NAME]

# Collection references
users = db["users"]
companions = db["companions"]
chats = db["chats"]

# Create indexes for better performance
def create_indexes():
    """Create database indexes for optimized queries"""
    try:
        # User indexes
        users.create_index("email", unique=True)
        
        # Companion indexes
        companions.create_index("gender")
        
        # Chat indexes
        chats.create_index([("user_id", 1), ("timestamp", -1)])
        
        logger.info("Database indexes created successfully!")
    except Exception as e:
        logger.warning(f"Index creation warning: {e}")

# Initialize indexes on module import
create_indexes()

def get_database():
    """Return database instance"""
    return db

def close_connection():
    """Close MongoDB connection"""
    client.close()
    logger.info("MongoDB connection closed")
