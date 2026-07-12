def chocolateFeast(n, c, m):
    bars = n // c
    total = bars
    wrappers = bars
    while wrappers >= m:
        new = wrappers // m
        total += new
        wrappers = wrappers % m + new
    return total
if __name__ == "__main__":
    t = int(input())  
    for _ in range(t):
        n, c, m = map(int, input().split())
        print(chocolateFeast(n, c, m))