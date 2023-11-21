# The deck is unlimited in size.
# There are no jokers.
# The Jack / Queen / King all count as 10
# Use the following list as the deck of cards : 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn
# Cards are not removed from the deck as they are drawn

import random

def draw_card(list, number_to_pick):
    if number_to_pick == 1:
        list.append(random.choice(cards))
    elif number_to_pick == 2:
        list.append(random.choice(cards))
        list.append(random.choice(cards))

def blackjack():
    print("Blackjack ! You win !")
    start_again = input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ")
    if start_again == 'y':
        return game()
    elif start_again == 'n':
        new_game = False
    

    
def game():
    new_game = True
    while new_game == True:
        my_cards = []
        draw_card(my_cards, 2)
        my_total = my_cards[0] + my_cards[1]

        computer_cards = []
        draw_card(computer_cards, 1)
        computer_total = computer_cards[0]

        print(f"Your cards: {my_cards}")
        print(f"Computer's first card: {computer_cards}")

        if my_total == 21:
            blackjack()
            break

        choice = input("Type 'y' to get another card, type 'n' to pass: ")

game()