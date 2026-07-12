def flatlandSpaceStations(n, c):
    c = sorted(c)
    dist = max(c[0], n - 1 - c[-1])
    for i in range(1, len(c)):
        dist = max(dist, (c[i] - c[i - 1]) // 2)
    return dist
if __name__ == "__main__":
    n, m = map(int, input().split())
    c = list(map(int, input().split())) 
    print(flatlandSpaceStations(n, c))