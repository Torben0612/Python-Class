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
#     y = (b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
#     x = (b - (b**2 - 4 *a *c) ** 0.5) / (2 * a)

#     solutions_list = [x, y]
#     return solutions_list

# print(quad_solve(2, -3, -9))


#Name: temp_converter
#Purpose convert F and C
#imputs: current_temp(int) choice(1 or 2)
#returns converted tempaute

def temp_converter(current_temp, choice):
    if choice == 1:
        converted_temp = (current_temp - 32) * (5/9)
    elif choice == 2:
        converted_temp = current_temp * (9 / 5) + 32
        print("invalid choice. enter 1 or 2")
    return tempature


#Name: weatherforcast
#Purpose: prints the weather forcast
#inputs: tempature(int), temp_type_num(int 1 or 2)
#retuens: nothing
def weatherforcast(tempature, temp_type_num):
    if temp_type_num == 1:
        if tempature <= 40:
            print("Cold, need winter jacket!")
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

weatherforcast(3, 0)

#Main program
while True:
    print("""Welcome to the weather forecast! Would you like to convert from 
          1) Fahrenheit to Celsius or 
          2) Celsius to Fahrenheit? 
          """)
    input("Please make your selection. Type quit if you want to exit.")