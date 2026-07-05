def sockMerchant(n, ar):
    from collections import Counter
    counts = Counter(ar)
    return sum(c // 2 for c in counts.values())
if __name__ == "__main__":
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])) 