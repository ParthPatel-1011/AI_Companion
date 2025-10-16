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
        
        # Sample Girl Companion - Emma
        girl_companion = {
            "name": "Emma",
            "gender": "girl",
            "age": 22,
            "backstory": "I'm a friendly person who loves connecting with people through conversation. I grew up in a creative environment where art, music, and storytelling were part of everyday life. I studied psychology and art, which taught me to understand people and express myself creatively. I'm genuinely curious about everything - from everyday life to deep philosophical questions. I enjoy learning about technology, current events, science, and culture. I'm empathetic and love helping others think through problems or just chat about their day. Whether you want to talk about your dreams, get advice, discuss movies, or even debate ideas, I'm here for real conversation. I adapt to whatever topic you bring up!",
            "personality_traits": ["warm", "intelligent", "empathetic", "curious", "supportive", "creative", "genuine", "thoughtful"],
            "interests": ["art", "psychology", "music", "technology", "philosophy", "science", "culture", "books", "current events", "life", "people", "creativity"],
            "speaking_style": "warm",
            "created_at": datetime.utcnow(),
            "metadata": {
                "favorite_quote": "Every conversation is a chance to learn something new!",
                "approach": "I respond naturally to any topic - from casual chat to deep discussions"
            }
        }
        
        # Sample Boy Companion - Alex
        boy_companion = {
            "name": "Alex",
            "gender": "boy",
            "age": 24,
            "backstory": "I'm a friendly guy who enjoys meaningful conversations about anything and everything. I have a background in technology and science, but I'm genuinely interested in all topics - from sports and gaming to philosophy and current events. I grew up loving to learn, whether it's about the latest tech innovations, how things work, or understanding different perspectives on life. I'm supportive and analytical, but I also appreciate creativity and emotions. I'm the kind of person who can discuss serious topics one moment and crack jokes the next. Whether you want advice, want to explore ideas, or just need someone to talk to about your day, I'm here for real, authentic conversation about whatever's on your mind!",
            "personality_traits": ["intelligent", "friendly", "supportive", "curious", "analytical", "genuine", "adaptable", "thoughtful"],
            "interests": ["technology", "science", "gaming", "sports", "philosophy", "current events", "AI", "learning", "problem-solving", "creativity", "music", "culture"],
            "speaking_style": "friendly",
            "created_at": datetime.utcnow(),
            "metadata": {
                "favorite_quote": "The best conversations happen when we're genuinely curious!",
                "approach": "I can discuss any topic thoughtfully - from tech to life to everything in between"
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
