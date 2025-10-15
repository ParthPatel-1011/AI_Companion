# 🏗️ AI Voice Companion - System Architecture

## 📊 High-Level Architecture

```mermaid
graph TB
    subgraph "Frontend - Voice UI"
        A[voice_chat.html]
        B[Web Speech API<br/>Speech Recognition]
        C[Audio Player<br/>TTS Playback]
        D[3D Character Display]
    end
    
    subgraph "Backend - FastAPI Server"
        E[Main App<br/>app/main.py]
        F[Voice Routes<br/>/voice/*]
        G[Auth Routes<br/>/auth/*]
        H[Chat Routes<br/>/chat/*]
    end
    
    subgraph "Services Layer"
        I[Enhanced AI Service<br/>OpenAI/Groq/Claude]
        J[TTS Service<br/>OpenAI TTS]
        K[User Service]
    end
    
    subgraph "Data Layer"
        L[(MongoDB)]
        M[users collection]
        N[companions collection]
        O[chats collection]
    end
    
    subgraph "External APIs"
        P[OpenAI API<br/>GPT-3.5/GPT-4]
        Q[OpenAI TTS API]
        R[Groq API<br/>Optional]
    end
    
    A --> B
    A --> C
    A --> D
    B --> F
    F --> I
    F --> J
    I --> P
    I --> R
    J --> Q
    G --> K
    H --> I
    F --> L
    G --> L
    H --> L
    L --> M
    L --> N
    L --> O
    J --> C
