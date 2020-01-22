import random

#game set up
print("Welcome to the guessing game partner of mine")
number_of_guesses = 3 #User has 3 guesses before losing the game

#Computer guesses a random int between 1 and 10
correct_answer = random.randint(1, 10)

while number_of_guesses > 0:
    #User guesses the number
    user_guess = input("guess my number: ")
    user_guess = int(user_guess)

    #Computer tells user if the guess was too high or too low
    if user_guess == correct_answer:
        print("Good guess!")
        print("You are right! Congratulations!!!!")
        user_won = True
        break
    elif user_guess > correct_answer:
        print("You went over try, something a little lower")
    elif user_guess < correct_answer:
        print("WOAH DERE, Too low scrub, try again")

    number_of_guesses -= 1

if user_won == True:
    print("Congrats friend you have won!!")
else:
    print("Sorry buddy, but you lose.")

