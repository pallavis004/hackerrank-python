def separateNumbers(s):
    n = len(s)
    for L in range(1, n // 2 + 1):
        if s[0] == '0':
            break
        num, pos = int(s[:L]), L
        while pos < n and s[pos:].startswith(str(num := num + 1)):
            pos += len(str(num))
        if pos == n:
            return print("YES", s[:L])
    print("NO")
if __name__ == "__main__":
    q = int(input()) 
    for _ in range(q):
        s = input().strip()
        separateNumbers(s)