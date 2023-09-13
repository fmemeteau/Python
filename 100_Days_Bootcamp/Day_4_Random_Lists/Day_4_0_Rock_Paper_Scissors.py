import random

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
---'    ____)____
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

# --- My Answer ---
'''choix = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

bot = random.randint(0, 2)


if choix == 0: #Rock
    print(rock)
    if bot == 0: # Rock
        print("Computer chose: \n")
        print(rock)
        print("Draw")
    elif bot == 2: #Scissors
        print("Computer chose: \n")
        print(scissors)
        print("You win")
    else:
        print("Computer chose: \n")
        print(paper)
        print("You lose")
elif choix == 1: #Paper
    print(paper)
    if bot == 0: #Rock
        print("Computer chose: \n")
        print(rock)
        print("You win")
    elif bot == 2: #Scissors
        print("Computer chose: \n")
        print(scissors)
        print("You lose")
    else:
        print("Computer chose: \n")
        print(paper)
        print("Draw")
elif choix == 2: #Scissors
    print(scissors)
    if bot == 0: #Rock
        print("Computer chose: \n")
        print(rock)
        print("You lose")
    elif bot == 2: #Scissors
        print("Computer chose: \n")
        print(scissors)
        print("Draw")
    else:
        print("Computer chose: \n")
        print(paper)
        print("You win")
else:
    print("Please type 0, 1 or 2")
'''

# ---Teacher's Answer---
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")


