import math
import random

correct_number = 5
number_of_guesses = 3
wrong_guess = 1

while number_of_guesses != 0:
    guess = input("What do you think the number is? ")
    if int(guess) == correct_number:
        print("Correct! Nice Job!")
        quit()
    elif int(guess) >= correct_number:
        print("That guess was too high! Try again")
        number_of_guesses -= wrong_guess
        print(f"Careful! You only have {number_of_guesses} tries left!")
    elif int(guess) <= correct_number:
        print("That guess was too low! Try again")
        number_of_guesses -= wrong_guess
        print(f"Careful! You only have {number_of_guesses} tries left!")
else:
    print("You ran out of guesses! Better luck next time!")
    quit()