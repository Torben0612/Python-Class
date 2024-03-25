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
