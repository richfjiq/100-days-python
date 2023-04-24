#from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bids = {}

should_continue = True

def find_highest_bider(bidding_record):
  max_bid = 0
  winner = ""
  
  for person in bids:
    if bidding_record[person] > max_bid:
      max_bid = bids[person]
      winner = person
      
  print(f"The winner is {winner} with a bid of ${max_bid}")
  
while should_continue:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  other_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  bids[name] = bid
  if other_bids == "no":
    should_continue = False
    print("Game over")
#  clear()

find_highest_bider(bids)

    
