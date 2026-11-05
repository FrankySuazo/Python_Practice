#Function to select items
def get_item(x):
  if x == 1:
    return "🍔 Cheeseburger"
  elif x == 2:
    return "🍟 Fries"
  elif x == 3:
    return "🥤 Soda"
  elif x == 4:
    return "🍦 Ice Cream"
  elif x == 5:
    return "🍪 Cookie"
  else: 
    return "Try again"

#The Menu for the user see to make selection 
def welcome():
  print("Welcome to Fast Food place")
  print("This is the menu:")
  print("1: 🍔 Cheeseburger")
  print("2: 🍟 Fries")
  print("3: 🥤 Soda")
  print("4: 🍦 Ice Cream")
  print("5: 🍪 Cookie")
  
#The call for the menu to be shown
welcome()  

#The user input
user_order = int(input("What number is your order?"))

#The connection of the user input to the function selection called: get_item
print(get_item(user_order))
