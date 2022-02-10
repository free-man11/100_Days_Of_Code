# INSTRUCTION
# WRITE A PROGRAM THAT INTERPRETS THE BODY MASS INDEX (BMI)BASED ON A USER'S WEIGHT AND HEIGHT


# THIS BMI SHOULD TELL THE INTERPRETATION OF THEIR BMI BASED ON THE BMI VALUE

# IF THE VALUE IS UNDER 18.5,THEY ARE UNDERWEIGHT
# IF THE VALUE IS OVER 18.5 BUT BELOW 25 THEY HAVE A NORMAL WEIGHT
# IF THE VALUE IS OVER 25 BUT BELOW 30 THEY ARE OVERWEIGHT
# IF THE VALUE IS OVER 30 BUT BELOW 35 THEY ARE OBESE
# IF THE VALUE IS ABOVE 35 THEY ARE CLINICALLY OBESE


# SO LET'S START

height = float(input("enter your height in m:\n"))
weight = float(input("enter your weight in kg:\n"))


bmi = round(weight / height ** 2)
bmi = 22
if bmi < 18.5:
    print("Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print("Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print("Your bmi is {bmi}, you are over overweight")
elif bmi < 35:
    print("Your bmi is {bmi}, you are obese")
else:
    print("Your bmi is {bmi}, you are clinically obese")
