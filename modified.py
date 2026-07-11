def kaprekarNumbers(p, q):
    res = []
    for n in range(p, q + 1):
        s = str(n * n)
        d = len(str(n))
        l, r = s[:-d] or "0", s[-d:]
        if int(l) + int(r) == n:
            res.append(n)
    print(*res) if res else print("INVALID RANGE")
if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)