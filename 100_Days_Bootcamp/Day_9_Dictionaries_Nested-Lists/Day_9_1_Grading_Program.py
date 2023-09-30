# You have access to a database of student_scores in the format of a dictionary. The keys are the names 
# of the students and the values are their exam scores. Write a program that converts their scores to 
# grades.
# By the end of the program, you should have a new dictionary called student_grades containing the names as keys and their grades as values.

# This is the scoring criteria:
#   91 - 100 : "Outstanding"
#   81 - 90 : "Exceeds Expectations"
#   71 - 80: "Acceptable"
#   70 or lower: "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

# --- My answer ---
'''
student_grades = {}

for x in student_scores:
    if student_scores[x] > 90:
        student_grades[x] = "Outstanding"
    elif student_scores[x] > 80:
        student_grades[x] = "Exceeds Expectations"
    elif student_scores[x] > 70:
        student_grades[x] = "Acceptable"
    elif student_scores[x] <= 70:
        student_grades[x] = "Fails"
    #print(student_grades[x])

print(student_grades)
'''

# --- Teacher's answer ---
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    elif score <= 70:
        student_grades[student] = "Fail"

print(student_grades)