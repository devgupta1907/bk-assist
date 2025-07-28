__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import json
import chromadb
from sentence_transformers import SentenceTransformer
from config import load_config

def embed_json_to_chroma(json_path):
    config = load_config()
    client = chromadb.PersistentClient(path="chroma_storage_3")
    collection = client.get_or_create_collection(config["chroma_collection"])

    model = SentenceTransformer("all-mpnet-base-v2")

    with open(json_path, "r", encoding="utf-8") as f:
        faqs = json.load(f)

    for faq in faqs:
        qid = faq["id"]
        question = faq["question"]
        answer = faq["answer"]
        embedding = model.encode(question).tolist()

        try:
            collection.delete(ids=[qid])
        except Exception:
            pass

        # try:
        #     existing = collection.get(ids=[qid])
        #     if existing["ids"]:
        #         continue
        # except:
        #     pass

        collection.add(
            ids=[qid],
            embeddings=[embedding],
            documents=[answer],
            metadatas=[{"question": question}]
        )
        print(f"✅ {qid} Embedded Successfully")

    print(f"✅ Embedded {len(faqs)} FAQs from '{json_path}' into ChromaDB.")


if __name__ == "__main__":
    embed_json_to_chroma("data/mac_ios_queries.json")