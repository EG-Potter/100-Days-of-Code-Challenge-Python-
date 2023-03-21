############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

from replit import clear
from art import logo
import random

user_hand = []
dealer_hand = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def score_update():
  print(f"Your cards: {user_hand}, current score = {sum(user_hand)}")
  print(f"Computer's first card: {dealer_hand[0]}\n")
  
def game_decide():
  if sum(user_hand) > 21:
    game_complete()
    print("you went over, you lose. \n")
    black_jack()
  if sum(dealer_hand) < 17:
    under_score()    
  if sum(user_hand) > sum(dealer_hand) or sum(dealer_hand) > 21:
    if sum(dealer_hand) > 21 and 11 in dealer_hand:
      elevens()
      game_decide()
    game_complete()
    if sum(user_hand) > sum(dealer_hand):
      print("You score higher, you win. \n")
    else:
      print("dealer went bust, you win. \n")
    black_jack()
  if sum(user_hand) < sum(dealer_hand) or sum(user_hand) > 21:
    if sum(user_hand) > 21 and 11 in user_hand:
      elevens()
      game_decide()
    game_complete()
    if sum(user_hand) > 21:
      if sum(user_hand) > 21 and sum(dealer_hand) > 21:
        print("you both went over, you draw. \n")
      else:
        print("you went over, you lose. \n")
    else:
      print("Dealer scored higher, you lose. \n")
    black_jack()
  if sum(user_hand) > sum(dealer_hand) or sum(dealer_hand) > 21:
    game_complete()
    if sum(user_hand) > sum(dealer_hand):
      print("You score higher, you win. \n")
    else:
      print("dealer went bust, you win. \n")
    black_jack()
  if sum(user_hand) == sum(dealer_hand):
    game_complete()
    print("You score the same, you draw. \n")
    black_jack()


def game_complete():
  print(f"Your final hand: {user_hand}, final score = {sum(user_hand)}")
  print(f"Computer's final hand: {dealer_hand}, final score = {sum(dealer_hand)}")

def user_draw(user_hand):
  user_hand += random.sample(set(cards),1)
  return user_hand

def dealer_draw(dealer_hand):
  dealer_hand += random.sample(set(cards),1)
  return dealer_hand

def under_score():
  while sum(dealer_hand) < 17:    
    dealer_draw(dealer_hand)
  return dealer_hand
  
def elevens():
  if sum(user_hand) > 21 and 11 in user_hand:
    for i in range(len(user_hand)):
      if user_hand[i] == 11:
        user_hand[i] = 1
  elif sum(dealer_hand) > 21 and 11 in dealer_hand:
    for i in range(len(dealer_hand)):
      if dealer_hand[i] == 11:
        dealer_hand[i] = 1
def black_jack():
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n") == 'y':
    clear()
    user_hand.clear()
    dealer_hand.clear()
    print(logo)
    for i in range(0,2):
      user_draw(user_hand)
      dealer_draw(dealer_hand)

    if sum(user_hand) > 21:
      elevens()
        
    score_update()
        
    active = True
    
    while active:
      if input("Type 'y' to get another card, type 'n' to pass: \n") == 'y':
        user_draw(user_hand)
        if sum(user_hand) > 21:
          game_decide()
        score_update()
      else:
        game_decide()
        score_update()
  else:
    black_jack()
black_jack()

