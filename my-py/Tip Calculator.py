
# Final project will be like this

# Wel To the tip Calculator
# What was the total bill? $
# What % tip would you like to give? 10,12,or15 ?
# How many people to split the bill ?
# Each person should pay: $0.00


# LETS START

# Wel To the tip Calculator
print("Welcome To the tip Calculator")


# What was the total bill? 10,12,or15 ?
bill = float(input("What was the total bill? $"))

# What % tip would you like to give? 10,12,or15 ?
tip = int(input(" What much tip would you like to give? 10,12,or15 ?"))

# How many people to split the bill ?
people = int(input("How many people to split the bill?"))




# CALCULATION

bill_with_tip = tip / 100 * bill + bill

# or  bill_with_tip = bill * (1 + tip / 100)
print(bill_with_tip)

# or you can go step by step
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# if we want to round any number (33.5) into its two deci figure;we use
# final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")



