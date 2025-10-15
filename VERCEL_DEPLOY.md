# 🚀 Deploy to Vercel - Complete Guide

Deploy your AI Companion backend to Vercel in minutes!

## 📋 Prerequisites

1. ✅ GitHub account with your code pushed
2. ✅ Vercel account (free) - https://vercel.com
3. ✅ Groq API Key (free) - https://console.groq.com/keys
4. ✅ MongoDB Atlas account (free) - https://www.mongodb.com/cloud/atlas

---

## 🎯 Step-by-Step Deployment

### Step 1: Get Your API Keys (5 minutes)

#### 1.1 Get Groq API Key (FREE!)
1. Go to: https://console.groq.com/keys
2. Sign up (it's free!)
3. Click "Create API Key"
4. Copy the key (starts with `gsk_...`)
5. Save it somewhere safe!

#### 1.2 Setup MongoDB Atlas (FREE!)
1. Go to: https://www.mongodb.com/cloud/atlas
2. Sign up for free
3. Create a free cluster:
   - Click "Build a Database"
   - Select **FREE** tier (M0 Sandbox)
   - Choose region closest to you
   - Click "Create"

4. Create database user:
   - Go to "Database Access"
   - Click "Add New Database User"
   - Username: `admin` (or your choice)
   - Password: (generate strong password)
   - **Save credentials!**

5. Whitelist all IPs (for Vercel):
   - Go to "Network Access"
   - Click "Add IP Address"
   - Select "**Allow Access from Anywhere**" (0.0.0.0/0)
   - Confirm

6. Get connection string:
   - Go to "Database" → "Connect"
   - Choose "Connect your application"
   - Copy the connection string
   - Replace `<password>` with your actual password
   - Example: `mongodb+srv://admin:YourPassword123@cluster0.xxxxx.mongodb.net/`

---

### Step 2: Deploy to Vercel (5 minutes)

#### 2.1 Sign Up & Connect GitHub
1. Go to: https://vercel.com/signup
2. Sign up with GitHub
3. Authorize Vercel to access your repositories

#### 2.2 Import Your Project
1. Click "**Add New...**" → "**Project**"
2. Find and select your repository: `AI_Companion`
3. Click "**Import**"

#### 2.3 Configure Project
1. **Framework Preset**: Other
2. **Root Directory**: `./` (leave as is)
3. **Build Command**: (leave empty)
4. **Output Directory**: (leave empty)

#### 2.4 Add Environment Variables
Click "**Environment Variables**" and add these:

| Name | Value |
|------|-------|
| `LLM_PROVIDER` | `groq` |
| `GROQ_API_KEY` | `gsk_your_groq_api_key_here` |
| `MONGO_URI` | `mongodb+srv://admin:password@cluster0.xxxxx.mongodb.net/` |
| `DATABASE_NAME` | `AICompanionDB` |

**Important:** Add to "Production", "Preview", and "Development"

#### 2.5 Deploy!
1. Click "**Deploy**"
2. Wait 2-3 minutes for deployment
3. Your backend will be live at: `https://your-project.vercel.app`

---

### Step 3: Test Your Deployment (2 minutes)

#### 3.1 Test API Health
Visit: `https://your-project.vercel.app/`

You should see:
```json
{
  "message": "AI Companion Backend is running!",
  "status": "healthy",
  "version": "1.0.0"
}
```

#### 3.2 Test API Documentation
Visit: `https://your-project.vercel.app/docs`

You should see the Swagger UI with all endpoints!

---

### Step 4: Connect Frontend to Vercel Backend

#### 4.1 Update Frontend
1. Go to your GitHub Pages site or open `docs/index.html`
2. Update the backend URL to your Vercel URL:
   ```
   https://your-project.vercel.app
   ```

#### 4.2 Test Connection
1. The status should show "Online" ✅
2. Sign in with name and email
3. Start chatting!

---

## 🎨 Custom Domain (Optional)

### Add Your Own Domain

1. Go to your Vercel project dashboard
2. Click "**Settings**" → "**Domains**"
3. Add your domain (e.g., `api.yourwebsite.com`)
4. Follow DNS configuration instructions
5. Update frontend to use your custom domain

---

## 🔄 Automatic Deployments

**Every time you push to GitHub:**
- ✅ Vercel automatically deploys
- ✅ No manual redeployment needed
- ✅ Preview deployments for branches

---

## 🐛 Troubleshooting

### Issue 1: "Module not found" Error
**Solution:** Make sure `requirements.txt` is in the root directory

### Issue 2: "Database connection failed"
**Solution:** 
- Check MongoDB Atlas connection string
- Ensure password has no special characters (or URL-encode them)
- Verify IP whitelist includes 0.0.0.0/0

### Issue 3: "Groq API error"
**Solution:**
- Verify API key is correct
- Check if you've hit rate limits (unlikely with free tier)

### Issue 4: "CORS error" from frontend
**Solution:** CORS is already configured in `main.py` to allow all origins

### Issue 5: Functions timing out
**Solution:** Vercel free tier has 10-second timeout. Consider:
- Optimize database queries
- Use Vercel Pro for 60-second timeout
- Or use Render.com instead (no timeout on free tier)

---

## 📊 Your Complete Setup

```
┌─────────────────────────────────────┐
│  GitHub Pages (Frontend)            │
│  https://parthpatel-1011.github.io/ │
│            AI_Companion/            │
└────────────┬────────────────────────┘
             │
             │ API Calls
             ↓
┌─────────────────────────────────────┐
│  Vercel (Backend - FastAPI)         │
│  https://your-project.vercel.app    │
└────────────┬────────────────────────┘
             │
             ├─→ Groq (LLM - Free!)
             │
             └─→ MongoDB Atlas (Database - Free!)
```

---

## ✅ Deployment Checklist

- [ ] Groq API key obtained
- [ ] MongoDB Atlas cluster created
- [ ] MongoDB connection string copied
- [ ] Vercel account created
- [ ] Repository imported to Vercel
- [ ] Environment variables added
- [ ] Deployment successful
- [ ] API health check passed (/health endpoint)
- [ ] API docs accessible (/docs endpoint)
- [ ] Frontend updated with Vercel URL
- [ ] Test user created and chat working

---

## 🎯 Next Steps

1. **Share Your Link**: 
   - Frontend: `https://parthpatel-1011.github.io/AI_Companion/`
   - Backend API: `https://your-project.vercel.app`

2. **Monitor Usage**:
   - Vercel Dashboard: Check function invocations
   - MongoDB Atlas: Monitor database usage

3. **Upgrade if Needed**:
   - Vercel Pro: $20/month (60s timeout, more bandwidth)
   - MongoDB Atlas: Upgrade for more storage

---

## 💡 Pro Tips

1. **Environment Variables**: Never commit API keys to GitHub!
2. **Database Backups**: MongoDB Atlas auto-backups on paid tiers
3. **Monitoring**: Use Vercel Analytics to track API usage
4. **Custom Domain**: Makes your API look professional
5. **Rate Limiting**: Consider adding rate limiting for production

---

## 🆘 Need Help?

- **Vercel Docs**: https://vercel.com/docs
- **Vercel Support**: https://vercel.com/support
- **MongoDB Docs**: https://www.mongodb.com/docs/atlas/
- **FastAPI Docs**: https://fastapi.tiangolo.com/

---

## 🎉 Success!

Your AI Companion is now:
- ✅ **Live on Vercel** (globally distributed)
- ✅ **Auto-deploying** from GitHub
- ✅ **Powered by LLM** (Groq)
- ✅ **100% Serverless**
- ✅ **FREE to use**

**Congratulations! 🎊**

Your backend URL: `https://your-project.vercel.app`

Share it with the world! 🌍
