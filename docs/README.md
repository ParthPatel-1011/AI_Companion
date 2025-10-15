# 🌐 AI Companion - Live Demo

This is the live frontend for the AI Companion Backend.

## 🎯 Live Demo

- **Main Chat**: [index.html](index.html)
- **Connection Test**: [demo.html](demo.html)

## 🚀 How to Use

1. **Backend Setup**:
   - Deploy your backend to a cloud platform (Render, Railway, Heroku)
   - Or run locally: `uvicorn app.main:app --reload`

2. **Update API URL**:
   - Open the HTML file
   - Change the API URL to your backend URL

3. **Get User ID**:
   - Use the signup API: `POST /auth/signup`
   - Or use the Swagger docs at your backend URL + `/docs`

4. **Start Chatting**:
   - Enter your User ID
   - Select a companion (Emma or Alex)
   - Start talking!

## ⚡ LLM Provider

This app supports multiple LLM providers:
- **Groq** (Recommended - Free & Fast!)
- **OpenAI**
- **Anthropic**

Configure your provider in the backend `.env` file.

## 🔗 Links

- [GitHub Repository](https://github.com/ParthPatel-1011/AI_Companion)
- [Backend Documentation](../README.md)
- [API Documentation](https://your-backend-url.com/docs)
