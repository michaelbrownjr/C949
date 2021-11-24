# my_list = [5, 10, 15, 20, 25, 30, 35, 40]
# my_list = [(i+5) for i in my_list]

# print(my_list)

def Average(list):
    return sum(list) / len(list)

inp = input('Enter numbers:')
my_list = [int(i) for i in inp.split()]

print(my_list)

#Find the sum of the row with the smallest sum in a 2-dimensional table.
my_list = [[5, 10, 15], [2, 3, 16], [100]]
min_row = min([sum(row) for row in my_list])
print(min_row)

#Find the sum of each row in a 2-dimensional list.
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = [sum(row) for row in my_list]
print(sum_list)

avg_list = [round((Average(row))) for row in my_list]
print(avg_list)