def cutTheSticks(arr):
    result = []
    while arr:
        result.append(len(arr))
        m = min(arr)
        arr = [x - m for x in arr if x > m]
    return result
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    for result in cutTheSticks(arr):
        print(result)