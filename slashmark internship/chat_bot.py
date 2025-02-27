from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from nltk.chat.util import Chat, reflections

def basic_chatbot():
    # Define pairs for pattern matching in basic chatbot
    pairs = [
        [r"hi|hello|hey", ["Hello! How can I help you today?"]],
        [r"what is your name\?", ["I am a chatbot created to assist you."]],
        [r"how are you\?", ["I'm just a program, but I'm functioning well. How can I assist you?"]],
        [r"(.*) your purpose\?", ["I am here to help you with your queries and provide information."]],
        [r"bye|exit|quit", ["Goodbye! Have a great day!"]],
    ]

    chatbot = Chat(pairs, reflections)
    print("Chatbot: Hi there! Start a conversation or type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot.respond(user_input))

def advanced_chatbot():
    # Create an advanced chatbot instance
    chatbot = ChatBot("AI Chatbot")

    # Train the chatbot with English data
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")

    print("Chatbot: Hi! How can I assist you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    print("Choose chatbot type:")
    print("1. Basic Chatbot (Rule-Based)")
    print("2. Advanced Chatbot (NLP-Based)")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        basic_chatbot()
    elif choice == "2":
        advanced_chatbot()
    else:
        print("Invalid choice. Exiting.")
