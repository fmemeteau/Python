# This time, we will decode the encoded text


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"The encoded text is {cipher_text}") 


# 1 - Create the function 'decrypt' that takes the 'text' and 'shift' as inputs
def decrypt(cipher_text, shift_amount):
    # 2 - Inside the 'decrypt' function, shift each letter of the 'text' backwards in the alphabet 
    # by the shift amount and print the decrypted text 
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}.")




# 3 - Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# Then call the correct function based on that direction variable.

if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(cipher_text = text, shift_amount = shift )
