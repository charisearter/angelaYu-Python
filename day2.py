# Day 2 Angela Yu - Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# GEt tip % is percent/100 * bill then add bill
tip_as_percent = tip / 100
amount_of_tip = int(bill * tip_as_percent)
total_amount = bill + amount_of_tip
split_amount = total_amount / people
final_amount = round(split_amount, 2)




print(f"Each person should pay: ${final_amount}")