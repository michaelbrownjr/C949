passing_grades = {
    'A': 100,
    'B': 90,
    'C': 80,
}

# student_grdes = input('Enter in student\'s grade:')

#if student_grdes in passing_grades:
 #   print('Student has a passing grade in the class')
#else:
 #   print('Student is failing the class')

for grade in passing_grades:
    print('%s is a score %d' % (grade, passing_grades[grade]))