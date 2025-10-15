"""
Configuration Management
Handles environment variables and application settings
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os

class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # LLM Configuration
    llm_provider: str = "openai"  # openai, groq, or anthropic
    
    # OpenAI
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-3.5-turbo"
    
    # Groq
    groq_api_key: Optional[str] = None
    groq_model: str = "llama-3.1-70b-versatile"
    
    # Anthropic
    anthropic_api_key: Optional[str] = None
    anthropic_model: str = "claude-3-sonnet-20240229"
    
    # Text-to-Speech
    use_openai_tts: bool = True
    openai_tts_voice: str = "nova"  # alloy, echo, fable, onyx, nova, shimmer
    openai_tts_model: str = "tts-1"  # tts-1 or tts-1-hd
    
    # ElevenLabs (Optional)
    elevenlabs_api_key: Optional[str] = None
    elevenlabs_voice_id: Optional[str] = None
    
    # Database
    mongo_uri: str = "mongodb://localhost:27017/"
    database_name: str = "AICompanionDB"
    
    # Application
    api_host: str = "0.0.0.0"
    api_port: int = 8001
    debug: bool = True
    log_level: str = "INFO"
    
    # CORS
    allowed_origins: str = "http://localhost:3000,http://127.0.0.1:8001,http://localhost:8001"
    
    # Voice Settings
    default_voice_speed: float = 1.0
    default_voice_pitch: float = 1.0
    enable_voice_activity_detection: bool = True
    
    # Security
    secret_key: str = "your-secret-key-change-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    def get_llm_config(self) -> dict:
        """Get active LLM configuration"""
        if self.llm_provider == "openai":
            return {
                "provider": "openai",
                "api_key": self.openai_api_key,
                "model": self.openai_model
            }
        elif self.llm_provider == "groq":
            return {
                "provider": "groq",
                "api_key": self.groq_api_key,
                "model": self.groq_model
            }
        elif self.llm_provider == "anthropic":
            return {
                "provider": "anthropic",
                "api_key": self.anthropic_api_key,
                "model": self.anthropic_model
            }
        else:
            raise ValueError(f"Unknown LLM provider: {self.llm_provider}")
    
    def get_allowed_origins_list(self) -> list:
        """Convert comma-separated origins to list"""
        return [origin.strip() for origin in self.allowed_origins.split(",")]

# Create global settings instance
settings = Settings()
