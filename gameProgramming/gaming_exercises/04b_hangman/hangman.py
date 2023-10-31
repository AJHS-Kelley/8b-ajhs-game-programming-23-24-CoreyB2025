# Hangman Game by Corey Battle, v0.0

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
                 
i = 0
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1





