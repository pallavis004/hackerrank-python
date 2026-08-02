def quickSort(arr):
    pivot = arr[0]
    left = []
    middle = []
    right = []
    for num in arr:

        if num < pivot:
            left.append(num)

        elif num > pivot:
            right.append(num)

        else:
            middle.append(num)

    return left + middle + right
arr = [4, 5, 3, 7, 2]
result = quickSort(arr)
print(result)