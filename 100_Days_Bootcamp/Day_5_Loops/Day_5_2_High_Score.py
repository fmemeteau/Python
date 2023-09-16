# This program will calculate the highest score from a list of student scores.
# Do not use the max() function. The goal of this exercise is to find a solution using the for loop.

student_scores = input("Input  list of student scores, separated by a space: \n").split()


for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


print(student_scores)

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
