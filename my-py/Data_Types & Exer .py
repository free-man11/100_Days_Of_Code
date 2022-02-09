
# STRINGS


# we now use an indend to position the numb a word has
print("hello"[0])


# strings don't operate with operational signs
print("123" + "345")



# INTEGERS---Numbers without decimal points
print(123 + 234)

123_456_789


# FLOAT---Numbers with decimal points
print(3.22)


# BOOLEAN---Always comes with True & False

True
False






# EXERCISE

# Write a program that adds the digits ina 2 digit number .eg. if the input was 35,then the output should be 3+5=8


two_digit_number = input("Type a two digit number\n")

# Check the data type of two_digit_number
#print(type(two_digit_number))

# Get the first and second digits using subscripting then convert string to int
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# Add the two digits together
result = int(first_digit) + int(second_digit)
print(result)
