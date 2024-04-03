print("Welcome to place the rabbit\n")
field = [ ["🍀", "🍀", "🍀"], ["🍀", "🍀", "🍀"], ["🍀", "🍀", "🍀"] ]

print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("\nWhere shoudl the rabbit go? 🐇 ")


position = input("Please choose a row and a column: ")
row = int(position[0])
column = int(position[1])

field[row][column] = "🐇"

print("\n Success ....\n")

print(f"{field[0]} \n{field[1]} \n{field[2]}")
