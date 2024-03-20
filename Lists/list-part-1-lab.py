#Same element
#list1 = [1, 2, 4, 5, 6]
#list2 = [1, 2, 4, 6, 3]

#list1start = list1[0]
#list1end = list1[-1]

#list2start = list2[0]
#list2end = list2[-1]

#print(list1start == list2start or list1end == list2end)

#Do The Shuffle
#num = [2, 5, 6]
#newlist = [1, 4, 6]

#if len(num) != 3:
#    print("List needs to be 3 int long")
#else:
#    newlist[0] = num[1]
#    newlist[1] = num[2]
#    newlist[2] = num[0]
#    print(newlist)

#Two Sum
#numbers = [4, 7]
#
#if len(numbers) >= 2:
#    print(numbers[0] + numbers[1])
#elif len(numbers) == 1:
#    print(numbers[0])
#elif len(numbers) == 0:
#    print(0)

#Sheep
list = [4, 6, 2]
if list[0] > list[2]:
    list[1] = list[0]
    list[2] = list[0]
    print(list)
else:
    list[0] = list[2]
    list[1]= list[2]
    print(list)