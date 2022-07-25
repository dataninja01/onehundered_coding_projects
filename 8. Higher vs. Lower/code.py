### Higher-lower game
# Display art
# Generate random account from game data
# Format account data into pritable format
# Ask user for a guess
# Check if user is correct
# Get follower count of each account
# Use if statement to check if user is correct
# Give user feedback on their guess
# Score keeping
# Make th game repeatable
# Making account at position B become the next account at position A
# Clear the screen
import random
from replit import clear
from art import higher_lower_logo, vs
from game import data

def play_game():
  print(higher_lower_logo)

  choice1 = random.choice(data)
  # print(choice)

  first_choice = []

  for i in choice1:
    first_choice.append(choice1[i])

  user_correct = True
  current_score = 0
  while user_correct:

    choice2 = random.choice(data)
    second_choice = []

    for i in choice2:
      second_choice.append(choice2[i])


    if first_choice[0] != second_choice[0]:
      print(F"Compare A: {first_choice[0]}, a {first_choice[2]}, from {first_choice[3]}")
      print(vs)
      print(F"Compare B: {second_choice[0]}, a {second_choice[2]}, from {second_choice[3]}")
      user_response = input("Who has more followers? Type 'A' or 'B' :").upper()   
      if (user_response == 'A' and first_choice[1] > second_choice[1]) or (user_response == 'B' and first_choice[1] < second_choice[1]):       
        current_score += 1
        print(first_choice[1], second_choice[1])
        print(f"You're right! Current score: {current_score}")
        first_choice = second_choice
      elif user_response == 'A' and first_choice[1] < second_choice[1]:
        print(first_choice[1], second_choice[1])
        print(f"Sorry, that's wrong. Final score: {current_score}")
        user_correct = False
      elif user_response == 'B' and first_choice[1] > second_choice[1]:
        print(first_choice[1], second_choice[1])
        print(f"Sorry, that's wrong. Final score: {current_score}")
        user_correct = False

  replay_game = input("Do you want to continue to play? Type 'y' or 'n': ").lower()
  if replay_game == 'y':  
    clear()
    play_game()
  else:
    clear()

play_game()