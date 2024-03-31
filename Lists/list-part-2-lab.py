numbersList = [[1, 3, 6, 37], [6, 8, 9, 5], 2]

favNum = int(input("What is your fav number? "))

maxNum = numbersList[0][0]
if maxNum < numbersList[0][1]:
    maxNum = numbersList[0][1]
if maxNum < numbersList[0][2]:
    maxNum = numbersList[0][2]
if len(numbersList[0]) == 4 and maxNum < numbersList[0][3]:
    maxNum = numbersList[0][3]

prodNum = (numbersList[1][0] * numbersList[1][1] * numbersList[1][2])
if len(numbersList[1]) == 4:
    prodNum = prodNum * numbersList[1][3]

if numbersList[2] % 2 == 0:
    print("Your Luckey Number are", maxNum % favNum, "and", prodNum % favNum)
else:
    print("You are not luckey, have an unlucky day :)")