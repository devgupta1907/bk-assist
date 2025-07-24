from chatbot import ask_question

# Step 2: Ask question
while True:
    query = input("Ask: ")
    if query.lower() in ["exit", "quit"]:
        break
    response = ask_question(query)
    print(f"Bot: {response}\n")
