def countSort(arr):
    buckets = [[] for _ in range(100)]
    for i, (x, s) in enumerate(arr):
        if i < len(arr) // 2:
            s = "-"
        buckets[int(x)].append(s)
    print(*sum(buckets, []))
if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        x, s = input().split()
        arr.append([x, s])
    countSort(arr)