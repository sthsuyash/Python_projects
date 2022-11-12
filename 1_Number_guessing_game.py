# The program selects a random number between two numbers, and the user guesses the correct number.

import random
import sys

n = int(sys.argv[1]) or 100
ran = random.randint(1, n)
guess = int(input(f"Guess a number between 1 and {n}: "))

guess_count = 1

while ran != guess and guess_count < 10:
    if ran > guess:
        print("Too low")
        print("You have {} guesses left".format(10 - guess_count))
        guess = int(input("Guess a number between 1 and 100: "))
        guess_count += 1

    elif ran < guess:
        print("Too high")
        print("You have {} guesses left".format(10 - guess_count))
        guess = int(input("Guess a number between 1 and 100: "))
        guess_count += 1

    else:
        break

if guess_count >= 10:
    print("You lose")
else:
    print("You got it! You did it in {} guesses".format(guess_count))
