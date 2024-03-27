# #Change Temperature Units

units = input("Would you like to enter a temperature in Fahrenheit or in Celsius (type F or C)?")
if units == "F":
    temp = float(input("Enter a Fahrenheit temperature:"))
    print("The tempature is", (temp-32) * 5/9, "degrees Celsius.")
elif units == "C":
    temp = float(input("Enter a Celsius temperature:"))
    print("The tempature is", (0/5 * temp) + 32, "degrees Fahrenheit.")

#Sorting
# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# z = int(input("Enter a thrid number:"))

# if x > y and x > z:
#     if y < z:
#         print(y,z,x)
#         print(x,z,y)
#     else:
#         print(z,y,x)
#         print(x,y,z)
# elif y > x and y > z:
#     if x < z:
#         print(x,z,y)
#         print(y,z,x)
#     else:
#         print(z,x,y)
#         print(y,x,z)
# else:
#     if y < x:
#         print(y,x,z)
#         print(z,x,y)
#     else:
#         print(x,y,z)
#         print(z,y,x)
    
#Grade Level
# grade = int(input("What grade are you in: "))
# if grade == 9:
#     print("Welcome to BHS")
# elif grade == 10 or 11 or 12:
#     print("Welcome back to BHS")
# else:
#     print("I guess you aren’t in high school.")