# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_letters = ""
password_symbols = ""
password_numbers = ""

if nr_letters > 0:
  for number in range(0, nr_letters):
    num = random.randint(0,len(letters) - 1)
    chosen = str(letters[num])
    password_letters += chosen
if nr_symbols > 0:
  for number in range(0, nr_symbols):
    num = random.randint(0,len(symbols) - 1)
    chosen = str(symbols[num])
    password_symbols += chosen
if nr_numbers > 0:
  for number in range(0, nr_numbers):
    num = random.randint(0,len(numbers) - 1)
    chosen = str(numbers[num])
    password_numbers += chosen

print(password_letters + password_symbols + password_numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list = []

if nr_letters > 0:
  for number in range(0, nr_letters):
    num = random.randint(0,len(letters) - 1)
    chosen = str(letters[num])
    list.append(chosen)
if nr_symbols > 0:
  for number in range(0, nr_symbols):
    num = random.randint(0,len(symbols) - 1)
    chosen = str(symbols[num])
    list.append(chosen)
if nr_numbers > 0:
  for number in range(0, nr_numbers):
    num = random.randint(0,len(numbers) -1)
    chosen = str(numbers[num])
    list.append(chosen)

final = ""

for number in range(0,len(list)):
  num = random.randint(0,len(list) - 1)
  final += list[num]
  list.remove(list[num])

print(final)