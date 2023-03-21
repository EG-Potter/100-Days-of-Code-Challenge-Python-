# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int(position[0])
row = int(position[1])

#map[row-1][column-1] = "X"

if row == 1:
    if column > 3:
        print("Incorrect column value.")
    else:
        map[0][column-1] = "X"
if row == 2:
    if column > 3:
        print("Incorrect column value.")
    else:
        map[1][column-1] = "X"
if row == 3:
    if column > 3:
        print("Incorrect column value.")
    else:
        map[2][column-1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

