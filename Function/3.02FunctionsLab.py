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
    else:
        converted_temp = current_temp * (9 / 5) + 32
    return temperature

def weatherforcast(tempature):
    if temp_type_num == 1:
        if tempature <= 40:
print(temp_converter(80, 2))