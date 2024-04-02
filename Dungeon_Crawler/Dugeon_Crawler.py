floor_2 = ['magic_stones', 'stairs down', 'monster', 'boss_monster', 'prize']
floor_1 = ['sword', 'stairs up', 'monster', 'stairs down', 'sword']
floor_0 = ['nothing', 'sword', 'monster', 'stairs up', 'sword']
dungeon = [floor_0, floor_1, floor_2]
user_inventory = []

print("""
left, 
right, 
up, 
down, 
grab, 
fight, 
help 
inventory
""")
game_running = True
while game_running:
