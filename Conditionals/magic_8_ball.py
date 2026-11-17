import random

question = input("Ask the Magic 8 Ball a question: ")

responses = [
    "Yes, definitely.",
    "It is certain.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Cannot predict now.",
    "Don't count on it.",
    "My sources say no.",
    "Very doubtful."
]

answer = random.choice(responses)

print("Question:", question)
print("Magic 8 Ball:", answer)
