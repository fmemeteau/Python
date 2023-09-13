names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

import random

# By using a random index on the list
buyer_name = names[random.randint(0, len(names) - 1)]

print(buyer_name + " is going to buy the meal today !")

# --- By using the "choice" function, coming with the random module ---

buyer_name = random.choice(names)

print(buyer_name + " is going to buy the meal today !")