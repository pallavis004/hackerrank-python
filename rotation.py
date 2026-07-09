def circularArrayRotation(a, k, queries):
    n = len(a)
    return [a[(i - k) % n] for i in queries]

if __name__ == '__main__':
    n, k, q = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    queries = [int(input().strip()) for _ in range(q)]
    for result in circularArrayRotation(a, k, queries):
        print(result)