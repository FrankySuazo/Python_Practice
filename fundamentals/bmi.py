# Ask the user to enter their weight in kilograms.
# Convert the input from a string to a float.
weight = float(input("Enter your weight in kilograms: "))

# Ask the user to enter their height in meters.
height = float(input("Enter your height in meters: "))

# Calculate Body Mass Index (BMI).
# Formula: BMI = weight / height squared.
bmi = weight / (height ** 2)

# Display the calculated BMI rounded to two decimal places.
print(f"Your BMI is: {bmi:.2f}")

# Determine the BMI category using conditional statements.
if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal weight")

elif bmi < 30:
    print("Overweight")

else:
    print("Obesity")
