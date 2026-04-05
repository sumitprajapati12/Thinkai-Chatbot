#Rule Based AI Python ChatBot

print("Hello! Welcome to ThinkAI-ChatBot")
print("You can ask me basic questions, Type 'bye' to exit.")

responses = {
    "hello": "Hi, Welcome. How Can I help you?",
    "hi": "Hi, Welcome. How Can I help you?",
    "how are you": "I am very fine.Thank you",
    "who are you": "I am smart AI chatbot",
    "happy": "Great to hear that",
    "motivate me": "keep going. Every bug of your project makes you a better developer",
    "bye": "Goodbye!"
}

# Method/Function
def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
       if eachKey in userQuestion:
          return responses[eachKey]

    return "I am not able to tell that yet. I am still in learning mode"

# take user input
while True:
    userInput= input("Please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break