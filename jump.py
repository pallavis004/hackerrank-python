def jumpingOnClouds(c):
    i, jumps = 0, 0
    while i < len(c) - 1:
        i += 2 if i + 2 < len(c) and c[i + 2] == 0 else 1
        jumps += 1
    return jumps
if __name__ == '__main__':
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    print(jumpingOnClouds(c))