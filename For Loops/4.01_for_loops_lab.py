import random

#Part 1

#Name: get_numbers
#purpose: ask for number and does stuff
#inputs: none
#returns: num_list(list)
def get_numbers():
    num_list = []
    while True:
        num = input("Please enter a integer or 'done' if finished: ")
        if num == "done":
            print(num_list)
            return num_list
        else:
            num_list.append(int(num))
    print("This the the list of numbers you inputed", num_list)
    return num_list

#Name: count_evens
#purpose: counts the number of even  umbers
#inputs: num_list(list)
#returns: y(int)
def count_evens(num_list):
    y = 0
    for i in num_list:
        if i % 2 == 0:
            y += 1
    print("the number of even numbers in the list is", y)
    return y

count_evens(get_numbers())

#Part 2

#Name: name_list
#purpose: asks for name add tom list
#inputs: none
#returns: names(list)
def name_list():
    names = []
    while True:
        name = input("Please enter a name or 'done' if finished: ")
        if name == "done":          
            return names
        else:
            names.append(name)
    return names

#Name: congats
#purpose: congrats the name with random eventrs
#inputs: name_list(list)
#returns: none
def congrats(name_list):
    events = ['on your first successful skydive', 'on getting your driver’s license', 'on getting straight A’s']
    for i in name_list:
        print("Congrats", i, events[random.randint(0,2)])

congrats(name_list())


#part 3

#Name: count_letter
#purpose: counts the number of letters
#inputs: word(string) letter(string)
#outputs: count(int)
def count_letter(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count

print(count_letter(input("enter a word"), input("enter a letter")))


#part 4

#Name: get_first_letter
#purpose: take in a word and return the first letter of the word capitalized.
#inputs: word(string)
#outputs: letter(str, captilized)
def get_first_letter(word):
    for i in word:
        letter = i.upper()
        return letter


#Name: acronym
#purpose: take in a sentence and output it as an ancronmym 
#inputs: sentence(str)
#outputs: acronym_list(list)
def acronym(sentence):
    sentence_list = sentence.split(" ")
    acronym_list = []
    for i in sentence_list:
        acronym_list.append(get_first_letter(i))
    return(acronym_list)

x = input("enter a sentence to convert into a acronym")
for i in acronym(x):
    print(i)