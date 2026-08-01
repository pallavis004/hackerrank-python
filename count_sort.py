def countingSort(arr):
    count = [0] * 100
    for number in arr:
        count[number] = count[number] + 1
    return count
arr = [1, 1, 3, 2, 1]
answer = countingSort(arr)
print(answer)