#Name: Olayemi Olawale Abdulganiyu
#Matric No: 16/30GN073

courses = int(input("Enter the number of courses you have registered for in this semester: "))

# Create lists to store the course codes, credit units, and scores
course_codes = []
credit_units = []
scores = []

# Loop through the courses to get the course codes, credit units, and scores
for i in range(courses):
    course_code = input("Enter the course code for course {}: ".format(i + 1))
    credit_unit = int(input("Enter the credit unit for course {}: ".format(i + 1)))
    score = int(input("Enter your score for course {}: ".format(i + 1)))
    
    course_codes.append(course_code)
    credit_units.append(credit_unit)
    scores.append(score)

# Calculate the GPA
total_points = 0
total_credit_units = 0
for i in range(courses):
    score = scores[i]
    credit_unit = credit_units[i]
    
    if score >= 70 and score <= 100:
        grade_point = 5
    elif score >= 60 and score <= 69:
        grade_point = 4
    elif score >= 50 and score <= 59:
        grade_point = 3
    elif score >= 46 and score <= 49:
        grade_point = 2
    elif score >= 40 and score <= 45:
        grade_point = 1
    else:
        grade_point = 0
    
    total_points += grade_point * credit_unit
    total_credit_units += credit_unit

gpa = total_points / total_credit_units

# Output the transcript
print("\nTranscript")
print("-" * 20)
print("Course Code\tCredit Unit\tScore\tGrade Point")
for i in range(courses):
    course_code = course_codes[i]
    credit_unit = credit_units[i]
    score = scores[i]
    
    if score >= 70 and score <= 100:
        grade_point = 5
    elif score >= 60 and score <= 69:
        grade_point = 4
    elif score >= 50 and score <= 59:
        grade_point = 3
    elif score >= 46 and score <= 49:
        grade_point = 2
    elif score >= 40 and score <= 45:
        grade_point = 1
    else:
        grade_point = 0
    
    print("{}\t\t{}\t\t{}\t\t{}".format(course_code, credit_unit, score, grade_point))

print("\nGPA: {:.2f}".format(gpa))