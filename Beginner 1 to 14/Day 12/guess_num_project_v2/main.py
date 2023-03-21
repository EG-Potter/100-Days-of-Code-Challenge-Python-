#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def difficulty_guesses(difficulty):
  '''Assigns number of guesses to difficulty'''
  if difficulty == 'easy':
    return 10
  elif difficulty == 'hard':
    return 5

def number_compare(numChoice,randNumber):
  '''Compares random number and users choices'''
  if numChoice > randNumber:
    print("Too high.")
    print("Guess again.")
    return 1
  elif numChoice < randNumber:
    print("Too low.")
    print("Guess again.")
    return 1
  elif numChoice == randNumber:
    print(f"\nBingo, the answer was {randNumber}\n")
    return 100
      
print("Welcome to the Number guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def guessTheNumber():
  '''Base Game/functionality'''
  game_on = True

  while game_on:

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lives = difficulty_guesses(difficulty)

    if lives != (10 or 5):
      print("Incorrect Input")
      guessTheNumber()
      
    else:
      attempts = 0
      randNumber = random.randrange(101)
      
      while (attempts < lives):
        print(f"You have {lives - attempts} attempts remaining to guess the number. ")
        numChoice = int(input("Make a guess: "))
        attempts += number_compare(numChoice,randNumber)

      if attempts == lives:
        print("\nYou've run out of guesses, you lose.\n")
        game_on = False
      elif attempts > lives:
        game_on = False
        
guessTheNumber()