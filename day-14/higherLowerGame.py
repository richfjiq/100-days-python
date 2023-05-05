import random
from art import logo, vs
from game_data import data
# from replit import clear

def compare_strings(a, b):
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

def statements(follower_a, follower_b, guess):
  if follower_a > follower_b:
    return guess == "a"
  else:
    return guess == "b"

def game():
  play = True
  current_score = 0
  while play:
    print(logo)
    
    a = random.choice(data)
    b = random.choice(data)
    if a == b:
      b = random.choice(data)

    if current_score != 0:
      print(f"You're right! Current score: {current_score}")
    compare_strings(a, b)
  
    option = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    follower_count_a = a['follower_count']
    follower_count_b = b['follower_count']
  
  
    is_correct = statements(follower_count_a, follower_count_b, option)
    if is_correct:
      current_score += 1
    else:
      play = False
    # clear()

  print(logo)
  print(f"Sorry, that's wrong. Final score: {current_score}")

game()