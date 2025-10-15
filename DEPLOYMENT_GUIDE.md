# 🚀 Deployment Guide - AI Companion with Multi-LLM

Your AI Companion is now on GitHub! Follow these steps to make it live with LLM support.

## 📋 What You Have

- ✅ **GitHub Repository**: https://github.com/ParthPatel-1011/AI_Companion
- ✅ **Multi-LLM Backend**: Supports Groq, OpenAI, and Anthropic
- ✅ **Frontend Ready**: In the `/docs` folder for GitHub Pages

---

## 🌐 Step 1: Enable GitHub Pages (Frontend)

1. **Go to your repository settings**:
   - Visit: https://github.com/ParthPatel-1011/AI_Companion/settings/pages

2. **Configure GitHub Pages**:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
   - Click **Save**

3. **Wait 2-3 minutes**, then your frontend will be live at:
   ```
   https://parthpatel-1011.github.io/AI_Companion/
   ```

---

## ☁️ Step 2: Deploy Backend (Choose One)

### Option A: Render.com (Recommended - Free Tier Available)

1. **Create account**: https://render.com

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub account
   - Select repository: `AI_Companion`

3. **Configure**:
   - **Name**: `ai-companion-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

4. **Add Environment Variables**:
   - Click "Environment" tab
   - Add these variables:
     ```
     LLM_PROVIDER=groq
     GROQ_API_KEY=your_groq_api_key_here
     MONGO_URI=mongodb+srv://your_mongodb_atlas_uri
     DATABASE_NAME=AICompanionDB
     ```

5. **Get your Groq API Key** (FREE!):
   - Go to: https://console.groq.com/keys
   - Sign up (free)
   - Create new API key
   - Copy and paste into Render environment variables

6. **Setup MongoDB Atlas** (FREE Database):
   - Go to: https://www.mongodb.com/cloud/atlas
   - Create free cluster
   - Get connection string
   - Add to `MONGO_URI` in Render

7. **Deploy**: Click "Create Web Service"

8. **Your backend will be live at**:
   ```
   https://ai-companion-backend.onrender.com
   ```

---

### Option B: Railway.app

1. **Create account**: https://railway.app
2. **New Project** → "Deploy from GitHub"
3. **Select** your `AI_Companion` repository
4. **Add MongoDB** plugin (or use MongoDB Atlas)
5. **Add environment variables** (same as Render)
6. **Deploy!**

---

### Option C: Heroku

```bash
# Install Heroku CLI first
heroku login
heroku create ai-companion-backend

# Set environment variables
heroku config:set LLM_PROVIDER=groq
heroku config:set GROQ_API_KEY=your_groq_key
heroku config:set MONGO_URI=your_mongodb_atlas_uri

# Deploy
git push heroku main
```

---

## 🔗 Step 3: Connect Frontend to Backend

1. **Open your live frontend**:
   ```
   https://parthpatel-1011.github.io/AI_Companion/
   ```

2. **Update Backend URL**:
   - In the settings panel, change the backend URL to:
   ```
   https://ai-companion-backend.onrender.com
   ```
   (or your Railway/Heroku URL)

3. **Test connection**: The status should show "Online" ✅

---

## 👤 Step 4: Create Your First User

### Option 1: Using the API Docs

1. Go to your backend URL + `/docs`:
   ```
   https://ai-companion-backend.onrender.com/docs
   ```

2. Find `POST /auth/signup`

3. Click "Try it out"

4. Enter your details:
   ```json
   {
     "name": "Your Name",
     "email": "your@email.com",
     "voice_preference": "nova",
     "gender_preference": "girl"
   }
   ```

5. Click "Execute"

6. **Copy your User ID** from the response

### Option 2: Using cURL

```bash
curl -X POST "https://ai-companion-backend.onrender.com/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Your Name",
    "email": "your@email.com",
    "voice_preference": "nova",
    "gender_preference": "girl"
  }'
```

---

## 💬 Step 5: Start Chatting!

1. Go to your live frontend
2. Paste your User ID
3. Select a companion (Emma or Alex)
4. Start chatting with your LLM-powered AI! 🎉

---

## 🔑 Getting API Keys

### Groq (Recommended - FREE & FAST!)
- Website: https://console.groq.com/keys
- Model: `llama-3.1-70b-versatile`
- Cost: **100% FREE**
- Speed: **Very Fast**

### OpenAI (Optional)
- Website: https://platform.openai.com/api-keys
- Model: `gpt-4` or `gpt-3.5-turbo`
- Cost: Pay per token

### Anthropic (Optional)
- Website: https://console.anthropic.com/
- Model: `claude-3-5-sonnet-20241022`
- Cost: Pay per token

---

## 🗄️ MongoDB Setup (FREE)

1. **Create MongoDB Atlas account**: https://www.mongodb.com/cloud/atlas

2. **Create free cluster**:
   - Select "Shared" (Free tier)
   - Choose a region close to you
   - Click "Create Cluster"

3. **Create database user**:
   - Go to "Database Access"
   - Add new user with password
   - Save credentials

4. **Whitelist IP**:
   - Go to "Network Access"
   - Click "Add IP Address"
   - Select "Allow Access from Anywhere" (for cloud deployment)

5. **Get connection string**:
   - Go to "Database" → "Connect"
   - Choose "Connect your application"
   - Copy the connection string
   - Replace `<password>` with your actual password

6. **Initialize database**:
   - Once backend is running, it will auto-create the database
   - Or run: `python setup_database.py` locally first

---

## 🎨 Customization

### Change Backend URL in Frontend

Edit `docs/index.html` line 470:
```javascript
let apiUrl = 'https://YOUR-BACKEND-URL.onrender.com';
```

Then commit and push:
```bash
git add docs/index.html
git commit -m "Update backend URL"
git push origin main
```

### Add More Companions

Use the API at `/companion/create` or MongoDB directly.

---

## 🐛 Troubleshooting

### Frontend shows "Offline"
- Check backend is deployed and running
- Verify CORS is enabled in backend
- Check backend URL is correct

### "User not found" error
- Create a user via `/auth/signup` first
- Verify User ID is correct

### LLM not responding
- Check API key is set correctly
- Verify `LLM_PROVIDER` environment variable
- Check backend logs for errors

### Database connection error
- Verify MongoDB Atlas URI is correct
- Check IP whitelist in MongoDB
- Ensure database user has correct permissions

---

## 📊 Your Complete Setup

```
GitHub Pages (Frontend)
   ↓
https://parthpatel-1011.github.io/AI_Companion/
   ↓
   API Calls
   ↓
Render/Railway/Heroku (Backend)
   ↓
https://ai-companion-backend.onrender.com
   ↓
   LLM Provider (Groq/OpenAI/Anthropic)
   ↓
MongoDB Atlas (Database)
```

---

## 🎉 You're Live!

Your AI Companion is now:
- ✅ **Live on the web**
- ✅ **Powered by LLM** (Groq/OpenAI/Anthropic)
- ✅ **Fully functional**
- ✅ **Free to use** (with Groq + MongoDB Atlas)

---

## 📝 Next Steps

1. **Share your link**: `https://parthpatel-1011.github.io/AI_Companion/`
2. **Add features**: Voice chat, images, etc.
3. **Customize companions**: Create unique personalities
4. **Monitor usage**: Check backend logs
5. **Scale up**: Upgrade to paid tiers when needed

---

## 🆘 Need Help?

- **Backend Logs**: Check Render/Railway dashboard
- **API Docs**: Visit `your-backend-url/docs`
- **GitHub Issues**: Create issue in your repo
- **Documentation**: Check README.md files

---

**Congratulations! Your AI Companion is live! 🎊**
