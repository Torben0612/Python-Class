# list = ['a', 'b', 'c', 'd']

# index = 0

# while index < len(list):
#     print(list[index])
#     index = index + 1

# for letter in list:
#     print(letter)

# for letter in "python class":
#     print("hi")

names = []
#FUNCTIONS

#name:

def get_numbers():
    while running == True:
        num_list = []
        num = input("Please enter a integer or 'done' if finished: ")
        num_list.append(num)
        print(num_list)
    return num_list

get_numbers()