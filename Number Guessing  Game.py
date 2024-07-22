correct_number = 5
number_of_guesses = 3

guess = input("What do you think the number is?")
if int(guess) <= correct_number:
    print("That guess was too low")
    int(number_of_guesses) - 1
    print(guess)

if int(guess) >= correct_number:
    print("That guess was too high")
    int(number_of_guesses) - 1
    print(guess)

if number_of_guesses == 0:
    print("You ran out of guesses! Better luck next time!")

print(guess)