from collections import Counter
def beautifulTriplets(d, arr):
    c = Counter(arr)
    return sum(c[x] * c[x + d] * c[x + 2 * d] for x in set(arr))
if __name__ == "__main__":
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(beautifulTriplets(d, arr))