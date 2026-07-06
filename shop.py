def getMoneySpent(keyboards, drives, b):
    max_spent = -1
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b and total > max_spent:
                max_spent = total
    return max_spent
if __name__ == '__main__':
    b, n, m = map(int, input().split())
    keyboards = list(map(int, input().split()))
    drives = list(map(int, input().split()))
    print(getMoneySpent(keyboards, drives, b))