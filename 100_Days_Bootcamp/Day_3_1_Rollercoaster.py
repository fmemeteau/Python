height = int(input("What is your height ? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster !")
    age = int(input("What is your age ? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Midlife crisis, have a free ride on us mate.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    want_photo = input("Do you want a photo ? Y or N. ")
    if want_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("You cannot ride the rollercoaster mate.")