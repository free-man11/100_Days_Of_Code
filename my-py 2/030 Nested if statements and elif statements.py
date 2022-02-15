 if condition:
    if another condition:
        do this                 # The one inside the main if/else statement is called the (Nested If / Else)
    else:
        do this
 else:
      do this



 LET'S START

 print("Welcome t the rollercoaster!")
 height = int(input("what is your height in cm?\n"))

 if height >= 120:
    print("you can run the rollercoaster!")
    age = int(input("What is your age?/n"))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print("sorry you have to grow taller before you can ride")



 But what if the ticket owner comes and say
 people who are < 12 should pay = $5
 people who are in between 12-18 should pay $7
 people who are > 18 should pay $12

 In here there are three conditions espectially (people who are in between 12-18 should pay $7 )
 So we then use (If/elif/Else) Statement to do this

 if condition1:
    do A
elif condition2:
    do B
 else:
    do this


# SO LET'S TRY THIS AND SEE

print("Welcome t the rollercoaster!")
height = int(input("what is your height in cm?\n"))
if height >= 120:
    print("you can run the rollercoaster!")
    age = int(input("What is your age?/n"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
  print("sorry you have to grow taller before you can ride")
ds

