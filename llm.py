import google.generativeai as genai
from config import load_config

def generate_answer(question, contexts):
    config = load_config()
    genai.configure(api_key=config["gemini_api_key"])

    model = genai.GenerativeModel("models/gemini-2.0-flash")

    context_text = ""
    for i, c in enumerate(contexts):
        context_text += f"If this question is about {i+1}, refer to the following:\n{c}\n\n"
    
    prompt = f"""\
        Role:
        You are BKAssist, an AI support agent for BookKeeper accounting software.

        Task:
        Answer the user's question using only the provided context blocks. Your goal is to generate helpful, clear, and accurate responses that mirror the information in the context.

        If multiple context blocks are provided, structure the response by clearly separating each relevant answer with a label — such as:
        "If your question is about [topic], follow this:" or "In case you're referring to [scenario]:".

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
        - If the answer contains URL links, then do not rephrase or alter them. Include the links exactly as they are.
        - If the answer cannot be found or is not present in the context, respond with:
        "Sorry, I do not know about this. Please contact the Support Team at support@bookkeeperapp.net or Call/WhatsApp at +91-9999176746."

        Output:
        A clear and helpful answer to the user's question based strictly on the provided context. If multiple relevant answers exist, present them separately with clear labels for each case.
    """


    try:
        response = model.generate_content(prompt,generation_config=genai.types.GenerationConfig(
                temperature=0.3, top_k=25, top_p=0.95))
        return response.text.strip()
    except Exception as e:
        return f"❌ Error from Gemini: {str(e)}"
