#Part 2: Game Show
prize1 = "1 Million Dollars"
prize2 = "Tesla Cybertruck"
prize3 = "10k"
prize4 = "Gaming Laptop"
prize5 = "Samsung Galaxy S24 Ultra"
prize6 = "1k"

doorchosen = int(input("Welcome to the game show. Pick a door number 1-6 and win a prize. Which door do you pick between 1 and 6"))

if doorchosen == 1:
    print("You won", prize1)
elif doorchosen == 2:
    print("You won", prize2)
elif doorchosen == 3:
    print("You won", prize3)
elif doorchosen == 4:
    print("You won", prize4)
elif doorchosen == 5:
    print("You won", prize5)
elif doorchosen == 6:
    print("You won", prize6)
else:
    print("You didn't pick a valid door. No prize for you.")