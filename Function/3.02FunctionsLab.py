import random
#1 Quadratic Equation Solver

# Name: quad_solve
# Purpose: Finds solutions to the equation ax^2 + bx + c = 0 and
#   returns the result. Uses the quadratic formula:
#      -b +/- sqrt(b^2 - 4ac)
#  x=  ----------------------
#               2a
# Input(s): a, b, and c (floats) <- you may assume user will enter floats
# Return(s): solutions_list(list) These are decimal values for the solutions to the quadratic rounded to the hundredths place.)

def quad_solve(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    s = b**2 - 4 * a * c
    y = (-b + (s) ** 0.5) / (2 * a)
    x = (-b - (s) ** 0.5) / (2 * a)
    solutions_list = [x, y]
    if s < 0:
        return "not real"
    else:
        return solutions_list



print(quad_solve(1, -4, 4))

#2 - Celsius/Fahrenheit Conversion

#Name: temp_converter
#Purpose convert F and C
#imputs: current_temp(int) choice(1 or 2)
#returns converted tempaute

def temp_converter(current_temp, choice):
     if choice == 1:
         tempature = (current_temp - 32) * (5/9)
         return int(tempature)
     elif choice == 2:
         tempature = current_temp * (9 / 5) + 32
         print("invalid choice. enter 1 or 2")
         return int(tempature)


#Name: weatherforcast
#Purpose: prints the weather forcast
#inputs: tempature(int), temp_type_num(int 1 or 2)
#retuens: nothing
def weatherforcast(tempature, temp_type_num):
    rain = random.randint(0,100)
    if temp_type_num == 1:
        if tempature <= 40:
            print("It is {} degrees Fahrenheit. Today weather will be Cold, need winter jacket! with a {} percent chance of rain".format(tempature, rain))
        elif 40 < tempature and tempature < 65:
            print("It is {} degrees Fahrenheit. Today weather will be Cool, sweater weather! with a {} percent chance of rain".format(tempature, rain))
        elif 65 <= tempature and tempature < 82:
            print("It is {} degrees Fahrenheit. Today weather will be Perfect, very comfortable with a {} percent chance of rain".format(tempature, rain))
        elif 82 <= tempature:
            print("It is {} degrees Fahrenheit. Today weather will be Too hot, don't melt! with a {} percent chance of rain".format(tempature, rain))
    elif temp_type_num == 2:
        if tempature <= 4:
            print("It is {} degrees Celsius. Today weather will be Cold, need winter jacket! with a {} percent chance of rain".format(tempature, rain))
        elif 4 < tempature and tempature < 18.5:
            print("It is {} degrees Celsius. Today weather will be Cool, sweater weather with a {} percent chance of rain".format(tempature, rain))
        elif 18.5 <= tempature and tempature < 27.8:
            print("It is {} degrees Celsius. Today weather will be Perfect, very comfortable with a {} percent chance of rain".format(tempature, rain))
        elif 27.8 <= tempature:
            print("It is {} degrees Celsius. Today weather will be Too hot, don’t melt! with a {} percent chance of rain".format(tempature, rain))

#Main program
doit = True

while doit == True:
    print("""Welcome to the weather forecast! Would you like to convert from 
          1) Fahrenheit to Celsius or 
          2) Celsius to Fahrenheit? 
          Please make your selection. Type quit if you want to exit.
          
          """)
    choice = input("User Input: ")
    if choice == "quit":
        doit = False
    elif int(choice) == 1:
        print("Great! Please enter your temperature in Fahrenheit.")
        curent_temp = int(input("User Input: "))
        weatherforcast(temp_converter(curent_temp, 1), 2)
    else:
        print("Great! Please enter your temperature in Celsius.")
        curent_temp = int(input("User Input: "))
        weatherforcast(temp_converter(curent_temp, 2), 1)

#3 - Check for Primes

#Name: check_prime
#Purpose check if a int is a prime number
#inputs num(int)
#retuens: boolean

def check_prime(n):
    if n <= 2:
        return False
    i = n - 1
    while i > 1:
        if n % i == 0:
            return False
        i = i - 1
    return True


#Name: create_prime_factors
#purpose: takesn in a number and returns a list of prime factors
#Inputs: int
#Returns: list of prime factors
def create_prime_factors(num):
    f = []
    d = 2
    while d <= num:
        if num % d == 0:
            f.append(d)
            num = num / d
        else:
            d = d + 1
    return f

#name: safe_to_integer
#purpose: ensures an input as an integer
#input: varies (type: varies)
#output: ture or false
def safe_to_integer(a):
    try:
        int(a)
        return True
    except ValueError:
        print("that is not an integer: ")
        return False
    except:
        print("a unknown error occured")
        return False

a = input("enter a character: ")

if safe_to_integer(a) == True:
    print("""enter 1 if you only want to check if its a prime.
          enter 2 if you want the full prime factorization""")
    if int(input("User Input: ")) == 1:
        if check_prime(int(a)) == True:
            print("That is a prime number")
        else:
            print("That is not a prime")
    else:
        print(create_prime_factors(int(a)))
else:
    print("please enter a integer")
