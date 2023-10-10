# Select the secret number from a given range. 
# Player must guess the number. 
# Compare guess to the secret number. 
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left.
    # Tell them if too high/ too low
# What happens if the guess is right
    # Tell them guess is correct.
    # Award a point.
# What happens if the player runs out of guesses?
    # Tell plauer round has been lost.
    # Award point to CPU. 
# Check to see if player or CPU has >= 3 points, if so they win

import random # Import random modules to our code

# DECLARATIONS
secretNumber = -1
playerScore = -1
cpuScore = 0
numGuesses = 0
playerName = ""
difficulty = "nooby"
rangeMin = 0
rangeMax = 6
numAttempts = 5
difficulty = "norm"
rangeMin = 7
rangeMax = 13
numAttempts = 4
difficulty = "sweaty"
rangeMin = 14
rangeMax = 20
numAttempts = 3


print("""
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    |                               |
    |      Guess a Number           |
    |      Corey Battle             |
    |       2023                    |
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*

    """)

# CPU SECRET NUMBER GENERATION
secretNumber = random.randint(0, 20)
print(secretNumber)

# GAME LOOP
difficulty = input("Choose your difficulty.\n")

print("You need to guess a number from 0 to 20 and you have four guesses.\nIf you guess it right you get a point.\nIf you can't guess it right the cpu gets a point")

print("You have chosen {nooby}Easiest game mode, suggest for new players")

print("You have chosen {norm}Normal game mode, not hard or easy")
    
print("You have chosen {sweaty}Hardest game mode, play if you want a challenges")


# Use input() to store difficulty in difficulty variable.
# assign values to numAttempts, rangeMin, and rangeMax based on choice.

while playerScore != 3 and cpuScore != 3 : # START THE MATCH (GAME)
    # Difficulty code needs to be BEFORE the round starts
    # pass -- Tells Python to skip this block of code. 
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    # secretNumber = random.randint(rangeMin, rangeMax)
    # Whenever you assign a specific value to something, it's called "hard coded"
    #print(secretNumber)
    # ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND

    numGuesses = 0
    for guesses in range(4): # START THE ROUND! 
        print(f"You have {4 - numGuesses} guesses remaining.\n")
        playerGuess = input("Type a number from 0 to 20 and press ENTER.\n")
        # input() saves all data as a STRING by default.
        # int() will convert to an INTERGER
        # float() will convert to a FLOAT
        print(f"You have chosen {playerGuess}. Let's see if you're right!\n")
        if playerGuess == secretNumber: 
            print("Whoa dude, what a guess! You got it!\n")
            playerScore += 1
            break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN!
        else: 
            print(" You did not guess correctly.\n")
            if playerGuess == secretNumber: 
                print("Your guess is too high.\n")
            else:
                print("Your guess is too now.\n")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses.\n")
if playerScore >= 3:
    print("Winner, winner, chicken dinner! You scored 3 points first!\n")
else:
    print("Yo, you lost to a computer. You are a scrub.\n")