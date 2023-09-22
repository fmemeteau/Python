import random
# Here, either simply import the file or specify the variable imported from the file
# So, either import X or from X import Y
from Day_7_5_Hangman_Words import word_list
import Day_7_5_Hangman_Words

# Same is said about the import of the Art file
import Day_7_5_Hangman_Art
from Day_7_5_Hangman_Art import stages, logo

from os import system, name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for Mac and Linux
    else:
        _ = system('clear')

# Here, the initialisation of chosen_word depends on how you imported the file / variable
# If you only imported the file, you have to specify nameFile.variable.
# If you did a from 'file' import 'variable', you can just specify the name of the variable
chosen_word = random.choice(Day_7_5_Hangman_Words.word_list)
chosen_word = random.choice(word_list)

word_length = len(chosen_word)

lives = 6
end_of_game = False

print(logo)

# Testing code
print(f"The solution is {chosen_word}.")

display = []

for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}")
        

    for position in range(word_length):
        char = chosen_word[position]
        
        
        if guess == char:
            display[position] = char

    

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")       

    if "_" not in display:
        end_of_game = True
        print("You win")

# From the way you imported either the file or the variable will depend the print down there
    print(stages[lives])

    
