# Step 2

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f"The solution is: {chosen_word}")

# Create an empty list called display. For each letter in the chosen_word, add a "_" to "display"
# If the chosen word is "apple", display should be 5 "_" representing each letter to guess.
display = []

for char in range(len(chosen_word)):
    display.append("_")                  

    # Another for loop is possible:
    # for char in chosen_word:
    #     display += "_"

guess = input("Guess a letter: ").lower()

# Loop through each position in the chosen_word. If the letter at that position matches "guess", 
# then reveal that letter in the display at that position

x = 0
for char in chosen_word:
    x += 1
    if guess == char:
        display[x] = guess
    
    # Another for loop:
    # for position in range(len(chosen_word)):
    #     letter = chosen_word[position]
    #     if letter == guess:
    #         display[position] = letter


# Print "display" and you should see the guessed letter in the correct position and every other letter replace with "_"
# Getting the user to guess the next letter will be tackled in Step 3
print(display)