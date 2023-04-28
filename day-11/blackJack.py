from art import logo
import random
# from replit import clear
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

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def black_jack():
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  
  if play == "y":
    # clear()
    
    player_cards = []
    computer_cards = []
    
    for _ in range(2):
      player_cards.append(deal_card())
      computer_cards.append(deal_card())
    
    player_sum = calculate_score(player_cards) 
    computer_sum = calculate_score(computer_cards)
    
    print(logo)
    print(f"  Your cards: {player_cards}, current score: {player_sum}")
    print(f"  Computer's first card: {computer_cards[0]}")
    
    if player_sum == 0 or computer_sum == 0:
      another_card = "n"
    else:
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    
    while another_card == "y":
      player_cards.append(deal_card())
      player_sum = calculate_score(player_cards)
      
      while computer_sum < 17:
        computer_cards.append(deal_card())
        computer_sum = calculate_score(computer_cards)
        
      print(f"  Your cards: {player_cards}, current score: {player_sum}")
      print(f"  Computer's first card: {computer_cards[0]}")

      if player_sum > 21 or computer_sum == 21:       
        another_card = "n"   
      elif computer_sum > 21 or player_sum == 21:
        another_card = "n"
      else:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        
    while computer_sum < 17:
        computer_cards.append(deal_card())
        computer_sum = calculate_score(computer_cards)
  
    print(f"  Your final hand: {player_cards}, final score: {player_sum}")
    print(f"  Computer's final hand: {computer_cards}, final score:  {computer_sum}")
      
    if player_sum > 21:    
      print("You went over. You lose 😤")          
    elif computer_sum > 21:
      print("Opponent went over. You win 😃")
    elif computer_sum == player_sum:
      print("Draw 🙃")
    elif computer_sum > player_sum or computer_sum == 0:
      print("You lose 😤")
    elif player_sum > computer_sum or player_sum == 0:
      print("You win 😃")
  
      
    black_jack()
        

black_jack()
