def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hello! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm doing well! Thanks for asking.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")
if __name__ == "__main__":
    chatbot()
