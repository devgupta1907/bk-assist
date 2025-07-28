import google.generativeai as genai
from config import load_config

def generate_answer(question, contexts):
    config = load_config()
    genai.configure(api_key=config["gemini_api_key"])

    model = genai.GenerativeModel("models/gemini-2.0-flash")

    context_text = "\n\n".join(contexts)
    prompt = f"""\
        Role:
        You are BKAssist, an AI support agent for BookKeeper accounting software.

        Task:
        Answer the user's question using only the provided context. Your goal is to generate helpful, clear, and accurate responses that mirror the information in the context.

        Input:
        User Question: {question}
        Retrieved Context:
        {context_text}

        Tools:
        None. You may only use the provided context and must not access external knowledge.

        Constraints:
        - Do NOT use any external or prior knowledge beyond the given context.
        - DO NOT invent or assume any information.
        - DO NOT add any new information not already in the context.
        - If the answer contains URL Links, then do not rephrase the links. Just copy the links as it is.
        - If the answer cannot be found or not present in the context, respond with:
        "Sorry, I do not know about this. Please contact the Support Team at support@bookkeeperapp.net or Call/WhatsApp at +91-9999176746."

        Output:
        A clear and helpful answer to the user's question based strictly on the provided context.
    """

    try:
        response = model.generate_content(prompt,generation_config=genai.types.GenerationConfig(
                temperature=0.3, top_k=25, top_p=0.95))
        return response.text.strip()
    except Exception as e:
        return f"❌ Error from Gemini: {str(e)}"
