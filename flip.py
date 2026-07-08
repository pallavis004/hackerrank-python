def flippingMatrix(matrix):
    n = len(matrix) // 2
    total = 0
    for i in range(n):
        for j in range(n):
            total += max(
                matrix[i][j],
                matrix[i][2*n-1-j],
                matrix[2*n-1-i][j],
                matrix[2*n-1-i][2*n-1-j]
            )
    return total
if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        n = int(input().strip())
        matrix = [list(map(int, input().rstrip().split())) for _ in range(2 * n)]
        print(flippingMatrix(matrix))
