def pickingNumbers(a):
    max_len = 0
    for i in range(1, 100):
        count = a.count(i) + a.count(i + 1)
        if count > max_len:
            max_len = count
    return max_len
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().split()))
    print(pickingNumbers(a))