from collections import Counter
def nonDivisibleSubset(k, s):
    r = Counter(x % k for x in s)
    c = min(r[0], 1)
    for i in range(1, k // 2 + 1):
        c += min(r[i], 1) if i == k - i else max(r[i], r[k - i])
    return c
if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    s = list(map(int, input().rstrip().split()))
    print(nonDivisibleSubset(k, s))