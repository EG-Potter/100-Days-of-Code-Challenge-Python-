# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true = 0
love = 0

check = name1.lower() + name2.lower()

if check.count('t') > 0:
    true += check.count('t')
if check.count('r') > 0:
    true += check.count('r')
if check.count('u') > 0:
    true += check.count('u')
if check.count('e') > 0:
    true += check.count('e')


if check.count('l') > 0:
    love += check.count('l')
if check.count('o') > 0:
    love += check.count('o')
if check.count('v') > 0:
    love += check.count('v')
if check.count('e') > 0:
    love += check.count('e')

score = str(true) + str(love)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
