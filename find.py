def findDigits(n):
    return sum(d != '0' and n % int(d) == 0 for d in str(n))

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(findDigits(n))