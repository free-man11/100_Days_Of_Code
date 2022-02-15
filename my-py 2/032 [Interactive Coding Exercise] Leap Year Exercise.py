# THIS IS A DIFFICULT CHALLENGE

# A program that works out weather if a given year is a leap year . A normal year has 365 days , A leap year with 366
# days, with extra day of February.

# A year that is evenly divisible by 4 is called a LEAP YEAR

# A year that is evenly divisible by 4 is called a LEAP YEAR
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also divisible by 400

year = int(input("Which year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
