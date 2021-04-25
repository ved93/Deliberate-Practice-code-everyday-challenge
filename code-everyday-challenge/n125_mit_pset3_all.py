# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"
from pathlib import Path


BASE_DIR= str(Path(__file__).resolve().parent)
# print(str(os.getcwd())+'//MOOC//')

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(BASE_DIR+'/'+WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # for l in lettersGuessed:
    for char in secretWord:
      if char not in lettersGuessed:
        return False

    return True



# secretWord = 'apple'  
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print(isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ''
    for char in secretWord:
        if char not in lettersGuessed:
          s=s+'_'
        else:
          s=s+char

    return s  

# print(getGuessedWord(secretWord, lettersGuessed))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string

    string  = string.ascii_lowercase

    tmp = ''
    for i in string:
      if i not in lettersGuessed:
        tmp+=i
    return tmp

# print(getAvailableLetters(lettersGuessed))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print ("Welcome to the game, Hangman!")
    print ("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")

    lettersGuessed = ''
    guessesLeft = 8
    print ("------------")

    # mistakesMade = 0
    # lettersGuessed = []

    # while 8 - mistakesMade > 0:
    #     if isWordGuessed(secretWord, lettersGuessed) == True:
    #         print('------------')
    #         print('Congratulations, you won!')
    #         break
    #     else:
    #     	print('------------')
    #     	print('You have', 8 - mistakesMade, 'guesses left.')
    #     	print('Available letters:', getAvailableLetters(lettersGuessed))
    #     	guess = str(input('Please guess a letter:')).lower()
    #     	if guess in secretWord and guess not in lettersGuessed:
    #     		lettersGuessed.append(guess)
    #     		print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
    #     	elif guess in lettersGuessed:
    #     		print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
    #     	elif guess not in secretWord:
    #     		print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
    #     		lettersGuessed.append(guess)
    #     		mistakesMade += 1
    #     if 8 - mistakesMade == 0:
    #     	print('------------')
    #     	print('Sorry, you ran out of guesses. The word was', secretWord)
    #     	break
    #     else:
    #     	continue


    while True:
        print ("You have " + str(guessesLeft) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        print ("------------")
        if guessesLeft <= 0:
            print ("Sorry, You've ran out of guesses. The word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations! You've won!")
            break






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
