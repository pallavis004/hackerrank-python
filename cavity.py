def cavityMap(grid):
    n = len(grid)
    g = [list(row) for row in grid]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            d = grid[i][j]
            if all(d > grid[i + di][j + dj] for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                g[i][j] = 'X'
    return ["".join(row) for row in g]
if __name__ == "__main__":
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    result = cavityMap(grid)
    for row in result:
        print(row)