#add numbers

#Name: add_num
#Purpose: takes 2 number that were in the argument when calling the function and add them
#Input(s): 2 numbers
#Returns: none
def add_num(number1, number2):
    print(number1 + number2)

add_num(3, 8)

#Birthday Song
#Name: birthday_song
#Purpose: birthday_song prints out a personalized birthday song
#inputs: name (str)
#Returns: none

def birthday_song(name):
    print("Happy birthday to you, happy birthday dear " + name + " happy birthday to you")

birthday_song(name="Torben")

#Magic 8-ball
import random

responses = ["Outlook is good", "Ask again later", "Yes", "No", "Most likely no", "Most likely yes", "Maybe", "Outlook is not good"]

#Name: eightball_response()
#Purpose: to simulate a magic eight-ball by selecting random responses to user questions.
#Input: none
#Return: string
def eightball_response():
    answer = responses[random.randint(0, 7)]
    return answer

play_again = True
while play_again:
    input("ask the magic 8 ball a yes or no question: ")
    answer = eightball_response()
    print(answer)
    replay = input("Would you like to continue? Enter yes or no: ")
    if replay=="no":
        play_again = False