# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_input = input("What do you choose? Rock, Paper, or Scissors? \n\n").lower()

list = ["rock", "paper", "scissors"]

active = 0
#computer = list[random.randint(0,len(list) - 1)]

if user_input == "rock":
  print(rock)
  computer = list[random.randint(0,len(list) - 1)]
  active += 1
elif user_input == "paper":
  print(paper)
  computer = list[random.randint(0,len(list) - 1)]
  active += 1
elif user_input == "scissors":
  print(scissors)
  computer = list[random.randint(0,len(list) - 1)]
  active += 1
else:
  print("\nWrong input, try again\n")

if active > 0:
  print("\nComputer chooses: ")
if active > 0 and computer == "rock":
  print(rock)
if active > 0 and computer == "paper":
  print(paper)
if active > 0 and computer == "scissors":
  print(scissors)

if user_input == "paper" and computer == "rock":
  print("You Win!")
elif user_input == "rock" and computer == "scissors":
  print("You Win!")
elif user_input == "scissors" and computer == "paper":
  print("You Win!")
elif user_input == "paper" and computer == "scissors":
  print("You Lose!")
elif user_input == "rock" and computer == "paper":
  print("You Lose!")
elif user_input == "scissors" and computer == "rock":
  print("You Lose!")
elif active > 0:
      print("Draw, try again\n")
