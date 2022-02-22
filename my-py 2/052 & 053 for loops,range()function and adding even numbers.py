# FOR LOOPS

# USING FOR LOOPS WITH THE RANGE FUNCTION

# RANGE
for number in range(1, 11, 2):
    print(number)






# [INTERACTIVE CODING EXERCISES] ADDING EVEN NUMBERS.


total = 0
for number in range(2, 101, 2):
    total += number
print(total)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total)
