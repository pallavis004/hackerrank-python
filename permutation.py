def largestPermutation(k, arr):
    n = len(arr)
    position = {}
    for i in range(n):
        position[arr[i]] = i
    for i in range(n):
        if k == 0:
            break
        biggest = n - i
        if arr[i] != biggest:
            index = position[biggest]
            position[arr[i]] = index
            position[biggest] = i
            arr[i], arr[index] = arr[index], arr[i]
            k = k - 1
    return arr
n = int(input("Enter number of elements: "))
k = int(input("Enter maximum swaps: "))
arr = list(map(int, input("Enter array elements: ").split()))
result = largestPermutation(k, arr)
print("Largest Permutation:", *result)