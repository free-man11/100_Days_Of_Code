# WE'RE GOING WRITE A CODE THAT IS TO CALCULATE THE HIGHEST SCORE FROM A LIST OF SCORES

student_heights = input("Input a list of students heights\n ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

student_score = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
