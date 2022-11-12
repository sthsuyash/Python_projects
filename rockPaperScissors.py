"""
    Game of Rock,Paper & Scissors in Python
    By: Suyash Shrestha
"""
from random import choice
import time

print("\n\n")
print("         |            |  _________            _______   ______            ________  ")
print("         |     /\     | |          |         |         |      | |\    /| |          ")
print("         |    /  \    | |          |         |         |      | | \  / | |          ")
print("         |   /    \   | |_______   |         |         |      | |  \/  | |_______   ")
print("         |  /      \  | |          |         |         |      | |      | |          ")
print("         | /        \ | |          |         |         |      | |      | |          ")
print("         |/          \| |_________ |________ |________ |______| |      | |________  \n\n")
print("-----------------------------Game of Rock, Paper and Scissors---------------------------------")

""" function definition section """
# function to print the loading type dots after quitting
def sleep_print(n):
    i = 0
    while i < n:
        time.sleep(0.4)
        print(".", end='')
        i += 1


# function to show the score of user and computer
def showScore():
    print(f'Your score: {user_score}\tComputer score: {computer_score}')

""" section ends """

# run the game until the condition is satisfied 
while True:
    # declare two variables for user and computer each to store the scores as the game is played 3 times before winner is decided
    user_score = 0
    computer_score = 0
    # to count the number of times the game has been won by either side
    count = 1

    # play the game 3 times
    while count <= 3:
        choices = ["ROCK", "PAPER", "SCISSORS"]
        user_choice = input("\nEnter your choice: ").upper()  # take input from user and make it uppercase
        computer_choice = choice(choices)

        # check if the choice is not in the given set of choices 
        if user_choice not in choices:
            print("Please enter any of the following: ('ROCK', 'PAPER', 'SCISSORS'): ")
            user_choice = input("Enter your choice: ")
        print("Computer Choice: ", computer_choice)

        if (user_choice == computer_choice):
            count += 0  #dont increment anybody's score as it is draw
            # and also the global score count
            showScore()
        elif ((user_choice == "ROCK" and computer_choice == "SCISSORS")
              or (user_choice == "PAPER" and computer_choice == "ROCK")
              or (user_choice == "SCISSORS" and computer_choice == "PAPER")):
            count += 1
            user_score += 1
            showScore()
        else:
            count += 1
            computer_score += 1
            showScore()

    if (user_score == 3):
        print("\n\nYou win!!\n")
    else:
        print("\n\nYou lose!!😢\n")

    play_again = input("Do you want to play again? (y/n) > ").lower()
    if play_again != "y":
        print("Play again soon.\nExiting.", end='')
        sleep_print(5)
        break
