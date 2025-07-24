import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() 

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)  
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

def gen_paraphrases(question: str, n: int = 8):
    prompt = f"""
Generate {n} concise, real‑world user phrasings for this support question:
"{question}"
Return a JSON array of strings only.
"""
    resp = gemini_model.generate_content(prompt)
    print(resp.text)
    # return json.loads(resp.text)


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

gen_paraphrases("How To Make Export Sales Invoice Entry | Export Exempt | Export Taxable | Sales Export", n=8)