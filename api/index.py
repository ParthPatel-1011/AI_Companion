"""
Vercel Serverless Function Entry Point
"""
from app.main import app

# Export the FastAPI app for Vercel
handler = app
