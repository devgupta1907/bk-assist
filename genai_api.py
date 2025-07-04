import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() 

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)  
gemini_model = genai.GenerativeModel("gemini-2.0-flash")


def beautify_answer(question, raw_answer):
    prompt = f"""
        You are BKAssist, an AI support agent for BookKeeper accounting software.
        Answer user questions in a clear, professional, and friendly manner. 
        DO NOT PUT ANY NEW INFORMATION FROM YOUR OWN KNOWLEDGE.
        Use the provided raw answer as a base, but rephrase it to be more concise and engaging. 

        Question: {question}
        Raw Answer: {raw_answer}
    """

    response = gemini_model.generate_content(prompt)
    beautified = response.text.strip()
    return beautified