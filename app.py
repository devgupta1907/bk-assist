import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb


@st.cache_resource
def get_db():
    client = chromadb.PersistentClient(path="chroma_storage")
    return client.get_or_create_collection("faq")

@st.cache_resource
def get_encoder():
    return SentenceTransformer("all-MiniLM-L6-v2")

collection = get_db()
model = get_encoder()

st.set_page_config(page_title="BKAssist", page_icon="📘")
st.title(":blue_book: Hii, I am BKAssist")


question = st.text_input("Ask your question:")
if question:
    query_vec = model.encode(question).tolist()
    results = collection.query(query_embeddings=[query_vec], n_results=1)
    if results["documents"]:
        st.markdown("### 💡 Answer")
        st.write(results["documents"][0][0])
    else:
        st.warning("Sorry, I couldn't find an answer for that question.")






# # app.py

# import streamlit as st
# import pickle
# import numpy as np
# from sentence_transformers import SentenceTransformer

# # Load index and model
# with open("faq_index.pkl", "rb") as f:
#     index, data, model_name = pickle.load(f)

# model = SentenceTransformer("all-MiniLM-L6-v2")

# st.title("🧠 FAQ Assistant")
# st.write("Ask your question below:")

# query = st.text_input("Your Question")

# if query:
#     query_embedding = model.encode([query])
#     D, I = index.search(np.array(query_embedding).astype("float32"), k=1)
#     matched = data[I[0][0]]

#     st.subheader("📌 Best Match:")
#     st.markdown(f"**Q:** {matched['question']}")
#     st.markdown(f"**A:** {matched['answer']}")
