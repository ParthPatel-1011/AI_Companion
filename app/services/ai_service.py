"""
AI Service Module
Handles AI response generation and conversation logic
This uses mock responses but can be easily replaced with OpenAI API or other LLMs
"""
import random
import re
from typing import List, Dict, Optional
from datetime import datetime

class AIService:
    """AI Response Generation Service"""
    
    def __init__(self):
        # Different response styles based on companion personality
        self.responses = {
            "greeting": [
                "Hey there! How are you doing today?",
                "Hi! It's so good to hear from you!",
                "Hello! I was just thinking about you!",
                "Hey! What's up? 😊",
            ],
            "happy": [
                "That sounds amazing! I'm so happy for you!",
                "Wow, that's awesome! Tell me more!",
                "That's so cool! I love hearing about this!",
                "Haha, that's great! You made my day!",
            ],
            "empathetic": [
                "I understand how you feel. I'm here for you.",
                "That must be tough. Want to talk about it?",
                "I'm sorry you're going through this. How can I help?",
                "You're not alone. I'm always here to listen.",
            ],
            "curious": [
                "That sounds interesting! Tell me more about it.",
                "Wow, I didn't know that! What happened next?",
                "Really? That's fascinating! How did you feel?",
                "I'm intrigued! Can you explain more?",
            ],
            "default": [
                "I totally get what you mean!",
                "That's really interesting!",
                "I was thinking the same thing!",
                "Tell me more about that!",
                "I'd love to hear more!",
            ]
        }
    
    def analyze_sentiment(self, message: str) -> str:
        """Analyze message sentiment (basic keyword matching)"""
        message_lower = message.lower()
        
        # Greeting patterns
        if any(word in message_lower for word in ["hi", "hello", "hey", "sup", "morning", "evening"]):
            return "greeting"
        
        # Happy patterns
        if any(word in message_lower for word in ["happy", "great", "awesome", "excited", "love", "amazing", "wonderful"]):
            return "happy"
        
        # Sad/empathetic patterns
        if any(word in message_lower for word in ["sad", "upset", "angry", "frustrated", "tired", "worried", "stressed"]):
            return "empathetic"
        
        # Question patterns
        if "?" in message or any(word in message_lower for word in ["what", "why", "how", "when", "where", "who"]):
            return "curious"
        
        return "default"
    
    def generate_ai_response(
        self, 
        user_message: str, 
        backstory: str = "",
        personality_traits: Optional[List[str]] = None,
        chat_history: Optional[List[Dict]] = None
    ) -> str:
        """
        Generate AI response based on user message and companion context
        
        Args:
            user_message: The user's message
            backstory: Companion's backstory
            personality_traits: List of personality traits
            chat_history: Recent chat history for context
            
        Returns:
            AI-generated response string
        """
        # Analyze sentiment
        sentiment = self.analyze_sentiment(user_message)
        
        # Get appropriate response category
        response_pool = self.responses.get(sentiment, self.responses["default"])
        
        # Select a random response from the pool
        base_response = random.choice(response_pool)
        
        # Add personality flavor if traits are provided
        if personality_traits and random.random() > 0.5:
            base_response = self._add_personality_flavor(base_response, personality_traits)
        
        return base_response
    
    def _add_personality_flavor(self, response: str, traits: List[str]) -> str:
        """Add personality-based modifications to response"""
        # Cheerful trait - add more emojis
        if "cheerful" in traits or "happy" in traits:
            if random.random() > 0.6:
                response += " 😊"
        
        # Creative trait - add more descriptive language
        if "creative" in traits:
            creative_additions = [
                " It's like opening a new chapter!",
                " That paints such a vivid picture!",
                " I can almost feel the energy!",
            ]
            if random.random() > 0.7:
                response += random.choice(creative_additions)
        
        # Empathetic trait - add supportive language
        if "empathetic" in traits or "caring" in traits:
            supportive_additions = [
                " I really care about what you're going through.",
                " Your feelings are totally valid.",
                " I'm here for you, always.",
            ]
            if random.random() > 0.7:
                response += random.choice(supportive_additions)
        
        return response
    
    def generate_contextual_response(
        self, 
        prompt: str,
        companion_context: Dict
    ) -> str:
        """
        Generate response with full companion context
        This method can be replaced with OpenAI API call
        
        Example:
            import openai
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": companion_context["backstory"]},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        """
        # For now, use the mock response generator
        return self.generate_ai_response(
            user_message=prompt,
            backstory=companion_context.get("backstory", ""),
            personality_traits=companion_context.get("personality_traits", []),
            chat_history=companion_context.get("chat_history", [])
        )

# Create singleton instance
ai_service = AIService()

# Convenience function for backward compatibility
def generate_ai_response(prompt: str, backstory: str = "") -> str:
    """Simple function for generating AI responses"""
    return ai_service.generate_ai_response(prompt, backstory)
