# UX improvements and final touches

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']





def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
            shift_amount *= -1
    for letter in start_text:
        # 3 - What happens if the user enters a number / symbol / space ?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded ?
        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
    print(f"The {direction}d text is {end_text}.")

# 1 - Import and print the logo from Art.py when the program start.

# 4 - Find a way to ask the user if they want to restart the cipher program.
# e.g. Type 'yes' if you want to go again, otherwise type 'no'.
# If they type 'yes', then ask for the direction/text/shift again and call the caesar() function again.
# Hint : create a new function that calls itself if they type 'yes'.
# Create variable quit_program = False ?

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# 2 - What if the user enters a shift that is greater than the number of letters in the alphabet ?
# Hint : Think about how you can use the modulus.


caesar(start_text = text, shift_amount = shift, cipher_direction = direction)