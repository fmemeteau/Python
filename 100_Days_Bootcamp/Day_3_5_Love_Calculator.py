print("Welcome to the Love Calcultor !")
name1 = (input("What is your name? \n")).lower()
name2 = (input("What is their name? \n")).lower()

combined_name = name1 + name2
lowered_name = combined_name.lower()

t = lowered_name.count("t")
r = lowered_name.count("r")
u = lowered_name.count("u")
e = lowered_name.count("e")
true_score = t + r + u + e

l = lowered_name.count("l")
o = lowered_name.count("o")
v = lowered_name.count("v")
e = lowered_name.count("e")
love_score = l + o + v + e


final_score = int(str(true_score) + str(love_score))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >=40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
