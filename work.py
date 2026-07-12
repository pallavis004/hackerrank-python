def workbook(n, k, arr):
    page = 1
    special = 0
    for problems in arr:
        for start in range(1, problems + 1, k):
            if page in range(start, min(start + k, problems + 1)):
                special += 1
            page += 1
    return special
if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(workbook(n, k, arr))