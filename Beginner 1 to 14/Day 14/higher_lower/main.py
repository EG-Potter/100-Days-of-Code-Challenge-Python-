#Imports
import art
import game_data
import random
from replit import clear
# Variables
optionA = {}
optionB = {}
score = 0
active = True

# Diagrams and basic Skeleton of the game
print(art.logo)

while active:
  
  def option():
    return random.choice(game_data.data)
  
  def printOptionA(optionA):
    filler, name = list(optionA.items())[0]
    filler, description = list(optionA.items())[2]
    filler, country = list(optionA.items())[3]
    return optionA, print(f"Compare A: {name}, {description}, {country}")
  
  def optionACount(optionA):
    filler, countA = list(optionA.items())[1]
    numA = int(countA)
    return numA
    
  def printOptionB(optionB):
    filler, name = list(optionB.items())[0]
    filler, description = list(optionB.items())[2]
    filler, country = list(optionB.items())[3]
    return print(f"Compare B: {name}, {description}, {country}")
    
  def optionBCount(optionB):
    filler, countB = list(optionB.items())[1]
    numB = int(countB)
    return numB

  def check(optionA,optionB):
    filler, nameA = list(optionA.items())[0]
    filler, nameB = list(optionB.items())[0]
    while nameA == nameB:
      optionB = random.choice(game_data.data)
      filler, nameB = list(optionB.items())[0]
    return optionB

  def game(option,score):
    if option == 'a':
      if followersA > followersB:
        return score + 1, True
      else:
        clear()
        return score, False
    elif option == 'b':
      if followersB > followersA:
        return score + 1, True
      else:
        clear()
        return score, False
  
  if optionA == {}:
    optionA = option()
  else:
    optionA = optionB
  
  followersA = optionACount(optionA)
  optionB = option()
  followersB = optionBCount(optionB)

  optionB = check(optionA,optionB)

  printOptionA(optionA)
  followersA = optionACount(optionA)
  
  print(art.vs)
  
  printOptionB(optionB)
  followersB = optionBCount(optionB)
  
  option = input("\nWho has more followers? Type 'A' or 'B': ").lower()
     
  score, active = game(option,score)

  clear()
  print(art.logo)
  print(f"You're right! Current score is: {score}\n")

clear()
print(art.logo)
print(f'Sorry, thats wrong. Your final score is: {score}')