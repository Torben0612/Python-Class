#Name: tell_chicken_joke
#Purpose: Asks the user why the chicken crosses the road. When the user types an answer, a random answer to the riddleis printed on the console.
#Inputs: None
#Returns: None   ←-------This function only prints to the console. Print statements don’t return anything!!

#Here is the main program:
import random

def tell_chicken_joke():
    answer = ["to get to the other side", "because he couldent fly", "because he was bored and watned to dodge carst"]
    input("Why did the chicken cross the road? ")
    print(answer[random.randint(0,2)])
over = False
while not over:
  tell_chicken_joke()
  answer = input("Do you want to ask me again? Type 'y' or 'n': ")

  if answer != 'y':
     print("Have a nice day.")
     over = True