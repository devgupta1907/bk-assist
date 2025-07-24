import streamlit as st
from chatbot import ask_question

st.set_page_config(page_title="BKAssist Chatbot", page_icon="🤖")
st.title("📘 BK AI – BookKeeper AI Support")

question = st.text_input("Ask your question:")

if question:
    with st.spinner("Thinking..."):
        answer = ask_question(question)
        st.markdown(f"**💬 Answer:**\n\n{answer}")