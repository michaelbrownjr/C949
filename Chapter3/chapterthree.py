names = ['Michael', 'Fatima', 'Joy', 'Geraldine']

print('Lets add some more names to the list. Add a name: ')
newName = input()

names.append(newName)
print('There are now ', len(names), ' names in the list.')
print('The new name added was,', newName)