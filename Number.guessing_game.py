"""
Number Guessing Game
"""

# importing the module
import random

# keeping the score of every game
attempts_list = []

# function to record the high score
def score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))

def game():
    # Picking the number
    answer = int(random.randint(1, 100))

    # Starting the Game
    print("Hello Player! Welcome to the Number Guessing Game")
    name = input("What is your name :")
    wanna_play = input(f"Hi, {name}, would you like to play the guessing game? (Enter Yes/No):")
    attempts = 0
    score()

    # whether player wants to play or not
    while wanna_play.upper() == "YES":
        try:
            guess = input("Pick a number between 1 and 100: ")

            # number shouldn't be invalid
            if int(guess) < 1 or int(guess) > 100:
                raise ValueError("Please guess a number within the given range")

            if int(guess) == answer:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print(f"It took you {attempts} attempts")
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                score()
                answer = int(random.randint(1, 100))

                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    break

            elif int(guess) > answer:
                print("It's lower")
                attempts += 1

            elif int(guess) < answer:
                print("It's higher")
                attempts += 1

        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("\nThat's cool, have a good one!")

if __name__ == '__main__':
    game()
