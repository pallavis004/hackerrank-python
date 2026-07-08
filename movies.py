def beautifulDays(i, j, k):
    return sum(abs(x - int(str(x)[::-1])) % k == 0 for x in range(i, j + 1))
if __name__ == '__main__':
    i, j, k = map(int, input().rstrip().split())
    print(beautifulDays(i, j, k))
