from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return EASY_LEVEL_TURNS
  elif difficulty == 'hard':
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  attempts = set_difficulty()
  
  random_number = random.randint(1, 100)
  guess_number = 0

  while random_number != guess_number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))
    attempts = check_answer(guess_number, random_number, attempts)
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      return
  
game()