#TODO-1 - Randomly choose a word from the word_list and assign it to 
# a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to 
# a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) 
# is one of the letters in the chosen_word.
# https://www.askpython.com/python/python-import-statement
import random
import hangman_art as ha
import hangman_words as hw

print(ha.logo)
lives = 6
end_of_game = False
chosen_word = random.choice(hw.word_list).lower()

#create blanks list
display = []
for i in range(len(chosen_word)):
    display.append("_")

# print(display)

while not end_of_game:
    guess = input('guess a letter ').lower()

    print(chosen_word, guess)
    if guess in display:
        print(f"You have already guessed {guess}")

    # for letter in chosen_word:
    #     if letter == guess:
    #     print('Right')
            
    #     else:
    #         print('Wrong')

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        # print(f'Current position:{i}\n Current letter:{letter}\nGuessed letter: {guess}')
        if letter == guess:
            display[i] = guess
            # print(display)
       

    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            end_of_game = True
            print('You Lose.')

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You have guessed all letters and you win.")
    
    print(ha.stages[lives])