def candies(n, arr):
    candies_given = []
    for i in range(n):
        candies_given.append(1)
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies_given[i] = candies_given[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            if candies_given[i] <= candies_given[i + 1]:
                candies_given[i] = candies_given[i + 1] + 1
    total_candies = 0
    for amount in candies_given:
        total_candies += amount
    return total_candies
n = int(input("Enter number of children: "))
arr = list(map(int, input("Enter ratings: ").split()))
result = candies(n, arr)
print("Total candies:", result)