# This program acts as a number guessing game 
# The program will ask the user to input a number 'x' | A random number will be generated in the range of 1 & 'x'
# When the user guesses the correct number, a 'Congrats' statement will be printed to the user telling them they guessed the correct random number

import random 

def guess(x):
    # The random number will be in the range of 1 & 'x' 
    random_number = random.randint(1, x)

    # Assigning an integer value to our guess variable 
    guess = int

    # While loop will continue to run until the user guesses the random number that is in the range of 1 & 'x' (user supplied number)
    while guess != random_number:
        # Reassiging guess var to hold an integer value which is input by the user
        guess = int(input(f"Guess a number between 1 and {x}: \n")) 
        
        if guess < random_number:
            print("Too low. Try again!")
        elif guess > random_number:
            print("Too high. Try again!")
    
    # Prints "Congrats" to the user when the random number is guessed correctly | The while loop above continues to run until the user guesses the number correctly.
    # This is why the "Congrats" statement is placed after the while loop 
    print(f"Congrats. You have guessed the random number {random_number}!")

# Calling our function with a value of '10'
# The program will select a random number in the range of 1 & 10 
guess(10)
