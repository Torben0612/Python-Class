import random

coins = random.randint(3,20)
print("Take turns removing 1, 2, or 3 coins. You win if you take the last coin.")

player1Name = input("Player 1 whats your name? ")
player2Name = input("Player 2 whats your name? ")

gameRunning = True


while gameRunning:
    player1Turn = True
    while player1Turn:
        print("There are", coins, "coins remaining.")
        player1Coins = int(input("{} How many coins do you take?".format(player1Name)))
        if player1Coins > 3:
            print("That's not a legal move. Try again.")
        elif player1Coins <= 0:
            print("That's not a legal move. Try again.")
        elif player1Coins > coins:
            print("That's not a legal move. Try again.")
        else:
            coins = coins - player1Coins
            if coins == 0:
                winner = player1Name
                gameRunning = False
                player2Turn = False
                player1Turn = False
                print("No more coins left")
                print("{} wins".format(player1Name))
                print("{} loses".format(player2Name))
            else:
                player2Turn = True
                player1Turn = False

        
    while player2Turn:
        print("There are", coins, "coins remaining.")
        player2Coins = int(input("{} How many coins do you take?".format(player2Name)))
        if player2Coins > 3:
            print("That's not a legal move. Try again.")
        elif player2Coins <= 0:
            print("That's not a legal move. Try again.")
        elif player2Coins > coins:
            print("That's not a legal move. Try again.")
        else:
            coins = coins - player2Coins
            if coins == 0:
                winner = player2Name
                gameRunning = False
                player2Turn = False
                player1Turn = False
                print("No more coins left")
                print("{} wins".format(player2Name))
                print("{} loses".format(player1Name))
            else:
                player2Turn = False
                player1Turn = True