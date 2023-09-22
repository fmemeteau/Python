# Step 4

import random
import Day_7_5_Hangman_Art
import Day_7_5_Hangman_Words

# 1 - Update the word list to use the "word_list" from hangman_words.py
# Delete the variable 'word_list

Day_7_5_Hangman_Words.word_list

chosen_word = random.choice(Day_7_5_Hangman_Words.word_list)
word_length = len(chosen_word)

lives = 6
end_of_game = False

# 3 - Import the logo from hangman_art.py and print it at the start of the game

print(Day_7_5_Hangman_Art.logo)

# Testing code
print(f"The solution is {chosen_word}.")

# Create blanks
display = []

for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

# 4 - If the user user has entered a letter they've already guessed, print the letter and let them know



 # Check guessed letter
    for position in range(word_length):
        char = chosen_word[position]
        
        if guess in display:
            print(guess)
            print("You've already guessed the letter.")
        
        if guess == char:
            display[position] = char

    

    if guess not in chosen_word:
        # 5 - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word
        print(f"You guessed {guess},  that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")       

# Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win")

    
# 2 - import the stage from hangman_art.py and make this error go away.
    print(Day_7_5_Hangman_Art.logo[lives])

    
