__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb
from sentence_transformers import SentenceTransformer
from config import load_config

def retrieve_similar(question, top_k=3):
    config = load_config()
    # client = chromadb.PersistentClient(path="chroma_storage_2")
    client = chromadb.PersistentClient(path="chroma_storage_3")
    collection = client.get_collection(config["chroma_collection"])

    # model = SentenceTransformer("all-MiniLM-L6-v2")
    model = SentenceTransformer("all-mpnet-base-v2")
    q_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[q_embedding],
        n_results=top_k
    )
    return results["documents"][0], results["metadatas"][0]
