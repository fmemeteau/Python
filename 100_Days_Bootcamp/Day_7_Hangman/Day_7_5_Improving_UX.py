# Step 4

import random
# Update the word list to use the "word_list" from hangman_words.py
# Delete the variable 'word_list
end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6

# Testing code
print(f"The solution is {chosen_word}.")

# Create blanks
display = []

for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

 # Check guessed letter
    for position in range(word_length):
        char = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {char}\n Guessed letter: {guess}")
        if guess == char:
            display[position] = char


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")       

# Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win")

    

    print(stages[lives])

    
