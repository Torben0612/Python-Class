floor_3 = ['prize', 'monster boss', 'monster', 'sword', 'sword', 'stairs down']
floor_2 = ['nothing', 'stairs down', 'sword', 'nothing', 'monster', 'stairs up']
floor_1 = ['magic stones', 'stairs up', 'monster', 'stairs down', 'nothing', 'nothing']
floor_0 = ['nothing', 'sword', 'monster', 'stairs up', 'sword', 'nothing']
dungeon = [floor_0, floor_1, floor_2, floor_3]
floor , room = 0,0
inventory=[]
lastMove="right"
print("""Welcome to Dungeon Crawler. Your command options are...
      left
      right
      up
      down
      grab
      fight 
      help
      inventory

      use help command to display more details of each command
      """)


while "prize" not in inventory:
  choice = input("\nYou are in a room with " + dungeon[floor][room] + ". What would you like to do?: ")
  if choice=="left":
    if (dungeon[floor][room]=="monster" or dungeon[floor][room]=="monster boss") and lastMove=="left":
      print("You cannot pass without defeating the " + dungeon[floor][room] + ".")      
    elif room!=0:
      room-=1
      lastMove="left"
    else:
      print("There are no rooms to the left. Please make another choice.")
  elif choice=="right":
    if (dungeon[floor][room]=="monster" or dungeon[floor][room]=="monster boss") and lastMove=="right":
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
      print("There are no stairs up in this room. Please make another choice")
  elif choice=="down":
    if dungeon[floor][room]=="stairs down":
      floor-=1
    else:
      print("There are no stairs down in this room. Please make another choice")
  elif choice=="grab":
    if dungeon[floor][room]=="magic stones" or dungeon[floor][room]=="sword" or dungeon[floor][room]=="prize":
      print("You grabbed " + dungeon[floor][room] + ".")
      inventory.append(dungeon[floor][room])
      dungeon[floor][room]="nothing"
    else:
      print("There is nothing to grab in this room. Please make another choice.")
  elif choice=="fight":
    if dungeon[floor][room]=="monster boss" and "sword" in inventory and "magic stones" in inventory:
      dungeon[floor][room]="nothing"
      inventory.remove("sword")
      print("You defeated the monster boss!")
    elif dungeon[floor][room]=="monster" and "sword" in inventory:
      dungeon[floor][room]="nothing"
      inventory.remove("sword")
      print("You defeated the monster!")
    else:
      print("You're missing the necessary items to fight. You must turn away.")
  elif choice=="help":
    print("""
      Welcome to Dungeon Crawler. help menu
      Your command options are...
      left - moves character left
      right - moves character right
      up - moves chacter up stairs if there
      down -moves character down stairs if there
      grab - grabs item in room if any
      fight - fight monster (with sword) or monster boss (with sword and stones)
      help - shows this help menu
      inventory - displays current items in inventory
      """)
  elif choice=="inventory":
    if len(inventory)==0:
      print("You are not carrying anything.")
    else:
      print("You are currently carrying:" , inventory)
  else:
    print("That's not a valid command. Please make another choice.")
print("You win!")