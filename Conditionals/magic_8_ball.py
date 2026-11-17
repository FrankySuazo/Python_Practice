# Import the random module to randomly select an answer.
import random

# Ask the user to enter a question and store it in a variable.
question = input("Ask the Magic 8 Ball a question: ")

# Create a list containing all possible Magic 8 Ball responses.
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

# Use random.choice() to select one response from the list.
# The selected response is stored in the variable 'answer'.
answer = random.choice(responses)

# Display the user's original question.
print("Question:", question)

# Display the randomly selected Magic 8 Ball response.
print("Magic 8 Ball:", answer)
