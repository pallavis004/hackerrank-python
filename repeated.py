def repeatedString(s, n):
    full = n // len(s) * s.count('a')
    return full + s[:n % len(s)].count('a')
if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())
    print(repeatedString(s, n))