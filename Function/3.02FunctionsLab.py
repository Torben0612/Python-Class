import random
# Name: quad_solve
# Purpose: Finds solutions to the equation ax^2 + bx + c = 0 and
#   returns the result. Uses the quadratic formula:
#      -b +/- sqrt(b^2 - 4ac)
#  x=  ----------------------
#               2a
# Input(s): a, b, and c (floats) <- you may assume user will enter floats
# Return(s): solutions_list(list) These are decimal values for the solutions to the quadratic rounded to the hundredths place.)

# def quad_solve(a, b, c):
#     a = float(a)
#     b = float(b)
#     c = float(c)
#     s = b**2 - 4 * a * c
#     y = (-b + (s) ** 0.5) / (2 * a)
#     x = (-b - (s) ** 0.5) / (2 * a)
#     solutions_list = [x, y]
#     if s < 0:
#         return "not real"
#     else:
#         return solutions_list



# print(quad_solve(1, -4, 4))


#Name: temp_converter
#Purpose convert F and C
#imputs: current_temp(int) choice(1 or 2)
#returns converted tempaute

def temp_converter(current_temp, choice):
     if choice == 1:
         tempature = (current_temp - 32) * (5/9)
     elif choice == 2:
         tempature = current_temp * (9 / 5) + 32
         print("invalid choice. enter 1 or 2")
         return tempature


#Name: weatherforcast
#Purpose: prints the weather forcast
#inputs: tempature(int), temp_type_num(int 1 or 2)
#retuens: nothing
def weatherforcast(tempature, temp_type_num):
    rain = randint(0,100)
    if temp_type_num == 1:
        if tempature <= 40:
            print("Today’s weather will be Cold, need winter jacket! with a", rain "percent chance of rain")
        elif 40 < tempature and tempature < 65:
            print("Cool, sweater weather!")
        elif 65 <= tempature and tempature < 82:
            print("Perfect, very comfortable")
        elif 82 <= tempature:
            print("Too hot, don’t melt!")
    elif temp_type_num == 0:
        if tempature <= 4:
            print("Cold, need winter jacket!")
        elif 4 < tempature and tempature < 18.5:
            print("Cool, sweater weather!")
        elif 18.5 <= tempature and tempature < 27.8:
            print("Perfect, very comfortable")
        elif 27.8 <= tempature:
            print("Too hot, don’t melt!")

#weatherforcast(3, 0)

#Main program
doit = True

while doit == True:
    print("""Welcome to the weather forecast! Would you like to convert from 
          1) Fahrenheit to Celsius or 
          2) Celsius to Fahrenheit? 
          """)
    choice = input("Please make your selection. Type quit if you want to exit.")
    tempature 
    if choice == "quit":
        doit = False
    else:
        temp_converter()

#check for primes
#Name: Check for Primes