# Hangman Game by Corey Battle, v0.0
import random
words = 'apple fun run sun bum hum calm pat rice cool potato tomato gringo missle pasta plane insane checker blaster infamous mitochondria phytoplankton piemountaindog epitome coincidental'.split()

# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
     +---+
          |
          |
          |
    ======''', '''
     +---+
     O    |
          |
        
    ======''', '''
     +---+
     O    |
     |    |
          |
    ======''', '''
    +---+
     O    |
    /|    |
          |
    ======''', '''
    +---+
     O    |
    /|\   |
          |
    ======''', '''
     +---+
     O    |
    /|\   |
    /     |
    ======''', '''
     +---+
     O    |
    /|\   |
    / \   |
    ======''']
                 
# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordList) -1)
    # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('missedLetters:', end = ' ')
    for eachLetter in missedLetters:
        print('eachLetter:', end = ' ')
      print()
      
      blanks = '_' * len(secretWord)

      # Replace Banks with Correct Letters
      for i in range(len(secretWord)):
            if secretWord[i] if correctLetters: 
                blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

      for letter in blanks:
          print(letter end = ' ')
      print()


def getGuess(alreadyGuessed):
      while True: 
            print('Please guess a letter and press enter.')
            guess = input
            guess = guess.lower()
            if len(guess) != 1:
                  print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                  print('Letter has been guesses already, try again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                  print('please guess a LETTER from the English alphabet.')
            else:
                  return guess

def playAgain():
      print('Do you want to play again? Yes or No?')
      return input().lower().startswith('y')





# i = 0
# while i < 50:
#    word = getRandomWord(words)
#    print(word)
#    i += 1




















