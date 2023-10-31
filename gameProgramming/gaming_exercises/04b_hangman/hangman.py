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

    print('missedLetters:', end = '')
    for eachLetter in missedLetters:
        print('eachLetter:', end = '')
# i = 0
# while i < 50:
#    word = getRandomWord(words)
#    print(word)
#    i += 1




















