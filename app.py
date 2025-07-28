import streamlit as st
from chatbot import ask_question
import random

cool_info = [
    "Thinking... By the way, do you know when BookKeeper was founded? It was in 2011 🥳!",
    "Searching... Make sure you are on the latest version of BookKeeper for the best experience! 🚀",
    "Hold on... Did you know that BookKeeper is the self-sustained application?",
    "Just a moment... BookKeeper has been helping users since 2011! 🎉",
    "Hang tight... Till then, Keep a note of BookKeeper Suuport Team WhatsApp Number - +91 9999176746 💬",
    "Almost there... Remember, you can always reach out to us via Email, WhatsApp, or Call! 📞"
]
random_index = random.randint(0, len(cool_info) - 1)

st.set_page_config(page_title="BKAssist Chatbot", page_icon="🤖")
st.title("📘 BK AI – BookKeeper AI Support")

question = st.text_input("Ask your question:")

if question:
    with st.spinner(f"{cool_info[random_index]}"):
        answer = ask_question(question)
        st.markdown(f"**💬 Answer:**\n\n{answer}")