#Secret Number Guessing Game
import random

secret_num = random.randint(1,20)
gussed = True
while gussed:
    user_guess = int(input("Guess a number between 1 and 20: "))
    if user_guess > secret_num:
        print("Guess a lower number!")
    elif user_guess < secret_num:
        print("Guess a higher number!")
    elif user_guess == secret_num:
        print("You guessed correctly!")
        gussed = False
    else:
        print("Try Again!")


#Secret Number Gue1ssing Game (partners)
import random

player1Name = input("Player 1 Name: ")
player2Name = input("Player 2 Name: ")

secret_num = random.randint(1,20)
gussed = True
while gussed:
    player1Guess = int(input("{} Guess a number: ".format(player1Name)))
    if player1Guess > secret_num:
        print("Guess a Lower Number")
    elif player1Guess < secret_num:
        print("Guess a Higher Number")
    elif player1Guess == secret_num:
        print("{} guessed Correctly!".format(player1Name))
        gussed = False
    player2Guess = int(input("{} Guess a number: ".format(player2Name)))
    if player2Guess > secret_num:
        print("Guess a Lower Number")
    elif player2Guess < secret_num:
        print("Guess a Higher Number")
    elif player2Guess == secret_num:
        print("{} guessed Correctly!".format(player2Name))
        gussed = False

    
#Secret Number Guessing Game (partners/scoring)
import random

player1Name = input("Player 1 Name: ")
player2Name = input("Player 2 Name: ")

player1Attempts = 0
player2Attempts = 0

secret_num = random.randint(1,20)
guessed = True
while guessed:
    player1Attempts += 1
    player1Guess = int(input("{} Guess a number: ".format(player1Name)))
    if player1Guess > secret_num:
        print("guess a Lower Number")
    elif player1Guess < secret_num:
        print("guess a Higher Number")
    elif player1Guess == secret_num:
        print("{} guessed Correctly in {} Attempts!".format(player1Name,player1Attempts))
        guessed = False
    player2Attempts += 1
    player2Guess = int(input("{} Guess a number: ".format(player2Name)))
    if player2Guess > secret_num:
        print("guess a Lower Number")
    elif player2Guess < secret_num:
        print("guess a Higher Number")
    elif player2Guess == secret_num:
        print("{} guessed Correctly in {} Attempts!".format(player2Name,player2Attempts))
        guessed = False