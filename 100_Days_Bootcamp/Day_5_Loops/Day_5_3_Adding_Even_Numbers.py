# This small exercise adds up every number from 1 to 100
'''total = 0
for number in range(1, 101):
    total += number

print(total)
  '''
# Day_5_3 exercise. We are to add every even numbers from 1 to 100 included.

# ---First way, with use of the modulo---
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(total)

# ---Second way, by modifying the step of range()
total = 0
for number in range(2, 101, 2):
    total += number
print(total)