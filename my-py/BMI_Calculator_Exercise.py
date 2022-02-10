height = float(input("enter your height in m:\n"))
weight = float(input("enter your weight in kg:\n"))


weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2
print(bmi)

# IF YOU WANT THIS AS AN INTEGER () WHOLE NUMBER

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

