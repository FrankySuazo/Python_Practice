# Ask the user how many steps the staircase should have.
steps = int(input("Enter the number of steps: "))

# Loop from 1 up to the total number of steps.
# Each iteration represents one level of the staircase.
for i in range(1, steps + 1):

    # Multiply the "#" symbol by the current step number.
    # Each new row contains one more "#" than the previous row.
    print("#" * i)
