def angryProfessor(k, a):
    return "NO" if sum(x <= 0 for x in a) >= k else "YES"
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().rstrip().split())
        a = list(map(int, input().rstrip().split()))
        print(angryProfessor(k, a))