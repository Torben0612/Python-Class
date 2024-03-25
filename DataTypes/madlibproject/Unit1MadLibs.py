#Instuctions
print("The Interview MadLib\n" + "I will ask you for nouns, verbs, adjectives, proper nouns, names, colors, clothing, \nlocations. ect. Using those words I will create an unexpected story for you!")
    
#Variables
adj1= input("Enter a adjective: ")
place1 = input("Enter a Place: ")
color1 = input("Enter a color: ")
color2 = input("Enter a color: ")
color3 = input("Enter a color: ")
clothing1 = input("Enter a piece of clothing: ")
clothing2 = input("Enter a piece of clothing: ")
clothing3 = input("Enter a piece of clothing: ")
transport = input("Enter a form of transportation : ")
place2 = input("Enter a Place: ")
place3 = input("Enter a Place: ")
number1 = input("Enter a number: ")
number1 = int(number1)**2 #convert the number input to a int and math modifed it
number1 = str(number1) #convert the modfifed int back to a string
time = input("Enter a time: ")
verb1 = input("Enter a verb: ")
propernoun1 = input("Enter a proper noun: ")
number2 = input("Enter a number: ")
propernoun2 = input("Enter a proper noun: ")
adj2 = input("Enter a adjective: ")
name1 = input("Enter a Name: ")
adj3 = input("Enter a adjective: ")
name2 = input("Enter a Name: ")
noun1 = input("Enter a noun: ")
facialexpress = input("Enter a facial expression: ")
adj4 = input("Enter a adjective: ")
yesno = input("Enter yes or no: ")

#Complete MadLib
print("The Interview:\n")
print("You are getting ready to go to a " + adj1 + "job interview at " + place1 + " you put on,\n" + color1 +
      " " + clothing1 + ", " + color2 + " " + clothing2 + ", and a " + color3 + " " + clothing3 + "\n" +
      "You take the " + transport + " from " + place2 + " to " + place3 + ". it \n" +
      "Takes you " + number1 + " minutes to get there you arrive at " + time + ". You " + verb1 + " down\n" +
      propernoun1 + " street and arrive at " + number2 + " " + propernoun2 + " street.\n" +
      "You go inside to meet a " + adj2 + " receptionist named " + name2 + ". you ask them\n" +
      "'I am here for a Job Interview with " + name2 + " for a job at " + noun1 + " LLC.'\n" +
      "The receptionist leads you to a room that looks very " + adj3 + ". The interviewr\n" +
      "look at you with a " + facialexpress + " face and asks you a few questions. you answer them\n" +
      "in a " + adj4 + " way. at the end he concludes " + yesno + " you get the job.")