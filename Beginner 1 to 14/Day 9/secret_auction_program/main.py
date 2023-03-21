from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
all_bids = {}

def bid_compare(name, bid):
  all_bids[name] = bid
  print(all_bids)

print(logo)
print("\nWelcome to the secret auction program. \n")

active = True

while active:
  name = input("What is your name?: ")
  bid = int(input("what's your bid?: $"))

  bid_compare(name, bid)

  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if more_bidders == 'no':
    active = False
    clear()
  else:
    clear()

winner = ""
compare = 0

for people in all_bids:
  bids = all_bids[people]
  if all_bids[people] > compare:
    compare = all_bids[people]
    winner = people

print(f"Winner is {winner} with a bid of ${compare}")
  