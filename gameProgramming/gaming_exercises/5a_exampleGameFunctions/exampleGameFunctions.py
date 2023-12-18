# Example Game Functions Project, Corey Battle, v0.0
import random

def playAgain():
    userChoices = ['yes']
    print("Do you want to play again? Yes or No?:\n")
    if userChoices:
        userChoices = 'si' or 's'
        return input().lower().startswith('y')
    else:
        print("great game")

playAgain()

def startGame():
    userChoices = ['yes']
    print("Are you ready to start the game?(yes or no):\n")
    if userChoices:
        userChoices = input().upper()
        userChoices = 'si' or 's'
    else:
        print("No, leave me alone")

def shotMade():
    choices = ['r', 't', 'z']
    computerChoice = random.choice(choices)

    userChoice = input("enter one of the folowing(R,T,Z);\n").lower()

    if userChoice not in choices:
        print("Pick a choice buddy")
        shotMade()

    print("CPU choice:", computerChoice)
    print("You chose:", userChoice)

