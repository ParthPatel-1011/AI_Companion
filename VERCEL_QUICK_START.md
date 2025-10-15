# ⚡ Vercel Quick Start - Deploy in 10 Minutes!

## 🎯 Super Fast Deployment Steps

### 1️⃣ Get Groq API Key (2 min)
👉 https://console.groq.com/keys
- Sign up (free)
- Create API key
- Copy it!

### 2️⃣ Setup MongoDB (3 min)
👉 https://www.mongodb.com/cloud/atlas
- Create free cluster
- Create user (username + password)
- Network Access → Allow 0.0.0.0/0
- Get connection string
- Replace `<password>` with your password

### 3️⃣ Deploy to Vercel (5 min)
👉 https://vercel.com

1. **Sign up** with GitHub
2. Click "**Add New Project**"
3. Import `AI_Companion` repository
4. Add **Environment Variables**:
   ```
   LLM_PROVIDER = groq
   GROQ_API_KEY = gsk_your_key_here
   MONGO_URI = mongodb+srv://admin:password@cluster.mongodb.net/
   DATABASE_NAME = AICompanionDB
   ```
5. Click "**Deploy**"
6. Wait 2-3 minutes ⏱️

### 4️⃣ Test & Use
✅ Your backend: `https://your-project.vercel.app`
✅ API Docs: `https://your-project.vercel.app/docs`
✅ Update frontend with this URL

---

## 🎉 Done!

**Your AI Companion is LIVE!** 🚀

- Backend on Vercel ✅
- Frontend on GitHub Pages ✅
- Powered by Groq LLM ✅
- 100% FREE ✅

---

## 📚 Detailed Guide
For complete instructions, see [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md)

## 🆘 Issues?
Check [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md) troubleshooting section
