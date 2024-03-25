#Secret Number Guessing Game
import random
secret_num = random.randint(1,20)
guessedCorrect = False
while not guessedCorrect:
    user_guess = int(input("Gues a number between 1 and 20"))
    if user_guess == secret_num:
        print("Your guessed Correctly!")
        guessedCorrect = True
    else:
        print("Try Again")


#Secret Number Guessing Game (partners)

import random

player1Name = input("Player 1 Name: ")
player2Name = input("Player 2 Name: ")
secret_num = random.randint(1,5)
guessedCorrect = False
while not guessedCorrect:
    player1Guess = int(input("Player 1 Guess a number"))
    if player1Guess == secret_num:
        print("{winingPlayer} guessed Correctly!".format(winingPlayer=player1Name))
        guessedCorrect = True
    else:
        player2Guess = int(input("Player 2 Guess a Number"))
    if player2Guess == secret_num:
        print("{winingPlayer} guessed Correctly!".format(winingPlayer=player2Name))
        guessedCorrect = True
    else:
        print("Try again")

    
#Secret Number Guessing Game (partners/scoring)
import random

player1Name = input("Player 1 Name: ")
player2Name = input("Player 2 Name: ")

player1Attempts = 0
player2Attempts = 0

secret_num = random.randint(1,5)
guessedCorrect = False
while not guessedCorrect:
    player1Guess = int(input("Player 1 Guess a number"))
    player1Attempts += 1
    if player1Guess == secret_num:
        print("{winingPlayer} guessed Correctly in {attemptNumber} attempts".format(winingPlayer=player1Name, attemptNumber=player1Attempts))
        guessedCorrect = True
    else:
        player2Guess = int(input("Player 2 Guess a Number"))
        player2Attempts += 1
    if player2Guess == secret_num:
        print("{winingPlayer} guessed Correctly in {attemptNumber} attempts".format(winingPlayer=player2Name, attemptNumber=player2Attempts))
        guessedCorrect = True
    else:
        print("Try again")