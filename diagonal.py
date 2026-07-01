n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

left_to_right = 0
right_to_left = 0

for i in range(n):
    left_to_right += matrix[i][i]
    right_to_left += matrix[i][n-i-1]
print(abs(left_to_right - right_to_left))