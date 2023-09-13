# These challenge is sets in order to test your ability to use the for loop.
# Do not use either the len() or the sum() function

print("This program will calculate the average height from a group of students.")
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

total_height = 0
number_of_students = 0

# By using this for loop, we are basically doing the same thing the sum() and len() function
# We calculate the sum of every heights with total_height and the length of the list with number_of_students
for height in student_heights:
    number_of_students += 1
    total_height += height

average_height = round(total_height / number_of_students)
print(f"The average height of the group of students is {average_height}")