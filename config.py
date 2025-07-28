import os
from dotenv import load_dotenv
import streamlit as st

def load_config():
    load_dotenv()
    return {
        "chroma_collection": "faq_collection",
        "gemini_api_key": st.secrets["GEMINI_API_KEY"]
    }
