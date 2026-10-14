def chatbot():
    print("🤖 Chatbot: Hello! Welcome to my chatbot.")
    print("🤖 Chatbot: You can ask me something or type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user_input in ["what is your name", "your name"]:
            print("Bot: I'm a simple Python chatbot.")

        elif user_input == "what is the weather":
            print("Bot: I can't check live weather, but you can check a weather website!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day! 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that. Try asking something else!")


chatbot()