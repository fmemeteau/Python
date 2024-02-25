import random

not_stopped = True
first_list = []
final_list = []

answer = input("Hello, do you intend to populate a list ? y / n : ")

if answer == 'y' and not_stopped:
    while not_stopped:
        choice = input("Please enter data to populate your list : ")
        first_list.append(choice)

        answer2 = input("Do you wish to add another item ? y / n : ")

        if answer2 == 'y':
            not_stopped
        else:
            not_stopped = False
            x = 0

    while x < len(first_list):
        person = random.choice(first_list)
        first_list.remove(person)
        final_list.append(person)

    for p in final_list:
        print(p)
                
else:
    print("Please, type either y or n !")

print("Good Bye !")
    

