import random

#global variables
health = 5
food = 500
distance_remain = 2000
month = 1
day = 0
DAYS_IN_MONTH = [0,31,28,31,30,31,30,31,31,30,31,30,31] 

def next_day():
    food -= 1 

def advance_days():


def is_last_day():
    

def helth_loss_days():
    loss_days = [random.randint(0,DAYS_IN_MONTH[month]), random.randint(0,DAYS_IN_MONTH[month])]
    return loss_days


def status():
    print("""
    Your status
    health = {}
    food = {}
    distance remaining {}
    date = {}/{}
    """.format(health, food, distance_remain, month, day))

def help():
    print("""
        The goal is to travel from St. Louis, Missouri to Oregon City Oregon (2000 miles) by Dec 31st. 
        Each turn, the player is asked what action they choose. The player can type any of the following: travel, rest, hunt, status, help, or quit
        The player's health randomly decreases 2 times during the month.
        The player eats 5 lbs of food a day.
        travel: moves you randomly between 30-60 miles and takes 3-7 days (random).
        rest: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).
        hunt: adds 100 lbs of food and takes 2-5 days (random).
        status: lists food, health, distance traveled, and day.
        help: lists all the commands.
        quit: will end the game.""")


def hunt():

def rest():

def travel():

def check_end():

#main program
print("""The goal is to travel from St. Louis, Missouri to Oregon City Oregon
      (2000 miles) by Dec 31st. However,the trail is arduous. Each day costs
      you food and health. You can hunt and rest, but you have to get there before winter!""")

player_name = input("What is your name")

while True:
    