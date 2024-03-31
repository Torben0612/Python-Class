coins = 22
print("Take turns removing 1, 2, or 3 coins. You win if you take the last coin.")

player1Name = input("Player 1 whats your name? ")
player2Name = input("Player 2 whats your name? ")

gameRunning = True


while gameRunning:
    player1Turn = True
    while player1Turn:
        print("There are", coins, "coins remaining.")
        player1Coins = int(input(player1Name "How many coins do you take?"))
        if player1Coins != 1 or 2 or 3 or player1Coins > coins:
            print("That's not a legal move. Try again.")
        coins = coins - player1Coins
        if coins == 0:
            winner = player1Name
            gameRunning = False
            player2Turn = False
        else:
            player2Turn = True
            player1Turn = False

        
    while player2Turn:
        print("There are", coins, "coins remaining.")
        player2Coins = input(int(player2Name, "How many coins do you take?"))
        if player2Coins != 1 or 2 or 3 or player2Coins > coins:
            print("That's not a legal move. Try again.")
        coins = coins - player2Coins
        if coins == 0:
            winner = player2Name
            gameRunning = False
            player2Turn = False
            player1Turn = False
        else:
            player2Turn = False
            player1Turn = True
