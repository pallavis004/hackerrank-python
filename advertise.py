def viralAdvertising(n):
    shared, cumulative = 5, 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative
if __name__ == '__main__':
    n = int(input().strip())
    print(viralAdvertising(n))