def findMedian(arr):
    arr.sort()
    size = len(arr)
    middle = size // 2
    median = arr[middle]
    return median
arr = [5, 3, 1, 2, 4]
print(findMedian(arr))