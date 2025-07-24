from retriever import retrieve_similar
from llm import generate_answer

def ask_question(question):
    contexts, _ = retrieve_similar(question)
    if not contexts or all(c.strip() == "" for c in contexts):
        return "Sorry, I do not know about this. Please contact Support Team."
    return generate_answer(question, contexts)
