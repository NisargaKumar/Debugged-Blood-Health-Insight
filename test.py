import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"Loaded key: {api_key}")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("Hello!")
print(response.text)

import litellm
print("💡 LLM Provider:", os.getenv("LITELLM_PROVIDER"))
print("💡 LLM Model:", os.getenv("LITELLM_MODEL"))