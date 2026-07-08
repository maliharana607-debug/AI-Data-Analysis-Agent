import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key:
    print(f"✅ API Key loaded: {api_key[:20]}...")
else:
    print("❌ API Key NOT found")