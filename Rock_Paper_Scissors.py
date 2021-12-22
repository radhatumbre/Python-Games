"""
ROCK PAPER SCISSOR GAME
"""

# importing module
import random

dict = {"1": "Rock", "2": "Paper", "3": "Scissors"}
rock = list(dict.keys())[0]
paper = list(dict.keys())[1]
scissors = list(dict.keys())[2]
comp = []
player = []
print("Welcome to the game!")
turns = int(input("How many rounds do you want to play?:"))
i = 0

if turns == 0:
    print("That's cool, have a good one!")
while i in range(0, turns):
    compTurn = random.choice(list(dict.keys()))
    print(f"Round No. {i + 1}")
    for key, value in dict.items():
        print(f"Select {key} for {value}: ")
    choice = input()
    userTurn = choice
    if (choice not in list(dict.keys())):
        print("Incorrect option selected. Try again...!!!")
        i -=1
    if compTurn == rock:
        if userTurn == scissors:
            print(f"Computer won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Won [{dict[compTurn]}]")
            player.append(f"Lost [{dict[userTurn]}]")
        elif userTurn == paper:
            print(f"You won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Lost [{dict[compTurn]}]")
            player.append(f"Won [{dict[userTurn]}]")
        elif userTurn == rock:
            print(f"Match Tied. Computer selected {dict[compTurn]} and you also selected {dict[userTurn]}")
            comp.append(f"Tied [{dict[compTurn]}]")
            player.append(f"Tied [{dict[userTurn]}]")
    elif compTurn == paper:
        if userTurn == rock:
            print(f"Computer won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Won [{dict[compTurn]}]")
            player.append(f"Lost [{dict[userTurn]}]")
        elif userTurn == scissors:
            print(f"You won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Lost [{dict[compTurn]}]")
            player.append(f"Won [{dict[userTurn]}]")
        elif userTurn == paper:
            print(f"Match Tied. Computer selected {dict[compTurn]} and you also selected {dict[userTurn]}")
            comp.append(f"Tied [{dict[compTurn]}]")
            player.append(f"Tied [{dict[userTurn]}]")
    elif compTurn == scissors:
        if userTurn == paper:
            print(f"Computer won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Won [{dict[compTurn]}]")
            player.append(f"Lost [{dict[userTurn]}]")
        elif userTurn == rock:
            print(f"You won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Lost [{dict[compTurn]}]")
            player.append(f"Won [{dict[userTurn]}]")
        elif userTurn == scissors:
            print(f"Match Tied. Computer selected {dict[compTurn]} and you also selected {dict[userTurn]}")
            comp.append(f"Tied [{dict[compTurn]}]")
            player.append(f"Tied [{dict[userTurn]}]")
    i += 1
    if (i == turns):
        compWinCount = sum("Won" in s for s in comp)
        userWinCount = sum("Won" in s for s in player)
        print("\n---------------------------------------------")
        print("Game No    Computer Result       Your Result")
        print("---------------------------------------------")
        for index in range(len(comp)):
            # print(item1, end = ", ")
            print(f"    {index + 1}      {comp[index]}       {player[index]}")
        if compWinCount > userWinCount:
            print(f'''
Final Result
Bad Luck! Computer is the Winner. Computor won {compWinCount} game(s) and you won {userWinCount} game(s)...!!!
Better Luck next time...!!!''')
        elif compWinCount < userWinCount:
            print(f'''
Final Result
Congratulations!You are the Winner. Computor won {compWinCount} game(s) and you won {userWinCount} game(s)...!!!''')
        else:
            print(f'''
Final Result
Match tied. Both won {compWinCount} game(s)...!!!''')

        while True:
            playagain = input("\nDo you want to play again? (Y/N): ")
            if playagain.upper() == "Y":
                turns = int(input("\nHow many games do you want to play?: "))
                i = 0
                comp = []
                player = []
                break
            elif playagain.upper() == "N":
                print("Thanks for playing...!!! Have a great day!")
                break
            else:
                print("Value should be either Y or N. Try again...!!!")
                continue

