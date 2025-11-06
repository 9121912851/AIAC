# Simple Chatbot in Python

def chatbot():
    print("🤖 Hello! I'm your support bot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Bot: Goodbye! Have a great day!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hello there! How can I help you today?")
        elif 'help' in user_input:
            print("Bot: Sure! Please tell me what you need help with.")
        elif 'order' in user_input:
            print("Bot: Can you provide your order number?")
        else:
            print("Bot: I'm sorry, I didn't understand that. Can you rephrase?")

# Run the chatbot
chatbot()