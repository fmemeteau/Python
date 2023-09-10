print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

crossroad = input('You\'re at a cross road. Where do you want to go ? \nType "left" or "right". ').lower()

if crossroad == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat or "swim" to swim accross. ').lower()
    if lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\nWhich color do you choose ? ").lower()
        if door == "yellow":
            print("You win !")
        elif door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room full of beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")
