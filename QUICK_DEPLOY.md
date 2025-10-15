# ⚡ Quick Deploy Checklist

## ✅ What's Done

- [x] Project uploaded to GitHub: https://github.com/ParthPatel-1011/AI_Companion
- [x] Frontend ready in `/docs` folder
- [x] `.gitignore` created (protects API keys)
- [x] `.env.example` created (template for configuration)

---

## 🎯 Next Steps (Do These Now!)

### 1️⃣ Enable GitHub Pages (5 minutes)

1. Go to: https://github.com/ParthPatel-1011/AI_Companion/settings/pages
2. Set:
   - **Source**: Deploy from a branch
   - **Branch**: main
   - **Folder**: /docs
3. Click **Save**
4. Wait 2-3 minutes
5. Your frontend will be live at: **https://parthpatel-1011.github.io/AI_Companion/**

---

### 2️⃣ Get Free Groq API Key (2 minutes)

1. Go to: https://console.groq.com/keys
2. Sign up (free)
3. Click "Create API Key"
4. Copy the key (starts with `gsk_...`)
5. Save it somewhere safe!

---

### 3️⃣ Setup Free MongoDB (5 minutes)

1. Go to: https://www.mongodb.com/cloud/atlas
2. Sign up (free)
3. Create cluster:
   - Click "Build a Database"
   - Select **FREE** tier (M0)
   - Choose region close to you
   - Click "Create"
4. Create user:
   - Username: `admin`
   - Password: (create strong password)
   - Save credentials!
5. Whitelist IP:
   - Network Access → Add IP
   - "Allow access from anywhere"
6. Get connection string:
   - Database → Connect
   - "Connect your application"
   - Copy the URI
   - Replace `<password>` with your actual password

---

### 4️⃣ Deploy Backend to Render (10 minutes)

1. Go to: https://render.com
2. Sign up (free)
3. Click "New +" → "Web Service"
4. Connect GitHub → Select `AI_Companion` repo
5. Configure:
   - **Name**: `ai-companion-backend`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add Environment Variables (click "Advanced"):
   ```
   LLM_PROVIDER=groq
   GROQ_API_KEY=gsk_YOUR_KEY_HERE
   MONGO_URI=mongodb+srv://admin:PASSWORD@cluster.mongodb.net/
   DATABASE_NAME=AICompanionDB
   ```
7. Click "Create Web Service"
8. Wait 5-10 minutes for deployment
9. Copy your backend URL: `https://ai-companion-backend.onrender.com`

---

### 5️⃣ Connect Frontend to Backend (1 minute)

1. Open your live frontend: https://parthpatel-1011.github.io/AI_Companion/
2. In the settings panel, update "Backend URL" to your Render URL
3. Should show "Online" ✅

---

### 6️⃣ Create Your First User

1. Go to: `https://your-backend-url.onrender.com/docs`
2. Find `POST /auth/signup`
3. Click "Try it out"
4. Enter:
   ```json
   {
     "name": "Your Name",
     "email": "your@email.com",
     "voice_preference": "nova",
     "gender_preference": "girl"
   }
   ```
5. Click "Execute"
6. Copy your `user_id`

---

### 7️⃣ Start Chatting! 🎉

1. Go to your frontend
2. Paste your User ID
3. Select Emma or Alex
4. Type a message
5. Enjoy your LLM-powered AI companion!

---

## 📊 Summary

| Item | URL/Value |
|------|-----------|
| **GitHub Repo** | https://github.com/ParthPatel-1011/AI_Companion |
| **Live Frontend** | https://parthpatel-1011.github.io/AI_Companion/ |
| **Backend** | https://ai-companion-backend.onrender.com |
| **API Docs** | https://ai-companion-backend.onrender.com/docs |
| **LLM Provider** | Groq (Free!) |
| **Database** | MongoDB Atlas (Free!) |

---

## 🆘 Troubleshooting

**Frontend shows "Offline"?**
- Wait for Render deployment to complete (5-10 min)
- Check backend URL is correct
- Visit backend URL to wake it up (free tier sleeps)

**"User not found" error?**
- Create user via API docs first
- Copy User ID exactly

**LLM not responding?**
- Check Groq API key in Render environment variables
- Check backend logs in Render dashboard

---

## 🎊 That's It!

Your AI Companion is now:
- ✅ Live on the internet
- ✅ Powered by LLM (Groq)
- ✅ 100% FREE
- ✅ Ready to chat!

**Share your link**: https://parthpatel-1011.github.io/AI_Companion/

---

For detailed instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
