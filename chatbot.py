import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

#enviorment building
# Define pairs of patterns and responses (possible response)
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Greetings!"]
    ],
    [
        r"what is your name?",
        ["Bot :)"]
    ],
    [
        r"how are you?",
        ["I'm just a program, but thanks for asking!", "Doing well, how about you?"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help you! What do you need help with?","What is it?"]
    ],
    [
        r"quit",
        ["Bye! Have a great day!"]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Starting convo
print("Bot: Hi there! Type 'quit' to exit.")
while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        print("Bot: Bye! Have a great day!")
        break
    response = chatbot.respond(user_input)

    # Attempt to get a response
    matched = False
    for pattern, responses in pairs:
        if nltk.re.search(pattern, user_input):
            response = responses[0]  
            matched = True
            break

    # DEFAULT RESPONSE
    if not matched:
        response = "Sorry, I don't understand that."

    print("Bot:", response)
  