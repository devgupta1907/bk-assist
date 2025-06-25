import json, uuid
from sentence_transformers import SentenceTransformer
import chromadb
from genai_api import beautify_answer

client = chromadb.PersistentClient(path="chroma_storage")
collection = client.get_or_create_collection("faq")
model = SentenceTransformer("all-MiniLM-L6-v2")


def append_new_faqs(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        faqs = json.load(f)

    added_count = 0
    for faq in faqs:
        question = faq["question"]
        raw_answer = faq["answer"]
        faq_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, question))

        try:
            existing = collection.get(ids=[faq_id])
            if existing["ids"]:
                continue
        except:
            pass

        beautified = beautify_answer(question, raw_answer)
        embedding = model.encode(question).tolist()

        collection.add(
            ids=[faq_id],
            documents=[beautified],
            embeddings=[embedding],
            metadatas=[{"question": question, "raw_answer": raw_answer}]
        )
        added_count += 1

    print(f"✅ Added {added_count} new FAQs to ChromaDB.")


if __name__ == "__main__":
    append_new_faqs("faq.json")