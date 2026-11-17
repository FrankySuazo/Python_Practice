#Keeping score below
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#Asking the first question
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
q1 = int(input("Enter your answer (1-2): "))

#Sorting the answer of question 1 for house score
if q1 == 1:
  gryffindor += 1
  ravenclaw += 1
elif q1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Wrong input")


#Asking the second question
print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
q2 = int(input("Enter your answer (1-4): "))

#Sorting the answer of question 2 for house score
if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor += 2
else:
  print("Wrong input")


#Asking the third question
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
q3 = int(input("Enter your answer (1-4): "))

#Sorting the answer of question 3 for house score
if q3 == 1:
  slytherin += 4
elif q3 == 2:
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:
  print("Wrong input")


#displaying each house score
print(f"Gryffindor: {gryffindor}")
print(f"Ravenclaw: {ravenclaw}")
print(f"Hufflepuff: {hufflepuff}")
print(f"Slytherin: {slytherin}")


#Finding out the score and displaying it as a result of which house you're in
highest_score = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if gryffindor == highest_score:
  print("Your house is Gryffindor!")
elif ravenclaw == highest_score:
  print("Your house is Ravenclaw")
elif hufflepuff == highest_score:
  print("Your house is Hufflepuff!")
elif slytherin == highest_score:
  print("Your house is Slytherin!")
else:
  print("Error, let's try this again")
