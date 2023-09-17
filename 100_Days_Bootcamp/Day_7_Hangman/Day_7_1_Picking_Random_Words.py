# Step 1

word_list = ["ardvark", "baboon", "camel"]

import random
# Randomly choose a word from the word_list and assign it to a variable called chosen_word

chosen_word = random.choice(word_list)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
guess = input("Guess a letter: ").lower()

# Check if the letter the user guessed is one of the letters in the chosen_word
for char in chosen_word:
    if guess == char:
        print("Right")
    else:
        print("Wrong")