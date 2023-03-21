import os

# with open('/Users/macbook/Desktop/my_file.txt') as file:
#     contents = file.read()
#     print(contents)

with open('../../Desktop/my_file.txt') as file:
    contents = file.read()
    print(contents)

# with open(os.path.expanduser("~/Desktop/my_file.txt")) as file:
#     contents = file.read()
#     print(contents)

# Appends to end of text file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# Overwrites text on file.
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")
