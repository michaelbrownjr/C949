# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Colin': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Mary': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

highest_points = 0
highest_gpa = 0
# Finds the student with the highest Total Points
for names, grades in student_grades.items():
    total_points = sum(grades)
    if total_points > highest_points:
      highest_student = names
      highest_points = total_points

print()
# Finds the student with the highest GPA
for names, grades in student_grades.items():
    student_gpa = sum(grades)/(len(grades))
    if student_gpa > highest_gpa:
      highest_gpa_student = names
      highest_gpa = student_gpa


print('%s has the highest total of grades with %d' % (highest_student, highest_points))
print('%s has the highest GPA with %d' % (highest_gpa_student, highest_gpa))
