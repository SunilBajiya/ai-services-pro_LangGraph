import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))
def get_gemini_llm():
    return genai.GenerativeModel("gemini-2.5-flash")