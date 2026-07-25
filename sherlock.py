def balancedSums(arr):
    for i in range(len(arr)):

        left_sum = sum(arr[:i])

        right_sum = sum(arr[i + 1:])

        if left_sum == right_sum:
            return "YES"

    return "NO"
arr = [1, 2, 3, 3]
print(balancedSums(arr))


