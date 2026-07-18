import math
def squares(a, b):
    return math.isqrt(b) - math.isqrt(a - 1)
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        a, b = map(int, input().rstrip().split())
        print(squares(a, b))