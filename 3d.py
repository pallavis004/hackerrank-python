def surfaceArea(A):
    H, W = len(A), len(A[0])
    area = 2 * H * W
    for i in range(H):
        for j in range(W):
            area += A[i][j] if i == 0 else abs(A[i][j] - A[i - 1][j])
            area += A[i][j] if i == H - 1 else 0
            area += A[i][j] if j == 0 else abs(A[i][j] - A[i][j - 1])
            area += A[i][j] if j == W - 1 else 0
    return area
if __name__ == "__main__":
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    print(surfaceArea(A))