# Start a loop at 99 and count backward to 1.
# range(99, 0, -1) decreases the number by 1 each iteration.
for bottles in range(99, 0, -1):

    # Display the current number of bottles.
    print(f"{bottles} bottles of beer on the wall.")
    print(f"{bottles} bottles of beer.")

    # Subtract one bottle after taking it down.
    remaining = bottles - 1

    # Check if there are bottles remaining.
    if remaining > 1:
        print(f"Take one down, pass it around, {remaining} bottles of beer on the wall.")

    # Use singular grammar when only one bottle remains.
    elif remaining == 1:
        print("Take one down, pass it around, 1 bottle of beer on the wall.")

    # Display the message when no bottles remain.
    else:
        print("Take one down, pass it around, no more bottles of beer on the wall.")

    # Print an empty line between verses for readability.
    print()

# Display the final verse after the loop finishes.
print("No more bottles of beer on the wall.")
print("No more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
