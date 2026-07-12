def howManyGames(p, d, m, s):
    count = 0
    while s >= m:
        cost = max(p, m)
        if s < cost:
            break
        s -= cost
        p -= d
        count += 1
    return count
if __name__ == "__main__":
    p, d, m, s = map(int, input().split())
    print(howManyGames(p, d, m, s))