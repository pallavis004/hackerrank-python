def jumpingOnClouds(c, k):
    n = len(c)
    e, i = 100, 0
    while True:
        i = (i + k) % n
        e -= 1 + 2 * c[i]
        if i == 0:
            break
    return e
if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    c = list(map(int, input().rstrip().split()))
    print(jumpingOnClouds(c, k))