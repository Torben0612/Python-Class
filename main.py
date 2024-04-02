floor_2 = ['a sword', 'stairs down', 'nothing', 'a monster boss', 'prize']
floor_1 = ['magic stones', 'stairs up', 'a monster', 'stairs down', 'nothing']
floor_0 = ['nothing', 'a sword', 'a monster', 'stairs up', 'a sword']
dungeon = [floor_0, floor_1, floor_2]
floor , room = 0,0
inventory=[]
lastMove="right"
print("Welcome to Dungeon Crawler.\nYour command options are...\n\tleft\n\tright\n\tup\n\tdown\n\tgrab\n\tfight\n\thelp\n\tinventory")


while "prize" not in inventory:
  choice = input("\nYou are in a room with " + dungeon[floor][room] + ". What would you like to do?: ")
  if choice=="left":
    if (dungeon[floor][room]=="a monster" or dungeon[floor][room]=="a monster boss") and lastMove=="left":
      print("You cannot pass without defeating the " + dungeon[floor][room] + ".")      
    elif room!=0:
      room-=1
      lastMove="left"
    else:
      print("There are no rooms to the left. Please make another choice.")
  elif choice=="right":
    if (dungeon[floor][room]=="a monster" or dungeon[floor][room]=="a monster boss") and lastMove=="right":
      print("You cannot pass without defeating the " + dungeon[floor][room] + ".")  
    elif room!=len(floor_0)-1:
      room+=1
      lastMove="right"
    else:
      print("There are no rooms to the right. Please make another choice.")
  elif choice=="up":
    if dungeon[floor][room]=="stairs up":
      floor+=1
    else:
      print("There are no stairs leading up in this room. Please make another choice")
  elif choice=="down":
    if dungeon[floor][room]=="stairs down":
      floor-=1
    else:
      print("There are no stairs leading down in this room. Please make another choice")
  elif choice=="grab":
    if dungeon[floor][room]=="magic stones" or dungeon[floor][room]=="a sword" or dungeon[floor][room]=="prize":
      print("You grabbed " + dungeon[floor][room] + ".")
      inventory.append(dungeon[floor][room])
      dungeon[floor][room]="nothing"
    else:
      print("There is nothing to grab in this room. Please make another choice.")
  elif choice=="fight":
    if dungeon[floor][room]=="a monster boss" and "a sword" in inventory and "magic stones" in inventory:
      dungeon[floor][room]="nothing"
      inventory.remove("a sword")
      print("You defeated the monster boss!")
    elif dungeon[floor][room]=="a monster" and "a sword" in inventory:
      dungeon[floor][room]="nothing"
      inventory.remove("a sword")
      print("You defeated the monster!")
    else:
      print("You're missing the necessary items to fight. You must turn away.")
  elif choice=="help":
    print("\nYour command options are...\n\tleft\n\tright\n\tup\n\tdown\n\tgrab\n\tfight\n\thelp\n\tinventory")
  elif choice=="inventory":
    if len(inventory)==0:
      print("You are not carrying anything.")
    else:
      print("You are currently carrying:" , inventory)
  else:
    print("That's not a valid command. Please make another choice.")
print("You win!")