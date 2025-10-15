# 🎤 AI Voice Companion - Complete Setup Guide

## 🌟 What's New - Voice-Enabled Features!

Your AI Companion can now **talk with you naturally** using:
- ✅ **Speech Recognition** - Talk to your AI (hands-free mode available!)
- ✅ **Text-to-Speech** - AI responds with natural human voice
- ✅ **Real LLM Integration** - OpenAI GPT, Groq Llama, or Anthropic Claude
- ✅ **Auto-Signup/Login** - Seamless authentication
- ✅ **3D Character Display Section** - Ready for your 3D model
- ✅ **Hands-Free Mode** - Automatic conversation flow
- ✅ **Conversation Memory** - AI remembers your chats

---

## 🚀 Quick Start

### 1. **Add Your API Key**

Edit the `.env` file:

```env
# Choose your LLM provider
LLM_PROVIDER=openai

# Add your OpenAI API key (or Groq/Anthropic)
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-3.5-turbo

# TTS Configuration (uses same OpenAI key)
USE_OPENAI_TTS=true
OPENAI_TTS_VOICE=nova
```

**Get API Keys:**
- **OpenAI**: https://platform.openai.com/api-keys
- **Groq** (Free, Fast): https://console.groq.com/keys
- **Anthropic Claude**: https://console.anthropic.com/

### 2. **Install New Dependencies**

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install new packages
pip install -r requirements.txt
```

### 3. **Start the Server**

```bash
# Make sure MongoDB is running
# Then start the backend
venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001
```

### 4. **Open Voice Chat UI**

Open `voice_chat.html` in your browser (Chrome recommended for best speech recognition)

---

## 🎯 How to Use

### **First Time Setup**

1. **Open `voice_chat.html`** in Chrome/Edge browser
2. **Sign Up:**
   - Enter your name
   - Enter your email
   - Choose AI companion (Emma or Alex)
   - Click "Start Talking"

3. **Grant Microphone Permission** when browser asks

### **Voice Interaction**

#### **Manual Mode:**
1. Click the **🎤 microphone button**
2. Speak your message
3. AI will respond with voice
4. Click again to speak next message

#### **Hands-Free Mode (Auto-Listen):**
1. Enable the **"🔄 Hands-free mode"** toggle
2. The system automatically:
   - Listens when you stop speaking
   - Gets AI response
   - Plays AI voice
   - Starts listening again
3. **No button clicking needed!**

---

## 🎨 UI Features

### **Three Main Sections:**

#### 1. **3D Character Display** (Left Side)
- Empty section ready for your 3D model
- Voice visualizer shows audio activity
- Can integrate Three.js, Ready Player Me, etc.

#### 2. **Chat Transcript** (Right Side)
- See all conversation text
- Companion avatar and info
- Microphone control button
- Auto-listen toggle

#### 3. **Header**
- Shows current companion name
- User info display
- Logout button

---

## 🔧 Configuration Options

### **Choose Your LLM Provider**

Edit `.env`:

**Option 1: OpenAI (Best quality, paid)**
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-key
OPENAI_MODEL=gpt-3.5-turbo
```

**Option 2: Groq (Fast & Free)**
```env
LLM_PROVIDER=groq
GROQ_API_KEY=your-groq-key
GROQ_MODEL=llama-3.1-70b-versatile
```

**Option 3: Anthropic Claude**
```env
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your-anthropic-key
ANTHROPIC_MODEL=claude-3-sonnet-20240229
```

### **Choose Voice Style**

Available TTS voices (in `.env`):
- `nova` - Female, warm and friendly (default)
- `alloy` - Neutral and balanced
- `echo` - Male, clear
- `fable` - British accent
- `onyx` - Deep male
- `shimmer` - Soft female

```env
OPENAI_TTS_VOICE=nova
```

---

## 🎤 Browser Compatibility

### **Speech Recognition Support:**
- ✅ **Chrome** - Full support (Recommended)
- ✅ **Edge** - Full support
- ✅ **Safari** - Supported
- ❌ **Firefox** - Limited support

### **Recommended:** Use **Google Chrome** for best experience

---

## 📡 API Endpoints

### **New Voice Endpoints:**

#### **Voice Chat**
```
POST /voice/chat
Body: {
  "user_id": "user_id",
  "companion_gender": "girl",
  "message": "transcribed speech text",
  "voice": "nova"
}
Response: {
  "ai_response": "text response",
  "audio_base64": "base64 encoded audio"
}
```

#### **Text-to-Speech**
```
POST /voice/tts?text=Hello&voice=nova
Returns: MP3 audio stream
```

#### **Check TTS Availability**
```
GET /voice/check-tts
```

#### **List Voices**
```
GET /voice/voices
```

---

## 🔌 Adding Your 3D Character

The UI includes a dedicated 3D character section. Here's how to add your model:

### **Using Three.js:**

```javascript
// In voice_chat.html, add this in <script> section
async function load3DCharacter() {
    const characterDisplay = document.getElementById('characterDisplay');
    characterDisplay.innerHTML = ''; // Clear placeholder
    
    // Initialize Three.js scene
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, 
        characterDisplay.offsetWidth / characterDisplay.offsetHeight, 0.1, 1000);
    
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(characterDisplay.offsetWidth, characterDisplay.offsetHeight);
    characterDisplay.appendChild(renderer.domElement);
    
    // Load your 3D model (GLB/GLTF)
    const loader = new THREE.GLTFLoader();
    loader.load('path/to/your/model.glb', (gltf) => {
        scene.add(gltf.scene);
        animate();
    });
    
    function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    }
}

// Call when screen loads
load3DCharacter();
```

### **Using Ready Player Me:**

```javascript
// Add Ready Player Me avatar
function loadReadyPlayerMe() {
    const iframe = document.createElement('iframe');
    iframe.src = 'https://your-character-url.readyplayer.me';
    iframe.style.width = '100%';
    iframe.style.height = '100%';
    iframe.style.border = 'none';
    
    const characterDisplay = document.getElementById('characterDisplay');
    characterDisplay.innerHTML = '';
    characterDisplay.appendChild(iframe);
}
```

---

## 🐛 Troubleshooting

### **No Audio Output**

**Problem:** AI text appears but no voice

**Solution:**
1. Check `.env` has valid `OPENAI_API_KEY`
2. Ensure `USE_OPENAI_TTS=true`
3. Check browser console for errors
4. Test endpoint: `http://127.0.0.1:8001/voice/check-tts`

### **Speech Recognition Not Working**

**Problem:** Microphone doesn't capture speech

**Solution:**
1. Use Chrome/Edge browser
2. Allow microphone permission
3. Check browser console
4. Try HTTPS (speech recognition requires secure context)

### **API Key Errors**

**Problem:** "API key not valid" or similar

**Solution:**
1. Verify `.env` file in `ai_companion_backend/` folder
2. Key should start with `sk-` for OpenAI
3. No quotes around the key
4. Restart server after changing `.env`

### **Auto-Listen Stops**

**Problem:** Hands-free mode stops after a while

**Solution:**
- This is normal browser behavior for security
- Simply re-enable the toggle
- Or click mic button to restart

---

## 💡 Advanced Features

### **Customize AI Personality**

Edit companion backstory in MongoDB:

```javascript
// Using MongoDB Compass
db.companions.updateOne(
    { gender: "girl" },
    { $set: {
        backstory: "Your custom backstory...",
        personality_traits: ["creative", "humorous", "wise"],
        speaking_style: "casual"
    }}
)
```

### **Change Voice Speed**

In `.env`:
```env
DEFAULT_VOICE_SPEED=1.2  # Faster (0.25 - 4.0)
```

### **Multiple Languages**

The UI and TTS support multiple languages. Modify:

```javascript
// In voice_chat.html
recognition.lang = 'es-ES'; // Spanish
recognition.lang = 'fr-FR'; // French
recognition.lang = 'de-DE'; // German
```

---

## 📊 Cost Estimates

### **OpenAI Pricing (as of 2024):**

**GPT-3.5-turbo:**
- Input: $0.0015 / 1K tokens
- Output: $0.002 / 1K tokens
- ~100 conversations = $0.10

**TTS:**
- $15 per 1M characters
- ~1 character per voice message
- ~1000 conversations = $0.015

**Total:** Very affordable! About $0.11 per 100 voice conversations

### **Groq (Free Tier):**
- Free tier available
- Fast inference
- Great for testing

---

## 🎓 Next Steps

### **1. Deploy to Production**
- Use HTTPS for speech recognition
- Deploy to Heroku, Railway, or AWS
- Use MongoDB Atlas for database

### **2. Add Features**
- Emotion detection
- Voice cloning
- Multi-language support
- Video chat integration

### **3. Integrate 3D Character**
- Use Three.js for custom models
- Add lip-sync animation
- Facial expressions based on emotion

### **4. Mobile App**
- Convert to React Native
- Use native speech APIs
- Offline mode

---

## 📞 Support

### **Common Commands**

```bash
# Check if API key is loaded
python -c "from app.config import settings; print(settings.openai_api_key)"

# Test TTS directly
curl "http://127.0.0.1:8001/voice/check-tts"

# Test LLM
python -c "from app.services.ai_service_enhanced import enhanced_ai_service; print(enhanced_ai_service.llm_client)"
```

### **Logs**

Check terminal where server is running for detailed logs

---

## 🎉 You're All Set!

Your AI Voice Companion is ready to talk! Open `voice_chat.html` and start having natural voice conversations with Emma or Alex.

**Tips for Best Experience:**
1. Use headphones to avoid echo
2. Speak clearly and at normal pace
3. Enable hands-free mode for continuous chat
4. Make sure room is quiet for best recognition

**Have fun talking with your AI companion! 🚀**

---

*Last Updated: 2025-10-15*
*Version: 2.0 - Voice-Enabled*
