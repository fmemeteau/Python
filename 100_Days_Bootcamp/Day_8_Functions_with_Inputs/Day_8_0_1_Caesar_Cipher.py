# As we insert data into a function, we basically create a new variable
# For the variable 'something = 123', something is the parameter (the name of the data beging passed in),
# while 123 is the argument (the actual value of the data)

# Positional and keyword arguments. my_function(a, b) is positional. First value given is passed into a then second into b.
# Keyword argument is my_function(a=1, b=2). I could intervert them both, the value would still go into the right variable


# Let's create a Ceasar Cipher ! By shifting the letter by a certain amount, we'll encode our text.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# --- My answer, which doesn't work ---
# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
'''def encrypt(text, shift):
    # Inside the 'encrypt' function, shift each letter of the 'text' forward in the alphabet by the 
    # shift amount and print the encrypted text.
    for char in text:
        code = []
        x = 0
        index = 0
        while char != alphabet[x - 1]:
            print(x)
            print(char)
            print(alphabet[x])
            x += 1
            print(f"Index is {index}")
        code[index] = alphabet[(x - 1) + shift]
        index += 1
    print(f"The code is {code}")
        
    
# Call the encrypt function and pass in the user inputs. You should be able to test the code.
encrypt(text, shift)'''


# --- Teacher's answer ---
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"The encoded text is {cipher_text}") 

encrypt(plain_text = text, shift_amount = shift)