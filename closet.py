def closestNumbers(arr):
    arr.sort()
    min_diff = arr[1] - arr[0]  
    for i in range(len(arr) - 1):
        current_diff = arr[i + 1] - arr[i]
        if current_diff < min_diff:
            min_diff = current_diff
    result = []
    for i in range(len(arr) - 1):
        current_diff = arr[i + 1] - arr[i]
        if current_diff == min_diff:
            result.append(arr[i])
            result.append(arr[i + 1])
    return result
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    print(result)
