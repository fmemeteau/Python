def prime_number_checker(number):
    i = 2
    while number % i != 0:
        i +=1
    
    if i == number:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


prime_number_checker(11)