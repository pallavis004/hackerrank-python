def minimumAbsoluteDifference(arr):
    arr.sort()
    minimum = abs(arr[1] - arr[0])

    for i in range(1, len(arr)):
        difference = abs(arr[i] - arr[i - 1])
        if difference < minimum:
            minimum = difference
    return minimum
n = int(input("Enter size: "))
arr = list(map(int, input("Enter numbers: ").split()))
answer = minimumAbsoluteDifference(arr)
print("Minimum Absolute Difference:", answer)