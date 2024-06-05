# list = ['a', 'b', 'c', 'd']

# index = 0

# while index < len(list):
#     print(list[index])
#     index = index + 1

# for letter in list:
#     print(letter)

# for letter in "python class":
#     print("hi")

import random

#FUNCTIONS
#name:
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

def count_evens(num_list):
    y = 0
    for i in num_list:
        if i % 2 == 0:
            y += 1
    print("the number of even numbers in the list is", y)
    return y

count_evens(get_numbers())

#Part 2
def name_list():
    names = []
    while True:
        name = input("Please enter a name or 'done' if finished: ")
        if name == "done":          
            return names
        else:
            names.append(name)
    return names

def congrats(name_list):
    events = ['on your first successful skydive', 'on getting your driver’s license', 'on getting straight A’s']
    for i in name_list:
        print("Congrats", i, events[random.randint(0,2)])

congrats(name_list())


#part 3

#Name: count_letter
#purpose: counts the number of letters
#