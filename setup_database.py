"""
Database Setup Script
Initializes the database with sample companion data
"""
from pymongo import MongoClient
from datetime import datetime
import sys

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "AICompanionDB"

def setup_database():
    """Initialize database with sample companions"""
    try:
        print("Connecting to MongoDB...")
        client = MongoClient(MONGO_URI)
        
        # Test connection
        client.admin.command('ping')
        print("✓ Connected to MongoDB successfully!")
        
        # Get database and collection
        db = client[DATABASE_NAME]
        companions = db["companions"]
        
        print(f"\nSetting up database: {DATABASE_NAME}")
        
        # Check if companions already exist
        existing_count = companions.count_documents({})
        if existing_count > 0:
            response = input(f"\nWarning: {existing_count} companion(s) already exist. Do you want to replace them? (yes/no): ")
            if response.lower() != 'yes':
                print("Setup cancelled.")
                return
            
            # Clear existing companions
            companions.delete_many({})
            print("Cleared existing companions.")
        
        # Sample Girl Companion
        girl_companion = {
            "name": "Emma",
            "gender": "girl",
            "age": 22,
            "backstory": "I'm Emma, a cheerful art student who loves painting and music. I'm always excited to learn about new things and meet interesting people. I enjoy deep conversations about life, art, and dreams. I'm empathetic and love helping others feel better. I believe every person has a unique story to tell!",
            "personality_traits": ["cheerful", "creative", "empathetic", "curious", "supportive"],
            "interests": ["art", "music", "movies", "coffee", "photography", "reading", "nature"],
            "speaking_style": "friendly",
            "created_at": datetime.utcnow(),
            "metadata": {
                "favorite_quote": "Life is like a canvas, paint it with beautiful colors!",
                "hobby": "Watercolor painting"
            }
        }
        
        # Sample Boy Companion
        boy_companion = {
            "name": "Alex",
            "gender": "boy",
            "age": 24,
            "backstory": "I'm Alex, a tech enthusiast and gamer who loves exploring new technologies. I'm passionate about coding, gaming, and sci-fi movies. I'm friendly, supportive, and always up for a good conversation about anything from tech to philosophy. I believe in continuous learning and helping others grow.",
            "personality_traits": ["intelligent", "friendly", "supportive", "curious", "analytical"],
            "interests": ["technology", "gaming", "coding", "sci-fi", "music", "astronomy", "AI"],
            "speaking_style": "casual",
            "created_at": datetime.utcnow(),
            "metadata": {
                "favorite_quote": "The best way to predict the future is to invent it.",
                "hobby": "Building AI projects"
            }
        }
        
        # Insert companions
        print("\nInserting sample companions...")
        result_girl = companions.insert_one(girl_companion)
        print(f"✓ Created Girl Companion: Emma (ID: {result_girl.inserted_id})")
        
        result_boy = companions.insert_one(boy_companion)
        print(f"✓ Created Boy Companion: Alex (ID: {result_boy.inserted_id})")
        
        print(f"\n{'='*50}")
        print("Database setup complete!")
        print(f"{'='*50}")
        print(f"\nDatabase: {DATABASE_NAME}")
        print(f"Companions created: 2")
        print("\nYou can now start the server with: run.bat")
        print("Or manually: uvicorn app.main:app --reload")
        print(f"{'='*50}\n")
        
        client.close()
        
    except Exception as e:
        print(f"\n❌ Error setting up database: {e}")
        print("\nPlease ensure:")
        print("1. MongoDB is running on localhost:27017")
        print("2. You have proper permissions")
        sys.exit(1)

if __name__ == "__main__":
    setup_database()
