import random

#global variables
health = 5
food = 500
distance_remain = 2000
month = 3
day = 1
DAYS_IN_MONTH = [0,31,28,31,30,31,30,31,31,30,31,30,31] 
loss_days = []

#Name: next_day
#purpose: advance the game by a day.
#inputs: none
#returns: none
def next_day():
    global day, loss_days, month
    deduct_food()
    if day == loss_days[0] or day == loss_days[1]:
        deduct_health()
    if is_last_day() == True:
        month += 1
        day = 1
        helth_loss_days()
    else:
        day += 1

#Name: advance_days
#purpose: calls next_day() a certain number of times
#inputs: add_days
#returns: none
def advance_days(add_days):
    while add_days > 0 and gameruning == True:
        next_day()
        add_days -= 1
        check_end()

#Name: is_last_day
#Purpose: checks if today is the last day of the month. makes necessary modifications if it is
#Inputs none
#returns none
def is_last_day():
    global day, month, DAYS_IN_MONTH
    if DAYS_IN_MONTH[month] == day:
        return True
    else:
        return False

#Name: helth_loss_days
#purpose: 	at the start of each month pick the 2 days the user will get sick on
#inputs: none
#returns: none
def helth_loss_days():
    global loss_days, month, DAYS_IN_MONTH
    loss_days = [random.randint(1,DAYS_IN_MONTH[month]), random.randint(2,DAYS_IN_MONTH[month])]

#Name: deduct_health
#purpose: reduce health by 1 on sick days
#inputs: none
#returns: none
def deduct_health():
    global health
    health -= 1

#Name: add_health 
#purpose: adds health by 1
#inputs: none
#returns: npone
def add_health():
    global health
    health += 1

#Name: deduct_food
#purpose: removes 5 food
#inputs: none
#returns: none
def deduct_food():
    global food
    food -= 5

#Name: status
#purpose: status info is printed when user requests it
#inputs: none
#returns: none
def status():
    global health, food, distance_remain, month, day
    print("""
    Your status:
    health = {} | food = {} | distance remaining {} | date = {}/{}
    """.format(health, food, distance_remain, month, day))

#Name: hunt
#purpose: adds 100 food after hunt
#inputs: none
#returns: none
def hunt():
    global food
    advance_days(random.randint(2,5))
    food += 100

#Name: rest
#purpose: rest and gain 1 health no more than 5
#inputs: none
#returns: none
def rest():
    global health
    if health < 5:
        add_health()
    else:
        print("your already at max health of 5")
    advance_days(random.randint(2,5))

#Name: 
#purpose: 
#inputs: 
#returns: 
def travel():
    global distance_remain
    distance_remain -= random.randint(30,60)
    advance_days(random.randint(3,7))

#Name: check_end
#purpose: checks if the game has ended and stops game
#inputs: none
#returns: none
def check_end():
    global month, day, DAYS_IN_MONTH, food, gameruning, health, distance_remain
    if month == 12 and day == DAYS_IN_MONTH[12] and distance_remain > 1:
        print("You Lose you ran out of time")
        gameruning = False
    elif food <= 0:
        print("You Lose, You Ran out of food")
        gameruning = False
    elif health == 0:
        print("you dead.")
        gameruning = False
    elif distance_remain <= 0 and health >= 1 and food >= 1:
        print("You Win")
        gameruning = False

#Name: help
#purpose: prints what each command does
#inputs: none
#returns: none
def help():
    print("""
        travel: moves you randomly between 30-60 miles and takes 3-7 days (random).
        rest: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).
        hunt: adds 100 lbs of food and takes 2-5 days (random).
        status: lists food, health, distance traveled, and day.
        help: lists all the commands.
        quit: will end the game.""")

#main program
print("""The goal is to travel from St. Louis, Missouri to Oregon City Oregon starting 
      (2000 miles) starting on 3/1 ending Dec 31st. However,the trail is arduous. Each day costs
      you food and health. You can hunt and rest, but you have to get there before winter!""")

player_name = input("What is your name")
gameruning = True
helth_loss_days()
while gameruning == True:
    status()
    choice = input("What do you want to do")
    if choice == "travel":
        travel()
    elif choice == "rest":
        rest()
    elif choice == "hunt":
        hunt()
    elif choice == "status":
        status()
    elif choice == "help":
        help()
    elif choice == "quit":
        gameruning = False
    else:
        print("invalid command")