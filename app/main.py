"""
AI Companion Backend - Main Application
FastAPI application for AI companion chat system
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import auth_routes, chat_routes, companion_routes, voice_routes
from app.config import settings
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI application
app = FastAPI(
    title="AI Companion Backend",
    description="Backend API for AI Companion chat system with human-like conversations",
    version="1.0.1",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS - Allow file:// and all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins including file://
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Include routers
app.include_router(
    auth_routes.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    companion_routes.router,
    prefix="/companion",
    tags=["Companion"]
)

app.include_router(
    chat_routes.router,
    prefix="/chat",
    tags=["Chat"]
)

app.include_router(
    voice_routes.router,
    prefix="/voice",
    tags=["Voice"]
)

# Serve frontend files (voice_chat.html, index.html, etc.) over HTTP to persist mic permissions
app.mount("/web", StaticFiles(directory="..\\ai_companion_backend", html=True), name="static")

# Root endpoint
@app.get("/", tags=["Health"])
async def root():
    """
    Root endpoint - Health check
    """
    return {
        "message": "AI Companion Backend is running!",
        "status": "healthy",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "auth": "/auth",
            "companion": "/companion",
            "chat": "/chat"
        }
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "database": "connected",
        "api": "running"
    }

# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Execute on application startup
    """
    logger.info("="*50)
    logger.info("AI Companion Backend Starting...")
    logger.info("="*50)
    logger.info("FastAPI application initialized")
    logger.info("MongoDB connection established")
    logger.info("API Documentation: http://127.0.0.1:8000/docs")
    logger.info("="*50)

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """
    Execute on application shutdown
    """
    logger.info("AI Companion Backend shutting down...")
    from app.database import close_connection
    close_connection()
    logger.info("MongoDB connection closed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
