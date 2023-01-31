# Program design based on "Bagels" by Al Sweigart al@inventwithpython.com
# Implementation is my own


import random

# Constants
MAX_VALUE = 999
MAX_GUESSES = 10

def printIntro():
    # Intro
    print("\n \nBagels, a deductive reasoning game: \n")
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:     That means:")
    print("Pico            One digit is correct but in the wrong position.")
    print("Fermi           One digit is correct and in the right position.")
    print("Bagels          No digit is correct.")
    print("I have thought up a number.")
    print("You have " + str(MAX_GUESSES) + " guesses to get the correct number.")

def numberStringFormat(num):
    if num < 10:
        numStr = "00" + str(num)
    
    elif num < 100:
        numStr = "0" + str(num)
    
    else:
        numStr = str(num)
    
    return numStr

def setCorrectNumber():
    # Set random number for correctNumber
    random.seed()
    correctNumber = random.randrange(0, MAX_VALUE + 1)
    correctNumberStr = numberStringFormat(correctNumber)
    return correctNumberStr

def guessValidationInteger(userGuess):    
    intFlag = False
    while intFlag == False:
        try:
            userGuess = int(userGuess)
        except:
            print("Please guess a 3-digit number (<= 999)")
            userGuess = input("> ")
        
        intFlag = isinstance(userGuess, int)
    
    return userGuess

def guessValidationUnder100(userGuess):
    userGuess = guessValidationInteger(userGuess)
    
    while userGuess > MAX_VALUE:
        print("Please guess a 3-digit number (<= 999)")
        userGuess = input("> ")
        userGuess = guessValidationInteger(userGuess)
    
    return userGuess

def getUserInput():
    guess = input("> ")
    guessInt = guessValidationUnder100(guess)
    guessStr = numberStringFormat(guessInt)
    return guessStr

def playAgainValidation(playAgain):
    playAgainList = ['y', 'n']
    while playAgain not in playAgainList:
        print("Please enter \'y\' or \'n\'")
        playAgain = input()
    return playAgain

def guessNum(correctNumberStr):
    correctFlag = False
    guessCounter = 1
    
    while correctFlag == False and guessCounter <= MAX_GUESSES:
        print("Guess #"+str(guessCounter)+":")
        guessStr = getUserInput()
        correctFlag = checkGuess(correctNumberStr, guessStr, correctFlag)
        guessCounter += 1
        
    if correctFlag == True:
        print("You got it!")
        
    else:
        print("You are out of guesses. Nice try!")
        
    print("The correct number was: " + correctNumberStr)


def checkGuess(correctNumberStr, guessStr, correctFlag):
    clue = ""
    if guessStr == correctNumberStr:
        correctFlag = True
        return correctFlag
    
    incorrectFlag = True
    for i in range(len(guessStr)):
        if guessStr[i] in correctNumberStr:
            if guessStr[i] == str(correctNumberStr[i]):
                clue += "Fermi "
                incorrectFlag = False
            
            else:
                clue += "Pico "
                incorrectFlag = False
    
    if incorrectFlag == True:
        print("Bagels")
    print(clue)
    return correctFlag


def main():
    
    playAgain = "y"
    
    while playAgain == "y":
        printIntro()
        correctNumberStr = setCorrectNumber()
        guessNum(correctNumberStr)
        
        playAgain = input("Would you like to play again? " )
        playAgain = playAgainValidation(playAgain)

if __name__ == '__main__':
    main()