# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

count = len(names)

num_list = random.randint(0,count - 1)

print(f"{names[num_list]} is going to buy the meal today!")

