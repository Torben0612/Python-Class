#Part I: Genie Program 1
print("I am a genie. You have 3 wishes")
wish1 = input("What would you like to wish for? ")
wish2= input("What would you like to wish for? ")
wish3 = input("What would you like to wish for? ")
print("Your wishes are " + wish1 + ",", wish2, "and",wish3)


#Part 2: Genie Program 3
print("I am a genie. You have 3 wishes")
wish1 = input("What would you like to wish for? ")
wish2 = input("What would you like to wish for? ")
wish3 = input("What would you like to wish for? ")

w1=wish1
w2=wish2
w3=wish3

wish1=w2
wish2=w3
wish3=w1

print("Your wishes are " + wish1 + ",", wish2, "and",wish3)

#Challenge
a=8
b=5

a=a+b
b=a-b
a=a-b

print("The Value of a is ",a)
print("The Value of b is ",b)