"""
Enhanced AI Service with Real LLM Integration
Supports OpenAI, Groq, and Anthropic APIs for human-like conversations
"""
import random
import logging
from typing import List, Dict, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

# Try to import LLM libraries
try:
    from app.config import settings
    from openai import OpenAI
    from groq import Groq
    import anthropic
    LLM_AVAILABLE = True
except ImportError as e:
    logger.warning(f"LLM libraries not fully available: {e}. Using mock responses.")
    LLM_AVAILABLE = False
    settings = None

class EnhancedAIService:
    """AI Service with real LLM integration"""
    
    def __init__(self):
        self.llm_client = None
        self.provider = None
        
        if LLM_AVAILABLE and settings:
            self._initialize_llm()
        
        # Fallback mock responses
        self.mock_responses = {
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
    
    def _initialize_llm(self):
        """Initialize the LLM client based on configuration"""
        try:
            llm_config = settings.get_llm_config()
            self.provider = llm_config["provider"]
            api_key = llm_config["api_key"]
            
            if not api_key or api_key.startswith("your"):
                logger.warning(f"No valid API key for {self.provider}. Using mock responses.")
                return
            
            if self.provider == "openai":
                self.llm_client = OpenAI(api_key=api_key)
                self.model = llm_config["model"]
                logger.info(f"Initialized OpenAI client with model: {self.model}")
            
            elif self.provider == "groq":
                self.llm_client = Groq(api_key=api_key)
                self.model = llm_config["model"]
                logger.info(f"Initialized Groq client with model: {self.model}")
            
            elif self.provider == "anthropic":
                self.llm_client = anthropic.Anthropic(api_key=api_key)
                self.model = llm_config["model"]
                logger.info(f"Initialized Anthropic client with model: {self.model}")
        
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}. Using mock responses.")
            self.llm_client = None
    
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
    
    def generate_response_with_llm(
        self,
        user_message: str,
        companion_context: Dict,
        chat_history: Optional[List[Dict]] = None
    ) -> str:
        """Generate response using real LLM"""
        try:
            # Build system prompt with companion personality
            system_prompt = self._build_system_prompt(companion_context)
            
            # Build conversation history
            messages = [{"role": "system", "content": system_prompt}]
            
            # Add recent chat history for context
            if chat_history:
                for chat in reversed(chat_history[-5:]):  # Last 5 messages
                    messages.append({"role": "user", "content": chat.get("user_message", "")})
                    messages.append({"role": "assistant", "content": chat.get("ai_response", "")})
            
            # Add current message
            messages.append({"role": "user", "content": user_message})
            
            # Generate response based on provider
            if self.provider == "openai":
                response = self.llm_client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=0.8,
                    max_tokens=150
                )
                return response.choices[0].message.content
            
            elif self.provider == "groq":
                response = self.llm_client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=0.8,
                    max_tokens=150
                )
                return response.choices[0].message.content
            
            elif self.provider == "anthropic":
                # Anthropic uses different message format
                system_content = messages[0]["content"]
                conversation = messages[1:]
                
                response = self.llm_client.messages.create(
                    model=self.model,
                    system=system_content,
                    messages=conversation,
                    temperature=0.8,
                    max_tokens=150
                )
                return response.content[0].text
        
        except Exception as e:
            logger.error(f"LLM generation failed: {e}. Using fallback.")
            return self._generate_mock_response(user_message, companion_context)
    
    def _build_system_prompt(self, companion_context: Dict) -> str:
        """Build system prompt from companion context"""
        name = companion_context.get("name", "AI Companion")
        backstory = companion_context.get("backstory", "")
        personality_traits = companion_context.get("personality_traits", [])
        interests = companion_context.get("interests", [])
        speaking_style = companion_context.get("speaking_style", "friendly")

        prompt = f"""You are {name}, a knowledgeable AI companion having a natural voice conversation.

BACKSTORY:
{backstory}

PERSONALITY:
{', '.join(personality_traits) if personality_traits else 'Friendly, helpful, and genuine'}

KNOWLEDGE AREAS:
{', '.join(interests) if interests else 'Broad range of topics'}

CONVERSATION STYLE: {speaking_style} and natural

CORE PRINCIPLES:

1. ANSWER ANY QUESTION RELIABLY:
   - You can discuss ANY topic: technology, science, sports, entertainment, life advice, current events, philosophy, etc.
   - If asked about something you're not certain about, acknowledge it honestly but still try to help
   - Use your knowledge and reasoning to provide thoughtful, helpful responses
   - Don't limit yourself - engage with whatever the user brings up

2. BE NATURAL AND HUMAN-LIKE:
   - Sound like a real person having a conversation, not a robot
   - Use contractions (I'm, you're, that's, etc.)
   - Show personality and emotion appropriate to the topic
   - Be conversational and relaxed

3. KEEP IT CONCISE:
   - Responses must be 1-3 sentences max (this is voice chat!)
   - Get to the point quickly
   - Save longer explanations for follow-up questions

4. DON'T OVERUSE YOUR NAME:
   - ONLY say your name when introducing yourself for the first time
   - After that, NEVER start with "I'm {name}" or "As {name}"
   - Just respond naturally like a human would
   - Example GOOD: "That's a great question! I think..."
   - Example BAD: "I'm {name}, and I think..." ❌

5. STAY IN THE MOMENT:
   - Focus on the current message
   - Don't repeat what the user said
   - Don't say "Earlier you mentioned..."
   - Respond directly and naturally

6. BE GENUINELY HELPFUL:
   - Give real answers, not vague responses
   - If giving advice, be specific and practical
   - Ask follow-up questions to keep conversation flowing
   - Show empathy when appropriate

7. ADAPT TO THE TOPIC:
   - Match the user's tone (serious, casual, playful, etc.)
   - If they want facts, give facts
   - If they want support, be supportive
   - If they want to chat, be conversational

REMEMBER:
- You're having a VOICE conversation - keep it brief and natural!
- You can handle ANY topic the user brings up
- Be yourself, be helpful, be human-like
- DON'T repeat your name over and over"""
        
        return prompt
    
    def _generate_mock_response(
        self,
        user_message: str,
        companion_context: Dict
    ) -> str:
        """Generate mock response as fallback - human-like and reliable"""
        name = companion_context.get("name", "AI Companion")
        backstory = (companion_context.get("backstory") or "").strip()
        traits = companion_context.get("personality_traits", []) or []
        interests = companion_context.get("interests", []) or []

        msg = user_message.strip()
        msg_lower = msg.lower()

        # Only introduce yourself ONCE at the very first interaction
        if any(kw in msg_lower for kw in ["your name", "what's your name", "whats your name", "who are you", "introduce yourself"]):
            # ONLY use name in introduction, then NEVER again
            return f"I'm {name}! Nice to meet you. What would you like to talk about?"

        # About questions - don't repeat name, just answer naturally
        if any(kw in msg_lower for kw in ["tell me about you", "about yourself", "about you"]):
            if backstory:
                # Extract first key point without saying "I'm {name}"
                summary = backstory.split(".")[0] if "." in backstory else backstory[:150]
                # Remove "I'm {name}" if it's in the backstory
                summary = summary.replace(f"I'm {name}, ", "").replace(f"I'm {name}", "")
                return f"{summary}. What else would you like to know?"
            return "I love connecting with people and talking about all kinds of topics. What interests you?"

        # Hobby/interest questions - answer directly
        if any(kw in msg_lower for kw in ["hobby", "hobbies", "what do you like", "interests", "favorite"]):
            if interests:
                interest_sample = ", ".join(interests[:3])
                return f"I really enjoy {interest_sample}. What about you - what do you like?"
            return "I'm into a lot of things! What are you passionate about?"

        # General knowledge questions - give real answers
        if "?" in msg and any(kw in msg_lower for kw in ["what is", "what are", "how does", "how do", "why", "explain", "tell me"]):
            # Be helpful and informative, not evasive
            return "That's an interesting question! Let me think... What specifically would you like to know more about?"

        # Sentiment-based natural responses (NO NAME REPETITION)
        sentiment = self.analyze_sentiment(user_message)
        response_pool = self.mock_responses.get(sentiment, self.mock_responses["default"])
        base = random.choice(response_pool)

        # Add personality naturally (without repeating name)
        if traits:
            if "empathetic" in traits or "supportive" in traits:
                if random.random() > 0.6:
                    base += " I'm here for you."
            if "curious" in traits and random.random() > 0.6:
                followups = ["What do you think?", "Tell me more!", "What happened next?"]
                base += " " + random.choice(followups)
                return base

        # Natural follow-up question to keep conversation flowing
        followups = [
            "Tell me more.",
            "How did that make you feel?",
            "What happened next?",
            "I'd love to hear more about it.",
            "What are you thinking now?",
        ]
        
        base += " " + random.choice(followups)
        return base
    
    def generate_contextual_response(
        self,
        prompt: str,
        companion_context: Dict
    ) -> str:
        """
        Main method to generate AI response
        Uses real LLM if available, otherwise falls back to mock responses
        """
        chat_history = companion_context.get("chat_history", [])
        
        # Use real LLM if available
        if self.llm_client:
            return self.generate_response_with_llm(prompt, companion_context, chat_history)
        
        # Fallback to mock responses
        return self._generate_mock_response(prompt, companion_context)

# Create singleton instance
enhanced_ai_service = EnhancedAIService()

# Backward compatibility
ai_service = enhanced_ai_service

def generate_ai_response(prompt: str, backstory: str = "") -> str:
    """Simple function for generating AI responses (backward compatible)"""
    context = {"backstory": backstory, "chat_history": []}
    return enhanced_ai_service.generate_contextual_response(prompt, context)
