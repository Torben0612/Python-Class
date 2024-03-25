#Part 2: Game Show
prize1 = "1 Million Dollars"
prize2 = "Tesla Cybertruck"
prize3 = "10k"
prize4 = "Gaming Laptop"
prize5 = "Samsung Galaxy S24 Ultra"
prize6 = "1k"

doorchosen = int(input("Welcome to the game show. Pick a door number 1-6 and win a prize. Which door do you pick between 1 and 6"))

if doorchosen == 1:
    print("You won", prize1)
elif doorchosen == 2:
    print("You won", prize2)
elif doorchosen == 3:
    print("You won", prize3)
elif doorchosen == 4:
    print("You won", prize4)
elif doorchosen == 5:
    print("You won", prize5)
elif doorchosen == 6:
    print("You won", prize6)
else:
    print("You didn't pick a valid door. No prize for you.")

#Part 3 Triangle
x = float(input("Enter the first side length: "))
y = float(input("Enter the second side length: "))
z = float(input("Enter the third side length: "))

if x + y > z and x + z > y and y + z > x:
  perimeter = x + y + z

  is_right = (x**2 + y**2 == z**2) or (y**2 + z**2 == x**2) or (x**2 + z**2 == y**2)

  triangle_type = "scalene"
  if x == y == z:
    triangle_type = "equilateral"
  elif x == y or y == z or x == z:
    triangle_type = "isosceles"

  print(f"\nYou can make a triangle with these sides.")
  print(f"Perimeter: {perimeter}")
  if is_right:
    print(f"Triangle type: {triangle_type} right")
  else:
    print(f"Triangle type: {triangle_type}")
else:
  print("\nYou cannot make a triangle with these side lengths.")
