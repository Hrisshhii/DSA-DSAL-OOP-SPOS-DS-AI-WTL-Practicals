responses = {
    "hello": "Hello! I'm your Movie Chatbot.",
    "hi": "Hey there! Ready for movie suggestions?",
    "who are you": "I am a Movie Recommendation Chatbot.",

    "action": "Action movies: John Wick, The Dark Knight.",
    "comedy": "Comedy movies: 3 Idiots, Superbad.",
    "romance": "Romantic movies: Titanic, La La Land.",
    "horror": "Horror movies: The Conjuring, Insidious.",
    "sci-fi": "Sci-Fi movies: Interstellar, Inception.",

    "sad": "Try watching Forrest Gump.",
    "happy": "Watch 3 Idiots or ZNMD.",

    "bye": "Goodbye! Enjoy your movies!"
}

print("Chatbot: Hello! Type 'bye' to exit.\n")

while True:
    user=input('\nYou: ').lower()
    found=False
    for key in responses:
        if key in user:
            print('\nChatbot: ',responses[key])
            found=True
            if key=='bye':
                exit()
            break
    if not found:
        print("Chatbot: Sorry, I don't have the answer!")
