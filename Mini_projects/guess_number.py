# Import the random module to generate a random number.
import random

# Generate a random number between 1 and 10.
secret_number = random.randint(1, 10)

# Initialize a variable to store the user's guess.
guess = 0

# Continue the game until the user guesses correctly.
while guess != secret_number:

    # Ask the user to enter a number.
    # Convert the input from a string to an integer.
    guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess is lower than the secret number.
    if guess < secret_number:
        print("Too low! Try again.")

    # Check if the guess is higher than the secret number.
    elif guess > secret_number:
        print("Too high! Try again.")

    # If neither condition is true, the guess is correct.
    else:
        print("Congratulations! You guessed the number!")
