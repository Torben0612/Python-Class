numbersList = [[1, 3, 6], [6, 8, 3], 8]

favNum = int(input("What is your fav number"))
maxNum = numbersList[0][0]
if maxNum < numbersList[0][1]:
    maxNum = numbersList[0][1]
elif maxNum < numbersList[0][2]:
    maxNum = numbersList[0][2]

