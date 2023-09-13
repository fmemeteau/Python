row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")


position = input("Where do you want to put the treasure ? The first digit is the column, the second one is the row number. ")

pos_x = int(position[1])
pos_y = int(position[0])

x = int(pos_x) - 1
y = int(pos_y) - 1

map[x][y] = "X"

print(f"{row1}\n{row2}\n{row3}")
