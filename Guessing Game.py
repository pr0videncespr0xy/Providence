#Import random module
import random

#Print out greeting
print("Welcome to the guessing game!!!")

#set number of guesses and define a variable for the user winning
number_of_guess = 3
user_won = False

#Set answer
correct_answer = random.randint(1, 10)

#set number of guesses and set assign variable as integer
while number_of_guess > 0 :
    input("Guess my number : ")
    number_of_guess = int(number_of_guess)

#set logic for guessing game
    if number_of_guess == correct_answer:
        print("congratulations!!!")
        user_won = True
        break
    elif number_of_guess > correct_answer:
        print("you guessed too high")
    elif number_of_guess < correct_answer:
        print("you guessed too low")
        
#set the negation of the number of guesses after every attempt
    number_of_guess -= 1
    
#set the dialogue of the end result
if user_won == True:
    print("congratulations you have won")
else:
    print("Sorry, but you lose.")

