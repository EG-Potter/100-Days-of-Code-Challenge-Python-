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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
dealer_hand = []

def check_count(hand1, hand2):
  '''Figures out the outcome of the game'''
  print(f"  Your final hand: {hand1}, final score: {sum(hand1)}")
  print(f"  Computer's final hand: {hand2}, final score: {sum(hand2)}")
    
  if sum(hand1) <= 21 and sum(hand2) <= 21:   
    if sum(hand1) == sum(hand2):
      print("Draw")
    elif sum(hand1) > sum(hand2):
      print("Winner")
    elif sum(hand1) < sum(hand2):
      print("Lose")

  else:
    if sum(hand1) > sum(hand2):
      print("Lose, you went bust")
    elif sum(hand1) < sum(hand2):
      print("Win, dealer went bust")

  blackjack()
  
def collect_cards(hand):
  '''Adds a random card to the hand'''
  hand += random.sample(cards, 1)
  return hand

def ace_checker(hand):
  '''If score over 21 converts aces from 11 to 1'''
  if 11 in hand and sum(hand) > 21:
    hand.remove(11)
    hand.append(1)
  return hand
    
def blackjack():
'''Need to clear up print statements'''
  game_on = True
  
  while game_on:
    choice = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    user_hand.clear(), dealer_hand.clear()
    clear()
  
    if choice == 'y':
      print(logo)
      
      for x in range(2):
        collect_cards(user_hand), collect_cards(dealer_hand)
  
      if sum(dealer_hand) < 17:
          '''Checks if dealer has hand larger than 17'''
          collect_cards(dealer_hand)
  
      if sum(user_hand) > 21 or sum(dealer_hand) > 21:
        '''Checks if user or dealer has elevens'''
        #print(f'ace checker activated user: {user_hand} and dealer: {dealer_hand}')
        ace_checker(user_hand), ace_checker(dealer_hand)
        
        if sum(dealer_hand) < 17:
          collect_cards(dealer_hand)
          
        if sum(user_hand) > 21 or sum(dealer_hand) > 21:
          '''if any are still over 21 they are bust'''
          #print(f'bust checker activated user: {user_hand} and dealer: {dealer_hand}')
          print(f"  Your cards {user_hand}, current score: {sum(user_hand)}")
          print(f"  Computer's first card: {dealer_hand[0]}, psst dealers full hand: {dealer_hand}")
          check_count(user_hand, dealer_hand)
          
      print(f"  Your cards {user_hand}, current score: {sum(user_hand)}")
      print(f"  Computer's first card: {dealer_hand[0]}, psst dealers full hand: {dealer_hand}")
      
      while choice == 'y' and (sum(user_hand) < 21 and sum(dealer_hand) < 21):
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if choice == 'y':
          collect_cards(user_hand)
  
          if sum(user_hand) > 21 or sum(dealer_hand) > 21:
            '''Checks if user or dealer has elevens'''
            #print(f'ace checker activated user: {user_hand} and dealer: {dealer_hand}')
            ace_checker(user_hand), ace_checker(dealer_hand)
            
            if sum(user_hand) > 21 or sum(dealer_hand) > 21:
              '''if any are still over 21 they are bust'''
              #print(f'bust checker activated user: {user_hand} and dealer: {dealer_hand}')
              print(f"  Your cards {user_hand}, current score: {sum(user_hand)}")
              print(f"  Computer's first card: {dealer_hand[0]}, psst dealers full hand: {dealer_hand}")
              check_count(user_hand, dealer_hand)
  
          if choice == 'y':
            print(f"  Your cards {user_hand}, current score: {sum(user_hand)}")
            print(f"  Computer's first card: {dealer_hand[0]}, psst dealers full hand: {dealer_hand}")
          
        elif choice == 'n' or sum(user_hand) > 21 or sum(dealer_hand) > 21:
          print(f"  Your cards {user_hand}, current score: {sum(user_hand)}")
          print(f"  Computer's first card: {dealer_hand[0]}, psst dealers full hand: {dealer_hand}")
          check_count(user_hand, dealer_hand)
        else:
          print("Incorrect Input")
          choice = 'y'
  
    elif choice == 'n':
      clear()
      
    else:
      print("Wrong Input\n")

blackjack()