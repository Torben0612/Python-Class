month = 5 
day = 30
DAYS_IN_MONTH = [0,31,28,31,30,31,30,31,31,30,31,30,31] 

#Name:
#Purpose
#Inputs
#returns
def is_last_day():
    if DAYS_IN_MONTH[month] == day:
        return True
    else:
        return False

#name: next day
#purpose
#inputs:
#returns:
#def advance_game_clock():
def next_day():
    if is_last_day() == True:
        month += 1
        day = 0
    else:
        day + 1


def advance_game_clock(num_days_to_advance):
    while num_days_to_advance != 0:
        next_day()
        num_days_to_advance -= 1