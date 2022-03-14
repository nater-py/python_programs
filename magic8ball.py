import random 

name = "Nate" # Name of User asking Magic 8-Ball

question = "Is the sky currently blue?" # User's Question
answer = "" # 8-Balls Answer

random_number = random.randint(1,9) # Random integer generated between 1-9 

# Creating if/elif/else statements to assign different answers that correspond to a random integer

if random_number == 1:
  answer = "Yes - definitely."

elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

# Testing Magic 8-Balls Responses

if name == "":
  print(f"Question: {question}") # Question is asked
  print(f"Magic 8-Balls answer: {answer}") # 8-Ball Responds to question 
else:
  print(f"{name} asks: {question}")
  print(f"Magic 8-Balls answer: {answer}")
  
