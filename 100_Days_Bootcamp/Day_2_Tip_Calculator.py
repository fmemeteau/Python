print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

people = (int(input("How many people to split the bill? ")))
total = round((bill + (bill * percentage) / 100) / people, 2)
print(f"Each person should paym: ${total}")

# There may be problems with the decimals after the comma. Such as 0 being not shown or a rounding not workind approprietely
# The end value should then be transformed as a string and formated in a specific way, like :
# final_amount = "{}:.2f}".format(total)
