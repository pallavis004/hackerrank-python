def countingSort(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1
    ans = []
    for i in range(100):
        for k in range(count[i]):
            ans.append(i)
    return ans
arr = [4, 3, 2, 1, 3, 4, 3, 0]
result = countingSort(arr)
print(result)