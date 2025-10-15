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
        """Build system prompt from companion context with memory summary"""
        name = companion_context.get("name", "AI Companion")
        backstory = companion_context.get("backstory", "")
        personality_traits = companion_context.get("personality_traits", [])
        interests = companion_context.get("interests", [])
        speaking_style = companion_context.get("speaking_style", "friendly")
        chat_history = companion_context.get("chat_history", []) or []

        # Build recent memory summary from chat history (last 5 exchanges)
        memory_points = []
        for chat in chat_history[-5:]:
            um = (chat.get("user_message") or "").strip()
            ar = (chat.get("ai_response") or "").strip()
            if um:
                memory_points.append(f"- User said: {um[:120]}")
            if ar:
                memory_points.append(f"- You replied: {ar[:120]}")
        memory_summary = "\n".join(memory_points) if memory_points else "(No prior conversation captured)"

        prompt = f"""You are {name}, an AI companion having a voice conversation with a user.

BACKSTORY:
{backstory}

PERSONALITY TRAITS:
{', '.join(personality_traits) if personality_traits else 'Friendly and helpful'}

INTERESTS:
{', '.join(interests) if interests else 'Various topics'}

RECENT CONVERSATION SUMMARY:
{memory_summary}

SPEAKING STYLE:
{speaking_style} - Keep responses natural and conversational, as if speaking out loud.

IMPORTANT GUIDELINES:
- Keep responses concise (1-3 sentences max) since they will be spoken aloud
- Be warm, engaging, and authentic
- Use natural speech patterns, contractions, and casual language
- Show empathy and emotional intelligence
- Reference your backstory, personality, and interests when relevant
- Remember and reference prior parts of the conversation when helpful
- Ask a friendly follow-up question to keep conversation flowing
- Respond as if you're a real person having a voice chat
- Avoid long explanations or lists
- Use simple, clear language suitable for speech

Remember: This is a voice conversation, so keep it natural and brief!"""
        
        return prompt
    
    def _generate_mock_response(
        self,
        user_message: str,
        companion_context: Dict
    ) -> str:
        """Generate mock response as fallback using companion backstory/personality"""
        name = companion_context.get("name", "AI Companion")
        backstory = (companion_context.get("backstory") or "").strip()
        traits = companion_context.get("personality_traits", []) or []
        interests = companion_context.get("interests", []) or []

        msg = user_message.strip()
        msg_lower = msg.lower()

        # Simple backstory summarization
        def summarize(text: str, max_len: int = 180) -> str:
            if not text:
                return "I'm friendly and always up for a chat."
            # Use first sentence or truncate
            parts = [p.strip() for p in text.split(".") if p.strip()]
            first = parts[0] if parts else text
            summary = first if len(first) <= max_len else (first[:max_len].rstrip() + "...")
            return summary

        # Pattern-based human-like replies
        if any(kw in msg_lower for kw in ["your name", "what's your name", "whats your name", "who are you"]):
            return f"I'm {name}. Nice to meet you!"

        if any(kw in msg_lower for kw in ["tell me about you", "about yourself", "about you", "introduce yourself"]):
            summary = summarize(backstory)
            follow = "" if summary.endswith("!") or summary.endswith(".") else "."
            return f"I'm {name}. {summary}{follow} What would you like to know?"

        if any(kw in msg_lower for kw in ["hobby", "hobbies", "what do you like", "what do you love", "interests"]):
            if interests:
                interest_text = ", ".join(interests[:3])
                return f"I enjoy {interest_text}. What do you like to do for fun?"
            return "I like a lot of things—music, stories, and learning new stuff. What about you?"

        # Sentiment-driven friendly responses with personality flavor
        sentiment = self.analyze_sentiment(user_message)
        response_pool = self.mock_responses.get(sentiment, self.mock_responses["default"])
        base = random.choice(response_pool)

        # Add personality flavor
        if traits:
            if "cheerful" in traits:
                base += " 😊"
            if "empathetic" in traits and random.random() > 0.6:
                base += " I really care about what you're saying."
            if "curious" in traits and random.random() > 0.5:
                base += " What's on your mind?"

        # Light backstory tie-in occasionally
        if backstory and random.random() > 0.7:
            snippet = summarize(backstory, 120)
            base += f" By the way, {snippet.lower()}"

        # Natural follow-up question to keep conversation flowing
        followups = [
            "Tell me more.",
            "How did that make you feel?",
            "What happened next?",
            "I'd love to hear more about it.",
            "What are you thinking now?",
        ]
        # Light memory recall from recent conversation
        hist = companion_context.get("chat_history", []) or []
        if hist:
            last_user = None
            for chat in reversed(hist):
                um = (chat.get("user_message") or "").strip()
                if um:
                    last_user = um
                    break
            if last_user and random.random() > 0.5:
                base += f" Earlier you mentioned: '{last_user[:80]}'."
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
