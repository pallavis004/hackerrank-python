def queensAttack(n, k, r_q, c_q, obstacles):
    obs = set(map(tuple, obstacles))
    count = 0
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
        r, c = r_q + dr, c_q + dc
        while 1 <= r <= n and 1 <= c <= n and (r, c) not in obs:
            count += 1
            r += dr
            c += dc
    return count
if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    r_q, c_q = map(int, input().rstrip().split())
    obstacles = [list(map(int, input().rstrip().split())) for _ in range(k)]
    print(queensAttack(n, k, r_q, c_q, obstacles))