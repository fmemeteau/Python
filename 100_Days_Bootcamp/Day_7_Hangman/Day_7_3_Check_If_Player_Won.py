# Step 3

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f"The solution is {chosen_word}")

# Create blanks
display = []

for _ in range(word_length):
    display += "_"

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and "display" 
# has no more blanks. Then you can tell the user they've won.

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        char = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {char}\n Guessed letter: {guess}")
        if guess == char:
            display[position] = char

    print(display)       

    if "_" not in display:
        end_of_game = True
        print("You win")
