# This program will generate random passwords, using letters, both lowercase and uppercase, as well as numbers and symbols

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many symbols would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# --- My answer ---
# I got lost in using a concatenated list which won't work when trying to create a string from it
letters_choice = random.sample(letters, nr_letters)
numbers_choice = random.sample(numbers, nr_numbers)
symbols_choice = random.sample(symbols, nr_symbols)


print(letters_choice)
print(numbers_choice)
print(symbols_choice)

added_password = [letters_choice + numbers_choice + symbols_choice]

password = random.sample(added_password, len(added_password))

print(password)
print(type(password))
# We change the password as a list into a string that will be given to the end user

final_password =""
for char in password:
    final_password += char

print(f"Your password is: {final_password}")


# --- Teacher's easy answer, dealing with a string of letters, then numbers and then symbols
'''
password =""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

print(password)

# --- Teacher's hard answer, dealing with lists in order to shuffle the characters composing the final password
password_list = []

for char in range(1, nr_letters + 1):
    #password_list += random.choice(letters)    Working with lists, why not use the append() function ?
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    #password_list += random.choice(numbers)
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    #password_list += random.choice(symbols)
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password =""
for char in password_list:
    password += char

print(f"Your password is: {password}")

'''