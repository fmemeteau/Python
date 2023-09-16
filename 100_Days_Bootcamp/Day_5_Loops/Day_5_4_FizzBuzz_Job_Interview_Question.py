# FizzBuzz is a game in which a group of people count from 1 to 100 aloud in turn
# Whenever a number is divided by 3, instead of saying the number, the person says "Fizz"
# Whenever a number is divided by 5, instead of saying the number, the person says "Buzz"
# And whenever a number is divided by both 3 and 5, e. g. 15, instead of saying the number, the person says "Buzz"

for number in range(1, 101):
    # Begin by numbers divisibable by both 3 and 5
    # Doing with order, beginning by 3, would result in TRUE, thus skipping the 'both 3 and 5' condition
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

