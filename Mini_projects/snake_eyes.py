# Import the random module to simulate rolling dice.
import random

# Initialize both dice with a starting value of 0.
die1 = 0
die2 = 0

# Keep rolling until both dice show 1 (Snake Eyes).
while die1 != 1 or die2 != 1:

    # Generate a random number between 1 and 6 for each die.
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Display the result of each roll.
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print()

# The loop ends when both dice equal 1.
print("Snake Eyes! Both dice rolled a 1!")
