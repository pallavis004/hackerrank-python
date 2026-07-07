def hurdleRace(k, height):
    tallest = max(height)
    if tallest > k:
        return tallest - k
    else:
        return 0
if __name__ == '__main__':
    n, k = map(int, input().split())
    height = list(map(int, input().split()))
    print(hurdleRace(k, height))