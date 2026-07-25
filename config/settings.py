from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found.")

if not GEMINI_MODEL:
    raise ValueError("GEMINI_MODEL not found.")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found.")