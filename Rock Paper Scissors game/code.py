Make a rock, paper, scissors game.

# You'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. 
# This will make it easy to print them out to the console.

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
images = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = random.randint(0,2)

if your_choice > 2 or your_choice < 0:
    print('Enter a valid number')
else:
    print(f'You chose {images[your_choice]}')
    print(f'Computer chose {computer_choice}')
    print(f'Computer chose {images[computer_choice]}')
    if your_choice == computer_choice:
        print('You are in a tie')
    elif your_choice == 0 and computer_choice == 2:
        print('You Win')
    elif your_choice == 2 and computer_choice == 0:
        print('You Lose')
    elif your_choice < computer_choice:
        print('You Lose')   
    elif your_choice > computer_choice:
        print('You Win')