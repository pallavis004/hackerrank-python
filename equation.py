def permutationEquation(p):
    n = len(p)
    q = [0] * (n + 1)
    for i, v in enumerate(p, 1):
        q[v] = i
    return [q[q[x]] for x in range(1, n + 1)]

if __name__ == '__main__':
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    for result in permutationEquation(p):
        print(result)