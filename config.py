import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        "chroma_collection": "faq_collection",
        "gemini_api_key": os.getenv("GEMINI_API_KEY"),
    }
