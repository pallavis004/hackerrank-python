def minimumDistances(a):
    seen = {}
    best = -1
    for i, x in enumerate(a):
        if x in seen:
            d = i - seen[x]
            best = d if best == -1 else min(best, d)
        seen[x] = i
    return best
if __name__ == "__main__":
    n = int(input())                  
    a = list(map(int, input().split())) 
    print(minimumDistances(a))