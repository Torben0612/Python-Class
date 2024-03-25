age = int(input("How old are you?"))
ageok = age >= 36
print("You are old enough to be President:", ageok)

yearslived = int(input("How many years have you lived in us?"))
yearslivedok = yearslived >= 14
print("You have been a resident for at least 14 years:", yearslivedok)


#Part III
print("Give me your height by giving total feed and then on the next prompt the remaining inches")
heightFeet = int(input("How many feet tall are you? "))
additonalInch = int(input("How many additional inches"))

heightInch = heightFeet * 12 + additonalInch
print("You are tall enough to ride the rolar coaster:", heightInch >= 50)

age = int(input("How old are you? "))
print("You are old enough to ride regarless of your height", age >= 18)

money = int(input("How many quarters do you have"))
print("You have enough money to ride without a pass:", money >= 4)

ridePass = input("Do you have a frequent rider pass")

print("You only need to pay two quarters to ride:", ridePass == "Yes" or "yes")

print("You can ride the coaster:", (heightInch>=50 or age >= 18) and (money>=4 or (ridePass == "Yes" or "yes" and money >= 2)))