# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

map[vertical][horizontal] = "X"

# coordinate = list(position) #converts the string into a list
# coordinate = int(position)
# print(coordinate)
# row = int(coordinate[1]) - 1
# column = int(coordinate[0]) - 1

# map[row][column] = "😺" #you first chose the row from the map list and then column represents the index out of that row.

# if row == 1:
#   if column == 1:
#     row1[0]="X"
    # print(row1)
# row1[row] = "X"
# print(row1)

#Write your code below this row 👇






#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")