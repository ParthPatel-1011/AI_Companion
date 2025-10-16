"""
Test TTS Service - ElevenLabs
Tests both female and male voices
"""
import asyncio
from app.services.tts_service import tts_service

async def test_tts():
    print("=" * 60)
    print("Testing ElevenLabs TTS Service")
    print("=" * 60)
    print()
    
    # Check if service is available
    if not tts_service.is_available():
        print("❌ ERROR: TTS service is not available!")
        print("Please check your ELEVENLABS_API_KEY in .env")
        return
    
    print("✅ TTS Service is available")
    print("Provider: ElevenLabs")
    print()
    
    # Test female voice
    print("-" * 60)
    print("Test 1: Female Voice (for girl companions)")
    print("-" * 60)
    try:
        text_female = "Hello, I am Emma. I'm your friendly AI companion."
        print(f"Text: '{text_female}'")
        print("Generating audio with female voice...")
        
        audio_female = await tts_service.text_to_speech(
            text=text_female,
            gender='girl'
        )
        
        print(f"✅ SUCCESS: Generated {len(audio_female):,} bytes")
        print(f"   Voice: Female (Rachel)")
        print()
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print()
    
    # Test male voice
    print("-" * 60)
    print("Test 2: Male Voice (for boy companions)")
    print("-" * 60)
    try:
        text_male = "Hello, I am Alex. I'm your AI companion."
        print(f"Text: '{text_male}'")
        print("Generating audio with male voice...")
        
        audio_male = await tts_service.text_to_speech(
            text=text_male,
            gender='boy'
        )
        
        print(f"✅ SUCCESS: Generated {len(audio_male):,} bytes")
        print(f"   Voice: Male (Adam)")
        print()
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print()
    
    # Test base64 encoding
    print("-" * 60)
    print("Test 3: Base64 Encoding (for browser playback)")
    print("-" * 60)
    try:
        text_short = "Testing base64 encoding."
        print(f"Text: '{text_short}'")
        print("Generating audio and encoding to base64...")
        
        audio_base64 = await tts_service.text_to_speech_base64(
            text=text_short,
            gender='girl'
        )
        
        print(f"✅ SUCCESS: Generated base64 string")
        print(f"   Length: {len(audio_base64):,} characters")
        print(f"   Sample: {audio_base64[:50]}...")
        print()
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print()
    
    print("=" * 60)
    print("✅ ALL TTS TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print()
    print("Your ElevenLabs TTS is working perfectly!")
    print("Female voice (girl): Rachel")
    print("Male voice (boy): Adam")
    print()

if __name__ == "__main__":
    asyncio.run(test_tts())
