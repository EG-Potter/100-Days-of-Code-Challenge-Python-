from replit import clear
import art
import random
from game_data import data

# Function to print diction values and store follower count.
def break_down(randNumber):
  '''Takes int value, prints/returns corresponding dictionary values'''
  name = data[randNumber]['name']
  description = data[randNumber]['description']
  country = data[randNumber]['country']
  print(f"{name}, {description}, {country}")

  follower_count = data[randNumber]['follower_count']
  return follower_count

# Function to compare follower count, then return 'a' or 'b'.
def compare_follower(number1, number2):
  '''Takes 2 int values, returns corresponding value similar ro user input'''
  if number1 > number2:
    return 'a'
  return 'b'

print(art.logo)
  
def higher_lower():

  # Generates random number from total length of the 'data' dictionary.
  choice1 = random.randrange(len(data))

  # Repeats the game and increases score until user input is incorrect.
  score = 0
  game_on = True
  
  while game_on:
    
    number1 = break_down(choice1)
    
    print(art.vs)    
    choice2 = random.randrange(len(data))
    number2 = break_down(choice2)

    # Lets the user input option.
    choice = input("Who has more follower? Type 'A' or 'B': ").lower()
    clear(), print(art.logo)
    
    # Checks if user option is the largest of the 2 options.
    if choice == compare_follower(number1, number2):
      score += 1
      choice1 = choice2
      print(f"You're right! Current score: {score}.")
    else:
      game_on = False
      print(f"Sorry, that's wrong. Final score: {score}.")

higher_lower()