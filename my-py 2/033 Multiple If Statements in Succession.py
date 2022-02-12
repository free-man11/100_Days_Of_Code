# MULTIPLE IF

# if condition1:
#    do A
# if condition2:
#     do B
# if condition3:
#     do C



print("Welcome t the roller-coaster!")
height = int(input("what is your height in cm?\n"))
bill = 0
if height >= 120:
    print("you can run the roller-coaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo taken?\n Y or N.")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is {bill}$")

else:
  print("sorry you have to grow taller before you can ride")
