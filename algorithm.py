def runningTime(arr):
    count = 0
    for i in range(1, len(arr)):
        number = arr[i]
        position = i - 1
        while position >= 0 and arr[position] > number:
            arr[position + 1] = arr[position]
            count = count + 1
            position = position - 1
        arr[position + 1] = number
    return count
arr = [2, 1, 3, 1, 2]
print(runningTime(arr))