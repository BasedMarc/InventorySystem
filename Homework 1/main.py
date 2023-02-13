wallHeight = float(input("Enter wall height (feet):\n"))
wallWidth = float(input("Enter wall width (feet):\n"))
wallArea = wallHeight * wallWidth

print("Wall area:", int(wallArea), "square feet")
paintNeeded = wallArea / 350
print("Paint needed: {:.2f} gallons".format(paintNeeded))
cansNeeded = round(paintNeeded)
print("Cans needed:", cansNeeded, "can(s)\n")

print("Choose a color to paint the wall:")
dict({"red": 35, "blue": 25, "green": 23})
color = input()
if color == "red":
    print("Cost of purchasing red paint: ${}".format(cansNeeded * 35))
elif color == "blue":
    print("Cost of purchasing blue paint: ${}".format(cansNeeded * 25))
elif color == "green":
    print("Cost of purchasing green paint: ${}".format(cansNeeded * 23))
