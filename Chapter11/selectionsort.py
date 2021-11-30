

def selection_sort(numbers):
    comparisons = 0
    for i in range(len(numbers) - 1):
        small = i
        for j in range(i+1, len(numbers)):
            comparisons = comparisons + 1
            if numbers[j] < numbers[small]:
                small = j

            temp = numbers[i]
            numbers[i] = numbers[small]
            numbers[small] = temp
    return comparisons
           

numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print('Unsorted list', numbers)

comparisons = selection_sort(numbers)

print('Sorted list', numbers)
print('There were %d total comparisons' % comparisons)