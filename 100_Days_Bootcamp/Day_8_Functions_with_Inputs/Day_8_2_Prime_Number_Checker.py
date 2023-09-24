# Write a function that checks whether if the number passed into it is a prime number or not.


# --- My answer ---
def prime_checker(number):
    is_prime = True
    
    x = 2
    while is_prime and x < number:
        if number % x == 0:
            is_prime = False
        x += 1    
    
    if is_prime == True:    
        print("It is a prime number.")
    else:
        print("It is not a prime number.")


n = int(input("Check this number: "))

prime_checker(number = n)

# --- Teacher's answer ---

'''def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))

prime_checker(number = n)
'''