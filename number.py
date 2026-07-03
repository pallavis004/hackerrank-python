def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    n = (x2 - x1) / (v1 - v2)
    return "YES" if n >= 0 and n == int(n) else "NO"


if __name__ == '__main__':
    x1, v1, x2, v2 = map(int, input().rstrip().split())
    print(kangaroo(x1, v1, x2, v2))