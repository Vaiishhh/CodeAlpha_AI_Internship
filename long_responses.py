import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Sounds about right.",
                "I am doing good and you?",
                "I am a Chatbot, here to help you",
                "Why does water never laugh at jokes? It isn't a fan of dry humor!",
                "Bye! Have a great day!",
                "What does that mean?"][
        random.randrange(8)]
    return response