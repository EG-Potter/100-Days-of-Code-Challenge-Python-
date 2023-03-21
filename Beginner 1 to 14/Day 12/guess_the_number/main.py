#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100")

number = random.randint(1,101)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower() 

def game(number, difficulty):
  lives = 0
  if difficulty == 'easy':
    lives += 10
  elif difficulty == 'hard':
    lives += 5

  while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number. ")
    guess = int(input("Make a guess: "))
    if guess != number:
      if guess > number:
        print("Too High")
      elif guess < number:
        print("Too Low")
    else:
      return print(f"You got it! answer was {number}")
    lives -= 1
    if lives == 0:
      return print("You've run out of guesses, you lose.")

    
game(number, difficulty)