def serviceLane(n, cases):
    return [min(width[i:j+1]) for i, j in cases]
if __name__ == "__main__":
    n, t = map(int, input().split()) 
    width = list(map(int, input().split()))
    cases = []
    for _ in range(t):
        i, j = map(int, input().split())
        cases.append((i, j))
    result = serviceLane(n, cases)
    for ans in result:
        print(ans)