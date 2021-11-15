#Using the strm, type, and id functions to learn about the parameters. 

birthday_year = 1986
birthday_month = 'April'
birthday_day = 22

print('birthday_year -->')
print(' value:', str(birthday_year))
print(' type:', type(birthday_year))
print(' id:', id(birthday_year))

print('\nbirthday_month -->')
print(' value:', str(birthday_month))
print(' type:', type(birthday_month))
print(' id:', id(birthday_month))

print('\nbirthday_day -->')
print(' value:', str(birthday_day))
print(' type:', type(birthday_day))
print(' id:', id(birthday_day), '\n')

white_house_coordinates = (38.8977, 77.0366)
print('Coordinates:', white_house_coordinates)
print('Tuple length:', len(white_house_coordinates))

# Access tuples via index
print('\nLatitude:', white_house_coordinates[0], 'north')
print('Longitude:', white_house_coordinates[1], 'west\n')

# Error. Tuples are immutable
#white_house_coordinates[1] = 50

#Difference between an array and list
newList = [4, 5, 6, 5]
#divisionList = newList/3
print(newList)
print(type(newList))

#Dictionary
student_grades = {'Michael': 'A', 'Fatima': 'B', 'Jamil': 'C', 'Andrew':'D'}
print(student_grades)
student_grades ['Jamil'] = 'B'
print(student_grades)
