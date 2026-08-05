def chessboardGame(x, y):
    if (x % 4 == 0 or x % 4 == 3) and (y % 4 == 0 or y % 4 == 3):
        return "Second"
    else:
        return "First"
x = int(input("Enter x: "))
y = int(input("Enter y: "))
answer = chessboardGame(x, y)
print("Winner:", answer)