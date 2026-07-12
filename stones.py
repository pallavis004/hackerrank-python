def stones(n, a, b):
    return sorted({i * a + (n - 1 - i) * b for i in range(n)})
if __name__ == "__main__":
    t = int(input()) 
    for _ in range(t):
        n = int(input())
        a = int(input())
        b = int(input())
        result = stones(n, a, b)
        print(*result)