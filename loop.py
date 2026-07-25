def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        position = i - 1
        current = numbers[i]
        while position >= 0 and numbers[position] > current:
            numbers[position + 1] = numbers[position]
            position = position - 1
        numbers[position + 1] = current
numbers = [2, 4, 6, 8, 3]
insertion_sort(numbers)
print(numbers)
