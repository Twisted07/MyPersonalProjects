'''
Name: Idris Abdullateef Adebowale
Matric No: 16/30GN041
Department: Materials and Metallurgical Engineering
Course code: MEE 505
Assignment: GPA Calculator
'''

'''
This program calculates the GPA a student by taking in the values of...
the number of courses (c) offered in a semester,
the course codes (c_code),
the credit units (c_units),
the scores (s)
and grade point (gp), then
Outputing:
the grade point average (gpa)
'''

# Take input of number of courses (c)
courses = input("How many courses did you register for in this semester?(number only) ")
try: 
    c = int(courses)
except:
    c = int(input("You have entered a wrong input format. Answer in digits only!\n How many courses did you register for this semester? "))

# Create empty lists to store the course codes, credit units, and scores
course_codes = []
credit_units = []
scores = []

# Loop through the courses to get the course codes, credit units, and scores
for i in range(c):
    c_code = input("Enter the course code for course {}: ".format(i + 1))
    credit_unitss = input("Enter the credit unit for course {}: ".format(i + 1))
    try:
        c_unit = int(credit_unitss)
    except:
        c_unit = int(input(f"You did not enter a valid input. Please enter number only.\nEnter the credit unit for course {i+1}: "))
    s = int(input("Enter your score for course {}: ".format(i + 1)))

#Add the results to the lists    
    course_codes.append(c_code)
    credit_units.append(c_unit)
    scores.append(s)

# Calculate the GPA
total_points = 0
total_credit_units = 0
for i in range(c):
    s = scores[i]
    c_unit = credit_units[i]
    
    if s >= 70 and s <= 100:
        gp = 5
    elif s >= 60 and s <= 69:
        gp = 4
    elif s >= 50 and s <= 59:
        gp = 3
    elif s >= 46 and s <= 49:
        gp = 2
    elif s >= 40 and s <= 45:
        gp = 1
    else:
        gp = 0
    
    total_points += gp * c_unit
    total_credit_units += c_unit

gpa = total_points / total_credit_units

# Print the transcript
print("\nTranscript")
print("-" * 20)
print("Course Code\tCredit Unit\tScore\tGrade Point")

for i in range(c):
    c_code = course_codes[i]
    c_unit = credit_units[i]
    s = scores[i]
    if s >= 70 and s <= 100:
        gp = 5
    elif s >= 60 and s <= 69:
        gp = 4
    elif s >= 50 and s <= 59:
        gp = 3
    elif s >= 46 and s <= 49:
        gp = 2
    elif s >= 40 and s <= 45:
        gp = 1
    else:
        gp = 0
        
    print("{}\t\t{}\t\t{}\t\t{}".format(c_code, c_unit, s, gp))

print("\n\nGPA: {:.2f}".format(gpa))