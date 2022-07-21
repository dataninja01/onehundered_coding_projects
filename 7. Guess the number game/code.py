# 1. Choosing a number between 1 and 100
# 2. Make a function to set difficulty
# 3. Let the user choose a number
# 4. Function to check the user's guess agaianst the actual answer
# 5. Track the number of attempts if the guess is wrong reduce it by 1
# Repeat the guessing functionality if they get it wrong
import random
from art import number_game_logo
from replit import clear
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def guess_number():
    return random.randint(1, 100)


def set_difficulty():
    difficulty_level = input("Choose a difficulty level. Type \"easy\" or \"hard\": ").lower()
    if difficulty_level == "easy":
        return EASY_ATTEMPTS
    elif difficulty_level == "hard":
        return HARD_ATTEMPTS

def compare_answer(guess, answer, attempts):
    """Checks the answer against the guess and return the number of turns"""
    if guess > answer:
        print("Too High")
        return attempts - 1
    elif guess < answer:
        print("Too Low")
        return attempts - 1
    else:
        print(f"You got it! The answer was {guess}")

def game():
    print("Welcome to the Number Guessing game")
    print(number_game_logo)
    answer = random.randint(1, 100)
    attempts = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {attempts} remaining to guess the number") 
        guess = int(input("Make a guess:"))
        attempts = compare_answer(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose")
        elif guess != answer:
            print("Guess again")

while (input("Do you want to play guessing the number game? 'y' or 'n': ")).lower() == 'y':
    clear()
    game()